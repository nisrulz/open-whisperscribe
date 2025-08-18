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
   git clone https://github.com/nisrulz/open-whisperscribe.git
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

   > You can configure this hotkey combination. See the [Configure](#configure) section below for details.

4. Release the hotkey to transcribe your speech and automatically copy the text to your clipboard.

### Stopping the Application

To stop the application, run:

```bash
./stop.sh
```

https://github.com/user-attachments/assets/a8d6d672-941a-417a-8082-91ed4e726320

### Configure

You can customize the application by modifying the `config.yaml` file located in the root directory of the project. Below are some common configurations you can change:

1. **Audio Settings**:

   - `sample_rate`: Adjust the audio sample rate (e.g., `16000` for 16kHz).
   - `audio_file`: Specify the name of the file where recorded audio will be saved.

2. **Logs**:

   - Logs are written to the `nohup.out` file by default when the application is run in the background using `./run.sh`.
     You can check this file for debugging or runtime information.

3. **Hotkey Combination**:

   - The hotkey combination is defined in `src/hotkey_combination.py` for better usability and autocompletion support inside the code editor.
   - To change the hotkey, open `src/hotkey_combination.py` and modify the `HOTKEY_COMBINATION` variable. For example:

     ```python
     HOTKEY_COMBINATION = {keyboard.Key.ctrl, keyboard.Key.space}
     ```

   - Use `keyboard.Key` and then type `.` for autocompletion and to avoid errors.

4. **Whisper Model**:

   - `model`: Specify the Whisper model to use. Possible values are `tiny`, `base`, `small`, `medium`, and `large`.
   - The model is downloaded and cached automatically when you run the application for the first time. Subsequent runs will use the cached model.

After making changes, restart the application for the updates to take effect, by running

```bash
./run.sh
```

## Credits

This project makes use of the following:

- [Whisper Model by OpenAI](https://openai.com/research/whisper): A state-of-the-art speech recognition model.
- [pynput](https://pynput.readthedocs.io/en/latest/): A library for controlling and monitoring input devices.
- [pyperclip](https://github.com/asweigart/pyperclip): A cross-platform Python module for clipboard operations.
- [pyautogui](https://pyautogui.readthedocs.io/en/latest/): A library for programmatically controlling the mouse and keyboard.
- [openai-whisper](https://github.com/openai/whisper): The official Python package for the Whisper model.
- [sounddevice](https://python-sounddevice.readthedocs.io/): A library for recording and playing back audio in real time.
- [numpy](https://numpy.org/): A fundamental package for scientific computing with Python.
- [scipy](https://scipy.org/): A library for mathematics, science, and engineering.
- [pyyaml](https://pyyaml.org/): A YAML parser and emitter for Python.

## License

This project is licensed under the Apache License 2.0.

See the [LICENSE.txt](./LICENSE.txt) file for the full license text.
