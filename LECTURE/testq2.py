popularity_score = {
	"C++": 99.7,
	"C": 96.7,
	"Java": 97.5,
	"Python": 100,
	"C#": 97.5
}

def ranking(dict):
	
	temp_arr = []
	new_dict = {}

	for i in dict:
		
		found = False
		
		for j in range(len(temp_arr)):

			if dict[i] >= temp_arr[j][1]:
				found = True
				temp_arr.insert(j, [i, dict[i]])
				break
		
		if not found:
			temp_arr.append([i, dict[i]])
 
	for i in range(len(temp_arr)):
	
		if temp_arr[i][1] == temp_arr[i-1][1]:
			new_dict[i] = new_dict[i] + ", " + temp_arr[i][0]
		else:
			new_dict[i+1] = temp_arr[i][0]

	return new_dict

def new_ranking(dict):
	dict_sort = sorted(dict.items(), key = lambda x:x[1], reverse = True)
 
	new_dict = {}
	for i in range(len(dict)):
		if dict_sort[i][1] == dict_sort[i-1][1]:
			new_dict[i] = new_dict[i] + ", " + dict_sort[i][0]
		else:
			new_dict[i+1] = dict_sort[i][0]
   
	return new_dict

print(ranking(popularity_score))
print(new_ranking(popularity_score))