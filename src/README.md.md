# Bangla Fake News Detection using BanglaBERT

## 📌 Project Overview
This project detects **AI-generated fake Bangla news** using a **BanglaBERT + CNN + Attention** hybrid model.  
It addresses the growing problem of misinformation in Bengali social media and news platforms.

## 🎯 Problem Statement
With the rise of generative AI (ChatGPT, BanglaT5), fake Bangla news is becoming indistinguishable from real news.  
There is no effective detection system for **Bengali** fake news. This project fills that gap.

## 🧠 Model Architecture
- **Base Model:** BanglaBERT (csebuetnlp/banglabert)  
- **Additional Layers:** CNN for local patterns + Attention for interpretability  
- **Framework:** PyTorch + Hugging Face Transformers

## 📊 Dataset
- **Total Samples:** 500 (balanced: 250 real, 250 fake)  
- **Real News:** Scraped from Prothom Alo, Ittefaq  
- **Fake News:** Generated using ChatGPT and BanglaT5  
- **Format:** CSV with `text` and `label` (1=real, 0=fake)

## 📈 Results
| Metric | Score |
|--------|-------|
| Accuracy | ~89% |
| F1-Score | ~0.89 |
| Precision | ~0.88 |
| Recall | ~0.89 |

## 📂 Project Structure
banglafake-detection/
├── data/
│ └── processed/
│ └── bangla_fake_news_clean.csv
├── notebooks/
│ ├── 01_data_prep.ipynb
│ ├── 02_model_training.ipynb
│ └── 03_evaluation.ipynb
├── src/
│ ├── preprocess.py
│ └── train.py
├── models/
│ └── best_banglabert_fake.pth
├── reports/
│ └── figures/
├── paper/
├── requirements.txt
└── README.md

text

## 🚀 How to Run
1. Clone the repository:
```bash
git clone https://github.com/your-username/banglafake-detection.git
cd banglafake-detection
Activate environment:

bash
source /home/your-username/pytorch-env/bin/activate
Install dependencies:

bash
pip install -r requirements.txt
Run Jupyter Notebook:

bash
jupyter notebook
Run notebooks in order: 01_data_prep.ipynb → 02_model_training.ipynb → 03_evaluation.ipynb

🔮 Future Work
Expand dataset to 5000+ samples

Add XAI (SHAP/LIME) for model explainability

Deploy as a web app using Streamlit

📝 Paper
This project is submitted to [BUET ICECE / DU COMPAS] conference.

👤 Author
JAIMUL HAQUE
Department of CSE
BANGLADESH UNIVERSITY OF BUSINESS AND TECHNOLOGY

📄 License
MIT