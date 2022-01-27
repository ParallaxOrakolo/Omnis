from inspect import Attribute
from .models import NodeSheet, defaultException, ProcessManager
from ariadne import MutationType

mutation = MutationType()
process = ProcessManager()

@defaultException
@mutation.field("createNodeSheet")
def createNodeSheet_resolver(obj, info, **kwargs):
    """Create a new NodeSheet object and return it like a payload"""
    returns = NodeSheet().createNodeSheet(**kwargs.get("input", {}))
    return {"success": True, "data": returns}


@defaultException
@mutation.field("updateNodeSheet")
def updateNodeSheet_resolver(obj, info, **kwargs):
    """Update a NodeSheet by id and return it like a payload"""
    returns = NodeSheet().updateNodeSheet(kwargs.get("id"), **kwargs.get("input", {}))
    return {"success": True, "data": returns}


@defaultException
@mutation.field("deleteNodeSheet")
def deleteNodeSheet_resolver(obj, info, id):
    """Delete a NodeSheet by id and return it like a payload"""
    returns = NodeSheet().deleteNodeSheet(id)
    return {"success": True, "data": returns}

@defaultException
@mutation.field("startProcess")
def startProcess_resolver(obj, info):
    """Start a process by id and return it like a payload"""
    # try:
    process.startProcess()
    returns = process.dict()
    print(returns)
    # except AttributeError:
    #     raise AttributeError("Id in last-values colletions does not match with any process")
    return {"success": True, "data": returns}

@defaultException
@mutation.field("stopProcess")
def stopProcess_resolver(obj, info):
    """Stop a process by id and return it like a payload"""
    # try:
    process.stopProcess()
    returns = process.dict()
    print(returns)
    # except AttributeError:
    #     raise AttributeError("Id in last-values colletions does not match with any process")
    return {"success": True, "data": returns}

@defaultException
@mutation.field("pauseProcess")
def pauseProcess_resolver(obj, info):
    """Pause a process by id and return it like a payload"""
    # try:
    process.pauseProcess()
    returns = process.dict()
    print(returns)
    # except AttributeError:
    #     raise AttributeError("Id in last-values colletions does not match with any process")
    return {"success": True, "data": returns}

@defaultException
@mutation.field("resumeProcess")
def resumeProcess_resolver(obj, info):
    """Resume a process by id and return it like a payload"""
    # try:
    process.resumeProcess()
    returns = process.dict()
    print(returns)
    # except AttributeError:
    #     raise AttributeError("Id in last-values colletions does not match with any process")
    return {"success": True, "data": returns}
