# for num in range(1, 100):
#     answer = 'hopwiz' if num % 15 else 'hope' if num % 3 else 'wiz' if num % 5 else str(num)
#     print(answer)


# if <condition> # bool(condition)
# 1 - 15 ---> num % 15  => 1 - 14 , 0
# bool(num % 15)

# def check_user_input():
#     <....>
#     if user_input --> correct:
#         return True
#     return False
#
# flag = True
#
# while True:
#     <......>
#     while True:
#
#         if not count - userInput:
#             break
#         if inp.lower() in ['q', 'quit']:
#             flag = False
#             break
#     if not flag:
#         break
#     if inp.lower() in ['n', 'no']:
#         break


alphabetString='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(alphabetString[::-1])
print('*'*40)
print(alphabetString[27::-1])
print(alphabetString[27:0:-1])

# -------------------------------

print(alphabetString[-1: -(len(alphabetString)+1): -1])


