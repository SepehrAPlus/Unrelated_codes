class MainCityDataHolder {
 	constructor(city_data_object){
    	this.city_data_object = city_data_object;
    }
  
  	
  	get_city_data(city_name) {
     	let output = this[city_name];
      	console.log(output);
        if (output === undefined){return "NO_DATA";}
      	return output;
          
    }
}



let IranCityData = new MainCityDataHolder(
  {tehran : "data1",yazd : "data2",})

console.log(IranCityData.get_city_data("kerman"))
