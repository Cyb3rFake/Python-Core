
Цель разработки: создании программы, контролирующей работу другой программы и прерывающей работу этой программы при превышении установленного лимита времени и препятствующей дальнейшей работе контролируемой программы в течении суток.
Разработанная программа должна:
1.	Запускаться автоматически при начале работы ОС;
2.	Проверять время работы определенной программы. Время работы контролируемой программы лимитируется в рамках суток (в новые сутки отсчет начинается сначала) с учетом пользователя. Для разных пользователей отработанное время считается отдельно;
3.	Суммарное время работы проверяемой программы под одним пользователем должно составлять 2 часа. Незначительные отклонения от этого лимита не критичны;
4.	Использование пользователем контролируемой программы не ограничено временем, только суммарной продолжительностью использования в рамках одних суток;
5.	Перезапуск контролируемой программы или ОС не должен влиять на учет времени работы контролируемой программы;
6.	В случае превышения суммарного времени использования контролируемой программы конкретным пользователем ему должно выводиться сообщение о принудительном закрытии программы через 10 минут.
7.	В случае однократной выдачи предупреждения о закрытии, в течении суток каждые 10 минут необходимо проверять работу контролируемой программы, и в случае ее использования прерываться без предупреждения.
