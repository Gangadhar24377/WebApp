from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Handle form submission (e.g., upload files, process data)
        return redirect(url_for('home'))
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')  # New route for the About Us page
def about():
    return render_template('about.html')

@app.route('/form')  # New route for the About Us page
def form():
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
