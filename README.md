# Sobre
A aplicação se trata de uma assistente virtual, como a Alexa, por exemplo. Desenvolvi durante o curso de técnico de informática.

# Como funciona?
Para funcionar os comandos de voz, você precisa específicar os caminho para chegar num executável(por exemplo "chrome.exe") que você queira que o Jarvis executa/obedeça, por exemplo:
```python
webbrowser.BackgroundBrowser("C://launcher.exe"))
```
Caso você queira que o Jarvis abra a pasta Documento do windows use este comando:
<br> *obs:  na aplicação usei "D:", porque eu mudei o caminho, e não queria consumir muito o meu SSD.
```python
diretorio_documento = "C://documentos"
os.startfile(diretorio_documento)
```
Se não der certo, tenta colocar o "D" maiúsculo(C://Documentos).
# Baixando às bibiotecas
Pra funcionar a aplicação, você terá que baixar às seguintes biblioteca: 
<br> **Pyttsx3** 
```bash
pip install pyttsx3
```
**Speech_recognition** 
```bash
pip install pip install SpeechRecognition
```
**Secure-smtplib** 
```bash
pip install pip install secure-smtplib
```
**Pyaudio** 
```bash
pip install pip install PyAudio
```
