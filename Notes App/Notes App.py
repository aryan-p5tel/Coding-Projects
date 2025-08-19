#Notes App
# This is a simple notes app that allows users to create, view, and delete notes.
#add tkinter later
#uses basic code for adding, reading and deleting
#Learning about files and saving, reading etc. 
# To create a new note
file=open("notes.txt", "a")
note=input("New note : ")
file.write(note + "\n")
print("Notes updated successfully.")
file.close()
# To view notes
file=open("notes.txt", "r")
notes=file.readlines() # Read all lines from the file
print("Your notes:")
file.close()
#To delete notes
note_to_delete=input("Enter note to delete: ")
file=open("notes.txt", "r")
notes.file.readlines() # Read all lines from the file
file.close()
if note_to_delete in notes:
    notes.remove(note_to_delete + "\n") # Remove the note from the list
    file=open("notes.txt", "w")
    file.writelines(notes) # Write the updated list back to the file
    print("Note deleted successfully.")
else:
    print("Note not found.")
file.close()