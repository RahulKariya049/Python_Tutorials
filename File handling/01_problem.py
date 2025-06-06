#Finding a keyword in a file.......

def is_keyword_in_file(file , keyword):
    with open(file , "r") as f:
        lineno = 1
        appeared_at = []
        flag = False
        for line in f:
            if(keyword in line):
                flag = True
                appeared_at.append(lineno)
            lineno += 1
        print(f"keyword is appeared at these lines{appeared_at}")
    return flag

print(f"is the keyword \"program\" is in file intro.txt {is_keyword_in_file("intro.txt" , "program")}")

#Advanced keyword search
# def is_keyword_in_file(filepath, keyword, ignore_case=True):
#     keyword = keyword.lower() if ignore_case else keyword

#     with open(filepath, "r", encoding="utf-8") as f:
#         for line in f:
#             check_line = line.lower() if ignore_case else line
#             if keyword in check_line:
#                 return True
#     return False
