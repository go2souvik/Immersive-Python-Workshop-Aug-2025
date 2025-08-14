# importing the necessary packages
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
# Loading our sentiment analyzer
sent_an = SentimentIntensityAnalyzer()

example_sentences = ["As I said above, if you're a novice, a relative newcomer or just an experienced web designer who wants a refresher course, this is a good way to do it.",
                     "Kinda dumb UI choice, initially confusing.",
                     "If you would like to dive into the publishing aspects and really optimizing your workflow, then this would be a good investment for you.",
                     "The exposition is clear, but perhaps a bit dry.",
                     "The software is well known and excellent."]

sent_an = SentimentIntensityAnalyzer()
def vader_sentiment(text):
    return sent_an.polarity_scores(text)['compound']

for text in example_sentences:
  sample_val = vader_sentiment(text)
  if sample_val < -0.05:
    label = 'negative'
  elif sample_val > 0.05:
    label = 'positive'
  else:
    label = 'neutral'
  print(text, sample_val, label)
  