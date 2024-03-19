# Speaker Diarization with AssemblyAI
This Flask app allows users to transcribe audio files by providing a link to the audio file. It utilizes the AssemblyAI API for transcription.

## Setup
Clone the repository:

```bash
git clone https://github.com/shaham-noorani/speaker-diarization.git
```

Navigate to the project directory:

```bash
cd speaker-diarization
```

Install dependencies:
  
  ```bash
pip install -r requirements.txt
```

Create a .env file in the project root directory and add your AssemblyAI API key:
  
```bash
touch .env
```

```js
ASSEMBLY_AI_KEY=your-assemblyai-api-key
```

## Running the App
To run the Flask app, execute the following command in your terminal:

```bash
python server.py
```

This will start the Flask development server. By default, the app will be accessible at http://127.0.0.1:5000/ in your web browser.

## Usage
Open your web browser and go to http://127.0.0.1:5000/.

Enter the URL of the audio file you want to transcribe into the provided form field.

Click the "Transcribe" button.

Wait for the transcription process to complete. Once done, the transcript will be displayed on the result page.

## Notes

Make sure your audio file is accessible via a direct URL.
