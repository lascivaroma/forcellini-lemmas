import os
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh.qparser import QueryParser, MultifieldParser
from whoosh import index
import math


automatic = True  # Set to false if you want to fine tune things
_base = os.path.dirname(os.path.abspath(__file__))
_indexdir = os.path.join(_base, "indexdir")


def parse(file=os.path.join(_base, "..", "dictionary.tsv")):
    data = []
    with open(file) as f:
        for line_no, line in enumerate(f):
            line = line.strip().split("\t")
            if line_no == 0:
                header = line
            else:
                data.append(dict(zip(header, line)))
    return header, data


FIELDS, DATA = parse()
PAGELEN = 100

if automatic:
    schema = Schema(**{
        header: TEXT(stored=True)
        for header in FIELDS
    })
else:
    schema = Schema()


def create_index(data=DATA, _schema=schema):
    if not os.path.exists(_indexdir):
        os.mkdir(_indexdir)
    ix = index.create_in(_indexdir, _schema)

    writer = ix.writer()

    for elem in data:
        writer.add_document(**elem)
    writer.commit()

    return ix


if os.path.isdir(_indexdir):
    search_index = index.open_dir(_indexdir)
else:
    print("WARNING: no search index")
    search_index = None


def full(page=1):
    max_pages = math.ceil(len(DATA) / PAGELEN)
    if page < 1:
        page = 1
    elif page > max_pages:
        page = max_pages

    return {
        "pages": {
            "last": max_pages,
            "current": page,
            "is_last": page == max_pages
        },
        "results": [
            dict(res)
            for res in DATA[(page-1)*PAGELEN:page*PAGELEN]
        ]
    }


def perform_search(query="*", page=1):
    if query.strip() in {"", "*"}:
        return full(page=page)

    query = query.replace("v", "u").replace("V", "u").replace("j", "i").replace("J", "I")
    qp = MultifieldParser(["lemma", "Description", "Variation"], schema=search_index.schema)
    q = qp.parse(query)

    with search_index.searcher() as s:
        results = s.search_page(q, pagenum=page, pagelen=PAGELEN)

        out = {
            "pages": {
                "last": results.pagecount,
                "current": results.pagenum,
                "is_last": results.is_last_page()
            },
            "results": [
                dict(res)
                for res in results
            ]
        }
    return out


def paginate(current_page, total_pages, max_pages=10):
    if current_page < 1:
        current_page = 1
    elif current_page > total_pages:
        current_page = total_pages

    start_page, end_page = 1, 1
    if total_pages <= max_pages:
        start_page = 1
        end_page = total_pages
    else:
        maxPagesBeforeCurrentPage = math.floor(max_pages / 2)
        maxPagesAfterCurrentPage = math.ceil(max_pages / 2) - 1
        if current_page <= maxPagesBeforeCurrentPage:
            start_page = 1
            end_page = max_pages
        elif current_page + maxPagesAfterCurrentPage >= total_pages:
            start_page = total_pages - max_pages + 1
            end_page = total_pages
        else:
            start_page = current_page - maxPagesBeforeCurrentPage
            end_page = current_page + maxPagesAfterCurrentPage

    out =  list(range(start_page, end_page+1))
    if 1 not in out:
        out = [1] + out
    if total_pages not in out:
        out.append(total_pages)

    return out
