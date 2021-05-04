var p2 = document.querySelectorAll(".pqr");
var para = document.querySelector(".desc");
var p3 = document.querySelector(".pppp");

// console.log(p);
var sources = ["https://www.techinn.com/f/13735/137354157/apple-iphone-11-128gb-6.1.jpg",
"https://images-na.ssl-images-amazon.com/images/I/61VK5q8L-oL._SL1024_.jpg",
"https://img.tatacliq.com/images/i7/1348Wx2000H/MP000000008075553_1348Wx2000H_202011300236391.jpeg",
"https://images-na.ssl-images-amazon.com/images/I/61m6DjujESL._SL1024_.jpg",
"https://cdn.vox-cdn.com/thumbor/SDDEa6E8l5Nu18-ZTkQa3n1Iev0=/1400x0/filters:no_upscale()/cdn.vox-cdn.com/uploads/chorus_asset/file/19206371/akrales_190914_3628_0262.jpg"
];

for(var i=0; i<5; i++){
	function fun(idx){
		p2[idx].addEventListener("click" , function(){
			var d = document.querySelector(".jkl");
			d.src = sources[idx];

			p2[idx].classList.add("border-class");
		});

		p2[idx].addEventListener("mouseenter",function(){
			var d = document.querySelector(".jkl");
			d.src = sources[idx];

			p2[idx].classList.add("border-class");
		});
		p2[idx].addEventListener("mouseleave",function(){
			var d = document.querySelector(".jkl");
			d.src = sources[idx];

			p2[idx].classList.remove("border-class");
		});
	}
	fun(i);
}

// var high = p3.style.height;
// prompt(high);
// console.log(para.style.height);

// p3.style.height = para.style.height;
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