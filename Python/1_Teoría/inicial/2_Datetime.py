import datetime

#estas sentencias son las que me fallaron
#porque se me olvidó poner el now()
print("¿qué día es?")
print(datetime.datetime.now().date())

print("¿qué hora es?")
print(datetime.datetime.now().time())