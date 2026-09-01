
import pandas as pd
import re
from googletrans import Translator

translator = Translator()

def translate_text(text):
    if pd.isna(text) or text == "":
        return ""
    try:
        translated = translator.translate(str(text), src='en', dest='bn')
        return translated.text
    except:
        return str(text)[:200]

def clean_bangla_text(text):
    if pd.isna(text):
        return ""
    text = str(text).strip()
    text = re.sub(r'[a-zA-Z]', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\u0980-\u09FF\s]', '', text)
    return text

# ১. বাংলা রিয়েল নিউজ লোড
real_bn = pd.read_excel("/mnt/g/banglafake-detection/data/raw/Bangla_Real_News_Dataset.xlsx")
print("বাংলা রিয়েল:", len(real_bn))

# ২. ইংরেজি রিয়েল নিউজ লোড
real_en = pd.read_excel("/mnt/g/banglafake-detection/data/raw/Translated_English_Real_News_Dataset.xlsx")
print("ইংরেজি রিয়েল:", len(real_en))

# ৩. ইংরেজি ফেক নিউজ লোড
fake_en = pd.read_excel("/mnt/g/banglafake-detection/data/raw/Translated_English_Fake_News_Dataset.xlsx")
print("ইংরেজি ফেক:", len(fake_en))

all_data = []

# ১. বাংলা রিয়েল (লেবেল 1)
for _, row in real_bn.iterrows():
    text = clean_bangla_text(row['Content'])
    if len(text) > 10:
        all_data.append([text, 1])

# ২. ইংরেজি রিয়েল → বাংলায় অনুবাদ (লেবেল 1)
for _, row in real_en.iterrows():
    text = translate_text(row['Content_Enlish'])
    text = clean_bangla_text(text)
    if len(text) > 10:
        all_data.append([text, 1])

# ৩. ইংরেজি ফেক → বাংলায় অনুবাদ (লেবেল 0)
for _, row in fake_en.iterrows():
    text = translate_text(row['Content_English'])
    text = clean_bangla_text(text)
    if len(text) > 10:
        all_data.append([text, 0])

df = pd.DataFrame(all_data, columns=['text', 'label'])
print("মোট ডেটা:", len(df))
print(df['label'].value_counts())

# ২৫০ রিয়েল + ২৫০ ফেক
real_sample = df[df['label'] == 1].sample(n=250, random_state=42)
fake_sample = df[df['label'] == 0].sample(n=250, random_state=42)

final_df = pd.concat([real_sample, fake_sample]).sample(frac=1, random_state=42)
final_df.to_csv("/mnt/g/banglafake-detection/data/processed/bangla_fake_news_500.csv", index=False)

print("✅ ডেটাসেট তৈরি হয়েছে!")
print(final_df.head())

