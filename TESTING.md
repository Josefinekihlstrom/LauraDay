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

## Validator Testing

## Manual Testing

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