import pandas as pd

# 读取数据
df = pd.read_excel('../合并.xlsx')

# 按照年份分
df2020_to_2021 = df[(df['销售日期'] >= '2020-07-01') & (df['销售日期'] < '2021-07-01')]
df2021_to_2022 = df[(df['销售日期'] >= '2021-07-01') & (df['销售日期'] < '2022-07-01')]
df2022_to_2023 = df[(df['销售日期'] >= '2022-07-01') & (df['销售日期'] < '2023-07-01')]

# 每年每种产品的销量统计
df2020_to_2021_S = df2020_to_2021.groupby(['单品编码', '单品名称', '销售单价(元/千克)']).agg({'销量(千克)': 'sum'}).reset_index()
df2021_to_2022_S = df2021_to_2022.groupby(['单品编码', '单品名称', '销售单价(元/千克)']).agg({'销量(千克)': 'sum'}).reset_index()
df2022_to_2023_S = df2022_to_2023.groupby(['单品编码', '单品名称', '销售单价(元/千克)']).agg({'销量(千克)': 'sum'}).reset_index()

# 保存数据
df2020_to_2021.to_excel('./品类按年分/2020_to_2021.xlsx', index=False)
df2021_to_2022.to_excel('./品类按年分/2021_to_2022.xlsx', index=False)
df2022_to_2023.to_excel('./品类按年分/2022_to_2023.xlsx', index=False)

df2020_to_2021_S.to_excel('./品类按年分/2020_to_2021_S.xlsx', index=False)
df2021_to_2022_S.to_excel('./品类按年分/2021_to_2022_S.xlsx', index=False)
df2022_to_2023_S.to_excel('./品类按年分/2022_to_2023_S.xlsx', index=False)