

def split_and_join(line):
    word = line.split(" ")
    result = "-".join(word)
    return result


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)