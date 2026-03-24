import pandas as pd

df = pd.DataFrame({
    'department': ['IT', 'IT', 'HR', 'HR', 'Finance'],
    'employee': ['A', 'B', 'C', 'D', 'E'],
    'salary': [50000, 60000, 45000, 70000, 80000]
})

result = df.groupby('department').agg(
    total_salary=('salary', 'sum'),
    avg_salary=('salary', 'mean'),
    highest_paid=('employee', lambda x: df.loc[x.index, 'salary'].idxmax())
)

result['highest_paid'] = result['highest_paid'].map(df['employee'])

print(result)
