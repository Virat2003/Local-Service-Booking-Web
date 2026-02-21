set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

python manage.py shell << END
from account.models import User
user = User.objects.get(username="viratadmin")
user.set_password("viratadmin@11")
user.is_staff = True
user.is_superuser = True
user.save()
END