class RestaurantDao:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_restaurants(self):
        with self.db_connection as cursor:
            cursor.execute("SELECT * FROM restaurantes")
            result = cursor.fetchall()

        restaurants = []
        for row in result:
            res_id, res_nombre, res_url, res_desc = row
            restaurants.append({
                'id': res_id,
                'nombre': res_nombre,
                'url': res_url,
                'descripcion': res_desc,
            })
        return restaurants

    # def create_restaurant(self, name, email):
    #     with self.db_connection as cursor:
    #         cursor.execute("INSERT INTO restaurants (name, email) VALUES (%s, %s)", (name, email,))
    
    # def update_restaurant(self, restaurant_id, name, email):
    #     with self.db_connection as cursor:
    #         cursor.execute("UPDATE restaurants SET name = %s, email = %s WHERE id = %s", (name, email, restaurant_id,))

    # def delete_restaurant(self, restaurant_id):
    #     with self.db_connection as cursor:
    #         cursor.execute("DELETE FROM restaurants WHERE id = %s", (restaurant_id,))