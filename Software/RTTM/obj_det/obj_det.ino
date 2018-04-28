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

//Initialization
int ind_array[12];
for (int i=0; i<global_detection_threshold; i++){
  ind_array[i] = 0;
}

//Boolean flags
bool zone_array[12];

int global_detection_threshold = 128;
int global_num_inductors = 12;

//Counters
int i, j, k;

//------------------------------------------------
//Comment/Uncomment for Serial Port Debug Printing
#define serial_debug
//------------------------------------------------

//Function Prototypes
void read_inductors(void);
int determine_detection_zone(void);
void serial_output(int detection_zone_array[]);

/**
 * @file obj_det.ino
 * @function void setup()
 * @brief initialize the serial port to 9600 baud
 * @author n.schram
 * @date 2018-APRL-27
 */
void setup() {
  Serial.begin(9600);
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
  //Read all inductor values
  read_inductors();

  //Determine if a detection is present
  //Output serial stream to python program
  serial_output(determine_detection_zone());
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
  ind_array[1] = analogRead(inductor_1_pin);
  ind_array[2] = analogRead(inductor_2_pin);
  ind_array[3] = analogRead(inductor_3_pin);
  ind_array[4] = analogRead(inductor_4_pin);
  ind_array[5] = analogRead(inductor_5_pin);
  ind_array[6] = analogRead(inductor_6_pin);
  ind_array[7] = analogRead(inductor_7_pin);
  ind_array[8] = analogRead(inductor_8_pin);
  ind_array[9] = analogRead(inductor_9_pin);
  ind_array[10] = analogRead(inductor_10_pin);
  ind_array[11] = analogRead(inductor_11_pin);
  ind_array[12] = analogRead(inductor_12_pin);
}

/**
 * @file obj_det.ino
 * @function int determine_detection(void)
 * @brief 
 * @author n.schram
 * @date 2018-APRL-27
 */
int determine_detection_zone(void){
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
  for (int i = 1; i<global_num_inductors; i++){
    if (ind_array[i] >= global_detection_threshold){
      zone_array[i] = 1;
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
void serial_output(int detection_zone_array[]){
  char output_string = 'na'

  for (i=0; i<global_detection_threshold; i++){
    switch (detection_zone_array[i]){
    case 1:
      output_string = 'A';
      #ifdef serial_debug
      println("Zone: A");
      #endif
    case 2:  
      output_string = 'B';
      #ifdef serial_debug
      println("Zone: B");
      #endif
    case 3:
      output_string = 'C';
      #ifdef serial_debug
      println("Zone: C");
      #endif
    case 4:
      output_string = 'D';
      #ifdef serial_debug
      println("Zone: D");
      #endif
    case 5:
      output_string = 'E';
      #ifdef serial_debug
      println("Zone: E");
      #endif
    case 6:
      output_string = 'F';
      #ifdef serial_debug
      println("Zone: F");
      #endif
    case 7:
      output_string = 'G';
      #ifdef serial_debug
      println("Zone: G");
      #endif
    case 8:
      output_string = 'H';
      #ifdef serial_debug
      println("Zone: H");
      #endif
    case 9:
      output_string = 'I';
      #ifdef serial_debug
      println("Zone: I");
      #endif
    case 10:
      output_string = 'J';
      #ifdef serial_debug
      println("Zone: J");
      #endif
    case 11:
      output_string = 'K';
      #ifdef serial_debug
      println("Zone: K");
      #endif
    case 12:
      output_string = 'L';
      #ifdef serial_debug
      println("Zone: L");
      #endif
    case default:
      output_string = 'N/A';
      #ifdef serial_debug
      println("NO DETECTION");
      #endif
    }
    Serial.println(output_string);
  }
  
}

