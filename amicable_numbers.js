var zad1 = (liczba1, liczba2) => {
	suma1=0;
	suma2=0;
	for(i=1;i < liczba1;i++){
		if((liczba1 % i) == 0) suma1 += i;
		if(suma1 > liczba2) return false;
	}

	for(i=1;i<liczba2;i++){
		if((liczba2 % i) == 0) suma2 +=i ;
		if(suma2 > liczba1) return false;
	}

	if((suma1 != liczba2) && (suma2 != liczba1)) return false;


	return true;
}


