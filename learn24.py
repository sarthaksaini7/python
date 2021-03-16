message = input("> ")


def emoji():
    words = message.split(" ")
    emoji = {
        ":)": "😁",
        ";)": "😉",
        ":(": "😭"
    }
    output = " "
    for word in words:
        output += emoji.get(word, word) + " "
    return output


print(emoji())
