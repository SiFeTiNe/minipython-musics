import buzzer
import time

buzzer.volume = 2
 
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
        
def we_will_keep_our_promise():
    bpm = 132
    t = 120/bpm
    buzzer.note("Bb5", duration=t)
    buzzer.note("G#5", duration=t/2)
    buzzer.note("Bb5", duration=t*1.5)
    buzzer.note("C#6 Eb6", duration=t)
    buzzer.note("C#6", duration=t*3)
    
    buzzer.note("Bb5", duration=t)
    buzzer.note("G#5", duration=t/2)
    buzzer.note("F#5", duration=t*1.5)
    buzzer.note("Eb5 Bb5", duration=t)
    buzzer.note("G#5", duration=t*3)
    
    buzzer.note("Bb5", duration=t)
    buzzer.note("G#5", duration=t/2)
    buzzer.note("Bb5", duration=t*1.5)
    buzzer.note("C#6 Eb6", duration=t)
    buzzer.note("C#6", duration=t*2)
    
    buzzer.note("Bb5", duration=t/2)
    buzzer.note("G#5", duration=t*1.5)
    buzzer.note("F#5", duration=t)
    buzzer.note("G#5", duration=t*6)
    
    buzzer.note("Bb5", duration=t)
    buzzer.note("G#5", duration=t/2)
    buzzer.note("Bb5", duration=t*1.5)
    buzzer.note("C#6 Eb6", duration=t)
    buzzer.note("C#6", duration=t*3)
    
    buzzer.note("Bb5", duration=t)
    buzzer.note("G#5", duration=t/2)
    buzzer.note("F#5", duration=t*1.5)
    buzzer.note("Eb5 Bb5", duration=t)
    buzzer.note("G#5", duration=t*2)
    
    buzzer.note("Eb6 F6", duration=t)
    buzzer.note("F#6", duration=t*8)
    
    buzzer.note("Eb5 F#5", duration=t)
    buzzer.note("G#5", duration=t/2)
    buzzer.note("Bb5", duration=t*1.5)
    
    buzzer.note("C#6", duration=t)
    buzzer.note("Eb6 Bb5", duration=t*1.5)
    buzzer.note("Bb5 G#5", duration=t)
    buzzer.note("F#5", duration=t/2)
    buzzer.note("Eb5", duration=t*1.5)
    buzzer.note("Bb5", duration=t)
    buzzer.note("G#5", duration=t*2)
    
    buzzer.note("Eb5", duration=t/2)
    buzzer.note("F#5", duration=t*1.5)
    buzzer.note("F#5", duration=t*8)
    
def touhou_hisouten():
    bpm = 120
    t = 120/bpm
    buzzer.note("Bb4 C5 D5 F5", duration=t/2)
    buzzer.note("G5", duration=t*3)
    buzzer.note("F5 G5 Bb5 A5", duration=t/2)
    buzzer.note("G5 A5 G5", duration=t/6)
    buzzer.note("F5", duration=t/2)
    buzzer.note("G5", duration=t)
    buzzer.note("D5 F5", duration=t/2)
    buzzer.note("G5", duration=t*3)
    buzzer.note("A5 Bb5 C6 D6", duration=t/2)
    buzzer.note("D6", duration=t*1.5)
    buzzer.note("C6 Bb5 A5", duration=t/2)
    buzzer.note("G5", duration=t*3)
    buzzer.note("F5 G5 Bb5 A5", duration=t/2)
    buzzer.note("G5 A5 G5", duration=t/6)
    buzzer.note("F5", duration=t/2)
    buzzer.note("G5", duration=t)
    for i in range(2):
        buzzer.note("F5 C6", duration=t/2)
        buzzer.note("G5", duration=t)
    buzzer.note("F5 C5", duration=t/2)
    buzzer.note("G5", duration=t*2)
    
    buzzer.note("Bb4 C5 D5 F5", duration=t/2)
    buzzer.note("G5", duration=t*3)
    buzzer.note("F5 G5 Bb5 A5", duration=t/2)
    buzzer.note("G5 A5 G5", duration=t/6)
    buzzer.note("F5", duration=t/2)
    buzzer.note("G5", duration=t)
    buzzer.note("D5 F5", duration=t/2)
    buzzer.note("G5", duration=t*3)
    buzzer.note("A5 Bb5 C6 D6", duration=t/2)
    buzzer.note("D6", duration=t*1.5)
    buzzer.note("C6 D6 Bb5 C6 A5 Bb5", duration=t/4)
    buzzer.note("G5", duration=t*3)
    buzzer.note("F5 G5 Bb5 A5", duration=t/2)
    buzzer.note("Bb5 A5 Bb5", duration=t/6)
    buzzer.note("C6", duration=t/2)
    buzzer.note("D6", duration=t)
    buzzer.note("C6 Bb5", duration=t/2)
    buzzer.note("Bb5 A5 G5", duration=t/1.5)
    buzzer.note("A5 D5", duration=t/1.5)
    buzzer.note("A5", duration=t/2)
    buzzer.note("A5 Bb5", duration=t/4)
    buzzer.note("G5", duration=t*3.75)
    
touhou_hisouten()
# we_will_keep_our_promise()
# ringtone()
# thoranee_gunsang()
# mission_impossible()
