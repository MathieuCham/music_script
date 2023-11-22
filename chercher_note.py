import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np
# Chemin du fichier wav
chemin_fichier = "son_plus_clean.wav"
import pandas as pd
import matplotlib.pyplot as plt
# Lire le fichier audio
audio_data, fs = sf.read(chemin_fichier)

# Convertir les valeurs audio en double
audio_data = audio_data.astype(float)

# Afficher la fréquence d'échantillonnage et les premières valeurs du tableau
print("Fréquence d'échantillonnage :", fs)
print("Tableau de signal audio : ")
print(audio_data[:10])


t=np.array(range(len(audio_data)))/fs

###################

tempo=132

DeltaT=60/tempo/2

#plt.plot(t,audio_data)


tempo=np.array(range(160))*DeltaT
#plt.plot(tempo,tempo*0,'o')


indice_note=7
numero_porte=14
trame=8*numero_porte+indice_note
indice= (trame*DeltaT<=t) * ((trame+1)*DeltaT>t)

s_loc=audio_data[indice,0]
t_loc=t[indice]


spectre=np.fft.fft(s_loc)
f=np.array(range(len(spectre)))/len(spectre)*fs

#plt.figure()
#plt.plot(omega[omega<=4000],abs(spectre[omega<=4000]))

#import pandas as pd
table_note = pd.read_csv("frequence_note.csv")

plt.close('all')
frequence_note=np.array(table_note['frequence'])
note=np.array(table_note['note'])
note=[note[ii]+'-'+str(ii//8-3) for ii in range(len(note))]
signal_interp=np.interp(frequence_note,f,spectre)
plt.figure()
plt.plot(frequence_note,abs(signal_interp))
for ii in range(len(frequence_note)):
    plt.text(frequence_note[ii],abs(signal_interp[ii]),note[ii])
#plt.ylim([0,300])


#def calculer_note(frequence):
    
    
    

