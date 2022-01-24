"""

MCAT CARS PROGRESSION
SEAN SOLOMON

Graphs showing my daily performance of CARS practice questions from the Jack Westin question bank
As more days come by, I will adjust the graph to represent a daily average as opposed to individual scores

"""

import numpy as np
from matplotlib import pyplot as plt
# from datetime import datetime as dt

def main():
    x_times = [487, 440, 441, 470, 680, 590, 758]
    y_scores = [5/6, 3/5, 3/5, 2/6, 3/7, 4/5, 5/6]
    
    # Graph properties
    plt.figure(figsize=(8, 6))
    plt.title("Scores vs. Times on CARS Practice Questions")
    plt.xlabel("Time (sec)")
    plt.ylabel("Score")
    plt.xlim([0, 781]) # Up to 13 mins (780 sec)
    plt.ylim([0, 1]) # Up to 13 mins (780 sec)
    plt.fill_between([i for i in range(300, 601)], 1, 0.8, color="skyblue") #(x_range, y_max, y_min)
    plt.scatter(x_times, y_scores, color='purple')

    # Minutes divider
    plt.axvline(x=600, color='r', label='10-min mark')
    plt.axvline(x=540, color='r', ls=":")
    plt.axvline(x=480, color='y', label='8-min mark')
    plt.axvline(x=420, color='y', ls=":")
    plt.axvline(x=360, color='g', label='6-min mark')
    plt.axvline(x=300, color='g', ls=":")
    plt.legend(loc='lower left')

    caption="The shaded blue region represents the score-time combination to aim for"
    plt.figtext(0.5, 0.01, caption, wrap=False, horizontalalignment='center', fontsize=10)

    plt.show()

if __name__ == "__main__":
    main()