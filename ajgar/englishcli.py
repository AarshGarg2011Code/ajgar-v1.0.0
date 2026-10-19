'''
Ajgar v1.0.0 COMPLETE RE-MODEL
v0.1.0 focused on direct Python builtins change and could've become chaotic when it came to syntax.
Re-Model v1.0.0 features a Ajgar Transpiler & Interpreter, easier to make and more feasible
This also enables syntax translation
This version of Ajgar can also be used as a template for other languages' versions of Python.
Made by Aarsh Garg in 2026.
File - 'englishcli.py'
'''
from .transpiler import transpile
import argparse
import sys
def main():
    parser = argparse.ArgumentParser(
            description="ajgar - a python-in-hindi transpiler & interpreter"
        )
    parser.add_argument("input_file", help="path to input python (.py) file to be interpreted")
    parser.add_argument(
            "-o", "--output", help="path for output python file if transpiled code needs to be saved"
        )
    args = parser.parse_args()
    if not args.input_file: print("no input file to transpile & interpret")
    else:
        try:
            payload = transpile(args.input_file)
            if args.output: payload.save(args.output)
            else: payload.runpy()
        except Exception as e: print(e)
    input("Press enter to continue . . .")
if __name__ == "__main__": main()
