/* Nesim Apps web sitesi analitiği (Google Analytics 4, Consent Mode v2).
   - AB/AEA, Birleşik Krallık ve İsviçre'de (saat diliminden tahmin) onay verilene kadar analitik reddedilmiş başlar ve bant çıkar.
   - Diğer ülkelerde (Türkiye dahil) bant yok, analitik doğrudan çalışır.
   - Reklam çerezleri/kişiselleştirme HİÇ kullanılmaz.
   - Kendi ziyaretini saymamak için siteyi bir kez ?notrack=1 ile aç (bu tarayıcıda kalıcı), ?notrack=0 ile geri al. */
(function () {
  var GA_ID = "G-L5BQL3D4WB";
  var h = location.hostname;
  if (h !== "nrazon.github.io") return; // yerel/önizleme sayılmaz

  try {
    var q = /[?&]notrack=([01])/.exec(location.search);
    if (q) localStorage.setItem("notrack", q[1]);
    if (localStorage.getItem("notrack") === "1") return;
  } catch (e) {}

  // --- Bölge: AB/AEA + BK + İsviçre (saat dilimi tahmini; şüphede bant çıkar) ---
  var EU_TZ = ("Amsterdam,Andorra,Athens,Berlin,Bratislava,Brussels,Bucharest,Budapest,Busingen,Copenhagen,Dublin,Helsinki,Isle_of_Man,Jersey,Guernsey," +
    "Lisbon,Ljubljana,London,Belfast,Luxembourg,Madrid,Malta,Monaco,Oslo,Paris,Prague,Riga,Rome,San_Marino,Stockholm,Tallinn,Vaduz,Vatican,Vienna," +
    "Vilnius,Warsaw,Zagreb,Zurich,Sofia,Nicosia").split(",");
  var EU_TZ_OTHER = ["Atlantic/Reykjavik", "Atlantic/Canary", "Atlantic/Madeira", "Atlantic/Azores", "Africa/Ceuta", "Asia/Nicosia", "Asia/Famagusta"];
  function inEU() {
    var tz = "";
    try { tz = Intl.DateTimeFormat().resolvedOptions().timeZone || ""; } catch (e) {}
    if (!tz) return true; // bilinmiyorsa güvenli taraf
    if (tz.indexOf("Europe/") === 0) return EU_TZ.indexOf(tz.slice(7)) >= 0;
    return EU_TZ_OTHER.indexOf(tz) >= 0;
  }

  var eu = inEU();
  var saved = null;
  try { saved = localStorage.getItem("consent_v1"); } catch (e) {}

  window.dataLayer = window.dataLayer || [];
  function gtag() { dataLayer.push(arguments); }
  window.gtag = gtag;
  var analyticsDefault = eu ? (saved === "granted" ? "granted" : "denied") : "granted";
  gtag("consent", "default", {
    analytics_storage: analyticsDefault,
    ad_storage: "denied", ad_user_data: "denied", ad_personalization: "denied",
    wait_for_update: 500,
  });
  gtag("js", new Date());
  gtag("config", GA_ID, { allow_google_signals: false, allow_ad_personalization_signals: false });

  // AB'de onay yokken gtag.js hiç yüklenmez (çerezsiz ping bile gönderilmez); onay gelince yüklenir.
  var loaded = false;
  function load() {
    if (loaded) return;
    loaded = true;
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + GA_ID;
    document.head.appendChild(s);
  }
  if (analyticsDefault === "granted") load();

  // --- Olaylar (tek dinleyici) ---
  function app(href) {
    var m = /[?&]id=([\w.]+)/.exec(href || "");
    return m ? m[1] : "";
  }
  function slugOf(a) {
    var m = /(?:^|\/)([a-z0-9]+)\/?(?:index\.html)?(?:[?#].*)?$/i.exec(a.getAttribute("href") || "");
    return m ? m[1].toLowerCase() : "";
  }
  document.addEventListener("click", function (e) {
    var el = e.target.closest ? e.target.closest("a,button") : null;
    if (!el) return;
    if (el.tagName === "A") {
      var href = el.href || "";
      if (href.indexOf("play.google.com/store/apps/details") >= 0) {
        gtag("event", "play_click", { app: app(href), page_path: location.pathname, transport_type: "beacon" });
      } else if (href.indexOf("play.google.com/store/apps/dev") >= 0) {
        gtag("event", "play_dev_click", { page_path: location.pathname, transport_type: "beacon" });
      } else if (el.hostname === h && /\/$|index\.html$|^[^.]*$/.test(el.pathname) && el.pathname !== location.pathname) {
        var parts = el.pathname.split("/").filter(Boolean);
        if (parts.length === 1 && parts[0] !== "site-privacy.html") {
          gtag("event", "app_open", { app: parts[0], page_path: location.pathname, transport_type: "beacon" });
        }
      }
    } else if (el.dataset && el.dataset.lang) {
      gtag("event", "lang_change", { lang: el.dataset.lang, transport_type: "beacon" });
    } else if (el.dataset && el.dataset.filter) {
      gtag("event", "filter_change", { filter: el.dataset.filter, transport_type: "beacon" });
    }
  }, true);

  // "QR ile yükle" açıldı (taramayı sitede ölçemeyiz; yüklemeler Play Console'da utm_medium=qr ile ayrışır).
  document.addEventListener("toggle", function (e) {
    var d = e.target;
    if (d && d.matches && d.matches("details.qr") && d.open) gtag("event", "qr_open", { app: d.getAttribute("data-qr") || "", page_path: location.pathname, transport_type: "beacon" });
  }, true);

  // --- Onay bandı (yalnız AB/AEA/BK/CH ve henüz seçilmediyse) ---
  var TXT = {
    tr: ["Siteyi iyileştirmek için anonim kullanım istatistiği (Google Analytics) kullanıyoruz. Kabul eder misin?", "Kabul et", "Reddet", "Ayrıntılar"],
    en: ["We use anonymous usage statistics (Google Analytics) to improve this site. Do you accept?", "Accept", "Decline", "Details"],
    es: ["Usamos estadísticas de uso anónimas (Google Analytics) para mejorar este sitio. ¿Aceptas?", "Aceptar", "Rechazar", "Detalles"],
    pt: ["Usamos estatísticas de uso anônimas (Google Analytics) para melhorar este site. Você aceita?", "Aceitar", "Recusar", "Detalhes"],
  };
  function lang() {
    var l = "";
    try { l = localStorage.getItem("lang") || ""; } catch (e) {}
    if (!TXT[l]) l = (document.documentElement.lang || navigator.language || "en").toLowerCase().slice(0, 2);
    return TXT[l] ? l : "en";
  }
  function setConsent(v) {
    try { localStorage.setItem("consent_v1", v); } catch (e) {}
    gtag("consent", "update", { analytics_storage: v });
    if (v === "granted") load();
    var b = document.getElementById("consent-bar");
    if (b) b.remove();
  }
  function showBar() {
    if (document.getElementById("consent-bar")) return;
    var t = TXT[lang()];
    var b = document.createElement("div");
    b.id = "consent-bar";
    b.setAttribute("role", "dialog");
    b.setAttribute("aria-label", "Cookies");
    b.style.cssText = "position:fixed;left:12px;right:12px;bottom:12px;z-index:99999;max-width:640px;margin:0 auto;background:#16322A;color:#F3FAF6;" +
      "border-radius:14px;padding:14px 16px;box-shadow:0 6px 28px rgba(0,0,0,.45);font:14px/1.45 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;" +
      "display:flex;flex-wrap:wrap;gap:10px;align-items:center";
    var p = document.createElement("span");
    p.style.cssText = "flex:1 1 260px";
    p.textContent = t[0] + " ";
    var more = document.createElement("a");
    more.href = "/site-privacy.html#" + lang();
    more.textContent = t[3];
    more.style.cssText = "color:#9FE8C8";
    p.appendChild(more);
    function btn(label, v, primary) {
      var x = document.createElement("button");
      x.type = "button";
      x.textContent = label;
      x.style.cssText = "border:0;border-radius:999px;padding:9px 16px;font:600 14px system-ui,sans-serif;cursor:pointer;" +
        (primary ? "background:#FFD166;color:#1B1B1B" : "background:#2B4A3F;color:#F3FAF6");
      x.addEventListener("click", function () { setConsent(v); });
      return x;
    }
    b.appendChild(p);
    b.appendChild(btn(t[2], "denied", false));
    b.appendChild(btn(t[1], "granted", true));
    document.body.appendChild(b);
  }
  // Gizlilik sayfasındaki "çerez tercihimi değiştir" bağlantısı için.
  window.nesimConsentReset = function () {
    try { localStorage.removeItem("consent_v1"); } catch (e) {}
    gtag("consent", "update", { analytics_storage: "denied" });
    showBar();
  };
  if (eu && saved !== "granted" && saved !== "denied") {
    if (document.body) showBar(); else document.addEventListener("DOMContentLoaded", showBar);
  }
})();
