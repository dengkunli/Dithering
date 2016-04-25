from skimage import io, color
import numpy

def filtre(m,taille):
    result = numpy.zeros(taille)
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

def orderedThreshold(img,m):
    #on charge l'image et on la transforme en niveau de gris
    img = io.imread(img)
    img_gray = color.rgb2gray(img)
    
    #on crée le filtre
    fil = filtre(m,img_gray.shape)
    
    #on quantifie les niveux de gris de l'image et on effectue le ceuillage
    imgQ = quantification(img_gray,m)
    result = ceuillage(imgQ,fil)
    
    return result

#Ordered threshold - Clustered dots
s1 = numpy.array([[34, 25, 21, 17, 29, 33],
                  [30, 13, 9 , 5 , 12, 24],
                  [18, 6 , 1 , 0 , 8 , 20],
                  [22, 10, 2 , 3 , 4 , 16],
                  [26, 14, 7 , 11, 15, 28],
                  [35, 31, 19, 23, 27, 32]])
                 
#Ordered matrix with central white point
s2 = numpy.array([[34, 25, 21, 17, 29, 33],
                  [30, 13, 9 , 5 , 12, 24],
                  [18, 6 , 1 , 0 , 8 , 20],
                  [22, 10, 2 , 3 , 4 , 16],
                  [26, 14, 7 , 11, 15, 28],
                  [35, 31, 19, 23, 27, 32]])

#Ordered matrix with balanced centered point
s3 = numpy.array([[30, 22, 16, 21, 33, 35],
		       [24, 11, 7 , 9 , 26, 28],
		       [13, 5 , 0 , 2 , 14, 19],
		       [15, 3 , 1 , 4 , 12, 18],
		       [27, 8 , 6 , 10, 25, 29],
		       [32, 20, 17, 23, 31, 34]])                
        
#ss = ss+0.5
#D = 255./36.
result = orderedThreshold("Lenna.png",s3)
io.imshow(result)
#io.show()