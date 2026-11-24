# Fashion MNIST Classification using CNN

## Project Overview

This project demonstrates how to build and train a Convolutional Neural Network (CNN) to classify images from the Fashion MNIST dataset. Fashion MNIST contains 70,000 grayscale images of 28x28 pixels, divided into 10 categories of clothing items such as T-shirts, trousers, sneakers, and more.

The goal is to leverage CNNs’ ability to extract spatial features from images to accurately classify these clothing items.

---

## Libraries Used

To solve Arabic issues in visualization, the following libraries were utilized:

- `arabic_reshaper`
- `python_bidi`

---

## Results

- Achieved approximately **88% accuracy** on the test dataset.
- Performed predictions on sample images with impressive accuracy and visualization.

---

## Links

| | Link |
|---|---|
| Live demo (Streamlit) | add your Streamlit app URL |
| Model (Hugging Face) | add https://huggingface.co/<user>/fashion-mnist-cnn |
| Notebook | [`Fashion_Mnist.ipynb`](Fashion_Mnist.ipynb) |

## 💬 Feedback and Collaboration

Feel free to connect with me on  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](www.linkedin.com/in/hishammislhy)
for feedback or potential collaboration!

---
This project is part of my continuous journey in the field of AI and machine learning. I’m excited to keep exploring real-world applications that create business impact!

---

## Run it

```bash
pip install -r requirements.txt
streamlit run app.py
```

`app.py` expects `fashion_cnn.keras` and `requirements.txt`, which the notebook produces (section 5).

## Repo layout

```
Fashion_Mnist.ipynb   data, model, evaluation, publish to Hugging Face, Gradio demo
app.py                Streamlit demo
fashion_cnn.keras     trained model (produced by the notebook)
requirements.txt      pinned to the TensorFlow version used for training
model_card.md         model card published on the Hugging Face Hub
```
