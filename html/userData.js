$(document).ready(function(){
        	$.getJSON("http://10.10.2.47/cgi-bin/lab2ajax.py",function(data,status){
                	tableEntry="";
			for (var ip in data){
				var os = data[ip]['OS'];
				console.log(os);
				tableEntry+='<tr><td>'+ip+'</td><td>'+os+'</td>';
				for (var service in data[ip]['services']){
					console.log(data[ip]['services'][service]);
					tableEntry+='<td>'+service+'</td>';
				
				}

			tableEntry+="</tr>";
			}
			document.getElementById("users").innerHTML+=tableEntry;
        	});     
});
