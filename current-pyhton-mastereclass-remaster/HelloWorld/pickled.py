import pickle

imelda = ("more mayhem",
          "Imelda may"
          "2011",
          ((1, "pulling the rug"),
           (2, "psycho"),
           (3, "mayhem"),
           (4, "kentish town waltz")))

with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file)