import pyaudio

p = pyaudio.PyAudio()

CHUNK = 1024
rec_duration = 10

stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=CHUNK)

frames = []
while True:
    data = stream.read(CHUNK)
    frames.append(data)
    
    if len(frames) > rec_duration * 44100/1024:
        break

print(frames)