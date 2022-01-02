# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

from __future__ import annotations

## main public api ##

def decode_command(command_string: str) -> Command:
    data = json.loads(command_string)
    cls = _find_command_class(data['channel'], data['commandType'])
    return cls._load(data)

## base classes ##

class Command:
    channel: str
    command_type: str

    @classmethod
    def _load(cls, data):
        # TODO: Be fault tolerant for now in case I make mistakes. Crash on error in future.
        obj = cls()
        for field in fields(cls):
            camel_key = _camel_case(field.name)
            if camel_key not in data:
                _logger.error(f'{cls.__name__}: missing field {field.name} in {data}')
                setattr(obj, field.name, None)
            else:
                value = data.pop(camel_key)
                setattr(obj, field.name, value)
        if data:
            _logger.error(f'{cls.__name__}: cannot recognize fields: {data}')
        return obj

class ToAlgoCommand(Command):
    channel: str = 'to-algo'

class FromAlgoCommand(command):
    channel: str = 'from-algo'

## utils ##

def _camel_case(name: str) -> str:
    words = name.split('_')
    return words[0] + ''.join(word.title() for word in words[1:])

def _find_command_class(channel, command_type):
    for cls in Command.__subclasses__():
        if cls.command_type == command_type and cls.channel == channel:
            return cls
    raise ValueError(f'Bad command type: channel="{channel}" command_type="{command_type}"')
