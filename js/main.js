/* danielgarbozo.github.io: small progressive enhancements, no dependencies.
   Everything here is optional: the page is complete without JavaScript. */
(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Mobile menu ---------- */
  var toggle = document.querySelector(".menu-toggle");
  var navList = document.getElementById("nav-list");

  function setMenu(open) {
    if (!toggle || !navList) return;
    toggle.setAttribute("aria-expanded", String(open));
    navList.classList.toggle("is-open", open);
  }

  if (toggle && navList) {
    toggle.addEventListener("click", function () {
      setMenu(toggle.getAttribute("aria-expanded") !== "true");
    });
    navList.addEventListener("click", function (e) {
      if (e.target.closest("a")) setMenu(false);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
        setMenu(false);
        toggle.focus();
      }
    });
    document.addEventListener("click", function (e) {
      if (!e.target.closest(".nav")) setMenu(false);
    });
  }

  /* ---------- Hide the "|" separator on roles that start a wrapped line ---------- */
  var roles = Array.prototype.slice.call(document.querySelectorAll(".roles li"));
  function markLineStarts() {
    var top = null;
    roles.forEach(function (li) {
      li.classList.remove("line-start");
      var t = li.offsetTop;
      if (top !== null && t > top + 2) li.classList.add("line-start");
      top = t;
    });
  }
  if (roles.length) {
    markLineStarts();
    window.addEventListener("resize", markLineStarts);
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(markLineStarts);
  }

  /* ---------- Current-section highlight ---------- */
  var links = Array.prototype.slice.call(document.querySelectorAll(".nav-list a[href^='#']"));
  var sections = links
    .map(function (a) { return document.querySelector(a.getAttribute("href")); })
    .filter(Boolean);

  if ("IntersectionObserver" in window && sections.length) {
    var current = null;
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) current = entry.target.id;
      });
      links.forEach(function (a) {
        if (a.getAttribute("href") === "#" + current) a.setAttribute("aria-current", "true");
        else a.removeAttribute("aria-current");
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    sections.forEach(function (s) { spy.observe(s); });
  }

  /* ---------- Reveal on scroll + counters ---------- */
  function countUp(el) {
    var target = parseInt(el.getAttribute("data-count"), 10);
    if (!target || reduceMotion) return;
    var start = null;
    var duration = 1100;
    function frame(t) {
      if (start === null) start = t;
      var p = Math.min((t - start) / duration, 1);
      el.textContent = String(Math.round(target * (1 - Math.pow(1 - p, 3))));
      if (p < 1) window.requestAnimationFrame(frame);
    }
    window.requestAnimationFrame(frame);
  }

  var revealables = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        var num = entry.target.querySelector("[data-count]");
        if (num) countUp(num);
        io.unobserve(entry.target);
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    revealables.forEach(function (el) { io.observe(el); });
  } else {
    revealables.forEach(function (el) { el.classList.add("is-visible"); });
  }

  /* ---------- Copy email ---------- */
  document.querySelectorAll("[data-copy]").forEach(function (btn) {
    var status = btn.parentElement.querySelector(".copy-status");
    function say(msg) { if (status) status.textContent = msg; }
    btn.addEventListener("click", function () {
      var text = btn.getAttribute("data-copy");
      function fallback() {
        var ta = document.createElement("textarea");
        ta.value = text;
        ta.setAttribute("readonly", "");
        ta.style.position = "fixed";
        ta.style.opacity = "0";
        document.body.appendChild(ta);
        ta.select();
        var ok = false;
        try { ok = document.execCommand("copy"); } catch (err) { ok = false; }
        document.body.removeChild(ta);
        say(ok ? "Copied to clipboard." : "Press Ctrl+C (or Cmd+C) to copy: " + text);
      }
      if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(text).then(function () { say("Copied to clipboard."); }, fallback);
      } else {
        fallback();
      }
    });
  });

  /* ---------- Footer year ---------- */
  var year = document.querySelector("[data-year]");
  if (year) year.textContent = String(new Date().getFullYear());

  /* ---------- Greeting popup (dismissal remembered) ---------- */
  var KEY = "greeting-dismissed";
  var greeting = document.getElementById("greeting");

  function dismissed() {
    try { return window.localStorage.getItem(KEY) === "1"; } catch (err) { return false; }
  }
  function remember() {
    try { window.localStorage.setItem(KEY, "1"); } catch (err) { /* storage blocked: fine */ }
  }

  if (greeting && !dismissed()) {
    window.setTimeout(function () {
      greeting.hidden = false;
      greeting.classList.add("is-entering");
    }, reduceMotion ? 0 : 1400);

    greeting.querySelector(".greeting-close").addEventListener("click", function () {
      greeting.hidden = true;
      remember();
    });
  }
})();
