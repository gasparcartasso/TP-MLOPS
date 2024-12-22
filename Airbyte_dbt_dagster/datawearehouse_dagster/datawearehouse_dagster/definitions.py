from pathlib import Path

from dagster import AssetExecutionContext, Definitions
from dagster_dbt import (
    DbtCliResource,
    DbtProject,
    build_schedule_from_dbt_selection,
    dbt_assets,
)

RELATIVE_PATH_TO_MY_DBT_PROJECT = "/home/gcartasso/Downloads/mlops-ecosystem-main/db_postgres"

my_project = DbtProject(
    project_dir=Path(__file__)
    .joinpath("..", RELATIVE_PATH_TO_MY_DBT_PROJECT)
    .resolve(),
)
my_project.prepare_if_dev()


@dbt_assets(manifest=my_project.manifest_path)
def my_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()



defs = Definitions(
    assets=[my_dbt_assets],
    resources={
        "dbt": DbtCliResource(project_dir=my_project),
    },
)