## Testing

### Django Testing

I attempted to do some local testing on the files test.py for some of the views, models, 
urls and forms. However, there are some views and models that I could not test due to their 
complexity and the limited time I had to apply them. 

### Manual Testing

This app has been manually tested extensively during the development process. When bugs and 
errors were found I have either fixed them or noted them for later review.
Each time I introduced a new feature, changed something or fixed a bug, I have attempted to 
break the app when possible.

As this is my first Django app developed by me, a number of issues were significant during the 
development process and required me to use mainly Stack Overflow to help me find solutions. 
Examples: getting urls paths right, generating a system for the user to login with password, 
errors implementing jinja templates with my python code, as well as several errors during the 
implementation of Subscription model with stripe api.

Extensive testing was required, and accessing pages from different starting points, registered 
and unregistered.
I also tested mobile responsiveness in Chrome Dev Tools and on my iPhone and iPad.

### Tests Performed

#### Navigation
- Regardless of what the user attempts to do, there's never the need to click the 'back' 
button to return to a page. Clicking either a button or a menu item would bring the user to their 
required spot in the app.
- The “Home” button and logo redirects successfully to the main homepage.
- The “Shop” page successfully displays all products from the database and can be seen by all users.
- The “Blog” page displays all blogs added from the database correctly. This also has a small navigation 
to get to display a list of blogs added by admins, lists of authors of the blogs and a section to comment 
on each blog for users that are logged in. 
- The “Pro Members” page correctly displays all information about the two courses. Clicking on either one of 
the courses redirects correctly to the course detail page where users can then select a video to view. Users 
with permissions can access the full video and watch it by simply clicking on the selected video. If a user is 
not logged in, the page will redirect the user to sign in before they can access the video.
        - Note: There is a slight error showing here in some cases. I will more extensively explain this in the 
        Known Issues list.
- Under each video on the course details page, there is call to action for users to subscribe - the button 
says “Pro subscription”. When clicked, this button redirects to the subscription page which gives two 
options, a Basic free plan or a Pro plan; selecting one and clicking “enroll” successfully redirects the 
user to the payment card method connected to Stripe api. 
        - Note: I didn't have enough time to successfully integrate the Stripe subscription 
        model after logging errors relative to authentication - I will explain this further in Known Issues.
- The “My account” button, when clicked, offers dropdown menu options for regular registered users who are 
logged in, showing “my profile” and “logout” options. When clicked, each button successfully redirects to the correct page, displaying information about the user or the option to sign out of their account, followed by messaging indicating successful action.
        - For admin users there is another option of ‘Product management’. When clicked, the admin 
        is redirected to a form where products can be added to the database.
        - For non-logged in users, they will see options to either register or login. 
        Clicking on “login” redirects to a from to enter their registered username and password. After successful login, the user is redirected to the home page where a message displays, indicating the successful login.
        - For non-registered users, they will also see options to either register or login. 
        Clicking on “register” redirects to a registration form where the user can enter personal 
        details to create an account. Message alert displays correctly when a user is created and then 
        redirects to account verification instructions. An email is sent successfully to the new user’s 
        email with a link and instructions on how to verify. When followed, the link redirects to 
        a “confirm” button; when this is clicked, an alert message indicates the successful verification 
        and redirects to the login page. Aa above, after a successful login here, the user is redirected 
        to the home page where a message displays, indicating the successful login.
- The ‘bag’ button, when clicked, redirects successfully to the user's bag, indicating either that it is empty 
or displaying a list of products selected by the user. This can be accessed and used by any user whether they 
are registered or not. When products are in the bag, there are options to keep shopping or securely checkout. 
Clicking “keep shopping” successfully redirects to the Shop home page. Clicking “secure checkout” redirects 
to the checkout page.

#### Application Features

Forms

- Forms are clear and explain what to do with them. When filling the forms, dropdown menus 
work properly. When trying to submit the forms without required fields it won’t allow it - it will 
indicate to fill in the required fields.
- Adding products: this only appears on the navbar when the admin user is logged in. After filling out 
all the required fields on the “Add product” form, the user is redirected to the “Shop” page, where 
the newly-added product will be displayed.
- If an admin user is logged in, each product shows two buttons - “edit” and “delete”. Clicking delete 
instantly deletes the product. Clicking on edit redirects to a form to edit the product; when this form 
is filled out, clicking on “update the products” will successfully make the changes and the user is redirected 
to the “Shop” page, where the newly-edited product will be displayed.

Messages

- When performing specific actions I successfully got alert messages with the correct feedback.

Product Categories

- On the “Shop” page, clicking on a category shows a list of products in that specific category. 
“Sort by” also performs sorting correctly (price, name, rating or category).

Reviews

- Under each product, the review form and section is displayed correctly. Login is required 
to leave a review. When the user is logged in, a form can be filled out with the review text, 
a title and a star rating. When submitted, the review successfully appears on the left-hand side 
under each product listing, showing the user’s review and the star rating.
 
Blog Comments

- Logged-in users can leave comments by clicking on “add comment”. If not logged in, the site 
will indicate that the user must log in first, providing a link to do so. Clicking “add comment” 
redirects correctly to a page with a text area to enter the desired comment. Then, by clicking the 
“add” button, the comment is successfully added and can be viewed publicly under each blog entry.

My Account

- The “My Account” page correctly shows the user’s order history and payment history, as well 
as the option for the user to update their default delivery information. When the form is correctly 
submitted, navigating to the page again will show the updated, saved information.

Registering an Account

- The “Sign up” page can be accessed by clicking on “My Account” when logged out, and selecting “Register” 
from the dropdown menu. On the “Sign up” page, a user is instructed to add their email address (twice), 
a username and a password (again, twice). If the username is already registered, an error message 
will show after form submission - “A user with that username already exists”. The password will not 
be accepted if it is shorter than 8 digits, contains only letters (a number or symbol is also required) 
or contains the username. If the form is successfully submitted, the user will be issued a message alert 
and then redirected to account verification instructions. An email will be sent to the new user’s email 
with a link and instructions on how to verify. When followed, the link redirects to a “confirm” button; 
when this is clicked, an alert message indicates the successful verification and redirects to the 
login page. After successfully logging in using the new credentials, the user is redirected to the 
home page where a message displays to indicate the successful login.

Logging In

- The “Login” page can be accessed by clicking on “My Account” when logged out, and selecting “Login” 
from the dropdown menu. Entering a registered username and password will result in a successful log in. 
The user will be redirected to the home page where a message displays to indicate the successful login.

Resetting a User Password

- To reset a user password, the user must access the “Login” page by clicking on “My Account” when 
logged out, and selecting “Login” from the dropdown menu. Clicking on the “Forgot password?” button 
will redirect to the “Password reset” page. From here, the user can enter their email address to 
receive a link to reset their password, as well as a reminder of their username. The user also has 
the option to navigate back to the “Login” page from this screen, if desired. Clicking on the link 
in the email will bring the user to the “Change Password” page, where the user can enter a new password 
twice, for verification purposes. After successful form submission, the user will be alerted that their 
password has been changed on the landing page, as well as through a message alert. The user can then 
navigate to the “Login” page via the navbar, to log in using the new password.

Bag 

- A user’s shopping bag can be accessed directly via the navbar. This can be accessed and used 
by any user whether they are registered or not. When products are in the bag, there are options 
to keep shopping or securely checkout. Clicking “keep shopping” successfully redirects to the Shop 
home page. Clicking “secure checkout” redirects to the checkout page.
The checkout page displays a form for the user to enter their personal details for delivery and billing. 
It also displays the stripe card payment form to enter card details. 
On the checkout page, there is also an option to adjust the bag, which when clicked redirects to the bag, 
where the quantity of products can be modified or items can be removed.

Checkout

- To successfully check out with the desired items in a user’s shopping bag, the user must fill 
in their personal details for delivery, billing and payment. 
Users must enter their full name, email address, phone number, street address, town or city and country. 
There is also the option to add a second line for street address, a postcode and a county.
For the credit card information, in this testing mode, users can add 4242424242424242, any cvv any 
date in the future and any ZIP code.
When all forms are filled correctly, clicking on “complete order” issues the payment. After payment 
is successful, an alert message shows the success and redirects the user to an order summary of item(s) purchased.
The user will then receive an email to their provided email address with infmroation about their order.
If the payment does not go through, the user will receive a message that the card was not accepted.


#### Known Issues

1. **Image Uploads:** I had an issue with uploading new images after the project has been deployed. 
        - Temporary solution: I used a suggested solution found online where I use the root url from 
        AWS S3 of the image. This correctly displays the image on the deployed app on heroku.
        - Ideally, later I would like to properly configure AWS on settings.py to be able to collectstatic 
        and update with new media added.
2. **Stripe Subscription Model:** I had several issues implementing this, I successfully wrote the models, views 
and admin to manage a video course area, where permission can be given to users to have access or not to courses. 
Due to a lack of time, I was having a problem with authentication - when the user made the payment for the course 
it was not authenticating the user properly and showed an error - “user has no subscription”. I followed the Stripe 
documentation to try and fix this but ran out of time.
        - Temporary solution: Seems like any user that registers on the page can access the video courses, this can 
        be managed on the stripe dashboard with a ‘free trial’ option. 
        I would like to finish integrating this feature properly to fulfill my idea that a user can purchase a 
        monthly subscription in order to access video courses on the site. I would also like to add an option to 
        update or cancel a subscription. For now, I encourage the users on the site to contact an admin to cancel 
        their subscription if necessary.
3. **New User Error:** An error is appearing sometimes relative to authentication and cached cookies I believe - when 
registering a new user and then trying to login on the same tab, an error will appear, saying that the user has no 
subscription; this is related to the Stripe api conflicting. I attempted to fix this by removing the required 
permissions needed to access some part of the Pro Courses section, which seemed to fix the issue. If this issue 
appears, it can be worked around by either refreshing the page to try again, or by using an incognito tab to log in. 
4. **404 Error Page:** This page is required for instances when a user visits an unavailable page. Due to lack of time, 
I added this page but wasn't able to test and implement properly.

#### Web testing

The devices the application was tested on were:

- Mobile: Galaxy S5, Pixel 2, Pixel 2 XL, iPhone 4, iPhone 5 SE, iPhone 6, 7 and 8, 
iPhone 6, 7 and 8 Plus (real device), iPhone X

- Tablet: iPad, iPad Pro

- Laptop: Macbook Pro

For the web testing I used Chrome dev tools and Safari web tools to find bugs, errors and test 
new styles for HTML, CSS and JavaScript.

#### Code Validation

- I used the W3C HTML Validator tool to validate my HTML code.
The validator doesn’t recognise the Django templates. No other errors found.
- I used the W3C CSS Validator tool to validate my CSS code.
The validator doesn’t recognise some of the classes from tailwindcss.com, marking them as errors.
- I used the Esprima Syntax Validator tool to validate my JavaScript syntax.
- I used the Pep8 Online tool to validate my Python syntax.
Some lines are long; for now, this doesn’t affect functionality.


### Testing Conclusion

The testing of the site was extensive. As described in detail above, I worked through all of 
these features to ensure all are working well. All actions performed by the add, edit, read and 
delete functionality are successfully reflected on both the front-end and the back-end on the database 
and Django Admin.

For the functionality just mentioned, I didn’t encounter any bugs. I also got a second person to test the 
same features mentioned above and no bugs were found apart from the ones mentioned in the Known Issues list.










