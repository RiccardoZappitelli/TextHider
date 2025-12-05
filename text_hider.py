START = "\u200D"
END = "\u2060"

bin_to_hidden = {
    "1":"\u200B",
    "0":"\u200C",
}
hidden_to_bin = {
    "\u200B":"1",
    "\u200C":"0"
}

def encode(text: str) -> str:
    res = START
    binary_text = ''.join(format(b, '08b') for b in text.encode('utf-8'))
    for bit in binary_text:
        res+=bin_to_hidden[bit]
    return res+END

def decode(text: str) -> str:
    try:
        start_index = text.index(START)
        end_index = text.index(END)
    except ValueError as e:
        if not(START in text):
            print("STARTING value not found in the text.")
        elif not(END in text):
            print("ENDING value not found in the text.")
        else:
            print(f"Unknown error:", e)
    except Exception as e:
            print(f"Unknown error:", e)

    encoded_text = text[start_index+1:end_index].replace(START, "").replace(END, "")

    binary = "".join([ hidden_to_bin[x] for x in encoded_text])
    text = ''.join(
        chr(int(binary[i:i+8], 2))
        for i in range(0, len(binary), 8)
    )
    return text 

if __name__ == "__main__":
    encoded = encode(input("Input: "))
    print(f"<Encoded>{encoded}<Encoded>")
    decoded = decode(encoded)
    print(f"<Decoded>{decoded}</Decoded>") 