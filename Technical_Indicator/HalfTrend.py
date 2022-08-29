from MovingAverage import*
def getHalfTrend(amplitude=2):
    global df
    
    trend=1
    nextTrend=0
    
    df['highma']=getMA(df['high'],amplitude,0)
    df['lowma']=getMA(df['low'],amplitude,0)
    df['highPrice']=df['high'].rolling(amplitude).max()
    df['lowPrice']=df['low'].rolling(amplitude).min() 
    
    maxlowPrice=df.loc[0,'low']
    minHighPrice=df.loc[0,'high']

    for i in range(amplitude-1,len(df)):
        
        

        # maxhigh=df['high'].rolling(amplitude).max()
        # minlow=df['high'].rolling(amplitude).min()
        
            
        # highPrice=maxhigh
        # lowPrice=minlow

        highPrice=df.loc[i,'highPrice']
        lowPrice=df.loc[i,'lowPrice']
        
        highma=df.loc[i,'highma']
        lowma=df.loc[i,'lowma']

        

        if nextTrend==1:
            maxlowPrice=max(lowPrice,maxlowPrice)

            if((highma<maxlowPrice) and (df.loc[i,'close']<df.loc[i-1,'low'])):
                trend=-1
                nextTrend=0
                minHighPrice=highPrice
        else:
            minHighPrice=min(highPrice,minHighPrice) 

            if((lowma>minHighPrice) and (df.loc[i,'close']>df.loc[i-1,'high'])):
                trend=1
                nextTrend=1
                maxlowPrice=lowPrice

        df.loc[i,'trend']=trend