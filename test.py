from DatabaseConnection import DatabaseConnection
from DAO.restaurantDAO import RestaurantDao

db_connection = DatabaseConnection('consorcio', 'consorcio', 'nomelase123', 'heflox.com', '5432')
restaurant_dao = RestaurantDao(db_connection)

# Crear usuario
result = restaurant_dao.get_restaurants()
print(type(result))
print(result)


# # Obtener usuario
# user = user_dao.get_user(1)
# print(user)

# # Actualizar usuario
# user_dao.update_user(1, 'Jane Doe', 'jane.doe@example.com')

# # Eliminar usuario
# user_dao.delete_user(1)
