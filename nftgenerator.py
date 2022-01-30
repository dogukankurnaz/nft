import pagan
inpt = input("Name: ")
img = pagan.Avatar(inpt, pagan.SHA512)
img.show()
outpath = 'output/'
filename = inpt+".png"
img.save(outpath, filename)
