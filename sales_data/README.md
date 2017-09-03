# Sales Data

The dataset can be downloaded [here](/purchases.gz).

Format of each line in the  is:
```
date  time  store-name  item-description  cost  method-of-payment
```

## List of Questions

Write some Mappers and Reducers to answer the following questions:

1. [Find the total sales across all the stores.](/01_store_totals)
2. [Find the total sales breakdown by product category across all the stores.](/02_product_totals)
3. [Find the monetary value for the highest individual sale for each separate store.](/03_store_highest_sale)
4. [Find the total sales value across all the stores, and the total number of sales. Assume there is only one reducer.](/04_total_sales_and_count)
5. [Find the mean (average) of sales for each weekday.](/05_mean_sales_by_weekday)
