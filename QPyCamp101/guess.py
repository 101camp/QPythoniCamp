# -*- coding: utf-8 -*-
from random import uniform
myNumber = int(uniform(2,99))
noGuess = 1
while noGuess:
    urNumber = int(input('猜个1~99的数字? --> '))
    if urNumber < myNumber: print("...(~_~)小了")
    elif urNumber > myNumber: print("......大了(^_-")
    else:
        print("猜对了\(^o^)/下次再来玩!")
        break

```
从 random 导入 uniform
我的数字 = 整数(uniform(2,99))
没猜中 = 真
当 没猜中:
    你猜 = 整数(输入('猜个1~99的数字? --> '))
    如果 你猜 < 我的数字: 打印  "...(~_~)小了"
    假使 你猜 > 我的数字: 打印  "......大了(^_-"
    否则:
        打印  "猜对了\(^o^)/下次再来玩!"
        中断
```