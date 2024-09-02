
import assemblyai as aai
from openai import OpenAI
import elevenlabs
import pyaudio

class AI_Assistant:
    def __init__(self):
        aai.settings.api_key = "API_KEY"
        self.openai_client = OpenAI(api_key="API_Key")
        self.elevenlabs_api_key = "API_KEY"

        self.transcriber = None
        self.full_transcript = [
            {"role": "system", "content": "You are a specialist assistant, providing concise and effective guidance."}
        ]

    def start_transcribing(self):
      self.transcriber = aai.RealtimeTranscriber(
        sample_rate=16000,
        on_data=self.on_data,
        on_error=self.on_error,
        on_close=self.on_close
    )
      self.transcriber.connect()
      microphone_stream = aai.extras.MicrophoneStream(sample_rate=16000)
      self.transcriber.stream(microphone_stream)
    def stop_transcribing(self):
        if self.transcriber:
            self.transcriber.close()
            self.transcriber = None

    def on_open(self, session_opened: aai.RealtimeSessionOpened):
        # print("Session ID:", session_opened.session_id)
        return

    def on_data(self, transcript: aai.RealtimeTranscript):
        if not transcript.text:
            return

        if isinstance(transcript, aai.RealtimeFinalTranscript):
            self.generative_ai_response(transcript)
        else:
            print(transcript.text, end="\r")

    def on_error(self, error: aai.RealtimeError):
        # print("An error occurred:", error)
        return

    def on_close(self):
        # print("Closing Session")
        return

    def generative_ai_response(self, transcript):
        self.full_transcript.append({"role": "user", "content": transcript.text})
        print("\nQuestion:", transcript.text, end="\r")

        response = self.openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.full_transcript
        )
        ai_response = response.choices[0].message.content
        self.generate_audio(ai_response)

    def generate_audio(self, text):
        self.full_transcript.append({"role": "assistant", "content": text})
        print(f"Answer: {text}")

        audio = elevenlabs.generate(
            text=text,
            voice="Elisa",
            api_key=self.elevenlabs_api_key
        )
        elevenlabs.stream(audio)

greeting = "Welcome ! My self Nexus, How can I assist you today?"
print(greeting)
ai_assistant = AI_Assistant()
ai_assistant.start_transcribing()