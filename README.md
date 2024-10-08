# DogAPI

## Description

DogAPI is a web service that allows users to manage and interact with dog-related data. This includes functionalities such as adding new dogs, voting on comments, and more.

The intent of this API is for learning purposes and fun.

The end goal is to hook up this API with a UX which show the created dogs in a kind of a big place so you can watch them. Also everytime you interact with those dogs they will change the behavior in real time in the UI.

The UI piece is not intended to be develop soon and only the API's are integrated now.

You can visit a live demo of this at (https://ingroca.dev/projects/dogapi/docs)

## Features
- Comments: Users can add comments to dogs.
- Votes: Users can vote on comments.
- CRUD Users: Manage user data with Create, Read, Update, and Delete operations.
- Auth via OAuth2 with JWT Token: Secure authentication using OAuth2 and JWT tokens.
- OpenAI: I use OpenAI to generate Json object representing dynamic data for the dogs, like traits and activity levels. 

## Technologies Used

- PostgreSQL: A powerful, open-source object-relational database system. [Learn more](https://www.postgresql.org/)
- Pydantic: Data validation and settings management using Python type annotations. [Learn more](https://pydantic-docs.helpmanual.io/)
- Jose: A JavaScript Object Signing and Encryption (JOSE) library for JWT tokens. [Learn more](https://python-jose.readthedocs.io/en/latest/)
- SQLAlchemy: The Python SQL toolkit and Object-Relational Mapping (ORM) library. [Learn more](https://www.sqlalchemy.org/)
- FastAPI: A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. [Learn more](https://fastapi.tiangolo.com/)
- NGINX: Is an HTTP and reverse proxy server, a mail proxy server, and a generic TCP/UDP proxy server. [Learn more] (https://nginx.org/en/)

## Requirements

- Python 3.x (Programming languaje)
- Uvicorn (Server)
- SQLAlchemy (ORM)
- PostgreSQL (Relational DB)
- Pydantic (Schema validation)
- Jose (JWT)
- Alembic (SQL Migrations)

## Installation

1. **Clone the repo:**

   ```sh
   git clone https://github.com/yourusername/dogapi.git

2. **Navigate to the project directory:**

   ```sh
   cd dogapi

3. **Install the requiered dependencies:**

   ```sh
   pip install -r requierements.txt


## Usage

1. **Activate the virtual environment**:
   Run the activate script located in the `scripts` directory.

   ```sh
   source scripts/activate

2. **Run the uvicorn server**:
   Start the server with the following command. Go to the root and execute the following

   ```sh
   uvicorn main:app --reload