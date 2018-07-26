# Y2 2018 Summer: Forms Lab

Welcome to the forms lab! Please read all the instructions so you don't
get lost halfway through, but definitely feel free to ask for help if you
get stuck. Good luck, and have fun!

## Lecture Exercises

### Part 0: Setup

Before you start coding, make sure you clone the repository for this lab:
```
cd ~/Desktop
git clone https://github.com/meet-projects/y2s18-routing.git
cd y2s18-routing
subl lab &
```

### Part 1: Routing Review

In `app.py`, add a route to `/add` to return the `add.html` template.

### Part 2: HTTP Methods

Edit your method for the route to `/add` so that it takes both GET and
POST requests.

If a GET request comes in, return the `add.html` template like before,
but if a POST request comes in, print `'Received POST request!'`
(remember `print` statements?) and then return the same template.

### Part 3: Creating a Form

In the `add.html` template, between the `<form>` tags, add two `<input>`
tags, one with `name=student_name` and one with `name=student_year`.
Add one more `<input>` tag, this time with `type=submit` and `value=Submit`.

### Part 4: POSTing Forms

Now we need to add to the POST method of the `/add` route we have created
in `app.py`. If the request is a POST request, add the information from
the article to the database.

*Hint*: The `name` of the form element corresponds to the value of that
element in `request.form`.

## Independent Lab


### Part 2: Deleting an article

1. In `article.html`, add a `<form>` tag somewhere that has one `<input>`
element with `type="submit"` and `value="delete"`. Edit the form element
so that when submitted, it makes a POST to `/delete/<article_id>`, where
the `article_id` is of the article currently being viewed. *Hint*: You
will need to change the `action` and `method` attributes of `<form>`.

2. In `app.py`, create a new route to `/delete/<int:article_id>` that
only accepts POST requests.

3. In the new route, use the database functions you've already created to
delete the article with the given `article_id`.

4. Then redirect the user back to the home page by returning the home page
using one of the Flask functions we've learned.

### Part 3: Editing an article (BONUS)

1. At this point, you're done with the forms lab! If you have a lot of
extra time or want to challenge yourself further, this section
has another forms-related task. Otherwise, feel free to skip ahead to
Part 4: Making it colorful.

2. For this part, you'll need to create a new template called `edit.html`.
Make sure you place it in the `templates` folder!

3. Add a form to this new template for editing the article rating. What
information is necessary to edit the database entry? *Hint*: It's less than
you need to add a new entry.

4. In `app.py`, add a new route to `/edit/<int:article_id>`. When a GET
request is made to this route, it should return the template we just made.
When a POST request is made to this route, it should make a database call
to update the given entry and then return the article page.

5. In `article.html`, add a link to the new route for editing. You should now
be able to navigate the website and add new articles, delete articles, and
update ratings on existing articles!

### Part 4: Making it colorful

1. Congratulations on finishing the forms lab!

2. You can now make your website look prettier using CSS and additional
templating, as you've learned in the past few days.
