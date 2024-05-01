# Raise-your-Voice
Repository to Svenja Guhr's Dissertation <br/><br/>
This repository contains: 

## Corpus and annotated corpus texts:
- Plain text corpus as TXT files (UTF-8) [https://github.com/SvenjaGuhr/ link]
- Plain text corpus as XML files [https://github.com/SvenjaGuhr/  link]
- Manually annotated training data as XML files with sound word annotations [https://github.com/SvenjaGuhr/ link]
- Manually annotated training data as XML files with sound event annotations [https://github.com/SvenjaGuhr/ link]
- Manually annotated test set with 10 XML files with sound event annotations [https://github.com/SvenjaGuhr/ link]
- Manually sound word-annotated XML file of M. v. Ebner-Eschenbach's _Die Resel_ [https://github.com/SvenjaGuhr/ link]
- Manually sound event-annotated XML file of M. v. Ebner-Eschenbach's _Die Resel_ [https://github.com/SvenjaGuhr/ link]
- XML files with automatically sound-annotated corpus texts with sound event annotation [https://github.com/SvenjaGuhr/ link]
- XML files automatically sound event-annotated and semi-automatically enriched with loudness levels [https://github.com/SvenjaGuhr/ link]

## Models:
- Trained NEISS NTEE Models for automated sound word and sound event annotation: 
The models can be regenerated using the indicated training data [https://github.com/SvenjaGuhr/ link]. The models will be uploaded on Zenodo after the publication of my dissertation.
For more information see NEISS NTEE's wiki (TEI Entity Enricher) [https://github.com/NEISSproject/tei_entity_enricher].
- Model trained on 20 manually sound word-annotated corpus texts
- Model trained on 55 manually sound event-annotated corpus texts

## Jupyter Notebooks:
- Preprocessing of plain text files as preparation for the manual sound word annotation in CSV [https://github.com/SvenjaGuhr/ link]
- Preprocessing of plain text files as preparation for the automated sound annotation in XML [https://github.com/SvenjaGuhr/ link]
- Preprocessing of the corpus for generating metadata (i.a. token and word count) [https://github.com/SvenjaGuhr/Raise-your-Voice/edit/main/README.md#:~:text=diss_corpus_preprocessing_and_word_count]
- Metadata generation: Corpus Keyword Search and Extraction [Link](https://github.com/SvenjaGuhr/Raise-your-Voice/blob/main/Corpus_Keyword_Search_and_Extraction.ipynb)
- Evaluation of inter-annotator agreement with Krippendorff's _alpha_ [Krippendorff 2018](https://github.com/pln-fing-udelar/fast-krippendorff) and _gamma_ by Mathet et al. (2015) using the [python package _pygamma-agreement_](https://pygamma-agreement.readthedocs.io/_/downloads/en/latest/pdf/) [Link to notebooks](https://github.com/SvenjaGuhr/Raise-your-Voice/tree/main/IAA_manual_annotation)
- Postprocessing the sound annotations for extracting the annotations from XML to CSV [Link](https://github.com/SvenjaGuhr/Raise-your-Voice/tree/main/Diss_extraction_of_annotations)
- Postprocessing the sound annotations through automated revision of the XML annotations [https://github.com/SvenjaGuhr/ link]
- Postprocessing of the manually annotated XML files through the extraction of sound event and loudness annotations for their analysis as data frames [Link](https://github.com/SvenjaGuhr/Raise-your-Voice/tree/main/Diss_extraction_of_annotations)
- Loudness annotation with dictionary approach [https://github.com/SvenjaGuhr/ link]

## Dataframes:
- Corpus metadata table as [CSV](https://github.com/SvenjaGuhr/Raise-your-Voice/blob/main/20240501_theme-d-Prose_Metadaten.csv)
- Dataframes with mapped manual annotations of sound events and loudness of T. Fontane's _Effi Briest_ and G. Reuter's _Aus guter Familie_ [https://github.com/SvenjaGuhr/  link]

## Annotation Guidelines:
- Guidelines for sound word and sound event annotation [Link](https://github.com/SvenjaGuhr/Raise-your-Voice/blob/main/Guidelines%20for%20Sound%20Annotation.md)

## License:
- Information on the GPL license 
