#!/usr/bin/env python3

# Fixes a couple of weirdnesses with Notion’s markdown
#
# It does two things:
#
# 1. Moves misplaced image captions into alts of the images.
#    This assumes that all images originally had captions,
#    if it was not the case something bad will happen.
# 2. Replaces `#` with `%` in the first line of the file,
#    which contains the title of the document.
#
# Usage: ./fix-notion-md.py <filename>
#

import re
import sys


def fix_image_captions(text):
  pat = re.compile(r'^!\[\]\((.*)\)\n\n(.*)$', re.MULTILINE)
  return pat.sub(r'![\2](\1)', text)

def fix_title(text):
  lines = text.splitlines()
  return '\n'.join(['% ' + lines[0][2:]] + lines[1:])


if len(sys.argv) != 2:
  raise ValueError('Expected a file name as a single argument')
fpath = sys.argv[1]

with open(fpath, 'r') as f:
  text = fix_title(fix_image_captions(f.read()))

with open(fpath, 'w') as f:
  f.write(text)
