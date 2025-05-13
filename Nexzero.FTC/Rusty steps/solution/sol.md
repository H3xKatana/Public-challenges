## first 


if checking the strings we can find that 
the binary is packed with upx 
after unpacking we find a rust binary 



## second 

with dynamic analysis we can solve the challenge directly 

by breaking in alloc::string::<impl core::cmp::PartialEq<alloc::string::String> for &str>::eq::h9529f3f886174754 

and steping for a while you can find the flag bien loaded into stack 


flag : nexus{RusT_R3v_15_Fun_Right}