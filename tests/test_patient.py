"""Tests for the Patient model."""


def test_create_patient():
    from inflammation.models import Patient

    name = 'Alice'
    p = Patient(name=name)

    assert p.name == name


def test_add_observation():
    from inflammation.models import Patient

    name = 'Alice'
    p = Patient(name=name)
    p.add_observation(value=3, day=0)

    assert (p.observations[0].day, p.observations[0].value) == (0, 3)


def test_create_doctor():
    from inflammation.models import Doctor

    name = 'Bob'
    d = Doctor(name=name)
    assert d.name == name
