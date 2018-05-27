from __future__ import print_function

import argparse
import ast
import io
import sys


def check_indents(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="python filenames to check.")
    args = parser.parse_args(argv)
    pattern = re.compile(r"""(?:\n{1,})
                             ([ ]{1,})
                             (?:.*)""", re.X)

    return_value = 0

    for f in filenames:
        with open(f):
            source = f.read()
        nodes = ast.parse(source).body
        doc_strings = [ast.get_docstring(node) for node in nodes if isinstance(node, ast.FunctionDef)]
        for dstring in doc_strings:
            white_space_strings = re.findall(pattern, dstring)
            for s in white_space_strings:
                if 0 < len(s) < 4:
                    return_val = 1
                elif len(s) % 4 != 0:
                    return_val = 1
        print(return_val)
        return return_val

   return return_value


if __name__ == "__main__":
    sys.exit(check_indents())
