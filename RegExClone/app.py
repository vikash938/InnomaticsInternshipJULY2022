import email
import re
from flask import Flask, render_template, request

app = Flask(__name__)

##########################################

@app.route('/')
def index():
    return render_template("index.html")

# regex = ""
# string = ""


@app.route('/regex',methods=['POST'])
def regex_func():
    regex=request.form.get('regex')
    string=request.form.get('string')
    
    # """return "The regex is {} and the string is {}".format(regex,string)

    match=[(ele.start(), ele.end()) for ele in re.finditer(regex,string,flags=re.IGNORECASE)]
    count=len(match)
    
    # #returning the index page and variables to index.html page.
    return render_template('regoutput.html', r=regex, s=string, match=match, count=count)



#########################################

if __name__ == '__main__':
    app.run(debug=True)