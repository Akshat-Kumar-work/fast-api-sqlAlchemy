# Create a virtual environment
```
python -m venv venv
```

# Activate the virtual environment in PowerShell
```
.\venv\Scripts\activate
```

# Or in CMD
```
venv\Scripts\activate.bat
```


# Install required packages
```
pip install fastapi
```
```
pip install uvicorn[standard]
```

# To start the server using uvicorn
```
uvicorn main:app --reload
```

# Install sql alchemy
```
pip install sqlalchemy
```

# Install alembic
```
pip install alembic
```

# Initalize alembic
```
alembic init alembic
```

# Configure alembic env.py

# Install
pip install psycopg2

# to migrate schema
alembic revision --autogenerate -m "you message"

# check latest migration
alembic heads

# to apply schema changes to db
alembic upgrade head

# to load env
. .\load_env.sh
or
. ./load_env.sh








