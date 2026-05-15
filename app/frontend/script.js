/* =============================================
   DEVWATCH — script.js
   ============================================= */

const API = "http://localhost:8000";

// ── HELPERS ──────────────────────────────────

function formatGB(bytes) {
  return (bytes / 1024 ** 3).toFixed(1) + " GB";
}

function colorClass(pct) {
  if (pct >= 85) return "crit";
  if (pct >= 60) return "warn";
  return "";
}

function setMetricUI(id, pct) {
  const el    = document.getElementById(id);
  const bar   = document.getElementById("bar-" + id);
  const cls   = colorClass(pct);

  el.textContent = pct.toFixed(1) + "%";
  el.className   = "value " + cls;

  bar.style.width  = pct + "%";
  bar.className    = "bar-fill " + cls;
}

function updateClock() {
  const now = new Date();
  document.getElementById("last-update").textContent =
    now.toLocaleTimeString("pt-BR");
}

function updateStatus(cpuPct) {
  const badge = document.getElementById("status-badge");
  const text  = badge.querySelector(".status-text");

  badge.className = "status";

  if (cpuPct >= 85) {
    badge.classList.add("crit");
    text.textContent = "System Critical";
  } else if (cpuPct >= 60) {
    badge.classList.add("warn");
    text.textContent = "System Under Load";
  } else {
    text.textContent = "System Healthy";
  }
}

// ── LIVE METRICS  →  GET /metrics/ ───────────

async function loadMetrics() {
  try {
    const res  = await fetch(`${API}/metrics/`);
    if (!res.ok) throw new Error(res.status);
    const data = await res.json();

    // cards
    setMetricUI("cpu",  data.cpu.percent);
    setMetricUI("ram",  data.memory.percent);
    setMetricUI("disk", data.disk.percent);

    // details panel
    document.getElementById("d-cores").textContent     = data.cpu.cores;
    document.getElementById("d-ram").textContent       = formatGB(data.memory.used);
    document.getElementById("d-ram-total").textContent = formatGB(data.memory.total);
    document.getElementById("d-disk").textContent      = formatGB(data.disk.used);
    document.getElementById("d-disk-total").textContent= formatGB(data.disk.total);

    updateStatus(data.cpu.percent);
    updateClock();

  } catch (err) {
    console.error("[metrics]", err);
    setOffline();
  }
}

// ── SUMMARY  →  GET /metrics/summary ─────────

async function loadSummary() {
  try {
    const res  = await fetch(`${API}/metrics/summary`);
    if (!res.ok) return;
    const data = await res.json();

    document.getElementById("s-cpu").textContent   = data.cpu_avg    != null ? data.cpu_avg.toFixed(1)    + "%" : "--";
    document.getElementById("s-ram").textContent   = data.memory_avg != null ? data.memory_avg.toFixed(1) + "%" : "--";
    document.getElementById("s-disk").textContent  = data.disk_avg   != null ? data.disk_avg.toFixed(1)   + "%" : "--";
    document.getElementById("s-count").textContent = data.count ?? "--";

  } catch (err) {
    console.error("[summary]", err);
  }
}

// ── HISTORY  →  GET /metrics/history ─────────

async function loadHistory() {
  try {
    const res  = await fetch(`${API}/metrics/history?limit=10`);
    if (!res.ok) return;
    const rows = await res.json();

    const tbody = document.getElementById("history-body");

    if (!rows.length) {
      tbody.innerHTML = `<tr><td colspan="5" class="table-empty">No history yet · click "Save Snapshot" to record</td></tr>`;
      return;
    }

    tbody.innerHTML = rows.map((r, i) => `
      <tr>
        <td>${r.id ?? i + 1}</td>
        <td>${formatDate(r.timestamp ?? r.created_at)}</td>
        <td class="${colorClass(r.cpu_percent) ? "val-" + colorClass(r.cpu_percent) : ""}">${r.cpu_percent?.toFixed(1)}%</td>
        <td>${r.memory_percent?.toFixed(1)}%</td>
        <td>${r.disk_percent?.toFixed(1)}%</td>
      </tr>
    `).join("");

  } catch (err) {
    console.error("[history]", err);
  }
}

function formatDate(str) {
  if (!str) return "--";
  const d = new Date(str);
  return d.toLocaleDateString("pt-BR") + " " + d.toLocaleTimeString("pt-BR");
}

// ── SAVE SNAPSHOT  →  POST /metrics/ ─────────

async function saveMetric() {
  const btn = document.getElementById("btn-save");
  btn.disabled = true;
  btn.textContent = "Saving…";

  try {
    const res = await fetch(`${API}/metrics/`, { method: "POST" });
    if (!res.ok) throw new Error(res.status);
    await loadHistory();
    await loadSummary();
    btn.textContent = "✓ Saved!";
    setTimeout(() => { btn.textContent = "+ Save Snapshot"; btn.disabled = false; }, 1500);
  } catch (err) {
    console.error("[save]", err);
    btn.textContent = "Error";
    setTimeout(() => { btn.textContent = "+ Save Snapshot"; btn.disabled = false; }, 2000);
  }
}

// ── OFFLINE STATE ─────────────────────────────

function setOffline() {
  const badge = document.getElementById("status-badge");
  badge.className = "status crit";
  badge.querySelector(".status-text").textContent = "Offline";
}

// ── INIT ──────────────────────────────────────

async function init() {
  await loadMetrics();
  await loadHistory();
  await loadSummary();
}

init();
setInterval(loadMetrics,  3000);   // live metrics every 3s
setInterval(loadHistory,  10000);  // history every 10s
setInterval(loadSummary,  15000);  // summary every 15s