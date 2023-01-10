# def solution(box):
#     count = 0
#     flag = True
#     q = sum(box)//len(box)
#     r = sum(box)%len(box)
#     if r >0:
#         avg = q + 1
#     else:
#         avg = q

#     while flag:
#         idx = box.index(max(box))
#         if idx == 0:
#             count = box[idx]
#             flag = False
#         else:
            
#             temp = avg * idx - sum(box[:idx])
#             print(sum(box[:idx]))
#             box[idx] = box[idx] - temp
#             box[idx-1] = box[idx-1] + temp
#             max_item = max(box)
#             min_item = min(box)        
#             print(box)
#             if max_item - min_item <=1 :
#                 count = max_item
#                 flag = False
            
#     return count

# box_count = int(input().strip())
# box = []

# for _ in range(box_count):
#     box_item = int(input().strip())
#     box.append(box_item)

# result = solution(box)

# print(result)
