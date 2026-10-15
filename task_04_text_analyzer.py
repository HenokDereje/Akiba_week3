# TEXT STATISTICS AND WORD ANALYZER

def count_words(text):
    text = text.split(" ")
    count = 0
    for word in text:
        count += 1
    return [count, text]

def longest(text):
    text.sort(key=len, reverse=True)

    return text[0]

def repeated_words(text):
    seen = set()
    duplicate = set()
    for word in text:
        if word in seen:
            duplicate.add(word)
        else:
            seen.add(word)

    return list(duplicate)

def stat(text):
    count, text_listed = count_words(text)
    longest_word = longest(text_listed)
    rep_words = repeated_words(text_listed)

    return f"Words: {count}\nLongest Word: {longest_word}\nRepeated words: {rep_words}"

text = "Python is useful and Python is powerful."

print(stat(text))