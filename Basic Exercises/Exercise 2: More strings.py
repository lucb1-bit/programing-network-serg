text = "  Hello, World! Welcome to Python Programming.  "
txs= text.strip()

def split_text(tx):
    words = tx.split(" ")
    return len(words)





print("Stripped: ", text.strip())
print("The number of words in the string",split_text(txs))
print("Capitalized",txs.title())
print("The string starts with ""Hello"" ",txs.startswith("Hello"))
print("The stripped string ends with ""ing."" ", txs.endswith("ing."))
print("The position (index) of the word ""Python""", txs.find("Python"))
print("The words joined back together separated by "" - "": "," - ".join(txs.split(" ")))