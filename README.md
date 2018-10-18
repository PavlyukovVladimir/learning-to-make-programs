<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <base href="https://github.com/PavlyukovVladimir/learning-to-make-programs/blob/master/" ></base>
</head>
<body>

  # learning to make programs
  
  ## Навигация <a name="navigation"></a>
  
  <p><a href="#spiral_matrix">1. Заполнение произвольной матрицы по спирали.</a></p>
  
  <p><a href="#quick_sorting">2. Быстрая сортировка с произвольной функцией сравнения.</a></p>
  
  ## 1. Заполнение произвольной матрицы по спирали. <a name="spiral_matrix"></a>
  
  <p><B>Нужно средствами какого-нибудь языка программирования заполнять произвольную матрицу по спирали во внутрь начиная с первого элемента по часовой стрелке.</B></p>
  <p>За не имением особых препочтений или требований языком программирования для решения задач выбираю Python, потому,что хочу потренироваться писать программы с его помощью.</p>
  <p>В условии задачи не сказанно чем заполнять, откуда брать элементы, какого они типа...</p>
  <p>Возможно следует создать нечто, что будет последовательно выдавать элементы для заполнения. Напрашивается метод get_element() он будет генератором элементов для заполнения матрицы.</p>
  <p>Матрицу нужно гдето хранить, в какойто структуре... Так как природа элементов заранее не ясна, логично хранить строки матрицы как списки, а саму матрицу, как список списков</p>
  <p>Информацию о размерах матрицы нужно получать от пользователя или иным способом, отнесем это к отдельному методу, чтобы иметь возможность модификации под меняющиеся варианты ввода, назовем метод get_sises(), пусть он возвращает кортеж (row_count,columns_count)</p>
  <p>Итак есть генератор элементов, есть размеры матрицы, теперь нужно ее заполнить. Вот бы был некий метод, который зная куда был вставлен предыдущий элемент, выдавал координаты следующего...</p>
<p>Вообще способов заполнения матрицы может быть множество, оставим себе гибкость, пусть будет метод create_matrix(dimentions,generator,change_status=change_status_for_spiral), который примет размеры матрицы, генератор элементов и функцию перехода от статуса к статусу, а вернет заполненную матрицу.</p>
<p>Хорошо бы теперь эту матрицу пользователю показать, сделаем метод print_matrix(Matrix) который получив матрицу, выводит ее на печать.</p>
<p>Программа будет выглядеть как вызов одного метода:</p>
<p>print_matrix(create_matrix(get_sises(),get_element))</p>

<p>Листинг скрипта на Python в jupiter реализующий заполнение 10 матриц случайных размерностей по спирали целыми числами начиная с 0:<a href='https://github.com/PavlyukovVladimir/learning-to-make-programs/blob/master/spiral_matrix.ipynb'>spiral_matrix.ipynb</a></p>

```Python
def get_element(maximum):
    """Выдает числа от 0 до maximum"""
    maximum-=1
    number=0
    yield number
    
    while number<maximum:
        next=number+1
        yield next
        number=next
```

```Python
def get_sises():
    """Возвращает кортеж (число строк матрицы, число столбцов матрицы), запрашивая числа у пользователя"""
    rows_count=int(input("Введите число строк матрицы m: "))
    columns_count=int(input("Введите число столбцов матрицы n: "))
    return (rows_count,columns_count)
```

```Python
def change_status_for_spiral(state):
    """Получает состояние на текущем шаге (координаты coordinates(row,col),границы border(left,top,right,bottom),
    направление движения direction{"right", "down", "left", "up"}), вернет на следующем"""
    (row,col)=state[0]
    (left,top,right,bottom)=state[1]
    direction=state[2]
    if direction=='r':#"right"
        if col<right:
            col+=1
        elif col==right:
            direction='d'#"down"
            top+=1
            row+=1
        return ((row,col), (left,top,right,bottom), direction)
    if direction=='d':#"down":
        if row<bottom:
            row+=1
        elif row==bottom:
            direction='l'#"left"
            right-=1
            col-=1
        return ((row,col), (left,top,right,bottom), direction)
    if direction=='l':#"left":
        if col>left:
            col-=1
        elif col==left:
            direction='u'#"up"
            bottom-=1
            row-=1
        return ((row,col), (left,top,right,bottom), direction)
    if direction=='u':#"up":
        if row>top:
            row-=1
        elif row==top:
            direction='r'#"right"
            left+=1
            col+=1
        return ((row,col), (left,top,right,bottom), direction)
    return 0
```

```Python
def create_matrix(dimentions,generator,change_status=change_status_for_spiral):
    """По размерам матрицы dimentions создаст ее и заполнит в очередности регулируемой change_status, получая элементы из generator"""
    rows_count=dimentions[0]
    columns_count=dimentions[1]
    ((row,col), (left,top,right,bottom), direction) = ((0,0), (0,0,columns_count-1,rows_count-1), 'r')
    Matrix = [[0 for j in range(columns_count)] for i in range(rows_count)]
    gen=generator(rows_count * columns_count)
    
    for i in gen:
        Matrix[row][col]=i
        ((row,col), (left,top,right,bottom), direction) = change_status(((row,col), (left,top,right,bottom), direction))
    return Matrix
```

```Python
import math
def print_matrix(Matrix,separator=' ',left_border='',right_border=''):
    """Распечатывает прямоугольные матрицы с числовыми данными"""
    row=len(Matrix)#количество строк
    col_counts=list(map(len,Matrix))#количества элементов в строках
    
    el_Matrix_lengths=[[0 for i in range(row)] for j in range(max(col_counts))]#транспонированная матрица
    for i in range(row):#вычисляем сколько символов нужно для записи каждого элемента
        for j in range(col_counts[i]):
            el_Matrix_lengths[j][i]=len(str(Matrix[i][j]))
            
    el_Matrix_lengths=list(map(lambda x: str(max(x)),el_Matrix_lengths))
    #получаем список максимальных длин элементов в столбцах Matrix
    #числа сразу преобразованы в строки
    for i in range(row):
        print(left_border,end='')
        for j in range(col_counts[i]-1):#печать элементов строки матрицы кроме последнего в одной строке
            print((("%"+el_Matrix_lengths[j]+"d") % Matrix[i][j])+separator,end='')
        print((("%"+el_Matrix_lengths[col_counts[i]-1]+"d") % Matrix[i][col_counts[i]-1])+right_border)
```

```Python
#напечатаем десяток матриц со случайными размерами в пределах от 1 до 10
import random
n= 10
print(str(1)+':')
print_matrix(create_matrix(get_sises_2arg(random.randint(1, 10),random.randint(1, 10)),get_element),' ','   ')

for i in range(1,n):
    print(str(i+1)+':')
    print_matrix(create_matrix(get_sises_2arg(random.randint(1, 10),random.randint(1, 10)),get_element),' ','   ')
```

```
1:
    0  1  2  3  4  5  6
   25 26 27 28 29 30  7
   24 43 44 45 46 31  8
   23 42 53 54 47 32  9
   22 41 52 55 48 33 10
   21 40 51 50 49 34 11
   20 39 38 37 36 35 12
   19 18 17 16 15 14 13
2:
    0  1  2  3  4  5
   23 24 25 26 27  6
   22 39 40 41 28  7
   21 38 47 42 29  8
   20 37 46 43 30  9
   19 36 45 44 31 10
   18 35 34 33 32 11
   17 16 15 14 13 12
3:
   0
   1
   2
   3
   4
   5
   6
   7
   8
4:
    0  1  2  3  4  5  6  7  8  9
   23 24 25 26 27 28 29 30 31 10
   22 39 38 37 36 35 34 33 32 11
   21 20 19 18 17 16 15 14 13 12
5:
    0  1  2  3  4 5
   13 14 15 16 17 6
   12 11 10  9  8 7
6:
   0 1 2 3 4 5 6 7 8
7:
    0  1 2
   17 18 3
   16 19 4
   15 20 5
   14 21 6
   13 22 7
   12 23 8
   11 10 9
8:
    0  1  2  3  4  5
   25 26 27 28 29  6
   24 43 44 45 30  7
   23 42 53 46 31  8
   22 41 52 47 32  9
   21 40 51 48 33 10
   20 39 50 49 34 11
   19 38 37 36 35 12
   18 17 16 15 14 13
9:
    0  1
   19  2
   18  3
   17  4
   16  5
   15  6
   14  7
   13  8
   12  9
   11 10
10:
    0  1  2
   21 22  3
   20 23  4
   19 24  5
   18 25  6
   17 26  7
   16 27  8
   15 28  9
   14 29 10
   13 12 11
```

<p>Альтернативное решение, с использованием 4х специализированных функций, которые отвечают за заполнение одного направления от границы до границы  и по очереди вызывают друг друга:</p>

```Python
#функции заполнения
#matr список списков представляющий собой матрицу
#j число с которого нужно заполнять
#l левая граница
#r правая граница
#b нижняя граница
#t верхняя граница
def lr(matr,j,l,r,b,t):
    "Заполняет вправо, самый верхний ряд и вызывает заполнение вниз"
    if(l<=r):#проверка на заполненность
        for i in range(l,r+1):
            matr[t][i]=j
            j+=1
        tb(matr,j,l,r,b,t+1)
    return

def tb(matr,j,l,r,b,t):
    "Заполняет вниз, самый правый столбец и вызывает заполнение влево"
    if(b>=t):#проверка на заполненность
        for i in range(t,b+1):
            matr[i][r]=j
            j+=1
        rl(matr,j,l,r-1,b,t)
    return

def rl(matr,j,l,r,b,t):
    "Заполняет влево самый нижний ряд и вызывает заполнение вверх"
    if(l<=r):#проверка на заполненность
        for i in range(r,l-1,-1):
            matr[b][i]=j
            j+=1
        bt(matr,j,l,r,b-1,t)
    return

def bt(matr,j,l,r,b,t):
    "Заполняет вверх самый первый столбец и вызывает заполнение вправо"
    if(b>=t):#проверка на заполненность
        for i in range(b,t-1,-1):
            matr[i][l]=j
            j+=1
        lr(matr,j,l+1,r,b,t)
    return
#ввод данных
m=int(input("Введите число строк матрицы m: "))
n=int(input("Введите число столбцов матрицы n: "))
print("Матрица содержит ",m*n, " элементов.")
matr=[[0 for i in range(n)] for i in range(m)]#создание матрицы m x n в виде m списков списков по n нулей

#заполнить matr возрастающими числами начиная с 0 с шагом 1
#заполнять инклюзивную прямоугольную область с границами по горизонтали от 0 до n-1
#по вертикали от 0 до m-1
lr(matr,0,0,n-1,m-1,0)

import math
#print(matr)
l=math.ceil(math.log(m*n,10))+1#максимальная длинна записи плюс 1
for i in range(m):
    s=""
    for j in range(n):
        s+=str(matr[i][j]).rjust(l," ")#Позиционирует вправо указанную строку, дополняя её слева до указанной длины указанным символом.
    print(s)
```

'''
Введите число строк матрицы m: 4
Введите число столбцов матрицы n: 6
Матрица содержит  24  элементов.
  0  1  2  3  4  5
 15 16 17 18 19  6
 14 23 22 21 20  7
 13 12 11 10  9  8
'''

<p><a href="#navigation">Вверх к Содержанию</a></p>

  ## 2. Быстрая сортировка с произвольной функцией сравнения. <a name="quick_sorting"></a>
  
  <p><B>Реализовать функцию быстрой сортировки с произвольной функцией сравнения</B></p>
  <p>Сортировать будем список, так как он может хранить элементы любой природы.</p>
  <p>Принципиально не имеет значения будет ли функция сравнения отвечать больше ли первый элемент второго или меньше, но для определенности пусть функция возвращает true если ее первый аргумент меньше второго и false в остальных случаях.</p>
  <p>Чтобы проверить меньше ли второй аргумент первого, достаточно просто поменять их местами.</p>
  <p>Будем считать однопорядковыми элементы которые не больше и не меньше друг друга.</p>
  <p>Реализуем функцию быстрой сортировки которая берет случайный элемент списка и разделяет все элементы на три списка в первом все элементы меньше выбранного, во втором все однопорядковые с ним, в третьем все больше него, затем соберем их в один список предварительно рекурсивно применив эту функцию к первому и третьему списку.</p>
  <p>Листинг скрипта на Python в jupiter реализующий заполнение 10 матриц случайных размерностей по спирали целыми числами начиная с 0:<a href='https://github.com/PavlyukovVladimir/learning-to-make-programs/blob/master/spiral_matrix.ipynb'>spiral_matrix.ipynb</a></p>

  ```Python
  import random
def quicksort(nums,fun):
    """рекурсивная быстрая сортировка, для определения n < q использует fun(n,q)"""
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        l_nums = [n for n in nums if fun(n,q)]#список элементов меньше q
        e_nums = [n for n in nums if ((not fun(n,q)) and (not fun(q,n)))]#список элементов одинакового порядка с q
                                                                         #т.е. не больше и не меньше q
        b_nums = [n for n in nums if fun(q,n)]##список элементов больше q
    return quicksort(l_nums,fun) + e_nums + quicksort(b_nums,fun)
  ```
  
```Python
nums=[1,2,5,3,10,1,3]
def fun(n,q):
    """функциональный эквивалент оператору <"""
    return n<q
print(quicksort(nums,fun))
```

```
[1, 1, 2, 3, 3, 5, 10]
```

```Python
num=[[1,2],[2,1],[2,2],[1,1],[1,1,1,3,4],[2,3,4,5],["a",4,"rules"]]
def fun2(l,r):
    """сравнивает списки, сравнивая их 2-е элементы"""
    return l[1] < r[1]
print(quicksort(num,fun2))
```

```
[[2, 1], [1, 1], [1, 1, 1, 3, 4], [1, 2], [2, 2], [2, 3, 4, 5], ['a', 4, 'rules']]
```

```Python
num=[[1,2],[2,1],[2,2],[1,1],[1,1,1,3,4],[2,3,4,5],[0,4,"rules"]]
def fun3(l,r):
    """сравнивает списки, по расстоянию от начала 2D координат, считая первые 2 элемента координатами"""
    return (l[0]*l[0]+l[1]*l[1]) < (r[0]*r[0]+r[1]*r[1])
print(quicksort(num,fun3))
```

```
[[1, 1], [1, 1, 1, 3, 4], [1, 2], [2, 1], [2, 2], [2, 3, 4, 5], [0, 4, 'rules']]
```

<p><a href="#navigation">Вверх к Содержанию</a></p>

</body>
</html>
