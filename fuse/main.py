from fuse.config import config_app

if __name__ == "__main__":
    app_conf = config_app()
    cmd = app_conf.func
    kwargs = vars(app_conf)
    del kwargs["func"]
    cmd(**kwargs)
