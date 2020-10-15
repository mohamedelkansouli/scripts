def createMACD(result):
    
    result['e26'] = pd.Series.ewm(result['Last Price'], span=26).mean()
    result['e12'] = pd.Series.ewm(result['Last Price'], span=12).mean()
    result['MACD'] = result['e12'] - result['e26']
    return result

result = createMACD(result)

def computeStrategy(result):
    # initialisation de quelques variables
    profit = 0
    move = 'buy' # drapeau qui servira à signaler le prochain mouvement 'buy' > 'sell' > 'buy' etc...
    
    # crée des colonnes vides dans laquelle nous placerons notre strategie et notre budget
    result['position'] = None
    result['budget'] = 0
    
for row in range (len(result)): 
    # conditions pour un achat
    if result['MACD'].iloc[row] < 0 and result['MACD'].iloc[row-1] > 0 and move == 'buy':
        result['position'].iloc[row] = 'buy'
        move = 'sell'
        lastLast Price = result['Last Price'].iloc[row]
        result['budget'].iloc[row] = result['budget'].iloc[row-1] - result['Last Price'].iloc[row]
    # conditions pour une vente
    elif result['MACD'].iloc[row] > 0 and result['MACD'].iloc[row-1] < 0 and move == 'sell' and result['Last Price'].iloc[row] > lastLast Price:
        result['position'].iloc[row] = 'sell'
        move = 'buy'
        result['budget'].iloc[row] = result['budget'].iloc[row-1] + result['Last Price'].iloc[row]
    # ni vente ni achat, nous tenons la position
    else:
        result['position'].iloc[row] = 'hold'
        result['budget'].iloc[row] = result['budget'].iloc[row-1]