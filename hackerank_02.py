if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    score = sorted(set(arr), reverse=True)[1] # you can also do it without using reverse, score = true sorted(set(arr))[-1]
    print(score)