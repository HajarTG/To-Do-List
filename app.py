from flask import Flask, render_template, request, url_for, redirect 
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
# Instantiate the Flask class by creating a flask application
app = Flask(__name__)
# Create the mongodb client
client = MongoClient('localhost', 27017)
# Get and Post Route
@app.route("/", methods=('GET', 'POST'))
def index():
    if request.method == "POST":   # if the request method is post, then insert the todo document in todos collection
        content = request.form['content']
        degree = request.form['degree']
        due_date = request.form.get('due_date')
        
        # Convert the date string to datetime object if it exists
        if due_date:
            due_date = datetime.strptime(due_date, '%Y-%m-%d').strftime('%Y-%m-%d')
        
        todos.insert_one({
            'content': content,
            'degree': degree,
            'due_date': due_date,
            'created_at': datetime.now(),
            'completed': False
        })
        return redirect(url_for('index')) # redirect the user to home page
    
    # Get filter parameter from URL
    priority_filter = request.args.get('filter', 'all')
    
    # Build the query
    query = {}
    if priority_filter != 'all':
        query['degree'] = priority_filter
    
    # Get todos with filters
    all_todos = todos.find(query).sort([
        ('completed', 1),
        ('created_at', -1)
    ])
    
    return render_template('index.html', todos=all_todos)

@app.post("/<id>/delete/")
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))

@app.post("/<id>/toggle/")
def toggle_complete(id):
    todo = todos.find_one({"_id": ObjectId(id)})
    if todo:
        todos.update_one(
            {"_id": ObjectId(id)},
            {"$set": {
                "completed": not todo.get('completed', False),
                "completed_at": datetime.now() if not todo.get('completed', False) else None
            }}
        )
    return redirect(url_for('index'))

db = client.flask_database # creating your flask database using your mongo client 
todos = db.todos # creating a collection called "todos"
# The dunder if __name__ code block
if __name__ == "__main__":
    app.run(debug=True) 
