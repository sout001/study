import numpy as np
import pandas as pd

# 生成带有索引的Series
test = pd.Series([1, 3, 5, np.nan, 6, 8])
print(type(test))

dates = pd.date_range('20201230', periods=6)

df = pd.DataFrame(np.random.rand(6, 4), index=dates, columns=list('ABCD'))
print(df)

print(type(dates))
