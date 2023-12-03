import pyaudio
import wave
from transcriber import transcribe

CHUNK =1024
FORMAT =pyaudio.paInt16
CHANNELS = 1
RATE = 44100

def audio_input():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels =CHANNELS,
                    rate =RATE,
                    input = True,
                    frames_per_buffer =CHUNK)

    print("Recording...")

    frames = []
    seconds = 10

    for i in range(0,int(RATE/CHUNK*seconds)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Recording Ended!")

    stream.stop_stream()
    stream.close()
    p.terminate()

    w = wave.open("output.wav",'wb')
    w.setnchannels(CHANNELS)
    w.setsampwidth(p.get_sample_size(FORMAT))
    w.setframerate(RATE)
    w.writeframes(b''.join(frames))
    w.close()
    res = transcribe()
    return res

audio_input()




