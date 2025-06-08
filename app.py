from flask import Flask, render_template_string, send_file

app = Flask(__name__)

menu = {
    'Tiffin 1': {'name': 'Idli with Sambar & Chutney', 'price': 40, 'image': 'idli.png'},
    'Tiffin 2': {'name': 'Masala Dosa', 'price': 50, 'image': 'masala.png'},
    'Tiffin 3': {'name': 'Poori', 'price': 40, 'image': 'poori.png'},
    'Tiffin 4': {'name': 'Chapathi with Curry', 'price': 45, 'image': 'chapathi.png'},
    'Lunch': {'name': 'Veg Meals', 'price': 130, 'image': 'image.png'}
}

def read_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        return f.read()

@app.route('/')
def welcome():
    return render_template_string(read_file('welcome.html'))

@app.route('/menu')
def menu_page():
    return render_template_string(read_file('index.html'), menu=menu)

@app.route('/<filename>')
def send_static_file(filename):
    return send_file(filename)

if __name__ == '__main__':
    app.run(debug=True)
