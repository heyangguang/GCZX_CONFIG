import sys
from backend import main



if __name__ == "__main__":
    interactive_obj = main.ArgvHandler(sys.argv)
    interactive_obj.call()