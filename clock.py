import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"The alarm is set for {alarm_time}")
    sound_file = "music.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("Wake UP!!!!!")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False
        time.sleep(1)

def main():
    alarm_time = input("Set the Alarm Time (HH:MM:SS): ")
    set_alarm(alarm_time)

if __name__ == "__main__":
    main()

