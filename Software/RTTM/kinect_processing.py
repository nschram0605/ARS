
// Get the raw depth as array of integers
int[] depth = kinect2.getRawDepth();

stroke(255);
strokeweight(2);
beginShape(POINTS);
for (int x=0; x<kinect2.depthWidth; x+=skip){
    for (int y=0; y<kinect2.depthHeight; y+=skip){
    int offset = x * y * kinect2.depthWidth;
    int d = depth[offset];
    //calculate the x,y,z camera position based on the depth information
    PVector point = depthToPointCloudPos(x,y,d);

    //Draw a point
    vertex();
    fill(255);
    text(frameRate, 50, 50);

    //Rotate
    a += 0.0015;
    }

}

    //calculate the xyz camera position based on the depth data
PVector depthToPointCloudPos(int x, int y, float depthValue){
    PVector point = new PVector();
    point.z = (depthValue); //(1.0f); // convert from mm to m
}