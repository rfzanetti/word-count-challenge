# word-count-challenge
This project was built using Django and implements the Word Count Coding Challenge and it contains a single page with a form containing a text box and a submit button. When the user clicks on that button, a request is sent to the back-end that counts the number of words in the box.

## Installing and running the project

To run the project, follow these next steps:

### Prerequisites
- Python 3 installed
- Pip package manager installed

### Steps
1. Create a new Python virtual environment, activate it and install the required packages:

    ```shell
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2. Run the migrations for Django Waffle (or, to run all migrations, omit the `waffle` in the end, but it is unncecessary):

    ```shell
    python manage.py migrate waffle
    ```

3. Run the server:

    ```shell
    python manage.py runserver
    ```

4. Finally, go to `localhost:8000` in your browser and check the project.

## Activating cache use

This application uses an Waffle switch to determine whether to cache the results. 

*Important note*: This feature was created because the test requirements are most front-end based, so since this is part of a back-end job application, I decided to add a feature focused on the backend. Also it is important to notice that this feature wouldn't make sense in real world scenario.

To activate the switch for the first time, run:

    ```shell
    python manage.py waffle_switch WORD_COUNT_CACHE on --create
    ```

To activate/deactivate it once it was created, run:

    ```shell
    python manage.py waffle_switch WORD_COUNT_CACHE {on/off}
    ```

## Running tests

The application unit tests can be run with:

    ```shell
    python manage.py test
    ```
