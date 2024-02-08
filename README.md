# Eire Settlers
(Developer: Valentino Braga)

Eire Settlers is a dynamic full-stack Django project designed to cultivate a vibrant community for immigrants relocating to Ireland. This project's purpose is to empower newcomers with essential information and establish a supportive network. Serving as a comprehensive platform, Eire Settlers enables individuals to share insights, experiences, and valuable advice on various aspects of settling in Ireland. Inspired by the active engagement of the Brazilian community on Facebook groups, Eire Settlers has evolved into a dedicated platform aimed at enhancing this concept. Drawing from the collaborative spirit observed within online communities, the goal is to provide a structured and inclusive space where immigrants from all backgrounds can come together to exchange knowledge, seek guidance, and forge meaningful connections as they embark on their journey to Ireland.

![Mockup image](/static/images/documentation/mockup.jpg)

[Live Website](https://eire-settlers-9b0e3e0c192c.herokuapp.com/)

# User Stories

[Kanban Board](https://github.com/users/tinobragaa/projects/3)

# Wireframes

<details>
<summary>Landing Page</summary>
<br>

![Landing Page](/static/images/documentation/wireframes/first-version/landing-page.jpg)

</details>

<details>
<summary>Sign In</summary>
<br>

![Sign In](/static/images/documentation/wireframes/first-version/sign-in.jpg)

</details>

<details>
<summary>Sign Up</summary>
<br>

![Sign Up](/static/images/documentation/wireframes/first-version/sign-up.jpg)

</details>

<details>
<summary>Groups</summary>
<br>

![Groups](/static/images/documentation/wireframes/first-version/group-selection.jpg)

</details>

<details>
<summary>Articles Interface</summary>
<br>

![Articles Interface](/static/images/documentation/wireframes/first-version/articles-view.jpg)

</details>

<details>
<summary>Article Details</summary>
<br>

![Articles Details](/static/images/documentation/wireframes/first-version/article-detail.jpg)

</details>

# Design

The website design adopts a friendly and pastel color scheme, strategically chosen to evoke a sense of warmth and approachability. Drawing from the principles of color psychology, our palette incorporates soft hues such as green, bege, blue, and turquoise. These pastel tones are known for their calming and uplifting effects, creating a visually pleasing environment that promotes a positive user experience.

## Typography/Colour Palette

Introducing a refined and trustworthy aesthetic, I chose the Protest Strike and Titillium fonts to convey elegance and credibility. Titillium exudes a subtle sophistication with its clean lines and balanced proportions, while Protest Strike adds a touch of gravitas with its sturdy and authoritative appearance. This carefully curated combination strikes a harmonious balance between elegance and seriousness, instilling confidence and reliability in the users. 

<details>
<summary>Typography</summary>
<br>

![Typography](/static/images/documentation/typography.jpg)

</details>

<details>
<summary>Colour Palette</summary>
<br>

![Colour Palette](/static/images/documentation/color-palette.jpg)

</details>
<br>

# Features

- Profile: Users can view their profile containing information such as username, profile picture, bio, and activity history.
- Edit Profile: Users can modify their profile information, including username, profile picture, and bio.
- Remove Profile: Users can opt to delete their profile permanently from the platform.
- Sign In/Sign Up: Users can log in to their existing accounts or create new accounts to access the platform's features.
- Register: New users can sign up for an account on the platform by providing necessary information such as email, username, and password.
- Like/Dislike: Users can express their preference for articles or comments by liking or disliking them.
- Save Articles: Users can bookmark articles they find interesting to access them later.
- Unsave Articles: Users can remove saved articles from their bookmarked list.
- Comment: Users can post comments on articles to share their thoughts or engage in discussions.
- Report Comment: Users can report inappropriate or abusive comments to the platform administrators.
- Edit Comment: Users can make changes to their own comments after posting them.
- Delete Comment: Users can delete their own comments if they wish to remove them from the platform.
- Create Article: Users can compose and publish new articles on the platform.
- Edit Article: Authors can make revisions to their published articles.
- Delete Article: Authors can remove their articles from the platform if needed.
- Hamburger Menu: The menu provides quick access to various features, including saved articles and articles created by the user.

# Future Features

A few features that could make the website even better are listed here:

1. Dark Mode: Introducing a dark mode option can enhance user experience by reducing eye strain and making the website more visually appealing in low-light environments. Users can switch between light and dark modes based on their preference.

2. Admin Panel: Implementing an admin panel empowers website administrators with comprehensive control over site operations. Admins can manage user accounts, moderate content, analyze website performance, and perform other essential tasks efficiently from a centralized dashboard.

3. Add Friend Functionality: Incorporating an "Add Friend" feature enables users to expand their social connections within the website's community. Users can send friend requests to others, fostering interaction and engagement. This feature enhances the social aspect of the platform and encourages networking among users.

4. Search Functionality: Integrating a robust search functionality enhances user navigation and accessibility. Users can quickly locate specific content, such as articles, posts, or user profiles, by entering relevant keywords or filters. This feature improves user satisfaction by facilitating effortless content discovery and retrieval.

5. Tag Functionality: Implementing a tag system allows users to categorize and organize content effectively. Users can assign tags to their posts, articles, or other contributions, enabling easy classification based on topics, themes, or interests. This feature enhances content organization, promotes discoverability, and facilitates targeted content consumption for users.

# Technologies Used

### Languages and Frameworks
The following languages, frameworks and databases were used to develop the website:
- HTML
- CSS
- JavaScript
- Python
- Bootstrap
- Django
- Elephant SQL
- Cloudinary

### Resources and Tools
The following resources and tools were used to develop the website:
- Git
- Figma
- Github
- Gitpod
- Favicon
- DevTools
- W3 Schools
- Codecademy
- Google Fonts
- Font Awesome
- Stack Overflow
- Tables Generator
- CI Python Linter
- JSHint Validation
- Adobe Photoshop 2023
- Techsini Mockup Generator
- GitHub Wiki TOC generator
- W3C CSS Validation Service
- W3C Markup Validation Service
- WAVE Web Accessibility Evaluation Tools

# Testing

I confirm that the website works as expected under the CRUD functionality for articles, profile and comments. 

# HTML Validation

The Nu HTML Checker (W3C) is used to validate HTML documents. The files passed without any errors.

<details>
<summary>index HTML Validation</summary>
<br>

![index HTML Validation]()

</details>

<details>
<summary>404 Error HTML Validation</summary>
<br>

![404 Error HTML Validation]()

</details>

# CSS Validation

The W3C Jigsaw CSS Validation Service is used to validate CSS documents. The file passed without any errors.

<details>
<summary>CSS Validation</summary>
<br>

![CSS Validation]()

</details>

# JS Validation

The JSHint is used to validate JavaScript documents. The files passed without any errors.

<details>
<summary>JS Validation</summary>
<br>

![JS Validation]()

</details>

# Python Validation

The project was validated using the provided CI Python Linter and it was cleared with no errors.

<details>
<summary>Python Validation</summary>
<br>

![Python Validation]()

</details>

# Deployment

[Click Here To See The Live Website](https://eire-settlers-9b0e3e0c192c.herokuapp.com/)

### Deploy
The website was deployed through the use of GitHub Pages, a feature built in to GitHub. This can be done by following the steps below.
1. In the desired repository, click on "Settings" from the top menu.
2. From the side menu to your left, select "Pages" in the "Code and automation" section.
3. Make sure the "Source" option is set to "Deploy from a branch"
4. Select the desired "Branch" from the drop down below (main branch in most cases, making sure the director is set to /(root)).
5. Select "Save", and after it refreshes the page, you will see a box at the top of the page providing you with the URL of your now published site.

To contribute or check the code yourself, you can fork or clone the repository as well.

### Fork
1. Go to the desired repository
2. Click "Fork" in the upper right corner
3. Select the owner, and set the repository name. A description can be added if desired
4. Choose whether to copy the default branch, or all branches
5. Click "Create Form"

### Clone

1. Go to the desired repository
2. Click the "Code" button at the top of the files section of the page
3. Select your desired method for cloning (HTTPS/SSH/GitHub CLI)
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory
6. Type "git clone", and then paste the URL you copied earlier. It will look like this, with your GitHub username instead of "YOUR-USERNAME": "$ git clone https://github.com/YOUR-USERNAME/DESIRED-REPOSITORY"
7. Press Enter. Your local clone will be created.

### Heroku

1. Create a user account with Heroku.
2. Click New in the top-right corner of your Heroku Dashboard.
3. Click on the dropdown menu and select create new.
4. The app name is unique to all apps within Heroku so select one that is not currently in use.
5. Select a region, EU or USA.
6. Click Create App.
7. In the app settings click Reveal Config vars, set the value of KEY to PORT, and the value to 8000 and click add.
8. Click Add Buildpack.
9. Choose Python first and click add.
10. Choose Node.js second.
11. The order is important, Python needs to be first, then Node.js second.
12. Click on the Deploy tab, select connect to Github and search for your repository.
13. Click on Enable automatic deploy or Deploy branch depending on your use case.

# Credits

A list of references and tutorials used for the site:

* GitHub Repositories
* Hello Django Project
* I Think Therefore I Blog
* Boutique Ado Project

# Acknowledgements

I would like to take this opportunity to acknowledge and thank the following people:

- A big thank you to my therapist for helping me thrive.
- A huge thank you to my husband for always being by my side.
- An even bigger thank you to my puppy, Rio, who never leaves me alone.