# shuffle-fitness-ms4

This is a full-stack web application using Django framework alongside HTML, CSS, Python and JavaScript.

This application is for a fictional fitness and nutrition company called Shuffle Fitness. The application will allow users to select an fitness subsrciption that suits them, they will be able to set-up payment using stripe. The user will need to create an account to be able to access paid for material, the user will also be able to rate the material that they have purchased. Some other features that this site will use are confirmation emails, CRUD for the admin to create new content and control the database. 

This webpage is for educational purposes and the stripe functionality will only accept test card details.

* To use the stripe card payment please use the following card information:
    * Card Number: 4242 4242 4242 4242
    * Any Date or you can use: 04/24
    * Any CVV Number

### Unforunately this is not complete and I have had to submit this site while not being 100% ready. I do apologise for the inconvience for this! I understand that this will be a fail and I will make sure that I work very hard to make it a pass on the potential resubmission date.

## **Table of Contents**
* [1.**UX**](#1-ux)
    * [**User Stories**](#user-stories)
    * [**Wireframes**](#wireframes)
    * [**Design**](#design)
* [2.**Database Design**](#2-database-design)
* [3.**Features**](#3-features)
    * [**Existing Features**](#exisiting-features)
    * [**Features to implement in the future**](#features-to-implement-in-the-future)
* [4.**Technologies Used**](#4-technologies-used)
* [5.**Deployment**](#5-deployment)
* [6.**Credits**](#6-credits)
* [7**Acknowledgements**](#7-acknowledgements)

## 1. **UX**
Overview of the UX design including the wireframse which have been created as a foundation for the site.

### **User Stories**
* Customers
    * Web Experience
        * As a customer, I would like to see what the options for fitness and nutrition are on the site.
        * As a customer, I want the site to be easy to navigate.
        * As a customer, I would like to see plenty of information on the company.
        * As a customer, I would like to be able to login securely.
        * As a customer, I would like to be able to send an email to the company. 
    * Shopping/Purchase
        * As a customer, I would like to have a good description of the different plans that are offered.
        * As a customer, I would like to have use of a shopping cart.
        * As a customer, I would like to be able to edit the shopping cart if needed.
        * As a customer, I would like to use a secure checkout.
        * As a customer, I would like to see confirmation when I successfly complete a task.
    * Searching
        * As a customer, I would like to see all the subscriptions that are offered.
        * As a customer, I would like to search by category or with a simple word search. 
    * Account
        * As a customer, I would like to have my details saved to an account. 
        * As a customer, I would like to be able to access my purchase on my profile.
        * As a customer, I would like to leave a rating for the products that I have purchased.
* Admin User, Business Owner
    * As the business owner, I would like to be able to add, edit and delete products with ease.
    * As the business owner, I would like my customers to enjoy using the website.
    * As the business owner, I would like to have access to a admin section.

### **Wireframes**
To create my wireframes I used a website called MockFlow. The JPEG of the wireframes are attached bellow. 
#### Home/Landing Page
![Wireframe Home Image](readme-img/wireframe-img/sf-home.jpg)
#### Membership/Product Page
![Wireframe Memberships Image ](readme-img/wireframe-img/sf-membership.jpg)
#### Login Page
![Wireframe Login Page](readme-img/wireframe-img/sf-login.jpg)
#### Profile Page
![Wireframe Profile Page](readme-img/wireframe-img/sf-profile.jpg)
#### Checkout Page
![Wireframe Checkout Page](readme-img/wireframe-img/sf-checkout.jpg)

### **Design**
The design of this site will be simplistic, but with images that bring out some life onto the site. There will be little bits of colour, to break up the white and black text. 

The colour I have chosen to use just to break up the white background and black text is #8FD0CA, which is a light blue, with a hint of grey. ![Color #8FD0CA](readme-img/colour/8FD0CA.png)

The buttons are a mix of black and white, each has the opposite colour for the font.

#### Font Family
The font family that I have chosen to use are from google fonts. I have used two fonts throughout my site one for main titles/headers and the other for all other text. 
    - For titles and headers I used Syncopate with a backup of sans-serif.
    - For all other text I used Raleway also with a backup of sans-serif.

#### Images
Images are used throughout this site, all the images have been selected from Unsplash. 

There are two main hero images, one is on the landing page and the other is on the membership page. I used the hero images to give the site more life and also to grab the users attention.

##### Icons
* Through out this project I have used icons provided by [Font Awesome](https://fontawesome.com/) they are used in my navbar and also within my footer.

## **Database Design**
![Data Schema](readme-img/data-schema/data-schema.png)

## **Features**
* Header & Navbar
    * The Navbar is positioned at the top of each page, and is can be accessed with ease.
    * The Navbar collaspes when the screen size changes to smaller screens.
    * At the left of the Navbar you have the company name in bold and caplitised letters, this is to draw attention so that the user knows the site they are visiting.
* Search
    * A search box can be found within the Navbar and is accessible on every page of the site. 
    * The search bar collapses with the rest of the Navbar when on mobile screens
    * The user can search keywords that link to a membership they wish to find more information about.
* Toasts
    * They appear on every page whenever the user makes a certian action that prompts a response. 
    * These messages will pop up in the right hand corner and can be closed with a click on the button. 
    * They give feedback to the user on actions such as logging in or out, adding a membership to the bag and also warnings, for example when editing a membership.
* Buttons & Links
    * all the buttons have a consistent colour scheme.
    * Every button will take the user to their desired location.

* Django Allauth feature
    * Django Allauth is a python package, I have used this, as it has features such as signup, login, logout and password change. These are all needed for the user to access the site correctly. 
    * Once signed up, an email verification will be sent to the user's email to confirm. Once this is confirmed they will have access to their purchased memberships.

* Memberships

* 

## **Technologies Used**

## **Deployment**

## **Credits**
* All the code has been written by Daniel Goodwin

* [Bootstrap 4](https://validator.w3.org/) library was used to create a responsive site.

* To help me along the way, I refered back to the Boutique Ado videos (this was a project from Code Institute).

* To help with the content of the website, I took inspiration from:
    * [Daily Burn](https://lp.dailyburn.com/byrdie/index.html)
    * [Obe Fitness](https://obefitness.com/)

* [Unsplash](https://unsplash.com/) was used for all the images on the site.
* [DrawSQL](https://drawsql.app/) was used to create my Data Schema image.
* I used [Color-Name](https://www.color-name.com/popular) as a tool to help me pick colours.
* [Google Fonts](https://fonts.google.com/) was used to choose two fonts for the site.

## **Acknowledgements**
* A huge shout out to the Code Institue tutors, as without them I never would have come close to finishing this project. These guys are amazing!
* A big thank you to my wife, for pushing me and reminding me that I can complete this. 




 


