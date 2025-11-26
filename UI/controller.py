from unicodedata import digit

import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        # TODO
        self._view.lista_visualizzazione.controls.clear()
        self._view.page.update()
        if self._view.guadagno_medio_minimo.value.isdigit():
            h, t, r = self._model.costruisci_grafo(self._view.guadagno_medio_minimo.value)
            self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di hubs {h}"))
            self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di tratte {t}"))
            self._view.lista_visualizzazione.controls.append(ft.Text(f"{r}"))
            self._view.page.update()
        else:
            self._view.show_alert("Inserisci un numero")
