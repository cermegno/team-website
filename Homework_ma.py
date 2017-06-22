import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def mainmenu():

    ## I need to edit "main.html" so that there is link to my function "alberto"
    return render_template('main.html')

@app.route('/michael')
def michael():

    ## First thing in my function: read the text file "michael.txt"
    ## then build my own page based on the contents of the file

    with open("michael.txt") as f:
        mylist = f.read().split(':')
    f.close()


    hobbies ="<ul>"
    
    for h in mylist[1].split(','):
        hobbies += "<li>" + h + "</li>"
    hobbies += "</ul>"
            
    dynamic = """<table style="width:50%"><tr><th>Name</th>"""
    dynamic += "<th>" + mylist[0] + "</th></tr>"
    dynamic += "<tr><td>Hobbies" + "</td><td>" + hobbies + "</td></tr>"
    dynamic += "<tr><td>Ideal Holiday" + "</td><td>" + mylist[2] + "</td></tr>"
    
    response = """<html><body>
                <style>
                    table, th, td {
                        border: 1px solid black;
                        border-collapse: collapse;
                    }
                    th {
                        text-align: left;
                    }
                </style>
    <h1>Michael's page<br/>""" + dynamic + """</html>"""
    
    return response

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
