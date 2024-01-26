from src import main


def setup_event():
    return main.Event()


def setup_event_store():
    return main.EventStore()


def test_class_event():
    res = setup_event()
    assert isinstance(res, main.Event)


def test_class_event_store():
    res = setup_event_store()
    assert isinstance(res, main.EventStore)

