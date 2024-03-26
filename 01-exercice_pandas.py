import pandas as pd

# Exercice 2
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Age': [25, 30, 35, 27, 29],
    'City': ['Paris', 'London', 'New York', 'Berlin', 'Tokyo']
}
df = pd.DataFrame(data)
print("Exercice 2:")
print(df)
print()

# Exercice 3
print("Exercice 3:")
print(df['Name'])
print()

# Exercice 4
print("Exercice 4:")
print(df['Age'] > 28)
print(df[df['Age'] > 28])
print()

# Exercice 5
print("Exercice 5:")
df['Salary'] = [50000, 60000, 70000, 55000, 65000]
print(df)
print()

# Exercice 6
print("Exercice 6:")
print(df.sort_values(by='Age', ascending=False))
print()

# Exercice 7
print("Exercice 7:")
print(df.describe())
# count : nombre de lignes
# mean : moyenne (arithmetic mean)
# std : standard deviation = écart type (racine de la somme des carrée divisée par le nombre de valeurs)
# 25%, 50%, 75% = percentiles
print()

# Exercice 8
print("Exercice 8:")
students_df = pd.read_csv('students.csv')
print(students_df)
print()

# Exercice 9
print("Exercice 9:")
print(students_df.groupby('Gender'))
grouped = students_df.groupby('Gender')['Grade'].mean()
print(grouped)
print()

# Exercice 10
print("Exercice 10:")
grouped.to_csv('student_grades_avg.csv', header=True)
print("Export successful!")
