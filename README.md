# Скрипты для автоматизации загрузки задач на платформу Яндекс.Контест
## Case:
Загружать задачи в Яндекс.Контест вручную - мучение, хорошо, что система позволяет импортировать задачи, сформированные по системе [POLYGON](https://polygon.codeforces.com/).

В `sample` расположен шаблон задачи. 
<details>
<summary>Как этот шаблон создавался</summary>
В https://polygon.codeforces.com/ создана самая простая задача, добавлено решение, чекер, тест для примера и один обычный тест. После этого задача экспортируется как package и из получившегося итеративно выкидывается всё "ненужное", то есть те файлы и настройки, без которых возможно импортировать задачу в Яндекс.Контест. Не исключено, что в дальнейшем что-то изменится в системе Яндекс.Контеста, и конкретно этот вид шаблона перестанет работать.
</details>

## Постановка задачи
Для загрузки задачи поступают в одном из двух форматов: `.docx` и `.ipynb`. В одном файле (вне зависимости от формата) находятся имена задач, тексты условий и решения. 

**Цель:** скрипт, который парсит содержание файла с задачами и использует результат (данные по каждой задачи) для создания package для каждой задачи.

## Current state of project:
 - `script.ipynb` - первая базовая версия скрипта, создающего необходимые директории и основную часть файлов, пока без нормального содержания.
 - `parsing_docs.ipynb` - ноутбук с экспериментами по парсингу файлов. Использует `LangChain` и `OpenAI API` для парсинга и валидации решений.



# TODO
1) Закончить `script.ipynb`: содержание (файл решения, условия задач и прочее) взять из `parsing_docs.ipynb`.
2) В `parsing_docs.ipynb` добавить chains с выводом input и output formats.
3) Создать скрипт для придумывания тестовых случаев к задачам (и добавить в структуру задачи валидатор тестов)