from fastapi.middleware.cors import CORSMiddleware

origins = [
    "https://quivr-frontend-3xr5bwxmyq-ey.a.run.app",
    "https://quivr-frontend-3xr5bwxmyq-ey.a.run.app:8080",
    "localhost:8080",
    "localhost"
]


def add_cors_middleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
