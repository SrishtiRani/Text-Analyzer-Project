from flask import Flask, render_template, request


app = Flask(__name__)

@app.get("/")
def showPage():
    return render_template('index.html')

@app.post('/analyze')
def analyze():
    text= request.form['text']
    action= request.form['action']
    answer=""
    if (action == "cntchr"):
        #count no of characters
        answer=f"the number of characters are:-{len(text)}"
    if (action=="cntws"):
        #count no of white spaces
        answer=f"the number of white spaces are:-{text.count(' ')}"
    if (action == "cstuc"):
        #convert string to upper case
        answer=f"upper case string is:-{text.upper()}"
    if (action == "cstlc"):
        #convert string to lower case
        answer=f"lower case string is:-{text.lower()}"
    if (action == "ctstc"):
        #capitalize the statement
        answer=f"capitalized string is:-{text.capitalize()}"
    if (action == "csil"):
        #check whether string is in lower case
        answer=f"the checked string is:-{text.islower()}"
    if (action == "csiu"):
        #check whether string is in upper case
        answer=f"the checked string is:-{text.isupper()}"
    if (action == "sts"):
        #swapcase the string
        answer=f"swapcase the string:-{text.swapcase()}"
    if (action == "csca"):
        #Check whether the string contains only alphabets
        answer=f"string ccontains only alphabets:-{text.isalpha()}"
    if (action == "cscad"):
        #Check string contains only alphabets and digits
        answer=f"string contains only alphabets and digits:-{text.isalnum()}"
    if (action == "cscd"):
        #Check whether the string contains only digits
        answer=f"string ccontains only alphabets:-{text.isdigit()}"
    return render_template('index.html', output = answer)

app.run(debug=True)