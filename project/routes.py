from apistar import Include, Route
from apistar.docs import docs_routes
from apistar.statics import static_routes
from project.views import welcome, stats

routes = [
    Route('/', 'GET', welcome),
    Route('/stats', 'GET', stats),
    Include('/docs', docs_routes),
    Include('/static', static_routes)
]
