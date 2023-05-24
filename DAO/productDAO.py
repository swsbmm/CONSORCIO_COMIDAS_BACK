class ProductDao:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_products(self, restaurant_id):
        with self.db_connection as cursor:
            cursor.execute(f'''SELECT
	            p.pro_id, p.pro_nombre, p.pro_url, p.pro_desc, t.tip_tipo
                FROM 
                restaurantes r, productos p, tipo t
                WHERE
                r.res_id = p.fk_res AND t.tip_id = p.fk_tip_id AND r.res_id = {restaurant_id}
                ORDER BY
                p.pro_id
''')
            result = cursor.fetchall()

        products = []
        for row in result:
            pro_id, pro_nombre, pro_url, pro_desc, tip_tipo = row
            products.append({
                'id': pro_id,
                'nombre': pro_nombre,
                'url': pro_url,
                'descripcion': pro_desc,
                'tipo': tip_tipo,
            })
        return products