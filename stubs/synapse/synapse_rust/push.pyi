from typing import Any, Collection, Dict, Mapping, Sequence, Tuple, Union

from synapse.types import JsonDict

class PushRule:
    @property
    def rule_id(self) -> str: ...
    @property
    def priority_class(self) -> int: ...
    @property
    def conditions(self) -> Sequence[Mapping[str, str]]: ...
    @property
    def actions(self) -> Sequence[Union[Mapping[str, Any], str]]: ...
    @property
    def default(self) -> bool: ...
    @property
    def default_enabled(self) -> bool: ...
    @staticmethod
    def from_db(
        rule_id: str, priority_class: int, conditions: str, actions: str
    ) -> "PushRule": ...

class PushRules:
    def __init__(self, rules: Collection[PushRule]): ...
    def rules(self) -> Collection[PushRule]: ...

class FilteredPushRules:
    def __init__(
        self,
        push_rules: PushRules,
        enabled_map: Dict[str, bool],
        msc3786_enabled: bool,
        msc3772_enabled: bool,
    ): ...
    def rules(self) -> Collection[Tuple[PushRule, bool]]: ...

def get_base_rule_ids() -> Collection[str]: ...