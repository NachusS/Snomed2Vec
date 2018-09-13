# Snomed2Vec
New approach to use Snomed-CT Concept using *Word Embedding* with **Word2vec**, A new approach **Clinica Semantic Tag**, NER(Named Entity Recognition).

## Introduction
**Snomed2Vec** is a framework to identify clinical concept from clinical text report o with simple sentences. 
We can test a diagnostic, procedure, sustances, until 19 classes (hierachy) of clinical concepts of Snomed-CT.

To identify de clinical concept we use the clinical Ontology **Snomed-CT** to get the **unique ConceptID** and it hierarchy, that define the class the concept belong. To get the semantic relation from the word of the text, we use the space vector model **"Word Embedding"** Word2Vec.


## Prerequisites
We use Python library gensim, for Word2Vec model.

## Ontology Snomed-CT Processing 
The first step is prepare the Snomed-CT structure to apply the model and the tool.
  
### Word Embedding. Train the model with "Word2Vec".

A word embedding is a distributed (dense) vector representation for each word of a text. It is capable of capturing semantic and syntactic properties of the input texts.  

*Word2Vec* from Mikolov et al. (2013) develop to kind of models:

-   Skip-Gram Negative Sampling.
-   CBoW Continue Bag of Words.
There are other approach like:
-   Global Word Vectors by Pennington, Socher, and Manning (2014) (GloVe)
-   FastText (Facebook)

Skip-gram negative sampling (or Word2Vec) is an algorithm based on a shallow neural network which aims to learn a word embedding. It is highly efficient, as it avoids dense matrix multiplication and does not require the full term co-occurrence matrix. Given some target word *w*<sub>*t*</sub>, the intermediate goal is to train the neural network to predict the words in the *c*-neighbourhood of *w*<sub>*t*</sub>: *w*<sub>*t* − *c*</sub>, …, *w*<sub>*t* − 1</sub>, *w*<sub>*t* + 1</sub>, …, *w*<sub>*t* + *c*</sub>.

First, the word is directly associated to its respective vector, which as used as input for a (multinomial) logistic regression to predict the words in the *c*-neighbourhood. Then, the weights for the logistic regression are adjusted,
as well as the vector itself (by back-propagation). The Word2Vec algorithm employs negative sampling: additional *k* noise words which do not appear in the *c*-neighbourhood are introduced as possible outputs, for which the desired output is known to be `false`. Thus, the model does not reduce the weights to all other vocabulary words but only to those sampled *k* noise words. When
these noise words appear in a similar context as *w*<sub>*t*</sub>, the model gets more and more fine-grained over the training epochs. 

In contrast to Word2Vec, the GloVe (Pennington, Socher, and Manning 2014) algorithm computes the whole term co-occurrence matrix for a given corpus. To obtain word vectors, the term co-occurrence matrix is factorised. The training objective is that the euclidean dot product of each two word vectors match the log-probability of their words’ co-occurrence.

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

## Final notes:
This documentation is part of my PH.D.Thesis and share to improve this new approach.
For any comments or help needed with how to test *Snomed2Vec* tool, you can write to: ignacio.martinez@carm.es
