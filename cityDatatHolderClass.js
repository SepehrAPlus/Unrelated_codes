//اینو بزار اول کدت
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

//اینو  بزار جای خط 11 تا 14
let IranCityData = new MainCityDataHolder(
  {tehran : "data1",yazd : "data2",})


//اینوطوریم ازش داده شهر رو بگیر 
// اگر شهر وجود ندشته باشه میزنه "NO_DATA"
console.log(IranCityData.get_city_data("kerman"))
