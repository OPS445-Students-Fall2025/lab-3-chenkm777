#!/usr/bin/env python3
# Author ID: kchen129

import os

def free_space():
    with os.popen("df -h | grep '/$' | awk '{print $4}'") as p:
        output = p.read()
    return output.strip()

if __name__ == '__main__':
    print(free_space())
