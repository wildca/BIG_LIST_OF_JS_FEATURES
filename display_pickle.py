import pickle
import os

all_features_list = "text_list-features-from-javascript-big-query.txt"

test_online_symbolink_link = "github_symbolik_link"
import pickle
import os
import sys


def display_content(file):
    f = open(file, 'r')
    content = f.read()
    contentList = content.split(",")
    print(contentList)
    print("--------------------------------")
    print("Total: ", len(contentList))
    f.close()


if __name__ == '__main__':
    #display_content(all_features_list)
    display_content(test_online_symbolink_link)
