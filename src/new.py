from flask import request, render_template_string

@app.route('/example')
def example():
    username = request.args.get('username')
    template = f"<p>Hello {username}</p>"
    return render_template_string(template) # Noncompliant
