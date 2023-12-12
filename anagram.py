'''
anagram
input=good
output=gdoo
'''
def anagram(string1,string2):
    string1=sorted(string1)
    string2=sorted(string2)
    print(string1,string2)
    if string1 == string2:
        print("it is an anagram")
    else:
        print("not an anagram")
    return
string1='synergistic'
string2='serendipity'
result=anagram(string1,string2)


