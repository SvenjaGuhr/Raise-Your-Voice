# Raise-your-Voice
Repository to Svenja Guhr's Dissertation <br/><br/>
This repository contains: 

## Corpus and annotated corpus texts:
- Plain text corpus as TXT files (UTF-8) 
- Plain text corpus as XML files
- Manually annotated training data as XML files with sound word annotations 
- Manually annotated training data as XML files with sound event annotations 
- Manually annotated test set with 10 XML files with sound event annotations 
- Manually sound word-annotated XML file of M. v. Ebner-Eschenbach's _Die Resel_ 
- Manually sound event-annotated XML file of M. v. Ebner-Eschenbach's _Die Resel_ 
- XML files with automatically sound-annotated corpus texts with sound event annotation 
- XML files automatically sound event-annotated and semi-automatically enriched with loudness levels 

## Models:
- Trained NEISS NTEE Models for automated sound word and sound event annotation: 
The models can be regenerated using the indicated training data [https://github.com/SvenjaGuhr/ link]. The models will be uploaded on Zenodo after the publication of my dissertation.
For more information see NEISS NTEE's wiki (TEI Entity Enricher) [https://github.com/NEISSproject/tei_entity_enricher].
- Model trained on 20 manually sound word-annotated corpus texts
- Model trained on 55 manually sound event-annotated corpus texts

## Jupyter Notebooks:
### Preprocessing of the texts
- Preprocessing of plain text files as preparation for the manual sound word annotation in CSV [Link][[https://github.com/SvenjaGuhr/ link](https://github.com/SvenjaGuhr/Raise-your-Voice/blob/main/tidy_Text-preprocessing_German_spacy.ipynb)]
- Preprocessing of plain text files as preparation for the automated sound annotation in XML [Link][[https://github.com/SvenjaGuhr/ link](https://github.com/SvenjaGuhr/Raise-your-Voice/blob/main/20240430_text_preprocessing_for_XML_preparation.ipynb)]
  
### Preprocessing of the corpus metadata 
- Preprocessing of the corpus for generating metadata (i.a. token and word count) [Link](https://github.com/SvenjaGuhr/Raise-your-Voice/blob/main/diss_corpus_preprocessing_word_count_sentence_split_lemmatization_Word2Vec_model.ipynb)
- Metadata generation: Corpus Keyword Search and Extraction [Link](https://github.com/SvenjaGuhr/Raise-your-Voice/blob/main/Corpus_Keyword_Search_and_Extraction.ipynb)

### Evaluationg if inter-annotator agreement
- Evaluation of inter-annotator agreement with Krippendorff's _alpha_ [Krippendorff 2018](https://github.com/pln-fing-udelar/fast-krippendorff) and _gamma_ by Mathet et al. (2015) using the [python package _pygamma-agreement_](https://pygamma-agreement.readthedocs.io/_/downloads/en/latest/pdf/) [Link](https://github.com/SvenjaGuhr/Raise-your-Voice/tree/main/IAA_manual_annotation)

### Postprocessing of the annotated corpus texts
- One script providing the entire process from automated annotation revision, annotation extraction to automated loudness level labeling via the dictionary approach [Linkl[https://github.com/SvenjaGuhr/Raise-your-Voice/blob/main/20240509_loudness_level_labeling_tidy.ipynb]
-- Postprocessing the sound annotations for extracting the annotations from XML to CSV [Link](https://github.com/SvenjaGuhr/Raise-your-Voice/tree/main/Diss_extraction_of_annotations)
-- Postprocessing the sound annotations through automated revision of the XML annotations [Link](https://github.com/SvenjaGuhr/Raise-your-Voice/blob/main/Diss_extraction_of_annotations/auto_revise_annotations.ipynb)
-- Loudness annotation with dictionary approach [Link](https://github.com/SvenjaGuhr/Raise-your-Voice/blob/main/Diss_extraction_of_annotations/20240509_loudness_level_labeling.ipynb)

## Building the Word2Vec Model
- 

## Dataframes:
- Corpus metadata table as [CSV](https://github.com/SvenjaGuhr/Raise-your-Voice/blob/main/20240503_theme-d-Prose_Metadaten.csv)

## Annotation Guidelines:
- Guidelines for sound word and sound event annotation [Link](https://github.com/SvenjaGuhr/Raise-your-Voice/blob/main/Guidelines%20for%20Sound%20Annotation.md)

## License:
- Information on the GPL license 
