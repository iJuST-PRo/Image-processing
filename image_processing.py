import sys, os


def flip_list(my_list):
    pass

def to_clean_list(file):
    as_list = []
    for line in file:
        as_list.append(line)
    clean_list = [q.replace('\n', ' ') for q in as_list]
    return clean_list

def longest_line(cln_lst):
    longest = max(len(long) for long in cln_lst)
    return longest



if __name__=='__main__':
    try:
        file_name=sys.argv[1]
    except:
        print(f'Error: file not specified\nUsage: python {os.path.basename(__file__)} file.txt')
        exit()

    with open(sys.argv[1]) as file:
        clean_list = to_clean_list(file.readlines())
        #print(list(file))


        longest = longest_line(clean_list)

        result = []
        for c,x in enumerate(clean_list):
            while len(x) < longest:
                x += " "
                clean_list[c] = x
                #print(gg[c])
        #print(gg)
        for x in range(longest):
            for y, z in enumerate(clean_list):
                print(z[x], sep='', end='')
                if y % longest == 0:
                    print('')
        print(result,end="\r")
    

    


