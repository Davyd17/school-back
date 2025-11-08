from domain.entities.group import Group
from entry_points.api_rest.request.group.group_request import GroupRequest


class GroupRequestMapper:

    @staticmethod
    def to_domain(request: GroupRequest) -> Group:
        return Group(
            id=request.id
        )

    @staticmethod
    def from_domain(domain: Group) -> GroupRequest:
        return GroupRequest(
            id=domain.id
        )