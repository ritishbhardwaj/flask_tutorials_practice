from  flask import Flask,render_template,url_for
app=Flask(__name__)

app.config['SECRET_KEY']='0ff0b9cf40e81e610d61c81e75f876db'

posts=[
    
    {
        'author': 'Nimish ',
        'title': 'Only Bhakchodi',
        'content' : 'not for us',
        'date_posted': 'April 1 , 2020'
    },
    {
        'author': 'Rishabh ',
        'title': 'Only Bhakchodi 2',
        'content' : 'not for general public',
        'date_posted': 'April 10 , 2020'
    }
    
    
]



@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html',poss=posts,title='home')


@app.route('/about')
def about():
    return render_template('about.html',title='about')
# @app.route('')

if __name__=="__main__":
    app.run(debug=True)