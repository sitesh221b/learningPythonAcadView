import re

#       QUESTION 1

emails = "zuck26@facebook.com page33@google.com jeff42@amazon.com"
pattern = re.compile(r"(\w+)@([a-z]+)\.([a-z]+)")
print(re.findall(pattern, emails, flags=re.IGNORECASE))


#       QUESTION 2

text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
pattern = re.compile(r"(\bB\w+)")
print(re.findall(pattern, text, flags=re.IGNORECASE))


#       QUESTION 3

sen = "A, very very; irregular_sentence"
pattern = re.compile(r"[a-zA-Z]+")
print(' '.join(re.findall(pattern, sen)))


#       QUESTION 1(Optional)

tweet = "Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats"
tweet = re.sub('http\S+', '', tweet)
tweet = re.sub('@\w+', '', tweet)
tweet = re.sub('#\w+', '', tweet)
tweet = re.sub('RT|cc|!|:', '', tweet)
tweet = re.sub('\s+', ' ', tweet)
print(tweet)
