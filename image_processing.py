
def flip_list(lst):
    if not lst:
        return lst

    is_vertical = isinstance(lst[0], list)
    
    if is_vertical:
        return [el[0] for el in lst]
    x = [[el] for el in lst]

    return x


if __name__=='__main__':
    with open('input.txt') as my_file:
        file_to_list = []
        for line in my_file:
            file_to_list.append(line)
        g = flip_list(file_to_list)
        gg = [q[0].replace('\n', ' ') for c,q in enumerate(g) ]
        #print(gg)
        ss = []
        longest = max(len(long) for long in gg )#for x in long)
        #print(longest)
        for c,x in enumerate(gg):
            while len(x) < longest:
                x += " "
                gg[c] = x
                #print(gg[c])
        #print(gg)
        for x in range(longest):
            for y, z in enumerate(gg):
                print(z[x], sep='', end='')
                if y % longest == 0:
                    print('')
        print(ss,end="\r")


