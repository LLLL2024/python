travel_vlog = {
"Franch":{"cities_visited":["Paris", "Little", "Dijon"], "total_visits": 12},
"Germany":{"cities_visited":["Barlin", "hambury","stuttgart"], "total_visits": 5},
}


travel_log = [
{"country" :"Franch",
 "cities_visited":["Paris", "Little", "Dijon"],
 "total_visits": 12},
{"country": "Germany",
 "cities_visited":["Barlin", "hambury", "stuttgart"],
 "total_visits": 5}
]
visited = "cities_visited"
franch = ""
print(travel_vlog['Franch']['cities_visited'])
print(travel_vlog['Franch'][visited])
query = input( "请输入查询内容:" )
if query in travel_vlog:
   franch = travel_vlog[query]
   print(franch)
   if visited in franch:
    print(franch[visited])