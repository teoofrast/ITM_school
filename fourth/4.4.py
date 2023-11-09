def sortalpha():
    spisok = ["a", "s", "1", "a", "32", "23"]
    bukvy = [i for i in spisok if i.isalpha()]
    bukvy.pop()
    bukvy.reverse()
    return bukvy


print(sortalpha())