import sys, os


def to_clean_list(file):
    as_list = []
    for line in file:
        as_list.append(line)
    clean_list = [q.replace('\n', ' ') for q in as_list]
    return clean_list

def longest_line(cln_lst):
    longest = max(len(long) for long in cln_lst)
    return longest

def add_spaces(clean_list, longest):
    equal_list = []
    for c,x in enumerate(clean_list):
        while len(x) < longest:
            x += " "
        equal_list.append(x)
    return equal_list    

def horizontal_to_vertical(longest, equal_length):
    result = []
    for x in range(longest):
        for y, z in enumerate(equal_length):
            result.append(z[x])
            if not y % longest:
                if not x and not y:
                    continue
                else:
                    result.append('\n')
    return result

def rotate(file):
    clean_list = to_clean_list(file.readlines())
    longest = longest_line(clean_list)
    equal_length = add_spaces(clean_list,longest)           
    result = horizontal_to_vertical(longest, equal_length)
    return result


if __name__=='__main__':
    try:
        file_name=sys.argv[1]
    except:
        print(f'Error: file not specified\nUsage: python {os.path.basename(__file__)} file.txt')
        exit()
    with open("output.txt", "w") as output:
        with open(sys.argv[1]) as file:
            result = rotate(file)
        
        output.writelines(result)
        print('Done, Check output.txt')
        
