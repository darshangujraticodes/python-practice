// gsap animation movement : x denote x axis , y denote y axis accept both type vaue (+ve and -ve)

// gsap.to()  we we move element from initial to final position
// gsap.from()  we we move element from final to initial position

gsap.to(".box1", {
  x: 1000,
  duration: 2,
  delay: 1,
  rotate: 360,
  backgroundColor: "crimson",
  borderRadius: "50%",
  scale: 0.5,
  // repeat -1 is given to animate for unlimited time
  repeat: -1,
  // yoyo provide returning back effect
  yoyo: true,
});

gsap.to(".box2", {
  x: 1000,
  scale: 0.5,
  duration: 2,
  repeat: -1,
  delay: 1,
  yoyo: true,
});

// headText animation

gsap.from(".headText", {
  opacity: 0,
  y: 20,
  duration: 1,
  delay: 0.5,
  stagger: 0.4,
});

// timeline  is an animation told that arrages all animating objectin in one thread an

// Here in this timeline we are binding multiple elements animation in common timeline to synchronize their animation sequence one after another

var navTimeline = gsap.timeline();

navTimeline.from(".logoHead", {
  opacity: 0,
  y: -20,
  duration: 0.6,
  delay: 0.5,
});

navTimeline.from(".navMenu", {
  opacity: 0,
  y: -20,
  duration: 0.6,

  // stagger divide multiple group animation in sequence line order animation like menu option after removing this all will load up in same time
  stagger: 0.4,
});
