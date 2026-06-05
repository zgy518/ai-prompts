// 暗色模式切换
const themeToggle = document.getElementById('themeToggle');
const html = document.documentElement;

themeToggle.addEventListener('click', () => {
  const current = html.getAttribute('data-theme');
  const next = current === 'dark' ? 'light' : 'dark';
  html.setAttribute('data-theme', next);
  localStorage.setItem('theme', next);
});

// 移动端菜单
const menuToggle = document.getElementById('menuToggle');
const siteNav = document.getElementById('siteNav');

menuToggle.addEventListener('click', () => {
  siteNav.classList.toggle('open');
});

// 点击页面其他区域关闭菜单
document.addEventListener('click', (e) => {
  if (!e.target.closest('.site-header')) {
    siteNav.classList.remove('open');
  }
});
