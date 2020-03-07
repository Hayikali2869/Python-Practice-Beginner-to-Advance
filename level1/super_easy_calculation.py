#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Let's begin with the classic Hello World
print("Hello, World")
print("你好，世界")
print("こんにちは世界"); print('Bonjour le monde')
print("안녕 세상");
print("Hello, Python!")

# Single equal sign = is called an assignment operator

# n = 1+3 == n is assigned the value of 1 plus 3
# This assigns the value of 4 to n.
n = 0
n = 1 + 3
k = 4

# Division operators (/,//)
x = 6.4 // 2
y = 6.5 // 2
z = -6.7 // 2
m = -6.4 // 2
print("Division:", x, y, z, m)
print()

# Exponent operator **
# x**y = x^y = 27
print("x**y = ",x**y)
print()
# Modulo operator %
print("4 % 2 = ", k % 2)
print("-4 % 2 = ", m % 2)
print("5 % 2 = ", 5 % 2)
print()

# Bool operations
print("Bool operations:")
print(n>5)
print(n>=4)
print(n>=4 and n<8)
print(n>=4 or n>5)
print(not n==4 or n>5)
print(not n==4 or n<5)
print(not n==4 and n>5)
print()

# A easy if-else statement
if k != n:
    print('no equal')
else:
    print('k is equal to n')

raining = True
highUV = True
if raining or highUV:
    print('Take an umbrella!!!')

cold = True
rain = False
if raining and highUV:
    print('You are good to go.')

# Make it to a single line
mark = 99
print('High Distinction') if mark >= 85 else print('Other Grade')
print()


# A easy way to understant while loop
# 从前有座山，山里有座庙，庙里有个老和尚，老和尚给小和尚讲故事
# 从前有座山，山里有座庙，庙里有个老和尚，老和尚给小和尚讲故事...
# A long long ago, on a mountain was a temple that housed an
# old monk. The old monk telling a story for the young monk.
# The story is:
# A long long ago, on a mountain was a temple that housed an
# old monk. The old monk telling a story for the young monk.
# The story continuous forever.

# Combination of while loop, bool and if-elif-else
# While loop will break when a == 0
a = 3
name = 'luka'
flag = False
while a > 0:
    if a == 1:
        name = 'python'
        flag = True
        print()
        print('Level Up, see u in next level :-) ')
    elif a == 3:
        height = 5
        weight = 10
        area = height*weight
        print("Area of 5*10 is ", area)
        print()
    else:

        print(""" 
                      _..-'(                       )`-.._
                   ./'. '||\\.       (\_/)       .//||` .`\.
                ./'.|'.'||||\\|..    )O O(    ..|//||||`.`|.`\.
             ./'..|'.|| |||||\`````` '`"'` ''''''/||||| ||.`|..`\.
           ./'.||'.|||| ||||||||||||.     .|||||||||||| |||||.`||.`\.
          /'|||'.|||||| ||||||||||||{     }|||||||||||| ||||||.`|||`\
         '.|||'.||||||| ||||||||||||{     }|||||||||||| |||||||.`|||.`
        '.||| ||||||||| |/'   ``\||``     ''||/''   `\| ||||||||| |||.`
        |/' \./'     `\./         \!|\   /|!/         \./'     `\./ `\|
        V    V         V          }' `\ /' `{          V         V    V
        `    `         `               V               '         '    '

            Vivian Aldridge
        ------------------------------------------------
        Thank you for visiting https://asciiart.website/
        This ASCII pic can be found at
        https://asciiart.website//index.php?art=animals/bats
        """)

    a -= 1

