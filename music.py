import buzzer
import time
 
# make a tone of 1500 Hz for 1/2 second, blocking
def thoranee_gunsang():
    bpm = 140
    t = 120/bpm
    buzzer.note("C6 C6 C6 Bb5 Eb6 C6", duration=t/2)
    buzzer.note("Bb5", duration=t)
    buzzer.note("G5 G5 G5 F5 Eb5 F5", duration=t/2)
    buzzer.note("G5", duration=t)
    buzzer.note("C6 C6 C6 Bb5 Eb6 C6", duration=t/2)
    buzzer.note("Bb5", duration=t)
    buzzer.note("G5 G5 G5 F5 Eb5 F5", duration=t/2)
    buzzer.note("G5", duration=t*3)
    
    buzzer.note("Eb5", duration=t)
    buzzer.note("F5", duration=t*1.5)
    buzzer.note("G5", duration=t/2)
    buzzer.note("Bb5", duration=t*1.5)
    buzzer.note("G5", duration=t/2)
    buzzer.note("F5", duration=t*1.5)
    buzzer.note("G5 F5 Eb5", duration=t/2)
    buzzer.note("C5", duration=t)
    buzzer.note("Eb5", duration=t*2)
    buzzer.note("F5 Eb5 G5 F5", duration=t/2)
    buzzer.note("Eb5", duration=t*4)
    
def mission_impossible():
    bpm = 172
    t = 120/bpm
    buzzer.note("G4 G4", duration=t*1.5)
    buzzer.note("Bb4 C5", duration=t)

    buzzer.note("G4 G4", duration=t*1.5)
    buzzer.note("F4 F#4", duration=t)

    buzzer.note("G4 G4", duration=t*1.5)
    buzzer.note("Bb4 C5", duration=t)

    buzzer.note("G4 G4", duration=t*1.5)
    buzzer.note("F4 F#4", duration=t)
    ###
    buzzer.note("Bb5 G5", duration=t/2.0)
    buzzer.note("D5", duration=t*5)

    buzzer.note("Bb5 G5", duration=t/2.0)
    buzzer.note("C#5", duration=t*5)

    buzzer.note("Bb5 G5", duration=t/2.0)
    buzzer.note("C5", duration=t*5)

    buzzer.note("Bb4 C5", duration=t/2.0)

    time.sleep(t*3)

    buzzer.note("G4 D5", duration=t/2.0)
    buzzer.note("G5", duration=t*5)

    buzzer.note("G4 D5", duration=t/2.0)
    buzzer.note("F#5", duration=t*5)

    buzzer.note("G4 D5", duration=t/2.0)
    buzzer.note("F5", duration=t*5)

    buzzer.note("E5 Eb5", duration=t/2.0)
    
def ringtone():
    bpm = 240
    t = 120/bpm
    while True:
        buzzer.note("E6 D6", duration=t/2)
        buzzer.note("F#5 G#5", duration=t)
        
        buzzer.note("C#6 B5", duration=t/1.975)
        buzzer.note("D5 E5", duration=t*1.05)
        
        buzzer.note("B5 A5", duration=t/1.95)
        buzzer.note("C#5 E5", duration=t*1.1)
        buzzer.note("A5", duration=t*3)
        time.sleep(1)
        
# ringtone()
thoranee_gunsang()
# mission_impossible()
