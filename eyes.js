/* Sevimli kartlar: gözler imleci (ya da parmağı) izler; imleç yokken ara sıra etrafa bakar. Hareketsizlik tercihinde durur. */
(function () {
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce) return;
  var groups = [].slice.call(document.querySelectorAll("[data-eyes]"));
  if (!groups.length) return;
  var idleTimer = null;
  function look(x, y) {
    groups.forEach(function (g) {
      var r = g.getBoundingClientRect();
      if (!r.width) return;
      var cx = r.left + r.width / 2, cy = r.top + r.height / 2;
      var dx = x - cx, dy = y - cy, d = Math.hypot(dx, dy) || 1, k = Math.min(1, d / 260);
      var mx = (dx / d) * k * 0.034, my = (dy / d) * k * 0.034;
      [].forEach.call(g.querySelectorAll(".pupil"), function (p) { p.setAttribute("transform", "translate(" + mx.toFixed(4) + " " + my.toFixed(4) + ")"); });
    });
  }
  function wander() {
    var w = window.innerWidth, h = window.innerHeight;
    look(Math.random() * w, Math.random() * h * 0.6);
  }
  function pointer(e) {
    var t = e.touches ? e.touches[0] : e;
    look(t.clientX, t.clientY);
    clearInterval(idleTimer);
    idleTimer = setInterval(wander, 3200);
  }
  window.addEventListener("pointermove", pointer, { passive: true });
  window.addEventListener("touchmove", pointer, { passive: true });
  idleTimer = setInterval(wander, 3200);
  wander();
})();
