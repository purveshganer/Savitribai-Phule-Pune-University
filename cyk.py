def cyk_parser(grammar, sentence):
    n = len(sentence)
    table = [[set() for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for production in grammar:
            if sentence[i] in production[1]:
                table[i][i].add(production[0])

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                for production in grammar:
                    if len(production[1]) == 2:
                        left, right = production[1]
                        if left in table[i][k] and right in table[k + 1][j]:
                            table[i][j].add(production[0])

    return "S" in table[0][n - 1]

# Define a simple CFG grammar
grammar = [
    ("S", ["NP", "VP"]),
    ("NP", ["Det", "N"]),
    ("VP", ["V", "NP"]),
    ("Det", ["the"]),
    ("N", ["cat"]),
    ("V", ["chased"]),
]

user_sentence = input("Enter a sentence: ")

# Tokenize the user-provided sentence
sentence = user_sentence.split()


if cyk_parser(grammar, sentence):
    print("The sentence is syntactically valid.")
else:
    print("The sentence is not syntactically valid.")
