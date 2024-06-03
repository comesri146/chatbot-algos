from rasa.core.policies import FallbackPolicy

@FallbackPolicy.register("FallbackPolicy")
class MyFallbackPolicy(FallbackPolicy):
    def __init__(self):
        super().__init__()
