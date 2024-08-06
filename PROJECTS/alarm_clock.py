from playsound import playsound
import time

#playsound('D:\python folder\PROJECTS\songalarm.mp3')

clearscreen = '\033[2J' # clears the terminal screen 
movecursor = '\033[H'  # moves the cursor to the top left corner 

runtime =int( input('Enter the runtime for the alarm: '))
def alarm_clock(runtime):
    print(clearscreen)
    timecount = 0

    while timecount < runtime:
        timecount+=1
        time.sleep(1)
        timeleft = runtime - timecount
        seceondsleft = timeleft % 60
        minutesleft = timeleft // 60
        print(f'{movecursor}{minutesleft:02d}:{seceondsleft:02d}')
    print("Good Luck for the rest of the day !\nLet's Groove first !!\n")
    for i in range(60):
        playsound("D:/python folder/PROJECTS/alarm.wav")
if __name__ == '__main__':
    
    alarm_clock(runtime)