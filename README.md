# Snomed2Vec
New approach to use Snomed-CT Concept using *Word Embedding* with **Word2vec**, A new approach **Clinica Semantic Tag**, NER(Named Entity Recognition).

## Introduction
**Snomed2Vec** is a framework to identify clinical concept from clinical text report o with simple sentences. We can test a diagnostic, procedure, sustances, etc...

To identify de clinical concept we use the clinical Ontology **Snomed-CT** to get the **unique ConceptID** and it hierarchy that define the class the concept belong. To get the semantic relation from the word of the text, we use the space vector model **Word Embedding"** Word2Vec.
This documentation is part of my PH.D.Thesis and share to improve this new approach.

## Prerequisites
We use Python library gensim, for Word2Vec model.

## Ontology Snomed-CT Processing 
The first step is prepare the Snomed-CT structure to apply the model and the tool.
  
## Word Embedding. Train the model "Word2Vec".

## Methods 

  
## Representation Learning
I create some jupyter notebook to test the framewotk
Prueba
  ```
  python Snomed2Vec.py *"sentence test"*
  ```
  This script get the SNomed-CT Clinical concept from a free text sentence. 

## Data sources, Space vector Models:
** Corpus Gold:**

## Final notes
For any comments or help needed with how to test *Snomed2Vec* tool, you can write to: ignacio.martinez@carm.es
