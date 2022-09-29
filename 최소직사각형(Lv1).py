def solution(sizes):
    max_width = 0
    max_height = 0
    for size in sizes:
        size.sort()
    for size in sizes:
        for index,i in enumerate(size):
            if index == 0:
                if max_width < i:
                    max_width = i
            else:
                if max_height < i:
                    max_height = i
                    
    return max_width * max_height