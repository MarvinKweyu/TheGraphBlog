# TheGraphBlog

> A django graphql blogging application

### Development setup

Clone the repository, install requirements and run the server

```bash
pip install -r requirements.txt
python manage.py runserver

```

For the API : `http://127.0.0.1:8000/graphql`


A sample query to get all posts:
```graphql

{
  allPosts {
    title
    subtitle
    author {
      user {
        username
      }
    }
    tags {
      name
    }
  }
}
```

Project guide: `https://realpython.com/python-django-blog/`

GraphQL guide: `https://docs.graphene-python.org/projects/django/en/latest/installation/`