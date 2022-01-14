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


# TODO(lesson-design) Add Patient class
# TODO(lesson-design) Implement data persistence
# TODO(lesson-design) Add Doctor class
