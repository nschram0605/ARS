////////////////////////////////////////////////////////////////////////////
///
/// program: obj_det.ino
///
/// author: n.schram
///
/// date: 2018-APRL-27
///
/// description: the purpose of this file is to read in the analog inductor value and
/// determine the zone and then send the zone identifier out through the
/// serial port to the python script which will read it in.
///
////////////////////////////////////////////////////////////////////////////


//Constants
//Inductors (x12)
//Each inductor number correlates to a terminal location on the purple PCB
const int inductor_1_pin = A1;
const int inductor_2_pin = A2;
const int inductor_3_pin = A3;
const int inductor_4_pin = A4;
const int inductor_5_pin = A5;
const int inductor_6_pin = A6;
const int inductor_7_pin = A7;
const int inductor_8_pin = A8;
const int inductor_9_pin = A9;
const int inductor_10_pin = A10;
const int inductor_11_pin = A11;
const int inductor_12_pin = A12;

//Counters
int i = 0;
int j = 0;
int k = 0;

//Inductor Array Values
int ind_array[13];
//Boolean flags
bool zone_array[13];

int global_detection_threshold = 875;
int global_num_inductors = 12;
int global_count = 100;
long int averaged_ind[13];


//------------------------------------------------
//Comment/Uncomment for Serial Port Debug Printing
//#define serial_debug 1
//#define serial_debug_
//#define zone_debug 1
//------------------------------------------------

//Function Prototypes
void read_inductors(void);
void determine_detection_zone(void);
void serial_output(void);
void clear_averaged_values(void);

/**
 * @file obj_det.ino
 * @function void setup()
 * @brief initialize the serial port to 9600 baud
 * @author n.schram
 * @date 2018-APRL-27
 */
void setup() {
  Serial.begin(115200);

  //Initialization
  for (i=1; i<global_num_inductors+1; i++){
    ind_array[i] = 0;
    zone_array[i] = 0;
    averaged_ind[i] = 0;
  }
}

/**
 * @file obj_det.ino
 * @function void loop()
 * @brief main loop that reads the inductors, determines the zone of 
 * detection and outputs the zone string out the serial port.
 * @author n.schram
 * @date 2018-APRL-27
 */
void loop() {
  
  if (j < global_count){
    //Read all inductor values and average
    read_inductors();
  }
  //clear the average and continue on
  else if (j == global_count){
    take_the_average();

    //Determine if a detection is present
    determine_detection_zone();

    //Clear the previous averaages
    clear_averaged_values();
    j = 0;
  }
  
  //Output serial stream to python program
  serial_output();

  //10ms delay
  delay(1000);

  //j is the main loop counter used for averaging
  j++;
}

/**
 * @file obj_det.ino
 * @function void read_inductors(void)
 * @brief read the analog value for each inductor and store it into the 
 * appropriate index in the inductor array
 * @author n.schram
 * @date 2018-APRL-27
 */
void read_inductors(void){


  ind_array[12] = analogRead(inductor_12_pin);
  ind_array[11] = analogRead(inductor_11_pin);
  ind_array[10] = analogRead(inductor_10_pin);
  ind_array[9] = analogRead(inductor_9_pin);
  ind_array[8] = analogRead(inductor_8_pin);
  ind_array[7] = analogRead(inductor_7_pin);
  ind_array[6] = analogRead(inductor_6_pin);
  ind_array[5] = analogRead(inductor_5_pin);
  ind_array[4] = analogRead(inductor_4_pin);
  ind_array[3] = analogRead(inductor_3_pin);
  ind_array[2] = analogRead(inductor_2_pin);
  ind_array[1] = analogRead(inductor_1_pin);

  averaged_ind[12] = averaged_ind[12] + ind_array[12];
  averaged_ind[11] = averaged_ind[11] + ind_array[11];
  averaged_ind[10] = averaged_ind[10] + ind_array[10];
  averaged_ind[9] = averaged_ind[9] + ind_array[9];
  averaged_ind[8] = averaged_ind[8] + ind_array[8];
  averaged_ind[7] = averaged_ind[7] + ind_array[7];
  averaged_ind[6] = averaged_ind[6] + ind_array[6];
  averaged_ind[5] = averaged_ind[5] + ind_array[5];
  averaged_ind[4] = averaged_ind[4] + ind_array[4];
  averaged_ind[3] = averaged_ind[3] + ind_array[3];
  averaged_ind[2] = averaged_ind[2] + ind_array[2];
  averaged_ind[1] = averaged_ind[1] + ind_array[1];
}

/**
* @file obj_det.ino
* @function 
* @brief 
* @author n.schram
* @date 2018-APRL-28
*/ 
void clear_averaged_values(void){
  for (i=1; i<global_num_inductors+1; i++){
    averaged_ind[i] = 0;
    zone_array[i] = 0;
  }
}

/**
* @file obj_det.ino
* @function 
* @brief 
* @author n.schram
* @date 2018-APRL-28
*/ 
void take_the_average(void){
  for (i=1; i<global_num_inductors+1; i++){
    averaged_ind[i] = averaged_ind[i] / global_count;
  }
}

/**
 * @file obj_det.ino
 * @function int determine_detection(void)
 * @brief 
 * @author n.schram
 * @date 2018-APRL-27
 */
void determine_detection_zone(void){
//Total number of detection zones: 12
//40"x30" inner dimensions
// |-------40"-------|
// 13.3"  13.3"  13.3"
// -------------------     ---
// |     |     |     | 15"  |
// |A    |B    |C    |      30"
// -------------------      |
// |     |     |     | 15"  |
// |D    |E    |F    |      |
// -------------------     ---
// |----------- 40" -------|
// |-10"-|
// ------------------------- -------
// |  1  |  2  |  3  |  4  |  10" |
// |  A  |  B  |  C  |  D  |   |  |
// ------------------------- ---- |
// |  5  |  6  |  7  |  8  |      |
// |  E  |  F  |  G  |  H  |     30"
// -------------------------      |
// |  9  | 10  | 11  | 12  |      |
// |  I  |  J  |  K  |  L  |      |
// -------------------------     ---

//Determine which zones are detecting

  for (i = 1; i<global_num_inductors+1; i++){

    #ifdef zone_debug
    Serial.print("ind_array: ");
    Serial.print(i);
    Serial.print(" = ");
    Serial.println(ind_array[i]);
    #endif
    if (averaged_ind[i] >= global_detection_threshold){
      zone_array[i] = 1;
      #ifdef zone_debug
      Serial.print("zone_array: ");
      Serial.print(i);
      Serial.println(" = 1");
      #endif
    }
    else {
      zone_array[i] = 0;
    }
  }
}

/**
 * @file obj_det.ino
 * @function void serial_output(int detection_zone_array[])
 * @brief takes an array of zone indicators and outputs the zone identifier
 * to the python script through the serial port at 9600 baud.
 * @author n.schram
 * @date 2018-APRL-27
 */
void serial_output(void){

  if (zone_array[1] == 1){
    Serial.println("A");
    #ifdef serial_debug
    Serial.println("Zone: A");
    #endif
  }
  else {
    Serial.println("N/A");
    #ifdef serial_debug
    Serial.println("N/A, A");
    #endif
  }

  if (zone_array[2] == 1){
    Serial.println("B");
    #ifdef serial_debug
    Serial.println("Zone: B");
    #endif
  }
  else {
    Serial.println("N/A");
    #ifdef serial_debug
    Serial.println("N/A, B");
    #endif
  }

  if (zone_array[3] == 1){
    Serial.println("C");
    #ifdef serial_debug
    Serial.println("Zone: C");
    #endif
  }
  else {
    Serial.println("N/A");
    #ifdef serial_debug
    Serial.println("N/A, C");
    #endif
  }

  if (zone_array[4] == 1){
    Serial.println("D");
    #ifdef serial_debug
    Serial.println("Zone: D");
    #endif
  }
  else {
    Serial.println("N/A");
    #ifdef serial_debug
    Serial.println("N/A, D");
    #endif
  }

  if (zone_array[5] == 1){
    Serial.println("E");
    #ifdef serial_debug
    Serial.println("Zone: E");
    #endif
  }
  else {
    Serial.println("N/A");
    #ifdef serial_debug
    Serial.println("N/A, E");
    #endif
  }

  if (zone_array[6] == 1){
    Serial.println("F");
    #ifdef serial_debug
    Serial.println("Zone: F");
    #endif
  }
  else {
    Serial.println("N/A");
    #ifdef serial_debug
    Serial.println("N/A, F");
    #endif
  }

  if (zone_array[7] == 1){
    Serial.println("G");
    #ifdef serial_debug
    Serial.println("Zone: G");
    #endif
  }
  else {
    Serial.println("N/A");
    #ifdef serial_debug
    Serial.println("N/A, G");
    #endif
  }

  if (zone_array[8] == 1){
    Serial.println("H");
    #ifdef serial_debug
    Serial.println("Zone: H");
    #endif
  }
  else {
    Serial.println("N/A");
    #ifdef serial_debug
    Serial.println("N/A, H");
    #endif
  }

  if (zone_array[9] == 1){
    Serial.println("I");
    #ifdef serial_debug
    Serial.println("Zone: I");
    #endif
  }
  else {
    Serial.println("N/A");
    #ifdef serial_debug
    Serial.println("N/A, I");
    #endif
  }

  if (zone_array[10] == 1){
    Serial.println("J");
    #ifdef serial_debug
    Serial.println("Zone: J");
    #endif
  }
  else {
    Serial.println("N/A");
    #ifdef serial_debug
    Serial.println("N/A, J");
    #endif
  }

  if (zone_array[11] == 1){
    Serial.println("K");
    #ifdef serial_debug
    Serial.println("Zone: K");
    #endif
  }
  else {
    Serial.println("N/A");
    #ifdef serial_debug
    Serial.println("N/A, K");
    #endif
  }
  
  if (zone_array[12] == 1){
    Serial.println("L");
    #ifdef serial_debug
    Serial.println("Zone: L");
    #endif
  }
  else {
    Serial.println("N/A");
    #ifdef serial_debug
    Serial.println("N/A, L");
    #endif
  }
}

