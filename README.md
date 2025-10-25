# Personal Assistant with Hand Gesture & Voice Control - README

A multi-modal personal assistant that combines hand gesture recognition and voice commands to control your computer. Switch seamlessly between voice and gesture modes for intuitive desktop control.

## 🎯 Features

### 🤖 Voice Control Mode
- **Application Launcher**: Open Chrome, File Explorer, VS Code, etc.
- **Media Control**: Play/pause, volume control
- **Window Management**: Minimize, switch between windows
- **Text Operations**: Select all, copy, paste
- **Mode Switching**: Activate/deactivate gesture mode via voice

### ✋ Hand Gesture Mode
- **Gesture Recognition**: 10+ predefined gestures
- **Combo Commands**: Sequence-based actions
- **Window Control**: Minimize, maximize, switch windows
- **Application Shortcuts**: Quick app launching
- **Media Control**: Play/pause functionality

## 🛠️ Tech Stack

### Core Technologies
- **OpenCV** - Computer vision and camera processing
- **MediaPipe** - Hand tracking and landmark detection
- **TensorFlow/Keras** - Gesture recognition model
- **SpeechRecognition** - Voice command processing
- **PyAutoGUI** - Desktop automation

### Machine Learning
- **Custom Gesture Model**: Pre-trained hand gesture classifier
- **Real-time Prediction**: Live gesture recognition
- **Google Speech API**: Cloud-based speech recognition

## 📋 Prerequisites

- Python 3.7+
- Webcam
- Microphone
- Windows OS (for hotkey compatibility)

## 🚀 Installation

### 1. Clone and Setup
```bash
git clone <your-repo-url>
cd personal-assistant
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install opencv-python mediapipe tensorflow keras pyautogui speechrecognition pyaudio numpy
```

### 3. Download Model Files
Place these files in your project directory:
- `mp_hand_gesture` - Pre-trained gesture recognition model
- `gesture.names` - Gesture class labels file

### 4. Run the Application
```bash
python assistant.py
```

## 🎮 Usage Guide

### Voice Commands Available

#### Application Control
- **"open chrome"** or **"open browser"** - Launch Chrome
- **"open file explorer"** - Open File Explorer
- **"open visual studio code"** - Launch VS Code
- **"open spotify"** - Open Spotify
- **"open microsoft edge"** - Launch Edge browser

#### Window Management
- **"minimise the window"** - Minimize current window
- **"open the last window"** - Switch to previous window

#### Media Control
- **"play"** / **"stop it"** - Play/pause media
- **"volume up"** / **"increase volume"** - Increase volume
- **"volume down"** / **"decrease volume"** - Decrease volume

#### Text Operations
- **"select all and copy"** - Select all and copy
- **"paste it"** - Paste clipboard content

#### Mode Switching
- **"activate hand gesture"** - Switch to gesture mode
- **"deactivate hand gesture"** - Return to voice mode

### Hand Gestures Available

#### Single Gesture Commands
- **"close"** - Minimize window (`Win + Down`)
- **"hold"** - Switch windows (`Alt + Tab`) and maximize (`Win + Up`)
- **"pause"** - Play/pause media (`Space`)
- **"two"** - Open app in position 2 (`Win + 2`)
- **"three"** - Open app in position 3 (`Win + 3`)
- **"six"** - Open app in position 6 (`Win + 6`)

#### Gesture Combinations
- **"select all" → "close"** - Select all and copy (`Ctrl + A`, `Ctrl + C`)
- **"close" → "select all"** - Paste content (`Ctrl + V`)

## ⚙️ Configuration

### Customizing Commands
Modify the command mappings in the main script:

```python
# Add new voice commands
elif recognized_text == "your custom command":
    pyautogui.hotkey('key1', 'key2')

# Add new gesture commands
elif first == "new_gesture":
    pyautogui.hotkey('key1', 'key2')
```

### Gesture Model
The system uses a pre-trained model. To train your own:
1. Collect gesture dataset
2. Train using MediaPipe landmarks
3. Update `gesture.names` with new classes

## 📁 Project Structure

```
personal-assistant/
├── assistant.py              # Main application
├── mp_hand_gesture/          # Trained gesture model
├── gesture.names             # Gesture class labels
├── requirements.txt          # Python dependencies
└── README.md
```

## 🔧 Troubleshooting

### Common Issues

1. **Webcam not detected**
   ```bash
   # Check camera index
   cap = cv2.VideoCapture(0)  # Try 0, 1, 2...
   ```

2. **Microphone access denied**
   - Grant microphone permissions
   - Check if other apps are using microphone

3. **Model files not found**
   - Verify file paths in code
   - Ensure model files are in correct directory

4. **Hotkeys not working**
   - Run as administrator (if required)
   - Check application focus

5. **Speech recognition errors**
   - Check internet connection (Google API requires internet)
   - Ensure clear audio input

### Performance Tips
- Ensure good lighting for gesture recognition
- Speak clearly and at moderate pace
- Keep hands clearly visible to camera
- Close unnecessary applications

## 🚀 Future Enhancements

- [ ] Custom gesture training interface
- [ ] More voice commands and applications
- [ ] Cross-platform compatibility (Linux, macOS)
- [ ] GUI configuration panel
- [ ] Plugin system for custom commands
- [ ] Machine learning model optimization
- [ ] Offline speech recognition
- [ ] Gesture sequence recording


## 🙏 Acknowledgments

- MediaPipe for hand tracking technology
- Google Speech Recognition API
- TensorFlow/Keras communities
- OpenCV for computer vision capabilities

---

**Note**: This application requires internet connection for speech recognition functionality. Gesture recognition works offline once the model is loaded.
