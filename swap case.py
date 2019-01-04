def swap_case(s):
    ls = s.split()
    res = []
    for i in ls:
        i.split
        for j in i:
            j.split()
            for k in j:
                if(k.isupper()):
                    l = k.lower()
                    res.append(l)
                elif(k.islower()):
                    u = k.upper()
                    res.append(u)
                else:
                    res.append(k)
        res.append(" ")
    fin = ''.join(map(str, res)) 
    return fin

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)