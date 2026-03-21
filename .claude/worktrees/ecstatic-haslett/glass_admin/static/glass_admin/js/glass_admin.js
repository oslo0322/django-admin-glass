/**
 * glass_admin.js - Django Glass Admin theme enhancements
 */
(function () {
  "use strict";

  // --- Theme auto-detection ---
  function applyAutoTheme() {
    const metaTheme = document.querySelector('meta[name="glass-admin-theme"]');
    if (!metaTheme || metaTheme.getAttribute("content") !== "auto") return;

    const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
    const lightLink = document.getElementById("glass-theme-light");
    const darkLink = document.getElementById("glass-theme-dark");

    if (lightLink && darkLink) {
      lightLink.media = prefersDark ? "not all" : "all";
      darkLink.media = prefersDark ? "all" : "not all";
    }

    window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", (e) => {
      if (lightLink && darkLink) {
        lightLink.media = e.matches ? "not all" : "all";
        darkLink.media = e.matches ? "all" : "not all";
      }
    });
  }

  // --- Smooth nav hover transitions ---
  function initNavTransitions() {
    const navLinks = document.querySelectorAll("#nav-sidebar a, #user-tools a");
    navLinks.forEach((link) => {
      link.style.transition = "all 0.2s ease";
    });
  }

  // --- Toast notifications ---
  function initToasts() {
    const messages = document.querySelectorAll(".messagelist li");
    messages.forEach((msg) => {
      msg.style.transition = "opacity 0.5s ease, transform 0.5s ease";
      setTimeout(() => {
        msg.style.opacity = "0";
        msg.style.transform = "translateY(-10px)";
        setTimeout(() => msg.remove(), 500);
      }, 5000);
    });
  }

  // --- Glass ripple effect on buttons ---
  function initRipple() {
    const buttons = document.querySelectorAll(".submit-row input, .submit-row button, .object-tools a");
    buttons.forEach((btn) => {
      btn.addEventListener("click", function (e) {
        const ripple = document.createElement("span");
        ripple.className = "glass-ripple";
        const rect = btn.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        ripple.style.cssText = `
          position: absolute;
          border-radius: 50%;
          background: rgba(255,255,255,0.3);
          width: ${size}px;
          height: ${size}px;
          left: ${e.clientX - rect.left - size / 2}px;
          top: ${e.clientY - rect.top - size / 2}px;
          animation: glassRipple 0.6s ease-out forwards;
          pointer-events: none;
        `;
        if (getComputedStyle(btn).position === "static") {
          btn.style.position = "relative";
        }
        btn.style.overflow = "hidden";
        btn.appendChild(ripple);
        setTimeout(() => ripple.remove(), 600);
      });
    });
  }

  // Inject ripple keyframe
  function injectRippleCSS() {
    const style = document.createElement("style");
    style.textContent = `
      @keyframes glassRipple {
        from { transform: scale(0); opacity: 1; }
        to { transform: scale(2.5); opacity: 0; }
      }
    `;
    document.head.appendChild(style);
  }

  // --- Init ---
  function init() {
    applyAutoTheme();
    initNavTransitions();
    initToasts();
    injectRippleCSS();
    initRipple();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
