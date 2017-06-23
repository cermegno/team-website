import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def mainmenu():

    ## I need to edit "main.html" so that there is link to my function "alberto"

    return render_template('main.html')

@app.route('/alberto')
def alberto():

    ## First thing in my function: read the text file "alberto.txt"
    ## then build my own page based on the contents of the file
    response = """<html><body>
    <h1>Alberto's page<br/><h3>Add your dynamic content here</html>"""
    
    return response


@app.route('/Warren')
def wpj():

    start_page = """<HTML><HEAD></HEAD><BODY><body bgcolor="#777799"><center><h1><font color="white"><p><a href=/>Back to Member List</a></p></center>"""
    end_page = "</body>"
    mid_page = """<font color="white">
    <style>
    table, th, td {
       border: 1px solid white;
       color: white;
    }
    </style>"""
    strings = []
    hobbylist = ""

    filename = 'warren.txt'
    with open(filename) as file_object:
        lines = file_object.readlines()
        for line in lines:
            strings.append(line)
        file_object.close()
 
        for string in strings:
            person = string.split(":")
            hobbies = person[1].split(",")
            for hobby in hobbies:
                hobbylist = hobbylist + "<li>{}</li>".format(hobby)

            mid_page = mid_page + """
                <table>
                    <tr>
                        <td>Name</td>
                        <td>{}</td>
                    </tr>
                    <tr>
                        <td>Hobbies</td>
                        <td><ul>
                            {}
                            </ul></td>
                    </tr>
                    <tr>
                        <td>Ideal Holiday</td>
                        <td>{}</td>
                    </tr>
                </table>

            """.format(person[0],hobbylist,person[2])
    
    full_page = start_page + mid_page + end_page
    return full_page

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
