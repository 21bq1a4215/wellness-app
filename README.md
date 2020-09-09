# WELLNESS APP

## Full Stack Ecommerce Django

### Demo App here: _https://wellness-app-django.herokuapp.com/_

The Wellness App was developed and deployed by Giselle Chacon as the last project
for the Code Institute Software Development diploma. It’s a place where users can connect
with an online wellness community, purchase products for their own at-home wellness routine,
read blogs from industry experts and access online workout content - all in one place.

Users can purchase products from the site and read the blog without needing 
to register or login. To access video content, and leave reviews and blog comments, 
users must register. They can register with their name, email and password in a secure 
manner. There is also an option to subscribe to the site to access advanced video content.

The app uses Stripe API to process payments for products and subscriptions.

## Table of Contents

- [**About**](#About)
- [**UX**](#UX)
  - [User Stories](#User-Stories)
  - [Design Choices](#Design-Choices)
  - [Wireframes](#Wireframes)
- [**Information Architecture**](#Information-Architecture)
  - [Database Structure](#Database-Structure)
- [**Features**](#Features)
  - [Existing Features](#Existing-Features)
  - [Features Left To Implement](#Features-Left-To-Implement)
- [**Technologies**](#Technologies)
  - [Tools](#Tools)
  - [Frontend Technologies](#Frontend-Technologies)
  - [Backend Technologies](#Backend-Technologies)
  - [Languages](#Languages)
- [**Testing**](#Testing)
- [**Deployment**](#Deployment)
  - [Getting Started](#Getting-Started)
  - [Github Deployment](#Github-Deployment)
  - [Heroku Deployment](#Heroku-Deployment)
- [**Credits**](#Credits)
  - [Code](#Code)
  - [Content](#Content)
  - [Media](#Media)
  - [Acknowledgements](#Acknowledgements)
- [**Disclaimer**](#Disclaimer)


## UX

### User Stories

**“As an online shopper____”**

- “...I want to easily purchase wellness products online, without needing to 
    create an account.”
- “...I want to purchase items securely, and receive confirmation of purchase to 
    my email account.”
- “...I want to read reviews of products I’m interested in, and leave reviews for 
    products I’ve purchased myself”

**“As someone interested in wellness…”**

- “...I want to access high quality yoga training online so that I can practice 
    in the comfort of my own home.”
- “...I want to read blogs by experienced professionals, and join a conversation
     in the comments.”
- “...I want to access basic online training materials before committing to a paid
     subscription.”

**“As a site user…”**

- “...I want to easily and securely register for an account, and be able to l
    og in and out.”
- “...I want to be able to recover my password if I forget it.”
- “...I want to be able to find information about the company, 
    such as email address and phone number.”


### Design Choices

The direction taken for styling this web app was to prioritise a minimal design in 
distinctive brand colours, which is easy and pleasant to read and navigate, as well as 
being responsive to provide the best possible user experience.

#### Primary Colour Palette
The colour palette was chosen to create a minimalist and calming experience. 
A simple and indigo and white colour palette was selected, to complement the tones of 
the yoga images and illustrations. 
Hex colours used #667eea, #fff and #F0F0F0.


#### Fonts

These two fonts used for all titles, subtitles and text on the app.

Font-family: 'Montserrat', sans-serif and 'Inter', sans-serif.


#### Responsivity

This website is fully responsive on all screen sizes and devices, making the app easy to navigate.  


### Wireframes

Wireframes were developed using Adobe XD. This was a personal choice as I find it to be a rapid and iterative process for developing wireframes.

The links to these images are available at the following links:



- [**_Wireframe 1_**](media/wireframe1.png)

- [**_Wireframe 2_**](media/wireframe2.png)

- [**_Wireframe 3_**](media/wireframe3.png)

- [**_Wireframe 4_**](media/wireframe4.png)

- [**_Wireframe 5_**](media/wireframe5.png)

- [**_Wireframe 6_**](media/wireframe6.png)

- [**_Wireframe 7_**](media/mobileviews.png)



### Information Architecture

Wellness App is composed of 10 different applications: users, profiles, bag, 
checkout, home, pro_payment, products, videos and wellness_apps. Using MVC 
architecture from the Django framework, each application holds its own model, 
view and controller that interacts all together into the wellness_app which basically 
is the controller of the overall application.

#### Database Structure

- Users: email / name / address / permissions
- Blog: blogpost / title / description / author / comments
- Checkout: orders / date / email / price
- Orders: user / email / products / personal info
- Products: product list / name / description / price / categories /sku / image
- Categories: name / data_name

**Stripe Subscription Model**

- Courses: video / pricing / vimeo_id / thumbnail
- Pricing: price per month / id / name / currency (basic/pro)
- Subscription: User / stripe_subscription_id / status (active / canceled / past_due / trialing / Pricing 
- Videos: vimeo_id / title / slug / description / order


## Features

### Existing Features

**Navbar**

- The navbar is fixed to the top for easy navigation
- Site logo redirects to homepage
- The navbar is responsive on on mobile screens

**Shop**

- Shows a list of products present in the database, user can view all available 
products, can sort by price or alphabetical order, or display only the products 
in one category
- Shopping layout is responsive when viewing on mobile
- Users can click on a product to see details of specific product and associated 
reviews
- Users have the option to add to their bag after selecting a product or to go 
back to the shop homepage to keep browsing

**Reviews**

- User can read reviews of each product left by other users
- When a user is logged in they can leave a review on any product
- Users can see product rating when viewing the shop homepage


**Bag**

- Users can add products to their bag - the bag on the navbar will automatically 
update with the total price of products added
- When clicking on the bag on the navbar, users are redirected to their 
shopping bag, displaying all the products they have selected
- User can update quantities or remove items from their bag
- User can proceed to checkout for payment or keep shopping
- Total amount to be paid by the user is shown in the bag


**Checkout**

- When selecting to proceed to checkout from the bag, the user is redirected to 
the checkout page with a summary of all items, detail and price
- Forms are displayed for the user to enter personal info like address, name of 
the user and delivery information
- Stripe card payment element is shown for the user to enter their card details 
to proceed with payment
- Checkout view includes the total cost of the order to be paid
- When all the required information is completed, the user will be redirected 
to a summary of their order and an alert message will be shown indicating the 
purchase was successfully complete
- An email confirmation with order summary is sent to the user


**Pro Membership**

- Users can view the free course available without a subscription
- Users can select to purchase a paid subscription  by selecting “get pro 
subscription”, which will redirect to a card payment form where the user 
can enter their card details and proceed with payment
- Once the user is subscribed, the user can access the pro members video course
- Admin users can log to Django admin and manage the ‘pro members’ video courses 
section, as well as manage subscriptions of registered users

**Footer**

- The footer contains contact information and social icon links, which redirect 
to appropriate social pages

**Register Account**

- Users can register securely with a username, email and secure password 
- Username must be unique
- Password must contain at least 8 characters, of which at least one must be numeric, 
and cannot contain the username
- When the user successfully registers, a pop-up alert communicates that a verification 
email has been sent to the user and redirects them to a new page with information 
about next steps
- The user receives an email with a verification link and information on how to use the 
link to verify their account
- Once the user completes the verification process, they are redirected to the homepage


**Log in**

- Once the account is verified, the user can log in with their username and password
- If the incorrect username or password is entered, the site will communicate this to the user

**Reset Password**

- On the login page, you can find the “forgot password” link, which will lead to a 
form where the user enters their email address
- User can enter the email from the account you need to reset the password for
- The user will receive an email with a link that will allow them to add a different 
password by sending you to a reset password form
- The user adds a new password and confirms it
- Once the password is confirmed, the user can log in using the new password

**Product Management**

- When an admin user is logged in, product management options are available
- Admin users can add, edit and delete products

**Django Admin Page**

- Admin users can also access the Django admin page with additional functionalities
- The admin page is separated into five sections:
        - Authentication and Authorisation, where the admin can see and manage the users 
        on the website
        - Checkout, where the admin can see orders made by customers.
        - Products and Categories, where the admin can manage all the products for sale 
        (add, edit and delete products, including a photo), as well as add and edit categories
        - Videos, where admin can manage all content for the Courses section of the 
        site  - add, edit and delete courses, change pricing, manage subscriptions 
        and add and manage video content using Vimeo
        - Blog, where the user can add, edit and delete blog entries


### Features Left to Implement

- **Cancel Subscription**
        - Add an option for users to cancel their subscription through 
        their profile (I didn’t have enough time to implement this feature)
- **Profile Personalisation**
        - Further develop the functionality on user profiles so users 
        can have a public bio and avatar, view their membership plan and edit their profiles
- **Social Account**
        - Enable single sign-in using Facebook, so users can register, 
        login and transfer their personal information from Facebook (I tried to implement this 
        feature and while it initially appeared to have worked, after deployment I was blocked 
        due to a lack of permissions, so I removed this feature from the code to avoid further issues)
- **Free Trial Subscription**
        - Offer the option of a free trial subscription to users when they register 


## Technologies 

The languages, frameworks, libraries and other tools utilised for building this web-app are:

## Tools

  - [Gitpod](https://www.gitpod.io/) as my dev enviroment and workspace for this project.
  - [Stripe](https://stripe.com/ie) to receive payments.
  - [Heroku](https://www.heroku.com/) for hosting the application and deploy.
  - [AWS S3](https://aws.amazon.com/s3/) was used as a cloud service to host static files.
  - [Github](https://github.com/) to share and store code remotely.
  - [Git](https://git-scm.com/) was used to manage version control.
  - [Sqlite3](https://www.sqlite.org/index.html) a database provided by django for development.
  - [PostgreSQL](https://www.postgresql.org/), a robust database provided by Heroku for production 
  development.
  - [Adobe XD](https://www.adobe.com/) for the wireframes design.

## Libraries and frameworks

  - [Django](https://www.djangoproject.com/) a high level python web-framework used to design this project.
  - [Bootstrap 4](https://getbootstrap.com/) a CSS library grid used for the development of this site.
  - [FontAwesome](https://fontawesome.com/) for the creation and implementation of icons.
  - [Google fonts](https://fonts.google.com/) to bring custom font styling.
  - [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) a template language for python used to bring 
  logic into templates.
  - [Psycopg2-binary](https://pypi.org/project/psycopg2-binary/#description) used as the Python 
  PostgreSQL adapter.
  - [Jquery](https://jquery.com/) a Javascript library to simplify the code.
  - [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) a library that 
  enables python code to modify AWS service.
  - [AOS](https://michalsnik.github.io/aos/) used to bring animation on scroll.

## Languages

  - This project uses HTML, CSS, Javascript and Python programming languages

## Testing

The testing information can be found in this separate file [Testing](https://github.com/GiselleNessi/django-wellness-app/blob/73b9ad945ad1e2041f9e4d8286eba33bed6a109a/README.md)

## Deployment 

### Getting Started

The web app is created in the Gitpod environment and regularly committed to 
GitHub after each crucial piece of coding. 


### Github Deployment

1. Created a master branch in Github repository.
2. Used Gitpod environment for the development process of the site.
3. Committed files to the using the terminal commands: git status; git add; 
git commit -m"add message" and git push.
4. Pushed files to github, which then updates the repository.
5. The repository can be cloned by clicking Clone or Download on the main page of the repository.
6. In the Clone with HTTPs section, clicked the clipboard icon to copy the clone URL for the repository.
7. Opened my terminal, typed git clone, and then pasted 
the URL https://github.com/GiselleNessi/django-wellness-app.
8. Pressed Enter; a local clone was created.
9. Created a file named env.py in the root directory of your project to define your 
environment variables; I used environment variables in gitpod settings for this project.


### Heroku Deployment

1. Created a Heroku account @ https://signup.heroku.com/
2. Created requirements.txt file in Gitpod workspace for Heroku to understand 
installation files to run app. From CLI type pip3 freeze --local > requirements.txt.
3. To install the Heroku command line on Gitpod, used the following command npm install -g heroku.
4. On the Heroku dashboard, created a new app with appropriate title and server in Heroku. 
5. This creates a connection between the Gitpod application and Heroku that would allow us 
to push our changes using Git to update the application at any given time.
6. To login to Heroku from the CLI, used the command heroku login.
7. To get the application up and running a Procfile is required that instructs Heroku which 
file is the entry point. I used the following command to create this: echo web: python app.py.
8. Code that is prepared to be pushed from Github to Heroku can be executed following the 
CLI commands: git add . git commit -m "fist Heroku commit" git push
9. Now that the relevant code has been pushed to Github, it can also be pushed to Heroku from 
the chosen branch (e.g. Master).
10. To connect an existing repository from Github to Heroku, I used the following 
CLI syntax: heroku git:remote -a [followed by name of Heroku app].
11. To push to Heroku Master Branch, then simply use git push heroku master.
12. In order for the server instance on Heroku to know how to run our application, we needed to 
specify a few Config Vars in Heroku. This was done by navigating to the to 
Settings tab > Config Variables and input: AWS_ACCESS_KEY_ID; AWS_SECRET_ACCESS_KEY; DATABASE_URL; 
DISABLE_COLLECTSTATIC; EMAIL_ADDRESS; EMAIL_PASSWORD EMAIL_PASSWORD; SECRET_KEY; STRIPE_PUBLISHABLE; 
STRIPE_SECRET.
13. The following syntax needs to be added to your settings.py file to access the SECRET KEY for 
the new database URL DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}
14. The Database could then be migrated to the Heroku Postgres (postgresql) database using the 
commands makemigrations and migrate from the command line.
15. Once the build in Heroku was complete, we clicked the Open app button.
16. Objects could then be added to the new postgres database using the Admin Panel and logging in 
with your superuser credentials.


## Credits

### Code

- All of the code was written by the author using the django documentation and open source examples
- I used Tailwind CSS https://github.com/mertJF/tailblocks to speed up the process of developing 
templates and maintaining a similar style on the site with clean design
- During the development, part of the original templates and snippets were modified
- The profile, bag and checkout apps were recycled from the Code Institute lessons but modified 
to fit with the project purpose https://www.youtube.com/watch?v=zu2PBUHMEew&ab_channel=JustDjango 
with this tutorial I was able to get a better idea of how to build a membership model using stripe api
- Sources of information, inspiration and to sort problems are Stack Overflow and W3Schools

### Content

- Product text and photos were taken from Holland and Barrett **https://www.hollandandbarrett.com/**
- I used lorem ipsum for the blog entries for this project
- The rest of the text was created by me

### Media

- All the images and illustrations for this app were taken from 
Unsplash (https://unsplash.com/) and Freepik (https://www.freepik.com/home)
- The Vimeo video is owned by me

### Acknowledgements

I got the idea of a fitness subscription app from the Code Institute and was 
subsequently inspired by the Classpass website (https://classpass.com/).
 
Thank you to the tutoring team for their support and my mentor Rohit.

Thanks to my partner Kathy Lee for her huge support throughout the entire course.


### Disclaimer

This project is for educational purposes only.

<div align="right">
    <b><a href="#table-of-contents">↥ Back To Top</a></b>
</div>
