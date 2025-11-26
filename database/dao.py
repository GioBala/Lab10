from database.DB_connect import DBConnect
from model.compagnia import Compagnia
from model.hub import Hub
from model.spedizione import Spedizione


class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO

    @staticmethod
    def get_arco(h1, h2):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        query = """
            SELECT COUNT(*) AS n, SUM(valore_merce)
            FROM spedizione
            WHERE (id_hub_origine = %s AND id_hub_destinazione = %s)
               OR (id_hub_origine = %s AND id_hub_destinazione = %s)
        """
        cursor.execute(query, (h1, h2, h2, h1))
        row = cursor.fetchone()
        n = row[0] or 0
        totale = row[1] or 0
        prezzo = totale / n if n > 0 else 0
        cursor.close()
        cnx.close()
        return (prezzo)

    @staticmethod
    def get_num_nodi():
        cnx = DBConnect.get_connection()
        cursor=cnx.cursor()
        query = "SELECT COUNT(id) FROM hub"
        cursor.execute(query)
        row = cursor.fetchone()
        results=row[0]
        cursor.close()
        cnx.close()
        return results

    @staticmethod
    def get_num_archi():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        query = """SELECT COUNT(*) AS n
                    FROM (
                    SELECT DISTINCT 
                    LEAST(id_hub_origine, id_hub_destinazione) AS hub_A,
                    GREATEST(id_hub_origine, id_hub_destinazione) AS hub_B
                    FROM spedizione
                    ) AS t;"""
        cursor.execute(query)
        row=cursor.fetchone()
        results= row[0]
        cursor.close()
        cnx.close()
        return results


    @staticmethod
    def get_hub(h):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        query = "SELECT nome,stato FROM `hub` WHERE id=%s"
        cursor.execute(query, (h,))
        row = cursor.fetchone()
        cnx.close()
        cursor.close()
        return row
    """
    @staticmethod
    def get_compagnia():
        cnx = DBConnect().get_connection()
        cursor = cnx.cursor
        query = "SELECT * FROM hub"
        cursor.execute(query)
        results = []
        for row in cursor:
            results.append(Compagnia(row[0], row[1], row[2], ))
        cursor.close()
        cnx.close()
        return results

    @staticmethod
    def get_spedizione():
        cnx = DBConnect().get_connection()
        cursor = cnx.cursor
        query = "SELECT * FROM spedizione"
        cursor.execute(query)
        results = []
        for row in cursor:
            results.append(Spedizione(row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7],row[8]))
        cursor.close()
        cnx.close()
        return results


    """