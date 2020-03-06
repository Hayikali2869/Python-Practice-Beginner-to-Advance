#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Let's begin with the classic Hello World
print("Hello, World")
print("你好，世界")
print("こんにちは世界"); print('Bonjour le monde')
print("안녕 세상");
print ("Hello, Python!")

# Single equal sign = is called an assignment operator

# n = 1+3 == n is assigned the value of 1 plus 3
# This assigns the value of 4 to n.
n = 0
n = 1 + 3
k = 4

# if-else statement
if k != n:
    print('no equal')
else:
    print('k is equal to n')

# Combination of while loop, bool and if-else
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
        print('loop started')
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
