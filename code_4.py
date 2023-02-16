import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code):
    country_code = country_code.upper()
    df = pd.read_csv(big_mac_file)
    query=(f"iso_a3 == '{country_code}'and date > '{year}-01-01' and date < '{year}-12-31'")
    # print(query)
    result_df = df.query(query)
    result = round(result_df['dollar_price'].mean(),2)
    return result
    

def get_big_mac_price_by_country(country_code):
    country_code = country_code.upper()
    df = pd.read_csv(big_mac_file)
    query = (f"iso_a3 == '{country_code}'and name")
    result_df = df.query(query)
    result = round(result_df['dollar_price'].mean(),2)
    return result


def get_the_cheapest_big_mac_price_by_year(year): 
    df = pd.read_csv(big_mac_file)
    query = (f"date > '{year}-01-01' and date < '{year}-12-31'")
    result_df = df.query(query)
    result = round(result_df['dollar_price'].min(),2)
    min_index = result_df['dollar_price'].idxmin()
    minrow = result_df.loc[min_index]
    result_message = f"{minrow['name']}({minrow['iso_a3']}): ${round(minrow['dollar_price'],2)}"
    return result_message


def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    query = (f"date > '{year}-01-01' and date < '{year}-12-31'")
    result_df = df.query(query)
    result = round(result_df['dollar_price'].max(),2)
    max_index = result_df['dollar_price'].idxmax()
    maxrow = result_df.loc[max_index]
    #print (maxrow)
    #print(type(maxrow))
    result_message = f"{maxrow['name']}({maxrow['iso_a3']}): ${round(maxrow['dollar_price'],2)}"
    #print(result_message)
    return result_message
    

    
if __name__ == "__main__":

   # print(get_big_mac_price_by_year("2012", "ARG")) 

   # print(get_big_mac_price_by_country("ARG"))

   print(get_the_cheapest_big_mac_price_by_year("2008"))

   #print(get_the_most_expensive_big_mac_price_by_year("2014"))
