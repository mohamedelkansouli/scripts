def createMACD(data):
    
    data['e12'] = pd.Series.ewm(data['Last Price'], span=26).mean()
    data['e26'] = pd.Series.ewm(data['Last Price'], span=12).mean()
    data['MACD'] = data['e12']- data['e26']
    return data


def computeStrategy(data):
        # initialisation de quelques variables
        
        # crée des colonnes vides dans laquelle nous placerons notre strategie et notre budget
        data['position'] = None
        data['budget'] = 0
        return data

profit = 0
move = 'buy' # drapeau qui servira à signaler le prochain mouvement 'buy' > 'sell' > 'buy' etc...
            
        

        


for name in result['Coin'].unique():
    data =result[result['Coin']==name]
    data = createMACD(data)
    data = computeStrategy(data)
    
        
    for row in range (len(data)): 
    # conditions pour un achat
        lastClose = data['Last Price'].iloc[row]

        if data['MACD'].iloc[row] < 0 and data['MACD'].iloc[row-1] > 0 and move == 'buy':
            data['position'].iloc[row] = 'buy'
            move = 'sell'
            data['budget'].iloc[row] = data['budget'].iloc[row-1] - data['Last Price'].iloc[row]
        # conditions pour une vente
        elif data['MACD'].iloc[row] > 0 and data['MACD'].iloc[row-1] < 0 and move == 'sell' and data['Last Price'].iloc[row] > lastClose:
            data['position'].iloc[row] = 'sell'
            move = 'buy'
            data['budget'].iloc[row] = data['budget'].iloc[row-1] + data['Last Price'].iloc[row]
        # ni vente ni achat, nous tenons la position
        else:
            data['position'].iloc[row] = 'hold'
            data['budget'].iloc[row] = data['budget'].iloc[row-1]