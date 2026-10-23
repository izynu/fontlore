(function(){
  var DATA = window.__FONTLORE__;
  function el(tag, cls, text){
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text !== undefined) e.textContent = text;
    return e;
  }
  function chip(text, accent){
    var c = el('span', 'chip' + (accent ? ' chip-accent' : ''), text);
    return c;
  }
  function cardLink(href, label){
    var a = el('a', 'card-link', label || 'Open guide');
    a.href = href;
    return a;
  }

  /* ---------- References panel ---------- */
  var refRoot = document.getElementById('references-root');
  var cats = {};
  DATA.references.forEach(function(r){ (cats[r.category] = cats[r.category] || []).push(r); });
  Object.keys(cats).sort().forEach(function(cat){
    var list = cats[cat];
    var d = el('details', 'cat');
    d.id = 'cat-' + cat;
    if (cat === 'sourcing') d.open = true;
    var s = el('summary');
    s.appendChild(el('span', null, cat.charAt(0).toUpperCase() + cat.slice(1)));
    s.appendChild(el('span', 'cat-count', list.length + ' guides'));
    d.appendChild(s);
    var body = el('div', 'cat-body');
    body.appendChild(el('p', 'cat-blurb', DATA.categoryBlurbs[cat] || ''));
    var ul = el('ul', 'ref-list');
    list.forEach(function(r){
      var li = el('li');
      var a = el('a', null, r.title);
      a.href = r.file;
      li.appendChild(a);
      ul.appendChild(li);
    });
    body.appendChild(ul);
    d.appendChild(body);
    refRoot.appendChild(d);
  });

  /* ---------- Fonts panel ---------- */
  var fontGrid = document.getElementById('fonts-grid');
  var fontNote = document.getElementById('fonts-count');
  function renderFonts(){
    var q = document.getElementById('font-search').value.trim().toLowerCase();
    var cat = document.getElementById('font-category').value;
    var lic = document.getElementById('font-license').value;
    var script = document.getElementById('font-script').value;
    var variable = document.getElementById('font-variable').value;
    fontGrid.innerHTML = '';
    var n = 0;
    var seen = {};
    DATA.fonts.forEach(function(f){
      if (seen[f.slug]) return; seen[f.slug] = 1;
      if (cat && f.category !== cat) return;
      if (lic && f.license !== lic) return;
      if (variable === 'variable' && !f.variable) return;
      if (variable === 'static' && f.variable) return;
      if (script && (f.scripts || []).indexOf(script) === -1) return;
      if (q && (f.family + ' ' + f.designer + ' ' + f.foundry + ' ' + (f.tags||[]).join(' ')).toLowerCase().indexOf(q) === -1) return;
      n++;
      var c = el('article', 'card');
      var h = el('h3');
      var a = el('a', null, f.family);
      a.href = 'guides/fonts/' + f.slug + '.html';
      a.style.color = 'inherit'; a.style.textDecoration = 'none';
      h.appendChild(a);
      c.appendChild(h);
      c.appendChild(el('p', null, f.designer + (f.foundry ? ' - ' + f.foundry : '')));
      var chips = el('div');
      chips.appendChild(chip(f.license, true));
      chips.appendChild(chip(f.category));
      if (f.variable) chips.appendChild(chip('variable'));
      (f.scripts || []).slice(0, 3).forEach(function(s){ chips.appendChild(chip(s)); });
      c.appendChild(chips);
      var lrow = el('div');
      lrow.style.marginTop = '8px';
      var a1 = cardLink('guides/fonts/' + f.slug + '-overview.html', 'Overview');
      var a2 = cardLink('guides/fonts/' + f.slug + '-implementation.html', 'Implementation');
      lrow.appendChild(a1);
      var sep = el('span', null, ' - ');
      sep.style.fontSize = '.86rem';
      lrow.appendChild(sep);
      lrow.appendChild(a2);
      c.appendChild(lrow);
      fontGrid.appendChild(c);
    });
    fontNote.textContent = n + ' of ' + DATA.counts.fonts + ' font records shown';
  }
  ['font-search','font-category','font-license','font-script','font-variable'].forEach(function(id){
    document.getElementById(id).addEventListener(id === 'font-search' ? 'input' : 'change', renderFonts);
  });

  /* ---------- Pairings panel ---------- */
  var pairGrid = document.getElementById('pairings-grid');
  var pairNote = document.getElementById('pairings-count');
  function renderPairs(){
    var q = document.getElementById('pair-search').value.trim().toLowerCase();
    var ctx = document.getElementById('pair-context').value;
    pairGrid.innerHTML = '';
    var n = 0;
    DATA.pairings.forEach(function(p){
      if (ctx && p.context !== ctx) return;
      if (q && ((p.headingFamily + ' ' + p.bodyFamily + ' ' + p.context + ' ' + p.rationale).toLowerCase().indexOf(q) === -1)) return;
      n++;
      var c = el('article', 'card pair-card');
      c.appendChild(chip(p.context, true));
      c.appendChild(el('p', 'sample-head', p.headingFamily));
      c.appendChild(el('p', 'sample-body', 'paired with ' + p.bodyFamily));
      c.appendChild(el('p', null, p.rationale));
      var links = el('div');
      links.style.marginTop = '8px';
      var a0 = cardLink('guides/pairings/' + p.file + '.html', 'Pairing guide');
      var a1 = cardLink('guides/fonts/' + p.heading + '-overview.html', p.headingFamily);
      var a2 = cardLink('guides/fonts/' + p.body + '-overview.html', p.bodyFamily);
      links.appendChild(a0);
      var sep = el('span', null, ' - ');
      sep.style.fontSize = '.86rem';
      links.appendChild(sep);
      links.appendChild(a1);
      var sep2 = el('span', null, ' + ');
      sep2.style.fontSize = '.86rem';
      links.appendChild(sep2);
      links.appendChild(a2);
      c.appendChild(links);
      pairGrid.appendChild(c);
    });
    pairNote.textContent = n + ' of ' + DATA.counts.pairings + ' curated pairings shown';
  }
  ['pair-search','pair-context'].forEach(function(id){
    document.getElementById(id).addEventListener(id === 'pair-search' ? 'input' : 'change', renderPairs);
  });

  /* ---------- Tools panel ---------- */
  var toolList = document.getElementById('tools-list');
  var toolNote = document.getElementById('tools-count');
  function renderTools(){
    var q = document.getElementById('tool-search').value.trim().toLowerCase();
    var section = document.getElementById('tool-section').value;
    toolList.innerHTML = '';
    var n = 0;
    DATA.tools.forEach(function(t){
      if (section && t.section !== section) return;
      if (q && ((t.name + ' ' + t.what).toLowerCase().indexOf(q) === -1)) return;
      n++;
      var row = el('div', 'tool-row');
      var left = el('div');
      left.style.minWidth = '160px';
      var h = el('h3');
      h.appendChild(el('span', null, t.name));
      h.style.color = 'inherit';
      left.appendChild(h);
      left.appendChild(chip(t.section));
      row.appendChild(left);
      row.appendChild(el('p', null, t.what));
      var links = el('div', 'tool-links');
      var visit = el('a', null, 'Visit site');
      visit.href = t.url;
      visit.target = '_blank';
      visit.rel = 'noopener noreferrer nofollow';
      links.appendChild(visit);
      var guide = el('a', null, 'Guide');
      guide.href = 'guides/tools/' + t.slug + '.html';
      links.appendChild(guide);
      row.appendChild(links);
      toolList.appendChild(row);
    });
    toolNote.textContent = n + ' of ' + DATA.counts.tools + ' tools shown';
  }
  ['tool-search','tool-section'].forEach(function(id){
    document.getElementById(id).addEventListener(id === 'tool-search' ? 'input' : 'change', renderTools);
  });

  renderFonts(); renderPairs(); renderTools();

  /* ---------- Tabs + deep links ---------- */
  var tabs = Array.prototype.slice.call(document.querySelectorAll('.tab'));
  var panels = {
    'references': document.getElementById('panel-references'),
    'fonts': document.getElementById('panel-fonts'),
    'pairings': document.getElementById('panel-panel'),
    'tools': document.getElementById('panel-tools')
  };
  function selectTab(name, push){
    if (!panels[name]) name = 'references';
    tabs.forEach(function(t){ t.setAttribute('aria-selected', String(t.dataset.tab === name)); });
    Object.keys(panels).forEach(function(k){ panels[k].classList.toggle('active', k === name); });
    if (push && history.replaceState) history.replaceState(null, '', '#' + name);
  }
  tabs.forEach(function(t){ t.addEventListener('click', function(){ selectTab(t.dataset.tab, true); }); });
  var hash = (location.hash || '').replace('#','');
  var params = new URLSearchParams(location.search);
  var wanted = params.get('tab') || hash;
  if (hash === 'references' || params.get('category')) {
    selectTab('references', false);
    var cat = params.get('category');
    if (cat) {
      var target = document.getElementById('cat-' + cat);
      if (target) { target.open = true; setTimeout(function(){ target.scrollIntoView({behavior:'smooth', block:'start'}); }, 60); }
    }
  } else if (wanted) {
    selectTab(wanted, false);
  } else {
    selectTab('references', false);
  }
})();
