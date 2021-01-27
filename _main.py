@@ -15,7 +15,11 @@ def main():
    logging.info("Stated application")
    with OpsDroid() as opsdroid:
        loader = Loader(opsdroid)
        opsdroid.config = loader.load_config_file("./configuration.yaml")
        opsdroid.config = loader.load_config_file([
            "./configuration.yaml",
            "~/.opsdroid/configuration.yaml",
            "/etc/opsdroid/configuration.yaml"
            ])
        if "logging" in opsdroid.config:
            set_logging_level(opsdroid.config['logging'])
        loader.load_config(opsdroid.config)
