df['salary'] = df.groupby('department')['salary'].transform(
    lambda x: x.fillna(x.mean())
)

df['salary'].fillna(df['salary'].mean(), inplace=True)
