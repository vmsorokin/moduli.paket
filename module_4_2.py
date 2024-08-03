def test_function():
    def inner_function():
        a = 'Я в области видимости функции test_function'
        return a
    return (inner_function())
print(test_function())
#print(inner_function()) #Не видит функцию при глобальном вызове