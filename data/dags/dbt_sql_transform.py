import os
import logging
from datetime import datetime
from datetime import timedelta
from pathlib import Path

from cosmos import (
    DbtDag,
    ProfileConfig,
    ProjectConfig
)

logger = logging.getLogger(__name__)

default_args = {
    "owner": "lake",
    "retries": 1,
    "retry_delay": 0
}

default_dbt_root_path = Path(__file__).parent / "dbt"
dbt_root_path = Path(os.getenv("DBT_ROOT_PATH", default_dbt_root_path))

profile_config = ProfileConfig(
    profile_name="iceberg",
    target_name="dev",
    profiles_yml_filepath=(dbt_root_path / "lake/profiles.yml")
)

dbt_sql_transform = DbtDag(
    project_config=ProjectConfig((dbt_root_path / "lake").as_posix()),
    profile_config=profile_config,
    operator_args={
        "install_deps": True,
        "full_refresh": True,
    },

    schedule_interval=timedelta(minutes=30),
    start_date=datetime(2024, 2, 23),
    catchup=False,
    dag_id="dbt_sql_transform",
    default_args={"retries": 2},
)
