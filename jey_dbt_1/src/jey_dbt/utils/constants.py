from enum import Enum
from pathlib import Path


class DBTProfileOptions(str, Enum):
    trino = "trino"
    hive = "hive"
    spark = "spark"


TEMPLATE_DIR: Path = Path(__file__).parent.parent.absolute() / "templates"

DBT_PROJECT_YAML_TEMPLATE = "dbt_project.yml.template"
DBT_PROJECT_YAML = "dbt_project.yml"
DBT_PACKAGES_YAML = "packages.yml"
DBT_PROFILE_FOLDER = "connection"
DBT_PROFILE_TEMPLATE = "profiles.yml.template"
DBT_PROFILE_YAML = "profiles.yml"

__CML_PROD_DOMAIN = 'ml-3ab7a488-2a6.apps.apps.prod7.ocbc.com'
__CML_PREPROD_DOMAIN = 'ml-4d924a26-750.apps.apps.prod6.ocbc.com'
__CML_UAT_DOMAIN = 'ml-bfaee539-4f6.apps.apps.uat5.ocbc.com'
__CML_DR_DOMAIN = 'ml-6d012adf-6bb.apps.apps.dr2.ocbc.com'
