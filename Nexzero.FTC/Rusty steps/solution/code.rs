
fn main() {
    let mut parts = Vec::new();
    parts.push((0x6E ^ 0x0A) as u8); // 'n' → 0x64
    parts.push(0x65);                // 'e' 
    parts.push((0x78 ^ 0x01) as u8); // 'x' → 0x79
    parts.push((0x75 - 1) as u8);    // 'u' → 0x74
    parts.push((0x73 ^ 0x02) as u8); // 's' → 0x71
    parts.push(0x7B);                // '{'
    parts.extend([0x52, 0x75, 0x73, 0x54]); // 'RusT'
    parts.push(0x5F);                // '_'
    parts.extend([0x52, 0x33, 0x76]); // 'R3v'
    parts.push(0x5F);                // '_'
    parts.extend([0x31, 0x35]);       // '15'
    parts.push(0x5F);                // '_'
    parts.extend([0x46, 0x75, 0x6E]); // 'Fun'
    parts.push(0x5F);                // '_'
    parts.push(0x52 ^ 0x0F as u8); //Right
    parts.push(0x69 ^ 0xE0 as u8);
    parts.push(0x67 + 0x02 as u8);
    parts.push(0x68 ^ 0x33 as u8);
    parts.push(0x74 ^ 0x05 as u8);
    parts.push(0x7D);                // '}'

    let flag: String = parts.iter().enumerate().map(|(i, &x)| {
        match i {
            0 => (x ^ 0x0A) as char,  // 
            2 => (x ^ 0x01) as char,  // 
            3 => (x + 1) as char,     // 
            4 => (x ^ 0x02) as char,
            // Reverse XOR for 's' (0x71 → 0x73)
            22 => (x ^ 0x0F) as char ,
            23 => (x ^ 0xE0) as char ,
            24 => (x - 0x02 ) as char ,
            25 => (x ^ 0x33) as char,
            26 => (x ^ 0x05 ) as char ,
            _ => x as char,           
        }
    }).collect();

    // Check user input
    let mut input = String::new();
    println!("Enter the flag:");
    std::io::stdin().read_line(&mut input).unwrap();
    
    if input.trim() == flag {
        println!("Correct!");
    } else {
        println!("Incorrect!");
    }
}
