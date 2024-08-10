import bokeh.io
import bokeh.plotting
from flask import Flask , render_template
from bokeh.plotting import figure , output_file , show
from bokeh.embed import components
from bokeh.resources import CDN
import numpy as np


app = Flask(__name__)

@app.route("/",methods=['GET'])
def home_page():
    #creating a bokeh plot 
    x = list(range(1,101))
    y = np.sin(x)
    p = figure(title="sin chart")
    p.line(x,y,color="red",legend_label = "red label",)
    script1,div1 = components(p)
    cdn_js = CDN.js_files
    cdn_css = CDN.css_files

    #Generating script and div elements
    script1 , div1 = components(p)
    cdn_js = CDN.js_files[0]
    cdn_css = CDN.css_files
    return render_template('index.html',script1=script1,div1=div1,cdn_js=cdn_js)

if __name__ == "__main__":
    app.run(debug=True)