import sys


par = sys.argv[1]

with open("about_use", "w", encoding="utf-8") as f:
    f.write(par)
    f.close()
