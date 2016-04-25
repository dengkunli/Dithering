from skimage import io, color
import numpy

def filtre(m,taille):
    result = numpy.zeros(img_gray.shape)
    for i in range(taille[0]) :
        for j in range(taille[1]) :
            result[i][j] = m[i%m.shape[0]][j%m.shape[1]]
    return result

def quantification(img,m):
    return img*m.size

def ceuillage(imgQ, filtre):
    result = numpy.zeros(imgQ.shape)
    for i in range(imgQ.shape[0]) :
        for j in range(imgQ.shape[1]) :
            if (imgQ[i][j] < filtre[i][j]) :
                result[i][j] = 0
            else :
                result[i][j] = 1
    return result

#matrice de ceuillage
s = numpy.array([[34, 25, 21, 17, 29, 33],
                 [30, 13, 9 , 5 , 12, 24],
                 [18, 6 , 1 , 0 , 8 , 20],
                 [22, 10, 2 , 3 , 4 , 16],
                 [26, 14, 7 , 11, 15, 28],
                 [35, 31, 19, 23, 27, 32]])

#on charge l'image et on la transforme en niveau de gris
img = io.imread("Lenna.png")
img_gray = color.rgb2gray(img)

#on crée le filtre
filtre = filtre(s,img_gray.shape)
        
#ss = ss+0.5
#D = 255./36.
        
#on quantifie les niveux de gris de l'image et on effectue le ceuillage
imgQ = quantification(img_gray,s)
result = ceuillage(imgQ,filtre)

io.imshow(result)
#io.show()