// gsap animation movement : x denote x axis , y denote y axis accept both type vaue (+ve and -ve)

// gsap.to()  we we move element from initial to final position
// gsap.from()  we we move element from final to initial position

gsap.to(".box1", {
  x: 1000,
  duration: 2,
  delay: 1,
  rotate: 360,
  backgroundColor: "crimson",
});

gsap.to(".box2", {
  x: 350,
  y: -300,
  duration: 2,
  delay: 1,
});

gsap.from(".box3", {
  x: 1000,
  duration: 2,
  delay: 1,
});
