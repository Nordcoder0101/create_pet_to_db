
from flask import Flask, render_template, request, redirect
# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
app = Flask(__name__)


@app.route("/")
def index():
    # call the function, passing in the name of our db
    mysql = connectToMySQL('pets')
    # call the query_db function, pass in the query as a string
    pets = mysql.query_db('SELECT * FROM pets;')
    print(pets)
    return render_template("index.html", all_pets=pets)


@app.route("/create_pet", methods=["POST"])
def add_pet_to_db():
  mysql = connectToMySQL('pets')
  query = 'INSERT into pets (name, type, created_at, udated_at) VALUES (%(name)s, %(type)s, NOW(), NOW())'
  data = {"name": request.form['pet_name'], "type": request.form['pet_type']}

  new_pet_id = mysql.query_db(query, data)
  return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
