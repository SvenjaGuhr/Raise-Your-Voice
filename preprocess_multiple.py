#All credits to Henny Sluyter-Gäthje, who provided me with this short script for running multiple texts through Hans Ole Hatzel's Event Segmentation 
#Hans Ole Hatzle (2022): Event Segmentation, https://github.com/uhh-lt/event-classification.

import os
import sys
from pathlib import Path 

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"usage {sys.argv[0]} path/to/input/dir path/to/output/dir")
        exit(-1)
    input_dir = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])

    for fp in input_dir.iterdir():
        print(f"processing {fp.name}")
        if fp.is_file():
            output_fp = output_dir / fp.name.replace("txt", "json")

            os.system(f'python preprocess.py preprocess --parser=spacy {fp} {output_fp}')
