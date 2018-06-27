from sanic import Sanic
from sanic import Blueprint
from sanic.request import Request

from DrQA.drqa.pipeline import DrQA


drqa_blueprint = Blueprint('drqa', url_prefix='drqa')


@drqa_blueprint.route('/search/<question>', methods=['GET', 'POST'])
def search(request: Request, question: str):
    """

    :param request:
    :param question:
    :return:
    """
    from urllib.parse import unquote
    from sanic.response import json

    app: Sanic = request.app
    model: DrQA = app.drqa

    json_form = request.json
    form = request.form if json_form is None else json_form

    top_n = form.get("top_n", 1)
    n_docs = form.get("n_docs", 100)

    predictions = model.process(
        unquote(question), None, top_n, n_docs, return_context=True
    )

    return json(predictions, 200)
