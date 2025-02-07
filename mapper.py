#!/usr/bin/env python
import sys
import re

def main():
    for line in sys.stdin:
        # Clean and split the text
        words = re.findall(r'\w+', line.lower())
        for word in words:
            print(f'{word}\t1')

if __name__ == "__main__":
    main()
