import time
import requests
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import wikipedia
import pyjokes
import pywhatkit
from os import listdir
from os.path import isfile, join
import pyautogui
import keyboard

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the voice for the assistant
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user's voice input
def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            voice_data = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            voice_data = ''
        except sr.RequestError:
            voice_data = ''
        return voice_data.lower()

def listen2():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            voice_data = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            voice_data = ''
        except sr.RequestError:
            voice_data = ''
        return voice_data

speak("Hey")
time.sleep(0.2)
speak("I'm alexa")
time.sleep(0.5)
speak("How can I assist you?")

# Function to process user's voice input and provide responses
def process_command(voice_data):
    try:  
        command = voice_data
        if 'wake up' in voice_data:
            speak("I am online")
        elif 'open website' in voice_data:
            speak("Sure, which website would you like me to open?")
            website = listen()
            try:
                if website:
                    url = f"https://www.{website}.com"
                    webbrowser.open(url)
                    speak(f"Opening {website} in your browser.")
                else:
                    speak("I'm sorry, please tell me again.")
            except:
                    speak("I did not hear")
                #Open application or folder in c/user/atanu
        elif 'open folder' in voice_data:
            speak("Which folder or application in atanu folder?")
            try:
               application = listen2()
               if application:
                   os.startfile(application)
                   speak(f"Opening {application}.")
               else:
                   speak("I'm sorry, I didn't catch the name.")
            except:
                speak("file not found")
        
        elif 'play' in command:
            command = command.replace('alexa', '')
            song = command.replace('play', '')
            try:
               speak('Playing ' + song)
               pywhatkit.playonyt(song)
            except:
               speak("I did not hear")
    
        elif 'time' in command:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            speak('The current time is ' + current_time)
        elif 'what is' in command or 'who' in command:
            try:
                person = command.replace('alexa', '')
                info = wikipedia.summary(person, sentences=2)
                print(info)
                speak(info)
            except:("i did not hear your voice")
    
        elif 'date' in command:
            speak("Sorry, I have a headache.")
        elif 'are you single' in command:
            speak('I am in a relationship with Wi-Fi.')
        elif 'joke' in command:
            try:
              speak(pyjokes.get_joke())
            except:("i did not hear your voice")
    
        elif 'code' in voice_data:
            speak('Please Wait a Moment Wile Generating From an Ai' + voice_data.split('code')[1])
            a = voice_data.lstrip("alexa ")
            search_query = a.replace(" ", "+")
            url = 'https://www.perplexity.ai/search?q=' + search_query
            try:
                webbrowser.get().open(url)
                time.sleep(1)
                speak('Wait a moment')
            except:
                speak('Please check your Internet')
        
        elif 'search' in voice_data:
            speak('searching' + voice_data.split('search')[1])
            a = voice_data.lstrip("alexa ")
            a = a.lstrip("search ")
            search_query = a.replace(" ", "+")
            url = 'https://www.google.com/search?q=' + search_query
            try:
                webbrowser.get().open(url)
                time.sleep(1)
                speak('Wait a moment')
            except:
                speak('Please check your Internet')
    
        elif 'write' in voice_data:
            speak('Please Wait a Moment Wile Generating From an Ai' + voice_data.split('write')[1])
            a = voice_data.lstrip("alexa ")
            search_query = a.replace(" ", "+")
            url = 'https://www.perplexity.ai/search?q=' + search_query
            try:
                webbrowser.get().open(url)
                time.sleep(1)
                speak('Wait a moment')
            except:
                speak('Please check your Internet')
                
        elif 'give' in voice_data:
            speak('Please Wait a Moment Wile Generating From an Ai' + voice_data.split('give')[1])
            a = voice_data.lstrip("alexa ")
            search_query = a.replace(" ", "+")
            url = 'https://www.perplexity.ai/search?q=' + search_query
            try:
                webbrowser.get().open(url)
                time.sleep(1)
                speak('Wait a moment')
            except:
                speak('Please check your Internet')
                
        elif 'tell' in voice_data:
            speak('Please Wait a Moment Wile Generating From an Ai' + voice_data.split('tell')[1])
            a = voice_data.lstrip("alexa ")
            search_query = a.replace(" ", "+")
            url = 'https://www.perplexity.ai/search?q=' + search_query
            try:
                webbrowser.get().open(url)
                time.sleep(1)
                speak('Wait a moment')
            except:
                speak('Please check your Internet')
        elif "weather" in voice_data:
            try:
                api_key="8ef61edcf1c576d65d836254e11ea420"
                base_url="https://api.openweathermap.org/data/2.5/weather?"
                speak("whats the city name")
                city_name=listen()
                complete_url=base_url+"appid="+api_key+"&q="+city_name
                response = requests.get(complete_url)
                x=response.json()
                if x["cod"]!="404":
                    y=x["main"]
                    current_temperature = y["temp"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    current_temperature=current_temperature-273.15
                    speak(" Temperature  is " +
                          str(current_temperature) +"Degree Celcious" +
                          "\n humidity in percentage is " +
                          str(current_humidiy) +
                          "\n description =\n" +
                          str(weather_description))
                    print(" Temperature  is " +
                          str(current_temperature) +"Degree Celcious" +
                          "\n humidity (in percentage) = " +
                          str(current_humidiy) +
                          "\n description =\n " +
                          str(weather_description))
    
                else:
                    speak(" City Not Found ")
            except:
                speak("Server Error")
                        
        elif 'pause' in command:
            # Simulate spacebar press to pause/play
            try:    
                keyboard.press('space')
                keyboard.release('space')
                speak("Playback paused.")
            except:("i did not hear your voice")   
         
        elif 'fast' in command:
                # Simulate spacebar press to >
            try:
                keyboard.press('shift')
                keyboard.press('>')
                
                keyboard.release('shift')
                keyboard.release('>')
                speak("speed fast.")
            except:("i did not hear your voice")
        
        elif 'slow' in command:
                # Simulate spacebar press to <
            try:
                keyboard.press('shift')
                keyboard.press('<')
                
                keyboard.release('shift')
                keyboard.release('<')
                speak("speed Slowed.")
            except:("i did not hear your voice")
        
        elif 'full' in command:
                # Simulate spacebar press to full screen
            try:
                keyboard.press('f')
                keyboard.release('f')
                speak("full screen.")
            except:("i did not hear your voice")            
        elif 'skip' in command:
                # Simulate spacebar press to right
            try:
                keyboard.press('right')
                keyboard.release('right')
                speak("skipped 5 seconds.")
            except:("i did not hear your voice")
    
        elif 'skip ten' in command:
                # Simulate spacebar press to l
            try:
                keyboard.press('l')
                keyboard.release('l')
                speak("skipped 10 seconds.")
            except:("i did not hear your voice")
    
        elif 'next' in command:
                # Simulate right arrow press to play next video
            try:
                keyboard.press('shift')
                keyboard.press('n')
                
                keyboard.release('shift')
                keyboard.release('n')
                speak("Playing next video.")
            except:("i did not hear your voice")
    
        elif 'previous' in command:
                # Simulate left arrow press to play previous video
            try:
                keyboard.press('shift')
                keyboard.press('p')
                
                keyboard.release('shift')
                keyboard.release('p')
                speak("Playing previous video.")
            except:("i did not hear your voice")
    
        elif 'mute' in command:
                # Simulate left arrow press to play previous video
            try:
                keyboard.press('m')
                keyboard.release('m')
                speak("Video is now mute.")
            except:("i did not hear your voice")
        
        elif 'volume up' in command:
                # Simulate left arrow press to volume up
            try:
                keyboard.press('up')
                keyboard.release('up')
                speak("Volume up.")
            except:("i did not hear your voice")
    
        elif 'volume down' in command:
                # Simulate left arrow press to volume down
            try:
                keyboard.press('down')
                keyboard.release('down')
                speak("Volume down.")
            except:("i did not hear your voice")
        
        elif 'stop' in command:
                # Simulate spacebar press to stop playback
            try:
                keyboard.press('q')
                keyboard.release('q')
                speak("Playback stopped.")
            except:("i did not hear your voice")
    
        elif 'subtitle' in command:
                    # Simulate left arrow press to volume up
            try:
                keyboard.press('c')
                keyboard.release('c')
                speak("Subtitle.")
            except:("i did not hear your voice") 
    
        elif 'mini' in command:
                # Simulate left arrow press to volume up
            try:
                keyboard.press('i')
                keyboard.release('i')
                speak("PIP mode.")
            except:("i did not hear your voice")    
        
        elif 'volume down' in command:
                # Simulate left arrow press to play volume down
            try:
                keyboard.press('down')
                keyboard.release('down')
                speak("Volume down.")
            except:("i did not hear your voice")
    
        elif 'search video' in command:
                # Simulate left arrow press to play SEARCH
            try:
                speak("Tell the video name?")
                search_query = listen()
                if search_query:
                    pywhatkit.playonyt(search_query)
                    speak("Searching " + search_query + ".")
                else:
                    speak("I'm sorry, I didn't catch hear your voice.")
            except:("i did not hear your voice")
    
    
    
                # open a drive folder navigation
    
        # elif 'open' in voice_data and ('drive' in voice_data or 'folder' in voice_data or 'file' in voice_data):
        #     speak("Sure, please provide the details of the drive, folder, and file.")
        #     path = ['D:\\']
        #     current_folder = ''
        #     while True:
        #         user_input = listen().lower()
        #         if 'drive' in user_input:
        #             speak("Tell the drive name?")
        #             drive = listen2()
        #             print('drive')
        #             drive = user_input.split()[0]
        #             current_folder = fr"{drive}:/"
        #             path.append(current_folder)
        #             speak(f"Opening {drive} drive.")
        #         elif 'folder' in user_input:
        #             speak("Tell the folder name?")
        #             folder = listen2()
        #             print(folder)
        #             folder = ' '.join(user_input.split()[1:])
        #             current_folder = os.path.join(current_folder, folder)
        #             path.append(current_folder)
        #             speak(f"Opening folder {folder}.")
        #         elif 'back' in user_input:
        #             if len(path) > 1:
        #                 path.pop()
        #                 current_folder = path[-1]
        #                 speak("Going back to the previous folder.")
        #             else:
        #                 speak("You are already at the root folder.")
        #         elif 'file' in user_input:
        #             file_name = ' '.join(user_input.split()[1:])
        #             file_path = os.path.join(current_folder, file_name)
        #             if os.path.isfile(file_path):
        #                 os.startfile(file_path)
        #                 speak(f"Opening file {file_name}.")
        #             else:
        #                 speak("Sorry, the specified file was not found.")
        #         elif 'stop' in user_input:
        #             speak("Stopping folder navigation.")
        #             break
        #         else:
        #             speak("Invalid command. Please try again.")
    
    
        
        elif 'screenshot' in command:
            # Take a screenshot using prnt scrn
            try:
                keyboard.press('Alt')
                keyboard.press('Prnt Scrn')
                keyboard.release('Alt')
                keyboard.release('Prnt Scrn')
                speak("Screenshot captured & Saved To Dexktop.")
            except:("i did not hear your voice")
            
        elif 'close this' in command:
            # Close app
            try:
                keyboard.press('Alt')
                keyboard.press('F4')
                keyboard.release('Alt')
                keyboard.release('F4')
                speak("App Closed.")    
            except:("i did not hear your voice")
    
        elif 'shutdown' in command:
            try:
                speak("Shutting down")
                os.system("shutdown /s /t 1")
            except:("i did not hear your voice")
        elif 'exit' in command:
            try:
                speak("Goodbye!")
                exit()
            except:("i did not hear your voice")
    except Exception as e:
        print("An error occurred:", e)
        speak("Speak loudly pease.")

# Main loop to continuously listen for user's commands
while True:
    try:
        voice_input = listen()
        process_command(voice_input)
    except Exception as e:
        print("An error occurred:", e)
        speak("Sorry,Speak loudly pease.")