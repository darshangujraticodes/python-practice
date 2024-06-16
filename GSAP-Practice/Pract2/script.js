gsap.from(".headText", {
  opacity: 0,
  y: -20,
  duration: 2,
  delay: 1,
});

gsap.from(".box1", {
  opacity: 0,
  rotate: 360,
  scale: 0,
  duration: 2,
  delay: 1,
});

gsap.from(".box3", {
  opacity: 0,
  rotate: 360,
  scale: 0,
  duration: 2,
  scrollTrigger: {
    trigger: ".section3 .box3",
    scroller: "body",
    start: "top 60%",
    // it restrict animation to mouse scroll movement
    scrub: true,
  },
});

gsap.from(".leftAnime", {
  opacity: 0,
  x: 50,
  duration: 0.7,
  stagger: 0.4,
  scrollTrigger: {
    trigger: ".leftAnime",
    scroller: "body",
    // markers: true,
    start: "top 50%",
  },
});

gsap.from(".rightAnime", {
  // scale: 0,
  opacity: 0,
  x: -50,
  duration: 1,
  stagger: 0.4,
  scrollTrigger: {
    trigger: ".leftAnime",
    scroller: "body",
    // markers: true,
    start: "top 50%",
  },
});

gsap.from(".upAnime", {
  // scale: 0,
  opacity: 0,
  y: 50,
  duration: 1,
  stagger: 0.4,
  scrollTrigger: {
    trigger: ".upAnime",
    scroller: "body",
    start: "top 40%",
  },
});

gsap.from(".downAnime", {
  // scale: 0,
  opacity: 0,
  y: -50,
  duration: 1,
  stagger: 0.4,
  scrollTrigger: {
    trigger: ".downAnime",
    scroller: "body",
    // markers: true,
    start: "top 50%",
  },
});
