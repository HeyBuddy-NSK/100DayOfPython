from flask import Flask, render_template

app = Flask(__name__)

user = {'username':'nk_boy'}

def add_post():
    posts = [
        {
            'author':{'username':'thor'},
            'body' : 'Today there will be some lighting. please take care.'
        },

        {
            'author':{'username':'ironman'},
            'body':'Chotimaster :-|'
        }

    ]

    return posts

@app.route('/')
@app.route('/index')
def index():
    return f"""

<html>
<head>
    <title> Home Page - nk_blog </title>
</head>
<body>
    <h1> Hello, {user['username']}! </h1>
</body>
</html>

"""

@app.route('/render-template')
def rend_temp():
    return render_template('index.html',user=user,title="Rendering Template",page="rendering page.")

@app.route('/conditional')
def conditional():
    return render_template('conditional.html',title="Conditionals",user=user,page="conditional")

@app.route('/loops')
def loops():
    posts = add_post()
    return render_template('loops.html',title='Loops',user=user,posts=posts)

@app.route('/inheritance')
def inherit():
    posts = add_post()
    return render_template('inheritance.html', title="Inheritance",user=user,posts=posts)

if __name__=="__main__":
    app.run(debug=True)