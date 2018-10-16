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
<pre class="python" style="font-family:monospace;"><span style="color: #ff7700;font-weight:bold;">def</span> get_element<span style="color: black;">&#40;</span>maximum<span style="color: black;">&#41;</span>:
    <span style="color: #483d8b;">&quot;&quot;&quot;Выдает числа от 0 до maximum&quot;&quot;&quot;</span>
    maximum-<span style="color: #66cc66;">=</span><span style="color: #ff4500;">1</span>
    number<span style="color: #66cc66;">=</span><span style="color: #ff4500;">0</span>
    <span style="color: #ff7700;font-weight:bold;">yield</span> number
&nbsp;
    <span style="color: #ff7700;font-weight:bold;">while</span> number<span style="color: #66cc66;">&lt;</span>maximum:
        next<span style="color: #66cc66;">=</span>number+<span style="color: #ff4500;">1</span>
        <span style="color: #ff7700;font-weight:bold;">yield</span> next
        number<span style="color: #66cc66;">=</span>next</pre>
<p><a href="#navigation">Вверх к Содержанию</a></p>
  ## 2. Быстрая сортировка с произвольной функцией сравнения. <a name="quick_sorting"></a>
  
  <p>Задано множество объектов X, и множество допустимых ответов Y, и существует целевая функция y*: X -> Y, значения которой y<sub>i</sub> = y*(x<sub>i</sub>) известны только на конечном подмножестве объектов {x<sub>1</sub>, …, x<sub>ℓ</sub>} ⊂ X.</p>

<p><a href="#navigation">Вверх к Содержанию</a></p>

</body>
</html>
