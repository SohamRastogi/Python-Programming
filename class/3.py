import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as alpha:
    print("OS error:", alpha)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as alpha:
    print(f"Unexpected {alpha=}, {type(alpha)=}")
    raise