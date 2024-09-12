import flet as ft
from UI.view import View
from model.modello import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listState = []
    def fillDD(self):
        SightingList = self._model.listSighting

        for s in SightingList:
            if s.datetime.year not in self._listYear:
                self._listYear.append(s.datetime.year)

        for a in self._listYear:
            self._view.ddyear.options.append(ft.dropdown.Option(a))

        self._view.update_page()

    def fillDDState(self, e):
        self._view.ddstate.options.clear()
        self._view.update_page()
        year = float(self._view.ddyear.value)
        SightingList = self._model.listSighting
        StateList = self._model.listStates
        for s in SightingList:
            if s.state not in self._listState and s.datetime.year == year:
                self._listState.append(s.state.upper())
        for s in StateList:
            if s.id in self._listState:
                self._view.ddstate.options.append(ft.dropdown.Option(s.name))
        self._view.update_page()
        self._listState.clear()

    def handle_graph(self, e):
        if self._view.ddyear.value is None:
            self._view.create_alert("Selezionare un anno!")
            return
        a = self._view.ddyear.value
        if self._view.ddstate.value is None or self._view.ddstate.value == "":
            self._view.create_alert("Selezionare uno stato!")
            return
        s = self._view.ddstate.value

        self._view.txt_result1.controls.clear()
        self._model.buildGraph(s, a)

        self._view.txt_result1.controls.append(ft.Text(f"Numero di vertici: {self._model.get_num_of_nodes()} Numero di archi: {self._model.get_num_of_edges()}"))
        self._view.txt_result1.controls.append(
            ft.Text(f"Il grafo ha: {self._model.get_num_connesse()} componenti connesse"))
        connessa = self._model.get_largest_connessa()
        self._view.txt_result1.controls.append(ft.Text(f"La componente connessa più grande "
                                                       f"è costituita da {len(connessa)} nodi:"))
        for c in connessa:
            self._view.txt_result1.controls.append(ft.Text(c))

        self._view.update_page()

    def handle_path(self, e):
        pass

