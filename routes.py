from flask import render_template, request, redirect, url_for
from init import app
from models import Feedback
from helpers import isEmpty

@app.route('/', methods=["GET", "POST"])
def index():
  if request.method == "POST":
    customer = request.form['customer']
    comments = request.form['comments']
    rate = request.form['rate']

    if isEmpty(customer):
      return render_template('form.html', message="please enter your name.")
    elif isEmpty(comments):
      return render_template('form.html', message="please type a comment.")

    feedback = Feedback(customer_name=customer, comments=comments, rating=rate)
    feedback.save()
    
    return render_template('success.html', title="Feedback sent successfully,")
  
  return render_template('form.html')


@app.route('/success/')
def success():
  return render_template('success.html', title="Feedback sent successfully.");


@app.route('/failed/')
def failed():
  return render_template('failed.html', title="Unexpected issue.")


@app.errorhandler(500)
def internal_server_error(error):
    return redirect(url_for('failed'))


@app.errorhandler(400)
def internal_server_error(error):
    return redirect(url_for('failed'))


@app.errorhandler(404)
def internal_server_error(error):
    return redirect(url_for('failed'))