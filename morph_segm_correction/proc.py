import sys

f = open(sys.argv[1], "rb")
text = f.read().decode(errors='replace')
print(text)
