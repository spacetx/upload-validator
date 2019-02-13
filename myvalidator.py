#!/usr/bin/env python

from glob import glob

from sys import argv
from sys import exit

import starfish  # fix recursive imports
from sptx_format import validate_sptx


def find_experiment_json(filenames):
    experiments = [x for x in filenames if x.split("/")[-1] == "experiment.json"]
    if len(experiments) != 1:
        raise Exception(f"Too many experiments: {experiments}")
    return experiments[0]


def validate_experiment_json(filename):
    if validate_sptx.validate(filename):
        return 0
    return 1


if __name__ == "__main__":
    exit(
        validate_experiment_json(
            find_experiment_json(argv[1:])
        )
    )
