from flask import request,render_template
import pandas as pd
from handlers import dfmodel



flag=0
df = None

def init_df():
    global df,flag
    if flag  == 0:
        flag = 1
        df = pd.read_csv('./data/diamonds.csv', index_col=0).head(20)


def configure(app):

    @app.route('/')
    def hello_world():
        global df
        init_df()
        return render_template('main.html',data=df)

    @app.route('/addnew')
    def add_new():
        return render_template('addnew.html')


    @app.route('/predict')
    def predict():
        return render_template('predict.html')

    
    @app.route('/additem',methods=['POST'])
    def additem():
        global df
        carat = float(request.form['carat'])
        cut = request.form['cut']
        color = request.form['color']
        clarity = request.form['clarity']
        depth = float(request.form['depth'])
        table = float(request.form['table'])
        x = float(request.form['x'])
        y = float(request.form['y'])
        z = float(request.form['z'])
        price = float(request.form['price'])
        df.loc[df.index.size] = [carat, cut, color, clarity, depth, table, price, x, y, z]
        print(df.loc[df.index.size])
        # df.to_csv('./data/diamonds.csv',index=False)
        return render_template('ok.html')

    @app.route('/predict',methods=['POST'])
    def predictitem():
        global df
        carat = float(request.form['carat'])
        cut = request.form['cut']
        color = request.form['color']
        clarity = request.form['clarity']
        depth = float(request.form['depth'])
        table = float(request.form['table'])
        x = float(request.form['x'])
        y = float(request.form['y'])
        z = float(request.form['z'])
        v = dfmodel.predict([carat, cut, color, clarity, depth, table, 0, x, y, z])
        return render_template('res.html',val=v)
    