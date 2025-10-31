!!!GIT BASH SCRIPT!!!
# 1. создаём корневую папку проекта (если ещё нет)
mkdir my_project && cd my_project

# 2. создаём основную структуру
mkdir src tests

# 3. создаём подкаталоги в src
mkdir src/pages src/models src/utils

# 4. создаём файлы внутри src
touch src/__init__.py
touch src/pages/__init__.py src/pages/main_page.py
touch src/models/__init__.py src/models/models.py
touch src/utils/__init__.py src/utils/helpers.py

# 5. создаём файлы тестов
touch tests/__init__.py tests/test_login.py tests/test_cart.py

# 6. создаём корневые файлы проекта
touch requirements.txt README.md .gitignore
