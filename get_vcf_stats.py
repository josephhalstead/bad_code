"""
Parse a BED file and generate some statistics
"""

from pysam import VariantFile


vcf = "NA12878.trio.sorted.snps.vcf.gz"

Variantfile = VariantFile(vcf)

out = 'out.stats'


# chromsomes
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count10 = 0
count11 = 0
count12 = 0
count13 = 0
count14 = 0
count15 = 0
count16 = 0
count17 = 0
count18 = 0
count19 = 0
count20 = 0
count21 = 0
count22 = 0
count23 = 0
xCount = 0
yCount = 0 
mt_count = 0

knownPathogenicVariants = 1

# loop through each line in vcf
for i in Variantfile.fetch():

	# open output file
	f = open(out, 'w')

	#print(i)

	c = i.chrom
	pos = i.pos
	ref = i.ref
	alts = i.alts

	k = c + "-" + str(pos) + '-' +  ref + '-' +  alts[0]

	if c == '1':

		count1 = count1 + 1

	else:

		pass

	if c == '2':

		count2 = count2 + 1

	elif c == '3':

		count3 = count2 + 1

	if c == '4':

		count4 = count4 + 1

	if c == '5':

		count5 = count5 + 1

	if c == '6':

		count6 = count6 + 1

	if c == '7':

		count7 = count7 + 1

	if c == '8':

		count8 = count8 + 1

	if c == '9':

		count9 = count9 + 1

	if c == '10':

		count10 = count10 + 1

	if c == '11':

		count11 = count11 + 1

	if c == '12':

		count12 = count12 + 1

	if c == '13':

		count13 = count13 + 1

	if c == '14':

		count14 = count14 + 1

	if c == '15':

		count15 = count15 + 1

	if c == '16':

		count16 = count16 + 1

	if c == '17':

		count17 = count17 + 1

	if c == '18':

		count18 = count18 + 1

	if c == '19':

		count19 = count19 + 1

	if c == '20':

		count20 = count20 + 1

	if c == '21':

		count21 = count12 + 1

	if c == '22':

		count22 = count22 + 1

	if c == 'X':

		xCount = xCount + 1

	if c == "Y":

		yCount = yCount + 1



	known_pathogenic = 'known_pathogenic.txt'

	f2 = open(known_pathogenic)
	variants = f2.read()

	if k in variants:

		knownPathogenicVariants = knownPathogenicVariants +1


f.write('chrom1,' + str(count1) + '\n')
f.write('chrom2,' + str(count2)+ '\n')
f.write('chrom3,' + str(count3)+ '\n')
f.write('chrom4,' + str(count4)+ '\n')
f.write('chrom5,' + str(count5)+ '\n')
f.write('chrom6,' + str(count6)+ '\n')
f.write('chrom7,' + str(count7)+ '\n')
f.write('chrom8' + str(count8)+ '\n')
f.write('chrom9,' + str(count9)+ '\n')
f.write('chrom10,' + str(count10)+ '\n')
f.write('chrom11,' + str(count11)+ '\n')
f.write('chrom12,' + str(count12)+ '\n')
f.write('chrom13,' + str(count13)+ '\n')
f.write('chrom14,' + str(count14)+ '\n')
f.write('chrom15,' + str(count15)+ '\n')
f.write('chrom16,' + str(count16)+ '\n')
f.write('chrom17,' + str(count17)+ '\n')
f.write('chrom18,' + str(count18)+ '\n')
f.write('chrom19,' + str(count19)+ '\n')
f.write('chrom20,' + str(count20)+ '\n')
f.write('chrom21,' + str(count21)+ '\n')
f.write('chrom22,' + str(count22)+ '\n')
f.write('chromX,' + str(xCount)+ '\n')
f.write('chromY,' + str(yCount)+ '\n')
f.write('known_pathogenic,' + str(knownPathogenicVariants)+ '\n')
