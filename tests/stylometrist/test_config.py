from src.stylometrist import config


def test_config_default():
    cnf = config.Config()
    assert cnf.model == config.DEFAULT_MODEL


def test_config_no_default():
    test_model = 'el_core_news_sm'
    cnf = config.Config(model=test_model)
    assert cnf.model == test_model
