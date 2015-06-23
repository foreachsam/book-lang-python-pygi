#!/usr/bin/env python3

import sys
from gi.repository import GLib

try:
	#help(GLib.file_get_contents)
	#rs = GLib.file_get_contents("data.txt")
	ok, content = GLib.file_get_contents("data.txt")
except GLib.GError as e:
	print("Error: ", e.message)
else:
	if not ok:
		print("Failed")
		sys.exit()
	print(content.decode("utf-8"))
	#print(str(content, "utf-8"))

# https://lazka.github.io/pgi-docs/#GLib-2.0/functions.html#GLib.file_get_contents
# https://docs.python.org/3/library/functions.html#bytearray
# https://docs.python.org/3/library/functions.html#bytes
# https://docs.python.org/3/library/functions.html#func-str
# https://docs.python.org/3/library/stdtypes.html#bytes.decode
# https://docs.python.org/3/library/stdtypes.html#str
# https://docs.python.org/3/library/stdtypes.html#textseq
# https://docs.python.org/3/reference/lexical_analysis.html#strings
# http://stackoverflow.com/questions/606191/convert-bytes-to-a-python-string
