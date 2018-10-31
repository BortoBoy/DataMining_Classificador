import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

def carregar():
	data = pd.read_csv('athlete_events.csv')
	return data

def modificar(data):
	data = data.fillna(0)
	for i in data.index:
	    if data.at[i, 'Medal'] == 'Gold':
	    	data.at[i, 'Medal'] = 3
	    elif data.at[i, 'Medal'] == 'Silver':
	    	data.at[i, 'Medal'] = 2
	    elif data.at[i, 'Medal'] == 'Bronze':
	    	data.at[i, 'Medal'] = 1	
	data[['Medal']] = data[['Medal']].apply(pd.to_numeric)
	data.to_csv(path_or_buf='athlete_events.csv', index=False)

def imprimir(data):
	print(data.cov())
	print(data.corr())
	print(data.describe())

def selecionar(data):
	l = list(data)
	l.remove('Year')
	l.remove('Season')
	data = data[l]
	data.to_csv(path_or_buf='athlete_events.csv', index=False)

def ApplyPCA(data):
	features = ['Age', 'Height', 'Weight', 'Year']
	x = data.loc[:, features].values
	x = StandardScaler().fit_transform(x)
	
	pca = PCA(n_components=2)
	principalComponents = pca.fit_transform(x)
	principalDf = pd.DataFrame(data=principalComponents, columns=['PC1', 'PC2'])
	principalDf = pd.concat([principalDf, data[['Sport']]], axis = 1)
	pd.DataFrame(data = principalComponents)

	#showing
	fig = plt.figure(figsize = (8,8))
	ax = fig.add_subplot(1,1,1) 
	ax.set_xlabel('Principal Component 1', fontsize = 15)
	ax.set_ylabel('Principal Component 2', fontsize = 15)
	ax.set_title('2 component PCA', fontsize = 20)

	#Sports = data.loc[:,['Sport']].values #all sports
	sports = ['Basketball', 'Judo', 'Football']
	colors = ['r', 'g', 'b']
	for s, color in zip(sports,colors):
	    indicesToKeep = finalDf['Sports'] == s
	    ax.scatter(principalDf.loc[indicesToKeep, 'PC1']
	               , principalDf.loc[indicesToKeep, 'PC2']
	               , c = color
	               , s = 50)
	ax.legend(targets)
	ax.grid()

data = carregar()
ApplyPCA(data)
