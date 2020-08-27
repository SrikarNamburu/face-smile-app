import tkinter as tk
import cv2
from PIL import ImageTk, Image
import imutils
from imutils.video import WebcamVideoStream
from imutils.video import FPS


class App:
    def __init__(self):
        self.cascade_face = cv2.CascadeClassifier('D:/face-smile-app/bin/haarcascade_frontalface_default.xml')
        self.cascade_smile = cv2.CascadeClassifier('D:/face-smile-app/bin/haarcascade_smile.xml')
        HEIGHT = 600
        WIDTH = 900
        self.root = tk.Tk()
        self.root.title("SmileDetectionApp")
        
        # creating a canvas
        canvas = tk.Canvas(self.root, height=HEIGHT, width=WIDTH)
        canvas.pack()
        
        # Frame to show the web cam feed 
        video = tk.Frame(self.root, bg="#263D42")
        video.place(relx = 0.05, rely =0.1, relwidth = 0.65, relheight = 0.8)
        # Frame to show the results from the video
        stats = tk.Frame(self.root, bg='#80c1ff')
        stats.place(relx = 0.75, rely=0.1, relwidth = 0.2, relheight = 0.5)
        
        self.panel = tk.Label(video)
        self.panel.grid()
        self.count_faces = tk.Label(stats)
        self.count_faces.place(relx = 0.2, rely=0.3)
        self.count_smiles = tk.Label(stats)
        self.count_smiles.place(relx = 0.2, rely=0.5)

        button = tk.Button(self.root, text = "Quit", command = self.close)
        button.place(relx = 0.8, rely = 0.8, anchor='s')

        self.vidCap = cv2.VideoCapture(0)
        #self.vidCap = WebcamVideoStream(src=0).start()
        #self.fps = FPS().start()
        fps = self.vidCap.get(cv2.CAP_PROP_FPS)
        print("Frames per second : {0}".format(fps))
        self.video_stream()
        #self.fps.stop()
        #print("[INFO] elasped time: {:.2f}".format(self.fps.elapsed()))
        #print("[INFO] approx. FPS: {:.2f}".format(self.fps.fps()))

        self.root.mainloop()
    
    def close(self):
        exit()
    
    def detectSmile(self, grayscale, img):
        num_faces = 0
        num_smiles = 0
        face = self.cascade_face.detectMultiScale(grayscale, 1.3, 5) 
        for (x_face, y_face, w_face, h_face) in face:
            cv2.rectangle(img, (x_face, y_face), (x_face+w_face, y_face+h_face), (255, 0, 0), 2)
            num_faces += 1
            ri_grayscale = grayscale[y_face:y_face+h_face, x_face:x_face+w_face] 
            ri_color = img[y_face:y_face+h_face, x_face:x_face+w_face]
            smile = self.cascade_smile.detectMultiScale(ri_grayscale, 1.7, 30) 
            for (x_smile, y_smile, w_smile, h_smile) in smile:
                cv2.rectangle(ri_color,(x_smile, y_smile),(x_smile+w_smile, y_smile+h_smile), (0, 0, 255), 2)
                num_smiles += 1
        return img, num_faces, num_smiles

    def video_stream(self):
        _, frame = self.vidCap.read()
        #frame = self.vidCap.read()
        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        final, faces_detected, smiles_detected = self.detectSmile(grayscale, frame)
        final = final[...,[2,1,0]]
        img = Image.fromarray(final)
        imgtk = ImageTk.PhotoImage(image=img)
        #self.fps.update()
        self.panel.imgtk = imgtk
        self.panel.configure(image=imgtk)
        self.count_faces.configure(text= "Faces Detected : "+str(faces_detected))
        self.count_smiles.configure(text= "Smiles Detected : "+str(smiles_detected))
        self.panel.after(1, self.video_stream) 

if __name__ == '__main__':
    appObj = App()