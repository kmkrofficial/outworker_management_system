from flask import Flask, redirect, request, render_template, url_for, flash
import pymysql.cursors
import base64
from PIL import Image
import io

app = Flask(__name__)
app.config['SECRET_KEY'] = '6ab8269e9b583f88bdc64468c71ff454'
app.config['UPLOAD_FOLDER'] = 'D:\\Projects\\FMS'
db_connect = pymysql.connect(
    host="localhost",
    user="root",
    password="4152",
    db="mydb",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)
boolean = False

@app.route('/', methods=["POST", "GET"])
def homepage():
    if request.method == 'POST':
        worker = request.form["worker"]
        location = request.form["place"]
        return searchPage(worker, location)
    else:
        return render_template('homepage.html')


@app.route('/search')
def searchPage(helper, place):
    print(helper)
    print(place)
    try:
        with db_connect.cursor() as cursor:
                query = f"select id,fname,lname,city from freelancersReg where skill=\"{helper}\" and city=\"{place}\""
                cursor.execute(query)
                result = cursor.fetchall()
                print(result)
    except Exception as e:
        flash("Some Error has occured! Try Later!")
        print(e)
    return render_template('search.html', results=result)


@app.route('/userReg', methods=["POST", "GET"])
def userReg():
    if request.method == 'POST':
        fname = request.form["fname"]
        lname = request.form["lname"]
        city = request.form["city"]
        state = request.form["state"]
        pincode = request.form["pincode"]
        mobile = request.form["mobile"]
        alt_mobile = request.form["alt_mobile"]
        email = request.form["email"]
        password = request.form["password"]
        try:
            with db_connect.cursor() as Cursor:
                query = "INSERT INTO usersReg (fname, lname, city, state, pincode, mobile, alt_mobile, email, " \
                        "_password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) "
                Cursor.execute(query, (fname, lname, city, state, pincode, mobile, alt_mobile, email, password))
            db_connect.commit()
            flash('Registration Successful', 'success')
            return redirect(url_for("homepage"))
        except Exception as e:
            flash('Some error has occurred!', 'alert')
            print("Error Occurred!", e)
            return render_template('userReg.html')
    else:
        return render_template('userReg.html')


@app.route('/freelancerReg', methods=["POST", "GET"])
def freelancerReg():
    if request.method == 'POST':
        fname = request.form["fname"]
        lname = request.form["lname"]
        dob = request.form["dob"]
        city = request.form["city"]
        state = request.form["state"]
        pincode = request.form["pincode"]
        ph_no = request.form["ph_no"]
        email = request.form["email"]
        password = request.form["password"]
        description = request.form["description"]
        skill = request.form["skill"]
        experience = request.form["experience"]
        previous_company = request.form["prev_company"]
        from_time = request.form["from_time"]
        to_time = request.form["to_time"]   
        time_flexible = request.form["time_flexible"]
        profile_photo = ""
        work_samples = ""

        try:
            with db_connect.cursor() as Cursor:
                query = "INSERT INTO freelancersReg (fname, lname, dob, city, state, pincode, ph_no, email, " \
                        "_password, _description, skill, experience, previous_company, from_time, to_time" \
                        ", time_flexible,profile_photo, work_samples) VALUES (%s, %s, %s, %s, %s, " \
                        "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                print(profile_photo, work_samples)
                Cursor.execute(query, (
                    fname, lname, dob, city, state, pincode, ph_no, email, password, description, skill,
                    experience, previous_company, from_time, to_time, time_flexible, profile_photo, work_samples))
            db_connect.commit()
            flash('Registration Successful', 'success')
        except Exception as e:
            flash('Some error has occurred!', 'alert')
            print("Error Occurred!", e)
        return redirect(url_for("homepage"))
    else:
        return render_template('freelancerReg.html')


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        try:
            with db_connect.cursor() as cursor:
                sql = "SELECT email, _password FROM usersReg WHERE email=%s"
                cursor.execute(sql, email)
                result = cursor.fetchone()
                print(result)
                if result is None:
                    flash("Login Unsuccessful, Check credentials!")
                    return render_template('/login')
                if password == result["_password"]:
                    flash("Login Successful")
                print(result)
        except Exception as e:
            print(e)
    return render_template("login.html")


@app.route('/profile', methods = ["POST"])
def profile():
    id = request.form["workerid"]
    try:
        with db_connect.cursor() as cursor:
            query = f"select * from freelancersReg where id='{ id }'"
            cursor.execute(query)
            result = cursor.fetchone()
            print(result)
    except Exception as e:
        print(e)
    return render_template('profile.html', result= result)


if __name__ == "__main__":
    app.run(debug=True)
