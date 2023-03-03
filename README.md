### Blog app with Django

This project was done following the [Django 4 by Example](https://www.amazon.com.br/Django-Example-powerful-reliable-applications/dp/1801813051?gclid=Cj0KCQiAutyfBhCMARIsAMgcRJSKdN3swVShdxHO05naBb9kclp2t8RQ-oTZldJRpXiJgpRouiRLZEMaArskEALw_wcB)
book.

A few takes after some time studying Django:

- Way steeper learning curve if compared to Flask and FastAPI. Many things are already implemented,
  like some views, simple authentication, an entire admin dashboard, a built in ORM, etc. At the
  same time, you need to learn how to actually use those pre-built things.
- You need to remember to keep registring some constants in `settings.py`. A bit of a nuisance, but
  understandable considering how it works (we're actually buying time).
- It seems that it's either used with the built in templating system or used with a real frontend
  framework plus Django Rest Framework. The templating system is basically like Jinja, but, as a
  frontender-turned-fullstack, I just don't like templating systems (but I understand how they can
  speed things up for simple UIs).
- Widely used by big enterprises, and I can see why. This framework is robust, with manny things
  already solved and it's been around since 2005. I'd consider a few things before choosing it: does
  anyone on the team already knows Django and can ramp up others? Is our client another business?
  How big is the product? And things like that. Nonetheless, I'm inclined to use FastAPI because of
  autodocumentation, easy of use, shallow learning curve, async/type hints built in support, but
  anyway, I'm still just a noob.

#### Notes from the book

> The responsibilities in the Django MTV pattern are divided as follows:
>
> - Model: Defines the logical data structure and is the data handler between the database and
>   the View.
> - Template: Is the presentation layer. Django uses a plain-text template system that keeps
>   everything that the browser renders.
> - View: Communicates with the database via the Model and transfers the data to the Template
>   for viewing.

How Django works:

![Django 4 by Example](./Django%204%20by%20Example.png)

#### Running the blog app

To run this app clone it on your machine and then create a virtual environment:

```bash
python3 -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Enter project folder:

```bash
cd mysite
```

Run server:

```bash
python manage.py runserver
```
