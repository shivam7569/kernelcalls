# Utils concerning the operations related to paths


import os
from datetime import datetime, timedelta, timezone

from loguru import logger


@logger.catch(reraise=True)
def setup_experiment_dir(
    experiment_name: str,
    experiment_dir: str,
    domain: str,
    task: str,
    resuming: bool = False,
) -> str:
    ist_zone = timezone(timedelta(hours=5, minutes=30))
    experiment_time = f"{datetime.now(ist_zone):%Y%m%d_%H%M%S}"
    experiment_dir = os.path.join(experiment_dir, domain, task, experiment_name)
    if not resuming:
        experiment_dir = os.path.join(experiment_dir, experiment_time)
    else:
        try:
            last_exp_dir = max(
                sorted(
                    [
                        i
                        for i in os.listdir(experiment_dir)
                        if os.path.isdir(os.path.join(experiment_dir, i))
                    ]
                )
            )
        except FileNotFoundError:
            logger.error(
                "This is the first run of the experiment, resuming not possible."
            )
            raise FileNotFoundError("No parent experiment directory to resume from.")
        experiment_dir = os.path.join(experiment_dir, last_exp_dir)
        any_resume_dir = [
            i
            for i in os.listdir(experiment_dir)
            if os.path.isdir(os.path.join(experiment_dir)) and "resume" in i
        ]

        if not any_resume_dir:
            experiment_dir = os.path.join(experiment_dir, "resume_0")
        else:
            last_index = (
                max(sorted([int(i.split("_")[-1]) for i in any_resume_dir])) + 1
            )
            experiment_dir = os.path.join(experiment_dir, f"resume_{last_index}")

    os.makedirs(name=experiment_dir, exist_ok=True)

    return experiment_dir
