# -*- coding: utf-8 -*-

import scraper
import time
import pandas as pd

#
scroll_range = 200
main_list = []


def main ():
    sc = scraper.Scraper()
    sc.load_url()
    car_count = 0
    
    for scroll in range(scroll_range):
        time.sleep(1)
        sc.scroll_down()
    
    time.sleep(3)
    sc.read_data()
    
    get_hrefs_df = pd.DataFrame(sc.get_hrefs())
    get_hrefs_df.to_csv('carlist.csv', index=False)
    
    
    for h in sc.get_hrefs()[887:]:
        car_info = sc.get_features('https://carsandbids.com' + h)
        main_list.append(car_info)
        
        car_count = car_count + 1
        print('car count =', car_count)
    
    main_list_df = pd.DataFrame(main_list)
    main_list_df.to_csv('full2.csv', index=False)
     
if __name__ == '__main__':
    main()