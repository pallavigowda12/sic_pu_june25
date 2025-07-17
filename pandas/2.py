# Filtering rows in Pandas based on a condition

# Explanation: Using boolean indexing to filter rows where Age > 25

filtered_df = df[df1['Age'] > 25]  # Selects rows where Age > 25
# SQL: select * from students where age > 25;
print(filtered_df)