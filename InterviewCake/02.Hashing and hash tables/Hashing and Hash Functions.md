<h2>Хэширование и хэш функции</h2>

Хэш функция принимает данные (например, строку или контент файла) и возвращает хэш, строку фиксированного размера,
содержащая символы или числа.

Для примера это хэш MD5 (известная хэш функция) для файла, содержащим строку "cake":
```
DF7CE038E2FA96EDF39206F898DF134D
```

а это хэш для строки "cakes":
```
0E9091167610558FDAE6F69BD6716771
```

Обратите внимание, что хэш совершенно другой, хотя строки очень похожи, также взглянем на хэш от длинного фильма:
```
664f67364296d08f31aec6fea4e9b83f
```

Этот хэш имеет такую же длину, как и предыдущие 2 хэша, но в этот раз файл значительно больше.

Мы можем думать про хэш, как про отпечаток пальцев у людей. Мы можем быть уверены, что один и тот же файл, 
всегда будет давать один и тот же хэш, но мы не можем из хэша получить оригинальный файл.

Иногда может случаться так, что несколько файлов могут предоставить один и тот же хэш, это называется хэш коллизией.

Некоторые варианты использования хэширования:
1. Словари. Предположим, что мы хотим массиво-подобную структуру данных с доступом к элементу за О(1),
но мы хотим хранить под значениями тоже какие то нужные нам данные, а не только стандартные индексы массива.
Для этого мы можем выделить массив и создать хэш функцию, которая будет переводить ключи в индексы массива.
2. Предовращение атак "человек по середине". Вы когда-нибудь замечали, что на сайтах загрузки написано «hash», «md5» или «sha1»?
Сайт говорит вам, что он имеет хэш от файла, который вы будете скачивать, после скачивания, вы тоже можете сделать хэш файла и
убедиться, в том, что вы получили тот же самый файл, и никакой злоумышленник не смог его подменить во время скачивания.
