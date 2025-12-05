INVIS1 = "\u200B"
INVIS2 = "\u200C"

START = INVIS1 * 10
END = INVIS2 * 10

STARTLEN = len(START)
ENDLEN = len(END)

bin_to_hidden = {"1": INVIS1, "0": INVIS2}
hidden_to_bin = {INVIS1: "1", INVIS2: "0"}

def encode(text: str) -> str:
    binary_text = "".join(format(b, "08b") for b in text.encode("utf-8"))
    hidden = "".join(bin_to_hidden[bit] for bit in binary_text)
    return START + hidden + END

def decode_file(filename: str):
    with open(filename, "r", encoding="utf-8") as fi:
        return decode(fi.read())

def decode(text: str) -> str:
    if START not in text:
        raise ValueError("START marker not found.")
    if END not in text:
        raise ValueError("END marker not found.")
    if text.count(START)>1:
        raise ValueError("More then one START marker found.")
    if text.count(END)>1:
        raise ValueError("More then one END marker found.")
    start_index = text.index(START) + STARTLEN
    end_index = text.rindex(END)
    encoded_text = text[start_index:end_index]
    try:
        binary = "".join(hidden_to_bin[ch] for ch in encoded_text)
    except KeyError:
        raise ValueError("Invalid hidden character encountered.")
    if len(binary) % 8 != 0:
        raise ValueError("Corrupted data: total bits is not a multiple of 8.")
    byte_arr = [int(binary[i:i+8], 2) for i in range(0, len(binary), 8)]
    return bytes(byte_arr).decode("utf-8")

if __name__ == "__main__":
    user_input = input("Input: ")
    encoded = encode(user_input)
    print(f"<Encoded>{encoded}<Encoded>")
    decoded = decode(encoded)
    print(f"<Decoded>{decoded}</Decoded>")
    with open("example_file.txt", "w", encoding="utf-8") as fo:
        fo.write(f"Hello, in this text there is an hidden string{encoded}.")
