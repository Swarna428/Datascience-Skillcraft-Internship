import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set_style("whitegrid", {'grid.linestyle': '--', 'grid.alpha': 0.3})
plt.rcParams['font.family'] = 'Arial'
titanic = sns.load_dataset('titanic').dropna(subset=['age'])
mean_age = titanic['age'].mean()
median_age = titanic['age'].median()
fig, ax = plt.subplots(figsize=(10, 6), constrained_layout=True)
hist = sns.histplot(data=titanic, x='age', bins=np.arange(0, 81, 5), kde=True, color='#1a698a', edgecolor='white', linewidth=0.5, alpha=0.9)
for line in ax.lines:
    line.set(color='#0d324d', linewidth=2.5)
ax.axvline(mean_age, color='#c1272d', linestyle='--', linewidth=1.5,label=f'Mean: {mean_age:.1f} yrs')
ax.axvline(median_age, color='#f7931e', linestyle='-', linewidth=1.5,label=f'Median: {median_age:.1f} yrs')
ax.text(0.02, 0.95, 'Key Insights:', transform=ax.transAxes,fontsize=11, fontweight='bold', va='top')
ax.text(0.02, 0.88, '- Peak at 20-30 year olds', transform=ax.transAxes,fontsize=10, va='top')
ax.text(0.02, 0.82, '- Right-skewed distribution', transform=ax.transAxes,fontsize=10, va='top')
ax.set_title('Age Distribution of Titanic Passengers',fontsize=16, pad=20, fontweight='bold')
ax.set_xlabel('Age (Years)', fontsize=12, labelpad=10)
ax.set_ylabel('Number of Passengers', fontsize=12, labelpad=10)
ax.set_xticks(np.arange(0, 81, 5))
ax.set_xticklabels(ax.get_xticks(), fontsize=10)
ax.set_yticklabels(ax.get_yticks(), fontsize=10)
ax.legend(frameon=True, framealpha=1, loc='upper right')
sns.despine(left=True, bottom=True)
ax.grid(axis='y', visible=True)
ax.set_axisbelow(True)
plt.savefig('professional_age_distribution.png', dpi=300, bbox_inches='tight')
plt.show()
