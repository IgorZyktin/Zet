# -*- coding: utf-8 -*-

"""Представление графа.
"""


class Graph:
    """Представление графа.
    """

    def __init__(self):
        """Инициализировать экземпляр.
        """
        self.nodes = {}
        self.edges = {}

    def add_node(self, name: str, label: str,
                 bg_color: str, link: str) -> None:
        """Добавить ноду в граф.
        """
        self.nodes[name] = {
            'label': label,
            'bg_color': bg_color,
            'link': link,
        }

    def add_edge(self, node_start: str, node_finish: str,
                 weight: float = 0.1) -> None:
        """Добавить грань в граф.
        """
        if node_start not in self.edges:
            self.edges[node_start] = {}

        self.edges[node_start][node_finish] = {
            'weight': weight,
        }

    def as_dict(self) -> dict:
        """Вернуть граф в форме словаря.
        """
        return {
            'nodes': self.nodes,
            'edges': self.edges,
        }