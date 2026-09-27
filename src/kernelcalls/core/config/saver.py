from omegaconf import DictConfig, ListConfig, OmegaConf


def save_config(cfg: DictConfig | ListConfig, path: str) -> None:
    data = OmegaConf.to_container(cfg, resolve=True)

    if isinstance(data, dict):
        secrets = data.get("secrets")
        if isinstance(secrets, dict):
            for key, value in secrets.items():
                if value:
                    secrets[key] = "***"

    OmegaConf.save(config=data, f=f"{path}/config.yaml", resolve=True)
