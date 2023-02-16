from flask import Flask
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
        host = "151.106.97.0",
        user = "u679110385_iperez",
        password = "Kay20071***314",
        database = "u679110385_eflkids"
)

@app.route("/", methods=["GET"])
def index():
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT id, teacher_id FROM users LIMIT 5")    
    return "test" 

if __name__ == "__main__":
    app.run(debug=True)
