JSONObject json;
int max;
int minMin;

void setup() {
  size(841,594);

JSONArray jsonArray = loadJSONArray("january_2016.json");
JSONObject jsonObject = jsonArray.getJSONObject(0); 
JSONObject maxTemperature = jsonObject.getJSONObject("Max Temperature");
max = maxTemperature.getInt("max");

  print(max);
}

void draw(){
//Max Temperature  
  textAlign(CENTER);
  text("Max Temperature",841/4, 594/2+100);

  ellipseMode(RADIUS);
  ellipse(841/4, 594/2, max, max); // max
  //ellipse(841/4, 594/2, 5*2, 5*2); //avg
  //ellipse(841/4, 594/2, 2*2, 2*2); //min
  
  //Mean Temperature
  textAlign(CENTER);
  text("Mean Temperature",841/4*2, 594/2+100);
  
  ellipse(841/4*2, 594/2, 10*2, 10*2); // max
  ellipse(841/4*2, 594/2, 5*2, 5*2); //avg
  ellipse(841/4*2, 594/2, 2*2, 2*2); //min

  //Min Temperature
  textAlign(CENTER);
  text("Min Temperature",841/4*3, 594/2+100);
  
  ellipse(841/4*3, 594/2, 10*2, 10*2); // max
  ellipse(841/4*3, 594/2, 5*2, 5*2); //avg
  ellipse(841/4*3, 594/2, 2*2, 2*2); //min
}