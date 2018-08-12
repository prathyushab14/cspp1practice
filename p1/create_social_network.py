"""sco"""
def create_social_network(data):
    """net"""
    data = data.split(" follows ")
    dict1 = {}
    def sns(data)
    data = data.split(" follows ")
    if i not in dict1:
        dict1[data[0]] = data[1].split(",")
    else:
        dict1[data[0]] += data[1].split(",")
return dict1
splitline = data.splitlines()
for i in splitline:
    sns(i)
print(dict1)
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
