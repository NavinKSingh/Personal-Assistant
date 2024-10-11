from output1 import output
from time1 import get_time, get_date
from input1 import take_input
from database import *
from connection import check_internet_connection, check_on_wikipedia
import assistant
from web1 import open_facebook, open_google, open_youtube, close_browser
from song import *
from news import get_news
from temperature import temperature
from background import update_wallpaper
from calculator import get_calculator
from notepad import get_notepad
from game import get_game
def process(query):
    answer = get_answer_from_memory(query)
    
    if answer == "get time details":
        return ("Time is " + get_time())
    
    elif answer == "check internet connection":
        if check_internet_connection():
            return "Internet is connected"
        else:
            return "Internet is not connected"
    
    elif answer == "hi":
        return "Hello sir"
    
    elif answer == "bye":
        return "Bye sir! See you soon"
    
    elif answer == "identity":
        return "I am your personal assistant"
    
    elif answer == "made":
        return "I was created by Navin"
    
    elif answer == "use":
        return "I am here to assist you"
    
    elif answer == "yourself":
        return "I am fine"
    
    elif answer == "yes":
        return "That's great!"
    
    elif answer == "play sound":
        return play_music_folder(folder_path)
    
    elif answer == "calculator":
        return get_calculator()
    
    elif answer == "game":
        return get_game()
    
    elif answer == "news":
        return get_news()
    
    elif answer == "temperature":
        return temperature()
    
    elif answer == "notepad":
        return get_notepad()
    
    elif answer == "wallpaper":
        return update_wallpaper()
    
    elif answer == "tell_date":
        return "Date is " + get_date()
    
    elif answer == "open facebook":
        open_facebook()
        return "Opening Facebook"
    
    elif answer == "open google":
        open_google()
        return "Opening Google"
    
    elif answer == "open tube":
        open_youtube()
        return "Opening YouTube"
    
    elif answer == "close browser":
        close_browser()
        return "Browser is closed"
    
    elif answer == "change name":
        output("What do you want to call me?")
        temp = take_input()
        if temp == assistant.name:
            return "This is already my name."
        else:
            update_name(temp)
            assistant.name = temp
            return "Now I am " + temp
        
    else:
        output("Should I search on the internet?")
        ans = take_input()
        if "yes" in ans:
            answer = check_on_wikipedia(query)
            if answer != "":
                return answer
        else:
            output("Can you please tell me what it means?")
        answer = take_input()
        if "it means" in answer:
            answer = answer.replace("it means", "")
            answer.strip()
            value = get_answer_from_memory(answer)
            if value == "":
                return "Can't help with this one."
            else:
                insert_question_and_answer(query, value)
                return "Thanks! I will remember it for the next time."
        else:
            return "Cannot understand."
