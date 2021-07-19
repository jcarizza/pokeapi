GREEN='\033[0;33m'

echo "${GREEN}Running black formater..."
black --line-length=79 .

echo "${GREEN}Running flake8..."
flake8

echo "${GREEN}Running tests..."
pytest
