use std::io;
use std::io::*;
fn main(){


let mut pnum = String::new().parse();
let mut qnum = String::new().parse();
let mut num = 1;
io::stdin::().read_line(&mut pnum);
io:stdin::().read_line(&mut qnum);

let mut N = pnum * qnum;
let mut phiN = (pnum-1) * (qnum-1);

coprime1(num);
println!("The encryption key is {},{}",num, N);
findingD(num, phiN);
println!("The decryption key is {},{}", D, N);


}
fn coprime1(pnum, qnum, num){
for(let mut i = 1, i<=pnum, i++)
{
	if(qnum%num==0 && num%i==0)
	let mut hcf = i;
	if(hcf == 1)
	{
		let mut coprimewithQ = true;
	}
	if(pnum%num==0 && num%i==0)
	{
	let mut coprimewithP = true;	
	}
	
	if(coprimewithP == true && coprimewithQ == true)
	{
	break;	
	}
	
	if(coprimewithP != true || coprimewithQ != true)
	{
	let mut num = num++;	
	}
}
}
fn findingD(num, phiN)
{
	for(let mut i2 = 1, i2 <=100000000000000000000, i2++)
	{
	let mut D = 0;
	for(D * num * phiN != 1)
	{
	D++	
	}
	if(D * num * phiN == 1)
	{
	let mut foundDecryptionKey = true;
	break;
	}
	}
}
