from flask import Flask # Import Flask package
from flask import render_template # Import render_template function
app = Flask(__name__) # Construct Flask object named 'app'

'''
@app.route() defines the URLs that route to the index() function.
The URLs will be appended to the end of the base URL.
Links within HTML files should use the defined routes (for example '/index') as
the values for href attributes.
URLs that will call the index() function if running app.py on localhost:
	http://localhost:5000/
	http://localhost:5000/index
'''
@app.route('/') # URL for function (default for home page)
@app.route('/index') # Secondary URL for function
def index():
	return render_template('index.html') # located in templates/

@app.route('/restaurants')
def restaurants():
	return render_template('Restaurants.html')

@app.route('/reviews')
def reviews():
	return render_template('Reviews.html') # Example of argument passing to HTML template

@app.route('/reviewers')
def reviewers():
	return render_template('Reviewers.html')

@app.route('/about')
def about():
	return render_template('About.html')

@app.route('/review/1')
def review_1():

	restaurant = { 'name': 'VertsKebap' }
	reviewer = {
		'name': 'John Anderson',
		'review': '"Their Kebaps are really good and healthy. This place has changed a lot since I first started UT. Still my go to place when I need something fast, but have been a little disappointed in the prices increases. In particular, I really enjoy their beef and gyro wrap. Having lived a majority of my life in Germany where Doner Kebaps are a staple food, I can attest that the meat is fresh and pleasingly authentic. I would recommend anyone who wants to try some quick and tasty German food to come here!" - 2/1/2017',
		'service_rating':'5/5',
		'atmosphere_rating':'4/5',
		'value_rating':'4/5',
		'food_rating':'5/5',
		'dress':'Casual',
		'would_recommend':'Yes'
	}
	images = {
		1:'../static/img/vertspic.jpg',
		2:'../static/img/verts2.jpg',
		3:'../static/img/verts3.jpg'
		}

@app.route('/review/2')
def review_2():
	restaurant = {'name': 'WildwoodKitchen'}
	reviewer = {
		'name': 'James Connelly',
		'review': '"Before I start harping on the quality of the food, I will applaud Wildwood for having tremendous customer service. My waiter Sarah was always quick and responsive to my requests and showed enthusiasm and genuine concern for my experience at the restaurant. But beyond that, I will say, Wildwood is nothing more than subpar barbeque." - 2/1/2017',
		'service_rating': '5/5',
		'atmosphere_rating': '5/5',
		'value_rating': '3/5',
		'food_rating': '3/5',
		'dress': 'Casual or snappy casual at night because it is a bar',
		'would_recommend': 'No'
	}
	images = {
		1: '../static/img/wildwood1.jpg',
		2: '../static/img/wildwood2.jpg',
		3: '../static/img/wildwood3.jpg'
	}

	return render_template('Review.html', restaurant = restaurant, reviewer = reviewer, images = images)

@app.route('/restaurants/vertskebap')
def vertskebap():
	restaurant = {
	'name': 'VertsKebap',
	'rating': 4,
	'image':'../static/img/verts.jpg',
	'circlepic':'../static/img/johnpic.jpg',
	'cuisine':'Mediterranean',
	'price': '$',
	'address':'1801 E 51st St #300, Austin, TX 78723',
	'phone':'(512) 373-8736',
	'url':'http://eatverts.com'
	}
	review = {
		'rating':4,
		'text':'Their Kebaps are really good and healthy. This place has changed a lot since I first started UT. Still my go-to place when I need something fast, but I have been a little disappointed in the price increases.',
		'signature':'John, 02/01/2017',
	}
	return render_template('Restaurant.html', restaurant = restaurant, review = review)

@app.route('/restaurants/WildwoodKitchen')
def wildwoodkitchen():
	restaurant = {
	'name': 'WildwoodKitchen',
	'rating': 3,
	'image':'../static/img/wildwood3.jpg',
	'circlepic':'../static/img/jamesconnelly.jpg',
	'cuisine':'Barbeque, Sandwiches',
	'price': '$$',
	'address':'410 E Haley St Santa Barbara, CA 93101',
	'phone':'(805) 845-3995',
	'url':'http://wildwoodkitchensb.com'
	}
	review = {
		'rating':4,
		'text':'Before I start harping on the quality of the food, I will applaud Wildwood for having tremendous customer service. My waiter Sarah was always quick and responsive to my requests and showed enthusiasm and genuine concern for my experience at the restaurant. But beyond that, I will say, Wildwood is nothing more than subpar barbeque.',
		'signature':'James, 04/15/2016',
	}
	return render_template('Restaurant.html', restaurant = restaurant, review = review)

@app.route('/reviewer/johnanderson')
def john_anderson():
	reviewer = {'name':'John Anderson', 'date_joined':'April 1, 2013', 'origin':'Germany','location':'Austin, TX', 'fave_restaurant':'VertsKebap', 'bio':'I\'m a food lover and computer geek. In my free time, I like to play basketball with friends. I recieved my undergraduate degree from Techincal University of Munich and my PhD in Computer Science from UT Austin. I work as a senior data scientist at IBM.', 'img':'../static/img/johnpic.jpg'}

	return render_template('Reviewer.html', reviewer = reviewer)

@app.route('/reviewer/jamesconnelly')
def james_connelly():
	reviewer = {'name':'James Connelly', 'date_joined':'May 3, 2011', 'origin':'USA','location':'Santa Barbara, CA', 'fave_restaurant':'In-N-Out, Buffalo Wild Wings', 'bio':'Always on the lookout for new food. I love a classic burger and great BBQ, but I\'m open to trying all kinds of new cuisines!', 'img':'../static/img/jamesconnelly.jpg'}

	return render_template('Reviewer.html', reviewer = reviewer)

if __name__ == '__main__':
	app.run() # Run application
