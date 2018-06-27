import logging

from DrQA.drqa.pipeline import DrQA

from sanic import Sanic
from server.sanic_extension import SanicExtension


logger = logging.getLogger(__name__)


def initialise(cuda: bool = False) -> DrQA:
    """

    :param cuda:
    :return:
    """
    from DrQA.drqa.retriever.ons_doc_ranker import OnsDocRanker
    from DrQA.drqa.retriever.doc_search import OnsSearchDB

    logger.info('Initializing pipeline...')
    model = DrQA(
        cuda=cuda,
        ranker_config={'class': OnsDocRanker},
        db_config={'class': OnsSearchDB}
    )
    logger.info('Pipeline initialised.')

    return model


class SanicDrQA(SanicExtension):
    """
    Class for initialising DrQA model.
    """

    def init_app(self, app: Sanic, **kwargs):
        use_cuda = app.config.get('CUDA_ENABLED', False)

        app.drqa = initialise(use_cuda)
