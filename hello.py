#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""INT6181 Tutorial 2: a small Python file to push to GitHub."""

from datetime import datetime


def greet(name="QuocQuang"):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return "Hello, {}! Current time: {}".format(name, now)


if __name__ == "__main__":
    print(greet())
    print("This file was pushed to GitHub for Tutorial 2.")
