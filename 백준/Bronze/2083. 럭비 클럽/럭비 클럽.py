while True:
    name, age, kg = input().split(' ')
    age = int(age)
    kg = int(kg)
    if name =='#' and age ==0 and kg == 0:
        break
    if age >17 or kg >=80:
        print(name + ' Senior')
    else:
        print(name + ' Junior')
