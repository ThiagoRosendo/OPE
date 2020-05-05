function capitalize(campoFormulario) {
	
	var string = document.getElementById(campoFormulario).value;
	
	if(string.length > 0) {
	
		string = string.toLowerCase();
		string = string.split(' ');
		
        for (var i = 0, len = string.length; i < len; i++) {
			
			if(string[i].length > 2) {
				
				string[i] = string[i].charAt(0).toUpperCase() + string[i].slice(1);
				
			};
			
        };
		
		document.getElementById(campoFormulario).value = string.join(' ');
		return true;
		
	}
	
}

