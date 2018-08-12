"""sco"""
def create_social_network(data):
    """net"""
    dict1 = {}
    def slomosplit(data):
        data = data.split(" follows ")
        if data[0] not in dict1:
            dict1[data[0]] = data[1].split(',')
        else:
            #print(data)
            dict1[data[0]] += data[1].split(',')
        return dict1
    splitline = data.splitlines()
    for i in splitline:
        slomosplit(i)
    return dict1


def main():
    """handling test cases"""
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'
    print(create_social_network(string))
if __name__ == "__main__":
    main()
s