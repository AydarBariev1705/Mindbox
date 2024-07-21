from pyspark.sql import SparkSession

spark = SparkSession.builder.appName(
    "test_app",
).getOrCreate()

# Пример для демонстрации
products_test = [
    (1, 'test_1'),
    (2, 'test_2'),
    (3, 'test_3'),
]

categories_test = [
    (101, 'category_test_1'),
    (102, 'category_test_2'),
    (103, 'category_test_3'),
]

product_category_data = [
    (1, 101),
    (2, 102),
    (1, 103),
    (3, 101),
]

# Создаем dataframe
products_df = spark.createDataFrame(
    products_test,
    ['product_id', 'product_name'],
)

categories_df = spark.createDataFrame(
    categories_test,
    ['category_id', 'category_name'],
)

product_category_df = spark.createDataFrame(
    product_category_data,
    ['product_id', 'category_id'],
)

product_category_join_df = product_category_df.join(
    products_df,
    on='product_id',
    how='inner',
).join(
    categories_df,
    on='category_id',
    how='inner',
).select(
    'product_name',
    'category_name',
)

products_with_categories_df = product_category_df.select('product_id').distinct()
products_without_categories_df = products_df.join(
    products_with_categories_df,
    on='product_id',
    how='left_anti',
)

product_category_join_df.show()
products_without_categories_df.select('product_name').show()
