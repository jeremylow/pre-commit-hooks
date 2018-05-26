#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import ast
import re
import sys


def check_indents(files):
    retval = 0
    failures = []
    finder = re.compile(r'^([ ]{1,})(?:.*)', re.UNICODE)

    for f in files:
        with open(f) as _file:
            source = _file.read()
        nodes = ast.parse(source).body
        for node in nodes:
            try:
                doc_string = ast.get_docstring(node)
            except:
                continue
            lineno = node.lineno + 1

            if not doc_string: continue

            for line in doc_string.split('\n'):
                white_space_strings = re.findall(pattern=finder, string=line)
                if not white_space_strings:
                    continue
                if 0 < len(white_space_strings[0]) < 4:
                    failures.append("{0}:{1} in {2}: spacing not a multiple of four.".format(f, lineno, node.name))
                    retval = 1
                elif len(white_space_strings[0]) % 4 != 0:
                    failures.append("{0}:{1} in {2}: spacing not a multiple of four.".format(f, lineno, node.name))
                    retval = 1
                lineno += 1
    if retval:
        [print(failure) for failure in failures]
        return retval
    return retval


if __name__ == "__main__":
    files = sys.argv[1:]
    exit(check_indents(files))