from MovingAverage import*

def adx(df,maperiod):
    
    for i in range(1,len(df)):
        df.loc[i,'high_low']=df.loc[i,'high']-df.loc[i,'low']
        df.loc[i,'high_preClose']=abs(df.loc[i,'high']-df.loc[i-1,'close'])
        df.loc[i,'low_preClose']=abs(df.loc[i,'low']-df.loc[i-1,'close'])
        df.loc[i,'trueRange']=max(df.loc[i,'high_low'],df.loc[i,'high_preClose'],df.loc[i,'low_preClose'])
        
        
        if(((df.loc[i,'high']-df.loc[i-1,'high'])>(df.loc[i-1,'low']-df.loc[i,'low']))  and (df.loc[i,'high']-df.loc[i-1,'high'] >0)):
            df.loc[i,'plusdm']=(df.loc[i,'high']-df.loc[i-1,'high'])
        else:
            df.loc[i,'plusdm']=0

        if(((df.loc[i-1,'low']-df.loc[i,'low'])>(df.loc[i,'high']-df.loc[i-1,'high'])) and(df.loc[i-1,'low']-df.loc[i,'low'] >0)):
            df.loc[i,'minusdm']=(df.loc[i-1,'low']-df.loc[i,'low'])
        else:
            df.loc[i,'minusdm']=0
    
    # print(df)
    
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)
    df['smoothed+dm']=getMA(df['plusdm'],maperiod,1)
    df['smoothed-dm']=getMA(df['minusdm'],maperiod,1)
    df['smoothedTR']=getMA(df['trueRange'],maperiod,1)
    # df.to_csv('data.csv')
    for i in range(0,len(df)):
        df.loc[i,'plus_di']= (df.loc[i,'smoothed+dm']/df.loc[i,'smoothedTR'])*100
        df.loc[i,'minus_di']= (df.loc[i,'smoothed-dm']/df.loc[i,'smoothedTR'])*100
        df.loc[i,'DX']= (abs(df.loc[i,'smoothed+dm']-df.loc[i,'smoothed-dm'])/(df.loc[i,'smoothed+dm']+df.loc[i,'smoothed-dm']))*100

    df['adx']=getMA(df['DX'],maperiod,1)
    return df
