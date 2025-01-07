
from flask import Flask, render_template, request, redirect, url_for, flash
import networkx as nx

app = Flask(__name__)
app.secret_key = "secret-key"

# Knowledge graph
knowledge_graph = nx.Graph()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    """Add nodes to the knowledge graph."""
    if request.method == 'POST':
        node_name = request.form.get('node_name')
        if node_name:
            if node_name not in knowledge_graph:
                knowledge_graph.add_node(node_name)
                flash(f'Node "{node_name}" added successfully!')
            else:
                flash(f'Node "{node_name}" already exists in the knowledge graph.')
            return redirect(url_for('index'))
        else:
            flash('Node name cannot be empty!')
    return render_template('add.html')

@app.route('/find', methods=['GET', 'POST'])
def find():
    """Check if a node exists in the knowledge graph."""
    if request.method == 'POST':
        node_name = request.form.get('node_name')
        if node_name:
            if node_name in knowledge_graph:
                flash(f'Node "{node_name}" is present in the knowledge graph.')
            else:
                flash(f'Node "{node_name}" is not found in the knowledge graph.')
            return redirect(url_for('index'))
        else:
            flash('Node name cannot be empty!')
    return render_template('find.html')

@app.route('/view')
def view():
    """Display all nodes in the knowledge graph."""
    nodes = list(knowledge_graph.nodes)
    return render_template('view.html', nodes=nodes)

if __name__ == '__main__':
    app.run(debug=True)
