# Digital Certificate Builder

This is a study purpose project. The main goal was work with file hashes and
digital certificate building through ficticious certificate authorities.

Warning: this is intented to be run only locally. Uncomment SECRET_KEY in settings file
to ensure the project works correctly. If you intend to use this in production environment
please generate a new SECRET_KEY.

# How to run

Install python virtualenv package:
```make dependencies```

Setup python virtual environment and install project dependencies:
```make setup```

Run server:
```make run```

# Clean workspace
To remove python virtual environment and cached files, run:
```make clean```


# Validation

File hashes and certificates can be validated in:

https://www.fileformat.info/tool/hash.htm

https://report-uri.com/home/pem_decoder


