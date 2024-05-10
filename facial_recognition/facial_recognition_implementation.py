from deepface import DeepFace
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to Analyze Photos
def analyze_photo(photo_path):
    try:
        # Analyze photo with DeepFace library for age, gender, and emotion with enforced_detection allowing
        # for the function to return without throwing an error if no faces found, and detector_backend optimized
        # to increase results of photo analysis
        analyses = DeepFace.analyze(img_path=photo_path, actions=['age', 'gender', 'emotion'], enforce_detection=False, detector_backend='ssd')
        print('Analysis Output:', analyses)  # print analyses

        # If analyses is list (faces detected)
        if isinstance(analyses, list):
            # Handle each face analysis in the list and compile results as a string
            result = ''
            for index, analysis in enumerate(analyses):
                result += (
                    f'Face {index+1}:\n'
                    f'Age: {analysis.get('age', 'N/A')}\n'
                    f'Gender: {analysis.get('dominant_gender', 'N/A')}\n'
                    f'Emotions: {analysis.get('dominant_emotion', 'N/A')}\n'
                )
            messagebox.showinfo('Analysis Results', result)  # Display results
        else:
            # If not face(s) detected
            messagebox.showinfo('Analysis Result', 'No face detected or unexpected result format.')
    except Exception as e:
        messagebox.showerror('Error', f'Error analyzing photo: {str(e)}')  # Error handling

# Function to open a filedialog and ask user to select a photo
def open_file_dialog():
    # Capture root file name
    root.filename = filedialog.askopenfilename(initialdir='/', title='Select file',
                                               filetypes=(('jpeg files', '*.jpg'),
                                                          ('png files', '*.png'),
                                                          ('all files', '*.*')))
    # If file is selected
    if root.filename:
        analyze_photo(root.filename)  # analyze photo from call to analyze_photo() passing picture for analysis

# Set up main GUI window
root = tk.Tk()
root.title('Emotion and Age Analyzer')  # Main window title
root.geometry('400x200')  # Set dimensions for the main GUI window

# Set up button to open files
btn_open = tk.Button(root, text='Open Image', command=open_file_dialog)
btn_open.pack(pady=20)

# Create mainloop
root.mainloop()