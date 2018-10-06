#%%
from flask import Flask, render_template, request
from flaskext.mysql import MySQL
import pandas

app = Flask(__name__)
app.debug = True
mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'scraper'
app.config['MYSQL_DATABASE_PASSWORD'] = 'scraper123$'
app.config['MYSQL_DATABASE_DB'] = 'scraper'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
TABLE_NAME = 'fxstreet'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

@app.route("/macrocal")
def econcalendar():
    start_date = request.args.get("start_date",None)
    end_date = request.args.get("end_date",None)
    data = ()
    #print (start_date,end_date)
    if start_date and end_date:
        start_date = int(start_date[6:] + start_date[3:5] + start_date[0:2])
        end_date   = int(end_date[6:] + end_date[3:5] + end_date[0:2])
        qStr = "SELECT * from " + TABLE_NAME + " where  nyc_date >= " + str(start_date) + " and nyc_date <= " + str(end_date) + " order by Country desc, nyc_date, nyc_time"
        #print(qStr)
        cursor.execute(qStr)
        # cursor.execute("SELECT * from "+TABLE_NAME + " where nyc_date = 20181003" )
        data = cursor.fetchall()
        #print(data)
        df = pandas.DataFrame(list(data), columns = ['Name', 'Country', 'Volatility', 'Actual', 'Estimated', 'Previous', 'utc_epoch', 'nyc_date', 'nyc_time'])
        df = df[['nyc_date', 'nyc_time', 'Name', 'Country', 'Volatility', 'Actual', 'Estimated', 'Previous', 'utc_epoch']]
        
    return render_template('index.html',data=data)


if __name__ == "__main__":
    app.run(port=5000)
    
