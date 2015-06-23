#!/usr/bin/env python3

import sys
from gi.repository import GLib

try:
	#help(GLib.file_set_contents)
	path = "data.txt"
	content = "中文"
	GLib.file_set_contents(path, content.encode("utf-8"))
	#GLib.file_set_contents(path, bytes(content, "utf-8"))
	#GLib.file_set_contents(path, bytearray(content, "utf-8"))
except GLib.GError as e:
	print("Error: ", e.message)
else:
	pass


# https://lazka.github.io/pgi-docs/#GLib-2.0/functions.html#GLib.file_set_contents
# https://docs.python.org/3/library/functions.html#bytearray
# https://docs.python.org/3/library/functions.html#bytes
# https://docs.python.org/3/library/functions.html#func-str
# https://docs.python.org/3/library/stdtypes.html#str.encode
# # https://github.com/GNOME/gnome-tweak-tool/blob/master/gtweak/gtksettings.py
# http://stackoverflow.com/questions/7585435/best-way-to-convert-string-to-bytes-in-python-3
