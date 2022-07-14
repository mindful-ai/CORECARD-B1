# Note we imported request!
from flask import Flask, render_template, request, send_file
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('allinputs.html')

@app.route('/process', methods=["GET", "POST"])
def process():
    '''
    # This is for GET request
    print('First  Name: -> ' + str(request.args.get('fname')))
    print('Middle Name: -> ' + str(request.args.get('mname')))
    print('Lase   Name: -> ' + str(request.args.get('lname')))
    '''
    print(request.form)
    print(request.files['cert']) # File upload and save
    file = request.files['cert']
    file.save('downloads/cert.txt')
    return ('<h1>Thank you! {} </h1>'.format(str(request.form.get('fname'))))

@app.route('/download', methods=['GET', 'POST'])
def download():
    return send_file(r"C:\Users\Purushotham\Desktop\OracleJET\part_01\css\css\pics\pic-kailash.jpg", attachment_filename='google.jpg')
    #return send_file(r"C:\Users\Purushotham\Desktop\Research\HTML\code\pics\google.jpg", attachment_filename='') # browser saves it

'''
# This page will have the sign up form
@app.route('/signup_form')
def signup_form():
    return render_template('06-Sign-up.html')

# This page will be the page after the form
@app.route('/thankyou')
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('06-thankyou.html',first=first,last=last)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('06-404.html'), 404
'''

if __name__ == '__main__':
    app.run(debug=True)
