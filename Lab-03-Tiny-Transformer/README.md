# PUSL 3205 – Large Language Models and Generative AI

## Lab 03: Building a Tiny Transformer

### 1. Introduction

In this laboratory activity, I built a small decoder-only Transformer language model using PyTorch. The model was trained on the TinyStories dataset to learn character patterns and generate simple stories from a starting prompt.

### 2. Dataset

- **Dataset:** TinyStories
- **Source:** Hugging Face – `roneneldan/TinyStories`
- **Dataset used:** 5,000 stories selected from the training split
- **Tokenization:** Character-level tokenization
- **Vocabulary size:** 90 unique characters
- **Total tokens:** 4,176,740

The text data was combined into one corpus and converted into numerical values using character-to-integer mappings.

### 3. Data Preparation

The dataset was divided into two parts:

- Training data: 90%
- Validation data: 10%

The following settings were used to prepare the training batches:

- Block size: 128
- Batch size: 64

The model used previous characters to learn and predict the next character in a sequence.

### 4. Transformer Model

A small decoder-only Transformer model was implemented using PyTorch.

The model includes:

- Character embeddings
- Positional embeddings
- Self-attention
- Multi-head attention
- Feed-forward neural networks
- Causal masking
- Dropout
- Linear output layer

### 5. Model Training

The model was trained using the AdamW optimizer.

| Parameter | Value |
|---|---:|
| Embedding size | 128 |
| Attention heads | 4 |
| Transformer layers | 4 |
| Dropout | 0.1 |
| Learning rate | 0.0003 |
| Training iterations | 1,500 |
| Evaluation interval | 250 |
| Model parameters | Approximately 0.83 million |

Training and validation loss were recorded during training to observe how the model learned.

### 6. Model Evaluation

The model was evaluated using validation loss and perplexity.

| Metric | Result |
|---|---:|
| Final validation loss | 1.5412 |
| Perplexity | 4.6700 |

A training and validation loss graph was also created to observe the model's performance during training.

### 7. Text Generation

After training, the model was tested by providing the starting prompt:

`Once upon a time`

The model generated a story by predicting one character at a time.

The generated text was also tested with different generation settings, including the maximum number of tokens and temperature.

### 8. Model Saving

The trained model parameters and configuration were saved in:

`tiny_transformer_model.pt`

The saved checkpoint includes the model state, vocabulary information, and model configuration.

### 9. Gradio Interface

A simple Gradio interface was created to allow users to generate stories.

The interface includes:

- Starting prompt
- Maximum number of tokens
- Temperature

Users can enter a prompt and generate text using the trained Tiny Transformer model.

### 10. Conclusion

In this laboratory activity, I learned how to prepare text data using character-level tokenization, build a decoder-only Transformer model, train the model using PyTorch, and evaluate its performance using validation loss and perplexity.

I also learned how to generate text using a trained model, save model parameters, and create a simple Gradio interface for text generation.