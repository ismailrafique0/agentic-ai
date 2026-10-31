# Week 03 - NLP & Machine Learning Labs

This repository contains all lab exercises for Week 03 covering:
- Text classification with Naive Bayes
- Text cleaning and preprocessing
- Tokenization (BERT, GPT-2, SentencePiece, BPE concepts)
- ML pipelines for text classification
- Sentence embeddings and semantic similarity
- Semantic search/RAG basics

## Structure

- `phase01/` - Sentiment classification with CountVectorizer & Naive Bayes
- `phase02/` - Text cleaning with regex
- `phase03/` - Tokenization techniques and custom tokenizers
- `phase04/` - Text classification with TF-IDF pipelines
- `phase05/` - Sentence embeddings and semantic similarity
- `phase06/` - Semantic search implementation
- `evidence/` - Lab outputs and evidence

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install scikit-learn transformers sentence-transformers sentencepiece pandas numpy
```

## Running Examples

```bash
python phase01/sentiment_classifier.py
python phase02/text_cleaning.py
python phase05/semantic_similarity.py
python phase06/semantic_search.py
```
