from flask import Flask, redirect, render_template_string, url_for
import subprocess
from flask import request 


app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head><title>Redirect Example</title></head>
        <body>
            <h1>Welcome to the Home Page</h1>
            <p>Click the button below to go to the Sample Page:</p>
            <form action="/sample">
                <button type="submit">Go to Sample Page</button>
            </form>
        </body>
    </html>
    """

@app.route('/sample')
def sample_page():
    return """
    <html>
        <head><title>Sample Page</title></head>
        <body>
            <h1>Welcome to the Sample Page</h1>
            <p>You reached this page by clicking the button on the Home Page!</p>
        </body>
    </html>
    """

@app.route('/run_program', methods=['GET', 'POST'])
def run_program():
    output = ""
    if request.method == 'POST':
        # Assuming you have some logic to capture answers from the form
        question1_answer = request.form.get('question1', '')
        question2_answer = request.form.get('question2', '')
        
        # Here, you would run your program and capture the output
        try:
            result = subprocess.run(['python3', 'Arrays & Hasing/duplicate.py'], capture_output=True, text=True, check=True)
            output = result.stdout
        except subprocess.CalledProcessError as e:
            output = f"Error: {e.stderr}"

    return render_template_string("""
    <html>
        <head>
            <title>Program Output</title>
            <style>
                body {
                    display: flex;
                    flex-direction: row;
                    height: 100vh;
                    margin: 0;
                }
                .left-panel, .right-panel {
                    width: 50%;
                    padding: 20px;
                    box-sizing: border-box;
                }
                .left-panel {
                    background-color: #f4f4f4;
                }
                .right-panel {
                    background-color: #e9e9e9;
                }
                pre {
                    white-space: pre-wrap;
                    word-wrap: break-word;
                    background: #333;
                    color: white;
                    padding: 10px;
                }
                form {
                    display: flex;
                    flex-direction: column;
                    gap: 10px;
                }
            </style>
        </head>
        <body>
            <div class="left-panel">
                <h2>Questions</h2>
                <form method="POST">
                    <label for="question1">Question 1: What is your name?</label>
                    <input type="text" id="question1" name="question1" required>
                    
                    <label for="question2">Question 2: What is your favorite color?</label>
                    <input type="text" id="question2" name="question2" required>
                    
                    <button type="submit">Run</button>
                </form>
            </div>
            <div class="right-panel">
                <h2>Output</h2>
                {% if output %}
                    <p>Program Output:</p>
                    <pre>{{ output }}</pre>
                {% endif %}
            </div>
        </body>
    </html>
    """, output=output)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
