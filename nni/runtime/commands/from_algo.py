# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

from .base import FromAlgoCommand

class InitializationCompleteCommand(FromAlgoCommand):
    command_type: str = 'initialization-complete'

class NewTrialJobCommand(FromAlgoCommand):
    command_type: str = 'new-trial-job'
    parameter_id: int
    parameter: HyperParameter

class KillTrialJobCommand(FromAlgoCommand):
    command_type: str = 'kill-trial-job'
    trial_job_id: str


#class CommandType(Enum):
#    RequestTrialJobs = 'to-algo/request-trial-jobs'
#    AddCustomizedTrialJob = 'to-algo/add-customized-trial-job'
#    Ping = 'to-algo/ping'
#
#    Initialized = 'from-algo/initialized'
#    SendTrialJobParameter = 'from-algo/send-trial-job-parameter'
#    NoMoreTrialJobs = 'from-algo/no-more-trial-jobs'
