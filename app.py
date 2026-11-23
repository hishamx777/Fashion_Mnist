import numpy as np
import streamlit as st
from PIL import Image, ImageOps
from tensorflow import keras

class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
               "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

# Must be identical to preprocess() in the notebook
def preprocess(img, invert=False):
    img = ImageOps.pad(img.convert("L"), (28, 28), color=0)
    if invert:
        img = ImageOps.invert(img)
    return np.array(img, dtype="float32").reshape(1, 28, 28, 1) / 255.0

@st.cache_resource
def load():
    return keras.models.load_model("fashion_cnn.keras")

model = load()

st.title("Fashion-MNIST Classifier")
st.caption("A small CNN trained on 28x28 grayscale clothing images (~88% test accuracy).")

file = st.file_uploader("Upload a clothing image", type=["png", "jpg", "jpeg"])
invert = st.checkbox("Invert colors (dark item on a white background)")

if file:
    img = Image.open(file)
    st.image(img, width=200)
    probs = model.predict(preprocess(img, invert), verbose=0)[0]
    st.subheader(f"{class_names[probs.argmax()]}  ({probs.max():.0%})")
    for c, p in zip(class_names, probs):
        st.progress(float(p), text=f"{c}: {p:.1%}")

st.info("The model was trained on centered, light-on-dark product images. "
        "Photos with busy backgrounds will be classified poorly.")
