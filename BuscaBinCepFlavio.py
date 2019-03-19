import struct
import sys

if len(sys.argv) != 2:
    print ("USO %s [CEP]" % sys.argv[0])
    quit()

registroCEP = struct.Struct("72s72s72s72s2s8s2s")
cepColumn = 5
print ('')
f = open("cep_ordenado.dat","rb")
ini = 0
f.seek(0,2)
end = f.tell()/registroCEP.size-1
counter = 0
while ini <= end:
    mid = int((ini+end)/2)
    f.seek(mid*registroCEP.size)
    line = f.read(registroCEP.size)
    record = registroCEP.unpack(line)
    cep = str(record[cepColumn],'latin1')
    counter += 1    
    if cep == sys.argv[1]:
        for i in range(0,len(record)-1):
            print (str(record[i],'latin1'))
        break
    elif cep < sys.argv[1]:
        ini = mid+1
    else:
        end = mid-1    

print ("Total de Registros Lidos: %d" % counter)
f.close()