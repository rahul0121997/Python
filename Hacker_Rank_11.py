def count_substring(string, sub_string):
    
    count = string.count(sub_string)
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    