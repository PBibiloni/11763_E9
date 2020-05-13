import pandas
from pandas.tools import plotting
from scipy.stats import ttest_1samp, ttest_ind, ttest_rel, wilcoxon, bartlett, kstest, shapiro

data = pandas.read_csv('data/brain_size.csv', sep=';', na_values=".")
print('Medidas: f{data.shape}')
print('Columnas: f{data.columns}')

plotting.scatter_matrix(data[['Weight', 'Height', 'MRI_Count']])
plotting.scatter_matrix(data[['PIQ', 'VIQ', 'FSIQ']])

female_viq = data[data['Gender'] == 'Female']['VIQ']
male_viq = data[data['Gender'] == 'Male']['VIQ']
