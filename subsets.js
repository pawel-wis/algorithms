var a = [1,2,3,4,5,6,7]

count =Math.pow(2,a.length)

amount = 0
for(i=0; i < count; i++){
	for(j=0; j<a.length;j++){
		if((i & (1 << j)) > 0) {process.stdout.write(`${a[j]} `)}
	}
	console.log()
	amount++
}
