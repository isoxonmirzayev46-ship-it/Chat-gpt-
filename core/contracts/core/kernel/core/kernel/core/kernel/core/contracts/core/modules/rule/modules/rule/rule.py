from core.contracts import I34Module, ModuleRequest, ModuleResponse


class RuleModule(I34Module):

    @property
    def name(self) -> str:
        return "rule"

    def handle(self, request: ModuleRequest) -> ModuleResponse:
        return ModuleResponse(
            success=True,
            data={
                "module": self.name,
                "action": request.action,
            },
        )

    def health(self) -> bool:
        return True
