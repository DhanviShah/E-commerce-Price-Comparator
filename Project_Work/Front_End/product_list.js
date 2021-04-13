var p2 = document.querySelectorAll(".inul");
// var p = document.querySelectorAll(".b");

// console.log(p);
var sources = ["https://www.techinn.com/f/13735/137354157/apple-iphone-11-128gb-6.1.jpg",
"https://images-na.ssl-images-amazon.com/images/I/61VK5q8L-oL._SL1024_.jpg",
"https://img.tatacliq.com/images/i7/1348Wx2000H/MP000000008075553_1348Wx2000H_202011300236391.jpeg"];

for(var i=0; i<3; i++){
	function fun(idx){
		p2[idx].addEventListener("click" , function(){
			var d = document.querySelector(".jkl");
			d.src = sources[idx];
		});
	}
	fun(i);
}

// for(var i=0; i<5; i++){
// 	function fun1(idx){
// 		p[idx].addEventListener("mouseenter" , function(){
// 			var d1 = document.querySelectorAll(".pqrs");
// 			var d2 = document.querySelectorAll(".jkl");
// 			var d3 = document.querySelectorAll("h2");
// 			var d4 = document.querySelectorAll(".navi");

// 			for(var j=0; j<d4.length; j++) d4[j].classList.add("another-class");
// 			p[idx].classList.add("another-class");
// 			for(var j=0; j<d1.length; j++) d1[j].classList.add("some-class");
// 			for(var j=0; j<d2.length; j++) d2[j].classList.add("some-class");
// 			for(var j=0; j<d3.length; j++) d3[j].classList.add("some-class");
// 		});

// 		p[idx].addEventListener("mouseleave" , function(){
// 			var d1 = document.querySelectorAll(".pqrs");
// 			var d2 = document.querySelectorAll(".jkl");
// 			var d3 = document.querySelectorAll("h2");

// 			for(var j=0; j<d4.length; j++) d4[j].classList.remove("another-class");
// 			p[idx].classList.remove("another-class");
// 			for(var j=0; j<d1.length; j++) d1[j].classList.remove("some-class");
// 			for(var j=0; j<d2.length; j++) d2[j].classList.remove("some-class");
// 			for(var j=0; j<d3.length; j++) d3[j].classList.remove("some-class");
// 		});
// 	}
// 	fun1(i);
// }