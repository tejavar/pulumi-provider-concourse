# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetArgs',
    'JobArgs',
    'PipelineConfigArgs',
    'PutArgs',
    'TaskArgs',
]

@pulumi.input_type
class GetArgs:
    def __init__(__self__, *,
                 identifier: pulumi.Input[str]):
        """
        Get step
        """
        pulumi.set(__self__, "identifier", identifier)

    @property
    @pulumi.getter
    def identifier(self) -> pulumi.Input[str]:
        return pulumi.get(self, "identifier")

    @identifier.setter
    def identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "identifier", value)


@pulumi.input_type
class JobArgs:
    def __init__(__self__, *,
                 identifier: pulumi.Input[str],
                 plan: pulumi.Input[Sequence[pulumi.Input[Union['GetArgs', 'PutArgs', 'TaskArgs']]]]):
        """
        Job configuration
        """
        pulumi.set(__self__, "identifier", identifier)
        pulumi.set(__self__, "plan", plan)

    @property
    @pulumi.getter
    def identifier(self) -> pulumi.Input[str]:
        return pulumi.get(self, "identifier")

    @identifier.setter
    def identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "identifier", value)

    @property
    @pulumi.getter
    def plan(self) -> pulumi.Input[Sequence[pulumi.Input[Union['GetArgs', 'PutArgs', 'TaskArgs']]]]:
        return pulumi.get(self, "plan")

    @plan.setter
    def plan(self, value: pulumi.Input[Sequence[pulumi.Input[Union['GetArgs', 'PutArgs', 'TaskArgs']]]]):
        pulumi.set(self, "plan", value)


@pulumi.input_type
class PipelineConfigArgs:
    def __init__(__self__, *,
                 jobs: pulumi.Input[Sequence[pulumi.Input['JobArgs']]]):
        """
        Pipeline configuration
        """
        pulumi.set(__self__, "jobs", jobs)

    @property
    @pulumi.getter
    def jobs(self) -> pulumi.Input[Sequence[pulumi.Input['JobArgs']]]:
        return pulumi.get(self, "jobs")

    @jobs.setter
    def jobs(self, value: pulumi.Input[Sequence[pulumi.Input['JobArgs']]]):
        pulumi.set(self, "jobs", value)


@pulumi.input_type
class PutArgs:
    def __init__(__self__, *,
                 identifier: pulumi.Input[str]):
        """
        Put step
        """
        pulumi.set(__self__, "identifier", identifier)

    @property
    @pulumi.getter
    def identifier(self) -> pulumi.Input[str]:
        return pulumi.get(self, "identifier")

    @identifier.setter
    def identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "identifier", value)


@pulumi.input_type
class TaskArgs:
    def __init__(__self__, *,
                 identifier: pulumi.Input[str]):
        """
        Task step
        """
        pulumi.set(__self__, "identifier", identifier)

    @property
    @pulumi.getter
    def identifier(self) -> pulumi.Input[str]:
        return pulumi.get(self, "identifier")

    @identifier.setter
    def identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "identifier", value)


