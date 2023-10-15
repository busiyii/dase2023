def square_root_3(c):
    g = c/2
    i = 0
    while(abs(g*g - c)> 0.00000000001):
        g = (g + c/g)/2
        i = i+1
        print("%d:%.13f"%(i,g))

square_root_3(2)
square_root_3(2000)

'''
牛顿法中将g= c/2 改为 g = c或 g = c/4对结果有影响
'''