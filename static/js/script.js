
// JavaScript Document



function validate(){
	
	var fname = document.getElementById('fname').value;
	var lname = document.getElementById('lname').value;
	var phone = document.getElementById('phone').value;
	var pswd1 = document.getElementById('password1').value;
	var pswd2 = document.getElementById('password2').value;

	
	if(isNaN(fname) && fname.length>3){
		
	
		document.getElementById('errfname').innerHTML="";
		
		if(isNaN(lname)){
		
			
			document.getElementById('errlname').innerHTML="";
			
			if(phone.length===10){
	
				document.getElementById('errphone').innerHTML="";
				
				
				if(pswd1===pswd2){
					if(pswd1.length>6 && pswd2.length>6)
					{
					return true;
					}
					else{
						document.getElementById('passwd').innerHTML="Password is Weak <br> Please use Alphanbets and Numbers to Make strong password";
						document.form1.password1.focus();
						return false;
					}
					
				
				}
				else{
					document.getElementById('passwd').innerHTML="Password miss match";
			document.form1.password1.focus();
				return false;
				}		
				
				
				
				
				
			}
			else{
				document.getElementById('errphone').innerHTML="Please Ente Valid Phone Number";
			document.form1.phone.focus();
				return false;
			}
			
		}
		else{
			document.getElementById('errlname').innerHTML="Please Ente Valid name";
			document.form1.lname.focus();
			return false;
		}
	}
		else{
			document.getElementById('errfname').innerHTML="Please Ente Valid name";
			document.form1.fname.focus();
			return false;
		}
			alert('last');
			return false;
			
	
	
	

	
	
}
