# Notifier 
This a notification app in which notifications which are sent via emails.<br />
This project was created using Django framework. It uses HTML, CSS and Bootstrap for frontend.

## Set up of the project

In the project directory, you can run below steps to set up the project in your local machine :

### `python manage.py make migrations` 

With the model created, the first thing you need to do is create a migration for it.

You can do this with the above command

### `python manage.py migrate` 

You have now created the migration, but to actually make any changes in the database, you have to apply it with the<br />
management command migrate

Migration is to create the necessary tables in the database

### `python manage.py runserver` 

Runs the app in the development mode. <br />
Open [http://127.0.0.1:8000/mysite/login/](http://127.0.0.1:8000/mysite/login/) to view it in the browser.

You can reload the page if you want to notice the edits done in the code instead of restarting the server again. <br />
You will also see errors in the console. (if any)


## Resources

For frontend (HTML, CSS, Bootsrap) : [W3Schools](https://www.w3schools.com/) and [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/)

For User Authentication : [User Authentication](https://docs.djangoproject.com/en/3.1/topics/auth/default/)

Login and registration pages : [Youtube video](https://www.youtube.com/watch?v=tUqUdu0Sjyc&t=644s)

For sending email : [send email](https://docs.djangoproject.com/en/3.1/topics/email/).
