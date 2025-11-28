# Recipe Sharing Platform

A Django-based web application for sharing and discovering recipes. Users can create, view, update, and delete recipes, leave comments, rate recipes, and add favorites.

## Features

- **User Authentication**: Registration and login using email (not username)
- **Recipe Management**: Full CRUD operations for recipes
- **Categories**: Organize recipes by categories
- **Comments & Ratings**: Users can comment and rate recipes
- **Favorites**: Save favorite recipes
- **Search**: Search recipes by title, description, or ingredients
- **User Profiles**: Customizable user profiles with bio and profile pictures

## Technical Requirements Met

✅ **Authorization & Registration**: Email-based registration, login, logout, password change  
✅ **Applications**: 2 apps (users, recipes)  
✅ **Models**: 5+ models (User, Profile, Recipe, Category, Comment, Rating)  
✅ **Relationships**: OneToMany (6), ManyToMany (1), OneToOne (1)  
✅ **CRUD Operations**: Full CRUD on Recipe model using ModelForms  
✅ **Signals**: Profile auto-creation, welcome email, recipe creation logging  
✅ **Pytest Testing**: 3+ tests included  
✅ **Management Command**: `create_sample_recipes` command  
✅ **UI/Design**: Bootstrap 5, base.html, visual forms  
✅ **Protected Pages**: Recipe creation/editing requires authentication  

## Installation

1. **Clone the repository**:
```bash
git clone <repository-url>
cd final_project
```

2. **Create a virtual environment**:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Run migrations**:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create a superuser** (optional, for admin access):
```bash
python manage.py createsuperuser
```

6. **Create sample data** (optional):
```bash
python manage.py create_sample_recipes
```

7. **Run the development server**:
```bash
python manage.py runserver
```

8. **Access the application**:
   - Open your browser and go to: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Project Structure

```
project/
├── config/              # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/               # User authentication app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── signals.py
│   └── tests.py
├── recipes/             # Recipes app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── signals.py
│   ├── tests.py
│   └── management/
│       └── commands/
│           └── create_sample_recipes.py
├── templates/           # HTML templates
│   ├── base.html
│   ├── users/
│   └── recipes/
├── static/              # Static files (CSS, JS, images)
├── media/               # User uploaded files
├── db.sqlite3           # SQLite database
├── manage.py
└── requirements.txt
```

## Models & Relationships

### Models:
1. **User** (Custom, email-based)
2. **Profile** (OneToOne with User)
3. **Category**
4. **Recipe** (ForeignKey to User and Category, ManyToMany with User for favorites)
5. **Comment** (ForeignKey to Recipe and User)
6. **Rating** (ForeignKey to Recipe and User)

### Relationships:
- **OneToMany**: User → Recipe, User → Comment, User → Rating, Category → Recipe, Recipe → Comment, Recipe → Rating
- **ManyToMany**: Recipe ↔ User (favorites)
- **OneToOne**: User ↔ Profile

## Testing

Run tests using pytest:
```bash
pytest
```

Or run specific test file:
```bash
pytest users/tests.py
pytest recipes/tests.py
```

## Management Commands

Create sample recipes:
```bash
python manage.py create_sample_recipes
```

## Deployment on Render.com

1. Push your code to GitHub
2. Connect your GitHub repository to Render.com
3. Create a new Web Service
4. Configure:
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Start Command**: `gunicorn config.wsgi:application`
5. Add environment variables:
   - `SECRET_KEY`: Your Django secret key
   - `DEBUG`: False (for production)
6. Deploy!

## License

This project is created for educational purposes.





