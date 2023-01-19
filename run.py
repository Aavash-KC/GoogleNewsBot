import time
from news.news import News
from news.onlinekhabar import OnlineKhabar


#with News() as bot:
    #user_input=input('key words to search: ')
    
    #bot.land_first_page(user_input)
    #bot.search_your_text("नेपाल ")
    #bot.export_data()
    #bot.export_pdf()
    #time.sleep(4)

with OnlineKhabar() as bot:
    bot.land_first_page()
    #bot.get_heading()
    bot.export_data()