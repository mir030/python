import string


def pangrams(s):
    sentence = s.lower()
    sentence_set = "".join(set(sentence))
    sentence_set_no_space = sentence_set.replace(" ", "")

    if len(sentence_set_no_space) != 26:
        return 'not pangram'
    return "pangram"

alphabets = list(string.ascii_lowercase);

print(alphabets)