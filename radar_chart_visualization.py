# COMP4037 Coursework 2 - Chan Wu

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

file_path = 'Results_21MAR2022_nokcaladjust.csv'  

df = pd.read_csv(file_path)
df.columns = df.columns.str.strip()  # remove space

# groups
diet_groups_present = ['vegan', 'veggie', 'fish', 'meat', 'meat50', 'meat100']
df_filtered = df[df['diet_group'].isin(diet_groups_present)]

selected_variables = [
    'mean_ghgs',
    'mean_land',
    'mean_watscar',
    'mean_eut',
    'mean_bio',
    'mean_watuse'
]

grouped = df_filtered.groupby('diet_group')[selected_variables].mean()

# 0-1
scaler = MinMaxScaler()
grouped_normalized = pd.DataFrame(
    scaler.fit_transform(grouped),
    index=grouped.index,
    columns=[
        'GHG emissions',
        'Land Use',
        'Water Scarcity',
        'Eutrophication Potential',
        'Biodiversity Impact',
        'Agricultural Water Usage'
    ]
)

categories = grouped_normalized.columns.tolist()
N = len(categories)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]  

# Initialize plot
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
colors = ['#2ca02c', '#1f77b4', '#ff7f0e', '#d62728', '#9467bd', '#8c564b']

for idx, (group, values) in enumerate(grouped_normalized.iterrows()):
    values = values.tolist()
    values += values[:1]
    ax.plot(angles, values, label=group, linewidth=2, color=colors[idx], alpha=0.9)
    ax.fill(angles, values, color=colors[idx], alpha=0.15)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12)

ax.set_yticks([0.2, 0.4, 0.6, 0.8])
ax.set_yticklabels(["0.2", "0.4", "0.6", "0.8"], fontsize=10)
ax.yaxis.grid(True)
ax.xaxis.grid(True)

ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10, title='Diet Group')

# title
plt.title('Comparison of Environmental Impacts Across Six Diet Groups', size=18, y=1.08)
plt.tight_layout()
plt.show()
