from typing import Annotated

from humps import camelize
from pydantic import BaseModel
from pydantic import Field


def to_camel(string):
    return camelize(string)


class AbstractTaskConfiguration(BaseModel):
    name: str
    ecs_tenant_id: Annotated[
        str,
        Field(
            title="ECS tenant ID",
            description=(
                "The tenant ID to use when making requests to FOLIO APIs for this task, if ",
                "different from library configuration",
            ),
        ),
    ] = ""
    batch_size: Annotated[
        int,
        Field(
            title= "Batch Size",
            description=(
                "The batch size let users to define the size of batch load"
            ),
            ge=1,
            default=100,
        )
    ]

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True
