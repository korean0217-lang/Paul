const CACHE='paul-game-v1';
self.addEventListener('install',e=>e.waitUntil(caches.open(CACHE).then(c=>c.add('./index.html')).then(()=>self.skipWaiting())));
self.addEventListener('activate',e=>e.waitUntil(self.clients.claim()));
self.addEventListener('fetch',e=>{
  if(e.request.method!=='GET')return;
  e.respondWith(caches.match(e.request).then(x=>x||fetch(e.request).then(r=>{
    const c=r.clone(); caches.open(CACHE).then(cache=>cache.put(e.request,c)); return r;
  }).catch(()=>x)));
});
