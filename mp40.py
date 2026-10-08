<!DOCTYPE html>
<html lang="en">
<head>
        <link rel="canonical" href="https://msxportal.in/student/FieldProject-2026/mp40.py">

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MSX Portal – Industry-Ready Tech Training | Ctronics Infotech</title>
    <meta name="description" content="Master MERN, AI, Data Science & Cloud with hands-on projects, internship opportunities and placement support at Ctronics Infotech.">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
    :root {
        --primary: #6c47ff;
        --primary-dark: #5035cc;
        --primary-light: #8b6dff;
        --secondary: #ff6b35;
        --accent: #00d4aa;
        --dark: #0d0b1f;
        --dark2: #13102e;
        --text: #1a1a2e;
        --text-muted: #64748b;
        --surface: #f8f7ff;
        --white: #ffffff;
        --grad-hero: linear-gradient(135deg, #0d0b1f 0%, #1a1045 50%, #0d1b4b 100%);
        --grad-primary: linear-gradient(135deg, #6c47ff 0%, #9b59ff 100%);
        --grad-accent: linear-gradient(135deg, #00d4aa 0%, #00b894 100%);
        --card-shadow: 0 8px 32px rgba(108,71,255,0.10);
        --card-shadow-hover: 0 20px 60px rgba(108,71,255,0.22);
    }
    *, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }
    html { scroll-behavior: smooth; }
    body { font-family:'Inter',sans-serif; color:var(--text); background:#fff; overflow-x:hidden; }

    /* ── NAVBAR override removed (shared styles in navbar.php) ── */

    /* ── HERO ─────────────────────────────────── */
    .hero { min-height:100vh; background: var(--grad-hero); position:relative; overflow:hidden; display:flex; align-items:center; }
    .hero::before { content:''; position:absolute; inset:0; background:url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%236c47ff' fill-opacity='0.04'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E"); }
    .hero-glow1 { position:absolute; top:-200px; right:-100px; width:700px; height:700px; background:radial-gradient(circle, rgba(108,71,255,0.25) 0%, transparent 65%); border-radius:50%; pointer-events:none; }
    .hero-glow2 { position:absolute; bottom:-200px; left:-100px; width:600px; height:600px; background:radial-gradient(circle, rgba(0,212,170,0.12) 0%, transparent 65%); border-radius:50%; pointer-events:none; }
    .hero-content { position:relative; z-index:2; padding:140px 0 80px; }
    .hero-eyebrow { display:inline-flex; align-items:center; gap:8px; background:rgba(108,71,255,0.15); border:1px solid rgba(108,71,255,0.3); color:#a78bfa; font-size:13px; font-weight:600; padding:6px 16px; border-radius:20px; margin-bottom:24px; animation:fadeUp 0.8s ease both; letter-spacing:0.5px; text-transform:uppercase; }
    .hero-eyebrow i { color:var(--accent); }
    .hero-title { font-family:'Plus Jakarta Sans',sans-serif; font-size:clamp(36px,5vw,68px); font-weight:900; color:#fff; line-height:1.08; margin-bottom:24px; animation:fadeUp 0.8s ease 0.1s both; }
    .hero-title .gradient-text { background:linear-gradient(90deg,#a78bfa,#60d2f5,#00d4aa); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; }
    .hero-desc { font-size:18px; color:rgba(255,255,255,0.7); line-height:1.7; margin-bottom:40px; max-width:540px; animation:fadeUp 0.8s ease 0.2s both; }
    .hero-cta { display:flex; flex-wrap:wrap; gap:14px; animation:fadeUp 0.8s ease 0.3s both; }
    .btn-hero-primary { background:var(--grad-primary); color:#fff; border:none; padding:15px 36px; border-radius:50px; font-size:16px; font-weight:700; text-decoration:none; display:inline-flex; align-items:center; gap:9px; transition:all 0.3s; box-shadow:0 8px 30px rgba(108,71,255,0.45); }
    .btn-hero-primary:hover { transform:translateY(-4px); box-shadow:0 14px 40px rgba(108,71,255,0.6); color:#fff; }
    .btn-hero-outline { background:rgba(255,255,255,0.07); color:#fff; border:1.5px solid rgba(255,255,255,0.25); padding:15px 36px; border-radius:50px; font-size:16px; font-weight:700; text-decoration:none; display:inline-flex; align-items:center; gap:9px; transition:all 0.3s; backdrop-filter:blur(8px); }
    .btn-hero-outline:hover { background:rgba(255,255,255,0.16); border-color:rgba(255,255,255,0.5); color:#fff; transform:translateY(-4px); }
    .hero-stats { display:flex; flex-wrap:wrap; gap:0; margin-top:52px; padding-top:32px; border-top:1px solid rgba(255,255,255,0.1); animation:fadeUp 0.8s ease 0.4s both; }
    .hero-stat { flex:1; min-width:120px; padding-right:32px; }
    .hero-stat:not(:last-child) { border-right:1px solid rgba(255,255,255,0.1); margin-right:32px; }
    .hero-stat-val { font-size:36px; font-weight:800; color:#fff; line-height:1; margin-bottom:4px; }
    .hero-stat-label { font-size:13px; color:rgba(255,255,255,0.55); font-weight:500; }
    .hero-image-wrap { position:relative; z-index:2; animation:fadeUp 0.8s ease 0.2s both; }
    .hero-image-wrap img { width:100%; border-radius:24px; filter:drop-shadow(0 30px 60px rgba(108,71,255,0.5)); }
    .hero-badge { position:absolute; background:#fff; border-radius:16px; padding:12px 18px; box-shadow:0 10px 40px rgba(0,0,0,0.18); display:flex; align-items:center; gap:10px; }
    .hero-badge-1 { bottom:60px; left:-30px; animation:float 4s ease-in-out infinite; }
    .hero-badge-2 { top:40px; right:-20px; animation:float 4s ease-in-out 1.5s infinite; }
    .hero-badge i { font-size:22px; }
    .hero-badge span { font-size:13px; font-weight:700; color:var(--text); }

    /* ── TRUST BAR ────────────────────────────── */
    .trust-bar { background: #f8f7ff; padding:24px 0; border-bottom:1px solid #ede9fe; }
    .trust-bar-inner { display:flex; align-items:center; flex-wrap:wrap; gap:24px; justify-content:center; }
    .trust-item { display:flex; align-items:center; gap:8px; font-size:14px; font-weight:600; color:var(--text-muted); }
    .trust-item i { color:var(--primary); font-size:16px; }

    /* ── SECTION COMMONS ──────────────────────── */
    .section { padding:100px 0; }
    .section-alt { background: var(--surface); }
    .section-dark { background: var(--grad-hero); }
    .sec-tag { display:inline-block; font-size:12px; font-weight:700; letter-spacing:1px; text-transform:uppercase; color:var(--primary); background:rgba(108,71,255,0.1); padding:4px 14px; border-radius:20px; margin-bottom:14px; }
    .sec-title { font-family:'Plus Jakarta Sans',sans-serif; font-size:clamp(28px,3.5vw,46px); font-weight:800; color:var(--text); line-height:1.15; margin-bottom:16px; }
    .sec-title .accent { color: var(--primary); }
    .sec-desc { font-size:17px; color:var(--text-muted); line-height:1.7; max-width:600px; margin:0 auto; }

    /* ── FEATURES ─────────────────────────────── */
    .feat-card { background:#fff; border-radius:20px; padding:36px 30px; border:1.5px solid #ede9fe; transition:all 0.35s cubic-bezier(.175,.885,.32,1.275); height:100%; position:relative; overflow:hidden; }
    .feat-card::before { content:''; position:absolute; top:0; left:0; right:0; height:3px; background:var(--grad-primary); transform:scaleX(0); transition:transform 0.35s; border-radius:2px 2px 0 0; }
    .feat-card:hover::before { transform:scaleX(1); }
    .feat-card:hover { transform:translateY(-10px); box-shadow:var(--card-shadow-hover); border-color:rgba(108,71,255,0.25); }
    .feat-icon { width:72px; height:72px; border-radius:18px; background:rgba(108,71,255,0.1); display:flex; align-items:center; justify-content:center; font-size:30px; color:var(--primary); margin-bottom:22px; transition:all 0.35s; }
    .feat-card:hover .feat-icon { background:var(--grad-primary); color:#fff; transform:scale(1.1) rotate(-5deg); }
    .feat-title { font-size:20px; font-weight:700; color:var(--text); margin-bottom:12px; }
    .feat-desc { font-size:14px; color:var(--text-muted); line-height:1.75; }

    /* ── STATS ────────────────────────────────── */
    .stats-section { background:var(--grad-primary); padding:80px 0; position:relative; overflow:hidden; }
    .stats-section::before { content:''; position:absolute; top:-100px; right:-100px; width:400px; height:400px; background:rgba(255,255,255,0.06); border-radius:50%; }
    .stats-section::after  { content:''; position:absolute; bottom:-100px; left:-100px; width:500px; height:500px; background:rgba(255,255,255,0.04); border-radius:50%; }
    .stat-item { text-align:center; position:relative; z-index:2; }
    .stat-num { font-size:52px; font-weight:900; color:#fff; line-height:1; margin-bottom:8px; }
    .stat-lbl { font-size:15px; color:rgba(255,255,255,0.8); font-weight:500; }
    .stat-sep { width:1px; background:rgba(255,255,255,0.15); align-self:stretch; }

    /* ── COURSES ──────────────────────────────── */
    .courses-section { background:linear-gradient(160deg,#0d0b1f 0%,#1a1045 60%,#0d1b4b 100%); padding:100px 0; position:relative; overflow:hidden; }
    .courses-section::before { content:''; position:absolute; top:-200px; right:-200px; width:600px; height:600px; background:radial-gradient(circle,rgba(108,71,255,0.18) 0%,transparent 70%); border-radius:50%; }
    .courses-section .sec-tag { color:#a78bfa; background:rgba(108,71,255,0.2); }
    .courses-section .sec-title { color:#fff; }
    .courses-section .sec-desc { color:rgba(255,255,255,0.6); }
    .course-card { background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.09); backdrop-filter:blur(12px); border-radius:20px; overflow:hidden; transition:all 0.35s cubic-bezier(.175,.885,.32,1.275); height:100%; position:relative; max-width:340px; margin:0 auto; }
    .course-card:hover { transform:translateY(-8px) scale(1.01); border-color:rgba(108,71,255,0.4); box-shadow:0 24px 60px rgba(0,0,0,0.4),0 0 40px rgba(108,71,255,0.15); }
    .course-img-wrap { height:160px; overflow:hidden; position:relative; }
    .course-img-wrap img { width:100%; height:100%; object-fit:cover; transition:transform 0.5s ease; }
    .course-card:hover .course-img-wrap img { transform:scale(1.08); }
    .course-img-overlay { position:absolute; inset:0; background:linear-gradient(180deg,transparent 40%,rgba(13,11,31,0.9) 100%); }
    .course-no-img { height:160px; display:flex; align-items:center; justify-content:center; background:linear-gradient(135deg,rgba(108,71,255,0.2),rgba(155,89,255,0.2)); font-size:50px; }
    .course-badge { position:absolute; top:10px; left:10px; background:var(--grad-accent); color:#fff; font-size:10px; font-weight:700; padding:3px 10px; border-radius:20px; letter-spacing:0.5px; }
    .course-body { padding:18px; }
    .course-title { font-size:16px; font-weight:700; color:#fff; margin-bottom:6px; line-height:1.4; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden; height:2.8rem; }
    .course-desc { font-size:12px; color:rgba(255,255,255,0.5); line-height:1.6; margin-bottom:12px; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden; height:2.4rem; }
    .course-meta { display:flex; gap:6px; flex-wrap:wrap; margin-bottom:14px; }
    .course-meta span { font-size:11px; font-weight:600; color:rgba(255,255,255,0.65); display:flex; align-items:center; gap:4px; background:rgba(255,255,255,0.07); border:1px solid rgba(255,255,255,0.1); padding:4px 8px; border-radius:20px; }
    .course-meta i { color:#a78bfa; }
    .btn-view-course { display:block; background:var(--grad-primary); color:#fff; border:none; border-radius:12px; padding:10px 16px; font-size:13px; font-weight:700; text-decoration:none; text-align:center; transition:all 0.3s; box-shadow:0 6px 20px rgba(108,71,255,0.4); }
    .btn-view-course:hover { transform:translateY(-2px); box-shadow:0 10px 30px rgba(108,71,255,0.6); color:#fff; }
    .btn-browse-all { display:inline-flex; align-items:center; gap:10px; background:transparent; border:2px solid rgba(255,255,255,0.25); color:#fff; padding:14px 40px; border-radius:50px; font-size:15px; font-weight:700; text-decoration:none; transition:all 0.35s; backdrop-filter:blur(8px); }
    .btn-browse-all:hover { background:#fff; color:var(--primary); border-color:#fff; transform:translateY(-4px); box-shadow:0 15px 40px rgba(255,255,255,0.15); }
    .btn-browse-all i:last-child { transition:transform 0.3s; }
    .btn-browse-all:hover i:last-child { transform:translateX(6px); }

    /* ── HOW IT WORKS ─────────────────────────── */
    .how-step { text-align:center; position:relative; }
    .how-step-num { width:56px; height:56px; background:var(--grad-primary); color:#fff; border-radius:50%; font-size:22px; font-weight:800; display:flex; align-items:center; justify-content:center; margin:0 auto 20px; box-shadow:0 8px 24px rgba(108,71,255,0.4); }
    .how-step-connector { position:absolute; top:28px; left:calc(50% + 28px); right:calc(-50% + 28px); height:2px; background:linear-gradient(90deg,var(--primary),transparent); }
    .how-step-icon { font-size:36px; margin-bottom:14px; }
    .how-step-title { font-size:18px; font-weight:700; color:var(--text); margin-bottom:10px; }
    .how-step-desc { font-size:14px; color:var(--text-muted); line-height:1.7; }

    /* ── TESTIMONIALS ─────────────────────────── */
    .testi-section { background:linear-gradient(135deg,#f8f7ff 0%,#ede9fe 100%); padding:100px 0; }
    .testi-card { background:#fff; border-radius:20px; padding:28px; box-shadow:0 4px 24px rgba(108,71,255,0.08); border-top:4px solid var(--primary); height:100%; display:flex; flex-direction:column; transition:all 0.3s; }
    .testi-card:hover { transform:translateY(-8px); box-shadow:0 16px 48px rgba(108,71,255,0.16); }
    .testi-avatar { width:64px; height:64px; border-radius:50%; object-fit:cover; border:3px solid #ede9fe; }
    .testi-name { font-size:17px; font-weight:700; color:var(--text); margin-bottom:3px; }
    .testi-company { font-size:13px; color:var(--primary); font-weight:600; }
    .testi-quote { font-size:14px; color:var(--text-muted); line-height:1.7; font-style:italic; flex-grow:1; display:-webkit-box; -webkit-line-clamp:5; -webkit-box-orient:vertical; overflow:hidden; }
    .testi-stars { color:#f59e0b; letter-spacing:2px; font-size:13px; margin-bottom:14px; }

    /* ── ABOUT ────────────────────────────────── */
    .about-check { display:flex; align-items:flex-start; gap:12px; margin-bottom:16px; }
    .about-check-icon { width:28px; height:28px; background:rgba(0,212,170,0.1); border-radius:50%; display:flex; align-items:center; justify-content:center; flex-shrink:0; margin-top:2px; }
    .about-check-icon i { font-size:12px; color:var(--accent); }
    .about-check-text { font-size:15px; color:var(--text); font-weight:500; }

    /* ── CTA BAND ─────────────────────────────── */
    .cta-band { background:var(--grad-primary); padding:80px 0; text-align:center; position:relative; overflow:hidden; }
    .cta-band::before { content:''; position:absolute; top:-80px; left:-80px; width:300px; height:300px; background:rgba(255,255,255,0.06); border-radius:50%; }
    .cta-band::after  { content:''; position:absolute; bottom:-80px; right:-80px; width:400px; height:400px; background:rgba(255,255,255,0.04); border-radius:50%; }
    .cta-band h2 { font-family:'Plus Jakarta Sans',sans-serif; font-size:clamp(26px,3.5vw,44px); font-weight:800; color:#fff; margin-bottom:14px; position:relative; z-index:2; }
    .cta-band p  { font-size:17px; color:rgba(255,255,255,0.8); margin-bottom:36px; position:relative; z-index:2; }
    .btn-cta-white { background:#fff; color:var(--primary); padding:15px 40px; border-radius:50px; font-size:16px; font-weight:700; text-decoration:none; display:inline-flex; align-items:center; gap:10px; transition:all 0.3s; box-shadow:0 8px 30px rgba(0,0,0,0.2); position:relative; z-index:2; }
    .btn-cta-white:hover { transform:translateY(-4px); box-shadow:0 16px 48px rgba(0,0,0,0.3); color:var(--primary-dark); }

    /* ── FOOTER ───────────────────────────────── */
    .footer-pub { background:linear-gradient(160deg,#0d0b1f 0%,#0d1b4b 100%); color:#fff; padding:72px 0 28px; }
    .footer-brand-img { height:42px; filter:brightness(0) invert(1); }
    .footer-about { font-size:14px; color:rgba(255,255,255,0.55); line-height:1.8; margin-top:14px; }
    .footer-social { display:flex; gap:12px; margin-top:22px; }
    .footer-social a { width:38px; height:38px; border-radius:50%; background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.12); display:flex; align-items:center; justify-content:center; color:rgba(255,255,255,0.7); text-decoration:none; font-size:15px; transition:all 0.3s; }
    .footer-social a:hover { background:var(--primary); border-color:var(--primary); color:#fff; transform:translateY(-3px); }
    .footer-heading { font-size:15px; font-weight:700; color:#fff; margin-bottom:20px; }
    .footer-links { list-style:none; padding:0; margin:0; }
    .footer-links li { margin-bottom:10px; }
    .footer-links a { font-size:14px; color:rgba(255,255,255,0.6); text-decoration:none; transition:all 0.3s; display:inline-flex; align-items:center; gap:6px; }
    .footer-links a:hover { color:#fff; padding-left:4px; }
    .footer-contact-item { display:flex; align-items:flex-start; gap:10px; margin-bottom:14px; }
    .footer-contact-icon { width:30px; height:30px; border-radius:50%; background:rgba(108,71,255,0.15); display:flex; align-items:center; justify-content:center; flex-shrink:0; }
    .footer-contact-icon i { font-size:12px; color:var(--primary-light); }
    .footer-contact-text { font-size:13px; color:rgba(255,255,255,0.65); line-height:1.6; }
    .footer-contact-text a { color:rgba(255,255,255,0.65); text-decoration:none; }
    .footer-contact-text a:hover { color:#fff; }
    .footer-bottom { border-top:1px solid rgba(255,255,255,0.07); padding-top:24px; margin-top:48px; }

    /* ── ANIMATIONS ───────────────────────────── */
    @keyframes fadeUp { from { opacity:0; transform:translateY(28px); } to { opacity:1; transform:translateY(0); } }
    @keyframes float { 0%,100% { transform:translateY(0); } 50% { transform:translateY(-14px); } }

    /* ── RESPONSIVE ───────────────────────────── */
    @media(max-width:991px) {
        .hero-content { padding:120px 0 60px; }
        .hero-image-wrap { margin-top:40px; }
        .hero-badge { display:none; }
        .stat-sep { display:none; }
        .how-step-connector { display:none; }
    }
    @media(max-width:768px) {
        .hero-stats { gap:20px; }
        .hero-stat { min-width:unset; border-right:none !important; margin-right:0 !important; padding-right:0 !important; }
        .section { padding:70px 0; }
        .stats-section { padding:60px 0; }
    }
    </style>
	<style>
	.upc-overlay{position:fixed;inset:0;z-index:99999;background:rgba(3,2,10,0.72);backdrop-filter:blur(8px);display:none;align-items:center;justify-content:center;padding:20px}
	.upc-modal{width:min(980px,96vw);border-radius:26px;overflow:hidden;background:linear-gradient(135deg, rgba(255,255,255,0.96) 0%, rgba(248,247,255,0.98) 100%);box-shadow:0 40px 110px rgba(0,0,0,0.45);border:1px solid rgba(108,71,255,0.18);position:relative;animation:upcPop 260ms ease-out}
	@keyframes upcPop{from{transform:translateY(18px) scale(0.98);opacity:0}to{transform:translateY(0) scale(1);opacity:1}}
	.upc-head{padding:22px 26px;background:linear-gradient(135deg,#6c47ff 0%,#9b59ff 100%);color:#fff;display:flex;align-items:center;justify-content:space-between;gap:18px}
	.upc-title{margin:0;font-weight:900;letter-spacing:-0.5px;font-size:22px;display:flex;align-items:center;gap:10px}
	.upc-sub{margin:0;opacity:0.85;font-size:13px;font-weight:600}
	.upc-close{border:none;background:rgba(255,255,255,0.18);color:#fff;width:42px;height:42px;border-radius:14px;font-size:22px;line-height:1;display:flex;align-items:center;justify-content:center;transition:all .2s}
	.upc-close:hover{background:rgba(255,255,255,0.26);transform:translateY(-1px)}
	.upc-body{padding:22px 26px}
	.upc-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
	@media (max-width: 900px){.upc-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
	@media (max-width: 560px){.upc-grid{grid-template-columns:1fr}.upc-head{align-items:flex-start;flex-direction:column}}
	.upc-card{background:#fff;border-radius:18px;border:1px solid rgba(108,71,255,0.12);box-shadow:0 10px 26px rgba(108,71,255,0.10);overflow:hidden;transition:all .25s;max-width:320px;margin:0 auto;}
	.upc-card:hover{transform:translateY(-4px);box-shadow:0 18px 46px rgba(108,71,255,0.18)}
	.upc-img{height:110px;background:linear-gradient(135deg, rgba(108,71,255,0.16), rgba(0,212,170,0.12));display:flex;align-items:center;justify-content:center;overflow:hidden}
	.upc-img img{width:100%;height:100%;object-fit:cover}
	.upc-c{padding:12px 12px 14px}
	.upc-name{margin:0 0 6px;font-weight:900;font-size:13px;color:#0d0b1f;line-height:1.3;height:2.6rem;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;}
	.upc-meta{display:flex;flex-wrap:wrap;gap:6px;font-size:11px;font-weight:700;color:#64748b}
	.upc-pill{display:inline-flex;align-items:center;gap:5px;padding:4px 10px;border-radius:999px;background:rgba(108,71,255,0.08);color:#6c47ff;border:1px solid rgba(108,71,255,0.12); font-size: 10px;}
	.upc-pill-date{background:rgba(0, 212, 170, 0.08); color:#00a381; border: 1px solid rgba(0, 212, 170, 0.15);}
	.upc-pill-duration{background:rgba(108, 71, 255, 0.08); color:#6c47ff; border: 1px solid rgba(108, 71, 255, 0.15);}
	.upc-actions{display:flex;gap:10px;flex-wrap:wrap;justify-content:flex-end;margin-top:16px}
	.upc-btn{display:inline-flex;align-items:center;gap:8px;padding:10px 16px;border-radius:999px;text-decoration:none;font-weight:800;font-size:13px;border:1px solid rgba(108,71,255,0.25);color:#6c47ff;background:#fff;transition:all .2s}
	.upc-btn:hover{background:rgba(108,71,255,0.07)}
	.upc-btn-primary{background:linear-gradient(135deg,#6c47ff 0%,#9b59ff 100%);border:none;color:#fff}
	.upc-btn-primary:hover{filter:brightness(1.03);transform:translateY(-1px)}
	</style>
</head>
<body>
<style>
/* Enhanced Navbar (from landing.php) */
.navbar {
    background: rgba(255, 255, 255, 0.98);
    backdrop-filter: blur(10px);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
    padding: 12px 0;
    transition: all 0.3s ease;
    border-radius: 50px;
    margin: 15px 20px 0;
    border: 1px solid rgba(0, 0, 0, 0.05);
}

.navbar.scrolled {
    padding: 10px 0;
    background: rgba(255, 255, 255, 0.98);
    box-shadow: 0 4px 25px rgba(0, 0, 0, 0.1);
    margin: 10px 20px 0;
    border-radius: 50px;
    border: 1px solid rgba(0, 0, 0, 0.05);
}

.navbar-brand {
    font-size: 26px;
    font-weight: 800;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    background-clip: text;
    letter-spacing: -1px;
    transition: all 0.3s;
    text-decoration: none;
    white-space: nowrap !important;
    flex-shrink: 0;
}

.navbar-brand:hover {
    transform: scale(1.05);
}

.navbar-brand img {
    height: 38px;
    margin-right: 12px;
    filter: none;
    transition: all 0.3s;
}

.navbar-brand:hover img {
    filter: brightness(1.1);
}

.navbar-nav {
    display: flex;
    align-items: center;
    flex-wrap: nowrap !important;
    white-space: nowrap !important;
}

.nav-item {
    white-space: nowrap !important;
    flex-shrink: 0;
}

.nav-link {
    color: #334155 !important;
    font-weight: 600;
    margin: 0 3px;
    padding: 6px 10px !important;
    border-radius: 25px;
    transition: all 0.3s;
    position: relative;
    font-size: 13.5px;
    white-space: nowrap !important;
    display: inline-block;
}

.nav-link::before {
    content: '';
    position: absolute;
    bottom: 5px;
    left: 50%;
    transform: translateX(-50%);
    width: 0;
    height: 3px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 2px;
    transition: width 0.3s;
}

.nav-link:hover {
    color: #667eea !important;
    background: rgba(102, 126, 234, 0.08);
}

.nav-link:hover::before {
    width: 60%;
}

.nav-link.active {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white !important;
}

/* ── Premium Dropdown ───────────────────────────── */
.dropdown { position: relative; }
.dropdown-toggle::after { display: none; }

.dropdown-menu {
    background: #ffffff;
    border: 1px solid rgba(108,71,255,0.12);
    border-radius: 18px;
    box-shadow: 0 20px 60px rgba(13,11,31,0.18), 0 0 0 1px rgba(108,71,255,0.08);
    padding: 0;
    min-width: 280px;
    margin-top: 12px !important;
    overflow: hidden;
    animation: dropFadeIn 0.2s cubic-bezier(.175,.885,.32,1.275) both;
    transform-origin: top center;
}
@keyframes dropFadeIn {
    from { opacity: 0; transform: translateY(-10px) scale(0.97); }
    to   { opacity: 1; transform: translateY(0) scale(1); }
}
.dropdown-header-band {
    background: linear-gradient(135deg, #6c47ff 0%, #9b59ff 100%);
    padding: 13px 16px 11px;
    display: flex; align-items: center; gap: 10px;
}
.dropdown-header-band .dh-icon { width:30px;height:30px;background:rgba(255,255,255,0.18);border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:13px;color:#fff;flex-shrink:0; }
.dropdown-header-band .dh-text { font-size:12px;font-weight:700;color:#fff;letter-spacing:0.3px; }
.dropdown-header-band .dh-sub  { font-size:10px;color:rgba(255,255,255,0.7);margin-top:1px; }
.dropdown-items-wrap { padding: 6px 0; }
.dropdown-item {
    display: flex; align-items: center; gap: 10px;
    padding: 9px 14px; color: #1a1a2e; font-weight: 600; font-size: 13.5px;
    transition: all 0.2s ease; border-radius: 0; margin: 0; position: relative;
}
.dropdown-item .di-icon {
    width:28px;height:28px;border-radius:8px;background:rgba(108,71,255,0.08);
    display:flex;align-items:center;justify-content:center;font-size:12px;color:#6c47ff;
    flex-shrink:0;transition:all 0.2s;
}
.dropdown-item:hover { background:rgba(108,71,255,0.07);color:#6c47ff;padding-left:18px; }
.dropdown-item:hover .di-icon { background:linear-gradient(135deg,#6c47ff,#9b59ff);color:#fff;box-shadow:0 4px 10px rgba(108,71,255,0.3); }
.dropdown-item:hover::after { content:'';position:absolute;left:0;top:0;bottom:0;width:3px;background:linear-gradient(180deg,#6c47ff,#9b59ff);border-radius:0 2px 2px 0; }
.dropdown-divider-custom { margin:3px 0;border:none;height:1px;background:linear-gradient(90deg,transparent,rgba(108,71,255,0.15),transparent); }
.dropdown-item-special { background:rgba(0,212,170,0.05); }
.dropdown-item-special .di-icon { background:rgba(0,212,170,0.1);color:#00b894; }
.dropdown-item-special:hover { background:rgba(0,212,170,0.1);color:#00a381; }
.dropdown-item-special:hover .di-icon { background:linear-gradient(135deg,#00d4aa,#00b894);color:#fff;box-shadow:0 4px 10px rgba(0,212,170,0.3); }
.dropdown-item-special:hover::after { background:linear-gradient(180deg,#00d4aa,#00b894); }
.dropdown-footer-link { display:flex;align-items:center;justify-content:center;gap:6px;padding:9px 14px;font-size:12px;font-weight:700;color:#6c47ff;text-decoration:none;border-top:1px solid rgba(108,71,255,0.1);transition:all 0.2s; }
.dropdown-footer-link:hover { background:rgba(108,71,255,0.05);color:#5035cc; }

.navbar-toggler {
    border: 2px solid rgba(102,126,234,0.6);
    padding: 8px 12px;
}
.navbar-toggler-icon {
    filter: none;
}

.navbar-toggler:focus {
    box-shadow: 0 0 0 0.2rem rgba(102, 126, 234, 0.25);
}

/* Navbar Login Buttons */
.navbar-login-buttons {
    display: flex;
    align-items: center;
    gap: 8px;
    white-space: nowrap !important;
    flex-shrink: 0;
}

.navbar-login-buttons .btn {
    font-size: 13px;
    font-weight: 600;
    padding: 7px 14px;
    border-radius: 20px;
    transition: all 0.3s ease;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    white-space: nowrap !important;
    flex-shrink: 0;
}

.navbar-login-buttons .btn-outline-primary {
    border-color: #667eea;
    color: #667eea;
}

.navbar-login-buttons .btn-outline-primary:hover {
    background: #667eea;
    color: white;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

.navbar-login-buttons .btn-primary {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border: none;
    color: white;
}

.navbar-login-buttons .btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
}

@media (min-width: 992px) and (max-width: 1200px) {
    .nav-link {
        padding: 5px 6px !important;
        margin: 0 1px;
        font-size: 12.5px;
    }
    .navbar-login-buttons .btn {
        padding: 6px 10px;
        font-size: 12px;
        gap: 4px;
    }
}

@media (max-width: 768px) {
    .navbar {
        margin: 0 10px;
        border-radius: 15px;
    }
    
    .navbar-login-buttons {
        flex-direction: column;
        gap: 8px;
        margin-top: 15px;
        width: 100%;
    }
    
    .navbar-login-buttons .btn {
        width: 100%;
        justify-content: center;
    }
}

/* ── Floating CTA Bot Button ───────────────────── */
.floating-bot-btn {
    position: fixed;
    bottom: 30px;
    right: 30px;
    width: 60px;
    height: 60px;
    background: linear-gradient(135deg, #6c47ff 0%, #00d4aa 100%);
    color: #ffffff !important;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 10px 30px rgba(108, 71, 255, 0.4);
    z-index: 99999;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    text-decoration: none;
}

.floating-bot-btn:hover {
    transform: translateY(-5px) scale(1.08);
    box-shadow: 0 15px 35px rgba(108, 71, 255, 0.6), 0 0 15px rgba(0, 212, 170, 0.4);
}

.floating-bot-btn i {
    font-size: 26px;
    animation: botPulse 2s infinite ease-in-out;
}

.floating-bot-btn::after {
    content: '';
    position: absolute;
    width: 100%;
    height: 100%;
    background: inherit;
    border-radius: 50%;
    z-index: -1;
    opacity: 0.4;
    animation: botGlow 2s infinite ease-out;
}

.floating-bot-btn .bot-tooltip {
    position: absolute;
    right: 75px;
    background: #0d0b1f;
    color: #fff;
    padding: 8px 16px;
    border-radius: 30px;
    font-size: 12px;
    font-weight: 700;
    white-space: nowrap;
    opacity: 0;
    pointer-events: none;
    transition: all 0.3s ease;
    box-shadow: 0 8px 24px rgba(108, 71, 255, 0.2);
    border: 1px solid rgba(255, 255, 255, 0.08);
}

.floating-bot-btn:hover .bot-tooltip {
    opacity: 1;
    transform: translateX(-5px);
}

@keyframes botPulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.08); }
}

@keyframes botGlow {
    0% { transform: scale(1); opacity: 0.6; }
    100% { transform: scale(1.5); opacity: 0; }
}

@media (max-width: 768px) {
    .floating-bot-btn {
        bottom: 20px;
        right: 20px;
        width: 50px;
        height: 50px;
    }
    .floating-bot-btn i {
        font-size: 22px;
    }
    .floating-bot-btn .bot-tooltip {
        display: none;
    }
}
</style>

<!-- Marquee Section -->
<!-- Marquee Debug Info:
     Conn Status: set (type: object)
     Query Status: success     Query Error:      Count: 2-->
<div class="marquee-announcement">
    <span class="marquee-badge text-nowrap animate-pulse-badge">
        <i class="fas fa-bullhorn me-2 animate-bell"></i> Latest Update
    </span>
    <marquee behavior="scroll" direction="left" onmouseover="this.stop();" onmouseout="this.start();" scrollamount="6" style="line-height: 30px;">
        <span class="mx-4">
            <a href="#" data-bs-toggle="modal" data-bs-target="#seminarRegModal" class="text-danger text-decoration-none hover-underline fw-bold font-bold" style="animation: pulse-text 1.5s infinite alternate;">
                🔥 REGISTER FOR SEMINAR NOW - CLICK HERE! 🔥
            </a>
        </span>
        <span class="text-danger fw-bold">|</span>
                    <span class="mx-4">
                                    <a href="https://msxportal.in/course_details.php?id=11" target="_blank" class="text-dark text-decoration-none hover-underline fw-bold">
                        New batch Start Python Data Science <i class="fas fa-external-link-alt ms-1 small"></i>
                    </a>
                            </span>
            <span class="text-danger fw-bold">|</span>
                    <span class="mx-4">
                                    <a href="https://msxportal.in/course_details.php?id=11" target="_blank" class="text-dark text-decoration-none hover-underline fw-bold">
                        New batch Start Data Science And AI - 6:00 pm to 7:30 pm <i class="fas fa-external-link-alt ms-1 small"></i>
                    </a>
                            </span>
            <span class="text-danger fw-bold">|</span>
            </marquee>
</div>
<style>
.marquee-announcement {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1040;
    height: 30px;
    background: #ffc107;
    border-bottom: 1px solid rgba(0,0,0,0.08);
    display: flex;
    align-items: center;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}
.marquee-badge {
    background: #dc3545;
    color: #fff;
    padding: 0 12px;
    height: 30px;
    display: flex;
    align-items: center;
    font-weight: 700;
    font-size: 11px;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    z-index: 1045;
    box-shadow: 2px 0 5px rgba(0,0,0,0.1);
}
.hover-underline:hover {
    text-decoration: underline !important;
}
.animate-bell {
    display: inline-block;
    animation: ring-bell 2s infinite ease-in-out;
}
.animate-pulse-badge {
    animation: pulse-bg 2s infinite ease-in-out;
}
@keyframes ring-bell {
    0% { transform: rotate(0); }
    10% { transform: rotate(15deg); }
    20% { transform: rotate(-10deg); }
    30% { transform: rotate(10deg); }
    40% { transform: rotate(-5deg); }
    50% { transform: rotate(5deg); }
    60% { transform: rotate(0); }
    100% { transform: rotate(0); }
}
@keyframes pulse-bg {
    0% { filter: brightness(1); }
    50% { filter: brightness(1.15); }
    100% { filter: brightness(1); }
}
@keyframes pulse-text {
    0% { color: #dc3545; text-shadow: 0 0 2px rgba(220, 53, 69, 0.2); }
    100% { color: #850612; text-shadow: 0 0 8px rgba(220, 53, 69, 0.5); }
}
/* Push floating navbar down below fixed marquee */
.navbar {
    margin-top: 45px !important;
}
.navbar.scrolled {
    margin-top: 40px !important;
}
body {
    padding-top: 30px !important;
}
</style>

<nav class="navbar navbar-expand-lg fixed-top">
    <div class="container-fluid px-lg-4 px-md-3 px-2">
        <a class="navbar-brand d-flex flex-column align-items-start" href="https://msxportal.in/landing.php" style="padding: 0; margin: 0;">
            <img src="https://msxportal.in/assets/images/dlogo.png" alt="MSX Portal" style="height: 34px;">
            <small style="font-size: 8px; font-weight: 700; color: #a78bfa; letter-spacing: 0.2px; text-transform: uppercase; margin-top: 2px; line-height: 1; white-space: nowrap;">An Initiative of Ctronics Infotech</small>
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav mx-auto">
                <li class="nav-item">
                    <a class="nav-link active" href="https://msxportal.in/landing.php#home">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="https://msxportal.in/landing.php#about">About</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="https://msxportal.in/landing.php#features">Features</a>
                </li>

                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle " href="#" id="coursesDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Courses <i class="fas fa-chevron-down ms-1"></i>
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="coursesDropdown">
                        <li>
                            <div class="dropdown-header-band">
                                <div class="dh-icon"><i class="fas fa-graduation-cap"></i></div>
                                <div>
                                    <div class="dh-text">All Programs</div>
                                    <div class="dh-sub">Choose your learning path</div>
                                </div>
                            </div>
                        </li>
                        <div class="dropdown-items-wrap">
                                                <li>
                            <a class="dropdown-item" href="https://msxportal.in/courses.php?cat=MSXINT">
                                <span class="di-icon"><i class="fas fa-code"></i></span>
                                Internship Programs                            </a>
                        </li>
                                                <li>
                            <a class="dropdown-item" href="https://msxportal.in/courses.php?cat=MSXBCW">
                                <span class="di-icon"><i class="fas fa-chart-bar"></i></span>
                                Bootcamp Workshops                            </a>
                        </li>
                                                <li>
                            <a class="dropdown-item" href="https://msxportal.in/courses.php?cat=MSXMAP">
                                <span class="di-icon"><i class="fas fa-cogs"></i></span>
                                Management Analytics Program                            </a>
                        </li>
                                                <li>
                            <a class="dropdown-item" href="https://msxportal.in/courses.php?cat=MSXWEB">
                                <span class="di-icon"><i class="fas fa-brain"></i></span>
                                Free Webinars                            </a>
                        </li>
                                                </div>
                        <a class="dropdown-footer-link" href="https://msxportal.in/courses.php">
                            <i class="fas fa-th-large"></i> View All Courses <i class="fas fa-arrow-right" style="font-size:10px;"></i>
                        </a>
                    </ul>
                </li>
                <li class="nav-item">
                    <a class="nav-link " href="https://msxportal.in/upcoming-courses.php">Upcoming Courses</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link " href="https://msxportal.in/contact.php">Contact</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="https://internify.ctronicsinfotech.in/" target="_blank" rel="noopener noreferrer">Careers</a>
                </li>
            </ul>
            <div class="navbar-login-buttons">
                <a href="https://msxportal.in/student_login.php" class="btn btn-outline-primary btn-sm">
                    <i class="fas fa-user-graduate"></i> Student Login
                </a>
                <a href="https://msxportal.in/college/login.php" class="btn btn-primary btn-sm">
                    <i class="fas fa-university"></i> College Login
                </a>
            </div>
        </div>
    </div>
</nav>

<script>
// Navbar Scroll Effect
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});
</script>

<!-- Floating CTA Bot Button -->
<a href="#" class="floating-bot-btn" aria-label="Support Bot">
    <i class="fas fa-robot"></i>
    <span class="bot-tooltip">Support Bot</span>
</a>

<!-- Seminar Registration Modal -->
<div class="modal fade" id="seminarRegModal" tabindex="-1" aria-labelledby="seminarRegModalLabel" aria-hidden="true" style="z-index: 1060;">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content seminar-modal-content border-0 shadow-lg" style="border-radius: 16px; overflow: hidden;">
            <div class="modal-header seminar-modal-header border-0 text-white p-4 position-relative" style="background: linear-gradient(135deg, #6c47ff 0%, #3f1fb8 100%);">
                <div class="seminar-header-overlay" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-image: radial-gradient(circle at 80% 20%, rgba(255,255,255,0.15) 0%, transparent 50%); pointer-events: none;"></div>
                <div class="position-relative" style="z-index: 1;">
                    <span class="badge bg-warning text-dark fw-bold mb-2 px-3 py-1 text-uppercase tracking-wider" style="font-size: 10px; border-radius: 30px;">Interactive Seminar</span>
                    <h4 class="modal-title fw-bold" id="seminarRegModalLabel">Secure Your Spot</h4>
                    <p class="text-white-50 mb-0 small">Enter details below to register and join the WhatsApp group</p>
                </div>
                <button type="button" class="btn-close btn-close-white position-absolute top-0 end-0 m-3" style="z-index: 2;" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body p-4 bg-light">
                <div id="seminarFormContainer">
                    <form id="seminarRegisterForm" novalidate>
                        <!-- Error Alert -->
                        <div id="seminarError" class="alert alert-danger d-none" role="alert"></div>
                        
                        <div class="mb-3">
                            <label for="semName" class="form-label fw-semibold text-dark small mb-1">Full Name <span class="text-danger">*</span></label>
                            <div class="input-group">
                                <span class="input-group-text bg-white border-end-0 text-muted" style="border-color: #dee2e6;"><i class="fas fa-user"></i></span>
                                <input type="text" class="form-control border-start-0 ps-0 shadow-none" id="semName" name="full_name" placeholder="E.g. Rahul Sharma" required style="border-color: #dee2e6;">
                            </div>
                        </div>
                        
                        <div class="mb-3">
                            <label for="semCollege" class="form-label fw-semibold text-dark small mb-1">College Name <span class="text-danger">*</span></label>
                            <div class="input-group">
                                <span class="input-group-text bg-white border-end-0 text-muted" style="border-color: #dee2e6;"><i class="fas fa-university"></i></span>
                                <input type="text" class="form-control border-start-0 ps-0 shadow-none" id="semCollege" name="college" placeholder="E.g. XYZ Institute of Technology" required style="border-color: #dee2e6;">
                            </div>
                        </div>

                        <div class="mb-3">
                            <label for="semPhone" class="form-label fw-semibold text-dark small mb-1">WhatsApp Phone Number <span class="text-danger">*</span></label>
                            <div class="input-group">
                                <span class="input-group-text bg-white border-end-0 text-muted" style="border-color: #dee2e6;"><i class="fas fa-phone"></i></span>
                                <input type="tel" class="form-control border-start-0 ps-0 shadow-none" id="semPhone" name="phone" placeholder="E.g. 9876543210" required style="border-color: #dee2e6;">
                            </div>
                        </div>

                        <div class="mb-4">
                            <label for="semYear" class="form-label fw-semibold text-dark small mb-1">Year of Study <span class="text-danger">*</span></label>
                            <div class="input-group">
                                <span class="input-group-text bg-white border-end-0 text-muted" style="border-color: #dee2e6;"><i class="fas fa-graduation-cap"></i></span>
                                <select class="form-select border-start-0 ps-0 shadow-none" id="semYear" name="year" required style="border-color: #dee2e6;">
                                    <option value="" disabled selected>Select your current year</option>
                                    <option value="1st">1st Year</option>
                                    <option value="2nd">2nd Year</option>
                                    <option value="3rd">3rd Year</option>
                                    <option value="Final">Final Year</option>
                                </select>
                            </div>
                        </div>

                        <button type="submit" class="btn btn-seminar-submit w-100 py-2.5 fw-bold text-white border-0 shadow-sm transition-all" style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); border-radius: 8px; transition: all 0.3s ease;">
                            <span class="submit-text">Register &amp; Join WhatsApp Group</span>
                            <span class="spinner-border spinner-border-sm d-none ms-2" role="status" aria-hidden="true"></span>
                        </button>
                    </form>
                </div>
                
                <!-- Success State -->
                <div id="seminarSuccessContainer" class="text-center py-4 d-none">
                    <div class="seminar-success-icon-wrapper mb-3">
                        <i class="fas fa-check-circle text-success" style="font-size: 56px; animation: bounce 1s infinite alternate;"></i>
                    </div>
                    <h5 class="fw-bold text-dark">Registration Successful!</h5>
                    <p class="text-muted small px-3">We are taking you to the WhatsApp group to complete your joining...</p>
                    <div class="progress mt-3 mx-4" style="height: 6px; border-radius: 10px;">
                        <div class="progress-bar bg-success progress-bar-striped progress-bar-animated" role="progressbar" style="width: 100%; border-radius: 10px;"></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
.btn-seminar-submit:hover {
    background: linear-gradient(135deg, #059669 0%, #047857 100%) !important;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(16, 185, 129, 0.2);
}
.seminar-modal-content input:focus, 
.seminar-modal-content select:focus {
    border-color: #6c47ff !important;
}
.seminar-modal-content input:focus + .input-group-text,
.seminar-modal-content select:focus + .input-group-text {
    border-color: #6c47ff !important;
}
@keyframes bounce {
    0% { transform: translateY(0); }
    100% { transform: translateY(-8px); }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('seminarRegisterForm');
    const formContainer = document.getElementById('seminarFormContainer');
    const successContainer = document.getElementById('seminarSuccessContainer');
    const errorDiv = document.getElementById('seminarError');
    const submitBtn = form ? form.querySelector('button[type="submit"]') : null;
    const submitText = submitBtn ? submitBtn.querySelector('.submit-text') : null;
    const spinner = submitBtn ? submitBtn.querySelector('.spinner-border') : null;

    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            errorDiv.classList.add('d-none');
            errorDiv.textContent = '';
            
            const name = document.getElementById('semName').value.trim();
            const college = document.getElementById('semCollege').value.trim();
            const phone = document.getElementById('semPhone').value.trim();
            const year = document.getElementById('semYear').value;
            
            if (!name || !college || !phone || !year) {
                errorDiv.textContent = 'All fields are required.';
                errorDiv.classList.remove('d-none');
                return;
            }
            
            submitBtn.disabled = true;
            spinner.classList.remove('d-none');
            if (submitText) submitText.textContent = 'Registering...';
            
            const formData = new URLSearchParams();
            formData.append('full_name', name);
            formData.append('college', college);
            formData.append('phone', phone);
            formData.append('year', year);
            
            fetch('https://msxportal.in/seminar_register.php', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: formData.toString()
            })
            .then(res => res.json())
            .then(data => {
                if (data.success) {
                    formContainer.classList.add('d-none');
                    successContainer.classList.remove('d-none');
                    
                    setTimeout(function() {
                        window.location.href = data.whatsapp_url;
                    }, 1500);
                } else {
                    errorDiv.textContent = data.message || 'An error occurred. Please try again.';
                    errorDiv.classList.remove('d-none');
                    submitBtn.disabled = false;
                    spinner.classList.add('d-none');
                    if (submitText) submitText.textContent = 'Register & Join WhatsApp Group';
                }
            })
            .catch(err => {
                console.error(err);
                errorDiv.textContent = 'Network error. Please try again.';
                errorDiv.classList.remove('d-none');
                submitBtn.disabled = false;
                spinner.classList.add('d-none');
                if (submitText) submitText.textContent = 'Register & Join WhatsApp Group';
            });
        });
    }
});
</script>

<!-- ════════════════════════ HERO ════════════════════════ -->
<section class="hero" id="home">
    <div class="hero-glow1"></div>
    <div class="hero-glow2"></div>
    <div class="container">
        <div class="row align-items-center">
            <div class="col-lg-6">
                <div class="hero-content">
                    <div class="hero-eyebrow"><i class="fas fa-bolt"></i> An Initiative Ctronics Infotech</div>
                    <h1 class="hero-title">
                        Launch Your<br>
                        <span class="gradient-text">Tech Career</span><br>
                        with Real Skills
                    </h1>
                    <p class="hero-desc">Master MERN Stack, AI, Data Science &amp; Cloud — through hands-on projects, live mentorship, and guaranteed placement support.</p>
                    <div class="hero-cta">
                        <a href="https://msxportal.in/courses" class="btn-hero-primary"><i class="fas fa-compass"></i> Explore Courses</a>
                        <a href="contact.php" class="btn-hero-outline"><i class="fas fa-calendar-check"></i> Book Free Demo</a>
                    </div>
                    <div class="hero-stats">
                        <div class="hero-stat">
                            <div class="hero-stat-val stat-number" data-target="1000" data-suffix="+">1000+</div>
                            <div class="hero-stat-label">Students Trained</div>
                        </div>
                        <div class="hero-stat">
                            <div class="hero-stat-val stat-number" data-target="300" data-suffix="+">300+</div>
                            <div class="hero-stat-label">Projects Built</div>
                        </div>
                       
                        <div class="hero-stat">
                            <div class="hero-stat-val stat-number" data-target="95" data-suffix="%">95%</div>
                            <div class="hero-stat-label">Placement Rate</div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-lg-6">
                <div class="hero-image-wrap">
                    <img src="assets/images/hero_learning.png" alt="Learn Tech Online" loading="lazy">
                    <div class="hero-badge hero-badge-1">
                        <i class="fas fa-certificate" style="color:#6c47ff;"></i>
                        <span>Industry Certificates</span>
                    </div>
                    <div class="hero-badge hero-badge-2">
                        <i class="fas fa-briefcase" style="color:#00d4aa;"></i>
                        <span>Placement Support</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ════════════════════════ TRUST BAR ════════════════════════ -->
<div class="trust-bar">
    <div class="container">
        <div class="trust-bar-inner">
            <div class="trust-item"><i class="fas fa-check-circle"></i> Industry-Aligned Curriculum</div>
            <div class="trust-item"><i class="fas fa-users"></i> Expert Mentors</div>
            <div class="trust-item"><i class="fas fa-laptop-code"></i> Hands-On Projects</div>
            <div class="trust-item"><i class="fas fa-briefcase"></i> Placement Assistance</div>
            <div class="trust-item"><i class="fas fa-certificate"></i> Verifiable Certificates</div>
            <div class="trust-item"><i class="fas fa-headset"></i> 24/7 Support</div>
        </div>
    </div>
</div>

<!-- ════════════════════════ FEATURES ════════════════════════ -->
<section class="section section-alt" id="features">
    <div class="container">
        <div class="text-center mb-5">
            <span class="sec-tag">Why Choose MSX Portal</span>
            <h2 class="sec-title">Everything You Need to <span class="accent">Succeed</span></h2>
            <p class="sec-desc">A complete learning ecosystem — from live classes and projects to certifications and job placements.</p>
        </div>
        <div class="row g-4">
            <div class="col-lg-4 col-md-6">
                <div class="feat-card">
                    <div class="feat-icon"><i class="fas fa-graduation-cap"></i></div>
                    <div class="feat-title">Structured Learning Path</div>
                    <p class="feat-desc">Follow a professionally structured curriculum with live classes, recorded sessions, assignments, and milestone projects.</p>
                </div>
            </div>
            <div class="col-lg-4 col-md-6">
                <div class="feat-card">
                    <div class="feat-icon"><i class="fas fa-code"></i></div>
                    <div class="feat-title">Real-World Projects</div>
                    <p class="feat-desc">Build production-ready applications with guidance from industry mentors. Projects that make your portfolio stand out.</p>
                </div>
            </div>
            <div class="col-lg-4 col-md-6">
                <div class="feat-card">
                    <div class="feat-icon"><i class="fas fa-video"></i></div>
                    <div class="feat-title">Live &amp; Recorded Classes</div>
                    <p class="feat-desc">Attend live Zoom sessions with expert instructors and access recorded lectures anytime, on any device.</p>
                </div>
            </div>
            <div class="col-lg-4 col-md-6">
                <div class="feat-card">
                    <div class="feat-icon"><i class="fas fa-chart-bar"></i></div>
                    <div class="feat-title">Progress Tracking</div>
                    <p class="feat-desc">Monitor your attendance, assignment scores, test results, and overall progress with detailed analytics dashboards.</p>
                </div>
            </div>
            <div class="col-lg-4 col-md-6">
                <div class="feat-card">
                    <div class="feat-icon"><i class="fas fa-certificate"></i></div>
                    <div class="feat-title">Verified Certificates</div>
                    <p class="feat-desc">Earn industry-recognized certificates and downloadable transcripts to showcase on LinkedIn and to employers.</p>
                </div>
            </div>
            <div class="col-lg-4 col-md-6">
                <div class="feat-card">
                    <div class="feat-icon"><i class="fas fa-briefcase"></i></div>
                    <div class="feat-title">Placement Support</div>
                    <p class="feat-desc">Get mock interviews, resume building sessions, and direct referrals to 40+ hiring partners across India.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ════════════════════════ STATS ════════════════════════ -->
<section class="stats-section">
    <div class="container">
        <div class="row g-4 align-items-center justify-content-center">
            <div class="col-6 col-md-3"><div class="stat-item"><div class="stat-num stat-number" data-target="1000" data-suffix="+">1000+</div><div class="stat-lbl">Students Trained</div></div></div>
            <div class="col-6 col-md-3"><div class="stat-item"><div class="stat-num stat-number" data-target="15" data-suffix="+">15+</div><div class="stat-lbl">Tech Courses</div></div></div>
            <div class="col-6 col-md-3"><div class="stat-item"><div class="stat-num stat-number" data-target="40" data-suffix="+">40+</div><div class="stat-lbl">Hiring Partners</div></div></div>
            <div class="col-6 col-md-3"><div class="stat-item"><div class="stat-num stat-number" data-target="95" data-suffix="%">95%</div><div class="stat-lbl">Placement Rate</div></div></div>
        </div>
    </div>
</section>

<!-- ════════════════════════ POPULAR COURSES ════════════════════════ -->
<section class="courses-section" id="courses">
    <div class="container" style="position:relative;z-index:2;">
        <div class="text-center mb-5">
            <span class="sec-tag">Top Programs</span>
            <h2 class="sec-title" style="color:#fff;">Popular <span style="background:linear-gradient(90deg,#a78bfa,#60d2f5);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">Courses</span></h2>
            <p class="sec-desc" style="color:rgba(255,255,255,0.6);">Explore our most popular programs and kickstart your tech career today</p>
        </div>
                <div class="row g-4 mt-2">
                        <div class="col-lg-4 col-md-6">
                <div class="course-card">
                                        <div class="course-no-img" style="position:relative;">
                        <span>💻</span>
                        <span class="course-badge">MSX-INT-QA</span>                    </div>
                                        <div class="course-body">
                        <h3 class="course-title">AI-Powered QA Engineering Program</h3>
                                                <p class="course-desc">This industry-focused Software QA Engineering Program is designed to help aspiring and experienced QA professionals master Manual Testing, Automation Testing, DevOps Integration, API Testing, and AI-enabled testing practices.</p>
                                                <div class="course-meta">
                                                        <div style="width:100%; margin-bottom:10px;">
                                <span style="background:rgba(0,212,170,0.15); border:1px solid rgba(0,212,170,0.3); color:var(--accent); font-size:11px; padding:4px 10px;">
                                    <i class="fas fa-calendar-check me-1"></i> Batch: Jul 15, 2026                                </span>
                            </div>
                                                        <span><i class="fas fa-clock"></i> 3 Months</span>                        </div>
                        <a href="https://msxportal.in/course_details?id=38" class="btn-view-course"><i class="fas fa-eye me-1"></i> View Details</a>
                    </div>
                </div>
            </div>
                        <div class="col-lg-4 col-md-6">
                <div class="course-card">
                                        <div class="course-img-wrap">
                        <img src="/uploads/website_courses/course_20260424_204612_0b3f5501.png" alt="Webinar on using GitHub" loading="lazy">
                        <div class="course-img-overlay"></div>
                        <span class="course-badge">MSX-WEB-GIT</span>                    </div>
                                        <div class="course-body">
                        <h3 class="course-title">Webinar on using GitHub</h3>
                                                <div class="course-meta">
                                                        <span><i class="fas fa-clock"></i> 2 to 3 hrs</span>                        </div>
                        <a href="https://msxportal.in/course_details?id=35" class="btn-view-course"><i class="fas fa-eye me-1"></i> View Details</a>
                    </div>
                </div>
            </div>
                        <div class="col-lg-4 col-md-6">
                <div class="course-card">
                                        <div class="course-img-wrap">
                        <img src="/uploads/website_courses/course_20260424_185151_a03204f2.jpg" alt="Excel, Advanced Excel and PowerBI" loading="lazy">
                        <div class="course-img-overlay"></div>
                        <span class="course-badge">MSX-MAP-SEM1</span>                    </div>
                                        <div class="course-body">
                        <h3 class="course-title">Excel, Advanced Excel and PowerBI</h3>
                                                <div class="course-meta">
                                                        <span><i class="fas fa-clock"></i> 1 Month</span>                        </div>
                        <a href="https://msxportal.in/course_details?id=15" class="btn-view-course"><i class="fas fa-eye me-1"></i> View Details</a>
                    </div>
                </div>
            </div>
                        <div class="col-lg-4 col-md-6">
                <div class="course-card">
                                        <div class="course-img-wrap">
                        <img src="/uploads/website_courses/course_20260424_204821_de07cd00.png" alt="Webinar on using LinkedIn" loading="lazy">
                        <div class="course-img-overlay"></div>
                        <span class="course-badge">MSX-WEB-LIN</span>                    </div>
                                        <div class="course-body">
                        <h3 class="course-title">Webinar on using LinkedIn</h3>
                                                <div class="course-meta">
                                                        <span><i class="fas fa-clock"></i> 2 to 3 hrs</span>                        </div>
                        <a href="https://msxportal.in/course_details?id=36" class="btn-view-course"><i class="fas fa-eye me-1"></i> View Details</a>
                    </div>
                </div>
            </div>
                        <div class="col-lg-4 col-md-6">
                <div class="course-card">
                                        <div class="course-img-wrap">
                        <img src="/uploads/website_courses/course_20260424_192521_84bfb3dc.jpg" alt="Excel and Advanced Excel" loading="lazy">
                        <div class="course-img-overlay"></div>
                        <span class="course-badge">MSX-BCW-EXL</span>                    </div>
                                        <div class="course-body">
                        <h3 class="course-title">Excel and Advanced Excel</h3>
                                                <div class="course-meta">
                                                        <span><i class="fas fa-clock"></i> 6 hrs / 2hrs per day for 3 days</span>                        </div>
                        <a href="https://msxportal.in/course_details?id=19" class="btn-view-course"><i class="fas fa-eye me-1"></i> View Details</a>
                    </div>
                </div>
            </div>
                        <div class="col-lg-4 col-md-6">
                <div class="course-card">
                                        <div class="course-img-wrap">
                        <img src="/uploads/website_courses/course_20260424_190544_ceb7c179.jpg" alt="Data Analysis using R language" loading="lazy">
                        <div class="course-img-overlay"></div>
                        <span class="course-badge">MSX-MAP-SEM2</span>                    </div>
                                        <div class="course-body">
                        <h3 class="course-title">Data Analysis using R language</h3>
                                                <div class="course-meta">
                                                        <span><i class="fas fa-clock"></i> 1 Month</span>                        </div>
                        <a href="https://msxportal.in/course_details?id=16" class="btn-view-course"><i class="fas fa-eye me-1"></i> View Details</a>
                    </div>
                </div>
            </div>
                    </div>
                <div class="text-center mt-5 pt-3">
            <a href="https://msxportal.in/courses" class="btn-browse-all"><i class="fas fa-th-large"></i> Browse All Courses <i class="fas fa-arrow-right"></i></a>
        </div>
    </div>
</section>

<!-- ════════════════════════ HOW IT WORKS ════════════════════════ -->
<section class="section section-alt">
    <div class="container">
        <div class="text-center mb-5">
            <span class="sec-tag">Simple Process</span>
            <h2 class="sec-title">Start Learning in <span class="accent">4 Easy Steps</span></h2>
        </div>
        <div class="row g-4 justify-content-center">
            <div class="col-6 col-md-3">
                <div class="how-step">
                    <div class="how-step-num">1</div>
                    <div class="how-step-icon">🔍</div>
                    <div class="how-step-title">Explore Courses</div>
                    <p class="how-step-desc">Browse our industry-curated programs and choose the right track for your goals.</p>
                </div>
            </div>
            <div class="col-6 col-md-3">
                <div class="how-step">
                    <div class="how-step-num">2</div>
                    <div class="how-step-icon">📝</div>
                    <div class="how-step-title">Enroll &amp; Register</div>
                    <p class="how-step-desc">Sign up in minutes and get instant access to your student dashboard and materials.</p>
                </div>
            </div>
            <div class="col-6 col-md-3">
                <div class="how-step">
                    <div class="how-step-num">3</div>
                    <div class="how-step-icon">🎓</div>
                    <div class="how-step-title">Learn &amp; Build</div>
                    <p class="how-step-desc">Attend live classes, complete projects, crack tests and earn your certificate.</p>
                </div>
            </div>
            <div class="col-6 col-md-3">
                <div class="how-step">
                    <div class="how-step-num">4</div>
                    <div class="how-step-icon">🚀</div>
                    <div class="how-step-title">Get Hired</div>
                    <p class="how-step-desc">Connect with our 40+ placement partners and launch your tech career with confidence.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ════════════════════════ TESTIMONIALS ════════════════════════ -->
<section class="testi-section" id="testimonials">
    <div class="container">
        <div class="text-center mb-5">
            <span class="sec-tag">Alumni Stories</span>
            <h2 class="sec-title">What Our <span class="accent">Students Say</span></h2>
            <p class="sec-desc">Real results from real students who transformed their careers with MSX Portal.</p>
        </div>
                <div class="swiper testimonials-swiper pb-4">
            <div class="swiper-wrapper">
                                <div class="swiper-slide p-2">
                    <div class="testi-card">
                        <div class="testi-stars">★★★★★</div>
                        <p class="testi-quote mb-3">"My journey at MindSparXs Computer Training has been truly amazing. I started with very basic knowledge, but today I feel confident in my skills thanks to the excellent teaching and personal attention given by the trainers. The supportive environment and encouragement helped me grow both personally and professionally. I will always be thankful to MindSparXs."</p>
                        <div class="d-flex align-items-center gap-3 mt-auto">
                            <img src="https://ui-avatars.com/api/?name=Ayush+Wankhade&amp;background=6c47ff&amp;color=fff&amp;size=128" alt="Ayush Wankhade" class="testi-avatar">
                            <div>
                                <div class="testi-name">Ayush Wankhade</div>
                                                            </div>
                        </div>
                    </div>
                </div>
                                <div class="swiper-slide p-2">
                    <div class="testi-card">
                        <div class="testi-stars">★★★★★</div>
                        <p class="testi-quote mb-3">"Completing my course at MindSparXs Computer Training has been a turning point in my career. The curriculum is well-structured and industry-oriented, which helped me understand real-world applications. The hands-on training and project work prepared me for job opportunities. Thank you to the entire team for their continuous support and mentorship."</p>
                        <div class="d-flex align-items-center gap-3 mt-auto">
                            <img src="https://ui-avatars.com/api/?name=Parikshit+Choudhary&amp;background=6c47ff&amp;color=fff&amp;size=128" alt="Parikshit Choudhary" class="testi-avatar">
                            <div>
                                <div class="testi-name">Parikshit Choudhary</div>
                                                            </div>
                        </div>
                    </div>
                </div>
                                <div class="swiper-slide p-2">
                    <div class="testi-card">
                        <div class="testi-stars">★★★★★</div>
                        <p class="testi-quote mb-3">"I am grateful to MindSparXs Computer Training for providing me with excellent guidance and practical knowledge. The trainers are highly supportive, and the learning environment is very motivating. This course has significantly improved my technical skills and confidence. I would highly recommend MindSparXs to anyone looking to build a strong foundation in computer technology."</p>
                        <div class="d-flex align-items-center gap-3 mt-auto">
                            <img src="https://ui-avatars.com/api/?name=Dhanshri+Jagtap&amp;background=6c47ff&amp;color=fff&amp;size=128" alt="Dhanshri Jagtap" class="testi-avatar">
                            <div>
                                <div class="testi-name">Dhanshri Jagtap</div>
                                                            </div>
                        </div>
                    </div>
                </div>
                            </div>
            <div class="swiper-pagination mt-4" style="position:relative;bottom:0;"></div>
        </div>
            </div>
</section>

<!-- ════════════════════════ ABOUT ════════════════════════ -->
<section class="section" id="about">
    <div class="container">
        <div class="row align-items-center g-5">
            <div class="col-lg-6">
                <img src="assets/images/about_illustration.png" alt="About MSX Portal" class="img-fluid rounded-4" style="filter:drop-shadow(0 20px 48px rgba(108,71,255,0.2));">
            </div>
            <div class="col-lg-6">
                <span class="sec-tag">About Us</span>
                <h2 class="sec-title">Building <span class="accent">Future-Ready</span><br>Tech Professionals</h2>
                <p class="text-muted mb-4" style="font-size:16px;line-height:1.8;">MSX Portal is Ctronics Infotech's flagship Ed-Tech platform, bridging the gap between college education and industry requirements through practical, mentor-led training.</p>
                <div class="about-check"><div class="about-check-icon"><i class="fas fa-check"></i></div><div class="about-check-text">Real-time attendance &amp; progress tracking</div></div>
                <div class="about-check"><div class="about-check-icon"><i class="fas fa-check"></i></div><div class="about-check-text">Interactive assignments, tests &amp; live coding sessions</div></div>
                <div class="about-check"><div class="about-check-icon"><i class="fas fa-check"></i></div><div class="about-check-text">Live Zoom classes with recorded playback</div></div>
                <div class="about-check"><div class="about-check-icon"><i class="fas fa-check"></i></div><div class="about-check-text">Industry-standard project portfolios</div></div>
                <div class="about-check"><div class="about-check-icon"><i class="fas fa-check"></i></div><div class="about-check-text">Payment management &amp; EMI-friendly fees</div></div>
                <div class="about-check"><div class="about-check-icon"><i class="fas fa-check"></i></div><div class="about-check-text">Downloadable certificates &amp; transcripts</div></div>
                <div class="mt-4 d-flex gap-3 flex-wrap">
                    <a href="courses.php" class="btn-hero-primary" style="background:var(--grad-primary);color:#fff;border:none;padding:13px 32px;border-radius:50px;font-size:15px;font-weight:700;text-decoration:none;display:inline-flex;align-items:center;gap:8px;transition:all 0.3s;box-shadow:0 8px 24px rgba(108,71,255,0.4);"><i class="fas fa-rocket"></i> Start Learning</a>
                    <a href="contact.php" class="btn-hero-outline" style="background:rgba(108,71,255,0.08);color:var(--primary);border:1.5px solid rgba(108,71,255,0.3);padding:13px 32px;border-radius:50px;font-size:15px;font-weight:700;text-decoration:none;display:inline-flex;align-items:center;gap:8px;transition:all 0.3s;"><i class="fas fa-phone"></i> Contact Us</a>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ════════════════════════ CTA BAND ════════════════════════ -->
<section class="cta-band">
    <div class="container">
        <h2>Ready to Transform Your Career?</h2>
        <p>Join 1000+ students who have already launched their tech careers with MSX Portal.</p>
       
    </div>
</section>

<!-- ════════════════════════ FOOTER ════════════════════════ -->
<footer class="footer-pub" id="contact">
    <div class="container">
        <div class="row g-5">
            <div class="col-lg-4 col-md-6">
                <img src="assets/images/dlogo.png" alt="MSX Portal" class="footer-brand-img">
                <p class="footer-about">Empowering careers through industry-ready software training. A platform built by Ctronics Infotech to bridge education and employment.</p>
                <div class="footer-social">
                    <a href="#"><i class="fab fa-facebook-f"></i></a>
                    <a href="#"><i class="fab fa-instagram"></i></a>
                    <a href="#"><i class="fab fa-linkedin-in"></i></a>
                    <a href="#"><i class="fab fa-youtube"></i></a>
                    <a href="#"><i class="fab fa-twitter"></i></a>
                </div>
            </div>
            <div class="col-lg-2 col-md-6 col-6">
                <div class="footer-heading">Quick Links</div>
                <ul class="footer-links">
                    <li><a href="landing.php#home"><i class="fas fa-chevron-right" style="font-size:10px;"></i> Home</a></li>
                    <li><a href="landing.php#features"><i class="fas fa-chevron-right" style="font-size:10px;"></i> Features</a></li>
                    <li><a href="courses.php"><i class="fas fa-chevron-right" style="font-size:10px;"></i> Courses</a></li>
                    <li><a href="internship_programs.php"><i class="fas fa-chevron-right" style="font-size:10px;"></i> Internships</a></li>
                    <li><a href="landing.php#about"><i class="fas fa-chevron-right" style="font-size:10px;"></i> About Us</a></li>
                </ul>
            </div>
            <div class="col-lg-2 col-md-6 col-6">
                <div class="footer-heading">Student</div>
                <ul class="footer-links">
                    <li><a href="student_login.php"><i class="fas fa-chevron-right" style="font-size:10px;"></i> Student Login</a></li>
                  
                    <li><a href="college/login.php"><i class="fas fa-chevron-right" style="font-size:10px;"></i> College Login</a></li>
                    <li><a href="courses.php"><i class="fas fa-chevron-right" style="font-size:10px;"></i> Browse Courses</a></li>
                </ul>
            </div>
            <div class="col-lg-4 col-md-6">
                <div class="footer-heading">Contact Us</div>
                <div class="footer-contact-item">
                    <div class="footer-contact-icon"><i class="fas fa-envelope"></i></div>
                    <div class="footer-contact-text"><a href="mailto:msxofficial2025@gmail.com">msxofficial2025@gmail.com</a></div>
                </div>
                <div class="footer-contact-item">
                    <div class="footer-contact-icon"><i class="fas fa-phone"></i></div>
                    <div class="footer-contact-text">+91 9823540321 &nbsp;|&nbsp; +91 9359653916 &nbsp;|&nbsp; +91 8421298578</div>
                </div>
                <div class="footer-contact-item">
                    <div class="footer-contact-icon"><i class="fas fa-map-marker-alt"></i></div>
                    <div class="footer-contact-text">Ctronics Infotech Pvt. Ltd., Swanand, Ganesh Colony, Amravati 444605, MH, India</div>
                </div>
            </div>
        </div>
        <div class="footer-bottom d-flex flex-wrap justify-content-between align-items-center gap-3">
            <p class="mb-0" style="font-size:13px;color:rgba(255,255,255,0.4);">&copy; 2025 MSX Portal. All rights reserved. An initiative of <a href="https://ctronicsinfotech.in" target="_blank" style="color:#a78bfa;text-decoration:none;font-weight:600;">Ctronics Infotech</a>.</p>
            <p class="mb-0" style="font-size:13px;color:rgba(255,255,255,0.3);">Designed with ❤️ for Future Tech Leaders</p>
        </div>
    </div>
</footer>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
<script>
// Testimonials Swiper
if(document.querySelector('.testimonials-swiper')) {
    new Swiper('.testimonials-swiper', {
        slidesPerView:1, spaceBetween:20, loop:true,
        autoplay:{ delay:3500, disableOnInteraction:false },
        pagination:{ el:'.swiper-pagination', clickable:true },
        breakpoints:{ 768:{ slidesPerView:2 }, 1024:{ slidesPerView:3 } }
    });
}

// Smooth Scroll
document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
        const t = document.querySelector(a.getAttribute('href'));
        if(t){ e.preventDefault(); t.scrollIntoView({ behavior:'smooth', block:'start' }); }
    });
});

// Navbar scroll effect
window.addEventListener('scroll', () => {
    const nb = document.querySelector('.navbar');
    if(nb) {
        if (window.scrollY > 60) {
            nb.classList.add('scrolled');
        } else {
            nb.classList.remove('scrolled');
        }
    }
});

// Counter animation
function countUp(el) {
    const target = parseInt(el.dataset.target || el.innerText);
    const suffix = el.dataset.suffix || '';
    let count = 0;
    const step = Math.max(1, Math.ceil(target / 70));
    const t = setInterval(() => {
        count = Math.min(count + step, target);
        el.innerText = count.toLocaleString() + suffix;
        if(count >= target) clearInterval(t);
    }, 18);
}

const obs = new IntersectionObserver(entries => {
    entries.forEach(e => {
        if(e.isIntersecting && !e.target.classList.contains('counted')) {
            e.target.classList.add('counted');
            countUp(e.target);
        }
    });
}, { threshold: 0.5 });

document.querySelectorAll('.stat-number').forEach(el => {
    el.dataset.target = el.innerText.replace(/[^0-9]/g,'');
    el.dataset.suffix = el.innerText.replace(/[0-9,]/g,'');
    el.innerText = '0' + el.dataset.suffix;
    obs.observe(el);
});

// Course card entrance animation
const cardObs = new IntersectionObserver(entries => {
    entries.forEach((e, i) => {
        if(e.isIntersecting) {
            setTimeout(() => { e.target.style.opacity='1'; e.target.style.transform='translateY(0)'; }, i * 80);
            cardObs.unobserve(e.target);
        }
    });
}, { threshold: 0.1 });

document.querySelectorAll('.course-card').forEach(c => {
    c.style.opacity='0'; c.style.transform='translateY(36px)';
    c.style.transition='opacity 0.5s ease, transform 0.5s ease';
    cardObs.observe(c);
});

// Feature card entrance animation
const featObs = new IntersectionObserver(entries => {
    entries.forEach((e, i) => {
        if(e.isIntersecting) {
            setTimeout(() => { e.target.style.opacity='1'; e.target.style.transform='translateY(0)'; }, i * 70);
            featObs.unobserve(e.target);
        }
    });
}, { threshold: 0.1 });

document.querySelectorAll('.feat-card, .how-step, .testi-card').forEach(c => {
    c.style.opacity='0'; c.style.transform='translateY(28px)';
    c.style.transition='opacity 0.5s ease, transform 0.5s ease';
    featObs.observe(c);
});
</script>

</body>
</html>
