from django.core.management import BaseCommand
from config.settings import PAD_DATABASE,USER,PASSWORD,HOST,PORT,DATABASE
import psycopg2

class Command(BaseCommand):
    def handle(self, *args, **options):
        connectString = f"""
            dbname={PAD_DATABASE}
            user={USER}
            password={PASSWORD}
            host={HOST}
            port={PORT}
        """

        try:

            conn = psycopg2.connect(connectString)
            conn.autocommit = True


            cursor = conn.cursor()

            cursor.execute(f"CREATE DATABASE {DATABASE}")
        except psycopg2.Error as ex:
            print(f"Произошла ошибка: {ex}")
        else:
            print("База данных создана успешно")


