# Flask Graphene Graphql
This is an example project for using [GraphQL](https://graphql.org/) with [Flask](http://flask.pocoo.org/) using [Graphene-SQLAlchemy](https://github.com/graphql-python/graphene-sqlalchemy).

**Table of contents**
- [Installing](#installing)
- [Setup the database](#setup-the-database)
- [Run the server](#run-the-server)
- [Hit the server](#hit-the-server)
    1. [Add a new user](#1-add-a-new-user)
    2. [List all users](#2-list-all-users)
    3. [Find a user by username](#3-find-a-user-by-username)
    4. [Update a user](#4-update-a-user)

## Installing
Use Virtualenv and install the packages.

```
git clone git@github.com:andrearampin/flask-graphene-graphql.git
cd flask-graphene-graphql
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

## Setup the database
```
cat struct.sql | sqlite3 data.db
```

## Run the server
```
python app.py
```

## Hit the server
Open on your browser the following URL [http://localhost:5000/graphql](http://localhost:5000/graphql)

### 1. Add a new user
```
mutation {
  createUser(name: "test", email: "hello@test.com", username: "testusername") {
    user {
      id,
      name,
      email,
      username
    }
    ok
  }
}
```

### 2. List all users
```
{
  allUsers {
    edges {
      node {
        name,
        email,
        username
      }
    }
  }
}
```

### 3. Find a user by username
```
{
  findUser(username: "testusername") {
    id,
    name,
    email
  }
}
```

### 4. Update a user
```
mutation {
  changeUsername(email: "hello@test.com", username:"testupdated") {
    user {
      name,
      email,
      username
    }
  }
}
```
