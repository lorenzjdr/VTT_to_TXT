from flask import Flask, request, render_template, send_file, jsonify
from files import Filing
import os
import re

app = Flask(__name__)

def sanitize_filename(filename):
    return re.sub(r'[^a-zA-Z0-9_\-]', '_', filename)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        vtt_file = request.files['vtt_file']
        output_filename = request.form['output_filename']
        
        if not vtt_file.filename.endswith('.vtt'):
            return render_template('index.html', error='Invalid file type. Please upload a .vtt file.')

        if vtt_file and output_filename:
            vtt_path = os.path.join('uploads', vtt_file.filename)
            vtt_file.save(vtt_path)
            Filing.openVTTFile(vtt_path)
            sanitized_filename = sanitize_filename(output_filename)
            output_path = os.path.join('outputs', f"{sanitized_filename}.txt")
            Filing.output(output_path)
            if os.path.exists(output_path):
                return send_file(output_path, as_attachment=True)
            else:
                return render_template('index.html', error='File not found')
    
    return render_template('index.html')

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    if not os.path.exists('outputs'):
        os.makedirs('outputs')
    app.run(debug=True)


