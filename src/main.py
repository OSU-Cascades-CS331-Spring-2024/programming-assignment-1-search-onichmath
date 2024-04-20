import usage
import sys

if __name__ == "__main__":
    try:
        raise Exception("Arguments were provided incorrectly")
    except:
        usage.help()
