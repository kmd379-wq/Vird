(function () {
  const nav = document.querySelector('.site-nav');
  const links = document.querySelectorAll('.nav-links a, .nav-cta');

  links.forEach(function (link) {
    link.addEventListener('click', function (e) {
      const href = link.getAttribute('href');
      if (!href || !href.startsWith('#')) return;
      const target = document.querySelector(href);
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });

  var sections = document.querySelectorAll('section[id]');
  var navLinks = document.querySelectorAll('.nav-links a');

  if ('IntersectionObserver' in window) {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          var id = entry.target.id;
          navLinks.forEach(function (link) {
            link.style.color = link.getAttribute('href') === '#' + id
              ? 'var(--teal)'
              : '';
          });
        });
      },
      { rootMargin: '-40% 0px -55% 0px', threshold: 0 }
    );
    sections.forEach(function (section) { observer.observe(section); });
  }

  window.addEventListener('scroll', function () {
    if (!nav) return;
    nav.style.borderBottomColor = window.scrollY > 20
      ? 'rgba(20, 20, 19, 0.15)'
      : '';
  }, { passive: true });
})();
