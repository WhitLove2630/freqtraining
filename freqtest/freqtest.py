from random import choice
from time import sleep
import os
import simpleaudio as sa
from username import *
import sqlite3

freq_bank = {
"50Hz": r'SineWaves\50Hz.wav',
"63Hz": r'SineWaves\63Hz.wav',
"80Hz": r'SineWaves\80Hz.wav',
"100Hz": r'SineWaves\100Hz.wav',
"125Hz": r'SineWaves\125Hz.wav',
"160Hz": r'SineWaves\160Hz.wav',
"200Hz": r'SineWaves\200Hz.wav',
"250Hz": r'SineWaves\250Hz.wav',
"315Hz": r'SineWaves\315Hz.wav',
"400Hz": r'SineWaves\400Hz.wav',
"500Hz": r'SineWaves\500Hz.wav',
"630Hz": r'SineWaves\630Hz.wav',
"800Hz": r'SineWaves\800Hz.wav',
"1kHz": r'SineWaves\1kHz.wav',
"1.25kHz": r'SineWaves\1.25kHz.wav',
"1.6kHz": r'SineWaves\1.6kHz.wav',
"2kHz": r'SineWaves\2kHz.wav',
"2.5kHz": r'SineWaves\2.5kHz.wav',
"3.15kHz": r'SineWaves\3.15kHz.wav',
"4kHz": r'SineWaves\4kHz.wav',
"5kHz": r'SineWaves\5kHz.wav',
"6.3kHz": r'SineWaves\6.3kHz.wav',
"8kHz": r'SineWaves\8kHz.wav',
"10kHz": r'SineWaves\10kHz.wav',
"12.5kHz": r'SineWaves\12.5kHz.wav',
"16kHz": r'SineWaves\16kHz.wav'
}
answer_bank = {
"1" : "50Hz",
"2" : "63Hz",
"3" : "80Hz",
"4" : "100Hz",
"5" : "125Hz",
"6" : "160Hz",
"7" : "200Hz",
"8" : "250Hz",
"9" : "315Hz",
"10" : "400Hz",
"11" : "500Hz",
"12" : "630Hz",
"13" : "800Hz",
"14" : "1kHz",
"15" : "1.25kHz",
"16" : "1.6kHz",
"17" : "2kHz",
"18" : "2.5kHz",
"19" : "3.15kHz",
"20" : "4kHz",
"21" : "5kHz",
"22" : "6.3kHz",
"23" : "8kHz",
"24" : "10kHz",
"25" : "12.5kHz",
"26" : "16kHz"
}

def single_turn() :
    frequency = choice(list(freq_bank.keys()))
    tone = sa.WaveObject.from_wave_file(freq_bank[frequency])
    playtone = tone.play()
    print()
    for value in answer_bank.values():
        print(value.center(7), end = '')
    print()
    for key in answer_bank.keys():
        print(key.center(7), end = '')
    print("\n\nType the number below the frequency being played or type 'again' to play the tone")
    answer = None
    score = 100
    while answer_bank.get(answer) != frequency :
        answer = input()
        if answer == 'again' :
            playtone = tone.play()
            continue
        if answer == 'skip':
            break
        print(answer_bank.get(answer))
        if answer_bank.get(answer) != frequency:
            score -= 25
            print('try again')
    if score < 0 :
        score = 0
    print("You got it")
    print("Score:", score)
    return frequency, score
def add_scorecard_to_table(_username, freqscore) :
    conn = sqlite3.connect('freqtest.db')
    c = conn.cursor()
    for item in freqscore : # adds test score to database
        c.execute('INSERT INTO scores VALUES(DATETIME("NOW", "LOCALTIME"), ?, ?, ?)',(_username, item[0], item[1]))
    c.execute('UPDATE users SET times_played = times_played + 1 WHERE username = ?',(_username,))
    conn.commit()

username = login()
scorecard = []
for i in range(5) :
    freqscore = single_turn() #returns list with results of turn
    scorecard.append(freqscore)
print(scorecard)
add_scorecard_to_table(username, scorecard)
