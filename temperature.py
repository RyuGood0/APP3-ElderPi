from sense_hat import SenseHat

sense = SenseHat()

def temperature():
    temp = sense.get_temperature()
    

    # alternatives
    #rhasspy.text_to_speech('il fait ' + str(round(temp,2) + 'degrés'))
    print('il fait ' + str(round(temp,2)) + ' degrés')
temperature()
    
    