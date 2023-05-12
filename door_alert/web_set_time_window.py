from flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        start_hour = int(request.form.get('start_hour'))
        start_minute = int(request.form.get('start_minute'))
        end_hour = int(request.form.get('end_hour'))
        end_minute = int(request.form.get('end_minute'))
        time_window = {
            'start_hour': start_hour,
            'start_minute': start_minute,
            'end_hour': end_hour,
            'end_minute': end_minute
        }
        with open('time_window.json', 'w') as f:
            json.dump(time_window, f)
        return 'Time window updated successfully!'
    else:
        return render_template('index.html')  # serve your HTML page

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
