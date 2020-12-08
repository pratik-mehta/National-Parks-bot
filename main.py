
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
  user_input = input("What region are you interested in seeing? \nSouthwest\nNorthwest\nMidwest\nSouth\nNortheast\n")
  if "southwest" in user_input.lower():
    print("Great pick! That's my personal favorite. \nThere is so much to see in the American Southwest. This region has all kinds of diverse landscapes and is home to more national parks than any other region in the US.")
    southwest()
  elif "northwest" in user_input.lower():
    print("Good pick! The American Northwest is home to many national parks. This region is known for its stunning mountains and lush forests.")
    northwest()
  elif "midwest" in user_input.lower():
    print("Nice! The American Midwest is know for its vast serene plains, beautiful lakes, and cool waterfalls.")
    midwest()
  elif "south" in user_input.lower():
    print("Cool! The South is know for its dense forests and the Appalachian mountains.")
    south()
  elif "northeast" in user_input.lower():
    print("Alright! The American Northeast is best know for its rugged coastline.")
    northeast()
  else:
    print("Hmm, I didn't get that. \nWell if you can't make up your mind I'd suggest my favorite region: the American Southwest. \nNow let's find a park you'll really enjoy!")
    southwest()
  return

def southwest():
  print("Alright, let find a great park for you in the American Southwest!\n")
  user_input = input("What are you interested in seeing?")
  if "rock formation" in user_input.lower():
    print("You should visit Arches National Park & Bryce Canyon National Park in Utah! \nArches is world famous for its more than 2,000 natural stone arches, while Bryce Canyon is known its hoodoos. Geat ready for some breathtaking scenery.")
  elif "waterfall" in user_input.lower():
    print("You should visit Yosemite National Park in California! \nYosemite is world famous for its waterfalls, granite mountains, and gergous valley. This will be a trip you'll never forget. \nFun fact: Yosemite was the 2nd national park.")
  elif "springs" in user_input.lower() or "geothermal" in user_input.lower():
    print("You should visit Lassen Volcanic National Park in California! \nLassen is world famous for its geothermal springs. Make sure you checkout the Bumpass Hell Trail. This will be a trip you'll never forget.")
  elif "mountain" in user_input.lower():
    print("You should visit Rocky Mountains National Park in Colorado! \nThe Rockies contain some of the tallest mountains in the US. Soak in the iconic mountains.")
  elif "valley" in user_input.lower():
    print("You should visit Death Valley National Park in California! \nDeath Valley in known for its extremes, blazing hot valley and cool mountains. Get ready for some breathtaking scenery.")
  elif "forest" in user_input.lower():
    print("You should visit Sequioa National Park in California! \nSoak in the iconic trees. \nFun fact: Sequioa was the 2nd national park.")
  elif "canyon" in user_input.lower():
    print("You should visit Grand Canyon National Park in Arizona! \nThe Grand Canyon is simply stunning. Geat ready to be blown away.")
  else:
    print("You should visit Kings Canyon National Park in California. Enjoy! ")
  return

def northwest():
  print("Alright, let find a great park for you in the American Northwest!\n")
  user_input = input("What are you interested in seeing?")
  if "lake" in user_input.lower():
    print("You should visit Crater Lake National Park in Oregon! \nThe pristine Crater Lake is the deepest lake in the US. Soak in the beauty. \nFun fact: Crater Lake was the 5th national park.")
  elif "springs" in user_input.lower() or "geothermal" in user_input.lower():
    print("You should visit Yellowstone National Park! \nYellowstone is known for its geothermal activity. \nFun fact: Yellowstone was the 1st national park.")
  elif "forest" in user_input.lower():
    print("You should visit Olympic National Park in Washington! \nSoak in the trees.")
  elif "animal" in user_input.lower():
    print("You should visit Yellowstone National Park! \nKeep a look out for bison. \nFun fact: Yellowstone was the 1st national park.")
  elif "volcano" in user_input.lower():
    print("You should visit Mount Rainier National Park in Washington! \nMount Rainier is actually an active volcano. Enjoy! \nFun fact: Mount Rainier was the 4th national park.")
  elif "mountain" in user_input.lower():
    print("You should visit Grend Teton National Park in Wyoming! \nSoak in the iconic Teton Range.")
  else:
    print("You should visit Olympic National Park in Washington. Enjoy!")
  return

def midwest():
  print("Alright, let find a great park for you in the Midwest!\n")
  user_input = input("What are you interested in seeing?")
  if "sand" in user_input.lower() or "dunes" in user_input.lower():
    print("You should check out Indiana Dunes National Park! \nFun fact Indiana Dunes is the 2nd most recently established national park, designated that status in 2019.")
  if "rock formation" in user_input.lower():
    print("You should visit Badlands National Park in South Dakota! \nBadlands is world famous for unique colorful rock formations. Geat ready for some breathtaking scenery.")
  elif "cave" in user_input.lower():
    print("You should visit Wind Cave National Park in South Dakota! Enjoy.")
  elif "prairie" in user_input.lower():
    print("You should visit Tallgrass Prarie National Preserve in Kansas! Enjoy.")
  elif "mountain" in user_input.lower():
    print("The midwest isn't really known for mountains! I'd recommend checking out the Southwest or Northwest. ")
    user_input = input("Would you like to check out the Southwest?")
    if "yes" in user_input:
      southwest()
      return
  print("You should visit Mount Rushmore National Memorial in South Dakota. Its a classic, enjoy!")
  return

def south():
  print("Alright, let find a great park for you in the South!\n")
  user_input = input("What are you interested in seeing?")
  if "animal" in user_input.lower() or "swamp" in user_input.lower() or "gator" in user_input.lower():
    print("You should visit Everglades National Park!")
  else:
    print("You should visit Great Smoky Mountains National Park nestled in the Appalachian hills! Fun fact: this is the most visited national park in the US. ")
  return

def northeast():
  print("Alright, let find a great park for you in the American Northeast!\n")
  user_input = input("What are you interested in seeing?")
  if "mountain" in user_input.lower():
    print("The northeast isn't really known for mountains! I'd recommend checking out the Southwest or Northwest. ")
    user_input = input("Would you like to check out the Southwest?")
    if "yes" in user_input:
      southwest()
      return
  print("You should visit Acadia National Park in Maine. Enjoy!")
  return

ranger()