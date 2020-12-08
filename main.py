
def ranger():
  print("Hello I'm Ranger Tik, I am here to help you plan your amazing National Parks vacation!\n \nThe National Parks Service works tirelessly to protect our country's wilderness for your exploration and preserve our beautiful landscape for future generations to experience.\n ")
  user_input = input("How are you doing today? ")
  mood(user_input)
  print("Alright then let's find the perfect national park for your vacation!")
  region()
  return


def mood(mood_input):
  if "you" in mood_input.lower():
    print("I'm doing great, thanks for asking. I love my job!")
  if "bad" in mood_input.lower() or "not good" in mood_input.lower() or "not doing well" in mood_input.lower():
    print("I'm sorry to hear that, well a national parks trip will make everything better!")
  elif "good" in mood_input.lower() or "well" in mood_input.lower():
    print("I'm glad to hear you're doing well!")
  return


def region():
  user_input = input("What region are you interested in seeing? \nSouthwest?\nNorthwest\nMidwest\nSouth\nNortheast\n")
  if "southwest" in user_input.lower():
    print("Great pick! That's my personal favorite. \nThere is so much to see in the American Southwest. This region has all kinds of diverse landscapes and is home to more national parks than any other region in the US.")
    #southwest()
  elif "northwest" in user_input.lower():
    print("Good pick! The American Northwest is home to many national parks. This region is known for its stunning mountains and lush forests.")
    #northwest()
  elif "midwest" in user_input.lower():
    print("Nice! The American Midwest is know for its vast serene plains, beautiful lakes, and cool waterfalls.")
    #northwest()
  elif "south" in user_input.lower():
    print("Cool! The South is know for its dense forests and the Appalachian mountains.")
    #south()
  elif "northeast" in user_input.lower():
    print("Alright! The American Northeast is best know for its rugged coastline.")
    #northeast()
  else:
    print("Hmm, I didn't get that. \nWell if you can't make up your mind I'd suggest my favorite region: the American Southwest. \nNow let's find a park you'll really enjoy!")
    #southwest()


def southwest():
  


ranger()