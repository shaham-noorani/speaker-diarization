from flask import Flask, request, render_template
import time
import dotenv
import os
import assemblyai as aai

dotenv.load_dotenv()

app = Flask(__name__)

aai.settings.api_key = os.environ.get("ASSEMBLY_AI_KEY")


def transcribe_audio(audio_url, config):
    return aai.Transcriber().transcribe(audio_url, config)


def process_transcript(transcript, students):
    output = []
    for utterance in transcript.utterances:
        speaker = "Student" if utterance.speaker in students else "Interviewee"
        speaker += f" (Speaker {utterance.speaker})"
        # Format start and end times
        start_time_formatted = format_time(utterance.start)
        end_time_formatted = format_time(utterance.end)
        output.append(
            {
                "speaker": speaker,
                "start": start_time_formatted,
                "end": end_time_formatted,
                "caption": utterance.text,
            }
        )
    return output


def format_time(milliseconds):
    # Convert milliseconds to HH:MM:SS format
    s, ms = divmod(milliseconds, 1000)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    return "{:02d}:{:02d}:{:02d}".format(int(h), int(m), int(s))


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        audio_url = request.form["audio_url"]
        number_of_speakers = request.form["number_of_speakers"]
        config = aai.TranscriptionConfig(
            speaker_labels=True,
            speakers_expected=number_of_speakers,
            disfluencies=False,
            audio_end_at=23000,
        )
        transcript = transcribe_audio(audio_url, config)
        students = ["A"]
        output = process_transcript(transcript, students)
        return render_template("result.html", output=output)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
