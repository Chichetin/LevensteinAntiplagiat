# LevensteinAntiplagiat
Антиплагиат кодов на питоне через Левенштейна

(питон только ради этого проекта начал изучать, до этого писал на джаве и си)

Логика проекта такова - переводим оба кода в ast-дерево. В ast-дереве мы (по желанию) удаляем все части формата id='*что-то*', чтобы избавиться от влияния названия переменных на итоговое значение <уровня> плагиата. 

Также, я избавляюсь от комментариев вида """*что-то*""", как я понял - это какая-то особая забавная форма комментариев, которые загружаются в ast-дерево.  Понятно, что таких <исключений> которые в действительности не изменяют код, но изменяют мой счетчик плагита есть еще очень много - но я не буду рассматривать их все. Так же, как и то что этот метод не считает за плагиат изменение порядка не меняющие код, как банальное изменение порядка импортов.

После этого я пропускаю два очищенных ast-дерева через функцию измеряющую их расстояние Левенштейна. После этого, я узнаю среднюю количество символов в слов. Делю полученное расстояние Левенштейна на это число, получаю примерное количество слов отделяющих один текст от другого. 
Оценка очень грубая, тем более что количество слов и знаков читается из изначального кода (неотчищенного), возможно потом придумаю что-то еще.

Работает по команде - python3 levencht.py files_dirs 
, где в файле files_dirs лежат пути к файлам для сравнения в формате два файла на одну строку. 

Вывод - сразу в консоль.
