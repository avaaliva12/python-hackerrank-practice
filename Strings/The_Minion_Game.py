def minion_game(string):
    kevin = 0
    stuart = 0
    n = len(string)

    vowels = "AEIOU"

    for i in range(n):
        if string[i] in vowels:
            kevin += n - i
        else:
            stuart += n - i

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")

s = input().upper()
minion_game(s)