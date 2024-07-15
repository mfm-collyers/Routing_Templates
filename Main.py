from flask import Flask, render_template #Flask library and functions
import datetime

#Instantiate Flask App
app = Flask(__name__)

def getCurrentDateTime():
    date = datetime.datetime.now().date()
    time = datetime.datetime.now().time()
    return date.strftime("%d/%m/%Y"), time.strftime("%X") #Format the date and time correctly before returning

#Starting (index) page
@app.route('/')
def index():
    date, time = getCurrentDateTime()
    return render_template('home.html', date = date, time = time)

@app.route('/home')
def home():
    date, time = getCurrentDateTime()
    return render_template('home.html', date = date, time = time)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')


#Run in debug mode.
if __name__ == '__main__':
    app.run(debug = True)