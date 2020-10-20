def createMACD(result):
    
    result['e26'] = pd.Series.ewm(result['Last Price'][result['Coin']==name], span=26).mean()
    result['e12'] = pd.Series.ewm(result['Last Price'][result['Coin']==name], span=12).mean()
    result['MACD'] = result['e12'][result['Coin']==name] - result['e26'][result['Coin']==name]
    return result


def computeStrategy(result):
        # initialisation de quelques variables
        profit = 0
        move = 'buy' # drapeau qui servira à signaler le prochain mouvement 'buy' > 'sell' > 'buy' etc...
        
        # crée des colonnes vides dans laquelle nous placerons notre strategie et notre budget
        result['position'] = None
        result['budget'] = 0
        
        
for name in result['Coin'].unique():
    result[result['Coin']==name] = createMACD(result[result['Coin']==name])
    
        
    for row in range (len(result[result['Coin']==name])): 
        # conditions pour un achat
        if result['MACD'][result['Coin']==name].iloc[row] < 0 and result['MACD'][result['Coin']==name].iloc[row-1] > 0 and move == 'buy':
            result['position'][result['Coin']==name].iloc[row] = 'buy'
            move = 'sell'
            lastClose  = result['Last Price'][result['Coin']==name].iloc[row]
            result['budget'][result['Coin']==name].iloc[row] = result['budget'][result['Coin']==name].iloc[row-1] - result['Last Price'].iloc[row]
        # conditions pour une vente
        elif result['MACD'].iloc[row] > 0 and result['MACD'].iloc[row-1] < 0 and move == 'sell' and result['Last Price'].iloc[row] > lastClose :
            result['position'].iloc[row] = 'sell'
            move = 'buy'
            result['budget'].iloc[row] = result['budget'].iloc[row-1] + result['Last Price'].iloc[row]
        # ni vente ni achat, nous tenons la position
        else:
            result['position'].iloc[row] = 'hold'
            result['budget'].iloc[row] = result['budget'].iloc[row-1]