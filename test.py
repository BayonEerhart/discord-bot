import datetime
import json
import pytz
import re


def test(p_message):

    if p_message == "!zone":
        zones = ['gmt', 'cet', 'eet', 'europe/moscow', 'asia/dubai', 'asia/riyadh', 'asia/kolkata', 'asia/dhaka', 'asia/bangkok', 'asia/shanghai', 'asia/tokyo', 'australia/sydney', 'pacific/auckland', 'pacific/honolulu', 'america/anchorage', 'america/los_angeles', 'america/denver', 'america/chicago', 'america/new_york', 'america/argentina/buenos_aires', 'america/sao_paulo', 'europe/lisbon', 'atlantic/azores', 'etc/gmt+12']
        max_len = max(len(zone) for zone in zones)
        back = ""
        for zone in zones:
            current_time = datetime.datetime.now(pytz.timezone(zone)).strftime('%H:%M:%S')
        
            formatted_zone = zone.ljust(max_len)
        
            back += f"{formatted_zone}: {current_time}\n"


        return back

print(test("!zone"))

 
 


 

 
 
 
 
 
 
 
 
 