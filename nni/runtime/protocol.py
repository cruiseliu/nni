# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

from __future__ import annotations

class CommandType(Enum):
    Initialize = 'to-algo/initialize'
    RequestTrialJobs = 'to-algo/request-trial-jobs'
    ReportMetricData = 'to-algo/report-metric-data'
    UpdateSearcSpace = 'to-algo/update-search-space'
    ImportData = 'to-algo/import-data'
    AddCustomizedTrialJob = 'to-algo/add-customized-trial-job'
    TrialEnd = 'to-algo/trial-end'
    Terminate = 'to-algo/terminate'
    Ping = 'to-algo/ping'

    Initialized = 'from-algo/initialized'
    NewTrialJob = 'from-algo/new-trial-job'
    SendTrialJobParameter = 'from-algo/send-trial-job-parameter'
    NoMoreTrialJobs = 'from-algo/no-more-trial-jobs'
    KillTrialJob = 'from-algo/kill-trial-job'

async def send(command: CommandType, data: str) -> None:
    assert command.value.startswith('from-tuner/'), command
    msg = json.dumps({'command': command, 'data': data})
    _out_queue.put_nowait(msg)

def receive():
    msg = None
    while msg is None:
        try:
            msg = _in_queue.get_nowait()
        except QueueEmpty:
            time.sleep(1)
    command_data = json.loads(msg)
    command = CommandType(command_data['command'])
    data = command_data['data']
    assert command.startswith('to-tuner/'), msg
    return command, data

_loop_thread = None
_stopping = False

async def _send_from_queue():
    while not _stopping:
        item = await _out_queue.get()
        await _websocket.send(item)

async def _receive_to_queue():
    while not _stopping:
        item = await _websocket.recv()
        await _in_queue.put(item)
