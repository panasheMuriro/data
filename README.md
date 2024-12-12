# Pandas Learning Path

## Beginner Level
1. Introduction to pandas
    - ✅ Understand what pandas is and its use cases.
    - ✅ Install pandas: pip install pandas.

2. Basic Data Structures
    - ✅ Series: Learn about 1D labeled arrays.
    - ✅ Creating, accessing, and modifying Series.
    - ✅ DataFrame: Learn about 2D labeled data structures.
    - ✅ Creating DataFrames from dictionaries, lists, NumPy arrays, and CSV/Excel files.
    - ✅ Accessing rows, columns, and individual elements (.loc, .iloc).
3. Basic Operations
    - Data inspection (.head(), .tail(), .info(), .describe()).
    - Data selection ([], .loc, .iloc).
    - Adding and deleting columns.
    - Basic descriptive statistics (.mean(), .sum(), .max(), .min()).
4. Data Cleaning
    - Handling missing values (.isna(), .fillna(), .dropna()).
    - Renaming columns and indices (.rename()).
    - Changing data types (.astype()).

## Intermediate Level
5. Data Manipulation
    - Filtering rows and columns.
    - Sorting (.sort_values(), .sort_index()).
    - Grouping data (.groupby()).
    - Aggregations (.agg(), .apply()).
    - Pivot tables (.pivot_table()).
6. Data Merging
    - Concatenation (pd.concat()).
    - Merging and joining (pd.merge(), .join()).
    - Reshaping data (.melt(), .stack(), .unstack()).
7. Time Series Analysis
    - Working with date and time data.
    - Parsing dates (pd.to_datetime()).
    - Indexing with time-series data.
    - Resampling (.resample()).
8. Data Visualization with pandas
    - Simple plotting with .plot().
    - Using pandas with Matplotlib or Seaborn for advanced visualizations.

## Advanced Level
9. Performance Optimization
    - Using vectorized operations instead of loops.
    - Working with large datasets (chunking, Dask, or modin.pandas).
    - Profiling performance (%%time, memory_usage()).
10. Advanced Indexing
    - MultiIndex (hierarchical indexing).
    - Slicing and dicing with MultiIndex.
11. Custom Functions
    - Applying functions with .apply(), .applymap().
    - Lambda functions for quick calculations.
12. Data Exporting
    - Saving DataFrames to files (CSV, Excel, JSON, SQL).
13. Real-World Applications
    - Data wrangling (cleaning and preprocessing).
    - Exploratory Data Analysis (EDA).
    - Integration with SQL databases (.read_sql(), .to_sql()).
14. Pandas with Machine Learning
    - Preparing datasets for machine learning models.
    - Feature engineering using pandas.