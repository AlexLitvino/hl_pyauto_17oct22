"""
Реализовать класс Pixel. Конструктор должен принимать три компоненты - красная, зеленая и голубая.
Это целые числа в диапазоне [0, 255] (включительно).
При попытке создать объект с компонентами не из этого диапазова должно выбрасываться исключение ValueError
Компоненты должны быть приватными полями.
Класс Pixel должен поддерживать перегрузку оператора +, - *, /, == и переопределять методы __str__ и __repr__ (возвращая строку с вызовом конструктора).

Оператор +(-) позволяет сложить (вычесть) два объекта класса Pixel.
В результате сложения (вычитания) должен возвращаться новый объект класса Pixel с компонентами равными сумме (разности) исходных объектов.

Оператор * (/) позволяет умножить (разделить) объект класса Pixel на число типа int или float больше 0.
В результате умножения должен возвращаться новый объекта класса Pixel с компонентами равными произведению (частному) компонент исходного объекта на число.
При попытке умножить (разделить) не на числа типа int или float должно выбрасываться исключение TypeError.
При попытке умножить (разделить) на число ноль или меньше нуля должно выбрасываться исключение ValueError.
Если при умножении (делении) компоненты на число получилось дробное число, дробную часть надо отброчить.

Если в результате применения операторов, какая-то компонента будет меньше 0, ее необходимо установить в 0.
Если в результате применения операторов, какая-то компонента будет больше 255, ее необходимо установить в 255.

Два объекта с равными компонентами считаются равными
"""