from flask import Flask, render_template,request,redirect,url_for
import csv
app = Flask(__name__)
#@app.route('/')
#def anyname():
#    return 'These are the contents'

@app.route('/') #for loading templates, default folder it looks from and necesary is templates also for css,js,favicon those should be in static folder
def webpage():
    return render_template('index.html')

'''
@app.route('/index.html') 
def homepage():
    return render_template('index.html')


@app.route('/works.html') 
def works():
    return render_template('works.html')


@app.route('/about.html') 
def about():
    return render_template('about.html')


@app.route('/contact.html') 
def contact():
    return render_template('contact.html')
'''
@app.route('/<string:page_name>')  # dynamically create function for displaying pages instead of the previous commands
def html_page(page_name):
	return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
    	try:
    		data = request.form.to_dict()
    		write_to_csv(data)
    		return redirect('/thankyou.html')
    	except:
    		return 'did not save in database'
    else:
    	print('something wrong')


def write_to_file(data):
	with open('database.txt',mode='a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
		with open('database.csv',newline='',mode='a') as database2:
			email = data["email"]
			subject = data["subject"]
			message = data["message"]
			csv_writer = csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
			csv_writer.writerow([email,subject,message])