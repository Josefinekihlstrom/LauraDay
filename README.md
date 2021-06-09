# Laura Day
## Content
- About
- UX
- Features
- Information Architecture
- Technologies Used
- Testing
- Deployment
- Cloning This Project
- Credits
- Acknowledgements
- Disclaimer

## About
<div align="center">
    <img src="/readme_images/responsive.jpg" alt="I am responsive image" width="600px">
    <br>
</div>

Laura Day is an online webshop that offers artwork and ceramics by the fictional brand Laura Day. 
The webshop also has a blog page where the team behind the brand adds blog posts for the visitor to 
read more about the work behind the brand. 

Link to live website [here](https://lauraday-josefinekihlstrom.herokuapp.com).

## UX
### UX goals
The UX goals for this website are the following:
- Simple design with a fixed navigation bar at the top for easy navigation.
- Clear sections of the different content of each page.
- The site is responsive to all devices.
- All text on the site is easy to read without any distracting backgrounds.


### User Stories
The user stories were defined during the **Stragety** Plane phase of this project.
As a user I want to:
- Buy handmade ceramics and artwork.
- Get to know the persons behind the brand.
- Be able to read more about what's going on and what's new within the brand.
- Be able to make safe purchases on the site.
- Be able to navigate easy on the site.
- Be able to view the products by category.
- Be able to view a more detailed page about each product on the site.
- Be able to search for a certain product.
- Be able to register for an account.
- Be able to view my order history.
- Get feedback while browsing the website, for example with pop ups when a product is added in the shopping bag.

### Owner goals
As the owner of the page I want:
- To make a website with an aesthetic appeal that reflects the brand.
- To make it easy for the visitor to navigate through the site with a clear navigation menu and buttons that clearly
displays the action behind it.
- To be able to add, edit and/or delete a product.
- To be able to add, edit and/or delete a blog post.

## Design process
The design of the website was based upon how I wanted the data to be displayed. You can read more about the
database that was used [here](#information-architecture).
<br>
<br>
My vision for the site was to create a place where the visitor should feel welcome and inspired.
The color scheme would be in earthy tones to reflect the materials used in the products sold on the website.
The overall goal for the site was to make it clear to the user what the page is about, with easy navigation to
lead the visitor in the right direction according to the visitor's needs.

### Color scheme
<div align="center">
    <img src="/readme_images/coolors.jpg" alt="color scheme" width="600px">
    <br>
</div>

- Beige: **#D6C5AB**
- Light Green: **#82906c**
- Dark Green: **#4a513d**
- Rusty Orange: **#9e532e**
- Dark Brown: **#261c15**

### Fonts
- Font used for Laura Day brand name: [Reenie Beenie](https://fonts.google.com/specimen/Reenie+Beanie?query=reenie+)
- Font used for overall text: [Open Sans](https://fonts.google.com/specimen/Open+Sans?query=open+sans)

### Wireframes
Skeleton and surface plane.
Figma images.

## Features
### All pages
#### Navigation Bar
The navigation bar is featured on the top of all pages of the website. It contains the following:
- **Logo** - Links to the home/index page.
- **Shop** - When clicked on a dropdown list appear with the following links: 
    - All Products
    - Ceramics
    - Artwork.
- **Blog** - Linked to the blog page.
- **Search** - When clicked on a search box appears under the navigation bar.
- **My Account** - When clicked on a dropdown list appear. The full list of the links in the dropdown list is the following:
    - Sign Up - *(If the user is not logged in)* Links to a page where the user can sign up.
    - Log In - *(If the user is not logged in)* Links to a page where the user can log in.
    - My Profile - **(If the user is logged in)* Links to the Profile page of the logged in user.
    - Log Out - *(If the user is logged in)* Links to a page where the user can log out.
    - Product Management - *(If a superuser is logged in)* Links to the 'Add a Product' page.
- **Shopping Bag** - Links to the 'Shopping Bag' page.

#### Footer
The footer is featured at the bottom of all pages. It's divided into two rows.
The first row is divided into three sections that contains the following:
- A section with a heading text of 'Payments' followed by a Visa icon and a Mastercard icon.
- A section with a heading text of 'Links' Followed by the following links:
    - Shop - Linked to the 'All Products' page.
    - Blog - Linked to the blog page.
-  A section with a heading text of 'Social' followed by the following icons:
    - Instagram - Links to instagram.com
    - Facebook - Links to facebook.com
    - LinkedIn - Links to linkedin.com
<br>

The second row contains the following:
- Logo name
- Copyright text

### Home page
The home page includes:
- An orange banner just under the navigation bar with a text about a free shipping deal.
- A hero image with the logo text and a 'Shop' button centered on top of it.
- A row divided into two sections. The left section consists of a round image and the right section consists of text about the brand and a button that links to the blog page.
- A row divided into three sections. Each section consists of an icon that reflects the text that follows.

### Products page
The product page contains the following:
- An orange banner just under the navigation bar with a text about a free shipping deal.
- A heading text of 'Products'
- A small text of the chosen category *(If the user is visiting the 'Ceramics' or 'Artwork' pages)*.
- 'All Products' link.
- 'Number of products shown'.
- A section with all products including:
    - Image of each product.
    - Heading text with the name of the product.
    - Price of the product.
    - Product category.
    - Edit and Remove links *(If the user is a logged-in superuser)*.
- A section with pagination.

### Product details page
The product detail page contains the following:
- Product image.
- Heading text with the name of the product.
- Price of the product.
- Product category.
- Edit and Remove links *(If the user is a logged-in superuser)*.
- A text describing the product.
- Quantity selector.
- A button with the text of 'Products' that links to the 'All products' page.
- A button with the text of 'Add To Bag' that adds the product and the chosen quantity of it to the shopping bag.

### Blog page
The blog page contains the following:
- A section with all blog posts including:
    - A heading text of each blog post.
    - The name of the author that wrote the blog post.
    - The date that the blog post was published.
    - The content of the blog post limited to 200 letters.
    - A button with the text of 'Read More' that links to the blog post details page.
- A section with a round image, text that describes the purpose of the page and icons that links to instagram
and facebook.
- If the user is logged-in as a superuser, there is also a button under the social links that links to the 'Add Post' page.

### Blog post details page
The blog post details page contains the following:
- A section with the blog post details including:
    - A heading text of each blog post.
    - The name of the author that wrote the blog post.
    - The date that the blog post was published.
    - The content of the blog post.
    - A button with the text of 'Back to all posts' that links to blog page.
- A section with a round image, text that describes the purpose of the page and icons that links to instagram
and facebook.

### Add post page

### Shopping bag page
The shopping bag page contains the following:
- An orange banner just under the navigation bar with a text about a free shipping deal.
- A heading text of 'Shopping Bag'.
- If the shopping bag is empty:
    - A text that tells the user that the bag is empty.
    - A button with the text of 'Keep Shopping' that links to the all products page.
- If the shopping bag has products in it:
    - A list with all products added to the shopping bag including:
        - Product image.
        - Name of the product.
        - The SKU number.
        - The product price.
        - The product quantity.
        - Subtotal.
        - Update and Remove links *(Only if the logged-in user is a superuser)*.
    - Bag total.
    - Delivery cost.
    - Grand total.
    - A button with the text of 'Keep Shopping' that links to the all Products page.
    - A button with the text of 'Checkout' that links to the checkout page.

### Checkout page
The checkout page contains the following:
- A heading text of 'Checkout'.
- A section with a form for the user to fill in the shipping and card details.
- A section with a order summary including:
    - Qty of total items in the bag.
    - Product images.
    - Name of the products.
    - Quantity of the products.
    - Subtotal of the products.
    - Order total.
    - Delivery cost.
    - Grand total.
- A button with the text of 'Adjust Bag' that links to the shopping bag page.
- A button with the text of 'Complete Order' that processes the order and redirects the user to the checkout success page.

### Checkout Success page
The checkout success page contains the following:
- A heading text of 'Thank You!'
- A summary of the order including the following:
    - Order info with the order number and date.
    - Order details with the name of the products, quantity and price of them each.
    - Delivery address.
    - Billing info including order total, delivery cost and grand total.
- A button with the text of 'Back To Products' that links to the all products page.

### Profile page
The profile page contains the following:
- A heading text of 'My Profile'.
- Delivery information section including a form the user can fill in with their delivery information.
- Update button that updates the form.
- Order history section that shows all orders made by the logged-in user including:
    - Order number.
    - Date that the order was made.
    - Product names.
    - Order total.

### Sign up page
The sign up page contains the following:
- A heading text of 'Sign Up'.
- A text that prompts the user to log in if they already have an account, followed by a link that links to the log in page.
- A sign up form.
- A button with the text of 'Sign Up' that redirects the user to a page that tells the user to confirm their account.

### Log in page
The log in page contains the following:
- A heading text of 'Log In'
- A text that prompts the user to create an account if they do not already have one, followed by a link that links to the sign up page.
- A log in form
- A remember me checkbox.
- A button with the text of 'Sign In' that redirects the user to the home page after being logged-in.
- A link that says 'Forgot Password?' that links the user to a password reset page.

### Log out page
The log out page contains the following:
-  A heading text of 'Sign Out'
- A text that asks the user if they are sure about logging out.
- A button with the text of 'Sign Out' that redirects the user to the home page and removes the session data.

### Error pages

### Pop up messages
To give the user feedback during their visit to the site, a modal will pop up in the upper right corner to indicate
to the user what events are taking place and to confirm the actions taken by the user. The color of the message
represents what kind of message is displayed. There are three types of messages:

#### Info messages
<div align="center">
    <img src="/readme_images/info.jpg" alt="info pop up message" width="600px">
    <br>
</div>

#### Error messages
<div align="center">
    <img src="/readme_images/error.jpg" alt="error pop up message" width="600px">
    <br>
</div>

#### Success messages
<div align="center">
    <img src="/readme_images/success.jpg" alt="success pop up message" width="600px">
    <br>
</div>


## Features left to implement
- Defensive programming when deleting a product from shopping bag.
- Back to top button in bag.html and product.html when many products.
- A timer to the toast messages that automatically closes the message after a certain time.
So the user don't have to click on the 'X' to close it.
- Messages for when adding, editing and deleting a blog post. Similar to the ones when adding, editing and deleting
a product. For the blog app I focused on learning class based views, and the messages function is a bit different to
implement. Due to lack of time this will be something I will have to add in the future.
- F.A.Q template with a contact form. In my original idea I wanted to add a F.A.Q page with a contact form for the user
to be able to read questions and answears and/or get in touch with the shop owners. However, due to lack of time, this
is something I will have to add in the future.
- Pagination for the blog post page. Due to lack of time I will have to add pagination in the future for the blog page.
The idea was to make it similar to the pagination on the product pages.

## Information Architecture
### The Database
Database values here with image.

### Data Models

## Technologies used
### Languages
- HTML
- CSS
- javascript
- Python

### Libraries
- [JQuery](https://jquery.com/) - Used to write the JavaScript code.
- [Django](https://www.djangoproject.com/) - Python framework.
- [Bootstrap](https://getbootstrap.com/) - Used as the front-end framework.
- [Font Awesome](https://fontawesome.com/) - Icons used on the site.
- [Stripe](https://stripe.com/) - Used as payment method for secure payments.

### Other
- [Git/GitHub](https://github.com/) - Used as remote repository.
- [Gitpod](https://gitpod.io/) - The developer environment used for this project.
- [Heroku]() - Used as hosting platform for the live app.
- [Figma](https://www.figma.com/) - Used to make wireframes.
- [Coolors](https://coolors.co/) - Used to generate the color scheme.
- [Google Fonts](https://fonts.google.com/) - Used for font styles.
- [AWS S3 bucket](https://aws.amazon.com/) - Used as storage for images.

## Testing
Testing.md link here
### Bugs
1. Categories not showing the specific products within a category.
This bug was solved by just simply making the category names into lowercase in the admin panel.
2. Remove link not working on the shoppong bag page. According to the terminal, a slash was missing in the 
javascript function url for the remove function. Solved it by adding a slash at the end of the url.
3. When adding > 1 qty of a product to the shopping bag, the subtotal would show the price of only 1 in qty.
4. When changing the form on the login page to crispy form all inner content covered the entire width of the page. 
I decided to not use the crispy form on the allauth pages, not make bug any bigger. Solved by putting the form
inside a column with the width of halv of the page.
5. Webhook 404 error. Webhook key was not exported correctly to my github variables. Solved by setting the variable
and restarting the workspace.
6. Circle image on index page not showing after adding it to S3. Not solved
7. Pagination not working correctly. Added an if statement for next and previous button. But the buttons would only link to 
the ceramics pages, no matter which category you where on. I solved it by adding the if statement within the 
href="".
8. When on the products page, the number of products shown only display the products that are shown on the current
page instead of the total of the products if the product page has more pages. Not fixed.

## Cloning this project
If you want to work further on my project, go ahead and clone it by following these steps:

1. Go to the top of the [Josefinekihlstrom/LauraDay](https://github.com/Josefinekihlstrom/LauraDay) repository.
2. Click the button named 'Code' next to the green 'Gitpod' button.
3. Choose HTTPS and copy the URL by clicking the icon next to the url.
4. Open Git Bash/Terminal and change the current working directory to the location where you want the cloned directory.
5. Type 'git clone' and then paste the copied URL.
6. Press 'Enter'.
7. To install all the required packages for this project use the following command:
    - ``` pip install -r requirements.txt ```
8. The following environment variables needs to be set up:
```
STRIPE_PUBLIC_KEY = <enter stripe public key here>
STRIPE_SECRET_KEY = <enter stripe secret key here>
STRIPE_WH_SECRET = <enter stripe wh secret key here>
```
9. To create the database you need to migrate the models by typing in the following commands in your terminal:
    - ``` python3 manage.py makemigrations ```
    - ``` python3 manage.py migrate ```
10. To access the django admin panel and database you need to create a superuser account. By typing in the 
following command in your terminal you will be asked to add an email address, username and password.
    - ``` python3 manage.py createsuperuser ```
11. To run the project type in the following command in your terminal:
    - ``` python3 manage.py runserver ```
12. When the site is running you can access the admin panel by adding ``` /admin ``` to the end of the url.
13. Make sure to sign up to the [Stripe](https://stripe.com/), [AWS S3 Bucket](https://aws.amazon.com/s3/) and 
[Gmail](https://gmail.com/) services that where also used for this project.

The information on how to clone a repository came from [GitHub](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository).

## Deployment
1. 
2. 
3. 

## Credits
### Media
- Hero image on home page [Monstera](https://images.pexels.com/photos/5302826/pexels-photo-5302826.jpeg?cs=srgb&dl=pexels-monstera-5302826.jpg&fm=jpg)
- Round image on home page by [Monstera](https://www.pexels.com/sv-se/foto/person-konst-hand-smutsig-5302906/)
- Round image on blog page by [Monstera](https://www.pexels.com/sv-se/foto/kvinna-industri-bord-arbete-5302899/)
- Vase 'Amigo' by [Girl with red hat](https://unsplash.com/photos/z0WVQWnSU2w)
- Bowl 'Franciska' by [Tom Crew](https://unsplash.com/photos/bgIO-u4GEfI)
- Mug 'Lorence' by [Tom Crew](https://unsplash.com/photos/vu0lyZYeseY)
- Bowl 'Francis' by [Tom Crew](https://unsplash.com/photos/YA2E3d7a9Wo)
- Bottle 'Loreen' by [Tom Crew](https://unsplash.com/photos/llGmK6HvOU0)
- Artprint 'Floral' by [Europeana](https://unsplash.com/photos/MvR30qxn-MM)
- Artprint 'Bird Nest' by [Boston Public Library](https://unsplash.com/photos/YoK5pBcSY8s)
- Artprint 'Bird Song' by [Boston Public Library](https://unsplash.com/photos/_f9cP4_unmg)
- Artprint 'Love Birds' by [McGill Library](https://unsplash.com/photos/COphCQKS660)
- Vase 'Lava' by [Girl with red hat](https://unsplash.com/photos/zW8i8h20VDA)
- Pot 'Alex' by [Tom Crew](https://unsplash.com/photos/3uwu5K0RtaE)
- Bottle 'Neya' by [Tom Crew](https://unsplash.com/photos/E64Hv5Ab_nQ)
- Mug 'Leah' by [Tom Crew](https://unsplash.com/photos/_9carLjK19I)

## Achknowledgements
### Pages used to find information
- [Stack overflow](https://stackoverflow.com/)
- [Youtube](https://www.youtube.com/)
- [Django docs](https://docs.djangoproject.com/en/3.2/)
- [Codemy](https://codemy.com/)

### Code
- This project was made with guidance from course videos of Boutique Ado Project - Code Institute
- Allauth setup code in lauraday/settings.py from (Django Allauth)[https://django-allauth.readthedocs.io/en/latest/installation.html]
- Pagination with the help from (Youtube)[https://www.youtube.com/watch?v=5FKL_voZuFw] and (Django docs)[https://docs.djangoproject.com/en/3.2/topics/pagination/]
- Blog application with the help from (Django docs)[https://djangocentral.com/building-a-blog-application-with-django/] and
(Codemy.com)[https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&index=1]
- Add Blog Post with the help from (Codemy.com)[https://www.youtube.com/watch?v=m3efqF9abyg&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&index=4]
- Edit Blog Post with the help from (Codemy.com)[https://www.youtube.com/watch?v=J7xaESAddDQ&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&index=6]
- Delete Blog Post with the help from (Codemy.com)[https://www.youtube.com/watch?v=8NPOwmtupiI&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&index=7]
- Blog comments with the help from (Codemy.com)[https://www.youtube.com/watch?v=hZrlh4qU4eQ&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&index=34]

### Thank you
- 
- 
- 
- To my pet bunny Bo for all your supporting cuddles throughout my Code Institute journey. I miss you, rest in peace.

## Disclaimer
This project was made as the fourth and last Milestone Project in the Full Stack Web Development Program at Code Institute. 
This website was created for educational use only. 

