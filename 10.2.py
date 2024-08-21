import string


def first_word(text):
    new_text = ''
    for i, char in enumerate(text):
        if char == "'":
            if i > 0 and i < len(text) - 1:
                if text[i - 1].isalpha() and text[i + 1].isalpha():
                    new_text += char
                    continue
            continue
        new_text += char

    text_list = (''.join(' ' if char in string.punctuation and char != "'" else char for char in new_text)).split()
    return text_list[0]


print(first_word("'''Hello world"))
print(first_word("greetings, friends"))
print(first_word("don't touch it"))
print(first_word(".., and so on ..."))
print(first_word("hi"))
print(first_word("Hello.World"))
