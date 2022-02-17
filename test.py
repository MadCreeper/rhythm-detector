import numpy as np
from matplotlib import pyplot as plt
import thinkdsp
import ffmpeg
from pydub import AudioSegment


def plot_wave_diff(t, wv, n=2):
    #plt.plot(t[:-1], np.diff(wv, n=1))
    fig, axs = plt.subplots(n,figsize=(20.5, 6))
    deri = wv[:]
    for i in range(n):
        axs[i].plot(t, deri)    
        deri = np.hstack([[0], np.diff(deri)])
        
    #plt.plot(t[:-2], np.diff(np.diff(wv, n=1),n=1))


musicfile = "canon_in_d.mp3"
tempwav = "temp.wav"
tempcut = "temp_cut.wav"
(
    ffmpeg
    .input(musicfile)
    .output(tempwav)
    .run()
)

music = AudioSegment.from_wav(tempwav)
ten_seconds = 10 * 1000
cut_music = music[:5000]
cut_music.export(tempcut, format='wav')
wave = thinkdsp.read_wave(tempcut)
#print(wave.ts[:10],wave.ys[:10])
print(np.diff(wave.ts))
#plt.figure(figsize=(20.5, 6))
#wave.plot()
#plot_wave_diff(wave.ts, wave.ys)
plt.show()
