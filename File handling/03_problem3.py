#Censoring lists of word in a file..
import os

bad_word = "fool"
def censor_words(file, C_list):
    with open(file, "r", encoding="utf-8") as reader, open("temp.txt", "w", encoding="utf-8") as writer:
        for line in reader:
            words = line.split()
            new_words = []
            for word in words:
                if word.lower() in C_list:
                    censored = word[0] + "*" * (len(word) - 1)
                    new_words.append(censored)
                else:
                    new_words.append(word)
            writer.write(" ".join(new_words) + "\n")

    #Now replace original file with the modified one
    os.replace("temp.txt", file)




censored_words = ["fool", "gadha", "jhat", "gandu", "lodu"]
censor_words("censored.txt",censored_words)