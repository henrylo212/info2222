# The Next Messager

This project is for INFO2222 in Semester 1 2023. It consists of creating a
secure website that runs a basic text-messaging service.

## Hosting

To host this project for yourself, there are a few things you need to do:
1. Install all the python modules listed in `requirements.txt`. This can be
   achieved by running the command
   ```bash
   pip install -r requirements.txt
   ```
2. Set up a self-signed certificate and corresponding private key. [This
   guide](https://alexanderzeitler.com/articles/Fixing-Chrome-missing_subjectAltName-selfsigned-cert-openssl/)
   did the job for me. REMINDER: Do NOT push certificates or private keys to
   GitHub. There are some patterns in the `.gitignore` that should hopefully
   help reduce the chance of this happening.
3. Set your OS up to trust the certificate. How to do this is OS-specific, but
   typically there is a spot in the web-browser settings that will open up the
   right tool for you. If in doubt, there are plenty of guides online.
4. Make sure at least the backup database exists and has contents. If it
   doesn't, run the `make_backup_database.py` script to create it.
5. Set up the values in the `server_conf.json` file.
    - `BACKUP_DATABASE_PATH` and `DATABASE_FILE_PATH` should probably be left
      as they are, but they could be changed if you want to change where the
      database is stored.
    - `CERTIFICATE_PATH` and `PRIVATE_KEY_PATH` should point to the certificate
      and the private key that were created in step 2.
    - `HOST`, `PORT`, and `DEBUG` can probably stay unchanged, but they do
      exist if needed.
    - `DEFAULT_COMMANDS` can definitely stay unchanged; there's only one
      command so far anyway.
6. At this point you should be able to run `python run.py` and have the server
   start up on the configured host and port.
