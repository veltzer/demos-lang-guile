#!/usr/bin/env python

""" Compile one Guile source into bytecode with `guild compile`, as a syntax
and semantics check of the demo. Invoked by the generator as
guile_build.py <input.scm> <output.go>. """

import os
import subprocess
import sys


def main():
    """ main entry point """
    source, output = sys.argv[1], sys.argv[2]
    os.makedirs(os.path.dirname(output), exist_ok=True)
    sys.exit(subprocess.call(
        ["guild", "compile", "-o", output, source]))


if __name__ == "__main__":
    main()
