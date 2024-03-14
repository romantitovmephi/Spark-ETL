## Построение пайплайна (ETL) обработки данных с помощью PySpark и SparkSQL 

`data/cars.csv` - источник

Считает по каждому производителю (поле `manufacturer_name`):
- количество объявлений
- средний год выпуска автомобилей
- минимальную цену
- максимальную цену

Выгружает результат в `output.csv`

`dataset_etl.ipynb` - jupyter notebook c ETL

`dataset_etl.py` - можно запустить в терминале в режиме standalone:
  
   ```bash
   (venv) spark-submit dataset_etl.py
   ```

## Установка Pyspark локально из pip

### Предварительные требования

1. Python 3.6+

2. Установленная Java версии 11 или выше

### Установка Apache Spark

1. Делаем виртуальное окружение Python:

   ```bash
   python3 -m venv venv
   ```

2. Активируем окружение:

   ```bash
   # Linux, macOs
   source venv/bin/activate
   ```

3. Ставим pyspark из `pip`:

   ```bash
   (venv) pip install pyspark
   ```

4. Ставим jupyter notebook:

   ```bash
   pip install notebook
   ```

5. Запускаем jupyter notebook:

   ```bash
   jupyter notebook
   ```

## Запуск Spark из Docker

Необходим установленный Docker

### Установка Spark

Можно использовать образ [Jupyter notebooks](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html) с установленным Apache Spark.

Запускаем контейнер в интерактивном режиме:

```bash
docker run -it -p 8888:8888 -p 4040:4040 -v $(pwd):/home/jovyan/work jupyter/pyspark-notebook
```
