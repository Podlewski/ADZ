import numpy as np
import matplotlib.pyplot as plt
from random import random


def trapezoid_func(x, a, b, c, d, multiplier=1):
    if x <= a:
        return 0
    elif a < x < b:
        return (x - a) / (b - a) * multiplier
    elif b <= x <= c:
        return 1 * multiplier
    elif c < x < d:
        return (d - x) / (d - c) * multiplier
    else:
        return 0


def trapezoid(a, b, c, d, multiplier=1):
    return lambda x: trapezoid_func(x, a, b, c, d, multiplier)


def plot_trapezoid(funcs, begin, end, name, xlabel, labels=[]):
    x = np.linspace(begin, end, 10000)
    for f in funcs:
        y = [f(xi) for xi in x]
        plt.plot(x, y, c=(random(), random(), random()))

    plt.xlabel(xlabel)
    plt.ylabel("Membership")
    plt.title(name)

    if len(labels) > 0:
        plt.legend(labels, loc='center right', fontsize="x-small")

    plt.savefig(f"plots/{name}.png", dpi=300)
    plt.close()


def create_fuzzy_sheet(sheet, df):
    not_liked = trapezoid(0, 0, 5, 10)
    neutrally_received = trapezoid(-0.2, 0, 0, 0.2)
    very_popular = trapezoid(5000, 7000, 10000, 15000)

    not_liked_title = "Tweet has no likes"
    neutrally_received_title = "Tweet was neutrally received"
    very_popular_title = "Tweet author is very popular"
    sheet.append(["Author", "Tweet", not_liked_title, neutrally_received_title, very_popular_title])

    for index, row in df.iterrows():
        sheet.append([row.twitter_name, row.text, not_liked(row.likes), neutrally_received(row.polarity), very_popular(row.followers)])

    plot_trapezoid([not_liked], 0, 15, not_liked_title, "Likes")
    plot_trapezoid([neutrally_received], -0.5, 0.5, neutrally_received_title, "Polarity")
    plot_trapezoid([very_popular], 4000, 16000, very_popular_title, "Followers")


def create_fuzzy_interval_sheet(sheet, df):
    very_liked_max = trapezoid(200, 300, 1000, 1000)
    very_liked_min = trapezoid(200, 300, 1000, 1000, multiplier=0.8)

    negatively_received_max = trapezoid(-1, -1, -0.7, -0.1)
    negatively_received_min = trapezoid(-1, -1, -0.7, -0.1, multiplier=0.8)

    moderately_popular_max = trapezoid(1000, 2000, 4000, 5000)
    moderately_popular_min = trapezoid(1000, 2000, 4000, 5000, multiplier=0.8)

    very_liked_title = "Tweet has a lot of likes"
    negatively_received_title = "Tweet was negatively received"
    moderately_popular_title = "Tweet author is moderately popular"
    sheet.append(["Author", "Tweet",
                  f"{very_liked_title} (min)", f"{very_liked_title} (max)",
                  f"{negatively_received_title} (min)", f"{negatively_received_title} (max)",
                  f"{moderately_popular_title} (min)", f"{moderately_popular_title} (max)"])

    for index, row in df.iterrows():
        sheet.append([row.twitter_name, row.text,
                      very_liked_min(row.likes), very_liked_max(row.likes),
                      negatively_received_min(row.polarity), negatively_received_max(row.polarity),
                      moderately_popular_min(row.followers), moderately_popular_max(row.followers)])

    plot_trapezoid([very_liked_max, very_liked_min], 100, 1000, very_liked_title, "Likes", ["max", "min"])
    plot_trapezoid([negatively_received_max, negatively_received_min], -1, 0, negatively_received_title, "Polarity", ["max", "min"])
    plot_trapezoid([moderately_popular_max, moderately_popular_min], 500, 6000, moderately_popular_title, "Followers", ["max", "min"])


def create_r_coefficient(sheet, df):
    negatively_received = trapezoid(-1, -1, -0.6, -0.3)
    moderately_negatively_received = trapezoid(-0.4, -0.35, -0.2, -0.1)
    neutrally_received = trapezoid(-0.2, 0, 0, 0.2)
    moderately_positively_received = trapezoid(0.1, 0.2, 0.35, 0.4)
    positively_received = trapezoid(0.3, 0.6, 1, 1)
    receival = [negatively_received, moderately_negatively_received, neutrally_received, moderately_positively_received, positively_received]

    not_popular = trapezoid(0, 0, 100, 200)
    little_popular = trapezoid(150, 500, 800, 1200)
    moderately_popular = trapezoid(1000, 2000, 4000, 5000)
    very_popular = trapezoid(5000, 7000, 10000, 15000)
    extremely_popular = trapezoid(15000, 20000, 1000000, 1000000)
    popularity = [not_popular, little_popular, moderately_popular, very_popular, extremely_popular]

    sheet.append(["Author", "Tweet", "Receival to popularity R coefficient"])

    for index, row in df.iterrows():
        numerator = [rec(row.polarity) * pop(row.followers) for rec, pop in zip(receival, popularity)]
        denominator = [rec(row.polarity) for rec in receival]

        r_coef = np.sum(numerator) / np.sum(denominator)

        sheet.append([row.twitter_name, row.text, r_coef])
        
    plot_trapezoid(receival, -1, 1, "Receival", "Polarity", ["Negatively received",
                                                             "Moderately negatively received",
                                                             "Neutrally received",
                                                             "Moderately positively received",
                                                             "Positively received"])

    plot_trapezoid(popularity, 0, 22000, "Popularity", "Followers", ["Not popular",
                                                                     "Little popular",
                                                                     "Moderately popular",
                                                                     "Very popular",
                                                                     "Extremely popular"])
