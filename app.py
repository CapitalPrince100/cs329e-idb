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
		
	return render_template('Review.html', restaurant = restaurant, reviewer = reviewer, images = images)

	
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
	
@app.route('/review/3')
def review_3():
	restaurant = {'name': 'Ulele'}
	reviewer = {
		'name': 'Gabriella Romero',
		'review': '"I\'ll admit, I went into Ulele expecting great things. I\'d heard my ex-husband and his brand new wife had them cater his new wedding (with his brand new wife). I made reservations for 1 at Ulele 2 weeks in advance because I have a lot of free time in my single life, and I\'m able to think far in advance without a man on my mind. When the evening rolled around, I donned my new bonnet which I regained custody of, and took a taxi to the restaurant. I was seated at a table close to the animatronic singing pelican and placed my napkin in my lap. When the waitress came around I asked for: "1 Hawaiian Punch" because I only need onre drink for one person, but I was thoroughly dismayed that a fine restaurant like Ulele\'s didnt\' have Hawaiian Punch. Fudrucker\'s wouldn\'t make this mistake!!! However, I rallied and ordered a glass of iced tea in its place. Then, I was starting to feel liberated and free all by my lonesome, so I ordered a bowl of ice cream for dinner. Only 1 bowl because I only need 1 for 1 person eating. Me. But I got overzealous and started ordering ice cream hand over fist. More MORE MORE!!!! My tab came out to well over a hundred dollars, but since I\'m not spending money on my husband anymore, this wasn\'t a problem. I would strongly reccomend this specific experience to all those lonely souls out there." - 2/14/2017',
		'service_rating': '5/5',
		'atmosphere_rating': '5/5',
		'value_rating': '5/5',
		'food_rating': '5/5',
		'dress': 'Snappy Casual',
		'would_recommend': 'Yes'
	}
	images = {
		1: '../static/img/ulele1.jpg',
		2: '../static/img/ulele2.jpg',
		3: '../static/img/ulele3.jpg'
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
		'rating':3,
		'text':'Before I start harping on the quality of the food, I will applaud Wildwood for having tremendous customer service. My waiter Sarah was always quick and responsive to my requests and showed enthusiasm and genuine concern for my experience at the restaurant. But beyond that, I will say, Wildwood is nothing more than subpar barbeque.',
		'signature':'James, 04/15/2016',
	}
	return render_template('Restaurant.html', restaurant = restaurant, review = review)

@app.route('/restaurants/ulele')
def ulele():
	restaurant = {
	'name': 'Ulele',
	'rating': 5,
	'image':'../static/img/ulele3.jpg',
	'circlepic':'../static/img/gabriellaromero.jpg',
	'cuisine':'Native American',
	'price': '$$$',
	'address':'1810 North Highland Avenue, Tampa Bay, FL 33602',
	'phone':'(813) 999-4952',
	'url':'http://ulele.com'
	}
	review = {
		'rating':5,
		'text':'I\'ll admit, I went into Ulele expecting great things. I\'d heard my ex-husband and his brand new wife had them cater his new wedding (with his brand new wife). I made reservations for 1 at Ulele 2 weeks in advance because I have a lot of free time in my single life, and I\'m able to think far in advance without a man on my mind. When the evening rolled around, I donned my new bonnet which I regained custody of, and took a taxi to the restaurant. I was seated at a table close to the animatronic singing pelican and placed my napkin in my lap. When the waitress came around I asked for: "1 Hawaiian Punch" because I only need onre drink for one person, but I was thoroughly dismayed that a fine restaurant like Ulele\'s didnt\' have Hawaiian Punch. Fudrucker\'s wouldn\'t make this mistake!!! However, I rallied and ordered a glass of iced tea in its place. Then, I was starting to feel liberated and free all by my lonesome, so I ordered a bowl of ice cream for dinner. Only 1 bowl because I only need 1 for 1 person eating. Me. But I got overzealous and started ordering ice cream hand over fist. More MORE MORE!!!! My tab came out to well over a hundred dollars, but since I\'m not spending money on my husband anymore, this wasn\'t a problem. I would strongly reccomend this specific experience to all those lonely souls out there.',
		'signature':'Gabriella, 02/14/2017',
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

@app.route('/reviewer/gabriellaromero')
def gabriella_romero():
	reviewer = {'name':'Gabriella Romero', 'date_joined':'September 8, 2013', 'origin':'Brazil','location':'Tampa Bay, FL', 'fave_restaurant':'Fudruckers, Applebee\'s', 'bio':'"A macaron by any other name would taste just as sweet" A well prepared, diverse meal is poerty. Each course should be a carefully thought out masterpiece to be cherished and savored. I\'m on a quest to find these master artists and to experience their masterpieces!', 'img':'../static/img/gabriellaromero.jpg'}

	return render_template('Reviewer.html', reviewer = reviewer)	
	
if __name__ == '__main__':
	app.run() # Run application
