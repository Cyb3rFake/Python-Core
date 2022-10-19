"""
Вам предоставляется программа с двумя входами: один в качестве пароля, а второй в качестве повторения пароля. Завершите и вызовите данную функцию для вывода "Правильного", если пароль и повтор равны, и вывода "Неправильного", если они не равны.
"""
password = input()
repeat = input()

def validate(text1, text2):
	#your code goes here
    if text1==text2:
        print("correct")
    else:
        print("Wrong")
validate(password,repeat)