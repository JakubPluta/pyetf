import { Link } from "react-router-dom";
import {
  MapPin,
  Phone,
  Mail,
  Clock,
  Heart,
  ArrowUpRight,
} from "lucide-react";
import Logo from "./Logo";
import { site, navLinks } from "../data/site";

function FacebookIcon(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden {...props}>
      <path d="M13.5 21v-8.2h2.75l.41-3.2H13.5V7.55c0-.92.26-1.55 1.59-1.55h1.7V3.14A22.4 22.4 0 0 0 14.32 3C12 3 10.4 4.42 10.4 7.02V9.6H7.63v3.2h2.77V21h3.1z" />
    </svg>
  );
}
function InstagramIcon(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden {...props}>
      <rect x="3" y="3" width="18" height="18" rx="5" />
      <circle cx="12" cy="12" r="4" />
      <circle cx="17.5" cy="6.5" r="0.8" fill="currentColor" />
    </svg>
  );
}
function LinkedinIcon(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden {...props}>
      <path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9h4v12H3V9zm7 0h3.84v1.64h.05c.53-1 1.84-2.04 3.79-2.04 4.05 0 4.8 2.66 4.8 6.12V21h-4v-5.67c0-1.35-.02-3.1-1.9-3.1-1.9 0-2.19 1.48-2.19 3V21h-4V9z" />
    </svg>
  );
}
function YoutubeIcon(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden {...props}>
      <path d="M23 7.5s-.22-1.56-.9-2.24c-.85-.9-1.81-.9-2.25-.96C16.8 4 12 4 12 4s-4.8 0-7.85.3c-.44.06-1.4.06-2.25.96C1.22 5.94 1 7.5 1 7.5S.78 9.32.78 11.13v1.74C.78 14.68 1 16.5 1 16.5s.22 1.56.9 2.24c.85.9 1.97.87 2.47.97C6.1 20 12 20 12 20s4.8 0 7.85-.3c.44-.07 1.4-.07 2.25-.97.68-.68.9-2.23.9-2.23s.22-1.82.22-3.63v-1.74c0-1.81-.22-3.63-.22-3.63zM9.75 14.5v-5l5 2.5-5 2.5z" />
    </svg>
  );
}

export default function Footer() {
  return (
    <footer className="relative mt-24 overflow-hidden bg-ink-900 text-cream-100">
      <div
        aria-hidden
        className="blob absolute -top-40 -left-20 h-80 w-80 bg-teal-500"
      />
      <div
        aria-hidden
        className="blob absolute -top-20 right-0 h-72 w-72 bg-ochre-500"
      />

      <div className="container-xl relative pt-20 pb-10">
        <div className="grid gap-12 lg:grid-cols-[1.4fr_1fr_1fr_1fr]">
          <div>
            <Logo variant="dark" />
            <p className="mt-5 max-w-sm text-[15px] leading-relaxed text-cream-100/80">
              {site.description}
            </p>
            <Link
              to="/get-involved#donate"
              className="mt-6 inline-flex items-center gap-2 rounded-full bg-ochre-400 px-5 py-3 text-sm font-semibold text-ink-900 transition hover:bg-ochre-300"
            >
              <Heart className="h-4 w-4 fill-rose-accent text-rose-accent" />
              Donate with love
            </Link>
          </div>

          <div>
            <h4 className="text-sm font-semibold uppercase tracking-[0.14em] text-teal-200">
              Explore
            </h4>
            <ul className="mt-4 space-y-2.5 text-[15px]">
              {navLinks.map((l) => (
                <li key={l.to}>
                  <Link
                    to={l.to}
                    className="inline-flex items-center gap-1 text-cream-100/85 transition hover:text-ochre-300"
                  >
                    {l.label}
                    <ArrowUpRight className="h-3.5 w-3.5 opacity-60" />
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          <div>
            <h4 className="text-sm font-semibold uppercase tracking-[0.14em] text-teal-200">
              Visit us
            </h4>
            <ul className="mt-4 space-y-3 text-[15px] text-cream-100/85">
              <li className="flex gap-3">
                <MapPin className="mt-1 h-4 w-4 shrink-0 text-ochre-300" />
                <span>
                  {site.address.line1}
                  <br />
                  {site.address.line2} — {site.address.pin}
                  <br />
                  {site.address.state}
                </span>
              </li>
              <li className="flex gap-3">
                <Clock className="mt-1 h-4 w-4 shrink-0 text-ochre-300" />
                <span>{site.hours}</span>
              </li>
              <li>
                <a
                  href={site.mapsUrl}
                  target="_blank"
                  rel="noreferrer"
                  className="mt-1 inline-flex items-center gap-1 text-ochre-300 hover:underline"
                >
                  View on Google Maps <ArrowUpRight className="h-3.5 w-3.5" />
                </a>
              </li>
            </ul>
          </div>

          <div>
            <h4 className="text-sm font-semibold uppercase tracking-[0.14em] text-teal-200">
              Say hello
            </h4>
            <ul className="mt-4 space-y-3 text-[15px] text-cream-100/85">
              <li className="flex gap-3">
                <Phone className="mt-1 h-4 w-4 shrink-0 text-ochre-300" />
                <a href={`tel:${site.contact.phone}`} className="hover:text-ochre-300">
                  {site.contact.phone}
                </a>
              </li>
              <li className="flex gap-3">
                <Mail className="mt-1 h-4 w-4 shrink-0 text-ochre-300" />
                <a
                  href={`mailto:${site.contact.email}`}
                  className="hover:text-ochre-300"
                >
                  {site.contact.email}
                </a>
              </li>
            </ul>

            <div className="mt-6 flex items-center gap-2">
              {[
                { href: site.social.facebook, Icon: FacebookIcon, label: "Facebook" },
                { href: site.social.instagram, Icon: InstagramIcon, label: "Instagram" },
                { href: site.social.linkedin, Icon: LinkedinIcon, label: "LinkedIn" },
                { href: site.social.youtube, Icon: YoutubeIcon, label: "YouTube" },
              ].map(({ href, Icon, label }) => (
                <a
                  key={label}
                  href={href}
                  target="_blank"
                  rel="noreferrer"
                  aria-label={label}
                  className="inline-flex h-9 w-9 items-center justify-center rounded-full border border-cream-100/15 text-cream-100/80 transition hover:border-ochre-300 hover:text-ochre-300"
                >
                  <Icon className="h-4 w-4" />
                </a>
              ))}
            </div>
          </div>
        </div>

        <div className="mt-14 flex flex-col items-start justify-between gap-4 border-t border-cream-100/10 pt-6 text-[13px] text-cream-100/60 md:flex-row md:items-center">
          <p>
            © {new Date().getFullYear()} {site.name}. {site.legal.registration}.{" "}
            {site.legal.eightyG}.
          </p>
          <p className="flex items-center gap-1.5">
            Crafted with <Heart className="h-3.5 w-3.5 fill-rose-accent text-rose-accent" /> for
            every child who deserves a home.
          </p>
        </div>
      </div>
    </footer>
  );
}
