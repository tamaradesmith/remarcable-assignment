## Django Server Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```  

2. Install Django and other dependencies:
   ```bash
   pip install django djangorestframework
   ```    

3. Run migrations:
  inside the API directory run:

    ```bash
    python3 manage.py migrate
    ``` 

4. Create a superuser to access the admin panel:
   ```bash
   python manage.py createsuperuser
   ```    

5. Start the development server:
   ```bash
   python manage.py runserver     
   ```

6. Visit http://127.0.0.1:8000/ in your browser.


## Seeding the Database

To populate the database with initial data, run the custom Django seed command:

```bash
  python manage.py seed
```

This will add sample products, categories, and tags for development and testing.

---


## Remix App Setup

1. Go to the Remix app directory:
   ```bash
   cd ../app
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

4. Visit http://localhost:5173/ in your browser.


## Notes

- I used AI to help with writing the readme and setup guide.
- As Django is not my primary framework and have not worked with it a lot, I used AI to help with some of the backend code.  I write most of the code my self but asked for help with understanding some of the Django specific syntax and best practices.
