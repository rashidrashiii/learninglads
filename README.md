LearningLads
------------
![LearningLads](https://socialify.git.ci/rashidrashiii/learninglads/image?language=1&name=1&owner=1&stargazers=1&theme=Light)



LearningLads is an open-source project made with Django framework, designed to enhance collaborative learning among students. It empowers students to sign up, create chat rooms with specific topic names, engage in discussions, and share knowledge with others. Additionally, users can personalize their profiles, report issues or other users with screenshots, and administrators have access to a comprehensive admin dashboard. This is a public chat room where all users can view recent activities.

Installation
------------

Follow these steps to set up the LearningLads project on your local development environment.

### Prerequisites

Ensure you have the following dependencies installed on your system:

*   Python 3.7+
*   Django 3.2+
*   pip (Python package manager)
*   Virtualenv (optional but recommended)

### Clone the Repository

1.  Open your terminal or command prompt.
2.  Navigate to the directory where you want to store the project files.
3.  Clone the LearningLads repository by running the following command:

    git clone https://github.com/rashidrashiii/LearningLads.git


### Set Up Virtual Environment (Optional)

It's a good practice to create a virtual environment to isolate project dependencies. If you don't have virtualenv installed, you can install it using `pip`:

    pip install virtualenv

Create a virtual environment and activate it:

On Windows:

    venv\Scripts\activate

On macOS and Linux:

    source venv/bin/activate

### Install Dependencies

While inside your virtual environment (if you created one), install the project dependencies:

    pip install -r requirements.txt

### Database Setup

1.  Apply database migrations to set up the database schema:

    python manage.py migrate

2.  Create a superuser account to access the admin dashboard:

    python manage.py createsuperuser

Follow the prompts to create your admin account.

### Run the Development Server

Start the development server to run the LearningLads project locally:

    python manage.py runserver

You can access the project at [http://localhost:8000](http://localhost:8000) in your web browser.

Usage
-----

LearningLads provides a platform for students to engage in discussions, create chat rooms, and collaborate on various topics. Here are some key features:

*   **User Registration**: Students can sign up for an account.
*   **Profile Customization**: Users can customize their profiles by adding profile pictures and bios.
*   **Chat Rooms**: Users can create chat rooms with topic names and invite others to join the discussion.
*   **Reporting**: Users can report issues or other users to the admin, along with attaching screenshots for reference.
*   **Admin Dashboard**: Admins have access to an admin dashboard with user details and reported issues.
*   **Public Chat Room**: The platform features a public chat room where everyone can see recent activities and join discussions.

Contributing
------------

We welcome contributions from the open-source community. If you'd like to contribute to the project, please follow our [Contributing Guidelines](CONTRIBUTING.md).

License
-------

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Contact
-------

If you have any questions, feedback, or issues related to LearningLads, feel free to contact us at [rashiofficialemail@gmail.com](mailto:rashiofficialemail@gmail.com).

Happy Learning with LearningLads! 📚👨‍🎓👩‍🎓

* * *



Project Screenshots
-------------------

![Screenshot 1](https://github.com/rashidrashiii/learninglads/blob/main/static/images/screenshoteasy%20(1).png)
![Screenshot 2](https://github.com/rashidrashiii/learninglads/blob/main/static/images/screenshoteasy%20(2).png)
![Screenshot 3](https://github.com/rashidrashiii/learninglads/blob/main/static/images/screenshoteasy%20(3).png)
![Screenshot 4](https://github.com/rashidrashiii/learninglads/blob/main/static/images/screenshoteasy%20(4).png)
