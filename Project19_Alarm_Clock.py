# Python Alarm Clock
import time # this will help to update the time
import datetime # It allows string representation of time
# First pygame needs to be installed, in the terminal >> pip install pygame
import pygame 


def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "Wooden_Train_Whistle.mp3" # Relative path of the music located in this directory...
    is_running = True
    
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        
        if current_time == alarm_time:
            print("Wakeeyyyy Wakeeyyyy !!! 😴")
            
            # mixer is a module for loading and playing sounds
            pygame.mixer.init() #init is used to call the constructor
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            
            is_running = False
        
        time.sleep(1)
        # is_running = False

# IF we directly run this specific python file
if __name__ == "__main__":
    print("\n")
    alarm_time = input("Enter the Alarm Time (HH:MM:SS): ")
    set_alarm(alarm_time) 