# 🌟 Wheel of Time Adventure Game

A text-based adventure game set in the world of Robert Jordan's Wheel of Time series.

## 🎮 About the Game

Journey through 6 iconic locations from the Wheel of Time universe:
- **Two Rivers** - The peaceful village of Emond's Field
- **White Tower** - Home of the Aes Sedai
- **Tel'aran'rhiod** - The World of Dreams
- **Shadar Logoth** - The cursed city
- **Caemlyn** - The royal capital
- **Tar Valon** - The great island city

### Features:
- 🧩 **6 Multiple Choice Puzzles** - Solve riddles to progress
- 🎒 **Item Collection** - Gather powerful artifacts
- ⚔️ **Combat System** - Battle dangerous foes
- 👑 **5 Different Endings** - Your choices determine your destiny
- 📊 **Progress Tracking** - Monitor your journey
- 🎨 **Colorful Interface** - Rich text formatting and emojis

## 🚀 How to Run

### Option 1: Run the Executable (Recommended)
1. Double-click `Wheel_of_Time_Adventure.exe` in the `dist` folder
2. The game will start immediately in a console window
3. No Python installation required!

### Option 2: Run from Source Code
1. Make sure Python 3.7+ is installed
2. Install required packages: `pip install colorama`
3. Run: `python wheel_of_time_adventure.py`

## 🔨 Building the Executable

If you want to rebuild the executable:

### Quick Build:
1. Double-click `build_game.bat`
2. Wait for the build to complete
3. Find your executable in the `dist` folder

### Manual Build:
```bash
pip install pyinstaller colorama
pyinstaller --onefile --console --name "Wheel_of_Time_Adventure" wheel_of_time_adventure.py
```

## 🎯 Game Commands

- **Movement**: Type location names (e.g., "white tower")
- **help** - Show help menu and puzzle hints
- **commands** - Show detailed command list
- **puzzle** - Attempt the current location's puzzle
- **inventory** - View your collected items
- **map** - View the world map
- **health** - Check your health status
- **progress** - See overall game progress
- **quit** - Exit the game

## 🧩 Puzzle Solutions

Need help? Here are the answers:
1. **Two Rivers**: Search the village square (Option 1)
2. **White Tower**: Light (Option 2)
3. **Tel'aran'rhiod**: Follow the moonlit path (Option 2)
4. **Shadar Logoth**: Sword of Light (Option 3)
5. **Caemlyn**: Wisdom (Option 3)
6. **Tar Valon**: Embrace the source (Option 2)

## 🏆 Endings

Collect specific items and visit certain locations to unlock different endings:
- 🗡️ **Warrior's Path** - Get Sword of Light, go to Shadar Logoth
- 📚 **Aes Sedai Path** - Get Book of Prophecy + One Power Ring, go to White Tower
- 🌙 **Dreamwalker Path** - Get Dream Ter'angreal, go to Tel'aran'rhiod
- 👑 **Royal Path** - Get Golden Crown + Royal Seal, go to Caemlyn
- ⚡ **Amyrlin Path** - Get Amyrlin's Staff + 5+ items, go to Tar Valon

## 📁 File Structure

```
📂 For_the_light/
├── 🎮 wheel_of_time_adventure.py    # Main game file
├── 🔧 wheel_of_time_adventure.spec  # PyInstaller spec file
├── ⚡ build_game.bat               # Quick build script
├── 📖 README.md                    # This file
├── 📂 dist/                       # Contains the executable
│   └── 🎮 Wheel_of_Time_Adventure.exe
├── 📂 build/                      # Build files (auto-generated)
└── 📂 __pycache__/               # Python cache (auto-generated)
```

## 🎨 Technical Details

- **Language**: Python 3.13+
- **Dependencies**: colorama (for colored text)
- **Executable**: Built with PyInstaller
- **Size**: ~15-20 MB (standalone)
- **Platform**: Windows (can be built for other platforms)

## 🎭 Credits

Based on the world created by Robert Jordan in the Wheel of Time series.
Game developed for educational and entertainment purposes.

---

**May you always find water and shade!** 🌟
