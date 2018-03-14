# Example UWSGI Application

This Django 2 note-taking app is designed to be used to demonstrate UWSGI in combination with NGINX.

### Dependencies

To run this application you'll need the following:

* [Python 3][1]
* [Pipenv][2]
* MySQL/MariaDB Client & Shared Libraries (for compiling the native database client package)
* Access to a MySQL/MariaDB Database

### Usage

The `Makefile` provides a few helper tasks to make setting up the application a little easier than it might otherwise be. Here are the tools at your disposal:

* `make install` - Creates a virtualenv local to the project and installs the Python dependencies.
* `make service` - Creates a `notes.uwsgi` systemd service to run the application. Assumes use with NGINX and changes ownership of application to `nginx:nginx`
* `make migrate` - Migrates the database. This is the default task.
* `make static` - Gathers all static assets to `/var/www/$NOTES_HOST/`

### Environment Variables

*Note:* for `make db_init` you'll need to have some environment variables set before running the command:

* `NOTES_DB` - The name of the database you've created.
* `NOTES_DB_USER` - The database user that the application will use.
* `NOTES_DB_PASSWORD` - The database user's password.

If no other values are set, then it is assumed that the database is on the same server. Here are optional environment variables when running the database on a separate server:

* `NOTES_DB_HOST` - The domain or IP address of the server housing the database.
* `NOTES_DB_PORT` - Defaults to `3306`, but you can set this if you're using a non-standard MySQL port.

For the running of the application, you'll want to set the following `HOST` related environment variables or the application will default to `notes.example.com`:

* `NOTES_HOST` - The application's primary hostname, and the destination for static assets at `/var/www/$NOTES_HOST/`
* `NOTES_ALLOWED_HOSTS` - All of the host names that Django should except traffic for. Defaults to `$NOTES_HOST`, `localhost`, and `127.0.0.1`.

[1]: https://www.python.org
[2]: https://docs.pipenv.org
