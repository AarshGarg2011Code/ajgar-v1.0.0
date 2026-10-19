'''
Ajgar v1.0.0 COMPLETE RE-MODEL
v0.1.0 focused on direct Python builtins change and could've become chaotic when it came to syntax.
Re-Model v1.0.0 features a Ajgar Transpiler & Interpreter, easier to make and more feasible
This also enables syntax translation
This version of Ajgar can also be used as a template for other languages' versions of Python.
Made by Aarsh Garg in 2026.
File - 'transpiler.py'
'''
import ast
import sys
from .wordreplace import wordreplace
class transpile:
    def __init__(self, filename): self.filename = filename
    def getpy(self):
        pythonsrc = wordreplace(self.filename)
        return pythonsrc
    def analysepy(self, src):
        try:
            ast.parse(src)
            return True, None, None, None
        except SyntaxError as e: return False, e.lineno, e.msg, e.text
    def verifypy(self):
        src = self.getpy()
        valid, lineno, msg, text = self.analysepy(src)
        if valid: return src
        else: raise SyntaxError(f"त्रुटि: पंक्ति {lineno} पर सिंटैक्स त्रुटि मिली। \nगलत कोड टुकड़ा: {text.strip() if text else 'N/A'}")
    def runpy(self):
        src = self.verifypy()
        exec(src, {})
    def save(self, newfile: str):
        src = self.verifypy()
        with open(newfile, "w", encoding="utf-8") as nf: nf.write(src)
भाषांतरण = transpile
