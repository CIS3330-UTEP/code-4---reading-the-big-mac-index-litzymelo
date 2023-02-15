import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code):
    country_code = country_code.upper()
    df = pd.read_csv(big_mac_file)
    query=(f"{iso_a3} == '{year}'and date > {year}-01-01 and date < {year}-12-31")
    result_df = df.query(f"{iso_a3} == '{year}'and date > {year}-01-01 and date < {year}-12-31")
    result = (round(result_df['dollar_price'].mean(),2))
    return result
    

def get_big_mac_price_by_country(country_code):
    country_code = country_code.upper()
    df = pd.read_csv(big_mac_file)
    query = (f"{iso_a3}=='{name}')
    result_df = df.query(f"{iso_a3}=='{name}')
    (round(result_df['dollar_price'].mean(),2))
    return result_df
    

def get_the_cheapest_big_mac_price_by_year(year):



    
  
    

def get_the_most_expensive_big_mac_price_by_year(year):
   


    
if __name__ == "__main__":
    
    