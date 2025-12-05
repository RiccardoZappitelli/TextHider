bin_to_hidden = {
    "1":"\u200B",
    "0":"\u200C",
}
hidden_to_bin = {
    "\u200B":"1",
    "\u200C":"0"
}

def encoder(text: str) -> str:
    res = ""
    binary_text = ''.join(format(b, '08b') for b in text.encode('utf-8'))
    for bit in binary_text:
        res+=bin_to_hidden[bit]
    return res

def decoder(text: str) -> str:
    binary = "".join([ hidden_to_bin[x] for x in text])
    text = ''.join(
        chr(int(binary[i:i+8], 2))
        for i in range(0, len(binary), 8)
    )
    return text 

if __name__ == "__main__":
    encoded = encoder(input("Input: "))
    print(f"<Encoded>{encoded}<End Encoded>")
    decoded = decoder(encoded)
    print(f"<Decoded>{decoded}<End Decoded>") 