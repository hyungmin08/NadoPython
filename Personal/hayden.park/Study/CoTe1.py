from cv2 import ellipse


def solution(x, y, z):
    pos = 0
    if abs(x-y)>z:
        pos = -1
    else:
        if x==y:
            pos = x + z//2
        elif x>y:
            pos = x + (z-(x-y))//2
        else:
            pos = y + (z-(y-x))//2

    return pos

if __name__=='__main__':
    fptr = open(os.environ['OUTPUT_PATH'],'w')

    x = int(input().strip())
    y = int(input().strip())
    z = int(input().strip())

    result = solution(x,y,z)
    fptr.write(str(result) + '\n')
    fptr.close()
