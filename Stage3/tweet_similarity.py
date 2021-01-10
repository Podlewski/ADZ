from itertools import combinations
from numpy import sum


def word_similarity(w1, w2):
    n = max(len(w1), len(w2))
    ngrams = [w1[i:j] in w2 for i, j in combinations(range(len(w1) + 1), 2)]

    return 2 / (n**2 + n) * sum(ngrams)


def text_similarity(t1, t2):
    words1, words2 = t1.split(), t2.split()
    n = max(len(words1), len(words2))

    similarities = []
    for w1 in words1:
        w1_similarities = [word_similarity(w1, w2) for w2 in words2]
        similarities.append(max(w1_similarities))

    return 1 / n * sum(similarities)


def tweet_name(i, text):
    return f"Tweet {i+1}: {text}"


def create_tweet_similarity_sheet(sheet, tweets_col):
    tweet_names = [tweet_name(i, text) for i, text in tweets_col.iteritems()]
    sheet.append(["Similarity"] + tweet_names)

    for i, tweet in tweets_col.iteritems():
        print(f"Calculating tweet {i+1}/{len(tweets_col)} similarity...")
        res = [tweet_name(i, tweet)] + [text_similarity(tweet, other) for other in tweets_col]
        sheet.append(res)