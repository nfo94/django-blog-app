### Blog app with Django

This project was done following the [Django 4 by Example](https://www.amazon.com.br/Django-Example-powerful-reliable-applications/dp/1801813051?gclid=Cj0KCQiAutyfBhCMARIsAMgcRJSKdN3swVShdxHO05naBb9kclp2t8RQ-oTZldJRpXiJgpRouiRLZEMaArskEALw_wcB)
book.

A few takes after some time studying Django:

- Way steeper learning curve if compared to Flask and FastAPI. Many things are already implemented,
  like many views, simple authentication, an entire admin dashboard, etc. At the same time, you need
  to learn how to actually use those things.
- Either used with the built in templating system or used with a real frontend framework, plus Django
  Rest Framework
- Widely used by enterprises.

#### Notes from the book

> The responsibilities in the Django MTV pattern are divided as follows:
>
> - Model: Defines the logical data structure and is the data handler between the database and
>   the View.
> - Template: Is the presentation layer. Django uses a plain-text template system that keeps
>   everything that the browser renders.
> - View: Communicates with the database via the Model and transfers the data to the Template
>   for viewing".
