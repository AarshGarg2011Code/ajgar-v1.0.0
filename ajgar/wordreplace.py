'''
Ajgar v1.0.0 COMPLETE RE-MODEL
v0.1.0 focused on direct Python builtins change and could've become chaotic when it came to syntax.
Re-Model v1.0.0 features a Ajgar Transpiler & Interpreter, easier to make and more feasible
This also enables syntax translation
This version of Ajgar can also be used as a template for other languages' versions of Python.
Made by Aarsh Garg in 2026.
File - 'wordreplace.py'
'''
import json, io, tokenize
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
def wordreplace(filename: str, keyjson=BASE_DIR / "keywords.json"):
    with open(keyjson, "r", encoding="utf-8") as f: keywords = json.load(f)
    with open(filename, "r", encoding="utf-8") as f: source = f.read()
    tokens = []
    for tok in tokenize.generate_tokens(io.StringIO(source).readline):
        if tok.type == tokenize.NAME and tok.string in keywords: tok = tok._replace(string=keywords[tok.string])
        tokens.append(tok)
    return tokenize.untokenize(tokens)
