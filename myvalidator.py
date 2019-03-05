#!/usr/bin/env python

from glob import glob
from json import dumps

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
    rv = {
        "validation_state": "VALID"
        "validation_errors": []
    }
    if not validate_sptx.validate(filename):
        rv["validation_state"] = "INVALID"
        rv["validation_errors"].append({
            "user_friendly_message": "FIXME",
            "filename": filename,
        })
    return dumps(rv)


if __name__ == "__main__":
    print(
        validate_experiment_json(
            find_experiment_json(argv[1:])
        )
    )
