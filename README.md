# Lab 04: Fine-Tuning Language Models with QLoRA

## Overview

This lab explored how to fine-tune a pre-trained Large Language Model (LLM), utilising both QLoRA and Supervised Fine Tuning.

I used the Qwen/Qwen2.5-0.5B-Instruct model and fine-tuned it to provide a ‘computer shop’ customer service model. The computer shop is situated in Homagama, Sri Lanka.

The objective was to explore how a pre-trained language model can be fine-tuned so that it can respond to questions within a defined area of expertise, by using an original bespoke dataset.


## Lab Objectives

- To comprehend the fundamentals of fine-tuning.
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

I installed the relevant libraries, and verified that a GPU was available in my Google Colab environment.

A GPU was used to both speed-up and effectively manage the fine-tuning and training of a model.

- **GPU:** NVIDIA Tesla T4
- **Total VRAM:** 14.56 GB

### 2. Model and Tokenizer Initialization

For this activity, I selected the `Qwen/Qwen2.5-0.5B-Instruct` model.

Furthermore, I also loaded and set up the associated model tokeniser. The end of sequence (EOS) token was designated as the padding token and right-padding was activated.

### 3. Custom Dataset Creation

I created a custom dataset containing **30 question-and-answer pairs** based on a local computer shop.

I developed a bespoke dataset, which contained 30 question and answer pairs relating to a local computer shop.

- Computer hardware and accessories
- Laptop and PC repair services
- Gaming PCs and components
- Pricing and payment methods
- Warranty and return policies
- Store location and opening hours
- Technical support and maintenance

Each query and answer pair was structured as follows:

```text
### Instruction:
{question}

### Response:
{answer}
```

The formatted dataset was then converted into a Hugging Face Dataset object for training.

### 4. QLoRA Configuration

QLoRA was set-up so that I could fine-tune my model and simultaneously decrease the GPU’s memory usage.

4-bit quantisation (using the ‘NF4’ quantisation method) was applied and calculations were conducted in FP16 format.


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

Having set-up my QLoRA and LoRA settings, I conducted supervised fine-tuning by using the ‘SFTTrainer’ class from the TRL library.

The main training configurations were:

| Parameter | Value |
|---|---|
| Batch Size | 2 |
| Gradient Accumulation Steps | 4 |
| Learning Rate | 2e-4 |
| Training Epochs | 3 |
| Optimizer | paged_adamw_8bit |
| Maximum Sequence Length | 512 |

Training of my model was then carried out using my bespoke computer shop dataset.

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

I have therefore practically explored how to fine-tune a pre-trained language model by using both QLoRA and supervised fine-tuning.

I ascertained how 4-bit quantisation and LoRA can be used to lessen the computational needs of model training. In addition, I analysed how a bespoke dataset can be used to specialise an already existing language model.

Ultimately, my analysis of the base and fine-tuned models enabled me to investigate how effective fine-tuning can be in specialising a model’s ability to answer queries in a defined area of expertise.
