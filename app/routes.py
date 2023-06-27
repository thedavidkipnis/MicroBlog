# DAVID KIPNIS
# 06/26/2023
# Micro Blog - Application

from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello world!"
