============================================================================
BanglaFakeNews2025: A Balanced and Manually Annotated Bangla Fake News Dataset
============================================================================

Published on:   Mendeley Data
DOI:            10.17632/c6hf7g5f3t.1
License:        CC BY 4.0

CONTRIBUTORS
----------------------------------------------------------------------------
Samia Maliha
Md. Shahrukh Hossain
Department of Information and Communication Technology,
Bangladesh University of Professionals (BUP), Dhaka, Bangladesh

Supervisor: Md. Musfique Anwar, PhD, Professor, Department of Computer
Science and Engineering, Jahangirnagar University, Dhaka, Bangladesh

Contact: samiamalihalamin@gmail.com


1. OVERVIEW
----------------------------------------------------------------------------
This dataset contains 4,000 manually annotated Bangla news articles for
fake news detection research, published between 2021 and 2025:

    - 2,000 Real news articles        (Label = 1)
    - 2,000 Fake news articles        (Label = 0)

The dataset is perfectly class-balanced and enriched with structured
metadata, supporting binary fake news detection, fake news type
classification, headline-content consistency analysis, topical category
prediction, and temporal generalization studies. English translations of
all headlines and article bodies are also provided to enable multilingual misinformation research.


2. FILES INCLUDED
----------------------------------------------------------------------------
1) Bangla_Real_News_Dataset.xlsx
   2,000 authentic Bangla news articles collected from credible
   mainstream Bangla news outlets.

2) Bangla_Fake_News_Dataset.xlsx
   2,000 fake Bangla news articles collected from verified reports of
   fact-checking organizations operating in Bangladesh.

3) Translated_English_Real_News_Dataset.xlsx
   English version of the real news file. The Headline and Content
   fields were translated from Bangla to English using Google Translate.
   All other fields are identical to the Bangla file.

4) Translated_English_Fake_News_Dataset.xlsx
   English version of the fake news file, translated the same way.

5) README.txt
   This file.


3. DATASET SCHEMA (COLUMN DESCRIPTIONS)
----------------------------------------------------------------------------
Column       | Description
-------------|--------------------------------------------------------------
Article ID   | Unique identifier for each article
Domain       | Publisher's website name
Date         | Publication date of the article
Category     | Topical category of the article (12 categories)
Headline     | Headline or title of the news article
Content      | Full article body text
Label        | 1 = Real (Authentic), 0 = Fake
Source       | Verifying source for the claim
Relation     | Related / Unrelated. "Related" if the headline accurately
             | reflects the claim made in the article body; "Unrelated"
             | if the headline misrepresents or exaggerates the content
F-type       | Fine-grained fake news type: Fabricated, Clickbait,
             | Satire, or Altered. Authentic articles are labeled
             | "Not Applicable"


4. CATEGORIES (12)
----------------------------------------------------------------------------
Politics, National, International, Sports, Entertainment, Crime,
Education, Technology, Finance, Lifestyle, Editorial, Miscellaneous


5. LABELING AND ANNOTATION
----------------------------------------------------------------------------
Every article was manually reviewed and labeled. Beyond the binary
Real/Fake label, each fake article was annotated with a fine-grained
fake news type (F-type), and every article was annotated for
headline-content consistency (Relation). The Relation field captures a
common form of "soft misinformation" in which a factual article body is
paired with a misleading or exaggerated headline.


6. DATA COLLECTION SOURCES
----------------------------------------------------------------------------
All data were collected from publicly available sources for academic
research purposes.

Fake news sources (fact-checking organizations):
    1. Rumor Scanner                  https://rumorscanner.com/
    2. DhakaFactCheck                 https://factcheckbangla.afp.com/
    3. FactWatch                      https://www.fact-watch.org/    
    4. Jachai (Bangladesh)            https://jachai.org/
    5. Boom BD                        https://www.boombd.com/
    6. Aaj Tak Bangla - Fact Check    https://bangla.aajtak.in/fact-check
    7. eArki                          https://earki.co/

Real (Authentic) news sources:
    1. Prothom Alo                    https://www.prothomalo.com/
    2. BBC News Bangla                https://www.bbc.com/bengali
    3. Jamuna TV                      https://www.jamuna.tv/
    4. Samakal                        https://samakal.com/
    5. News24                         https://www.news24bd.tv/
    6. Dhaka Tribune                  https://www.dhakatribune.com/
    7. Somoy TV                       https://www.somoynews.tv/
    8. Independent TV                 https://www.itvbd.com/
    9. Ittefaq                        https://www.ittefaq.com.bd/
   10. Bangladesh Pratidin            https://www.bd-pratidin.com/


7. TRANSLATION NOTE
----------------------------------------------------------------------------
The English files were produced by machine-translating the Headline and
Content fields from Bangla to English using Google Translate. Machine
translation may introduce minor grammatical or semantic artifacts;
researchers requiring exact wording should refer to the original Bangla
files, which are the authoritative version of the dataset.


8. INTENDED USES
----------------------------------------------------------------------------
- Binary fake news detection (Real vs. Fake)
- Fake news type classification (Fabricated / Clickbait / Satire / Altered)
- Headline-content analysis
- Topical category classification
- Cross-lingual and multilingual misinformation research
- Temporal generalization studies (2021-2025 coverage)


9. ETHICAL STATEMENT
----------------------------------------------------------------------------
All articles were collected from publicly available news and
fact-checking websites. No private or personally identifiable user data
was collected. The dataset is released strictly for academic and
research purposes in misinformation detection. The "Fake" label reflects
the verdicts of the listed fact-checking organizations and the authors'
manual review at the time of collection.



