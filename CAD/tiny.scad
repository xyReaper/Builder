slope = 20;
//degrees of the cut

//cut:
b_1=15;
b_3=10;
b_2=((b_3)*tan(slope));

//universal dimen
width=2;
length=(2);

module rectangle()
 {  //translate([-3.25, -15, 0])
    cube([length,width,2]);
 }

module slot ()
{  cube([b_3,width,2]);
}
module origin_slot ()
{  union()
    {
      cube([width/5,width,h]); 
        
      translate([1-width/2,width/2-1,0])
      cube([width,width/5,h]);       
    }
}

module hole()
{
 cylinder(3.6, r = 2.2, $fa=5, $fs=0.1);
}

    module prism(l, w, h) {
       polyhedron(points=[
               [0,0,h],           // 0    front top corner
               [0,0,0],[w,0,0],   // 1, 2 front left & right bottom corners
               [0,l,h],           // 3    back top corner
               [0,l,0],[w,l,0]    // 4, 5 back left & right bottom corners
       ], 
        faces=[ // points for all faces must be ordered clockwise when looking in
               [0,2,1],    // top face
               [3,4,5],    // base face
               [0,1,4,3],  // h face
               [1,2,5,4],  // w face
               [0,3,5,2],  // hypotenuse face
       ]);
}



    rectangle();

    
   