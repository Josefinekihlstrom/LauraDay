# Laura Day
## Content
About
UX
Features
Technologies Used
Testing
Deployment
Cloning This Project
Credits
Acknowledgements
Disclaimer

## About
IAmResponsive Image here.

Laura Day is an online webshop that offers artwork and ceramics by the fictional brand Laura Day. 
The webshop also has a blog page where the team behind the brand adds blog posts for the visitor to 
read more about the work behind the brand. 

Link to live website [here](https://lauraday-josefinekihlstrom.herokuapp.com).

## UX
### UX goals
The UX goals for this website are the following:

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
The color scale would be in earthy tones to reflect the materials used in the products sold on the website.
The overall goal for the page was to make it clear to the user what the page is about, with easy navigation to
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
### All pages features:
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
    - Sign Up - **(If the user is not logged in)* Links to a page where the user can sign up.
    - Log In - **(If the user is not logged in)* Links to a page where the user can log in.
    - My Profile - **(If the user is logged in)* Links to the Profile page of the logged in user.
    - Log Out - **(If the user is logged in)* Links to a page where the user can log out.
    - Product Management - **(If a superuser is logged in)* Links to the 'Add a Product' page.
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
<br>

The second row contains the following:
- Logo name
- Copyright text

### Home page features:
### Shop page:
### Product details page:
### Blog page:
### Contact page:
### Shopping bag page:
### Profile page:
### Error pages:

More pages here...

## Features left to implement
- Defensive programming when deleting a product from shopping bag.
- Back to top button in bag.html and product.html when many products.
- A timer to the toast messages that automatically closes the message after a certain time.
So the user don't have to click on the 'X' to close it.

## Information Architecture
### The Database
Database values here with image.

### Data Models

## Technologies used
### Languages
- 
- 
- 

### Libraries
- 
- 
- 

### Other
- Figma
- Coolors
- Google Fonts
- 
- 
- 
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

## Cloning this project
1.
2.
3.

## Deployment
1. 
2. 
3. 

## Credits
### Media

## Achknowledgements
### Pages used to find information
- 
- 
- 

### Code
- This project was made with guidance from course videos of Boutique Ado Project - Code Institute
- Allauth setup code in lauraday/settings.py from (Django Allauth)[https://django-allauth.readthedocs.io/en/latest/installation.html]
- Pagination with the help from (Youtube)[https://www.youtube.com/watch?v=5FKL_voZuFw] and (Django docs)[https://docs.djangoproject.com/en/3.2/topics/pagination/]
- Blog application with the help from (Django docs)[https://djangocentral.com/building-a-blog-application-with-django/]
- 

### Thank you
- 
- 
- 
- To my pet bunny Bo for all your supporting cuddles throughout my Code Institute journey. I miss you, rest in peace.

## Disclaimer
This project was made as the fourth and last Milestone Project in the Full Stack Web Development Program at Code Institute. 
This website was created for educational use only. 

