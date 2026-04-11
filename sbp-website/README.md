# Swami Brahmanand Pratishthan — Website

A warm, modern website for **Swami Brahmanand Pratishthan (SBP)**, a
not‑for‑profit trust in Navi Mumbai that has been empowering children and
young adults with intellectual and developmental disabilities since 1990.

> _"A home where every child learns to fly."_

## Tech stack

- **React 19** + **TypeScript** (strict)
- **Vite 8** (fast dev server, Rolldown‑based build)
- **Tailwind CSS 4** (via `@tailwindcss/vite`, custom `@theme` tokens)
- **React Router v7** for routing
- **Framer Motion** for subtle, accessible animations
- **Lucide React** for icons
- Custom SVG illustrations (no photo dependencies for launch)
- WCAG‑minded: focus rings, skip link, prefers‑reduced‑motion, semantic
  landmarks, accessible forms.

## Project structure

```
sbp-website/
├── index.html                # SEO + OG tags
├── public/
│   └── favicon.svg           # Brand mark
└── src/
    ├── App.tsx               # Router
    ├── main.tsx              # Entry
    ├── index.css             # Tailwind v4 theme + utilities
    ├── components/
    │   ├── Layout.tsx
    │   ├── Navbar.tsx
    │   ├── Footer.tsx
    │   ├── Logo.tsx
    │   ├── Section.tsx
    │   ├── Reveal.tsx
    │   ├── CtaBand.tsx
    │   └── IllustrationCard.tsx
    ├── pages/
    │   ├── Home.tsx
    │   ├── About.tsx
    │   ├── Programs.tsx
    │   ├── Gallery.tsx
    │   ├── GetInvolved.tsx
    │   ├── Contact.tsx
    │   └── NotFound.tsx
    └── data/
        └── site.ts           # Centralised content
```

All textual content, contact details, programs and testimonials live in
`src/data/site.ts` — update that file once SBP shares final copy and
real photographs.

## Pages

- `/` — Hero, mission, programs preview, story, voices, CTA
- `/about` — History, mission, vision, timeline, approach
- `/programs` — Disha, Falguni, Sea Bird + curriculum pillars
- `/gallery` — Life at SBP (illustrated until real photos arrive)
- `/get-involved` — Ways to help + donation flow with 80G info
- `/contact` — Contact form, address, map, FAQ

## Scripts

```bash
npm install      # install dependencies
npm run dev      # dev server on http://localhost:5173
npm run build    # type‑check + production build (→ dist/)
npm run preview  # preview production build locally
npm run lint     # ESLint
```

## Before going live

1. Replace the placeholder contact number, email and social links in
   `src/data/site.ts` with SBP's real details.
2. Swap the `IllustrationCard` placeholders in `Home.tsx`, `Programs.tsx`
   and `Gallery.tsx` with real photographs (keep consent in mind).
3. Wire the donation form in `GetInvolved.tsx` to a payment gateway
   (Razorpay, Instamojo, Give India, etc.).
4. Wire the contact form in `Contact.tsx` to an email service
   (Formspree, Resend, Fastmail, …).
5. Replace the embed in `Contact.tsx` with the official Google Maps
   embed URL.

Made with ♥ for every child who deserves a home.
