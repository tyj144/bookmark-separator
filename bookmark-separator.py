import sys, pyperclip

def create_separator(title, style="-"):
  dash = ((48 - len(title)) // 2 ) * (style + " ")
  return dash + title + " " + dash

separator = create_separator(sys.argv[1])
pyperclip.copy(separator)
print(separator)
