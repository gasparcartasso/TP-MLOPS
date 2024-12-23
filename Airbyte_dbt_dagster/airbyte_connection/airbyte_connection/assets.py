from dagster import EnvVar
from dagster_airbyte import AirbyteResource

airbyte_instance = AirbyteResource(
    host="localhost",
    port="8000",
    # If using basic auth, include username and password:
    username="airbyte",
    password='password',
)
from dagster_airbyte import load_assets_from_airbyte_instance

# Use the airbyte_instance resource we defined in Step 1
airbyte_assets = load_assets_from_airbyte_instance(airbyte_instance)