set -o errexit

pip install -r requirements.txt

python Mainapp/manage.py collectstatic --no-input
python Mainapp/manage.py migrate