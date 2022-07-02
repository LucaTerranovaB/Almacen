from logging.config import dictConfig


capitales = {"Guatemala": "Ciudad de Guatemala"
            , "El Salvador": "San Salvador"
            , "Honduras": "Honduras"
            ,"Nicaragua": "Managua"
            , "Costa Rica": "San Jose"
            , "Panama": "Panama"
            , "Argentina": "Buenos Aires"
            , "Colombia": "Bogota"
            , "Venezuela": "Caracas"
            , "España": "Madrid"}

pais = input("Ingresar el pais: ")
print("La capital es :  ")
print(capitales[pais]) 
