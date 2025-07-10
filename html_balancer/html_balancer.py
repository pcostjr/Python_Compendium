# html_balancer.py
# description: A simple program which reads in an html file and uses a stack to determine if every html tag
# possesses an opening and a closing. Prerequisite: for this assignment we assume that each HTML tag (open & close)
# exists on its own newline without indentation.
# created 7.10.2025
# last update: 7.10.2025

# import the stack ADT from the lectures.
from stack import Stack
# import regular expression matching so we can check for html tags regardless of the specific tag
import re


# processes a string of characters where each term is (ideally) separated by newlines. Checks that each opened tag
# has a closed tag, and returns true or false depending on the result.

def html_checker(html_string):
    # create a new instance of Stack that we will use to store the contents
    tag_s = Stack()
    # split the string along newlines
    tag_l = html_string.split("\n")
    balanced = True
    i = 0
    # while there are items to iterate over, and we are still considered balanced
    while i < len(tag_l) and balanced:
        tag = tag_l[i]
        # Note: this would be easy to defeat in most contexts, but HTML validation is beyond the scope of this project
        # if the term is any assortment of characters between two angle brackets
        if re.match(r'<.*>', tag):
            # if we're looking at a closing tag:
            if re.match(r'</.*>', tag):
                # if the stack is empty, there is a close without an open
                if tag_s.is_empty():
                    balanced = False
                # the closer might not match the opener, or vice versa
                elif not tag[2:len(tag) - 1] == tag_s.peek():
                    balanced = False
                # else, we must have a match and can pop the tag off of the stack
                else:
                    tag_s.pop()

            else:
                # if not, push the substring of the tag onto the stack
                tag_s.push(tag[1:len(tag) - 1])
        i += 1
    # finally, return the result of checking if we're balanced, and if there are any remaining tags left in the stack
    return balanced and tag_s.is_empty()


# main method declaration
if __name__ == "__main__":
    filenames = ["missing_opener.html", "missing_closer.html", "missing_half.html", "mismatching.html", "good.html",
                 "empty.html"]
    for filename in filenames:
        with open(filename) as file:
            print(f"Results of checking {filename}: {html_checker(file.read())}")

