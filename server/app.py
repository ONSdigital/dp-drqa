from sanic import Sanic


def create_app() -> Sanic:
    import asyncio
    import uvloop

    from server.log_config import default_log_config
    from server.sanic_drqa import SanicDrQA

    from server.drqa.routes import drqa_blueprint

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    app = Sanic(log_config=default_log_config)
    app.blueprint(drqa_blueprint)

    # Initialise DrQA pipeline
    SanicDrQA(app)

    return app
