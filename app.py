from flask import Flask,render_template,url_for,request,redirect
from detecto import core, utils, visualize
import os
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = {'png', 'jfif', 'mov', 'jpg', 'jpeg', 'gif'}
app=Flask(__name__)


@app.route('/')
def game1():
  return render_template('home.html') 
@app.route('/document')

def game():
  return render_template('index.html') 


@app.route('/implement')
def gam():
  return render_template('base.html')
  
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file'] 
        basepath=os.path.dirname(__file__)
        file_path=os.path.join(basepath,secure_filename(f.filename))
        
       
        
        
        f.save(file_path)
        model = core.Model.load('heo_model_weights.pth', ['heo'])
        image = utils.read_image(file_path)
        predictions = model.predict(image)
        
        labels, boxes, scores = predictions
        
        scores=scores
        
        alt_score=[]
        for i in scores:
            alt_score.append(float(i))
        
        heo=[0]
       
        j=0
        for i in labels:
            if i=="heo":
                heo.append(alt_score[j])
            
            j=j+1
        final=[]    
        heo_score=max(heo)
        
        heo_score=round(heo_score*100,2)
        if (heo_score>75):
            final.append("heo")
     
        
        
        
       
        return render_template("base.html",heo_score=heo_score,final=final,len=len(final))
        final=[]



if __name__=='__main__':
     app.run(debug=True)