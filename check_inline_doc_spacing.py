#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import ast
import re
import sys


def check_indents(files):
    failures = []
    finder = re.compile(r'(?:\n{1,})([ ]{1,})(?:.*)', re.UNICODE)

    for f in files:
        with open(f) as _file:
            source = _file.read()
        nodes = ast.parse(source).body
        doc_strings = [
            (ast.get_docstring(node), node)
            for node in nodes
            if isinstance(node, ast.FunctionDef)
        ]
        for (dstring, node) in doc_strings:
            if not dstring: continue

            for line in dstring.split('\n'):
                white_space_strings = re.findall(pattern=finder, string=line)
                lineno = node.lineno
                if 0 < len(line) < 4:
                    failures.append("{0}:{1} in {2}: spacing not a multiple of four.".format(f, node.lineno, node.name))
                    retval = 1
                elif len(line) % 4 != 0:
                    failures.append("{0}:{1} in {2}: spacing not a multiple of four.".format(f, node.lineno, node.name))
                    retval = 1
                lineno += 1
    if retval:
        [print(failure) for failure in failures]
        return retval
    return 0


if __name__ == "__main__":
    files = sys.argv[1:]
    exit(check_indents(files))
