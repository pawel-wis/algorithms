var zad3 = (a, b) => {
	if( a == b) return a
	if((a && b) == 0) return console.log('Zero/Zero')
	if(a == 0 ) return b;
	if(b == 0) return a;
	if(b > a){
		t = a
		a = b
		b = t
	}

	var temp = b % a
	var greater = 0

	for(i=1; i <= temp; i++){
		if((temp % i == 0) && (a % i) == 0) greater = i
	}

	return greater
}
