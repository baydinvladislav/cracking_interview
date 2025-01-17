<h2>Bottom-Up Algorithms</h2>

Использование Bottom-Up алгоритма, это способ избежать рекурсии, сохраняя затраты памяти, которые несет рекурсия, 
когда она создает стек вызовов.

Проще говоря, Bottom-Up алгоритм начинает работу с начала, в то время как рекурсивный алгоритм начинает работу с конца 
и работает в обратном направлении.

Например, если мы хотим умножить все числа в диапазоне 1...n, мы могли бы использовать такой однострочный рекурсивный 
Top-Down алгоритм:

```python
def product_1_to_n(n):
    # We assume n >= 1
    return n * product_1_to_n(n - 1) if n > 1 else 1
```

Такой способ имеет проблему: это построит стэк вызовов размером O(n), 
который обойдется нам как общее O(n) пространственной сложности для всего нашего алгоритма. Это сделает его уязвимым
для ошибки переполнения стэка (stack overflow), когда стэк становится слишком большим и ему не хватает места.

Чтобы избежать подобных проблем, мы можем использовать Bottom-Up алгоритм:
```python
def product_1_to_n(n):
    # We assume n >= 1
    result = 1
    for num in range(1, n + 1):
        result *= num
    
    return result
```

Временная сложность этого алгоритма: O(n) 
Пространственная сложность этого алгоритма: O(1)

Bottom-Up - это распространенная стратегия для задач на динамическое программирование, которые представляют собой задачи,
решение которых состоит из решений той же задачи с меньшими входными данными, как, например, в примере с умножением чисел.
Другая распространенная стратегия для задач на динамическое программирование - это мемоизация.
