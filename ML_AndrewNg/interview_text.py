def betterCompression(s):

    s = list(s)
    # Write your code here
    array = []
    i = 0

    while i < len(s) - 1:
        if s[i].isalpha() and s[i] not in array:
            array.append(s[i])
            continue
        elif s[i].isalpha() and s[i] in array:
            add_num = s[i+1]
            index = s.index(s[i])
            s[index+1] = s[index+1] + add_num
        elif s[i+1].isdigit() and s[i].isdigit():
            print(f's[{i}] = {s[i]}')
            print(f's[{i+1}] = {s[i+1]}')
            num = int(s[i]) * 10 + int(s[i+1])
            array.append(num)
            i += 1
        i += 1

    print(f"array = {array}")
    return array

input = "a12c56a1b5"
betterCompression(input)