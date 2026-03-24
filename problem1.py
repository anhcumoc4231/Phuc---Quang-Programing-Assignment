def next_s(s):
    chars = list(s)
    n = len(chars)
    
    for i in range(n-1,-1,-1):
        if chars[i] == 'a':
            chars[i] = 'b'
            break
        elif chars[i] == 'b':
            chars[i] = 'c'
            break
        else:
            chars[i] = 'a'
    res = ''.join(chars)
    if(res == 'a' * n): 
        res = 'a' + res
    return res

def previous_s(s):
    chars = list(s)
    n = len(chars)
    
    for i in range(n-1, -1, -1):
        if chars[i] == 'c':
            chars[i] = 'b'
            break
        elif chars[i] == 'b':
            chars[i] = 'a'
            break
        else:
            chars[i] = 'c'
    res = ''.join(chars)
    if s == 'a' * n:
        if n > 1:
            res = 'c' * (n - 1)
        else:
            res = "" 
    return res

def count_behind(s):
    count = 0
    for char in s:
        count = count * 3
        if char == 'a':
            count += 2
        elif char == 'b':
            count += 1
    return count

def count_contains_ab(n, s):
    if s != "ab":
        return -1
    if n < 2:
        return 0  
    end_a = 1      
    not_a = 2      
    for i in range(2, n + 1):
        new_end_a = end_a + not_a
        new_not_a = (end_a + not_a) + not_a 
        end_a = new_end_a
        not_a = new_not_a 
    total_without_ab = end_a + not_a
    total_strings = 1
    for _ in range(n):
        total_strings *= 3
    return total_strings - total_without_ab

def main():
    print("=================== PROBLEM 1 BẮT ĐẦU ===================")
    
    t_case1 = 'abca'
    t_case2 = 'aacc'
    t_case3 = 'cc'
    
    print("--- Câu 1.1: Hàm next(s) ---")
    print(f'Test case 1: next({t_case1}) = {next_s(t_case1)}')
    print(f'Test case 2: next({t_case2}) = {next_s(t_case2)}')
    print(f'Test case 3: next({t_case3}) = {next_s(t_case3)}')
    
    print("\n--- Câu 1.2: Hàm previous(s) ---")
    print(f'Test case 1: previous({t_case1}) = {previous_s(t_case1)}')
    print(f'Test case 2: previous({t_case2}) = {previous_s(t_case2)}')
    print(f'Test case 3: previous({t_case3}) = {previous_s(t_case3)}')

    print("\n--- Câu 1.3: Đếm số chuỗi cùng độ dài đứng sau s ---")
    t_behind1 = 'aab'
    t_behind2 = 'ccc'
    print(f'Test case 1: count_behind({t_behind1}) = {count_behind(t_behind1)}')
    print(f'Test case 2: count_behind({t_behind2}) = {count_behind(t_behind2)}')

    print("\n--- Câu 1.4: Đếm số chuỗi chứa 'ab' ---")
    print(f'Test case 1 (n=2, s="ab"): count_contains_ab = {count_contains_ab(2, "ab")}')
    print(f'Test case 2 (n=4, s="ab"): count_contains_ab = {count_contains_ab(4, "ab")}')

if __name__ == "__main__":
    main()