import sys

capitals = {
    "France":"Paris",
    "Germany":"Berlim"
}

travel_log = {
    "France": {"cities_visited":["Paris","Lille","Diion"],"total_visits":21}
}


travel_jeri = {
    "Brasil": {"custos_hotel":["Hotel Manay","Hotel Lusitano R","Hotel Treco Caiçara"],"dias_totais":32},
    "German": {"custos_hotel": ["Hotel Many"]}

}


#Here is because i need to show to user or run the nested list
for key in travel_jeri:
    print(travel_jeri[key]["custos_hotel"])


#This is just for show what the nested list have in
for key in travel_jeri:
    print(key)
    print(travel_jeri[key] == "Brasil")
    if travel_jeri[key] == "Brasil":

        print("Encontrei essa porra eu vou mudar esse valor seu filho da puta do caralho")
        travel_jeri[key]["custos_hotel"] = ["Hotel bundão"]
        print(travel_jeri[key])


