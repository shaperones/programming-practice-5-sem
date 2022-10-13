### Как можно описать отношения родительского и дочернего классов?
Дочерний класс наследует методы и классовые переменные 
родителя, но также может иметь свои, не присутствующие 
у родителя.
### Каким образом работает обращение к методу через super()?
`super()` позволяет обратиться к методу предка в каком-то
колене. Причем поиск вызываемого метода будет осуществляться
как обход графа в ширину (если есть 
`class Derived(Base1, Base2)`, то сначала поиск запустится
в первом родителе, потом во втором, потом в их родителях)
### Зачем нужна обработка исключений? В каких случаях ее использование некорректно?
Обработка исключений нужна для отлавливания ошибок 
пользователя, чтобы даже при некорректном взаимодействии
с интерфейсом программа не падала. Это замедляет 
выполнение кода, so использование исключений в местах,
 где пользователь не взаимодействует с программой 
и мы не ожидаем ошибок от последствий его
взаимодействия, считается некорректным.
### Что нужно сделать, чтобы реализовать свое собственное исключение?
Наследовать класс твоего исключения от Класса Исключений!
   
    class MyError(Exception):
        pass
    ...
    raise MyError("ваше пояснение")