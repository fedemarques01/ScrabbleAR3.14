import sys
import PySimpleGUI as sg
import time

"""

"""


# ----------------  Create Form  ----------------
sg.ChangeLookAndFeel('Black')
sg.SetOptions(element_padding=(0, 0))

layout = [[sg.Text('')],
         [sg.Text('', size=(8, 2), font=('Helvetica', 20), justification='center', key='text')],
         [#sg.Button('Pause', key='button', button_color=('white', '#001480')),
          #sg.Button('Reset', button_color=('white', '#007339'), key='Reset'),
          sg.Exit(button_color=('white', 'firebrick4'), key='Exit')]]

timer_window = sg.Window('Running Timer', layout, no_titlebar=True, auto_size_buttons=False, keep_on_top=True, grab_anywhere=True)



def timer_pause(timer_window,current_time):

    #paused_time = int(round(time.time() * 100))
    paused_time = current_time
    element = timer_window['button']
    element.update(text='Run')
    return paused_time

def timer_init(start_time):
    
    current_time = start_time
    return current_time

 # --------- Display timer in timer_window --------
def timer_GUI(timer_window,current_time, mins, secs):    
    timer_window['text'].update('{:02d}:{:02d}'.format(mins, secs))
    #solucion trucha para que el usuario vea el 00:00
def timer_check(current_time,cloock):
    if (current_time == -2):
        cloock = False
    return cloock

    # --------- Read and update timer_window --------
def timer_normal(cloock,current_time,paused,timer_window):
    """
    Funcion que va dentro del loop while cloock == true y controla al timer
    """
    if not paused:
        event, values = timer_window.read(timeout=10)
        mins, secs = divmod(current_time, 60)
        time.sleep(1)
        current_time -= 1
        #current_time = (start_time - int(round(time.time() * 100))) 
            
    else:
       event, values = timer_window.read()
    if event == 'button':
        event = timer_window[event].GetText()
    # --------- Do Button Operations --------
   
    timer_GUI(timer_window,current_time, mins, secs)

    if event == 'Exit':
        current_time=-2
    
    return current_time
   

   ################ prueba  ############################

st = 11
ct = timer_init(st)

ps = False
cloock = True
while (cloock):
    ct=timer_normal(cloock,ct,ps,timer_window)
    cloock = timer_check(ct,cloock)


print("El tiempo ha terminado")
                                                                  
   
   
   
   
   
   
   
   
   
    #def countdown(t):
   # while t:
    #    mins, secs = divmod(t, 60)
    #    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    #    print(timeformat, end='\r')
    #    time.sleep(1)
    #    t -= 1

   #  timer_window['text'].update('{:02d}:{:02d}.{:02d}'.format((current_time // 100) // 60,
    #                                                              (current_time // 100) % 60,
     #                                                             current_time % 100))