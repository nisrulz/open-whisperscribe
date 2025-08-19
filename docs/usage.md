# Usage

## Running the Application

1. Start the application:

   ```bash
   ./run.sh
   ```

   ![GUI](../assets/sc_1.png)

   Once the GUI loads, click "Start" to activate the hotkey functionality.

2. Place your cursor inside the application or text field where you want the transcribed text to appear.

3. Press and hold the hotkey combination `Option + Shift-Left` (or `Alt + Shift-Left` on Windows/Linux) to start recording your voice.

   > You can configure this hotkey combination. See the [Configure](#configure) section below for details.

4. Release the hotkey to transcribe your speech and automatically copy the text to your clipboard.

## Stopping the Application

To stop the application, you can:

1. Press the "Stop" button in the GUI.

   ![GUI quit from stop button](../assets/sc_6.png)

2. Quit the GUI by clicking the "x" button on the top left corner.

   ![GUI quit from x](../assets/sc_7.png)

3. Run the following script to stop all running instances:

   ```bash
   ./stop.sh
   ```

## Configure

Customize the application by modifying the `config.yaml` file located in the root directory. Below are some common configurations:

1. **Audio Settings**:

   - `sample_rate`: Adjust the audio sample rate (e.g., `16000` for 16kHz).
   - `audio_file`: Specify the name of the file where recorded audio will be saved.

2. **Logs**:

   - Logs are written to the `nohup.out` file by default when the application is run in the background using `./run.sh`.

3. **Hotkey Combination**:

   - The hotkey combination is defined in `src/hotkey_combination.py`. To change it, modify the `HOTKEY_COMBINATION` variable. For example:

     ```python
     HOTKEY_COMBINATION = {keyboard.Key.ctrl, keyboard.Key.space}
     ```

   - Use `keyboard.Key` and then type `.` for autocompletion and to avoid errors.

4. **Whisper Model**:

   - `model`: Specify the Whisper model to use. Possible values are `tiny`, `base`, `small`, `medium`, and `large`.
   - The model is downloaded and cached automatically when you run the application for the first time.

After making changes, restart the application for the updates to take effect:

```bash
./run.sh
```
