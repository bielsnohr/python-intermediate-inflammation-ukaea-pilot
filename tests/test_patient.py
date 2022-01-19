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


def test_add_patients_to_doctor():
    from inflammation.models import Doctor

    name = 'Bob'
    d = Doctor(name=name)
    days = (0, 1, 2)
    alice_values = (3, 3, 3)
    danny_values = (3, 5, 6)
    d.add_patient(name='Alice', values=alice_values, days=days)
    d.add_patient(name='Danny', values=danny_values, days=days)
    alice = d.patients[0]
    danny = d.patients[1]
    for i in range(len(days)):
        assert (alice.observations[i].day, alice.observations[i].value) == (
            days[i], alice_values[i])
        assert (danny.observations[i].day, danny.observations[i].value) == (
            days[i], danny_values[i])
