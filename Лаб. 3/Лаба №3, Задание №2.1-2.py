user_input = input("Введите текст, который вы хотите сохранить в файл: ")
with open('user_input.txt', 'w', encoding='utf-8') as file:
    file.write(user_input)
print("Текст успешно сохранён в файл user_input.txt.")
# 'w' - Задание 1
# 'a' - Задание 2

'''
a = open('user_input.txt', 'r', encoding='utf-8')
print(a.read())
a.close()
'''
