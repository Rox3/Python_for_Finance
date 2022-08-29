def getMA(series, maperiod ,ema):
    
    
    if ema == True:
        # Use exponential moving average
        alpha=1/(maperiod) ###RMA
        #alpha=2/(maperiod+1) ###EMA
        ma = series.ewm(alpha=alpha,adjust=True, min_periods = maperiod).mean()
        #ma = series.ewm(com = maperiod - 1, adjust=True, min_periods = maperiod).mean()
        
    else:
        # Use simple moving average
        ma = series.rolling(window = maperiod).mean()
        
    return ma


def MA(series, maperiod ):
    
    alpha=1/(maperiod) ###RMA
    #alpha=2/(maperiod+1) ###EMA
    ma = series.ewm(alpha=alpha).mean()
    return ma
