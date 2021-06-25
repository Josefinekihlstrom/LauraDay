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
    - Shopping bag page
    - Checkout page
    - Checkout success page
    - Profile page
    - Sign up page
    - Log in page
    - Log out page
    - Error pages

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
- Unnecessary semicolons.
- 'template literal syntax' is only available in ES6 (use 'esversion: 6').
	- Solved by adding the the following line at the top of the affected JavaScript files: ``//jshint esversion: 6``.
- 'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
    - Solved by adding the the following line at the top of the affected JavaScript files: ``//jshint esversion: 6``.
 
### PEP8


## Manual Testing
All pages
Home page
Products page
Product details page
Add product page
Blog page
Blog post details page
Add post page
Delete post page
Shopping bag page
Checkout page
Checkout success page
Profile page
Sign up page
Log in page
Log out page
Error pages

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
6. Circle image on index page not showing after adding it to S3. Not solved
7. Pagination not working correctly. Added an if statement for next and previous button. But the buttons would only link to 
the ceramics pages, no matter which category you where on. I solved it by adding the if statement within the 
href="".
8. When on the products page, the number of products shown only display the products that are shown on the current
page instead of the total of the products if the product page has more pages. Not fixed.
9. If the category field is left out empty when a superuser is adding a product to the site, the product 
will only be visible on the 'All Product' page. This can cause confusion for those who visit the website 
and are looking for a specific product that should be included in the belonging category. In this case, 
the user may think that the product does not exist and do not think about checking the 'All products' page where
the product is actually displayed. This bug remains unsolved for now.

### Bugs found during testing of the site