import coeffs

def readXYZ(fileName):
    # чтение из файла трёх сигналов осей X Y и Z
    file = open(fileName + '.txt' , 'r')
    strings = []
    X = []
    Y = []
    Z = []
    for line in file:
        strings.append(line)
    file.close()
    # распределение трёх чисел из каждой строки файла в определённый список
    for line in strings:
        ind1 = line.find(' ')
        ind2 = line.find(' ', ind1 + 2)
        X.append(float(line[0:ind1]))
        Y.append(float(line[ind1 + 1:ind2]))
        Z.append(float(line[ind2 + 1:len(line)]))
    return X,Y,Z

def writeXYZ(fileName,X_btt,Y_btt,Z_btt, X_cb,Y_cb,Z_cb, X_bp,Y_bp,Z_bp):
    #функкция записи отфильтрованных сигналов в соответствующие файлы

    #папка в которой хранятся все отфильтрованные записи
    package = 'filtered signals/'

    file = open(package + fileName + '_butt' + '.txt','w')
    for i in range(len(X_btt)):
        file.write(str(X_btt[i]) + ' ' + str(Y_btt[i]) + ' ' + str(Z_btt[i]) + '\n')
    file.close()

    file = open(package + fileName + '_cheb' + '.txt','w')
    for i in range(len(X_cb)):
        file.write(str(X_cb[i]) + ' ' + str(Y_cb[i]) + ' ' + str(Z_cb[i]) + '\n')
    file.close()

    file = open(package + fileName + '_bandpass' + '.txt','w')
    for i in range(len(X_bp)):
        file.write(str(X_bp[i]) + ' ' + str(Y_bp[i]) + ' ' + str(Z_bp[i]) + '\n')
    file.close()

def IIRfilterXYZ(X,Y,Z,a,b):
    # применение БИХ фильтра для сигналов осей X Y и Z используя коэффициенты числителя (b) и знаменателя ПФ
    # сигналы после фильтрации
    X_f = [0 for i in range(len(X))]
    Y_f = [0 for i in range(len(Y))]
    Z_f = [0 for i in range(len(Z))]

    for i in range(len(X)):
        for j in range(len(a)):
            if (i - j) >= 0:
                X_f[i] = X_f[i] - a[j]*X_f[i-j]
                X_f[i] = X_f[i] + b[j]*X[i-j]

                Y_f[i] = Y_f[i] - a[j]*Y_f[i-j]
                Y_f[i] = Y_f[i] + b[j]*Y[i-j]

                Z_f[i] = Z_f[i] - a[j]*Z_f[i-j]
                Z_f[i] = Z_f[i] + b[j]*Z[i-j]
    return X_f,Y_f,Z_f

def FIRfilterXYZ(X,Y,Z,c):
    # применение КИХ фильтра имеющего коэффциенты c (реализация свёртки)
    # сигналы после фильтрации
    X_f = [0 for i in range(len(X))]
    Y_f = [0 for i in range(len(Y))]
    Z_f = [0 for i in range(len(Z))]

    for i in range(len(X)):
        for j in range(len(c)):
            if (i-j)>=0:
                X_f[i] =  X_f[i] + c[j] * X[i-j]
                Y_f[i] =  Y_f[i] + c[j] * Y[i-j]
                Z_f[i] =  Z_f[i] + c[j] * Z[i-j]
    return X_f,Y_f,Z_f

def filtration(fileName,a_butt,b_butt,a_chb,b_chb,c_bp):
    X,Y,Z = readXYZ(fileName)
    X_btt,Y_btt,Z_btt = IIRfilterXYZ(X,Y,Z,a_butt,b_butt)
    X_chb,Y_chb,Z_chb = IIRfilterXYZ(X,Y,Z,a_chb,b_chb)
    X_bp,Y_bp,Z_bp = FIRfilterXYZ(X,Y,Z,c_bp)
    writeXYZ(fileName,X_btt,Y_btt,Z_btt,X_chb,Y_chb,Z_chb,X_bp,Y_bp,Z_bp)


filtration('xyz_100Hz', coeffs.a_butt_100, coeffs.b_butt_100,
                     coeffs.a_cheb_100, coeffs.b_cheb_100,
                     coeffs.bandPass_100)


filtration('xyz_200Hz', coeffs.a_butt_200, coeffs.b_butt_200,
                     coeffs.a_cheb_200, coeffs.b_cheb_200,
                     coeffs.bandPass_200)


filtration('xyz_300Hz', coeffs.a_butt_300, coeffs.b_butt_300,
                     coeffs.a_cheb_300, coeffs.b_cheb_300,
                     coeffs.bandPass_300)

