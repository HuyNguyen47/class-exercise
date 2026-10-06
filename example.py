import pandas as pd
import matplotlib.pyplot as plt
import re

data = {"ID":range(100),"Score":[10]*2+[20]*3+[30]*5+[50]*15+[60]*20+
[70]*25+[80]*15 +[90]*8 +[100,100,5,5,0,0,5000]}
df = pd.DataFrame(data)
print(df)

print(df.shape)
print(df.dtypes)
print(df.describe())

df_original = df.copy()

# df['Score'][:-1].plot.hist(bins=300, edgecolor='black')
# plt.show()


q1 = df["Score"].quantile(0.25)
q3 = df["Score"].quantile(0.75)
iqr = q3 - q1
# Use the equation above to replace None
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
print(lower)
print(upper)

# df_score_cleaned = df[(df["Score"] >= lower) & (df["Score"] <= upper)]
# df_score_cleaned['Score'].plot.hist(bins=300, edgecolor='black')
# plt.show()


mean = df["Score"].mean()
std = df["Score"].std()
# Use the equation above to replace None
z_scores = (df["Score"] - mean) / std
print(z_scores)

df_score_cleaned = df[z_scores.abs() <= 3]

iqr_threshold = 1.5
zscore_threshold = 3

import pandas as pd
data = {"ID":range(4),"Message":["Now Here "," now here ", " NOW HERE",
"Now here"]}
df = pd.DataFrame(data)
print(df)

# Strip Whitespace
df["Message"] = df["Message"].str.strip()
print(df)
# Convert to Lowercase
df["Message"] = df["Message"].str.lower()
print(df)
# removing repeated whitespace between words?
print(df["Message"].str.replace(' ',''))

print(re.sub(r"\s+", " ", "Hi      there"))
print(re.findall(r"\S+", "Hi there"))

def clean_text(text):
    text = text.strip()
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text

df["Message"] = df["Message"].apply(clean_text)
print(df)

links = ["https://example.com", "www.github.com/mylink/"]
data = pd.Series(links)
print(data)
def replace_url(text):
    text = re.sub(r"https?://\S+|www\.\S+", "URL", text)
    return text
# Remove URLs
data = data.apply(replace_url)
print(data)

