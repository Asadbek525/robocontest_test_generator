# // input.txt → avtor bergan input
# // author.txt → avtor bergan output
# // code.txt → userning kodi
# // user.txt → user bergan output

ac = 0xAC
wa = 0xAD
pe = 0xAE
tl = 0xAF

def check():
    a_in = open("input.txt", "r").read()
    a_out = open("author.txt", "r").read()
    u_ans = open("user.txt", "r").read()
    u_code = open("code.txt", "r").read()
check()
