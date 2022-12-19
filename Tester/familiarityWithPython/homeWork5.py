print("Напишите программу, удаляющую из текста все слова, содержащие 'абв'. \
В тексте используется разделитель пробел.")

txt = input("Enter text: ")
#txt = 'абв кабв абвк кабвк бва www'
txt = txt.split(" ")
txt = list(filter(lambda x: x.find('абв')<0 , txt))
print((' ').join(txt))

print()
