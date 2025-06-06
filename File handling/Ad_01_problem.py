# Task:
# Write a function that takes a filename and returns:
# - Total number of lines
# - Total number of words
# - Total number of characters (excluding whitespaces)

# Example:
# lines: 10, words: 57, characters: 284
def Counter(filepath):
    lines = 0
    words = 0
    characters = 0
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            word_list = line.split()
            words += len(word_list)
            characters += sum(len(word) for word in word_list)
            lines += 1
    
    return lines, words, characters

lin, wor, char = Counter("File handling/censored.txt")

print(f"Lines: {lin}, Words: {wor}, characters: {char}")
