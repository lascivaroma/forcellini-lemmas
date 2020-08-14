from flask import Flask, render_template, jsonify, send_file, request
import os.path


from .schema import FIELDS, create_index, perform_search, paginate


_base = os.path.dirname(os.path.abspath(__file__))
_templates = os.path.join(_base, "templates")
_statics = os.path.join(_base, "statics")


app = Flask(__name__, template_folder=_templates, static_folder=_statics)


@app.template_filter("read_pagination")
def read_pagination(pages):
    return zip(pages, [0] + pages)


@app.cli.command("create-index")
def create():
    print("Writing...")
    create_index()
    print("Done")


@app.route("/", methods=["GET"])
def index():
    page = request.args.get('p', 1)
    if not isinstance(page, int) and page.isnumeric():
        page = int(page)
    else:
        page = 1

    query = request.args.get('q', "")

    results = perform_search(
        query=query,
        page=page
    )
    return render_template(
        "index.html",
        results=results,
        current_page=results["pages"]["current"],
        pagination=paginate(
            current_page=results["pages"]["current"],
            total_pages=results["pages"]["last"],
            max_pages=10
        ),
        query=query,
        fields=FIELDS
    )


@app.route("/favicon.ico")
def favicon():
    return send_file(os.path.join(_base, "..", "favicon.ico"))

@app.route("/api/data")
def api_json():
    page = request.args.get('page', 1)
    query = request.args.get('q', "")
    return jsonify(perform_search(query, page))
