'''
Ajgar v1.0.0 COMPLETE RE-MODEL
v0.1.0 focused on direct Python builtins change and could've become chaotic when it came to syntax.
Re-Model v1.0.0 features a Ajgar Transpiler & Interpreter, easier to make and more feasible
This also enables syntax translation
This version of Ajgar can also be used as a template for other languages' versions of Python.
Made by Aarsh Garg in 2026.
File - 'hindicli.py'
'''

# avoided use of argparse to keep CLI strictly in Hindi
from .transpiler import transpile
import sys
def parse():
    print("अजगर हिंदी CLI में आपका स्वागत है")
    print(
        "अगर कोई त्रुटि अंग्रेज़ी में दिखाई दे, तो घबराएँ नहीं! "
        "Python की अंग्रेज़ी समझने वाले किसी व्यक्ति से मदद माँगें। "
        "अजगर के आने वाले संस्करणों में इस समस्या को ठीक करने का "
        "प्रयास किया जाएगा।"
    )
    args = sys.argv[1:]
    config = {"input_file": None, "output_file": None}
    i = 0
    while i < len(args):
        item = args[i]
        if item in ("-h", "--help", "--सहायता"):
            print("उपयोग: ajgar [इनपुट-फ़ाइल] [--उत्पादन निर्गम-संचिका] [--सहायता]")
            print("\nअजगर को इन तर्कों की ज़रूरत है:")
            print("  इनपुट-फ़ाइल    प्रोसेस करने के लिए सोर्स फ़ाइल")
            print("  --उत्पादन    अगर आप प्रोसेस्ड Python कोड को सेव करना चाहते हैं, तो यह ऑप्शन उपलब्ध है")
            print("  निर्गम-संचिका    अगर आपने '--उत्पादन' ऑप्शन लिया है, तो आपको वह जगह डालनी होगी जहाँ कोड सेव करना है")
            print("  --सहायता    यह ऑप्शन हेल्प मेनू खोलता है")
            input("आगे बढ़ने के लिए Enter दबाएँ . . .")
            sys.exit(0)
        elif item in ("-o", "--output", "--उत्पादन"):
            if i + 1 < len(args):
                config["output_file"] = args[i + 1]
                i += 2
            else:
                print(f"त्रुटि (Error): '{item}' विकल्प के लिए आउटपुट फ़ाइल पथ आवश्यक है।")
                sys.exit(1)
        else:
            if config["input_file"] is not None:
                print(f"त्रुटि (Error): अनपेक्षित आर्गुमेंट '{item}'।")
                print("उपयोग: ajgar [इनपुट-फ़ाइल] [--उत्पादन निर्गम-संचिका] [--सहायता]")
                sys.exit(1)
            config["input_file"] = item
            i += 1
    return config
def main():
    cli_args = parse()
    if cli_args["input_file"] is None:
        print("चेतावनी: कोई इनपुट फ़ाइल नहीं दी गई। अजगर बंद हो रहा है।")
        input("आगे बढ़ने के लिए Enter दबाएँ . . .")
        sys.exit(0)
    infile = cli_args["input_file"]
    try: payload = transpile(infile)
    except Exception as e:
        print(f"फ़ाइल को ट्रांसपाइल करते समय एक त्रुटि आई है। \nइनपुट-फ़ाइल - {infile}. \n\nत्रुटि संदेश (अंग्रेज़ी): \n{str(e)}")
        sys.exit(1)
    if cli_args["output_file"] is not None:
        outfile = cli_args["output_file"]
        try:
            payload.save(outfile)
            print(f"प्रसंस्कृत कोड सफलतापूर्वक सहेज लिया गया है। \nइनपुट-फ़ाइल - {infile}. \nनिर्गम-संचिका - {outfile}.")
        except Exception as e: print(f"संपादित कोड को सहेजने का प्रयास करते समय एक त्रुटि आई है। \nइनपुट-फ़ाइल - {infile}. \nनिर्गम-संचिका - {outfile}. \n\nत्रुटि संदेश (अंग्रेज़ी): \n{str(e)}")
    else:
        try: payload.runpy()
        except Exception as e: print(f"कोड निष्पादित करते समय एक त्रुटि उत्पन्न हुई है। \nइनपुट-फ़ाइल - {infile}. \n\nत्रुटि संदेश (अंग्रेज़ी): \n{str(e)}")
    input("आगे बढ़ने के लिए Enter दबाएँ . . .")
