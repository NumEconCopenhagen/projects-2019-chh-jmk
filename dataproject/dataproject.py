#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'dataproject'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # **Project 1: Data Analysis Project**
#%% [markdown]
# **By Christian Hjorth Hansen and Jacob Mai Kaaber**
#%% [markdown]
# ## **Introduction**
#%% [markdown]
# In this project we look at the stock prices of the 3 biggest energy firms world wide. These 3 firms are *Exxon Mobile Corporation*, *Chevron Corporation* and *Royal Dutch Shell* (It should be mentioned, that due to the fact that Royal Dutch Shell has split their stocks in A and B, we only look at the B shares since they get traded more often). 
#  
# We will describe the devolpment of these 3 firms stock prices by presenting data visually and using methods from descreptive economics.
#%% [markdown]
# ## **Importing packages**
#%% [markdown]
# We start by importing all the necessary packages. 

#%%
import pandas as pd
import matplotlib.pyplot as plt
import datetime as datetime
import pandas_datareader
import numpy as np
import ipywidgets as widgets

#%% [markdown]
# ## **Pick start- and enddate**
#%% [markdown]
# Here we have chosen the 1st of January 2016 as the start date and the 20th of March as the end date. 

#%%
start = datetime.datetime(2016,1,1)
end   = datetime.datetime(2019,3,20)

#%% [markdown]
# ## **Importing stock prices**
#%% [markdown]
# We are going to import the data in 3 section, one for each firm. The data is being imported as daily data from IEX.
#%% [markdown]
# ### Exxon Mobile Corporation
#%% [markdown]
# **First** we import the data.

#%%
XOM = pandas_datareader.iex.daily.IEXDailyReader('XOM', start, end).read()

#%% [markdown]
# **Next** we drop the variables, which we aren't going to use.

#%%
del XOM['open']
del XOM['high']
del XOM['low']

#%% [markdown]
# **Next** we add 3 new variable, one with the company name, one which shows the closing prices demeaned and the last variable shows the precentage change in the closing price.

#%%
XOM['firm'] = 'Exxon Mobile'
XOM['close_demeaned'] = XOM.groupby('firm')['close'].transform(lambda x: x - x.mean())
XOM['percentage_change, %'] = ((XOM.close - XOM.close.shift(1)) / XOM.close.shift(1))*100

#%% [markdown]
# **Lastly** we convert the date from index to dates using datetime

#%%
XOM.index = pd.to_datetime(XOM.index)

#%% [markdown]
# To test that the code works as expected we print the first 5 observations.

#%%
XOM.head()

#%% [markdown]
# ### Chevron Corporation
#%% [markdown]
# **First** we import the data.

#%%
CVX = pandas_datareader.iex.daily.IEXDailyReader('CVX', start, end).read()

#%% [markdown]
# **Next** we drop the variables, we are not going to use.

#%%
del CVX['open']
del CVX['high']
del CVX['low']

#%% [markdown]
# **Next** we add a new variable with the company name.

#%%
CVX['firm'] = 'Chevron'
CVX['close_demeaned'] = CVX.groupby('firm')['close'].transform(lambda x: x - x.mean())
CVX['percentage_change, %'] = ((CVX.close - CVX.close.shift(1)) / CVX.close.shift(1))*100

#%% [markdown]
# **Lastly** we convert the date from index to dates using datetime

#%%
CVX.index = pd.to_datetime(CVX.index)

#%% [markdown]
# And to test that the code works as expected we print the first 5 observations.

#%%
CVX.head()

#%% [markdown]
# ### Royal Dutch Shell (Shares B)
#%% [markdown]
# **First** we import the data

#%%
RDS = pandas_datareader.iex.daily.IEXDailyReader('RDS.B', start, end).read()

#%% [markdown]
# **Next** we drop the variables, we are not going to use.

#%%
del RDS['open']
del RDS['high']
del RDS['low']

#%% [markdown]
# **Next** we add a new variable with the company name.

#%%
RDS['firm'] = 'Shell'
RDS['close_demeaned'] = RDS.groupby('firm')['close'].transform(lambda x: x - x.mean())
RDS['percentage_change, %'] = ((RDS.close - RDS.close.shift(1)) / RDS.close.shift(1))*100

#%% [markdown]
# **Lastly** we convert the date from index to dates using datetime

#%%
RDS.index = pd.to_datetime(RDS.index)

#%% [markdown]
# And to test that the code works as expected we print the first 5 observations.

#%%
RDS.head()

#%% [markdown]
# ## **Combining the data sets**
#%% [markdown]
# **First** we combine the 3 data sets in one set called Top3_energy_stocks

#%%
Top3_energy_stocks = pd.concat([XOM,CVX,RDS])

#%% [markdown]
# And then we print the first 5 observations to test, whether the code works.

#%%
Top3_energy_stocks.head()

#%% [markdown]
# ## **Visualisations**
#%% [markdown]
# In this section we create 4 figures. One for the closing price, one for the closing price demeaned, one for the precentage growth and one for the volume. The first 3 figures shows the devolopments for each of the 3 firms. We added a widget, which allows the reader to choose which firms to consider (The widget is by default set to look at all 3 firms). The last figure shows the volume, which has been divided into the 5 weekdays. 
#%% [markdown]
# ### Closing price

#%%
def Fig1():
    
    def fig(temp1, temp2, temp3):
        if temp1 == True:
            XOM.groupby('firm')['close'].plot(legend=True, color='green')
        if temp2 == True:
            CVX.groupby('firm')['close'].plot(legend=True, color='blue')
        if temp3 == True:
            RDS.groupby('firm')['close'].plot(legend=True, color='orange')

        plt.xlabel('Date')
        plt.ylabel('Dollars')
        plt.title('Figure 1: Closing price')

    widgets.interact(fig,
           temp1=widgets.Checkbox(description='Exxon', value=True, disabled=False),
           temp2=widgets.Checkbox(description='Chevron', value=True, disabled=False),
           temp3=widgets.Checkbox(description='Royal Dutch Shell', value=True, disabled=False),
        );

Fig1()

#%% [markdown]
# We note that Chevron has the highest stockprice in the period. We also see that both Shell's and Chevron's stockprice have increased in the period, while Exxon's stockprice has been more stable. All firms seems to follow the same trend, which is seen clearly illustrated during the first quarter of 2018, where all the stockprices fell simultaneously. 
# They co-move to some extend, which - among other things - might be due to them operating in the same industri (Energy production). Some market shocks are reltated to specific industries, while other are more generel. This means that firms operating in same industries tend to covariate more than firms from different industries. Some individual shock occur as well, but all the big shocks seems to take effect across the firms.  
#%% [markdown]
# ### Closing price demeaned

#%%
def Fig2():
    
    def fig(temp1, temp2, temp3):
        if temp1 == True:
            XOM.groupby('firm')['close_demeaned'].plot(legend=True, color='green')
        if temp2 == True:
            CVX.groupby('firm')['close_demeaned'].plot(legend=True, color='blue')
        if temp3 == True:
            RDS.groupby('firm')['close_demeaned'].plot(legend=True, color='orange')
        
        plt.xlabel('Date')
        plt.ylabel('Dollars')
        plt.title('Figure 2: Closing price demeaned')

    widgets.interact(fig,
           temp1=widgets.Checkbox(description='Exxon', value=True, disabled=False),
           temp2=widgets.Checkbox(description='Chevron', value=True, disabled=False),
           temp3=widgets.Checkbox(description='Royal Dutch Shell', value=True, disabled=False),
        );

Fig2()

#%% [markdown]
# Here we clearly see that both Chevron's and Shell's stockprice has risen since 2016 and almost at the same level, but since Chevron's stocksprice is higher than Shell's, it means that Shell's stockprice has risen relativly more in the period. Exxon's stockprice is almost at the same level as in 2016, and it only fluctuates around its average.
#%% [markdown]
# ### Percentage change in the closing price

#%%
XOM_C=XOM.copy()
XOM_C=XOM.dropna(subset=['percentage_change, %'])
CVX_C=CVX.copy()
CVX_C=CVX.dropna(subset=['percentage_change, %'])
RDS_C=RDS.copy()
RDS_C=RDS.dropna(subset=['percentage_change, %'])

def Fig3():
    
    def fig(temp1, temp2, temp3):
        if temp1 == True:
            XOM_C.groupby('firm')['percentage_change, %'].plot(legend=True, color='green')
        if temp2 == True:
            CVX_C.groupby('firm')['percentage_change, %'].plot(legend=True, color='blue')
        if temp3 == True:
            RDS_C.groupby('firm')['percentage_change, %'].plot(legend=True, color='orange')
        
        plt.xlabel('Date');
        plt.ylabel('Percent');
        plt.title('Figure 3: Percentage change in closing price');

    widgets.interact(fig,
           temp1=widgets.Checkbox(description='Exxon', value=True, disabled=False),
           temp2=widgets.Checkbox(description='Chevron', value=True, disabled=False),
           temp3=widgets.Checkbox(description='Royal Dutch Shell', value=True, disabled=False),
        );

Fig3()

#%% [markdown]
# Looking at the percentage change we see that they all more or less comove. We also see that the percentage change in the stockprice for both Shell and Chevron lies slightly above 0, which is consistent with figure 1 and 2. In this figure we also see the outliers more clearly, and espicially the decrease in Shell's stockprice in medio 2016. 
#%% [markdown]
# ### Volume grouped by weekdays

#%%
Top3_energy_stocks_C=Top3_energy_stocks.copy()
Top3_energy_stocks_C['Weekday'] = Top3_energy_stocks_C.index.weekday
ax1 = Top3_energy_stocks_C.groupby('Weekday')['volume'].mean().plot(kind='bar', color='purple') 
ax1.set_ylabel('Average number of traded stocks')
ax1.set_title('Figure 4: Average number of traded stocks divided by weekdays')
ax1.set_xlabel('')
plt.xticks(np.arange(5),('Monday','Tuesday','Wednesday','Thursday','Friday'), rotation='horizontal')
for txt in ax1.texts:
    txt.set_visible(False)

#%% [markdown]
# Here we see that the average number of traded stocks is rising through the week, which means that the number of traded stocks monday is less than the traded stocks friday. We also see that the average number of traded stocks on a weekday is approximately 7 billion.
#%% [markdown]
# ## **Descriptive statistics**
#%% [markdown]
# First we define all of the statistical variables, that we are going to use to describe our dataset.

#%%
# First we find the number of observations (Remember that precentage change is missing the first value for each firm)
Observations=round(Top3_energy_stocks['close'].count(),0)

# Next we find the average
Avg_closing_price=round(Top3_energy_stocks['close'].mean(),2)
Avg_volume=round(Top3_energy_stocks['volume'].mean(),2)
Avg_closing_demeaned=round(Top3_energy_stocks['close_demeaned'].mean(),2)


#%%
# First we find the observations
Observations_XOM=round(XOM['close'].count(),0)

# Next we find the average (Here we notice that since we got precentage change, we need to use a formula to calculate the average precentage change)
Avg_closing_price_XOM=round(XOM['close'].mean(),2)
Avg_volume_XOM=round(XOM['volume'].mean(),2)
Avg_closing_demeaned_XOM=round(XOM['close_demeaned'].mean(),2)
Avg_precentage_change_XOM=round(((XOM.close[-1]/XOM.close[0])**(1/Observations_XOM)-1)*100,2)

# Next we calculate the standard diviation
Std_closing_price_XOM=round(XOM['close'].std(),2)
Std_volume_XOM=round(XOM['volume'].std(),2)
Std_close_demeaned_XOM=round(XOM['close_demeaned'].std(),2)

# Next we find the minimum value and which day this occured
Min_closing_price_XOM=round(XOM['close'].min(),2)
Min_volume_XOM=round(XOM['volume'].min(),2)
Min_close_demeaned_XOM=round(XOM['close_demeaned'].min(),2)

# Next we find the maximum value and which day this occured
Max_closing_price_XOM=round(XOM['close'].max(),2)
Max_volume_XOM=round(XOM['volume'].max(),2)
Max_close_demeaned_XOM=round(XOM['close_demeaned'].max(),2)

# And lastly we find the median, which we do by first finding the middle observation
XOM_median_obs=(Observations_XOM)//2
Median_closing_price_XOM=round(XOM.close[XOM_median_obs],2)
Median_volume_XOM=round(XOM.volume[XOM_median_obs],2)
Median_closing_demeaned_XOM=round(XOM.close_demeaned[XOM_median_obs],2)


#%%
# First we find the observations
Observations_CVX=round(CVX['close'].count(),0)

# Next we find the average (Here we notice that since we got precentage change, we need to use a formula to calculate the average precentage change)
Avg_closing_price_CVX=round(CVX['close'].mean(),2)
Avg_volume_CVX=round(CVX['volume'].mean(),2)
Avg_closing_demeaned_CVX=round(CVX['close_demeaned'].mean(),2)
Avg_precentage_change_CVX=round(((CVX.close[-1]/CVX.close[0])**(1/Observations_CVX)-1)*100,2)

# Next we calculate the standard diviation
Std_closing_price_CVX=round(CVX['close'].std(),2)
Std_volume_CVX=round(CVX['volume'].std(),2)
Std_close_demeaned_CVX=round(CVX['close_demeaned'].std(),2)

# Next we find the minimum value and which day this occured
Min_closing_price_CVX=round(CVX['close'].min(),2)
Min_volume_CVX=round(CVX['volume'].min(),2)
Min_close_demeaned_CVX=round(CVX['close_demeaned'].min(),2)

# Next we find the maximum value and which day this occured
Max_closing_price_CVX=round(CVX['close'].max(),2)
Max_volume_CVX=round(CVX['volume'].max(),2)
Max_close_demeaned_CVX=round(CVX['close_demeaned'].max(),2)

# And lastly we find the median, which we do by first finding the middle observation
CVX_median_obs=(Observations_CVX)//2
Median_closing_price_CVX=round(CVX.close[CVX_median_obs],2)
Median_volume_CVX=round(CVX.volume[CVX_median_obs],2)
Median_closing_demeaned_CVX=round(CVX.close_demeaned[CVX_median_obs],2)


#%%
# First we find the observations
Observations_RDS=round(RDS['close'].count(),0)

# Next we find the average (Here we notice that since we got precentage change, we need to use a formula to calculate the average precentage change)
Avg_closing_price_RDS=round(RDS['close'].mean(),2)
Avg_volume_RDS=round(RDS['volume'].mean(),2)
Avg_closing_demeaned_RDS=round(RDS['close_demeaned'].mean(),2)
Avg_precentage_change_RDS=round(((RDS.close[-1]/RDS.close[0])**(1/Observations_RDS)-1)*100,2)

# Next we calculate the standard diviation
Std_closing_price_RDS=round(RDS['close'].std(),2)
Std_volume_RDS=round(RDS['volume'].std(),2)
Std_close_demeaned_RDS=round(RDS['close_demeaned'].std(),2)

# Next we find the minimum value and which day this occured
Min_closing_price_RDS=round(RDS['close'].min(),2)
Min_volume_RDS=round(RDS['volume'].min(),2)
Min_close_demeaned_RDS=round(RDS['close_demeaned'].min(),2)

# Next we find the maximum value and which day this occured
Max_closing_price_RDS=round(RDS['close'].max(),2)
Max_volume_RDS=round(RDS['volume'].max(),2)
Max_close_demeaned_RDS=round(RDS['close_demeaned'].max(),2)

# And lastly we find the median, which we do by first finding the middle observation
RDS_median_obs=(Observations_RDS)//2
Median_closing_price_RDS=round(RDS.close[RDS_median_obs],2)
Median_volume_RDS=round(RDS.volume[RDS_median_obs],2)
Median_closing_demeaned_RDS=round(RDS.close_demeaned[RDS_median_obs],2)

#%% [markdown]
# And then we combine all the variables in one table

#%%
TableL1 = pd.DataFrame({'All firms':Observations,'Exxon Mobile':Observations_XOM,'Chevron':Observations_CVX,'Shell':Observations_RDS}, index=['Observations'])

TableLL = pd.DataFrame({'All firms':'','Exxon Mobile':'','Chevron':'','Shell':''}, index=[''])

TableL2 = pd.DataFrame({'All firms':'','Exxon Mobile':'','Chevron':'','Shell':''}, index=['Closing price'])
TableL3 = pd.DataFrame({'All firms':Avg_closing_price,'Exxon Mobile':Avg_closing_price_XOM,'Chevron':Avg_closing_price_CVX,'Shell':Avg_closing_price_RDS}, index=['Average'])
TableL4 = pd.DataFrame({'All firms':'','Exxon Mobile':Std_closing_price_XOM,'Chevron':Std_closing_price_CVX,'Shell':Std_closing_price_RDS}, index=['Standard deviation'])
TableL5 = pd.DataFrame({'All firms':'','Exxon Mobile':Min_closing_price_XOM,'Chevron':Min_closing_price_CVX,'Shell':Min_closing_price_RDS}, index=['Minimum'])
TableL6 = pd.DataFrame({'All firms':'','Exxon Mobile':Max_closing_price_XOM,'Chevron':Max_closing_price_CVX,'Shell':Max_closing_price_RDS}, index=['Maximum'])
TableL7 = pd.DataFrame({'All firms':'','Exxon Mobile':Median_closing_price_XOM,'Chevron':Median_closing_price_CVX,'Shell':Median_closing_price_RDS}, index=['Median'])

TableL8 = pd.DataFrame({'All firms':'','Exxon Mobile':'','Chevron':'','Shell':''}, index=['Closing price demeaned'])
TableL9 = pd.DataFrame({'All firms':Avg_closing_demeaned,'Exxon Mobile':Avg_closing_demeaned_XOM,'Chevron':Avg_closing_demeaned_CVX,'Shell':Avg_closing_demeaned_RDS}, index=['Average'])
TableL10 = pd.DataFrame({'All firms':'','Exxon Mobile':Std_close_demeaned_XOM,'Chevron':Std_close_demeaned_CVX,'Shell':Std_close_demeaned_RDS}, index=['Standard deviation'])
TableL11 = pd.DataFrame({'All firms':'','Exxon Mobile':Min_close_demeaned_XOM,'Chevron':Min_close_demeaned_CVX,'Shell':Min_close_demeaned_RDS}, index=['Minimum'])
TableL12 = pd.DataFrame({'All firms':'','Exxon Mobile':Max_close_demeaned_XOM,'Chevron':Max_close_demeaned_CVX,'Shell':Max_close_demeaned_RDS}, index=['Maximum'])
TableL13 = pd.DataFrame({'All firms':'','Exxon Mobile':Median_closing_demeaned_XOM,'Chevron':Median_closing_demeaned_CVX,'Shell':Median_closing_demeaned_RDS}, index=['Median'])

TableL14 = pd.DataFrame({'All firms':'','Exxon Mobile':'','Chevron':'','Shell':''}, index=['Precentage change in closing price'])
TableL15 = pd.DataFrame({'All firms':'','Exxon Mobile':Avg_precentage_change_XOM,'Chevron':Avg_precentage_change_CVX,'Shell':Avg_precentage_change_RDS}, index=['Average'])

TableL16 = pd.DataFrame({'All firms':'','Exxon Mobile':'','Chevron':'','Shell':''}, index=['Volume'])
TableL17 = pd.DataFrame({'All firms':Avg_volume,'Exxon Mobile':Avg_volume_XOM,'Chevron':Avg_volume_CVX,'Shell':Avg_volume_RDS}, index=['Average'])
TableL18 = pd.DataFrame({'All firms':'','Exxon Mobile':Std_volume_XOM,'Chevron':Std_volume_CVX,'Shell':Std_volume_RDS}, index=['Standard deviation'])
TableL19 = pd.DataFrame({'All firms':'','Exxon Mobile':Min_volume_XOM,'Chevron':Min_volume_CVX,'Shell':Min_volume_RDS}, index=['Minimum'])
TableL20 = pd.DataFrame({'All firms':'','Exxon Mobile':Max_volume_XOM,'Chevron':Max_volume_CVX,'Shell':Max_volume_RDS}, index=['Maximum'])
TableL21 = pd.DataFrame({'All firms':'','Exxon Mobile':Median_volume_XOM,'Chevron':Median_volume_CVX,'Shell':Median_volume_RDS}, index=['Median'])

Table1 = pd.concat([TableL1,TableLL,TableL2,TableL3,TableL4,TableL5,TableL6,TableL7,TableLL,TableL8,TableL9,TableL10,TableL11,TableL12,TableL13,TableLL,TableL14,TableL15,TableLL,TableL16,TableL17,TableL18,TableL19,TableL20,TableL21])

Table1

#%% [markdown]
# In the table we see that the number of observations add up since there are 808 in each of the firms dataset and 2424 in the collective dataset. When we look at the closing price, we see that the average closing price is highest for Chevron (104.5 dollars), which we also saw in figure 1. Shell has the lowest (average) stock price, which is 55.26 dollars. When considering the volatility we see that Chevron and Shell are more volatile than Exxon, which we also see when looking at the highest and lowest stock price in the period for each of the 3 firms. Here we see that the spand between min and max for Exxon is much smaller than it is for Chevron and Shell. The closing price demeaned average is 0 for all firms and the standard deviation is the same as for closing price. This is due to the definitation of the variable. We also see that Chevron experienced both the highest postive change (22.87 dollars) and negative change (-35.16 dollars), although we would anticipate this since Chevron's stockprice is higher in terms of an absolute value. When we look at the average change in the closing price, we get that Shell has grown relativly more than the 2 other firms. Shell has an average percentage change in the closing price at 0.07% per day. Lastly, we look at the volume, where we see that Exxon is the most traded stock with an average of 12.4 billion stocks traded a day, this can be explained by the lower price compared to Chevron. The reason why Shell doesn't get traded as much could be the number of shares and because we only look at the B-shares. When looking at the maksimum number of traded stocks, we see that one day the Exxon stocks were traded 47,3 billion times. And when looking at the minimum we see that only 436.660 of the Shell stock was traded one day.

