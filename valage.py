def valid_age(age):
    if age <18:
        return "Exceed"
    if age>=18 and age<=60:
        return "eligible"
    if age>60:
        return "age limit exceed"