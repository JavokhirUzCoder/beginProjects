import pynecone as pc

class ProjectConfig(pc.Config):
    pass

config = ProjectConfig(
    app_name="Project",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
