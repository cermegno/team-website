import os
from flask import Flask, render_template

app = Flask(__name__)

f = open('Elliot.txt')
about_me = f.readlines()
f.close()

@app.route('/')
def mainmenu():

    ## I need to edit "main.html" so that there is link to my function "alberto"
    return render_template('main.html')

@app.route('/elliot')
def elliot():
    me_info = []
    for sections in about_me:
        me_info = sections.split(':')

    ## First thing in my function: read the text file "alberto.txt"
    ## then build my own page based on the contents of the file
    response = """<html><body>
    <h1>Elliot's page</h1></br>
    <h3>Name: {}</br>
    Hobbies: {}</br>
    Ideal Holiday: {}</html>""".format(me_info[0], me_info[1], me_info[2])
    
    return response

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
