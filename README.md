# quickbase

> API REST implemented with Django to manage Customers - Products - Bills system. Authentication using JWT

## Build setup

``` bash
# Start virtual environment and activate

python3 -m venv venv
source venv/bin/activate

# Clone the proyect inside virtual env folder
git clone git@github.com:Gabospa/quickbase.git

# Install dependencies. Run the following command

pip install -r requirements.txt

# Create migrations and apply them

python manage.py makemigrations
python manage.py migrate

# Start server, by default on http://localhost:8000

python manage.py runserver

```
## API Documentation
Loot at here for detailed documentation!

https://documenter.getpostman.com/view/13014433/TWDUoxXJ



