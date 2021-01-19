"""
Clean text data corpus

1. Use itterator insted of loading whole data in memory.
2. Remove stupid characters from dataSet.
3. make this approach class based and general.
4. use pandas if needed.

"""

import re

from stop_words import character_set


def clean_line(raw_line: str) -> str:
    """Clean raw line and remove unwanted characters

    Args:
        raw_line (str): raw input

    Returns:
        str: cleaned and lowered case line.
    """
    cleanedLine = re.sub("\W", " ", raw_line)

    while bool(re.search("\s\s", cleanedLine)):
        cleanedLine = re.sub("  ", " ", cleanedLine)

    return cleanedLine


# if __name__ == "__main__":
#     print(clean_line("this is not $23 type of deat @ my house").split(" "))
#     print(clean_line("this # $ 6846 % ^ & & ").split(" "))
#     print(clean_line("    ").split(" "))