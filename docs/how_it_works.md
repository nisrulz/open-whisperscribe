# How it works

1. The application starts when the user launches the app, which loads the GUI defined in `gui.py`. The GUI is built with [**Tkinter**](https://docs.python.org/3/library/tkinter.html) and displays the main interface.
2. The GUI sets up a hotkey listener, configured in `src/hotkey_combination.py`. The hotkey functionality is implemented using the [**pynput**](https://pypi.org/project/pynput/) library.
3. When the user presses the hotkey, the app records audio using code in `src/audio_recorder.py`. Audio recording is handled by the [**sounddevice**](https://pypi.org/project/sounddevice/) library, with data processing by [**numpy**](https://numpy.org/) and [**scipy**](https://scipy.org/).
4. The recorded audio is transcribed into text using the OpenAI Whisper model, called from `src/whisper_transcriber.py`. This step uses the [**openai-whisper**](https://github.com/openai/whisper) Python package (which internally uses the [**Whisper Model by OpenAI**](https://github.com/openai/whisper)).
5. The transcribed text is copied to the clipboard by code in `src/clipboard_manager.py`, which uses the [**pyperclip**](https://pypi.org/project/pyperclip/) library for clipboard operations.
6. The tool automatically pastes the copied transcribed text at the currently focused app window where the cursor is.

![Flow Diagram](../assets/flow_diagram.svg)
