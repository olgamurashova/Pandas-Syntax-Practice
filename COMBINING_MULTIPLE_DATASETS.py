Append dataframes
 # 1. # Add an offset parameter to get cafes 51-100
params = {"term": "cafe", 
          "location": "NYC",
          "sort_by": "rating", 
          "limit": 50,
          "offset": 50}

result = requests.get(api_url, headers=headers, params=params)
next_50_cafes = json_normalize(result.json()["businesses"])

# Append the results, setting ignore_index to renumber rows
cafes = top_50_cafes.append(next_50_cafes, ignore_index=True)

# Print shape of cafes
print(cafes.shape)

#2. # Merge crosswalk into cafes on their zip code fields
cafes_with_pumas = cafes.merge(
    crosswalk,
    left_on = "location_zip_code",
    right_on = "zipcode"
)

# Merge pop_data into cafes_with_pumas on puma field
cafes_with_pop = cafes_with_pumas.merge(
    pop_data,
    left_on = "puma",
    right_on = "puma"
)

# View the data
print(cafes_with_pop.head())
