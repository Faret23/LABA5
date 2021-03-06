import re


def main():
    counter = 0
    pattern = re.compile(r'.*((08/Mar/2004:02:11:(3[7-9]|[3-5]\d|'
                         r'08/Mar/2004:02:2\d:\d\d|'
                         r'08/Mar/2004:(0[2-9]|2[0-3]):\d\d:\d\d|'
                         r'09/Mar/2004:\d\d:\d\d:\d\d|'
                         r'10/Mar/2004:18:41:([0-4]\d|5[0-2])|'
                         r'10/Mar/2004:18:([0-3]\d|4[0-1]):\d\d|'
                         r'10/Mar/2004:([0-1][0-8]):\d\d:\d\d)))'
                         r'.*200')


    
    with open('access.log', 'r') as file:
        contents = file.read()
        result = pattern.finditer(contents)
        for match in result:
            print(match.group(0))
            counter += 1
        print(counter)


if __name__ == "__main__":
    main()
