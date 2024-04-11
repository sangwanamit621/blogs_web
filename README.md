# Blogs Web Application

Welcome to the Blogs Web Application! This project is a full-fledged web platform designed for managing blogs, posts, and comments. It provides a user-friendly interface for users to interact with various features such as registering accounts, creating posts, commenting on posts, and managing profiles. Token-based authentication is employed to ensure secure access to the application's functionalities.


## Features

* __User Authentication:__ Seamless registration and login system for users, ensuring secure access to the application.
* __Post Management:__ Users can effortlessly create, update, delete, and view posts with intuitive user interfaces.
* __Commenting System:__ Interactive commenting system enables users to engage with posts by adding, editing, and deleting comments.
* __Token-Based Authentication:__ Robust token-based authentication mechanism safeguards user accounts and sensitive data.
* __Permissions:__ Fine-grained permissions system ensures that only authorized users can perform certain actions, such as editing or deleting posts/comments.


## Technologies Used

* __Python:__ Versatile programming language used for backend development.
* __Django:__ High-level Python web framework for rapid development and clean design.
* __Django REST Framework (DRF):__ Powerful toolkit for building Web APIs in Django, providing serialization and authentication capabilities.
* __SQLite:__ Lightweight and easy-to-use relational database management system.
* __Postman:__ Collaborative API development platform for testing and documenting APIs.
* __JSON Web Tokens (JWT):__ Standard for securely transmitting information between parties as a JSON object.


## Installation

1. Clone the repository:
    ```
    git clone https://github.com/sangwanamit621/blogs_web.git
    ```

2. Navigate to the project directory:
    ```
    cd blogs_web
    ```

3. Allow the permission of execution to shell-scripts
    ```
    sudo chmod +x shell_scripts/setup_project.sh
    ```

4. Execute the setup_project.sh file to setup the project
    ```
    ./shell_scripts/setup_project.sh 
    ```

5. Execute the below command to run the server
    ```
    python3 manage.py runserver 
    ```

6. Access the application in your web browser at http://localhost:8000.

## Usage

* Register a new account or log in with existing credentials.
* Create, edit, or delete posts.
* Comment on posts and interact with other users.
* Manage your profile details and change your password.


## API Endpoints

Check out the full list of API endpoints and their functionalities in the <a href="https://github.com/sangwanamit621/blogs_web/blob/84c22e4a8c1b7fd9466a843f2b65211d75d936ba/API%20docs/API_DOCS.md">API documentation</a>.



