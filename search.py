import csv
import difflib
# from fuzzywuzzy import fuzz
# from fuzzywuzzy import process
import json
from flask import Flask
from flask import request


app = Flask(__name__)

name = []
with open('word_search.tsv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t')
    for row in reader:
        # append your lists
        name.append(row['name'])


print(len(name))


@app.route("/search")
def get_matches():
    print(request.args.get('word'))
    results = difflib.get_close_matches(request.args.get('word'), name, 10, 0.9)
    return json.dumps(results)


if __name__ == '__main__':
    app.run(debug=True)

