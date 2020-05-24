# game-picker-server

Checking out python, django and graphene. Making a GraphQL API to choose a random game based on some light criteria. Cuz you know. Who wants to pick the boardgame.

Loosely following this tutorial https://www.howtographql.com/graphql-python/3-mutations/

GraphiQL: http://localhost:8000/graphql

```
source venv/bin/activate
python manage.py runserver
```

Make a topic:
```
python manage.py startapp games
```

Change models:
```
python manage.py makemigrations
python manage.py migrate
```

Seed models (for a model called 'Link'):
```
python manage.py shell

from links.models import Link
Link.objects.create(url='https://www.howtographql.com/', description='The Fullstack Tutorial for GraphQL')
Link.objects.create(url='https://twitter.com/jonatasbaldin/', description='The Jonatas Baldin Twitter')
```


