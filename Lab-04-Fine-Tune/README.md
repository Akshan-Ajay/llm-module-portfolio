# Lab 04: Fine-Tuning Language Models with QLoRA

## Overview

This laboratory focuses on fine-tuning a pre-trained Large Language Model (LLM) using **QLoRA (Quantized Low-Rank Adaptation)** and Supervised Fine-Tuning (SFT).

For this lab, I used the `Qwen/Qwen2.5-0.5B-Instruct` model and fine-tuned it to work as a customer service assistant for a computer shop located in Homagama, Sri Lanka.

The main purpose of this activity was to understand how a pre-trained language model can be adapted to answer questions related to a specific domain using a custom dataset.

## Lab Objectives

- Understand the basic concept of fine-tuning a pre-trained language model.
- Set up a GPU environment using Google Colab.
- Create a custom dataset containing 30 question-and-answer pairs related to a computer shop.
- Apply 4-bit quantization and QLoRA to reduce GPU memory usage during training.
- Use LoRA and PEFT techniques for efficient model fine-tuning.
- Compare the responses of the original model with the fine-tuned model.
- Evaluate how fine-tuning improves the model's responses to domain-specific questions.

## Tools and Technologies

The following tools and libraries were used in this laboratory:

- Python
- Google Colab
- PyTorch
- Hugging Face Transformers
- Hugging Face Datasets
- PEFT
- TRL
- BitsAndBytes
- Qwen 2.5 (0.5B Instruct)

## Requirements and Installation

The following libraries were installed before starting the implementation.

```bash
pip install -q transformers datasets peft trl accelerate bitsandbytes
```

## Laboratory Implementation

### 1. Environment Setup and GPU Verification

First, I installed the required libraries and checked whether a GPU was available in Google Colab.

The GPU environment was used to make the fine-tuning process faster and to handle the model training efficiently.

- **GPU:** NVIDIA Tesla T4
- **Total VRAM:** 14.56 GB

### 2. Model and Tokenizer Initialization

For this activity, I selected the `Qwen/Qwen2.5-0.5B-Instruct` model.

The tokenizer was also loaded using Hugging Face Transformers. The EOS token was configured as the padding token, and right-side padding was enabled.

### 3. Custom Dataset Creation

I created a custom dataset containing **30 question-and-answer pairs** based on a local computer shop.

The dataset covers different topics, including:

- Computer hardware and accessories
- Laptop and PC repair services
- Gaming PCs and components
- Pricing and payment methods
- Warranty and return policies
- Store location and opening hours
- Technical support and maintenance

Each question and answer was formatted using the following instruction template:

```text
### Instruction:
{question}

### Response:
{answer}
```

The formatted dataset was then converted into a Hugging Face Dataset object for training.

### 4. QLoRA Configuration

In this step, I configured QLoRA to fine-tune the model while reducing GPU memory requirements.

The model was loaded using 4-bit quantization with the NF4 quantization type and FP16 computation.

The main configurations were:

**Quantization Settings**
- Load in 4-bit: Enabled
- Quantization type: NF4
- Compute data type: Float16
- Double quantization: Enabled

**LoRA Settings**

| Parameter | Value |
|---|---|
| Rank (r) | 16 |
| Alpha | 32 |
| Dropout | 0.05 |
| Bias | None |
| Task Type | CAUSAL_LM |

The following model modules were selected as LoRA target modules:

- `q_proj`
- `k_proj`
- `v_proj`
- `o_proj`
- `gate_proj`
- `up_proj`
- `down_proj`

### 5. Model Training

After configuring QLoRA and LoRA, I used `SFTTrainer` from the TRL library to perform supervised fine-tuning.

The main training configurations were:

| Parameter | Value |
|---|---|
| Batch Size | 2 |
| Gradient Accumulation Steps | 4 |
| Learning Rate | 2e-4 |
| Training Epochs | 3 |
| Optimizer | paged_adamw_8bit |
| Maximum Sequence Length | 512 |

The model was trained using the custom computer shop dataset.

### 6. Model Evaluation

After completing the fine-tuning process, I compared the original base model with the fine-tuned model.

I used three test questions, including one question from the training dataset and two questions that were not included in the training dataset.

The purpose was to observe how the model's responses changed after fine-tuning.

**Evaluation Results**

| Test Question | Base Model | Fine-Tuned Model |
|---|---|---|
| What are your store opening hours? (Seen) | Provided a generic response and stated that it did not have access to real-time store information. | Provided a response based on the computer shop's information, including its opening hours. |
| Do you repair liquid-damaged mechanical keyboards? (Unseen) | Generated a generic DIY repair guide. | Provided a direct answer about available repair or replacement services. |
| Do you sell custom water cooling loops? (Unseen) | Generated a generic explanation about cooling systems. | Provided a relevant answer about liquid cooling products. |

### Observations

From the evaluation, I observed that:

- The original model mainly provided general-purpose responses.
- The fine-tuned model was more focused on the computer shop domain.
- The fine-tuned model provided more relevant answers to the questions.
- The model was able to respond to questions that were not directly included in the training dataset.

Overall, this activity helped me understand how fine-tuning can adapt a pre-trained language model to a particular domain using a relatively small custom dataset.

## Repository Structure

```text
Lab-04-Fine-Tune/
│
├── README.md
│
├── notebooks/
│   └── lab04_fine_tune.ipynb
│
└── screenshots/
    ├── gpu_status.png
    ├── dataset_creation.png
    ├── training_progress.png
    └── model_evaluation.png
```

## Conclusion

Through this laboratory activity, I gained practical experience in fine-tuning a pre-trained language model using QLoRA and supervised fine-tuning.

I learned how 4-bit quantization and LoRA can help reduce the computational requirements of model training. I also understood how a custom dataset can be used to adapt an existing language model to a specific domain.

Finally, comparing the base model and the fine-tuned model helped me understand the impact of fine-tuning on domain-specific question answering.