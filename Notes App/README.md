# Notes App

This is a **simple Python Notes App** that demonstrates how to **create, read, and delete notes** using files.  
It is written at **GCSE Computer Science J277 level**, focusing on the fundamentals of **file handling in Python**.

---

## Features
- **Create Notes**: Add new notes that are stored permanently inside a text file (`notes.txt`).  
- **View Notes**: Instantly display all notes saved in the file.  
- **Delete Notes**: Remove unwanted notes and update the file automatically.  
- **Persistent Storage**: Notes remain saved even after the program closes.  

---

## How It Works
This program relies on Python’s basic **file operations**:
- `open()` to create or access files in different modes (`a`, `r`, `w`).  
- `write()` and `writelines()` to add new content.  
- `readlines()` to load and display existing notes.  
- A simple update cycle that rewrites the file when notes are deleted.  

It runs in the **terminal/command line** and has been tested in **Visual Studio Code**.

---

## Why This Project Matters
This project is an early step in learning how **files allow programs to store data permanently**.  
It shows:
- How I can combine **basic Python logic** with **file handling** to make a working app.  
- That I can already think about real-world use cases (note-taking, saving data for later).  
- That I’m building confidence to extend small projects into something bigger (like adding a GUI with Tkinter later).  

---

## Next Steps
- Add a **Tkinter GUI** so the app has buttons and text areas instead of only terminal input.  
- Organise notes with **timestamps** or categories.  
- Explore saving data in **CSV or JSON formats** for more advanced features.  
