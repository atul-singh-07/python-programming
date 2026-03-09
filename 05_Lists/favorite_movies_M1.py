# Q: Write a programme to ask the user to enter name of 3 Favourite movies and store them in a list.

# Method:01
movies=[] # --> declaring empty list

mov_1=input("Enter First Faviorite Movie:")
mov_2=input("Enter Second Faviorite Movie:")
mov_3=input("Enter Third Faviorite Movie:")

movies.append(mov_1)
movies.append(mov_2)
movies.append(mov_3)

print(movies)