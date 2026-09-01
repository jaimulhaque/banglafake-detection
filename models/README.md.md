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