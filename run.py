from flaskblog import create_app
app = create_app()
app.app_context().push()
@app.route('/')
def index():
    try:
        # Code that might cause the exception
        # For example, accessing a database or performing an operation that could fail
        result = 1 / 0  # This will cause a ZeroDivisionError
    except Exception as e:
        # Handle the exception
        error_message = f"An exception occurred: {e}"
        return render_template('error.html', error_message=error_message)

if __name__ == '__main__':
        app.run(debug=False)
         

        