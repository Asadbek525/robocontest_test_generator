# // input.txt → avtor bergan input
# // author.txt → avtor bergan output
# // code.txt → userning kodi
# // user.txt → user bergan output

ac = 0xAC
wa = 0xAD
pe = 0xAE
tl = 0xAF


a_in = open("input.txt", "r", encoding='utf-8').read()
a_out = open("author.txt", "r", encoding='utf-8').read()
u_out = open("user.txt", "r", encoding='utf-8').read()
u_code = open("code.txt", "r", encoding='utf-8').read()

if a_out == u_out:
    exit(ac)
a = a_out.replace('\r', '').split('\n')
b = u_out.replace('\r', '').split('\n')
n = len(a)
m = len(b)
# slice empty lines
while n > 0 and a[n - 1] == '':
    n -= 1
while m > 0 and b[m - 1] == '':
    m -= 1
a = a[:n]
b = b[:m]
if n != m:
    exit(wa)
for i in range(n):
    if a[i].lower() != b[i].lower():
        exit(wa)
exit(ac)
