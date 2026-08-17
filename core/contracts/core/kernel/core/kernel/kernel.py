from core.contracts.module import ModuleRequest, ModuleResponse
from core.kernel.registry import ModuleRegistry


class I34Kernel:
    def __init__(self) -> None:
        self.registry = ModuleRegistry()

    def register(self, module) -> None:
        self.registry.register(module)

    def dispatch(
        self,
        module_name: str,
        request: ModuleRequest,
    ) -> ModuleResponse:
        module = self.registry.get(module_name)

        if not module.health():
            return ModuleResponse(
                success=False,
                error=f"Module is unhealthy: {module_name}",
            )

        return module.handle(request)

    def modules(self) -> list[str]:
        return self.registry.list_modules()
