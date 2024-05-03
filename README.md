# Eire Settlers
(Developer: Valentino Braga)

Eire Settlers is a dynamic full-stack Django project designed to cultivate a vibrant community for immigrants relocating to Ireland. This project's purpose is to empower newcomers with essential information and establish a supportive network. Serving as a comprehensive platform, Eire Settlers enables individuals to share insights, experiences, and valuable advice on various aspects of settling in Ireland. Inspired by the active engagement of the Brazilian community on Facebook groups, Eire Settlers has evolved into a dedicated platform aimed at enhancing this concept. Drawing from the collaborative spirit observed within online communities, the goal is to provide a structured and inclusive space where immigrants from all backgrounds can come together to exchange knowledge, seek guidance, and forge meaningful connections as they embark on their journey to Ireland.

![Mockup image](/docs/mockup.jpg)

[Live Website](https://eire-settlers-9b0e3e0c192c.herokuapp.com/)

## Table of Contents

- [Eire Settlers](#eire-settlers)
  * [User Stories](#user-stories)
    + [Project Setup and Planning](#project-setup-and-planning)
    + [User Authentication and Profile Management](#user-authentication-and-profile-management)
    + [Content Creation and Interaction](#content-creation-and-interaction)
    + [User Interface and Experience](#user-interface-and-experience)
    + [Accessibility and Responsiveness](#accessibility-and-responsiveness)
  * [Design](#design)
    + [Typography](#typography)
    + [Colour Scheme](#colour-scheme)
    + [Imagery](#imagery)
  * [Wireframes](#wireframes)
    + [Desktop](#desktop)
    + [Mobile](#mobile)
  * [Features](#features)
    + [Existing Features](#existing-features)
    + [Future Features](#future-features)
  * [Database Design](#database-design)
    + [UserAllAuth Model](#userallauth-model)
    + [User Model](#user-model)
    + [Article Model](#article-model)
    + [Comment Model](#comment-model)
    + [Tag Model](#tag-model)
  * [Agile Development](#agile-development)
    + [GitHub Projects](#github-projects)
    + [GitHub Issues](#github-issues)
    + [MoSCoW Prioritization](#moscow-prioritization)
  * [Technologies Used](#technologies-used)
    + [Languages and Frameworks](#languages-and-frameworks)
    + [Resources and Tools](#resources-and-tools)
    + [Django and Python Packages](#django-and-python-packages)
  * [Testing](#testing)
  * [Deployment](#deployment)
    + [ElephantSQL Database](#elephantsql-database)
    + [Deploy with Heroku](#deploy-with-heroku)
    + [Fork](#fork)
    + [Clone](#clone)
  * [Credits](#credits)
  * [Acknowledgements](#acknowledgements)

## User Stories

For the project's advancement, I generated 29 user stories that detailed the essential tasks for achieving a well-constructed website. Following an agile development approach, I then categorized these user stories into 5 distinct Epics on the Kanban board to manage the project's progression effectively.

To see the User Stories list, click [here](https://github.com/tinobragaa/eire-settlers/issues?q=is%3Aissue+sort%3Acreated-asc+).
<br>

To see the Epics List, click [here](https://github.com/tinobragaa/eire-settlers/milestones).
<br>

To see the Kanban Board, click [here](https://github.com/users/tinobragaa/projects/3/views/1).

### Project Setup and Planning
- As a developer, I want to create user stories for project planning using agile methodology so that I can efficiently plan and organize project requirements.
- As a developer, I want to create a README file so that I can provide comprehensive information about the project, ensuring clarity and facilitating usage.
- As a developer, I want to create a wireframe so that I can visualize the project's layout and design and have a clear reference for implementation.
- As a developer, I want to plan my database interactions so that I can effectively organize and structure my project.
- As a developer, I need to set up the base Django application so that we can build features.
- As a developer, I need to deploy the application so that it is live for use.
- As a developer, I need to create a 404 page so that users are redirected when entering a broken URL.

### User Authentication and Profile Management
- As a user, I would like to be able to sign up, so that I can network with other users in the Eire Settlers community. 
- As a user, I need a profile where I can store info about me, my name, location, and nationality.
- As a user, I would like to be able to edit my profile when I want to make changes to my details. 
- As a user, I want to sign in with one of my social accounts so that I can sign in or sign up quickly and easily.
- As a user, I want to be able to add friends so that I can expand my social connections within the website's community.
- As a user, I want to be able to log in and out so that I can protect my personal information, create new articles, and interact with other users through likes, comments, and saving articles. 

### Content Creation and Interaction
- As a user, I want to create an article so that I can share my thoughts or start discussions on topics of interest to me.
- As a user, I want to be able to edit articles that I have previously published so that I can update and improve the content as needed.
- As a user, I want to be able to save articles that I find interesting or want to revisit late so that I can easily access and reference them at a later time. 
- As a user, I want to be able to like comments posted by other users so that I can express appreciation or agreement with their contributions. 
- As a user, I want to be able to report comments that I believe violate the site's community guidelines so that I can notify the administrators of inappropriate content for review and potential removal.
- As a user, I want to be able to create new comments, edit existing comments, and delete comments from articles so that I can engage with the content and express my thoughts effectively.
- As a developer, I need to create reusable resources so that further pages can be developed.

### User Interface and Experience
- As a user, I would like a responsive navigation menu so that I can easily navigate from any device.
- As a user when I log in, I want to be able to access the latest articles so I am up to date with the user's discussions.
- As a user, I would like the site to have a customized favicon so I can easily identify it when I have multiple tabs open.
- As a user, I want to be able to search for content and profiles so that I can easily find relevant information and connect with others.
- As a user, I want to be able to add tags to my content so that I can categorize it effectively and enhance its discoverability.
- As a developer, I need to style the allauth pages so that they fit with the theme styling.

### Accessibility and Responsiveness
- As a developer, I want to ensure that the website is designed and developed with accessibility features so that users with disabilities can navigate and interact with the site effectively.
- As a user, I can view and use the web app on all screen sizes so that I can change my device and access the app.
- As a User, I want to have the option to enable and use dark mode in the application so that I can reduce eye strain and enhance readability in low-light environments.

## Design
The project's design was inspired and created to envelop users in a friendly and inviting atmosphere, carefully selecting pastel hues to evoke warmth and approachability. Drawing from color psychology principles, soft tones like green, beige, blue, and turquoise were chosen for their calming and uplifting effects, ensuring a positive user experience. To convey credibility and refinement, the Protest Strike and Titillium fonts were meticulously selected, striking a balance between elegance and seriousness. This thoughtful combination instills confidence and reliability in users, fostering trust and engagement from the moment they land on the website.

### Typography
Introducing a refined and trustworthy aesthetic, I chose the Protest Strike and Titillium fonts to convey elegance and credibility. Titillium exudes a subtle sophistication with its clean lines and balanced proportions, while Protest Strike adds a touch of gravitas with its sturdy and authoritative appearance. This carefully curated combination strikes a harmonious balance between elegance and seriousness, instilling confidence and reliability in the users. 

![Typography](/docs/typography.jpg)

### Colour Scheme
The website colour scheme adopts a friendly and pastel color scheme, strategically chosen to evoke a sense of warmth and approachability. Drawing from the principles of color psychology, our palette incorporates soft hues such as green, bege, blue, and turquoise. These pastel tones are known for their calming and uplifting effects, creating a visually pleasing environment that promotes a positive user experience.

![Colour Palette](/docs/color-palette.jpg)

### Imagery
In imagery, I've chosed a captivating centerpiece to resonate with the website's mission of fostering community among immigrants. The main illustration, sourced from [Pexels](https://www.pexels.com/), portrays a diverse array of individuals connecting and interacting harmoniously. Through vibrant depictions of shared experiences and cultural diversity, this illustration beautifully encapsulates the essence of the platform's goal—to unite immigrants and create a supportive, inclusive community. 

## Wireframes

### Desktop

<details>
<summary>Landing Page</summary>
<br>

![Landing Page](/docs/wireframes/landing-page.jpg)

</details>

<details>
<summary>Sign In</summary>
<br>

![Sign In](/docs/wireframes/sign-in.jpg)

</details>

<details>
<summary>Sign Up</summary>
<br>

![Sign Up](/docs/wireframes/sign-up.jpg)

</details>

<details>
<summary>Groups</summary>
<br>

![Groups](/docs/wireframes/group-selection.jpg)

</details>

<details>
<summary>Articles Interface</summary>
<br>

![Articles Interface](/docs/wireframes/articles-view.jpg)

</details>

<details>
<summary>Article Details</summary>
<br>

![Articles Details](/docs/wireframes/article-detail.jpg)

</details>

### Mobile

## Features

### Existing Features

- **Landing Page**

    - This is the page a user lands on when arriving at the site for the first time or before they've logged in if they don't have an active session. It welcomes them to the site and gives them the option to see the existent articles, sign up for an account or log in to an existing account.

    <details>
    <summary>Landing Page Guest View</summary>
    <br>

    ![screenshot](/docs/features/landing-page-guest.jpg)

    </details>

    <details>
    <summary>Landing Page Member View</summary>
    <br>

    ![screenshot](/docs/features/landing-page-member.jpg)

    </details>

- **Sign Up Page**

    - This is where the user can create an account for themselves by entering their desired username and password twice to confirm. If the user accidentally comes to this page instead of the login page they can get to the right page using the link in the card text.

    <details>
    <summary>Sign Up Page</summary>
    <br>

    ![screenshot](/docs/features/sign-up-page.jpg)

    </details>

- **Sign In Page**

    - This is where users with existing accounts can log in with either their username and password. They can choose to let their browser remember them if they plan on returning to the site on the same device to avoid having to log in again. There's a link to the sign up page too if the user accidentally navigated to this page instead of trying to create an account.

    <details>
    <summary>Sign In Page</summary>
    <br>

    ![screenshot](/docs/features/sign-in-page.jpg)

    </details>

- **Sign Out Page**

    - When the user wants to finish their session and logout, they can do so from the nav menu. When a user clicks the "Sign Out" button they're met with a page asking them to confirm they want to log out. They're redirected to the landing page if they click the confirmation button and a message pops up confirming that they've logged out.

    <details>
    <summary>Sign Out Page</summary>
    <br>

    ![screenshot](/docs/features/sign-out-page.jpg)

    </details>

- **All Article Page**

    - This is where users can see displayed the list of all available articles within EireSettlers. Each article is presented in a visually appealing manner, inviting users to explore further. With intuitive navigation controls, users can seamlessly sift through the library.

    <details>
    <summary>All Articles Page</summary>
    <br>

    ![screenshot](/docs/features/all-articles-page.jpg)

    </details>

- **New Article page**

    - The "New Article" Page enables users to compose new articles by filling in specific fields: title, description, content and image.

    <details>
    <summary>New Article Page</summary>
    <br>

    ![screenshot](/docs/features/new-article-page.jpg)

    </details>

- **Navigation Bar**

    - The nav menu contains everything the user will need to navigate the site. The site logo always appears on the site menu with the other items only showing for logged in users. From the nav menu, user's can go to website's article feed, create article, their saved articles, their profile, view articles they've created and log out.

    <details>
    <summary>Navbar Guest</summary>
    <br>

    ![screenshot](/docs/features/nav-bar-guest.jpg)

    </details>
  
    <details>
    <summary>Navbar Member</summary>
    <br>

    ![screenshot](/docs/features/nav-bar-member.jpg)

    </details>


    <details>
    <summary>Navbar - Mobile</summary>
    <br>

    ![screenshot](/docs/features/nav-bar-mobile.jpg)

    </details>

- **Footer**

    - The footer appears across the website and includes the logo where users can click to return to the website's feed.

    <details>
    <summary>Footer</summary>
    <br>

    ![screenshot](/docs/features/footer.jpg)

    </details>

- **Pagination**

    - On the all article page and the homepage pagination is implemented so if more than 6 posts appear in the feed then buttons appear at the bottom to split the feed into individual pages with a maximum of 6 posts on a page. This is to increase the user experience and make the site content easier to digest.

    <details>
    <summary>Pagination</summary>
    <br>

    ![screenshot](/docs/features/pagination.jpg)

    </details>

- **Individual Article Page**

    - Articles are found in the homepage for guests and on the article feed view for both guests/members. When viewing a article, users can endorse articles, bookmark it, see when the article was created, see the author's name and edit/delete the article if they're the original author. Displays the count of endorsements and the bookmark icon. Under the article the users can see a list of comments on the post and a form to add their own comment to the post if they're logged in.

    <details>
    <summary>Individual Article Page Guest</summary>
    <br>

    ![screenshot](/docs/features/article-detail-guest.jpg)

    </details>

    <details>
    <summary>Individual Article Page Member</summary>
    <br>

    ![screenshot](/docs/features/article-detail-member.jpg)

    </details>

    <details>
    <summary>Edit/Delete Article Buttons</summary>
    <br>

    ![screenshot](/docs/features/edit-delete-article.jpg)

    </details>

    <details>
    <summary>Edit/Delete/Report Comment Buttons</summary>
    <br>

    ![screenshot](/docs/features/edit-delete-report-comment.jpg)

    </details>

    <details>
    <summary>Endorse, Save and Comments Icons</summary>
    <br>

    ![screenshot](/docs/features/endorse-bookmark-comment-icons.jpg)

    </details>

    <details>
    <summary>Add Comment Form</summary>
    <br>

    ![screenshot](/docs/features/add-comment-form.jpg)

    </details>

- **Delete Article**

    - Articles can be deleted by the post author and the admin by clicking on the delete icon. When deleting a post, the user is brought to a confirmation page to avoid posts being deleted accidentally. There's a button to bring them back to the post if the user changes their mind about deleting their post.

    <details>
    <summary>Delete Article Page</summary>
    <br>

    ![screenshot](/docs/features/delete-article-page.jpg)

    </details>

- **Edit Article**

    - Articles can be egit by the post author and the admin by clicking on the edit button. When editing a article, the user is brought to a confirmation page to avoid posts being deleted accidentally. There's a button to bring them back to the post if the user changes their mind about deleting their post.

    <details>
    <summary>Edit Article Page</summary>
    <br>

    ![screenshot](/docs/features/edit-article-page.jpg)

    </details>

- **Comments**

    - Articles comments are viewed under a article. Comments can be deleted and edit by the comment author or the admin.

    <details>
    <summary>Add Comment - Guest</summary>
    <br>

    ![screenshot](/docs/features/add-comment-guest.jpg)

    </details>

    <details>
    <summary>Add Comment - Member</summary>
    <br>

    ![screenshot](/docs/features/add-comment-form.jpg)

    </details>

- **Delete Comment**

    - Comments can be deleted by the comment author and the admin. Clicking the delete button users are brought to a confirmation page to avoid comments being deleted accidentally. There's a button to bring them back to the post they commented on if the user changes their mind about deleting the comment.

    <details>
    <summary>Delete Comment Page</summary>
    <br>

    ![screenshot](/docs/features/delete-comment-page.jpg)

    </details>

- **Edit Comment**

    - Comments can be edited by the comment author and the admin. Clicking the edit button brings them to a page where they can see their comment and make changes before hitting a button to save it. There's also a button to bring them back to the post where the comment was made if they hit the edit button by mistake.

    <details>
    <summary>Edit Comment Page</summary>
    <br>

    ![screenshot](/docs/features/edit-comment-page.jpg)

    </details>

- **Report Comment**

    - Comments can be reported by members that are not the comment's author. Clicking the report it displays a message stating that comment was reported which is then flagged to the admin.

    <details>
    <summary>Report Comment</summary>
    <br>

    ![screenshot](/docs/features/report-comment.jpg)

    </details>

- **Profile**

    - The profile contains a card with the user's information including profile picture, display name, username, bio, nationality and country. When user is viewing their profile they'll have an button to edit and to delete their profile. 

    <details>
    <summary>Profile Page</summary>
    <br>

    ![screenshot](/docs/features/profile-page.jpg)

    </details>

- **Delete Profile**

    - This is where the user can delete their profile. There's a button to bring them back to their profile if they decide not to delete their profile.

    <details>
    <summary>Delete Profile Page</summary>
    <br>

    ![screenshot](/docs/features/delete-profile-page.jpg)

    </details>

- **Edit Profile**

    - This is where the user can edit their profile details including profile picture, display name, username, bio, nationality and country. There's a button to bring them back to their profile if they decide not to make any edits.

    <details>
    <summary>Edit Profile Page</summary>
    <br>

    ![screenshot](/docs/features/edit-profile-page.jpg)

    </details>

- **Saved Articles Page**

    - On the "My Saved Articles" Page, members find a collection of their saved articles. Each saved article is neatly organized, making it simple for users to revisit and engage with the content that resonates with them.

    <details>
    <summary>Saved Articles Page</summary>
    <br>

    ![screenshot](/docs/features/saved-articles-page.jpg)

    </details>

- **My Articles Page**

    - On the "My Articles" Page, members find a collection of the articles created by them. This page serves as a place for members to easily access their creations. 

    <details>
    <summary>My Articles Page</summary>
    <br>

    ![screenshot](/docs/features/my-articles-page.jpg)

    </details>

- **Error Pages**

    - If a user ends up on a page that either doesn't exist or that they shouldn't be on (regular user using admin panel link or trying to delete other user's post through a link) then they'll be shown an error page with a button to bring them back to their feed.

    ![screenshot]()

    ![screenshot]()

    ![screenshot]()

### Future Features
A few features that could make the website even better are listed here. These features have been logged as "Future Release" in my [Kanban Board](https://github.com/users/tinobragaa/projects/3/views/1).

- **Dark Mode**
  - Introducing a dark mode option can enhance user experience by reducing eye strain and making the website more visually appealing in low-light environments. Users can switch between light and dark modes based on their preference.

- **Social Media Login**
  - Enabling social media login functionality allows users to sign in to the platform using their existing social media accounts, such as Facebook, Twitter, or Google. This feature simplifies the registration and login process, saving users time and effort. Additionally, it enhances user convenience by eliminating the need to remember separate login credentials for the platform.

- **Add Friend Functionality**
  - Incorporating an "Add Friend" feature enables users to expand their social connections within the website's community. Users can send friend requests to others, fostering interaction and engagement. This feature enhances the social aspect of the platform and encourages networking among users.

- **Search Functionality**
  - Integrating a robust search functionality enhances user navigation and accessibility. Users can quickly locate specific content, such as articles, posts, or user profiles, by entering relevant keywords or filters. This feature improves user satisfaction by facilitating effortless content discovery and retrieval.

- **Tag Functionality**
  - Implementing a tag system allows users to categorize and organize content effectively. Users can assign tags to their posts, articles, or other contributions, enabling easy classification based on topics, themes, or interests. This feature enhances content organization, promotes discoverability, and facilitates targeted content consumption for users.

## Database Design
I utilized [dbdiagram](https://dbdiagram.io/home) to create an entity relationship diagram, offering a clear visualization of the interconnections among my data structures. This streamlined the development process by offering a comprehensive visualization.

![Database Design](/docs/database-schema.jpg)

### UserAllAuth Model
- The user model is the default Django user model.

| key | Field Type | Validation |
| --- | --- | --- |
| id | IntegerField | |
| password | CharField |  |
| last_login | DateTimeField |  |
| is_superuser | BooleanField |  |
| username | CharField | max_length=150, unique=True |
| first_name | CharField | max_length=150, blank=True |
| last_name | CharField | max_length=150, blank=True |
| email | EmailField | max_length=254, unique=True |
| is_staff | BooleanField |  |
| is_active | BooleanField |  |
| date_joined | DateTimeField |  |

### User Model
-  User model is connected to the UserAllAuth model with OneToOneField. This model is used to store extra user information.

| key | Field Type | Validation |
| --- | --- | --- |
| user | OneToOneField | User, on_delete=models.CASCADE |
| first_name | CharField | max_length=50, null=True, blank=True |
| last_name | CharField | max_length=50, null=True, blank=True |
| location | CharField | max_length=100, null=True, blank=True |
| email | EmailField | max_length=100, null=True, blank=True |
| bio | TextField | max_length=500, null=True, blank=True |
| user_image | ResizedImageField | upload_to='users/', null=True, force_format='WEBP', quality=85, blank=True, default='users/default_user.webp' |
| created | DateTimeField | auto_now_add=True |

### Article Model
- The Article model is used to store all the articles uploaded by users.

| key | Field Type | Validation |
| --- | --- | --- |
| title | CharField | max_length=100, null=True |
| body | TextField | upload_to='memes/', null=True, force_format='WEBP', quality=85, blank=True, default='memes/default.webp |
| user_id | Integer | User |
| created | DateTimeField | auto_now_add=True |

### Comment Model
- The Comment model is used to store all the comments on the articles.

| key | Field Type | Validation |
| --- | --- | --- |
| user | ForeignKey | UserProfile, on_delete=models.CASCADE, null=True, blank=True |
| comment | TextField | max_length=500 |
| created | DateTimeField | auto_now_add=True |
| article | ForeignKey | Meme, on_delete=models.CASCADE, related_name='comment' |

### Tag Model
- The tag model is used to store all the tags for the articles.

| key | Field Type | Validation |
| --- | --- | --- |
| name | CharField | max_length=20, null=True, blank=True |
| created | DateTimeField | auto_now_add=True |
| id | UUIDField | primary_key=True, default=uuid.uuid4, editable=False |

## Agile Development

### GitHub Projects
GitHub Projects was utilized as an Agile tool for managing this project. This platform facilitated the planning and tracking of user stories, issues, and epics, which were then monitored on a weekly basis using a basic Kanban board setup.

- User Stories: full list [here](https://github.com/tinobragaa/eire-settlers/issues?q=is%3Aissue+sort%3Acreated-asc+).
- Epics: full list [here](https://github.com/tinobragaa/eire-settlers/milestones).

![Kanban Board](/docs/kanban-board.jpg)

### GitHub Issues
GitHub Issues functioned as an additional Agile tool for me. I employed my custom User Story Template within it to organize user stories effectively. Additionally, it facilitated tracking milestones (Epics) for the project.

To see the User Stories list, click [here](https://github.com/tinobragaa/eire-settlers/issues?q=is%3Aissue+sort%3Acreated-asc+).
<br>

To see the Epics List, click [here](https://github.com/tinobragaa/eire-settlers/milestones).
<br>

To see the Kanban Board, click [here](https://github.com/users/tinobragaa/projects/3/views/1).

### MoSCoW Prioritization
I broke down my Epics into individual stories before prioritizing and implementing them. This method allowed me to utilize the MoSCoW prioritization and apply labels to the user stories in the Issues tab.

- **Must Have**: guaranteed to be delivered (*max 60% of stories*)
- **Should Have**: adds significant value, but not vital (*the rest ~20% of stories*)
- **Could Have**: has small impact if left out (*20% of stories*)
- **Won't Have**: not a priority for this iteration

## Technologies Used

### Languages and Frameworks
This project was created using the following languages and frameworks:
- [HTML](https://en.wikipedia.org/wiki/HTML) as the markup language and templating language.
- [CSS](https://en.wikipedia.org/wiki/CSS) as the style sheet language.
  - [Bootstrap](https://getbootstrap.com/) as the CSS framework.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) to create carousel on index.html.
  - [jQuery](https://jquery.com/) to simplify DOM manipulation.
- [Python](https://www.python.org/) as the backend programming language.
  - [Django](https://www.djangoproject.com/) as the Python web framework.

### Resources and Tools
The following resources and tools were used to develop the website:
- [GitHub](https://github.com/) - Source code hosted on GitHub, deployed using Git Pages.
- [GitPod](https://www.gitpod.io/) - Used to commit, comment and push code during the development process.
- [Font Awesome](https://fontawesome.com/) - Used to source necessary icons used in the project.
- [Behance](https://www.behance.net/) - Used to research design trends.
- [Pexels](https://www.pexels.com/) - Used to search for images to use on the website.
- [Figma](https://www.figma.com/) - Used to create wireframes and website structure map for the project.
- [Adobe Photoshop](https://www.adobe.com/ie/products/photoshop.html) - Used to design the store's mockups and placeholders. 
- [Gramarly](https://app.grammarly.com/) - Used for general spell-check.
- [Google Fonts](https://fonts.google.com/) - Used to import fonts to the project.
- [Heroku](https://www.heroku.com/) - Used to deploy the project.
- [dbdiagram](https://dbdiagram.io/home) - Used to make the database design.
- [Am I Responsive?](https://ui.dev/amiresponsive) - Used to create the website mockup.
- [TOC](https://ecotrust-canada.github.io/markdown-toc/) - Used to create the TOC of this file.
- [ElephantSQL](https://www.elephantsql.com/) - Free and open-source relational database management system (RDBMS).
- [Bootstrap](https://getbootstrap.com/) - Used for adding predefined styled elements and creating responsiveness.
- [JsHint](https://jshint.com/) - Used for validating the javascript code.
- [CI Python Linter](https://pep8ci.herokuapp.com/#) - Used for validating the python code.
- [HTML W3C HTML Validator](https://validator.w3.org/#validate_by_uri+with_options) - Used for validating the HTML.
- [CSS Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri) - Used for validating the CSS.
- [Chrome Del Tools](https://developer.chrome.com/docs/devtools/) - For debugging the project.
- [W.A.V.E.](https://wave.webaim.org/) - Used for testing accessibility.
- [LightHouse](https://developer.chrome.com/docs/lighthouse/overview/) - Used for testing performance.
- [Stack Overflow](https://stackoverflow.com/) - Used for finding solutions to coding issues and asking programming-related questions.

### Django and Python Packages
The following Django applications and Python Packages were used to develop the website:
- [asgiref](https://pypi.org/project/asgiref/) - ASGI (Asynchronous Server Gateway Interface) framework, a standard interface between web servers and Python web applications.
- [dj-database-url](https://pypi.org/project/dj-database-url/) - A utility for utilizing database URLs in Django applications.
- [Django](https://www.djangoproject.com/) - A Python-based web framework that follows the model-template-view architectural pattern, used for building the project.
- [django-allauth](https://django-allauth.readthedocs.io/) - A Django application used for account registration, management, and authentication.
- [django-crispy-forms](https://pypi.org/project/django-crispy-forms/) - A Django application that makes it easy to style Django forms.
- [django-resized](https://pypi.org/project/django-resized/) - A Django application to resize and convert images.
- [gunicorn](https://pypi.org/project/gunicorn/) - A Python Web Server Gateway Interface (WSGI) HTTP server.
- [oauthlib](https://pypi.org/project/oauthlib/) - A generic and reusable Python library for implementing OAuth1 and OAuth2 providers.
- [Pillow](https://pypi.org/project/Pillow/) - The Python Imaging Library adds image processing capabilities to your Python interpreter.
- [psycopg2](https://pypi.org/project/psycopg2/) - A PostgreSQL adapter for Python.
- [python3-openid](https://pypi.org/project/python3-openid/) - A set of Python packages for implementing OpenID Connect.
- [requests-oauthlib](https://pypi.org/project/requests-oauthlib/) - OAuthlib authentication support for Requests.
- [sqlparse](https://pypi.org/project/sqlparse/) - A non-validating SQL parser module for Python.
- [urllib3](https://pypi.org/project/urllib3/) - A powerful HTTP client for Python, which provides features such as connection pooling, request retries, and more.
- [whitenoise](https://pypi.org/project/whitenoise/) - Whitenoise serves its own static files, making it a self-contained unit that can be deployed anywhere without relying on nginx, Amazon S3 or any other external service. 

## Testing
For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment
[Click Here To See The Live Website](https://eire-settlers-9b0e3e0c192c.herokuapp.com/)

### ElephantSQL Database
This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:
- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: eire-settlers).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

### Deploy with Heroku
This project uses [Heroku](https://www.heroku.com/) to host and deploy the website

To deploy your website using Heroku, begin by signing up for a Heroku account. Then, proceed with the following steps:s
1. Go on to [Heroku](https://www.heroku.com/) website and [log in](https://id.heroku.com/login) if you already have an account or [sign up](https://signup.heroku.com/) if you don't. 
2. Click on the "New" button on the top right of the home page and select "Create new App" from the drop-down menu.
3. In the "App name" field enter the name of your app. This name has to be unique. 
    - Heroku displays a green tick if your app name is available.
4. In the "Choose a region" field choose either the United States or Europe based on your location.
5. Click the "Create app" button.
6. Next page, top centre of the screen, select the "Settings" tab. 
7. In the "Config Vars" section, click on the "Reveal config Vars" button.
8. In this section you need to enter your environment variables. Usually stored in the env.py file locally. In my case, I have the folllwing variables: 
    - SECRET_KEY - Django secret key.
    - CLOUDINARY_URL - Cloudinary API key.
    - DATABASE_URL - ElephantSQL database URL.
9. Copy and paste these variables into the KEY field and their values into the VALUE field.
10. Go back to the top of the screen and select the "Deploy" tab.
11. In the "Deployment method" section select "GitHub".
    1. In "Connect to GitHub" click on the "Search" button. Find the project repository in the list and click on the "Connect" button.
    2. Scroll to the bottom of that page. Click on the "Deploy Branch" button to deploy.
    3. You should also see an option to enable automatic deployment. If you enable this, every time you push to GitHub, Heroku will automatically deploy the app.
12. You will see build log scrolling at the bottom of the screen after that. When successfully finished building the app, you should see the link to your app.

### Fork
By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/tinobragaa/eire-settlers)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Clone
You can clone the repository by following these steps:

1. Go to the [GitHub Repository](https://github.com/tinobragaa/eire-settlers) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/tinobragaa/eire-settlers`
7. Press Enter to create your local clone.

## Credits
A list of references and tutorials used for the site:

* The development process relied on The Code Institute's "Hello Django", "Boutique Ado" and "I Think Therefore I Blog" walkthrough projects.
* Stack Overflow, CI Slack and Google was used for countless research into code functionalities and problem solving.
* The developer leveraged their past projects, including [Mil's Kitchen](https://tinobragaa.github.io/mils-kitchen/) (GitHub repository [here](https://github.com/tinobragaa/mils-kitchen)), [codit Quiz - Your JavaScript Quiz](https://tinobragaa.github.io/codit-quiz/) (GitHub repository [here](https://github.com/tinobragaa/codit-quiz)), [Password Creator](https://password-creatorr.herokuapp.com/) (GitHub repository [here](https://github.com/tinobragaa/password-creator)), and [HefestusCave](https://eire-settlers-9b0e3e0c192c.herokuapp.com/) (GitHub repository [here](https://github.com/tinobragaa/eire-settlers)), as primary references for accessing code solutions and CSS, as well as for README documentation purposes.

## Acknowledgements
I would like to take this opportunity to acknowledge and thank the following people:

- A big thank you to my therapist for helping me thrive.
- A huge thank you to my husband for always being by my side.
- An even bigger thank you to my puppy, Rio, even though he is not really good at coding, he is excellent at keeping me company.