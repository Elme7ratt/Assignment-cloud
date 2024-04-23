import nltk
from nltk.corpus import stopwords
from collections import Counter

# download stopwords list
nltk.download('stopwords')
nltk.download('punkt')

# Read the contents of file
with open("random_paragraphs.txt", "r") as file:
    text = file.read()

# convert text into words
words = nltk.word_tokenize(text)

# Remove stopwords
stop_words = set(stopwords.words('english'))

filtered_words = [word for word in words if word.lower() not in stop_words]

# Count the frequency of each word
word_freq = Counter(filtered_words)

# Display word frequency count
for word, freq in word_freq.items():
    print(f"{word}: {freq}")


