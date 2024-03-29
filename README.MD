# Package Cleaner

## Overview

This program is designed to delete all locally installed Python packages. If you're a beginner programmer, you might have accumulated numerous pip packages on your system, which are no longer needed, especially after you've learned how to create and manage virtual environments. While this program serves no practical purpose other than aesthetic, it can help you clean up your environment by removing all locally installed packages.

**Please Note:** This program will delete all locally downloaded packages.

## How to Use

To use this program, follow these simple steps in your terminal:

1. First, create a `requirements.txt` file containing a list of all installed packages by running the following command:
    ```bash
    pip freeze > requirements.txt
    ```

2. Next, execute your Python application using the following command:
    ```bash
    py app.py
    ```

That's it! Your local Python environment will now be free of any installed packages.
