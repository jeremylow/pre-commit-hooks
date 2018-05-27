#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import ast
import re
import sys

FIND_PATTERN = re.compile(r'^([ ]{1,})(?:.*)', re.UNICODE)


def check_module_indents(module):
    try:
        if not isinstance(model.body[0], ast.Expr):
            return (0, '')

        expr = model.body[0]
        init_lineno, doc_string = expr.lineno, expr.value.s

        # for modules, lineno is the *end* of the doc string
        lineno = init_lineno - len(re.findall('\n', doc_string))
        return (lineno, doc_string)
    except:
        return (0, '')


def check_doc_string(f, lineno, node, doc_string):
    fails = []
    retval = 0
    for line in doc_string.split('\n'):
        lineno += 1
        print(lineno, line)
        white_space_strings = re.findall(pattern=FIND_PATTERN, string=line)
        if not white_space_strings:
            continue
        if 0 < len(white_space_strings[0]) < 4:
            fails.append("{0}:{1} in {2}: spacing not a multiple of four.".format(f, lineno, node.name))
            retval = 1
        elif len(white_space_strings[0]) % 4 != 0:
            fails.append("{0}:{1} in {2}: spacing not a multiple of four.".format(f, lineno, node.name))
            retval = 1
    return (retval, fails)


def main(files):
    retval = 0
    failures = []

    for f in files:
        with open(f) as _file:
            source = _file.read()

        tree = ast.parse(source)
        for node in ast.walk(tree):

            # print(node)
            # print(failures)
            # print("#"*30)

            if isinstance(node, ast.Module):
                # import ipdb; ipdb.set_trace()
                lineno, doc_string = check_module_indents(node)
                retval, fails = check_doc_string(f, lineno, node, doc_string)
                if fails: failures += fails
                # print(retval, failures)
            else:
                try:
                    doc_string = ast.get_docstring(node)
                except Exception as e:
                    continue

                if doc_string:
                    retval, fails = check_doc_string(f, node.lineno, node, doc_string)
                    if fails: failures += fails

                else:
                    continue

    if failures:
        print(failures, type(failures))
        [print(failure) for failure in failures]
        return 1
    else:
        return 0


if __name__ == "__main__":
    files = sys.argv[1:]
    exit(main(files))
