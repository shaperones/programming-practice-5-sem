### Какое количество процессов имеет смысл создавать в программе для параллельной работы?
Не более, чем `mp.cpu_count() - 1`. 1 ядро закладывается на оперативку и
текущий процесс. При большем числе процессов наступает 
конкурентность
### Какие проблемы могут возникнуть при записи результатов работы разных процессов в один файл (или печати в консоль)
Процессы выполняются слегка с разной скоростью и зачастую 
очень быстро, что:
1) мешает функциям вывода типа `print()` справляться с 
разделением вывода от разных процессов
2) в принципе не отражает очередность начала 
процессов в записи
### Каким должно быть отношение времени выполнения различных параллельных процессов?
Примерно равным
### Какие особенности работы функции `Pool.map()`?
`mp.Pool(n)` - бригада из n рабочих, `map(work, data)` 
принимает итерируемый объект и возвращает итератор, 
применяющий work к data. Таким образом, 
`Pool.map(work, data)` принимает итерируемый объект 
data и раздает его по рабочим (процессам) для выполнения
некой work. При этом позволяет сохранить в выводе 
результатов очередность вызова