import pandas as pd

# 读取数据
df1 = pd.read_excel('附件1.xlsx')
df2 = pd.read_excel('附件2.xlsx')
# df3 = pd.read_excel('附件3.xlsx')
# df4 = pd.read_excel('附件4.xlsx')

# 合并数据
df = pd.merge(df1, df2, on=['单品编码'])

# 保存数据
df.to_excel('合并.xlsx', index=False)
