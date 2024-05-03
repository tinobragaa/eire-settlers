# Table of Contents

- [Testing](#testing)
  * [Validation](#validation)
    + [HTML](#html)
    + [CSS](#css)
    + [JavaScript](#javascript)
    + [Python](#python)
  * [Browser Compatibility](#browser-compatibility)
  * [Responsiveness Testing](#responsiveness)
  * [Lighthouse Audit](#lighthouse-audit)
  * [Manual Testing](#manual-testing)
  * [User Story Testing](#user-story-testing)
  * [Bugs](#bugs)

**Return back to the [README.md](README.md) file.**

# Testing

During the evolution of this project, I've conducted a multitude of tests to verify the functionality of the site. Within this section, you'll discover comprehensive documentation detailing every test performed across the site.

## Validation

### HTML

The [HTML W3C Validator](https://validator.w3.org) was used to validate HTML files.

| Page | Validator | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | W3C | ![screenshot](/docs/testing/home-html-validation.jpg) | Pass: No Errors |
| All Articles | W3C | ![screenshot](/docs/testing/all-articles-html-validation.jpg) | Pass: No Errors |
| Individual Article | W3C | ![screenshot](/docs/testing/article-details-html-validation.jpg) | Pass: No Errors |
| Create Article | W3C | ![screenshot](/docs/testing/create-article-html-validation.jpg) | Pass: No Errors |
| Edit Article | W3C | ![screenshot](/docs/testing/edit-article-html-validation.jpg) | Pass: No Errors |
| Delete Article | W3C | ![screenshot](/docs/testing/delete-article-html-validation.jpg) | Pass: No Errors |
| Edit Comment | W3C | ![screenshot](/docs/testing/edit-comment-html-validation.jpg) | Pass: No Errors |
| Delete Comment | W3C | ![screenshot](/docs/testing/delete-comment-html-validation.jpg) | Pass: No Errors |
| View Profile | W3C | ![screenshot](/docs/testing/view-profile-html-validation.jpg) | Pass: No Errors |
| Edit Profile | W3C | ![screenshot](/docs/testing/edit-profile-html-validation.jpg) | Pass: No Errors |
| Remove Profile | W3C | ![screenshot](/docs/testing/remove-profile-html-validation.jpg) | Pass: No Errors |
| Sign In | W3C | ![screenshot](/docs/testing/signin-html-validation.jpg) | Pass: No Errors |
| Sign Out | W3C | ![screenshot](/docs/testing/signout-html-validation.jpg) | Pass: No Errors |
| Sign Up | W3C | ![screenshot](/docs/testing/signup-html-validation.jpg) | No errors were found, except for the one "Element ul not allowed as child of element small". Error originated from Django Allauth. Contacted Tutor Support and I was told a note should suffice. |

<details>
<summary>Tutor Support Feedback HTML Error</summary>
<br>

![Tutor Feedback](/docs/tutor-feedback.jpg)

</details>
<details>
<summary>Sign Up HTML</summary>
<br>

![Sign Up HTML](/docs/signup-code.jpg)

</details>

### CSS

The [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) was used to validate CSS files.

| File | Validator | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | Jigsaw | ![screenshot](/docs/testing/style-css-validation.jpg) | Pass: No Errors |

### JavaScript

The [JShint Validator](https://jshint.com) was used to validate JS files.

| File | Validator | Screenshot | Notes |
| --- | --- | --- | --- |
| script.js  | JShint | ![screenshot](/docs/testing/script-js-validation.jpg) | Undefined variable Bootstrap |

### Python

The [CI Python Linter](https://pep8ci.herokuapp.com) was used to validate Python files.

| File | Validator | Screenshot | Notes |
| --- | --- | --- | --- |
| settings.py | CI PEP8 | ![screenshot](/docs/testing/settings-python-idation.jpg) | Pass: No Errors |
| urls.py (main) | CI PEP8 | ![screenshot](/docs/testing/urls-python-main-validation.jpg) | Pass: No Errors |
| forms.py (hubspace) | CI PEP8 | ![screenshot](/docs/testing/forms-python-hubspace-validation.jpg) | Pass: No Errors |
| models.py (hubspace) | CI PEP8 | ![screenshot](/docs/testing/models-python-hubspace-validation.jpg) | Pass: No Errors |
| urls.py (hubspace) | CI PEP8 | ![screenshot](/docs/testing/urls-python-hubspace-validation.jpg) | Pass: No Errors |
| views.py (hubspace) | CI PEP8 | ![screenshot](/docs/testing//views-python-hubspace-validation.jpg) | Pass: No Errors |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](/docs/testing/chrome-compatibility.jpg) | Works as expected |
| Firefox | ![screenshot](/docs/testing/firefox-compatibility.jpg) | Works as expected |
| Safari | ![screenshot](/docs/testing/safari-compatibility.jpg) | Works as expected |
| Edge | ![screenshot](/docs/testing/edge-compatibility.jpg) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Screenshot | Notes |
| --- | --- | --- |
| Mobile (DevTools) | ![screenshot](/docs/testing/mobile-responsiveness.jpg) | Works as expected |
| Tablet (DevTools) | ![screenshot](/docs/testing/tablet-responsiveness.jpg) | Works as expected |
| Desktop | ![screenshot](/docs/testing/desktop-responsiveness.jpg) | Works as expected |

## Lighthouse Audit

All pages were tested with [Google Chrome Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/). Testing was performed in private browsing mode and on the live website on Heroku.

| Page | Image |
| --- | --- |
| Home Page | ![Lighthouse Screenshot](/docs/testing/homepage-lighthouse.jpg) |
| All Articles Page | ![Lighthouse Screenshot](/docs/testing/all-articles-lighthouse.jpg) |
| My Articles Page | ![Lighthouse Screenshot](/docs/testing/members-articles-lighthouse.jpg) |
| Saved Articles Page | ![Lighthouse Screenshot](/docs/testing/saved-articles-lighthouse.jpg) |
| Article Detail Page | ![Lighthouse Screenshot](/docs/testing/article-detail-lighthouse.jpg) |
| Create Article Page | ![Lighthouse Screenshot](/docs/testing/create-article-lighthouse.jpg) |
| Edit Article Page | ![Lighthouse Screenshot](/docs/testing/edit-article-lighthouse.jpg) |
| Remove Article Page | ![Lighthouse Screenshot](/docs/testing/remove-article-lighthouse.jpg) |
| Profile Page | ![Lighthouse Screenshot](/docs/testing/profile-lighthouse.jpg) |
| Edit Profile Page | ![Lighthouse Screenshot](/docs/testing/edit-profile-lighthouse.jpg) |
| Remove Profile Page | ![Lighthouse Screenshot](/docs/testing/remove-profile-lighthouse.jpg) |
| Edit Comment Page | ![Lighthouse Screenshot](/docs/testing/edit-comment-lighthouse.jpg) |
| Remove Comment Page | ![Lighthouse Screenshot](/docs/testing/remove-comment-lighthouse.jpg) |
| Sign In Page | ![Lighthouse Screenshot](/docs/testing/sign-in-page-lighthouse.jpg) |
| Sign Out Page | ![Lighthouse Screenshot](/docs/testing/sign-out-page-lighthouse.jpg) |
| Sign Up Page | ![Lighthouse Screenshot](/docs/testing/sign-up-page-lighthouse.jpg) |

## Manual Testing

| Page | User | User Action | Expected Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| **Navigation Bar** | | | | |
| | Guest/Member | Click on Logo | Redirection to home page | Pass |
| | Guest/Member |  Click on "Articles" link | Redirection to all articles page | Pass |
| | Guest/Member |  Click on "Register" link | Redirection to the sign up page | Pass |
| | Guest/Member |  Click on "Login" link | Redirection to the sign in page | Pass |
| | Member |  Click on profile icon | Opens a dropdown menu | Pass |
| | Member |  Click on "My Profile" link | Redirection to the profile page | Pass |
| | Member |  Click on "My Articles" link | Redirection to the user's articles | Pass |
| | Member |  Click on "Saved Articles" link | Redirection to the user's saved articles | Pass |
| | Member |  Click on "Sign Out" link | Redirection to the sign out page | Pass |
| **Home Page** | | | | |
| | Guest/Member | Click on "Join Now" button | Redirection to sign up page | Pass |
| | Guest/Member | Click on one of the articles | Redirection to the article page | Pass |
| | Member | Be on the home page | Hero banner removed and article feed displayed | Pass |
| **Sign Up** | | | | |
| | Guest/Member | Enter valid email address | Field will only accept email address format | Pass |
| | Guest/Member | Enter valid password (twice) | Field will only accept password format | Pass |
| | Guest/Member | Click on "Sign Up" button | Redirects user to feed | Pass |
| | Guest/Member | Click on "Sign In" link | Redirects user to sign in page | Pass |
| **Sign In** | | | | |
| | Guest/Member | Click on "Sign In" button | Redirects user to feed | Pass |
| | Guest/Member | Click on "Sign Up" link | Redirects user to sign up page | Pass |
| **Log Out** | | | | |
| | Member | Click on "Sign Out" button | Redirects user to home page | Pass |
| **Profile** | | | | |
| | Member | Click on "Edit" button | User will be redirected to the edit profile page | Pass |
| | Member | Click on "Delete" button | User will be redirected to the delete profile page | Pass |
| **Delete Profile Page** | | | | |
| | Member | Click on "Delete" button | Profile will be permanently deleted | Pass |
| | Member | Click on "Cancel" button | User will be redirected to the profile page | Pass |
| **Edit Profle Page** | | | | |
| | Member | Fill in profile form and click on "Save" button | Profile will be edited and user redirected to the profile page | Pass |
| | Member | Click on "Cancel" button | User will be redirected to the profile page | Pass |
| **All Articles Feed** | | | | |
| | Guest/Member | Click on a article | User will be redirected to the individual article page | Pass |
| **Individual Article Page** | | | | |
| | Member | If user is the author | "Edit" and "Remove" buttons displayed | Pass |
| | Guest | If user isn't the author and a member | "Edit" and "Remove" buttons not displayed | Pass |
| | Member - Author | Click on "Delete" button | User will be redirected to the delete article page | Pass |
| | Guest/Member | Brute forcing the URL to delete another user's article | Error raised | Pass |
| | Member - Author | Click on "Edit" button | User will be redirected to the edit article page | Pass |
| | Guest/Member | Brute forcing the URL to edit another user's article | Error raised | Pass |
| | Member | Click the endorse icon on the article | Endorse icon will fill and the like count will increase by 1 | Pass |
| | Guest | Click the endorse icon on the article | Nothing happens | Pass |
| | Member | Click the bookmark icon on the article | Bookmark icon will fill and the article will be added to the saved list | Pass |
| | Guest | Click the bookmark icon on the article | Nothing happens | Pass |
| **Delete Article Page** | | | | |
| | Admin/Member - Author | Click on "Delete" button | Article will be permanently deleted | Pass |
| | Admin/Member - Author | Click on "Cancel" button | User will be redirected to the article page | Pass |
| **Edit Article Page** | | | | |
| | Admin/Member - Author | Fill in article form and click on "Save" button | Article will be edited and user redirected to the article page | Pass |
| | Admin/Member | Click on "Cancel" button | User will be redirected to the article page | Pass |
| **Comments** | | | | |
| | Guest/Member | Be on a individual article page | Comments count displayed | Pass |
| | Guest/Member | Be on a individual article page | Comments displayed | Pass |
| | Guest | Comments displayed | Add comment field hidden and message informing login in is required | Pass |
| | Member | Click on "Post" button | Comment is posted and comment count increased by 1 | Pass | 
| | Member | Click on "Post" button without a content| Error raised | Pass | 
| | Member - Comment Author | Click on "Delete" button | User will be redirected to the edit comment page | Pass |
| | Guest/Member | Brute forcing the URL to delete another user's comment | Error raised | Pass |
| | Member - Comment Author | Click on "Edit" button | User will be redirected to the edit comment page | Pass |
| | Guest/Member | Brute forcing the URL to edit another user's comment | Error raised | Pass |
| | Member | Click on "report" button on another's user comment | Comment flagged to the admin | Pass |
| **Delete Comment Page** | | | | |
| | Admin/Member | Click on the "Delete" button | Comment will be permanently deleted | Pass | 
| | Admin/Member | Click on the "Cancel" button | User will be redirected to the original comment | Pass | 
| **Edit Comment Page** | | | | |
| | Admin/Member | Fill in comment form and click on the "Save" button | Original comment will be edited | Pass | 
| | Admin/Member | Click on the "Cancel" button | User will be redirected to the original comment | Pass | 
| **"My Articles" Page** | | | | |
| | Member | Be on the "My Articles" page | Articles created by the user displayed | Pass |
| | Member | Click on a article | User will be redirected to the individual article page | Pass |
| **"Saved Articles" Page** | | | | |
| | Member | Be on the "Saved" Articles page | Articles saved by the user displayed | Pass | 
| | Member | Click on a article | User will be redirected to the individual article page | Pass |

## User Story Testing

The following are user stories I've implemented with screenshots accordingly. 

| User Story | Screenshot |
| --- | --- |
| As a user, I would like to be able to sign up, so that I can network with other users in the Eire Settlers community. | ![screenshot](/docs/features/sign-up-page.jpg) |
| As a user, I want to be able to log in and out so that I can protect my personal information, create new articles, and interact with other users through likes, comments, and saving articles. | ![screenshot](/docs/features/sign-in-page.jpg) |
| As a user when I log in, I want to be able to access the latest articles so I am up to date with the user's discussions. | ![screenshot](/docs/features/logged-in-homepage.jpg) |
| As a user, I need a profile where I can store info about me, my name, location, and nationality. | ![screenshot](/docs/features/profile-page.jpg) |
| As a user, I would like to be able to edit my profile when I want to make changes to my details. | ![screenshot](/docs/features/edit-profile-page.jpg) |
| As a user, I want to create an article so that I can share my thoughts or start discussions on topics of interest to me. | ![screenshot](/docs/features/create-article-page.jpg) |
| As a user, I want to be able to edit articles that I have previously published so that I can update and improve the content as needed. | ![screenshot](/docs/features/edit-article-page.jpg) |
| As a user, I want to be able to like articles posted by other users so that I can express appreciation or agreement with their contributions. | ![screenshot](/docs/features/endorse-article-button.jpg) |
| As a user, I want to be able to save articles that I find interesting or want to revisit late so that I can easily access and reference them at a later time. | ![screenshot](/docs/features/saved-articles.jpg) |
| As a user, I want to be able to create new comments, edit existing comments, and delete comments from articles so that I can engage with the content and express my thoughts effectively. | ![screenshot](/docs/features/manage-comments.jpg) |
| As a user, I want to be able to report comments that I believe violate the site's community guidelines so that I can notify the administrators of inappropriate content for review and potential removal. | ![screenshot](/docs/features/report-comment.jpg) |
| As a user, I would like the site to have a customized favicon so I can easily identify it when I have multiple tabs open. | ![screenshot](/docs/features/favicon-tab.jpg) |
| As a user, I can view and use the web app on all screen sizes so that I can change my device and access the app. | ![screenshot](/docs/features/desktop-mobile-design.jpg) |
| As a user, I would like a responsive navigation menu so that I can easily navigate from any device. | ![screenshot](/docs/features/desktop-mobile-navbar.jpg) |

The following are user stories I wasn't able to implement and have been set as Future Release on the [Kanban Board](https://github.com/users/tinobragaa/projects/3/views/1).

<details>
<summary>Future Release Issues</summary>
<br>

![screenshot](/docs/testing/future-release-issues.jpg)

</details>

| User Story | Status |Issue |
| --- | --- | --- |
| As a user, I want to be able to search for content and profiles so that I can easily find relevant information and connect with others. | Open | [Search Functionality](https://github.com/tinobragaa/eire-settlers/issues/29) |
| As a user, I want to be able to add tags to my content so that I can categorize it effectively and enhance its discoverability. | Open | [Articles Tag](https://github.com/tinobragaa/eire-settlers/issues/30) |
| As a user, I want to be able to add friends so that I can expand my social connections within the website's community. | Open | [Add Friends Functionality](https://github.com/tinobragaa/eire-settlers/issues/28) |
| As a user, I want to sign in with one of my social accounts so that I can sign in or sign up quickly and easily. | Open | [Social Media Login](https://github.com/tinobragaa/eire-settlers/issues/20#issue-2124208831) |
| As a User, I want to have the option to enable and use dark mode in the application so that I can reduce eye strain and enhance readability in low-light environments. | Open | [Dark Mode Feature](https://github.com/tinobragaa/eire-settlers/issues/23) |

## Bugs

`Bug`: CSS was not showing on deployed heroku app.
<br>
`Fix`: Fixed by setting DEBUG to False in settings.py and disabling collect static variable in Heroku.

`Bug`: Multiple NoReverseMatch error with links on the website.
<br>
`Fix`: Fixed by passing argument to the appropriate page on the link.

`Bug`: Default profile image not displaying.
<br>
`Fix`: Fixed by replacing link to default profile picture in profile models with 'placeholder' and adding an if statement to profile if the user's profile picture link is 'placeholder' the image will display the default picture and if not it will show the user's uploaded image.

`Bug`: Article containers were overlaying hamburguer menu on smaller screens devices.
<br>
`Fix`: Fixed by adding a z-index on the menu so it would be displayed on top of the articles.