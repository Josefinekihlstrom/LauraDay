# Testing
## Content
1. User Testing
2. Validator Testing
3. Manual Testing
    - All pages
    - Home page
    - Products page
    - Product details page
    - Add product page
    - Blog page
    - Blog post details page
    - Add post page
    - Delete post page
    - Add Comment page
    - Delete Comment page
    - Shopping bag page
    - Checkout page
    - Checkout success page
    - Profile page
    - Sign up page
    - Log in page
    - Log out page
    - Messages
    - Error pages
    - Other devices
        - Navbar Collapsed
        - Footer Collapsed

4. Bugs Found
    - Bugs found during development
    - Bugs found during testing

## User Testing

1. Buy handmade ceramics and artwork that are high quality.
    - The Laura Day brand focuses on selling high-quality handmade ceramics and printed 
    prints. The focus is on the craft's manufacturing process, which contributes to high 
    quality that lasts for a long time.
    Each art print is produced on a high-quality paper with color that does not fade over 
    time and that keeps a high color finish down to the smallest detail.
    The ceramic is made by working with the clay carefully and for a long time to prevent 
    any air bubbles. By glazing each ceramic product with a high-quality glaze, these 
    crafts also hold up when washed in a dishwasher.
    All products are carefully checked before they are sent and the only thing that can 
    stand out is the handmade results of the production process of each unique product.

2. Get to know the persons behind the brand.
    - On the first page of the website there is a small section with a short description 
    of Laura and her work behind the brand, this to give the visitor a first glimpse of 
    who the brand's creator is and with a short description tell where the inspiration 
    for the products comes from.
    - By adding the blog function on the page, those who visit the website can get a more 
    personal insight into the brand and the people behind it. Super users can log in to 
    the site and access features that make it possible to create, edit and delete blog posts.
    - The posts on the website are mainly about how the work is done in the production 
    of the products, but also presentations of the employees who are involved in the creative process 
    together with Laura.

3. Be able to read more about what's going on and what's new within the brand.
    - See user testing above.

4. Be able to make safe purchases on the site.
    - The website uses a payment function (Stripe) that is authorized and certified and therefore safe 
    to use. The user can therefore feel confident in making purchases as the data with 
    sensitive card details remains encrypted. Source: [Stripe Docs](https://stripe.com/docs/security/stripe)

5. Be able to navigate easy on the site.
    - The site has a fixed navigation bar at the top wich makes it easy to navigate to all pages
    of the site at any time. The footer also contains some navigation links, albeit a few 
    less than the navigation bar to illuminate those pages that have a greater visitor value.

6. Be able to view the products by category.
    - The products kan be viewed all at once or by category. This makes it easier for the 
    user to navigate to the products that are most relevant to their needs.
    - The navigation bar provides links to all the different categories and when the user 
    wants to review another category, he can easily do so by navigating in the fixed 
    navigation bar. 
    If the user is on the product page for a selected category, he can also easily switch 
    to see all products through the link 'All products' which is available just above the 
    top row of products.

7. Be able to view a more detailed page about each product on the site.
    - To be able to see more details about the different products, the user can click 
    on the image for the selected product to be redirected to a page with a more detailed 
    product view.
    - The detailed product view provides the user with a more detailed description of the 
    product, but also with the opportunity to click on the product image to see it in an enlarged 
    format.

8. Be able to search for a certain product.
    - In the navigation bar at the top of each page there is an icon in the shape of a 
    magnifying glass. When the user clicks on it, a search form appears that allows the user 
    to do a text search for all product names and descriptions.

9. Be able to register for an account.
    - The user has the opportunity to register and log in to the page to access detailed 
    order history. By clicking on the user icon on the upper right in the navigation bar, 
    the user gets the options of 'Sign Up' and 'Login'. When the user is logged in, the same icon
    provides new links with the options to view the Profile or Log out of the page.

10. Be able to view my order history.
    - A user who has made an order on the website while being logged in has the opportunity 
    to go to the user profile and see detailed information about previous orders.
    - The user can click on each individual order to see details such as order date, 
    order total, products ordered and shipping address.

11. Get feedback while browsing the website, for example with pop ups when a product is added in the shopping bag.
    - To give the user feedback during their visit to the site, a modal pops up in the 
    upper right corner to indicate what events are taking place and to confirm the actions 
    taken by the user. The color of the message represents what kind of message is displayed.
    These actions can be when the user adds a product to the shopping bag, when the user views
    a past order confirmation or when an error occurs.

## Validator Testing

### HTML
All HTML templates where tested using [W3C Markup Validation Service](https://validator.w3.org/) by direct input of the code.
The validation did not reveal any bigger issues with the code except for some forbidden placements of ``<p>`` tags as child elements and 
missing ``<ul>`` tags.

Errors caused by the Jinja templating where ignored because they were expected to occur. Changing the Jinja in the code
would simply break the site entirely.

### CSS
The CSS was tested by using [Jigsaw CSS Validation Service](https://jigsaw.w3.org/css-validator/) by direct input of the code.
The CSS passed the test without any errors.

### JS Hint
The JavaScript was tested using [JSHint](https://jshint.com/). The warnings that occurred were the following:
- One undefined variable ($)
    - This could not lead to any change of the code, since it would break the jQuery.
- One undefined variable (Stripe)
    - This could not lead to any change of the code, since it would break the Stripe functions.
- Missing semicolons.
    - Added semicolons.
- Unnecessary semicolons.
    - Removed semicolons.
- 'template literal syntax' is only available in ES6 (use 'esversion: 6').
	- Solved by adding the the following line at the top of the affected JavaScript files: ``//jshint esversion: 6``.
- 'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
    - Solved by adding the the following line at the top of the affected JavaScript files: ``//jshint esversion: 6``.
 
### PEP8
The Python code was tested using [PEP8](http://pep8online.com/). The following errors occured:
- Line too long (90 > 79 characters) in urls.py file for the blog application.
    - Solved by simply rearrange the url path.
- Expected 2 blank lines, found 1 in the views.py file for the checkout application.
    - Solved by simply adding blank line.
- Lines too long in the settings.py file for the lauraday application.
    - Line 143, Column 80, line too long (91 > 79 characters). No changes were made to this line of code as this would have caused the code not to work properly.
    - Line 146, Column 80, line too long (81 > 79 characters). No changes were made to this line of code as this would have caused the code not to work properly.
    - Line 149, Column 80, line too long (82 > 79 characters). No changes were made to this line of code as this would have caused the code not to work properly.
    - Line 152, Column 80, line too long (83 > 79 characters). No changes were made to this line of code as this would have caused the code not to work properly.


## Manual Testing
All manual tests were done in the following browsers:

- Firefox
- Google Chrome
- Microsoft Edge


### All pages
#### Navbar
- Click on the Laura Day icon to see that it links to the home page.
- Click on the Shop button to see that the drowdown works and displays the following content:
    - All Products - Click on it to see that it links to the 'All Products' page.
    - Ceramics - Click on it to see that it links to the 'Ceramics' page.
    - Artwork - Click on it to see that it links to the 'Artwork' page.
- Click on the Blog button..:
    - *(If logged in as superuser)* .. to see that the dropdown works and displays the following content:
        - Blog Posts - Click on it to see that it links to the Blog page displaying all blog posts.
        - Add Post - Click on it to see that it links to the 'Add Post' page.
    - *(If not logged in)* .. to see that it links to the Blog page displaying all blog posts.
    - *(If logged in as regular user)* .. to see that it links to the Blog page displaying all blog posts.
- Click on the Search icon to see that the dropdown works displaying the search input and search button.
    - Type in search word 'mug' and click on search icon to see that it links to the product page displaying all products containing the word 'mug' in the product name.
    - Type in search word 'hej' and click on search icon to see that it links to the product page displaying 0 products as no product contains the word 'hej' in the product name or description. **bug noted of pagination not being pushed down to bottom of page. Please see the 'bugs found' section.*
    - Type in search word 'beautiful' and click on the search icon to see that it links to the product page displaying products that contains the word 'beautiful' in the product description.    
- Click on the My Account icon to see that the dropdown works displaying the following content:
    - *(If logged in as superuser)*
        - Product Management - Click on it to see that it links to the 'Add Product' page.
        - My Profile - Click on it to see that it links to the 'Profile' page.
        - Logout - Click on it to see that it links to the 'Log Out' page.
    - *(If not logged in)*
        - Sign Up - Click on it to see that it links to the sign up page.
        - Log In - Click on it to see that it links to the 'Log In' page.
    - *(If logged in as regular user)*
        - My Profile - Click on it to see that it links to the 'Profile' page.
        - Logout - Click on it to see that it links to the 'Log Out' page.
- Click on the Shopping bag icon to see that it links to the 'Bag' page.
    
#### Footer
- Make sure the footer is displaying the following content in the dark green area:
    - Payments section with Visa and Mastercard icons.
    - Links section.
        - Click on the Shop link to see that it links to the 'All Products' page.
        - Click on the Blog link to see that it links to the 'Blog' page displaying all blog posts.
    - Social section.
        - Click on the instagram icon to see that it links to the Instagram page in a new tab.
        - Click on the facebook icon to see that it links to the Facebook page in a new tab.
        - Click on the LinkedIn icon to see that it links to the LinkedIn page in a new tab.
    - Contact section with email and phone number.
- Make sure footer is displaying the following content in the light green area:
    - Laura Day logo.
    - Copyright text.

### Home page
- Make sure the orange banner is displayed and covering the width of the page.
- Make sure the hero image is covering both the width and height of viewport when first arriving to the page.
- Click on 'Shop Collection' button to see that it links to the 'All Products' page. **(Bug noted of Laura Day text and 'Shop Collection' button not being centered correctly. Please see 'bugs found' section)*
- Make sure that the circle image and 'About' text are displayed on the same row.
- Click on the 'Visit Blog' button to see that it links to the 'Blog' page displaying all blog posts.
- Make sure that the three information boxes in the information section are displayed on the same row.

### Products page
The following tests where made on the 'All Products' page, 'Ceramics' page and 'Artwork' page.
- Make sure the orange banner is displayed and covering the width of the page.
- When on the 'Ceramics' products page, make sure that the text of 'Ceramics' appears right under the heading text of 'Products'.
- Make sure that the product counter just above the products is displaying the number of products. *(Bug noted of product counter only showing the products shown on the current page, and not the total amount of products within the current category. Please see 'bugs found' section for more details.)* 
- Make sure that products are shown with a maximum of three on each row and a total of eight on each page. *(Bug noted of products not filling out on last row. Please see 'bugs found' section for more information)*
- Make sure that if a product has no image or broken image url, a default image replaces it instead.
- Click on a product image to see that it links to the 'Product Details' page.
- Click on a products category name to see that it links to the product page of that category.

### Product details page

### Add product page

### Blog page

### Blog post details page

### Add post page

### Delete post page

### Add Comment page

### Delete Comment page

### Shopping bag page

### Checkout page

### Checkout success page

### Profile page

### Sign up page

### Log in page

### Log out page

### Messages

### Error pages
(de sidor som har inbugda error också)

### Other devices
All of the tests mentioned above were also made on the following devices using the developer tool on Google Chrome:

- iPad
- iPad Pro
- iPhone 5/SE
- iPhone 6/7/8
- Galaxy S5

The following things where further tested on smaller devices:

#### Navbar Collapsed (Not on iPad Pro)
- Click on navbar toggler icon to see that the dropdown works displaying:
    - Home - Click on it to see that it links to the 'Home' page.
    - My Account - Click on it to see that the dropdown works displaying..:
        - *(When logged in as superuser)*
            - Product Management - Click on it to see that it links to the 'Add Product' page.
            - My Profile - Click on it to see that it links to the 'Profile' page.
            - Logout - Click on it to see that it links to the 'Log Out' page.
        - *(When not logged in)*
            - Sign Up - Click on it to see that it links to the 'Sign Up' page.
            - Login - Click on it to see that it links to the 'Login' page.
        - *(When logged in as regular user)*
            - My Profile - Click on it to see that it links to the 'Profile' page.
            - Logout - Click on it to see that it links to the 'Log Out' page.
    - Shop - Click on it to see that the dropdown works displaying:
        - All Products - Click on it to see that it links to the 'All Products' page.
        - Ceramics - Click on it to see that it links to the 'Ceramics' page.
        - Artwork - Click on it to see that it links to the 'Artwork' page.
    - Blog - Click on it..:
        - *(If logged in as superuser)* ..to see that the dropdown works displaying:
            - Blog Posts - Click on it to see that it links to the Blog page displaying all blog posts.
            - Add Post - Click on it to see that it links to the 'Add Post' page.
        - *(If not logged in)* to see that it links to the 'Blog' page displaying all blog posts.
        - *(If logged in as regular user)* to see that it links to the 'Blog' page displaying all blog posts.
- Click on the navbar toggler when navbar menu is already showing to see that the navbar menu collapses.
- When navbar menu is showing and not collapsed, click on the Search icon to see that the search input displays right below the navbar menu.

#### Footer (Not on iPad Pro)
- Make sure the dark green area is displaying the different sections below each other and not on the same row.
- Make sure the Payments section is not displayed.

#### Home page
- Make sure that the circle image and 'About' text are displayed on their own row starting with the circle image *(Not on iPad or iPad Pro)*.
- Make sure that the three information boxes in the information section are displayed separately on their own row *(Not on iPad or iPad Pro)*.

## Bugs
### Bugs found during development of the site
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

6. Circle images on index and blog pages not showing at all after adding it to S3. The images was already circle shaped when I added them to the project and therefor in png format. 
However, it seemed like png format was not supported by S3 so therefor I Solved it by simply adding the images in square shape to the project folder and S3 folder and 
added css styling to make them circle.

7. Pagination not working correctly. Added an if statement for next and previous button. But the buttons would only link to 
the ceramics pages, no matter which category you where on. I solved it by adding the if statement within the 
href="".

8. When on the products page, the number of products shown only display the products that are shown on the current
page instead of the total amount of the products within the category. This bug remains unsolved due to lack of time fixing it.

9. If the category field is left out empty when a superuser is adding a product to the site, the product 
will only be visible on the 'All Product' page. This can cause confusion for those who visit the website 
and are looking for a specific product that should be included in the belonging category. In this case, 
the user may think that the product does not exist and do not think about checking the 'All products' page where
the product is actually displayed. This bug remains unsolved for now.

### Bugs found during testing of the site
1. The limit of a product you can add is set to 99 on the product details page, however if you have added 99 pieces of a product to the shopping bag
you can go back to the same product and add even more items so that it exceeds the 99 limit. This is noted as a bug
as the most ideal thing would be to add a limit so that it is not possible to add more items of a product when you have already
added 99 of them. A more realistic feature would be to make it impossible to add more than a certain number of an item than 
what is in stock. This probably requires some coding and may be something to think about adding in the future. The bug remains unsolved.

2. When searching for a word that results in 0 products being shown on the products page that follows, the pagination is not pushed down to the 
page as there is no content filling the page to push it down with. This bug remains unsolved due to lack of time fixing it.

3. When visiting the 'Home' page on an iPhone 5 device, the Laura Day text and 'Shop Collection' button is not centered correctly.
Both the text and the button are displayed slightly to the right which they should not be. Unfortunately due to lack of time, this bug remains unsolved at the moment.

4. Bug noted of products not filling out on the last row when on desktop view or iPad Pro device. This bug could be solved by adding an if statement in the template that makes the products 
fill in all the places on both desktop view and iPad Pro however, the bug remains unsolved due to lack of time fixing it.
<div align="center">
    <img src="/readme_images/bug1.jpg" alt="bug image" width="600px">
    <br>
    <br>
</div>