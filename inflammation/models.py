"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row
contains inflammation data for a single patient taken over a number of days
and each column represents a single day across all patients.

Functions:
    load_csv - Load a Numpy array from a CSV file
    daily_mean - Calculate the daily mean of a 2D inflammation data array
    daily_max - Calculate the daily max of a 2D inflammation data array
    daily_min - Calculate the daily min of a 2D inflammation data array
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array."""
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array."""
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array."""
    return np.min(data, axis=0)


def attach_names(data, names):
    """Attach names to each patient in a simple list of patient data

    :param data: 2D inflammation data array, 0th axis (i.e. rows) are patients
    :param names: the patient names to attach to each row in data
    :returns: A list of dict objects, where each dict represents a patient
    with their name and inflammation data
    """
    if data.shape[0] != len(names):
        raise TypeError("data and names have mismatched length")
    patients = []
    for patient_data, name in zip(data, names):
        patients.append({'name': name, 'data': patient_data})
    return patients


def patient_normalise(data):
    """Normalise patient data from a 2D inflammation data array.

    :param data: 2D inflammation data array, 0th axis (i.e. rows) are patients
    """
    max = np.nanmax(data, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / max[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0
    normalised[normalised < 0] = 0
    return normalised


class Observation:
    def __init__(self, day, value):
        self.day = day
        self.value = value

    def __str__(self):
        return str(self.value)


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Patient(Person):
    """A patient in an inflammation study."""
    def __init__(self, name):
        super().__init__(name)
        self.observations = []

    def add_observation(self, value, day=None):
        if day is None:
            try:
                day = self.observations[-1].day + 1

            except IndexError:
                day = 0

        new_observation = Observation(day, value)

        self.observations.append(new_observation)
        return new_observation


class Doctor(Person):
    def __init__(self, name):
        super().__init__(name)
        self.patients = []

    def add_patient(self, name, values, days):
        if len(values) != len(days):
            raise ValueError("Values and days to not match.")
        patient = Patient(name=name)
        for value, day in zip(values, days):
            patient.add_observation(value, day)
        self.patients.append(patient)

# TODO(lesson-design) Implement data persistence
# TODO(lesson-design) Add Doctor class
