# Face Smile Detection

This project aims to to detect faces and show indicators if the face is smiling or not. 

## Getting started

- Run the application directly, open the .exe file
- Or can run it via terminal, run the python script `app.py`

## Design Consideration 

- Used Haarcascade features to detect smile and face 
- Tkinter is used to build the GUI as it is simple and light

## Limitations

- App may fail to recognize the smile sometimes if the angle and lighting is bad, can use deep learning to improve the results

## How the design can scale for large-scale implementation

- If it's being deployed on many edge devices it doesn't require backend processing, the .exe can be installed directly on each device
- We can also deploy it on a cloud platform and we can use auto scaling features like Kubernetes to manage it  
