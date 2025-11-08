from domain.entities.group import Group
from entry_points.api_rest.response.group.group_response import GroupResponse


class GroupResponseMapper:

    @staticmethod
    def from_domain(domain: Group) -> GroupResponse:

        return GroupResponse(
            id = domain.id,
            name = domain.name
        )

    @staticmethod
    def to_domain(response: GroupResponse) -> Group:

        return Group(
            id = response.id,
            name = response.name
        )