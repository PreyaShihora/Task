import scheduling_task

from flask import Flask, render_template, request, flash

app = Flask(__name__)


@app.route('/')
def student():
   return render_template('test.html')

@app.route('/user',methods = ['POST', 'GET'])
def users():
   if request.method == 'POST':
      user = request.form.get("User")
      profile = request.form.get("Profile")
      startdate = request.form.get("StartDate")
      enddate = request.form.get("EndDate")
      data_file=scheduling_task.schedule_task(user, profile, startdate, enddate)

      return render_template("user.html", result = data_file)

@app.route('/result',methods = ['POST', 'GET'])
def res():
   if request.method == 'POST':
      data_file = scheduling_task.result()
   return render_template('result.html',result=data_file)


if __name__ == '__main__':
   app.run(debug = True)