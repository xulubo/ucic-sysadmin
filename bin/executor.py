#!/usr/bin/env python
import os

def main():
    cmd = raw_input()

    print os.popen(cmd).read()

if __name__ == "__main__":
    main()

