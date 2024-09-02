# Nexus AI

Nexus is a voice modulation based AI which works on your responses.

## Libraries used 
* assemblyai
* openai
* elevenlabs
* pyaudio

## Requirements 
* Install all these python libraries
```bash
!pip install assemblyai
!pip install openai
!pip install elevenlabs
!pip install pyaudio
```
* Fretch your api keys from : OpenAI, AssemblyAI, ElevenLabs and replace it in the code
```bash
aai.settings.api_key = "API_KEY"
self.openai_client = OpenAI(api_key="API_Key")
self.elevenlabs_api_key = "API_KEY"

```

* To run

```bash
python3 main.py
```
