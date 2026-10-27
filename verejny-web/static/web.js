// Prohlížeč fotek galerie: klik otevře fotku přes celou obrazovku, šipky listují, Esc zavře.
(function () {
  const links = [...document.querySelectorAll('.gallery a')];
  if (!links.length || typeof HTMLDialogElement !== 'function') return;

  const dlg = document.createElement('dialog');
  dlg.className = 'lightbox';
  dlg.setAttribute('aria-label', 'Prohlížeč fotek');
  dlg.innerHTML =
    '<div class="lightbox-inner"><img alt=""><p></p>' +
    '<button class="lb-close" type="button" aria-label="Zavřít">×</button>' +
    '<button class="lb-prev" type="button" aria-label="Předchozí fotka">‹</button>' +
    '<button class="lb-next" type="button" aria-label="Další fotka">›</button></div>';
  document.body.append(dlg);

  const img = dlg.querySelector('img');
  const caption = dlg.querySelector('p');
  let current = 0;

  function show(i) {
    current = (i + links.length) % links.length;
    const a = links[current];
    img.src = a.href;
    img.alt = a.querySelector('img').alt;
    caption.textContent = a.closest('figure').querySelector('figcaption')?.textContent || '';
  }

  links.forEach((a, i) => a.addEventListener('click', (e) => {
    e.preventDefault();
    show(i);
    dlg.showModal();
  }));

  dlg.querySelector('.lb-close').addEventListener('click', () => dlg.close());
  dlg.querySelector('.lb-prev').addEventListener('click', () => show(current - 1));
  dlg.querySelector('.lb-next').addEventListener('click', () => show(current + 1));
  dlg.addEventListener('click', (e) => { if (e.target === dlg || e.target.classList.contains('lightbox-inner')) dlg.close(); });
  dlg.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft') show(current - 1);
    if (e.key === 'ArrowRight') show(current + 1);
  });
})();

// Kalendář: proběhlé termíny ztlumí a označí nejbližší další. Počítá se v prohlížeči, ať to sedí i bez nového buildu.
(function () {
  const terminy = [...document.querySelectorAll('.termin[data-datum]')];
  if (!terminy.length) return;
  const dnes = new Date().toLocaleDateString('sv');  // RRRR-MM-DD v místním čase
  terminy.forEach(t => { if (t.dataset.datum < dnes) t.classList.add('probehlo'); });
  const pristi = terminy.find(t => t.dataset.datum >= dnes && !t.classList.contains('zruseno'));
  if (pristi) pristi.classList.add(pristi.dataset.datum === dnes ? 'dnes' : 'pristi');
})();
