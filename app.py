import streamlit as st
from transformers import BertForSequenceClassification, BertTokenizer
import torch  # Ensure PyTorch is imported

# Load model and tokenizer from Hugging Face Model Hub
model = BertForSequenceClassification.from_pretrained("omkars20/bert-fine-tuned-streamlit")
tokenizer = BertTokenizer.from_pretrained("omkars20/bert-fine-tuned-streamlit")

# Streamlit app
st.title("Sentiment Analysis with BERT")
text = st.text_area("Enter text for sentiment analysis:")

if st.button("Predict"):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()

    st.write("Prediction:", "Positive" if predicted_class == 1 else "Negative")


