// ── Z-index management ──
let zTop = 10;
const DESKTOP_BREAKPOINT = 768;

function isMobileViewport() {
  return window.innerWidth <= DESKTOP_BREAKPOINT;
}

// ── Panel open/close ──
function openPanel(id) {
  const panel = document.getElementById('panel-' + id);
  if (!panel) return;

  if (isMobileViewport()) {
    // close all panels
    document.querySelectorAll('.panel').forEach(p => p.classList.remove('open'));
    panel.classList.add('open');
    document.body.classList.add('mobile-panel');
    return;
  }

  // Close all currently open panels before opening the new one
  document.querySelectorAll('.panel.open').forEach(p => {
    p.classList.remove('open');
  });

  // Desktop: reset position to top-left, bring to front
  panel.style.top = '12px';
  panel.style.left = '12px';
  panel.style.width = '';
  panel.classList.add('open');
  bringToFront(panel);
}

function closePanel(id) {
  const panel = document.getElementById('panel-' + id);
  if (panel) panel.classList.remove('open');
}

function bringToFront(panel) {
  zTop++;
  panel.style.zIndex = zTop;
}

function mobileBack() {
  document.querySelectorAll('.panel').forEach(p => p.classList.remove('open'));
  document.body.classList.remove('mobile-panel');
}

// ── Archive dropdown ──
function toggleArchive(el) {
  const dropdown = document.getElementById('archive-dropdown');
  const arrow = document.getElementById('archive-arrow');
  const isOpen = dropdown.classList.toggle('open');
  arrow.classList.toggle('open', isOpen);
  if (el) {
    el.setAttribute('aria-expanded', String(isOpen));
  }
}

document.addEventListener('click', function(e) {
  const openTrigger = e.target.closest('[data-open-panel]');
  if (openTrigger) {
    openPanel(openTrigger.dataset.openPanel);
    return;
  }

  const closeTrigger = e.target.closest('[data-close-panel]');
  if (closeTrigger) {
    closePanel(closeTrigger.dataset.closePanel);
    return;
  }

  const actionTrigger = e.target.closest('[data-action]');
  if (!actionTrigger) return;

  if (actionTrigger.dataset.action === 'mobile-back') {
    mobileBack();
    return;
  }

  if (actionTrigger.dataset.action === 'toggle-archive') {
    toggleArchive(actionTrigger);
  }
});

// ── Drag ──
(function() {
  let dragging = null, ox = 0, oy = 0;

  document.addEventListener('mousedown', function(e) {
    const tb = e.target.closest('.panel-titlebar');
    if (!tb || e.target.closest('.panel-close')) return;
    if (isMobileViewport()) return;

    const panel = tb.closest('.panel');
    bringToFront(panel);
    dragging = panel;

    const rect = panel.getBoundingClientRect();
    const mainRect = document.getElementById('main').getBoundingClientRect();
    ox = e.clientX - rect.left;
    oy = e.clientY - rect.top;

    // convert to explicit px position relative to #main
    panel.style.left = (rect.left - mainRect.left) + 'px';
    panel.style.top  = (rect.top  - mainRect.top)  + 'px';
    panel.style.width = rect.width + 'px';

    e.preventDefault();
  });

  document.addEventListener('mousemove', function(e) {
    if (!dragging) return;
    const mainRect = document.getElementById('main').getBoundingClientRect();
    let x = e.clientX - mainRect.left - ox;
    let y = e.clientY - mainRect.top  - oy;
    // clamp so titlebar stays visible
    x = Math.max(-dragging.offsetWidth + 60, x);
    y = Math.max(0, y);
    dragging.style.left = x + 'px';
    dragging.style.top  = y + 'px';
  });

  document.addEventListener('mouseup', function() { dragging = null; });
})();

// ── Resize (vertical only) ──
(function() {
  let resizing = null, startY = 0, startH = 0;

  document.addEventListener('mousedown', function(e) {
    const handle = e.target.closest('.panel-resize');
    if (!handle) return;
    if (isMobileViewport()) return;
    const panel = handle.closest('.panel');
    resizing = panel;
    startY = e.clientY;
    startH = panel.offsetHeight;
    e.preventDefault();
  });

  document.addEventListener('mousemove', function(e) {
    if (!resizing) return;
    const dy = e.clientY - startY;
    const newH = Math.max(160, startH + dy);
    resizing.style.height = newH + 'px';
  });

  document.addEventListener('mouseup', function() { resizing = null; });
})();

// ── Click titlebar to bring to front ──
document.addEventListener('mousedown', function(e) {
  const panel = e.target.closest('.panel');
  if (panel) bringToFront(panel);
});

// ── Handle resize back from mobile ──
window.addEventListener('resize', function() {
  if (!isMobileViewport()) {
    document.body.classList.remove('mobile-panel');
  }
});

// ── Open hero panel by default on desktop ──
if (!isMobileViewport()) {
  openPanel('hello');
}
