from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/url_you_want")
def view_method():
    dropdown_list = ['Air', 'Land', 'Sea']
    return render_template('your_template.html', dropdown_list=dropdown_list)
if __name__ == '__main__':
   app.run(debug = True)