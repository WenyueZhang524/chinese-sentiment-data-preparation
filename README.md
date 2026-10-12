# Chinese Sentiment Analysis — Data Preparation

## Project Overview

This repository contains the data preparation component of a Chinese text sentiment analysis project developed as part of an undergraduate dissertation.

The script transforms labelled Chinese text data into an instruction-based format suitable for language model fine-tuning and divides the processed data into training and validation sets.

**Scope:** This repository currently contains data preprocessing code only. It does not include the complete language model training pipeline or reproduce the fine-tuning results discussed in the dissertation.

## Project Objectives

- Prepare Chinese text data for sentiment classification.
- Convert labelled text samples into structured instruction-response records.
- Support five sentiment categories.
- Generate reproducible training and validation splits.

## Sentiment Categories

| Original Label | Chinese Label | English Meaning |
| --- | --- | --- |
| sadness | 伤心 | Sadness |
| happiness | 开心 | Happiness |
| anger | 生气 | Anger |
| fear | 害怕 | Fear |
| disgust | 厌恶 | Disgust |

## Technologies Used

- Python
- pandas
- scikit-learn
- openpyxl (for reading Excel files)

## Data Processing Workflow

1. Read labelled text samples from `data.xlsx` using pandas.
2. Extract the `content` and `label` columns.
3. Map English sentiment labels to their corresponding Chinese categories.
4. Convert each sample into an instruction-based record containing `instruction`, `input`, and `output` fields.
5. Split the processed records into training (90%) and validation (10%) datasets using `random_state=42`.
6. Export the results as UTF-8 JSON files named `train.json` and `val.json`.

## Example Output Format

The following is an illustrative example, not a sample from the original dataset.

```json
{
  "instruction": "您是一位情感分析师，请根据我提供的<句子>,输出对应的情感类别:伤心,开心,害怕,生气,厌恶",
  "input": "<句子>今天我很开心。",
  "output": "开心"
}
```

## Repository Structure

```text
chinese-sentiment-data-preparation/
├── prepare_dataset.py
├── README.md
└── requirements.txt
```

The source dataset and generated JSON files are not included in this public repository.

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Prepare the input data

Place a file named `data.xlsx` in the project directory.

The Excel file must contain:
- `content`: Chinese text samples
- `label`: one of `sadness`, `happiness`, `anger`, `fear`, or `disgust`

### 3. Run the preprocessing script

```bash
python prepare_dataset.py
```

### 4. Generated files

The script creates:
- `train.json` — 90% of the processed samples
- `val.json` — 10% of the processed samples

The script requires a compatible input dataset to run. The original dataset is not publicly distributed here.

## Limitations

- This repository provides the data preparation component, not a complete sentiment classification model.
- No pretrained model weights or fine-tuning checkpoints are included.
- Model evaluation results are not reproduced by the files in this repository.
- The preprocessing script assumes that the input file contains valid column names and supported sentiment labels.

## Academic Context

This work formed part of an undergraduate dissertation exploring Chinese text sentiment analysis using large language models.

The publicly available code focuses on preparing structured sentiment classification data for subsequent experimentation.

## Author

Wenyue Zhang

BSc Computer Science — Shanghai University of Finance and Economics

Currently pursuing an MSc in Business Analytics at the University of Sheffield.
