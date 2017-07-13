import sys, pyperclip, argparse

# Creates a separatethis.com style separator with a title
def create_separator(title, style="-"):
  length = 48 - len(title) // 2 
  start = length * (style + " ")
  end = length * (" " + style)
  return start + title + end

parser = argparse.ArgumentParser(description='Create a bookmark separator.')
parser.add_argument('title', metavar='title', type=str, help='title of bookmarks section')
args = parser.parse_args()

separator = create_separator(sys.argv[1])
pyperclip.copy(separator)
print(separator)
