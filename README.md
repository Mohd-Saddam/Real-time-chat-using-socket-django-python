
This is the Task:
Create User
A user can sign up with the following property:
Full Name, Email, Phone, Gender, Country, Password, and interests(should have the option to select multiple interests)
A user can log in using a combination of Phone or Email and a password.

Make Connection
After login/Signup one toggle should be there to make them online or offline.
There should be one button for connecting to another user. After clicking on that button, I should find another user who is online.
Connection logic:
One person can connect with only one person at a time.
First, find users with interests, if there is no person who matches with interests, connect with anyone who is online.
After connection, show the user name, gender, and country details to each other
Connection should happen using a socket.
Users can chat with each other after connection (Optional)



Set Up a Virtual Environment (optional but recommended) Create a virtual environment to isolate the project dependencies:

python -m venv env

Activate the virtual environment:

For Windows: env\Scripts\activate For macOS/Linux: source env/bin/activate

Install Dependencies Install the project dependencies using pip: pip install -r requirements.txt

Apply the database 
# I have added admin already use this url http://localhost:8000/admin 
# You can use below credentials for login as a admin
# username=admin
# password=1234
migrations: python manage.py makemigrations 
python manage.py migrate

Create a superuser to access the admin interface:

python manage.py createsuperuser

Run the Server Start the Django development server:

python manage.py runserver
Open your web browser and go to http://localhost:8000/ to access the application.
