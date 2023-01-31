import pandas as pd
data=pd.DataFrame.from_dict(
    {
        'Product':['Table','Desktop','Bed','Dressing table'],
        'Selling Price':[1500,3000,2000,5700],
        'Profit':[500,500,200,800],
        'Shipping mode': ['First class', 'Second class', 'Same day','Standard class'],
        'Destination': ['Hyderabad','Chenani','Noida','Mumbai']

    }
)
def surcharge(x):
    if x=="Same day":
        return 0.2
    elif x=="First class":
        return 0.1
    elif x=="Standard class":
        return 0.5
    else:
        return 0
data["Surcharge"]=data["Shipping mode"].apply(surcharge)
data["Total cost"]=((data['Selling Price']-data['Profit'])*(1+data['Surcharge'])).apply(int)
print(data)