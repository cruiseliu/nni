# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

from .base import ToAlgoCommand

class InitializeCommand(ToAlgoCommand):
    command_type: str = 'initialize'
    config: ExperimentConfig

    @classmethod
    def _load(cls, data):
        # a little bit tricky, it will invoke superclass' method, but with cls=InitializeCommand
        obj = super()._load(data)
        obj.config = ExperimentConfig(**obj.config)
        return obj

class ReportMetricDataCommand(ToAlgoCommand):
    command_type: str = 'report-metric-data'
    parameter_id: int
    value: MetricData
    type: Literal['FINAL', 'PERIODICAL']

class UpdateSearchSpaceCommand(ToAlgoCommand):
    command_type: str = 'update-search-space'
    search_space: SearchSpace

class ImportDataCommand(ToAlgoCommand):
    command_type: str = 'import-data'
    parameter: HyperParameter
    value: MetricData

class TrialEndCommand(ToAlgoCommand):
    command_type: str = 'trial-end'
    trial_job_id: str
    # ...

class TerminateCommand(ToAlgoCommand):
    command_type: str = 'terminate'
