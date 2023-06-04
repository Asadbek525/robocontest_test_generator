# input.txt → avtor bergan input
# author.txt → avtor bergan output
# code.txt → userning kodi
# user.txt → user bergan output

ac = 0xAC
wa = 0xAD
pe = 0xAE
tl = 0xAF

author_input = open("input.txt", "r")
author_output = open("author.txt", "r")
user_output = open("user.txt", "r")
user_code = open("code.txt", "r")


def close(x):
    author_input.close()
    author_output.close()
    user_output.close()
    user_code.close()
    exit(x)


def main():
    # a + b misol uchun checker
    try:
        ans = int(author_output.readline())
        user_ans = int(user_output.readline())

        # user javob sifatida 1 tadan ortiq son chiqargan taqdirda
        if user_output.readline():
            close(pe)

        if ans == user_ans:
            close(ac)
        else:
            close(wa)
    except:
        close(pe)


if __name__ == "__main__":
    main()
