# Open WhisperScribe

> Transcribe. Paste. Done. Let your voice do the typing.

![Banner](./assets/github_banner.jpg)

## Highlights

🎙️ **Speak Naturally**: Converts your voice into text effortlessly using advanced Whisper speech recognition.

⚡ **Instant Transcription**: Transcribes spoken words in real time, ready to paste anywhere.

📋 **Clipboard Integration**: Automatically copies the transcribed text to your clipboard for quick use.

💼 **For Everyone**: Ideal for professionals, creatives, students, and anyone who wants to save typing time.

🛠️ **Lightweight CLI Tool**: Easy to install and run from the command line without distractions.

✍️ **Boost Productivity**: Streamlines note-taking, writing, and communication by bridging speech and text seamlessly.

🌙 **Runs in Background**: Operates quietly without interrupting your workflow or demanding attention.

## Usage

### Prerequisites

- Python 3.8 or higher installed on your system.
- `pip` package manager.
- Tested on macOS, but it should also work on Windows and Linux since it is written in Python.

### Setup

1. Open your terminal and clone the repository:

   ```bash
   git clone https://github.com/yourusername/open-whisperscribe.git
   cd open-whisperscribe
   ```

2. Run the setup script to create a virtual environment and install dependencies:

   ```bash
   ./setup.sh
   ```

### Running the Application

1. Start the application:

   ```bash
   ./run.sh
   ```

   > **Note**:
   > The app runs in the background, so you are free to close the terminal window if you want to.
   > When you run this script it will first stop all running instances of Open WhisperScribe and then start a fresh new instance.

2. Place your cursor inside the application or text field where you want the transcribed text to appear.

3. Press and hold the hotkey combination `Option + Shift-Left` (or `Alt + Shift-Left` on Windows/Linux) to start recording your voice.

4. Release the hotkey to transcribe your speech and automatically copy the text to your clipboard.

### Stopping the Application

To stop the application, run:

```bash
./stop.sh
```

### Configure

You can customize the application by modifying the `config.yaml` file located in the root directory of the project. Below are some common configurations you can change:

1. **Audio Settings**:

   - `sample_rate`: Adjust the audio sample rate (e.g., `16000` for 16kHz).
   - `audio_file`: Specify the name of the file where recorded audio will be saved.

2. **Logging**:

   - `file`: Set the path for the log file (e.g., `logs.txt`).
   - `level`: Change the logging level (e.g., `ERROR`, `INFO`, `DEBUG`).

3. **Hotkey Combination**:

   - The hotkey combination is defined in `src/hotkey_combination.py` for better usability and autocompletion support inside the code editor.
   - To change the hotkey, open `src/hotkey_combination.py` and modify the `HOTKEY_COMBINATION` variable. For example:

     ```python
     HOTKEY_COMBINATION = {keyboard.Key.ctrl, keyboard.Key.space}
     ```

   - Use `keyboard.Key` and then type `.` for autocompletion and to avoid errors.

After making changes, restart the application for the updates to take effect, by running

```bash
./run.sh
```

## License

This project is licensed under the Apache License 2.0.

See the [LICENSE.txt](./LICENSE.txt) file for the full license text.
