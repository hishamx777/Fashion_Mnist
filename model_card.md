---
datasets:
  - zalando-datasets/fashion_mnist
metrics:
  - accuracy
pipeline_tag: image-classification
library_name: keras
---

# fashion-mnist-cnn

Small CNN (3 Conv2D blocks + Dense head, Dropout) trained on Fashion-MNIST, 10 clothing classes.

## Results
About 88% accuracy on the 10,000-image Fashion-MNIST test set.

## Usage
```python
from huggingface_hub import hf_hub_download
from tensorflow import keras

model = keras.models.load_model(hf_hub_download("<user>/fashion-mnist-cnn", "fashion_cnn.keras"))
```
Input: `(1, 28, 28, 1)` float array scaled to [0, 1]. Resize/pad to 28x28 grayscale, light item on a dark background.

## Limitations
- Trained on centered 28x28 studio-style product images. Photos with backgrounds or other framing are out of distribution.
- Not intended for production use.
