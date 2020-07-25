#perception -> Decision ->Navigation
from flask import Flask
import time
app = Flask(__name__)
@app.route("/envoyerMsg1",methods=['GET'])
def predict1():
    k=time.time()
    response = app.response_class(
        response=str(k),
        status=200
    )
    return response

@app.route("/",methods=['GET'])
def predict12():
    import cv2
    import gluoncv as gcv
    cap = cv2.VideoCapture(0)
    while (True):
        ret, frame = cap.read()
        print(type(frame))
        fram = frame
        gcv.utils.viz.cv_plot_image(fram)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    response = app.response_class(
        response=fram,
        status=200
    )
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
