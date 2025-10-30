import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
BMI = df['weight'] / (df['height'] **2)
df['overweight'] = 0
df['overweight'] = (df['weight'] / (df['height'] ** 2) > 25).astype(int)

# 3
df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0 
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1

df.loc[df['gluc'] == 1, 'gluc'] = 0 
df.loc[df['gluc'] > 1, 'gluc'] = 1

# 4
def draw_cat_plot():
    # 5
    df_cat =  pd.melt(df, id_vars='cardio', value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])


    # 6
    combos = pd.MultiIndex.from_product(
    [df['cardio'].unique(), df_cat['variable'].unique(), [0,1]],
    names=['cardio','variable','value']
)
    df_cat = df_cat.groupby(['cardio','variable','value'], as_index=False).size().rename(columns={'size':'total'})
    df_cat = df_cat.set_index(['cardio','variable','value']).reindex(combos, fill_value=0).reset_index()


    # 7
    g = sns.catplot(
        data=df_cat,
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar'
    )

    # 8
    fig = g.figure
 

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    cols_order = ['id', 'age', 'sex', 'height', 'weight', 'ap_hi', 'ap_lo',
                  'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio', 'overweight']
    df_heat = df_heat[cols_order]

    corr = df_heat.corr().round(1)

    corr = corr.mask(np.isclose(corr, 0.0), 0.0)

    mask = np.triu(np.ones_like(corr, dtype=bool))

    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", cmap='coolwarm', ax=ax)

    fig.savefig('heatmap.png')
    return fig