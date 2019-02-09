from flask import Flask, render_template, request, redirect, url_for
from form import PersonalInfo

app = Flask('__name__')

app.secret_key = "development_key"

@app.route("/", methods=['POST', 'GET'])
def indexPage():
    form = PersonalInfo()
    fruits = ['Strawberry', 'Rospberry', 'Apple', 'Banana', 'Orange', 'Pear']
    f_ln = len(fruits)
    quanity = [0,1,2,3,4,5,6,7,8,9,10]
    q_ln = len(quanity)
    return render_template("index.html", form=form, fruits=fruits, f_ln=f_ln, quanity=quanity, q_ln=q_ln)

@app.route("/checkout", methods=['POST', 'GET'])
def checkout():
    form = PersonalInfo()
    if form.validate == False:
        return redirect("/")
    else:
        straw = form.straw.data
        ras = form.ras.data
        app = form.app.data
        total_order = int(straw) + int(ras) + int(app)
        studname = form.name.data
        studid = form.yourid.data
        print("Charging " + studname + " for " + str(total_order) + " fruits")
        return render_template("checkout.html", total_order=total_order, straw=straw, ras=ras, app=app, studname=studname, studid=studid)

if __name__ == '__main__':
    app.run(debug=True)