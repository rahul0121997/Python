def solution(text, ending):
    if text.endswith(ending):
        return True
    else:
        return False
    
print(solution('abcd', 'ab'))