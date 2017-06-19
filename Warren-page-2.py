import os
import uuid
from flask import Flask
app = Flask(__name__)

@app.route('/')
def piedpipers():

##    start_page = """<HTML><HEAD></HEAD><BODY><body bgcolor="#777799"><center><h1><font color="white"><h2>Pied Piper 2017 Team Members</h2></center>"""
##    end_page = "</body>"
##    mid_page = """<h1><font color="blue">"""
##    names = []
##    members = ""
##
##    filename = 'members.txt'
##    with open(filename) as file_object:
##        for line in file_object.readlines():
##            names.append(line.title())
##        for name in names:
##            members = members + """<a href={}>{}</a><br>""".format(name,name)
##        file_object.close()
##            
##    mid_page = mid_page + members
##    return start_page + mid_page + end_page

    return """
    <h2>Pied Piper 2017 Team Members</h2>
    <a href="alberto.html">Alberto</a><br>
    <a href="clive.html">Clive</a><br>
    <a href="Warren">Warren</a><br>"""

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
