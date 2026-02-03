from flask import Flask, render_template
from flask_mysqldb import MySQL
import config

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'mysql-21d9f0f9-iisgalvanimi-8e81.b.aivencloud.com'
app.config['MYSQL_USER'] = 'avnadmin'
app.config['MYSQL_PASSWORD'] = 'AVNS_xogXO8BBfCghY5AJ2nn'
app.config['MYSQL_DB'] = 'defaultdb'
app.config['MYSQL_PORT'] = 13692

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("select * from utenti")
    tables = cur.fetchall()
    cur.close()
    return render_template('index.html', utenti=tables)

if __name__ == '__main__':
    app.run(debug=True)
