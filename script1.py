print "Общество XXI века"
age = int(raw_input("Введите ваш возраст "))
if age >=0 and age <= 7:
     print "Вам в детсад"
elif age >=7 and age<=18:
     print "Вам в школу"
elif age >=18 and age<=24:
     print "Вам в ВУЗ"
elif age >=25 and age<=59:
     print "Вам на работу"
elif age >=60 and age<=119:
     print "Вам предоставляется выбор"
else:
     age >0 or age < 120
     print ("Error, это программа для людей")
print ("Cпасибо")
