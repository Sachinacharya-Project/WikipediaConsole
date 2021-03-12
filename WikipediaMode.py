import pyttsx3, speech_recognition as sr, wikipedia, os, time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')[0].id
engine.setProperty('voice', voices)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listenning...")
        r.pause_threshold = 1
        r.energy_threshold = 1000
        audio = r.listen(source)
        query = "Cannot Understand"
        try:
            print('Recognizing...')
            query = r.recognize_google(audio)
            print('Search Keyword: {}'.format(query))
        except Exception:
            print('Cannot Recognize what you said... :)')
        return query

def print_menus():
    print("""Choose Modes:
    1. Handles Mode
    2. Podcast Mode
    3. General Mode
    98. Clear Screen
    99. Exit
    """)
def search_contents(query):
    """Returns
    False: ask to break
    """
    query = str(query)
    if query.lower() == 'exit()' or query.lower() == 'exit program':
        print("Thanks for Using Our Services")
        speak("Thanks for Using Our Services")
        exit()
    elif query.lower() == 'menu()' or query.lower() == 'show menu' or query.lower() == 'show menus':
        return False
    elif query.lower() == 'clear()' or query.lower() == 'clear screen':
        os.system('cls')
        return ''
    else:
        data = 'Cannot Found Data'
        try:
            data = wikipedia.wikipedia.summary(query)
        except Exception:
            print('Sorry, Cannot find the result.\nPerhaps, try with another keyword which is more accurate')
        return data
if __name__ == '__main__':
    print('Welcome To Wikipedia Console')
    while True:
        print_menus()
        menu = input('Option: ')
        mode = ''
        if menu.isdigit():
            if int(menu) == 1:
                mode = 'handless'
            elif int(menu) == 2:
                mode = 'podcast'
            elif int(menu) == 3:
                mode = 'general'
            elif int(menu) == 99:
                print('Thanks for using OUR SERVICE')
                exit()
            elif int(menu) == 98:
                os.system('cls')
                continue
            else:
                print('Invalid Option choosed')
                continue
        elif menu == '':
            continue
        else:
            print('Invalid Option choosed')
            continue
        while True:
            if mode == 'general':
                query = search_contents(input("Search Keyword: "))
                if query == False:
                    break
                elif query == '':
                    pass
                else:
                    print(query)
            elif mode == 'handless':
                print('Example: Search Dextrose')
                data = str(takeCommand())
                query = ''
                if data == 'Cannot Understand':
                    query = ''
                    pass
                else:
                    query = search_contents(data.replace('search ', '', 1))
                if query == False:
                    break
                elif query == '':
                    pass
                else:
                    print(query)
                    speak(query)
                    query = ''
            elif mode == 'podcast':
                query = search_contents(input('Search Keyword: '))
                if query == False:
                    break
                elif query == '':
                    pass
                else:
                    print(query)
                    speak(query)
                    query = ''
            else:
                exit()