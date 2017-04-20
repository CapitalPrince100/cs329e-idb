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

#REVIEWS

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

@app.route('/review/4')
def review_4():
	restaurant = {'name': 'Tulio'}
	reviewer = {
		'name': 'Tyler Durden',
		'review': '"Fantastic! Brought my girlfriend here for a date night and we both really enjoyed it. This place is expensive, but well worth it for a special occasion. The ambience was extremely conducive for setting an intimate mood; the soft music that plays in the background complements the dimly lit interior perfectly. Our servers were also excellent - they executed our orders perfectly without fail and even gave us a complimentary dessert at the end of dinner! Can\'t wait to come back." - 3/3/2016',
		'service_rating': '5/5',
		'atmosphere_rating': '5/5',
		'value_rating': '3/5',
		'food_rating': '5/5',
		'dress': 'Formal',
		'would_recommend': 'Yes'
	}
	images = {
		1: '../static/img/tulio1.jpg',
		2: '../static/img/tulio2.jpg',
		3: '../static/img/tulio3.jpg'
	}

	return render_template('Review.html', restaurant = restaurant, reviewer = reviewer, images = images)

@app.route('/review/5')
def review_5():
	restaurant = {'name': 'The Capital Grill'}
	reviewer = {
		'name': 'Paul Edgars',
		'review': '"I ordered the tuna tartare with avocado, mango and sriracha. Expecting a very fine meal, I ordered a fine glass of Pinot Grigio to go along with (what I *expected* to be) the culinary masterpiece that followed. Three words for the experience. Un. Be. Lievable. First the waitress tripped and spilled the wine bottle on my three piece suit. Proceeded to apologize and offer me my entire meal for free. Since I\'d already planned to go to the dry cleaners, I thought I\'d calmly wait it out and eat the free meal. Not worth it! The tuna tartare was TERRIBLY tart and the mango was well overripe. And one would think Sriracha would be the same restaurant to restaurant, but apparently NOT. Horribly tangy and watery. Overall *VERY* poor experience! The only thing redeeming was the cheesy bread appetizers (which I MUST find the recipe for). " - 4/01/2017',
		'service_rating': '2/5',
		'atmosphere_rating': '5/5',
		'value_rating': '1/5',
		'food_rating': '1/5',
		'dress': 'Formal',
		'would_recommend': 'No'
	}
	images = {
		1: '../static/img/capitalgrille1.jpg',
		2: '../static/img/capitalgrille2.jpg',
		3: '../static/img/capitalgrille3.jpg'
	}

	return render_template('Review.html', restaurant = restaurant, reviewer = reviewer, images = images)

@app.route('/review/6')
def review_6():
	restaurant = {'name': 'Snake River Grill'}
	reviewer = {
		'name': 'Madison Monet',
		'review': '"Let me just start by saying I consider myself a duck fry connoisseur. Now when I say Snake River Grill has some damn good duck fries I mean it. They are to die for! The service was great yadda yadda world class blah blah. The duck fries were the bees knees that\'s all that mattered. Go eat their duck fries." - 1/4/2014',
		'service_rating': '5/5',
		'atmosphere_rating': '4/5',
		'value_rating': '4/5',
		'food_rating': '5/5',
		'dress': 'Casual',
		'would_recommend': 'Yes'
	}
	images = {
		1: '../static/img/snakerivergrill3.jpg',
		2: '../static/img/snakerivergrill4.jpg',
		3: '../static/img/snakerivergrill5.jpg'
	}

	return render_template('Review.html', restaurant = restaurant, reviewer = reviewer, images = images)

@app.route('/review/7')
def review_7():
	restaurant = {'name': 'Slymans'}
	reviewer = {
		'name': 'Alex Buff',
		'review': '"I\'m a regular at Slyman\'s. I know the owner. The owner knows me. I walk in, give him a nod and he starts cooking my usual. Thats how a resuraunt should be run. No talking, no shenanigans.The food is great what else can I say. Their corned beef is good." - 5/4/2011',
		'service_rating': 'who cares',
		'atmosphere_rating': 'good enough',
		'value_rating': 'meat is value',
		'food_rating': 'quality',
		'dress': 'wear clothes',
		'would_recommend': 'do what you want'
	}
	images = {
		1: '../static/img/slymans1.jpg',
		2: '../static/img/slymans2.jpg',
		3: '../static/img/slymans3.jpg'
	}

	return render_template('Review.html', restaurant = restaurant, reviewer = reviewer, images = images)

@app.route('/review/8')
def review_8():
	restaurant = {'name': 'Scala\'s Bistro'}
	reviewer = {
		'name': 'Josh Davis',
		'review': '"The fog of time probably distorts my memory of Scala\'s somewhat but the standard of quality is down quite a bit and it\'s evident in the service, menu, and food. It\'s unfortunate but it is what it is - just another okay restaurant serving passable food to tourists. It was once so much better." - 3/3/2017',
		'service_rating': '3/5',
		'atmosphere_rating': '2/5',
		'value_rating': '2/5',
		'food_rating': '2/5',
		'dress': 'Casual',
		'would_recommend': 'No'
	}
	images = {
		1: '../static/img/scalasbistro.jpg',
		2: '../static/img/scalasbistro2.jpg',
		3: '../static/img/scalasbistro3.jpg'
	}

	return render_template('Review.html', restaurant = restaurant, reviewer = reviewer, images = images)

@app.route('/review/9')
def review_9():
	restaurant = {'name': 'Park\'s Barbeque'}
	reviewer = {
		'name': 'Young-Joun Kim',
		'review': '"On a blisteringly cold day in LA, several bros and I stepped into Park\'s for some kalbi and soondobu jjigae to warm the soul. Love the meat here - it\'s always so fresh and juicy. We ordered 4 platters of kalbi, 3 platters of bulgolgi, 3 platters of samgyobsal (pork belly), 4 orders of NY strip steak, 2 orders of grilled squid, and 4 bowls of soondobu jjigae. And the banchan here are soooo good!! Especially love the kimchi - Park\'s ferments their kimchi so it\'s pretty sour when you eat it, which is what I love. But, some of my non-Korean friends don\'t love it as much as I do, which is cool. My only request for Park\'s is to serve their food faster next time. They do use a classic KBBQ stalling technique to try to save some cash." - 12/28/2014',
		'service_rating': '3/5',
		'atmosphere_rating': '4/5',
		'value_rating': '5/5',
		'food_rating': '5/5',
		'dress': 'Casual',
		'would_recommend': 'Yes'
	}
	images = {
		1: '../static/img/parksbbq1.jpg',
		2: '../static/img/parksbbq2.jpg',
		3: '../static/img/parksbbq3.jpeg'
	}

	return render_template('Review.html', restaurant = restaurant, reviewer = reviewer, images = images)

@app.route('/review/10')
def review_10():
	restaurant = {'name': 'La Contenta'}
	reviewer = {
		'name': 'Amy Yang',
		'review': '"Beef wasn\'t well cooked...way too chewy and unseasoned. Probably wouldn\'t return again. But everything else wasn\'t bad...I will say, for vegetarians, it does have a redeeming factor: they do have a temporary buy-one-get-one deal for vegetarian tacos during certain hours. So perhaps if you\'re looking for a cheap, vegetarian meal in NYC for you and a friend...maybe you can stop by here. Just don\'t get the beef." - 10/22/2016',
		'service_rating': '4/5',
		'atmosphere_rating': '4/5',
		'value_rating': '1/5',
		'food_rating': '2/5',
		'dress': 'Casual',
		'would_recommend': 'No'
	}
	images = {
		1: '../static/img/la-contenta-interior.jpg',
		2: '../static/img/la-contenta-food-2.jpg',
		3: '../static/img/la-contenta-food-1.jpg'
	}

	return render_template('Review.html', restaurant = restaurant, reviewer = reviewer, images = images)

@app.route('/review/11')
def review_11():
	restaurant = {'name': 'El Taco Riendo'}
	reviewer = {
		'name': 'Sally Chen',
		'review': '"Everything on El Taco Riendo\'s menu is incredible. I\'ve ordered multiple variations of their taco trio, ranging from chicken to brisket to pork to tofu tacos - they have it all. Anything you want in a taco, they can make for you. I love the chill atmosphere of the restaurant. It\'s a great place to kick it with friends on the weekend; they also have an amazing drink selection. I\'d recommend the house sangria - but don\'t have more than two because they\'re quite strong :) I\'d highly recommend this to anyone who is taco obsessed like me!" - 01/15/2017',
		'service_rating': '4/5',
		'atmosphere_rating': '5/5',
		'value_rating': '5/5',
		'food_rating': '5/5',
		'dress': 'Casual',
		'would_recommend': 'Yes'
	}
	images = {
		1: '../static/img/eltacoriendo1.jpg',
		2: '../static/img/eltacoriendo2.jpg',
		3: '../static/img/eltacoriendo3.jpg'
	}

	return render_template('Review.html', restaurant = restaurant, reviewer = reviewer, images = images)

@app.route('/review/12')
def review_12():
	restaurant = {'name': 'Brasserie Les Halles'}
	reviewer = {
		'name': 'Robert Evremonde',
		'review': '"This is Chef Anthony Bourdain\'s restaurant. This is a fantastic restaurant, truly superb. The wine pairing is well thought out and a true delight. I am thankful that the oysters here at Les Halles remind me of the freshly shucked oysters I grew up eating in France. The bread here is also great, very fresh and aromatic -- all in all, this restaurant really reminds me of the famous Les Halles in Paris!" - 3/30/2017',
		'service_rating': '5/5',
		'atmosphere_rating': '5/5',
		'value_rating': '5/5',
		'food_rating': '5/5',
		'dress': 'Classy',
		'would_recommend': 'Yes'
	}
	images = {
		1: '../static/img/leshallespic.jpg',
		2: '../static/img/leshalles1.jpg',
		3: '../static/img/leshalles2.jpg'
	}

	return render_template('Review.html', restaurant = restaurant, reviewer = reviewer, images = images)

#RESTAURANTS

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
		'text':'I\'ll admit, I went into Ulele expecting great things. I\'d heard my ex-husband and his brand new wife had them cater his new wedding (with his brand new wife). I made reservations for 1 at Ulele 2 weeks in advance because I have a lot of free time in my single life, and I\'m able to think far in advance without a man on my mind. When the evening rolled around, I donned my new bonnet which I regained custody of, and took a taxi to the restaurant. I was seated at a table close to the animatronic singing pelican and placed my napkin in my lap. When the waitress came around I asked for: "1 Hawaiian Punch" because I only need onre drink for one person, but I was thoroughly dismayed that a fine restaurant like Ulele\'s didn\'t have Hawaiian Punch. Fudrucker\'s wouldn\'t make this mistake!!! However, I rallied and ordered a glass of iced tea in its place. Then, I was starting to feel liberated and free all by my lonesome, so I ordered a bowl of ice cream for dinner. Only 1 bowl because I only need 1 for 1 person eating. Me. But I got overzealous and started ordering ice cream hand over fist. More MORE MORE!!!! My tab came out to well over a hundred dollars, but since I\'m not spending money on my husband anymore, this wasn\'t a problem. I would strongly recommend this specific experience to all those lonely souls out there.',
		'signature':'Gabriella, 02/14/2017',
	}
	return render_template('Restaurant.html', restaurant = restaurant, review = review)

@app.route('/restaurants/tulio')
def tulio():
	restaurant = {
	'name': 'Tulio',
	'rating': 5,
	'image':'../static/img/tulio3.jpg',
	'circlepic':'../static/img/durdenpic.jpg',
	'cuisine':'Italian cuisine',
	'price': '$$$',
	'address':'1100 5th Ave Seattle, WA 98101 ',
	'phone':'(206) 624-5500',
	'url':'http://tulio.com'
	}
	review = {
		'rating':5,
		'text':'Fantastic! Brought my girlfriend here for a date night and we both really enjoyed it. This place is expensive, but well worth it for a special occasion. The ambience was extremely conducive for setting an intimate mood; the soft music that plays in the background complements the dimly lit interior perfectly. Our servers were also excellent - they executed our orders perfectly without fail and even gave us a complimentary dessert at the end of dinner! Can\'t wait to come back.',
		'signature':'Tyler, 03/03/2016',
	}
	return render_template('Restaurant.html', restaurant = restaurant, review = review)

@app.route('/restaurants/thecapitalgrill')
def thecapitalgrill():
	restaurant = {
	'name': 'The Capital Grill',
	'rating': 1,
	'image':'../static/img/capitalgrille2.jpg',
	'circlepic':'../static/img/pauledgars.jpg',
	'cuisine':'American, Steakhouse',
	'price': '$$$',
	'address':'801 Hennepin Ave, Minneapolis, MN 55402',
	'phone':'(612) 692-9000',
	'url':'http://thecapitalgrille.com/home'
	}
	review = {
		'rating':1,
		'text':'"I ordered the tuna tartare with avocado, mango and sriracha. Expecting a very fine meal, I ordered a fine glass of Pinot Grigio to go along with (what I *expected* to be) the culinary masterpiece that followed. Three words for the experience. Un. Be. Lievable. First the waitress tripped and spilled the wine bottle on my three piece suit. Proceeded to apologize and offer me my entire meal for free. Since I\'d already planned to go to the dry cleaners, I thought I\'d calmly wait it out and eat the free meal. Not worth it! The tuna tartare was TERRIBLY tart and the mango was well overripe. And one would think Sriracha would be the same restaurant to restaurant, but apparently NOT. Horribly tangy and watery. Overall *VERY* poor experience! The only thing redeeming was the cheesy bread appetizers (which I MUST find the recipe for). "',
		'signature':'Paul, 04/01/2017',
	}
	return render_template('Restaurant.html', restaurant = restaurant, review = review)

@app.route('/restaurants/snakerivergrill')
def snakerivergrill():
	restaurant = {
	'name': 'Snake River Grill',
	'rating': 4,
	'image':'../static/img/snakerivergrill2.jpg',
	'circlepic':'../static/img/madisonpic.jpg',
	'cuisine':'American Fare',
	'price': '$$$',
	'address':'84 East Broadway Jackson, WY',
	'phone':'(307) 733 0557',
	'url':'http://snakerivergrill.com/home'
	}
	review = {
		'rating':4,
		'text':'"Let me just start by saying I consider myself a duck fry connoisseur. Now when I say Snake River Grill has some damn good duck fries I mean it. They are to die for! The service was great yadda yadda world class blah blah. The duck fries were the bees knees that\'s all that mattered. Go eat their duck fries."',
		'signature':'Madison, 1/4/2014',
	}
	return render_template('Restaurant.html', restaurant = restaurant, review = review)

@app.route('/restaurants/slymans')
def slymans():
	restaurant = {
	'name': 'Slyman\'s',
	'rating': 5,
	'image':'../static/img/slymans1.jpg',
	'circlepic':'../static/img/AlexBuffpic.jpg',
	'cuisine':'Deli',
	'price': '$$',
	'address':'3106 St Clair Ave NE, Cleveland, OH 44114',
	'phone':'(216) 621-3760',
	'url':'http://slymans.com'
	}
	review = {
		'rating':5,
		'text':'I\'m a regular at Slyman\'s. I know the owner. The owner knows me. I walk in, give him a nod and he starts cooking my usual. Thats how a resuraunt should be run. No talking, no shenanigans.The food is great what else can I say. Their corned beef is good.',
		'signature':'Alex, 05/04/2011',
	}
	return render_template('Restaurant.html', restaurant = restaurant, review = review)

@app.route('/restaurants/scalasbistro')
def scalasbistro():
	restaurant = {
	'name': 'Scala\'s Bistro',
	'rating': 3,
	'image':'../static/img/scalasbistro.jpg',
	'circlepic':'../static/img/joshD.jpg',
	'cuisine':'Italian',
	'price': '$$$',
	'address':'432 Powell St San Francisco, CA 94102',
	'phone':'(415) 395-8555',
	'url':'http://scalasbistro.com'
	}
	review = {
		'rating':3,
		'text':'The fog of time probably distorts my memory of Scala\'s somewhat but the standard of quality is down quite a bit and it\'s evident in the service, menu, and food. It\'s unfortunate but it is what it is - just another okay restaurant serving passable food to tourists. It was once so much better.',
		'signature':'Josh, 3/3/2017',
	}
	return render_template('Restaurant.html', restaurant = restaurant, review = review)

@app.route('/restaurants/parksbarbeque')
def parksbarbeque():
	restaurant = {
	'name': 'Park\'s Barbeque',
	'rating': 5,
	'image':'../static/img/parksbbq1.jpg',
	'circlepic':'../static/img/youngjoun.jpg',
	'cuisine':'Korean Barbeque',
	'price': '$$',
	'address':'955 S. Vermont Ave, Los Angeles, CA 90006',
	'phone':'(213) 380-1717',
	'url':'http://parksbbq.com'
	}
	review = {
		'rating':5,
		'text':'On a blisteringly cold day in LA, several bros and I stepped into Park\'s for some kalbi and soondobu jjigae to warm the soul. Love the meat here - it\'s always so fresh and juicy. We ordered 4 platters of kalbi, 3 platters of bulgolgi, 3 platters of samgyobsal (pork belly), 4 orders of NY strip steak, 2 orders of grilled squid, and 4 bowls of soondobu jjigae. And the banchan here are soooo good!! Especially love the kimchi - Park\'s ferments their kimchi so it\'s pretty sour when you eat it, which is what I love. But, some of my non-Korean friends don\'t love it as much as I do, which is cool. My only request for Park\'s is to serve their food faster next time. They do use a classic KBBQ stalling technique to try to save some cash.',
		'signature':'Young-joun, 12/28/2014',
	}
	return render_template('Restaurant.html', restaurant = restaurant, review = review)

@app.route('/restaurants/lacontenta')
def lacontenta():
	restaurant = {
	'name': 'La Contenta',
	'rating': 2,
	'image':'../static/img/la-contenta-interior.jpg',
	'circlepic':'../static/img/amypic.jpg',
	'cuisine':'Mexican Cuisine',
	'price': '$$',
	'address':'102 Norfolk St New York, NY 10002 ',
	'phone':'(212) 432-4180',
	'url':'http://lacontentanyc.com'
	}
	review = {
		'rating':2,
		'text':'Beef wasn\'t well cooked...way too chewy and unseasoned. Probably wouldn\'t return again. But everything else wasn\'t bad...I will say, for vegetarians, it does have a redeeming factor: they do have a temporary buy-one-get-one deal for vegetarian tacos during certain hours. So perhaps if you\'re looking for a cheap, vegetarian meal in NYC for you and a friend...maybe you can stop by here. Just don\'t get the beef.',
		'signature':'Amy, 10/23/2011',
	}
	return render_template('Restaurant.html', restaurant = restaurant, review = review)

@app.route('/restaurants/eltacoriendo')
def eltacoriendo():
	restaurant = {
	'name': 'El Taco Riendo',
	'rating': 5,
	'image':'../static/img/eltacoriendo3.jpg',
	'circlepic':'../static/img/sallychen.jpg',
	'cuisine':'Mexican Cuisine',
	'price': '$',
	'address':'2412 Central Ave NE Minneapolis, MN 55418',
	'phone':'(612) 781-3000',
	'url':'http://eltaco-riendo.com'
	}
	review = {
		'rating':5,
		'text':'Everything on El Taco Riendo\'s menu is incredible. I\'ve ordered multiple variations of their taco trio, ranging from chicken to brisket to pork to tofu tacos - they have it all. Anything you want in a taco, they can make for you. I love the chill atmosphere of the restaurant. It\'s a great place to kick it with friends on the weekend; they also have an amazing drink selection. I\'d recommend the house sangria - but don\'t have more than two because they\'re quite strong :) I\'d highly recommend this to anyone who is taco obsessed like me!',
		'signature':'Sally, 01/15/2017',
	}
	return render_template('Restaurant.html', restaurant = restaurant, review = review)

@app.route('/restaurants/brasserieleshalles')
def brasserieleshalles():
	restaurant = {
	'name': 'Brasserie Les Halles',
	'rating': 5,
	'image':'../static/img/leshalles1.jpg',
	'circlepic':'../static/img/robertpic.jpg',
	'cuisine':'French Cuisine',
	'price': '$$$',
	'address':'15 John St, New York, NY 10038',
	'phone':'(212) 285-8585',
	'url':'http://leshalles.net'
	}
	review = {
		'rating':5,
		'text':'This is Chef Anthony Bourdain\'s restaurant. This is a fantastic restaurant, truly superb. The wine pairing is well thought out and a true delight. I am thankful that the oysters here at Les Halles remind me of the freshly shucked oysters I grew up eating in France. The bread here is also great, very fresh and aromatic -- all in all, this restaurant really reminds me of the famous Les Halles in Paris!',
		'signature':'Robert, 03/30/2017',
	}
	return render_template('Restaurant.html', restaurant = restaurant, review = review)

#REVIEWERS

@app.route('/reviewer/johnanderson')
def john_anderson():
	reviewer = {'name':'John Anderson',
				'date_joined':'April 1, 2013',
				'origin':'Germany','location':'Austin, TX',
				'fave_restaurant':'VertsKebap',
				'bio':'I\'m a food lover and computer geek. In my free time, I like to play basketball with friends. I recieved my undergraduate degree from Techincal University of Munich and my PhD in Computer Science from UT Austin. I work as a senior data scientist at IBM.', 'img':'../static/img/johnpic.jpg'
				}

	return render_template('Reviewer.html', reviewer = reviewer)

@app.route('/reviewer/jamesconnelly')
def james_connelly():
	reviewer = {'name':'James Connelly', 'date_joined':'May 3, 2011', 'origin':'USA','location':'Santa Barbara, CA', 'fave_restaurant':'In-N-Out, Buffalo Wild Wings', 'bio':'Always on the lookout for new food. I love a classic burger and great BBQ, but I\'m open to trying all kinds of new cuisines!', 'img':'../static/img/jamesconnelly.jpg'}

	return render_template('Reviewer.html', reviewer = reviewer)

@app.route('/reviewer/gabriellaromero')
def gabriella_romero():
	reviewer = {'name':'Gabriella Romero', 'date_joined':'September 8, 2013', 'origin':'Brazil','location':'Tampa Bay, FL', 'fave_restaurant':'Fudruckers, Applebee\'s', 'bio':'"A macaron by any other name would taste just as sweet" A well prepared, diverse meal is poerty. Each course should be a carefully thought out masterpiece to be cherished and savored. I\'m on a quest to find these master artists and to experience their masterpieces!', 'img':'../static/img/gabriellaromero.jpg'}

	return render_template('Reviewer.html', reviewer = reviewer)

@app.route('/reviewer/tylerdurden')
def tyler_durden():
	reviewer = {'name':'Tyler Durden', 'date_joined':'July 25, 2015', 'origin':'USA','location':'Seattle, WA', 'fave_restaurant':'Tulio', 'bio':'I am a freelance writer based in Seattle. When I\'m not writing, I love taking long walks along the beach, sitting in coffee shops, and enjoying fine wine. My first book inspired an award winning movie, so I am doing quite well. I love to explore the Seattle outdoors.', 'img':'../static/img/durdenpic.jpg'}

	return render_template('Reviewer.html', reviewer = reviewer)

@app.route('/reviewer/pauledgars')
def paul_edgars():
	reviewer = {'name':'Paul Edgars', 'date_joined':'June 3, 2015', 'origin':'USA','location':'Minneapolis, MN', 'fave_restaurant':'La Finca, Hasta La Pasta', 'bio':'Food, food, food. Three meals a day just doesn\'t cut it for me. Looking to experience all the riches the culinary world has to offer while meeting other enthusiasts along the way.', 'img':'../static/img/pauledgars.jpg'}

	return render_template('Reviewer.html', reviewer = reviewer)

@app.route('/reviewer/madisonmonet')
def madison_monet():
	reviewer = {'name':'Madison Monet', 'date_joined':'March 15, 2012', 'origin':'USA','location':'Jackson, WY', 'fave_restaurant':'Snake River Grill', 'bio':'I like to consider myself a small time duck fry critic. Up here in Wyoming, it might not seem to be very very exciting to focus in on the quality duck fries this town provides, but I love this town and I\'m set on giving my opinion for every single place that serves duck fries.', 'img':'../static/img/madisonpic.jpg'}

	return render_template('Reviewer.html', reviewer = reviewer)

@app.route('/reviewer/alexbuff')
def alex_buff():
	reviewer = {'name':'Alex Buff',
				'date_joined':'May 4, 2011',
				'origin':'USA','location':'Cleveland, OH',
				'fave_restaurant':'Slyman\'s',
				'bio':' I\'m just a dude who likes meat. Don\'t connect with me. I don\'t use the internet.', 'img':'../static/img/AlexBuffpic.jpg'
				}

	return render_template('Reviewer.html', reviewer = reviewer)

@app.route('/reviewer/joshdavis')
def josh_davis():
	reviewer = {'name':'Josh Davis',
				'date_joined':'June 4, 2013',
				'origin':'Germany',
				'location':'Santa Rosa, CA',
				'fave_restaurant':'None',
				'bio':' I am a business executive with a passion for cloud computing and data mining.', 'img':'../static/img/joshD.jpg'
				}

	return render_template('Reviewer.html', reviewer = reviewer)

@app.route('/reviewer/youngjounkim')
def young_joun_kim():
	reviewer = {'name':'Young-Joun Kim',
				'date_joined':'October 12, 2014',
				'origin':'South Korea',
				'location':'Los Angeles, CA',
				'fave_restaurant':'Park\'s Barbeque, KFC',
				'bio':'Korean food is the best type of food. Nothing beats a soondobu jjigae when it\'s cold outside, samgyobsal when it\'s time to celebrate, or Korean Fried Chicken (KFC) when you\'ve been having a rough week. Ya feel?',
				'img':'../static/img/youngjoun.jpg'
				}

	return render_template('Reviewer.html', reviewer = reviewer)

@app.route('/reviewer/amyyang')
def amy_yang():
	reviewer = {'name':'Amy Yang',
				'date_joined':'October 23, 2011',
				'origin':'China',
				'location':'New York, NY',
				'fave_restaurant':'Trump Grill, Le Bernardin',
				'bio':'I am film major at New York University. I am passionate about adventure and fantasy films in particular. Someday I hope I can a be a successful director. I enjoy going to the gym, trying food from different countries, and connecting with people from different cultures.',
				'img':'../static/img/amypic.jpg'
				}

	return render_template('Reviewer.html', reviewer = reviewer)

@app.route('/reviewer/sallychen')
def sally_chen():
	reviewer = {'name':'Sally Chen',
				'date_joined':'June 6, 2016',
				'origin':'Taiwan',
				'location':'Minneapolis, MN',
				'fave_restaurant':'Pappasito\'s Cantina, On the Border, small local taco joints',
				'bio':' I love to eat Mexican food! In particular, I have a love for tacos. I believe a taco can be made out of any meal. So far my favorite tacos have been from local taco food trucks in the area!',
				'img':'../static/img/sallychen.jpg'
				}

	return render_template('Reviewer.html', reviewer = reviewer)

@app.route('/reviewer/robertevremonde')
def robert_evremonde():
	reviewer = {'name': 'Robert Evremonde',
				'date_joined': 'March 28, 2017',
				'origin': 'France',
				'location': 'New York, NY',
				'fave_restaurant': 'Pappasito\'s Cantina, On the Border, small local taco joints',
				'bio': 'Growing up in South France, I\'ve developed a true passion for the world\'s freshest oysters. As I begin life in New York, I look forward to trying out the best that New York has to offer.',
				'img': '../static/img/robertpic.jpg'
				}

	return render_template('Reviewer.html', reviewer = reviewer)

if __name__ == '__main__':
	app.run('107.170.6.199', '8910') # Run application
