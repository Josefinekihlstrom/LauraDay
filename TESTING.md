# Testing
## Content
1. [User Testing](#user-testing)
2. [Validator Testing](#validator-testing)
    - [HTML](#html)
    - [CSS](#css)
    - [JS Hint](#js-hint)
    - [PEP8](#pep8)
3. [Manual Testing](#manual-testing)
    - [All pages](#all-pages)
    - [Home page](#home-page)
    - [Products page](#products-page)
    - [Product details page](#product-details-page)
    - [Add product page](#add-product-page)
    - [Blog page](#blog-page)
    - [Blog post details page](#blog-post-details-page)
    - [Add post page](#add-post-page)
    - [Delete post page](#delete-post-page)
    - [Add Comment page](#add-comment-page)
    - [Delete Comment page](#delete-comment-page)
    - [Shopping bag page](#shopping-bag-page)
    - [Checkout page](#checkout-page)
    - [Checkout success page](#checkout-success-page)
    - [Profile page](#profile-page)
    - [Sign up page](#sign-up-page)
    - [Log in page](#log-in-page)
    - [Log out page](#log-out-page)
    - [Messages](#messages)
    - [Error pages](#error-pages)
    - [Different devices](#different-devices)
4. [Bugs](#bugs)
    - [Bugs found during development](#bugs-found-during-development-of-the-site)
    - [Bugs found during testing](#bugs-found-during-testing-of-the-site)

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
- Make sure the orange banner is displayed and covers the width of the page.
- Make sure the hero image is covering both the width and height of viewport when first arriving to the page.
- Click on 'Shop Collection' button to see that it links to the 'All Products' page. **(Bug noted of Laura Day text and 'Shop Collection' button not being centered correctly. Please see 'bugs found' section)*
- Make sure that the circle image and 'About' text are displayed on the same row.
- Click on the 'Visit Blog' button to see that it links to the 'Blog' page displaying all blog posts.
- Make sure that the three information boxes in the information section are displayed on the same row.

### Products page
The following tests where made on the 'All Products' page, 'Ceramics' page and 'Artwork' page.
- Make sure the orange banner is displayed and covering the width of the page.
- When on the 'Ceramics' products page, make sure that the text of 'Ceramics' appears right under the heading text of 'Products'.
- When on the 'Artwork' products page, make sure that the text of 'Artwork' appears right under the heading text of 'Products'.
- Make sure that the product counter just above the products is displaying the number of products. *(Bug noted of product counter only showing the products shown on the current page, and not the total amount of products within the current category. Please see 'bugs found' section for more details.)* 
- Make sure that products are shown with a maximum of three on each row and a total of eight on each page. *(Bug noted of products not filling out on last row. Please see 'bugs found' section for more information)*
- Make sure that if a product has no image or has a broken image url, a default image replaces it instead.
- Click on a product image to see that it links to the 'Product Details' page.
- Click on a products category name to see that it links to the products page of that category.
- *(When logged in as a superuser)*
    - Click on the 'Edit' link to see that it links to the 'Edit Product' page of the chosen product.
        - Make sure toast message is displayed.
    - Click on the 'Remove' link to see that it links back to the 'All Products' page after deleting the chosen product.
        - Make sure toast message is displayed.
- *(When not logged in)*
    - Make sure the user cannot see the edit and remove links.
    - Make sure that the user cannot access the edit page of a product by typing in ``/products/edit/<product sku number>`` at the end of the url.
    Instead, the user gets redirected to the login page.
- *(When logged in as a regular user)*
    - Make sure the user cannot see the edit and delete links.
    - Make sure that the user cannot access the edit page of a product by typing in ``/products/edit/<product sku number>`` at the end of the url.
    Instead, the user gets redirected to the 'Home' page with a toast message displaying a 404 error.
- Make sure the pagination displays ``Page X of X``.
- Make sure the pagination is displaying correct depending on total amount of products:
    - When a category has more than 8 products the user is provided with a next button, a previous button or both next and previous buttons (Depending on the total amount of products there is in the category and/or which page the user is visiting).
    - When a category has less than 8 products no additional buttons are displayed.

### Product details page
- Make sure the orange banner is displayed and covers the width of the page.
- Make sure product image column and product information column are displayed on the same row.
- Click on the product image to see that it links to a new tab displaying the image in larger size.
- Click on the category name to see that it links to the products page displaying all products within that category.
- *(When logged in as a superuser)*
    - Click on the 'Edit' link to see that it links to the 'Edit Product' page of the chosen product.
        - Make sure toast message is displayed
    - Click on the 'Remove' link to see that it links back to the 'All Products' page after deleting the chosen product.
        - Make sure toast message is displayed.
- *(When not logged in)*
    - Make sure the user cannot see the edit and remove links.
    - Make sure that the user cannot access the edit page of a product by typing in ``edit/`` between ``products/`` and ``<product id>/`` in the url.
    Instead, the user gets redirected to the login page.
- *(When logged in as a regular user)*
    - Make sure the user cannot see the edit and delete links.
    - Make sure that the user cannot access the edit page of a product by typing in ``edit/`` between ``products/`` and ``<product id>/`` in the url.
    Instead, the user gets redirected to the 'Home' page with a toast message displaying a 404 error.
- When the product quantity is displayed as ``1``, make sure that the minus button is disabled but the plus button work as intended.
- When the product quantity is displaying a number larger than ``1`` but less than ``99``, make sure that both minus and plus buttons work as intended. 
- When the product quantity is displayed as ``99``, make sure that the plus button is disabled but the minus button work as intended.
- Click on the 'Products' button to see that it links to the 'All Products' page.
- Click on the 'Add To Bag' button after choosing a quantity between ``1`` and ``99`` and the product/products gets added to the shopping bag.
A toast message appears displaying the current content of the shopping bag.
- Manually type in a number larger than ``99`` and click on the 'Add To Bag' button.
    - The quantity of the product will not be added to the shopping bag and the user the user is prompted to select a number between ``1`` and ``99`` instead.
- Manually type in a number less than ``1`` and click on the 'Add To Bag' button.
    - The quantity of the product will not be added to the shopping bag and the user is prompted to select a number larger than ``1``.
- Manually remove the number inside the quantity input and leave it blank, when clicking on the 'Add To Bag' button the user is prompted to 
add a number to the input field before clicking the button.
- Manually add letters to the quantity input field without success until trying to add the letter ``e``. When clicking the 'Add To Bag' button
the user is prompted to add a number to the field instead.
- Click on the 'Add To Bag' button after selecting a quantity and the page reloads with a toast message displaying.

### Add product page
This page is only available for superusers.
- Make sure the form contains of the following fields to fill in:
    - Name 
    - Category 
    - Sku 
    - Description 
    - Price 
    - Price 
    - Image url 
    - Image Upload
- Click on the 'Cancel' button and the user gets redirected to the 'All Products' page.
- Click on the 'Add Product' button without filling out any fields and the user is prompted to fill in the fields.
- Fill out all fields and click on the 'Add Product' button to see that it adds the product and links to the 
'Product Details' page of the added product with a toast message displaying.
- Fill out all fields except the name field and click on the 'Add Product' button and the user is prompted to fill in the name field.
- Fill out all fields except the category field and click on the 'Add Product' button to see that it adds the product and links to the 
'Product Details' page of the added product with a toast message displaying. *(This is noted as a bug in the 'bugs found' section as the product will only be visible on the 'All Products' page)*
- Fill out all fields except the sku field and click on the 'Add Product' button to see that it adds the product and links to the 
'Product Details' page of the added product with a toast message displaying. *(This is noted as a bug in the 'bugs found' section as the sku is important key information to add to the products to keep better track of them.)*
- Fill out all fields except the description field and click on the 'Add Product' button to see that it adds the product and links to the 
'Product Details' page of the added product with a toast message displaying.
- Fill out all fields except the price field and the user is prompted to fill the field out before proceeding.
- Make sure that if no image is uploaded or linked in the image url field when adding a product, a default image will be displayed on the 'Product Details' page.
- Make sure that when a broken image url is added to the image url field when adding a product, a default image will be displayed on the 'Product Details' page.
- *(When not logged in)*
    - Make sure that the user cannot access the 'Add Product' page by typing in ``products/add/`` at the end of the url.
    Instead, the user gets redirected to the login page.
- *(When logged in as a regular user)*
    - Make sure that the user cannot access the 'Add Product' page by typing in ``products/add/`` at the end of the url.
    Instead, a toast message appears displaying a 404 error.

### Blog page
- In the blog posts column:
    - Click on the blog post heading text to see that it links to the 'Post Details' page of the chosen blog post.
    - Click on the blog post body text to see that it links to the 'Post Details' page of the chosen blog post.
    - *(When logged in as superuser)* Click on the 'Edit' link to see that it links to the 'Edit Post' page of the chosen blog post.
    - *(When logged in as superuser)* Click on the 'Remove' link too see that it links to the 'Delete Post' page displaying the chosen blog post to delete.
    - *(When not logged in or logged in as a regular user)* Make sure the Edit and Remove links are not displayed.
    - Make sure the number of comments are displayed in the down right of each blog post.
- In the sidebar column:
    - *(When logged in as superuser)* Click on the 'Add Post' button to see that it links to the 'Add Post' page.
    - *(When not logged in or logged in as a regular user)* Make sure the 'Add Post' button is not displayed.
    - Click on the Instagram icon to see that it links to the Instagram page in a new tab.
    - Click on the Facebook icon to see that it links to the Facebook page in a new tab.

### Blog post details page
- Click on the 'Blog Posts' button to see that it links to the 'Blog Posts' page.
- In the post details column:
    - *(When logged in as superuser)* Click on the 'Edit' link to see that it links to the 'Edit Post' page of the chosen blog post.
    - *(When logged in as superuser)* Click on the 'Remove' link too see that it links to the 'Delete Post' page displaying the chosen blog post to delete.
    - *(When not logged in or logged in as a regular user)* Make sure the Edit and Remove links are not displayed.
- In the sidebar column:
    - Click on the Instagram icon to see that it links to the Instagram page in a new tab.
    - Click on the Facebook icon to see that it links to the Facebook page in a new tab.
- In the comments section:
    - Make sure the number of comments are displayed.
    - If a blog post has no comments, make sure the text of "No comments yet.. Be the first and add a comment!" is displayed.
        - Click on the 'add a comment' link to see that it links to the 'Add Comment' page of the chosen blog post.
    - *(When logged in as superuser)* Click on the red dust-bin icon next to the commenters name to see that it links to the 'Delete Comment' page displaying the chosen comment to delete.
    - *(When not logged in or logged in as a regular user)* Make sure the red dust-bin icon is not displayed.
    - Click on the 'Blog Posts' button to see that it links to the 'Blog Posts' page.
    - Click on the 'Comment' button to see that it links to the 'Add Comment' page of the chosen blog post.

### Add post page
This page is only available for superusers.
- Make sure the form contains of the following fields to fill in:
    - Title
    - Slug
    - Author 
    - Content 
    - Status
- Click on the 'Cancel' button to see that it links to the 'Blog Posts' page.
- Fill in all the fields and click on the 'Add Post' button to see that it adds the blog post and links to the 
'Post Details' page of the added blog post.
- Fill in all the fields except the Title field and click on the 'Add Post' button and the user is prompted to fill in the missing field.
- Fill in all the fields except the slug field and click on the 'Add Post' button and the user is prompted to fill in the missing field.
- Fill in all the fields except the author field and click on the 'Add Post' button and the user is prompted to fill in the missing field.
- Fill in all fields except the content field and click on the 'Add Post' button and the user is prompted to fill in the missing field.
- Fill in all fields but put the status on 'Draft' and click the 'Add Post' button to see that it adds the blog post and links to the 'Post Details' 
page of the added blog post. However when the user goes back to the 'Blog Posts' page, the added post will not be shown. *(This is noted as a bug. Please see the 'bugs found' section for more details.)*
- *(When not logged in)* Make sure the user can't get access to the 'Add Post' page
by typing in ``/blog/add_post`` at the end of the url. Instead the page will show a 404 error.
- *(When logged in as a regular user)* Make sure the user can't get access to the 'Add Post' page
by typing in ``/blog/add_post`` at the end of the url. Instead the page will show a 404 error.

### Delete post page
- Make sure the page displays the name of the blog post that is about to be deleted.
- Click on the 'Cancel' button to see that it links to the 'Blog Posts' page.
- Click on the 'Delete Post' button to delete the post and see that it links to the 'Blog Posts' page. The deleted post is
no longer on the 'Blog Posts' page.
- *(When not logged in or logged in as a regular user)* Type in ``/blog/delete_post/<blog post name here>`` and the user
is redirected to a 404 error page.

### Add Comment page
- Make sure the form contains of the following fields to fill in:
    - Name
    - Body
- Click on the 'Cancel' button to see that it links to the 'Blog Posts' page.
- Fill in all fields in the form and click on the 'Add Comment' button to see that it links to the 'Post Details' page
of the post that was just commented on with the comment now displayed.
- Click on the 'Add Comment' button without filling any field in and the user is prompted to fill in the fields.
- Fill in the body field and not the name field and click on the 'Add Comment' button, the user is prompted to fill in the empty field.
- Fill in the name field and not the body field and click on the 'Add Comment' button, the user is prompted to fill in the empty field.

### Delete Comment page
- Make sure the page displays the body of the comment that is about to be deleted.
- Click on the 'Cancel' button to see that it links to the 'Blog Posts' page.
- Click on the 'Delete Comment' button to delete the comment and see that it links to the 'Blog Posts' page. The deleted comment is
no longer on the 'Post Details' page.
- *(When not logged in or logged in as a regular user)* Type in ``/blog/delete_comment/<comment id here>`` and the user
is redirected to a 404 error page.

### Shopping bag page
- Make sure the orange banner is displayed and covers the width of the page.
- Make sure the shopping bag page displays the following sections for every product that was added:
    - Product image
    - Product name 
    - Sku number 
    - Price 
    - Quantity
    - Subtotal 
- Make sure the quantity section contains a quantity form with an update link and remove link.
- Make sure if the product has no image or a broken image url, a default image replaces it instead.
- Change the quantity of a product and click on 'Update' link to see that the page reloads, now with the added quantity of the product, with a toast message displaying. *(Bug noted of minus and plus buttons not working correct when on desktop view. Please see bugs found section for more details.)*
- Click on the 'Remove' link to see that the page reloads, now with the removed product gone from the shopping bag page with a toast message displaying.
- Remove all product from the shopping bag and the page reloads and displays a text telling the user that the shopping bag is empty. Click on the 'Keep Shopping' button to see that it links to the 'All Products' page.
- Make sure the bag total displays the total amount of all products added to the shopping bag.
- Make sure the delivery cost is displayed.
    - When the user has enough goods in excess of the sum of $ 50, the cost of shipping becomes $ 0.
    - When the user does not have enough goods in excess of the sum of $ 50, the cost of shipping becomes 10% of the bag total sum.
        - A red text is displayed under the grand total, encouraging the user to get free delivery by adding more products to the shopping bag.
- Make sure the grand total is displaying the total amount of the bag total and delivery cost combined.
- Click on the 'Keep Shopping' button to see that it links to the 'All Products' page.
- Click on the 'Checkout' button to see that it links to the 'Checkout' page.

### Checkout page
- Make sure the following sections are displayed correct:
    - Details form with the following fields to fill in:
        - Full Name
        - Email Address
    - Delivery form with the following fields to fill in:
        - Phone Number
        - Street Address 1
        - Street Address 2
        - Town or City
        - County
        - Postal Code
        - Country
    - Payment form.
- *(When the user is not logged in)* Click on 'Create an account' link below the delivery section to see that it links to the 'Sign Up' page.
- *(When the user is not logged in)* Click on the 'login' link below the delivery section to see that it links to the 'Login' page.
- *(When the user is logged in)* Make sure the presaved information is displayed in the details form and delivery form.
- Click on the 'Adjust Bag' button to see that it links to the 'Shopping Bag' page.
- Click on the 'Complete Order' button when required fields are left out to see that the user is prompted to fill in the fields.
- Make sure the red text under the 'Adjust Bag' button and 'Complete Order' button displays the total amount that the user will be charged if proceeding.
- Type in the card details for Stripe test card and click on the 'Complete Order' button to see that the loading overlay displays and then redirects the user to the 'Checkout Success' page with a toast message displaying.
    - Stripe test card number: ``4242 4242 4242 4242``
    - Stripe test card MM/YY: ``04/24``
    - Stripe test card CVC: ``242``
    - Stripe test card postal code: ``42424``
- Type in ``/checkout`` at the end of the url when the user has no products in the shopping bag and the page displays a toast message telling the user that the shopping bag is empty.
- Make sure the order summary section displayes the following:
    - Product image
        - If the product has no product image or a broken image link a default image will replace it.
    - Product name
    - Product quantity
    - Subtotal
    - Order total
    - Delivery cost
    - Grand total
- Click on an image in the order summary section to see that it links to the product details page of the chosen product.

### Checkout success page
- Make sure the email used when placing the order is displayed above the order information.
- Make sure the order information section contains the following:
    - Order number
    - Order date
    - Order details
        - Name of the product
        - Quantity
        - Price each
    - Delivery information:
        - Full name
        - Address 1
        - Address 2 *(if it was added to the order)*
        - County
        - Town or City
        - Postal code
        - Country
        - Phone number
    - Billing info:
        - Order total
        - Delivery cost
        - Grand total
- Click on the 'Back to Products' button to see that it links to the 'All Products' page.

### Profile page
- Make sure the name of the user is shown at the top of the profile page.
- Make sure the Delivery Information column and Order History column are displayed on the same row.
- Make sure the Delivery Information column show the following fields:
    - Phone number
    - Street Address 1
    - Street Address 2
    - Town or City 
    - County, State or Locality 
    - Postal Code 
    - Country
- Type in information in any field and click on 'Update' button to reload the page, with the recently added information saved to the field.
A toast message appears.
- Make sure the Order History column displays the following sections (even if no order has been made):
    - Order Number 
    - Date 
    - Items 
    - Order Total 
- If a user has a order history, make sure the information of each order history displays:
    - The Order Number of the order that was made.
    - The date that the order was made.
    - The items that was ordered.
    - The order total.
- If a user has a order history, click on the order number to see that it links to the Checkout Success' page of the order,
with a toast message displaying information that it is a past confirmation.

### Sign up page
- Click on the 'Sign In' link to see that it links to the 'Log In' page.
- Make sure the sign up form displays the following fields:
    - E-mail 
    - E-mail (again)
    - Username 
    - Password 
    - Password (again)
- If any field is left out when clicking the 'Sign Up' button, the user is prompted to fill the empty field out.
- If all fields are filled in click on the 'Sign Up' button to see that the user gets redirected to the 'Confirm E-mail' page with a toast message displaying, prompting the user to check the email address for a confirmation link.
    - Make sure email was sent with a confirmation link.
    - Click on the confirmation link in the e-mail and the user gets redirected to the 'Confirm E-mail' displaying a button with the text of 'Confirm'.
    - Click on the 'Confirm' button and the user is redirected to the 'Log In' page with a toast message displaying that the email is now confirmed.

### Log in page
-  Click on the 'Sign Up' link to see that it links to the 'Sign Up' page.
- Make sure the form is displaying the following:
    - Login 
    - Password
    - Remember me checkbox
- Click on the 'Sign Up' button without filling out the form and the user is prompted to fill out the empty fields.
- Click on the 'Sign Up' button after filling out the form and the user is redirected to the 'Home' page with a toast message 
displaying.
- Click on the 'Forgot Password?' link to see that it links to the 'Password Reset' page.
- Type in ``/accounts/login/`` at the end of the url when a user is already logged in, and the user gets redirected 
to the home page.

### Log out page
- When a user is logged in click on the 'Sign Out' button to see that it logs the user out and redirects back to the 
home page with a toast message displaying.
- Type in ``/accounts/logout/`` at the end of the url when a user has already logged out, and the user gets redirected 
to the home page.

### Messages
shopping bag messages when full or empty

### Error pages
#### 404 Page not found
- Type in ``/hej`` at the end of the url (a path that does not excist) and the user gets an '404 Page Not Found' page.
- Click on the 'Home' button to see that it links to the 'Home' page.

#### 500 Internal Server Error
- In the views.py file inside the products app, remove the last letter from the ``products`` variable in the all_products function. Go to the 
'All Products' page of the site and the user gets an '500 Internal Server Error' page.
- Click on the 'Home' button to see that it links to the 'Home' page.

### Different devices
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
- Make sure that the circle image and 'About' text are displayed on their own row starting with the circle image *(This does not apply on iPad or iPad Pro)*.
- Make sure that the three information boxes in the information section are displayed separately on their own row *(This does not apply on iPad or iPad Pro)*.

#### Products page
- When on an iPad, make sure that products are shown with a maximum of two on each row and a total of eight on each page. *(This does not apply to iPad Pro)*
- When on a phone device, make sure that products are shown with a maximum of one on each row and a total of eight on each page.

#### Product Details page
- Make sure the product image column and product information column are displayed on separate rows starting with the the product image *(This does not apply to iPad Pro)*.

#### Add Product page 
- Make sure the form covers the width of the device. *(This does not apply to iPad and iPad Pro)*

#### Blog page
- Make sure that the blog posts are displayed on their own row on smaller screens. *(This does not apply on iPad Pro)*
- Make sure that the sidebar is displayed on its own row right under all the blog posts. *(This does not apply on iPad Pro)* *(Bug noted of flaws in the layout of the sidebar. Please see bugs found section for more details.)*

#### Blog post details page
- Make sure the sidebar is not displayed on smaller devices. *(This does not apply to iPad Pro)*

#### Add post page
- Make sure the 'Add Post' form covers the whole width of the screen on phone devices.

#### Delete post page
- Make sure the content of the page covers the whole width of the screen on phone devices.

#### Add Comment page
- Make sure the form covers the whole width of the screen when on phone devices.

#### Delete Comment page
- Make sure the content of the page covers the whole width of the screen on phone devices.

#### Profile page
- Make sure the Delivery Information column and the ORder History column displays on their own row, starting with the Delivery Information column.

#### Sign up page
- Make sure the sign up form covers the width of the screen on phone devices.

#### Log in page
- Make sure the content and log in form covers the width of the screen on phone devices.

#### Log out page
- Make sure the content and log out form covers the width of the screen on phone devices.

#### 404 Page not found
- Make sure the content covers the width of the screen on phone devices.

#### 500 Internal Server Error
- Make sure the content covers the width of the screen on phone devices.

#### Shopping bag page
- Make sure that the mobile view displays the bag total first, checkout buttons second and bag items last.

#### Checkout page
- Make sure the content covers the width of the screen when on mobile view and iPad view. *(This does not apply to iPad Pro)*
- Make sure the order summary is displayed first and the checkout details section second.

#### Checkout success page
- Make sure the content covers the width of the screen when on mobile view and iPad view. *(This does not apply to iPad Pro)*

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

10. When developing and testing the quantity input on the Product Details page of a product, I stumbled across a bug that was
caused when I left out the couantity field empty and then tried to click on the 'Add To Bag' button. 
The error message that I got was ``invalid literal for int() with base 10: ''``. At the time I had no idea what was causing the error,
but I later discovered that it was because I had forgotten to add the text of 'required' at the end of the quantity input in my product_details.html template.
A simple fix, but it caused me to loose a few braincells before realising it.

11. If the sku input field is left out empty when a superuser is adding a product to the site, it will still add the product to the product list.
This may not make much difference when you have a small webshop with a smaller number of products, 
but this is an important key figure to have when developing a larger website with more products. 
Sku numbers are important and useful in such a way that you can better keep the products separated from each other. 
One solution to this would have been to make the sku field required however, this bug remains unsolved due to lack of time fixing it.

### Bugs found during testing of the site
1. The limit of a product you can add is set to 99 on the product details page, however if you have added 99 pieces of a product to the shopping bag
you can go back to the same product and add even more items so that it exceeds the 99 limit. This is noted as a bug
as the most ideal thing would be to add a limit so that it is not possible to add more items of a product when you have already
added 99 of them. A more realistic feature would be to make it impossible to add more than a certain number of an item than 
what is in stock. This probably requires some coding and may be something to think about adding in the future. The bug remains unsolved.
<div align="center">
    <img src="/readme_images/bug3.jpg" alt="bug image" width="600px">
    <br>
    <br>
</div>

2. When searching for a word that results in 0 products being shown on the products page that follows, the pagination was not pushed down to the 
page as there is no content filling the page to push it down with. This was solved by putting a min-height of 50vh to the products row.

3. When visiting the 'Home' page on an iPhone 5 device, the Laura Day text and 'Shop Collection' button is not centered correctly.
Both the text and the button are displayed slightly to the right which they should not be. Unfortunately due to lack of time, this bug remains unsolved at the moment.

4. Bug noted of products not filling out on the last row when on desktop view or iPad Pro device. This bug could be solved by adding an if statement in the template that makes the products 
fill in all the places on both desktop view and iPad Pro however, the bug remains unsolved due to lack of time fixing it.
<div align="center">
    <img src="/readme_images/bug1.jpg" alt="bug image" width="600px">
    <br>
    <br>
</div>

5. Bug noted of flaws in the layout of the sidebar when you visit the blog page on iPad device.
The text becomes more difficult to read and a lot of voids arise around the content which is not the most ideal 
for this layout.
A solution to this would have been to place the round image in a separate column placed to the left of the row, 
with the corresponding text in a separate column to the right of it. At the moment this bug remains unsolved due to 
lack of time fixing it.
<div align="center">
    <img src="/readme_images/bug2.jpg" alt="bug image" width="300px">
    <br>
    <br>
</div>

6. When a superuser adds a blog post but adds it with the status of 'Draft', the blog post will not be shown on the blog page. To get
access to the blog post the superuser has to manually type in ``/blog/<blog post name here>`` at the end of the url to be able to read it and edit/remove it. The superuser 
can however, go in to the admin panel to get an overview of all posts. An ideal solution for this would be to add a list in the blog sidebar with an overview of which posts have the status
of 'Draft' and a link to get access to the 'Post Details' page to each post. A non logged in user or a regular user can also manually type in ``/blog/<blog post name here>`` to get access to the 
blog post. At the moment this bug remains unsolved due to lack of time fixing it.

7. When on desktop view, the minus and plus buttons does not work correctly when a user wants to update the quantity of a product. The range limit is suppose to be between 1-99 but when on desktop view the user can exceed and fall below those limits. The problem does not seem to persist when the user uses mobile view. At the moment this bug remains unsolved due to lack of time fixing it. 
