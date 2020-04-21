from flask_migrate import MigrateCommand
from flask_script import Server
from application import manage, app
import www

manage.add_command('runserver', Server(port=app.config['SERVERPORT'], use_debugger=True, use_reloader=True))
manage.add_command('db', MigrateCommand)


def main():
    manage.run()


if __name__ == '__main__':
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()
