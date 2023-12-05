# DeFlicker PRISM
 Samsung PRISM project: removing flickering in high fps videos


Process: 

1. Synthetic data generation: using flawed atlas paper's ready model on their flickering dataset to obtain and unflickered dataset.
2. Fully convolutional LSTMs: using supervised learning (owing to the presence of paired data), with a 2 layered same convolutions
