# Instalar o módulo SpeechRecognition -> pip install SpeechRecognition
# Instalar o módulo PyAudio -> pip install pyaudio

# Você pode usar a URL do PyAudio caso surja algum problema durante a instalação
# -> https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
# Ou você pode pesquisar no Google pela seguinte frase
# -> install pyaudio <seu_sistema_operacional>
# Ou caso o seu SO seja Windows você pode digitar no terminal o seguinte comando
# -> pipwin install pyaudio

# Let's Code: https://letscode.com.br/blog/speech-recognition-com-python

import speech_recognition as sr

# print(sr.Microphone().list_microphone_names())
# print(sr.Microphone().list_working_microphones())

MIC = sr.Recognizer()

with sr.Microphone(0) as mic:
    MIC.adjust_for_ambient_noise(mic)
    print('Gravando ...')
    audio = MIC.listen(mic)
    texto = MIC.recognize_google(audio, language='pt-BR')
    print(texto)
