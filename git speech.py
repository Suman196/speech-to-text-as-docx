import docx
import speech_recognition as sr
r = sr.Recognizer()

filename = "" #put your audiofile in 'wav' format
with sr.AudioFile(filename) as source:
    print("Fetching your data!")
    audio=r.record(source)

    text = r.recognize_google(audio)

doc = docx.Document()
doc_para = doc.add_paragraph(text)
doc.save("") # save your text in 'docx' format
