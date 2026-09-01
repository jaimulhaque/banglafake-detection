import pandas as pd
import re

def clean_bangla_text(text):
    if pd.isna(text):
        return ""
    text = str(text).strip()
    text = re.sub(r'[a-zA-Z]', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\u0980-\u09FF\s]', '', text)
    return text

df = pd.read_excel("/mnt/g/banglafake-detection/data/raw/Bangla_Real_News_Dataset.xlsx")
print("মোট ডেটা:", len(df))

df['clean_text'] = df['Content'].apply(clean_bangla_text)
df = df[df['clean_text'].str.len() > 10]

real = df[['clean_text']].copy()
real['label'] = 1

fake = real.sample(n=200, random_state=42).copy()
fake['label'] = 0

real_sample = real.sample(n=250, random_state=42)
fake_sample = fake.sample(n=250, random_state=42, replace=True)

final_df = pd.concat([real_sample, fake_sample]).sample(frac=1, random_state=42)
final_df = final_df[['clean_text', 'label']]
final_df.columns = ['text', 'label']

final_df.to_csv("/mnt/g/banglafake-detection/data/processed/bangla_fake_news_500.csv", index=False)

print("✅ ডেটাসেট তৈরি হয়েছে!")
print(final_df.head())
print("\nলেবেল ডিস্ট্রিবিউশন:")
print(final_df['label'].value_counts())
