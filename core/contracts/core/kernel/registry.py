from core.contracts.module import I34Module


class ModuleRegistry:
    def __init__(self) -> None:
        self._modules: dict[str, I34Module] = {}

    def register(self, module: I34Module) -> None:
        if module.name in self._modules:
            raise ValueError(f"Module already registered: {module.name}")

        self._modules[module.name] = module

    def get(self, name: str) -> I34Module:
        if name not in self._modules:
            raise KeyError(f"Module not found: {name}")

        return self._modules[name]

    def has(self, name: str) -> bool:
        return name in self._modules

    def list_modules(self) -> list[str]:
        return list(self._modules.keys())
