/* Prototipo estático; no requiere AJAX ni acceso WordPress. */
const btn=document.querySelector('.jb-toggle');
const nav=document.querySelector('#jb-menu');
if(btn&&nav){
  btn.addEventListener('click',()=>{
    const open=btn.getAttribute('aria-expanded')!=='true';
    btn.setAttribute('aria-expanded',String(open));
    btn.setAttribute('aria-label',open?'Cerrar menú':'Abrir menú');
    nav.classList.toggle('is-open',open);
  });
  nav.addEventListener('click',event=>{
    if(event.target.closest('a')&&btn.getAttribute('aria-expanded')==='true'){
      nav.classList.remove('is-open');
      btn.setAttribute('aria-expanded','false');
      btn.setAttribute('aria-label','Abrir menú');
    }
  });
  document.addEventListener('keydown',event=>{
    if(event.key==='Escape'){
      nav.classList.remove('is-open');
      btn.setAttribute('aria-expanded','false');
    }
  });
}
