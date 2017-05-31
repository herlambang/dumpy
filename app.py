from apistar import App, environment, schema
from project.routes import routes


class Env(environment.Environment):
    properties = {
        'DEBUG': schema.Boolean(default=False)
    }

env = Env()


settings = {
    'DEBUG': env['DEBUG']
}

app = App(routes=routes, settings=settings)
