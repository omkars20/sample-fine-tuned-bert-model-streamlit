# BERT Fine-Tuned Sentiment Analysis

This project demonstrates a sentiment analysis app using a fine-tuned BERT model. The model is deployed on [Streamlit](https://streamlit.io/) and hosted at:  
[Sentiment Analysis App](https://sentiment-analysis-bert-bert.streamlit.app/)

## Overview

The app performs **sentiment analysis** on input text, classifying the sentiment as **positive** or **negative**. It uses a BERT model fine-tuned on movie reviews to provide accurate sentiment predictions.

## Features

- **Input:** The user can input any text (such as movie reviews).
- **Prediction:** The model will classify the text sentiment as either positive or negative.
- **Model:** A BERT model fine-tuned on a sentiment analysis task is used, with the model hosted on Hugging Face.

## How to Run Locally

To run this app on your local machine, follow these steps:

1. Clone the repository

```bash
git clone https://github.com/omkars20/sample-fine-tuned-bert-model-streamlit.git
cd sample-fine-tuned-bert-model-streamlit
2. Create and activate a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

3. Install the dependencies

pip install -r requirements.txt

streamlit run app.py

Model Details
The model is a BERT model fine-tuned for sentiment classification. It has been uploaded to Hugging Face Model Hub and is loaded in the app using the transformers library.


Deployment
The app is deployed on Streamlit Cloud and can be accessed via the following link:

https://sentiment-analysis-bert-bert.streamlit.app/


