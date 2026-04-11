import { useState } from "react";
import { MapPin, Phone, Mail, Clock, Send, ArrowUpRight } from "lucide-react";
import Section from "../components/Section";
import Reveal from "../components/Reveal";
import { site, faq } from "../data/site";

export default function Contact() {
  const [sent, setSent] = useState(false);
  const [openFaq, setOpenFaq] = useState<number | null>(0);

  return (
    <>
      <section className="relative overflow-hidden py-16 md:py-24">
        <div aria-hidden className="blob absolute -top-10 left-0 h-72 w-72 bg-teal-200" />
        <div aria-hidden className="blob absolute -top-20 right-10 h-72 w-72 bg-ochre-200" />
        <div className="container-xl relative">
          <Reveal>
            <span className="inline-flex items-center gap-2 rounded-full border border-teal-200 bg-white/70 px-3.5 py-1.5 text-[11px] font-semibold uppercase tracking-[0.14em] text-teal-700 backdrop-blur">
              Let's talk
            </span>
          </Reveal>
          <Reveal delay={0.05}>
            <h1 className="mt-5 max-w-4xl font-display text-[40px] leading-[1.05] tracking-tight text-ink-900 md:text-[64px]">
              Our gates are{" "}
              <span className="gradient-text italic">always open</span>.
            </h1>
          </Reveal>
          <Reveal delay={0.12}>
            <p className="mt-6 max-w-2xl text-lg leading-relaxed text-ink-600">
              Whether you're a parent looking for admission, a volunteer, a
              partner or simply a kind soul wanting to say hello — we would
              love to hear from you.
            </p>
          </Reveal>
        </div>
      </section>

      {/* CONTACT GRID */}
      <Section className="pt-0 md:pt-0">
        <div className="grid gap-6 lg:grid-cols-[1.1fr_1fr]">
          <Reveal>
            <form
              onSubmit={(e) => {
                e.preventDefault();
                setSent(true);
              }}
              className="rounded-[1.75rem] border border-ink-900/5 bg-white p-8 shadow-card"
              aria-label="Contact form"
            >
              <h2 className="font-display text-2xl text-ink-900">Write to us</h2>
              <p className="mt-1 text-[14px] text-ink-500">
                We try to reply within two working days.
              </p>

              <div className="mt-6 grid gap-4 sm:grid-cols-2">
                <label className="block">
                  <span className="text-[11px] font-semibold uppercase tracking-[0.14em] text-ink-500">
                    Full name
                  </span>
                  <input
                    required
                    type="text"
                    className="mt-1 w-full rounded-xl border border-ink-900/10 bg-cream-50 px-4 py-3 text-[15px] text-ink-900 focus:border-teal-400 focus:outline-none"
                  />
                </label>
                <label className="block">
                  <span className="text-[11px] font-semibold uppercase tracking-[0.14em] text-ink-500">
                    Phone
                  </span>
                  <input
                    type="tel"
                    className="mt-1 w-full rounded-xl border border-ink-900/10 bg-cream-50 px-4 py-3 text-[15px] text-ink-900 focus:border-teal-400 focus:outline-none"
                  />
                </label>
                <label className="block sm:col-span-2">
                  <span className="text-[11px] font-semibold uppercase tracking-[0.14em] text-ink-500">
                    Email
                  </span>
                  <input
                    required
                    type="email"
                    className="mt-1 w-full rounded-xl border border-ink-900/10 bg-cream-50 px-4 py-3 text-[15px] text-ink-900 focus:border-teal-400 focus:outline-none"
                  />
                </label>
                <label className="block sm:col-span-2">
                  <span className="text-[11px] font-semibold uppercase tracking-[0.14em] text-ink-500">
                    I'd like to talk about
                  </span>
                  <select className="mt-1 w-full rounded-xl border border-ink-900/10 bg-cream-50 px-4 py-3 text-[15px] text-ink-900 focus:border-teal-400 focus:outline-none">
                    <option>Admission enquiry</option>
                    <option>Volunteering</option>
                    <option>Donation / CSR partnership</option>
                    <option>A message of support</option>
                    <option>Something else</option>
                  </select>
                </label>
                <label className="block sm:col-span-2">
                  <span className="text-[11px] font-semibold uppercase tracking-[0.14em] text-ink-500">
                    Message
                  </span>
                  <textarea
                    required
                    rows={5}
                    className="mt-1 w-full resize-none rounded-xl border border-ink-900/10 bg-cream-50 px-4 py-3 text-[15px] text-ink-900 focus:border-teal-400 focus:outline-none"
                  />
                </label>
              </div>

              <button
                type="submit"
                className="mt-6 inline-flex items-center gap-2 rounded-full bg-ink-900 px-6 py-3.5 text-sm font-semibold text-cream-50 shadow-[0_18px_40px_-18px_rgba(11,29,34,0.55)] transition hover:bg-teal-700"
              >
                <Send className="h-4 w-4" /> Send message
              </button>

              {sent && (
                <p className="mt-4 rounded-xl bg-teal-50 px-4 py-3 text-[14px] text-teal-800">
                  Thank you. We've received your note and will get back to you
                  soon.
                </p>
              )}
            </form>
          </Reveal>

          <Reveal delay={0.1}>
            <div className="flex h-full flex-col gap-4">
              <div className="rounded-[1.5rem] border border-ink-900/5 bg-white p-6">
                <h3 className="font-display text-xl text-ink-900">Visit us</h3>
                <ul className="mt-4 space-y-4 text-[15px] text-ink-700">
                  <li className="flex gap-3">
                    <MapPin className="mt-1 h-5 w-5 shrink-0 text-teal-600" />
                    <span>
                      {site.address.line1}
                      <br />
                      {site.address.line2} — {site.address.pin}
                      <br />
                      {site.address.state}
                    </span>
                  </li>
                  <li className="flex gap-3">
                    <Phone className="mt-1 h-5 w-5 shrink-0 text-teal-600" />
                    <a href={`tel:${site.contact.phone}`} className="hover:text-teal-700">
                      {site.contact.phone}
                    </a>
                  </li>
                  <li className="flex gap-3">
                    <Mail className="mt-1 h-5 w-5 shrink-0 text-teal-600" />
                    <a href={`mailto:${site.contact.email}`} className="hover:text-teal-700">
                      {site.contact.email}
                    </a>
                  </li>
                  <li className="flex gap-3">
                    <Clock className="mt-1 h-5 w-5 shrink-0 text-teal-600" />
                    <span>{site.hours}</span>
                  </li>
                </ul>
                <a
                  href={site.mapsUrl}
                  target="_blank"
                  rel="noreferrer"
                  className="mt-5 inline-flex items-center gap-1 text-sm font-semibold text-teal-700 hover:gap-2"
                >
                  Open in Google Maps <ArrowUpRight className="h-4 w-4" />
                </a>
              </div>

              <div className="overflow-hidden rounded-[1.5rem] border border-ink-900/5 bg-white shadow-card">
                <iframe
                  title="SBP location on Google Maps"
                  src={site.mapsEmbed}
                  width="100%"
                  height="280"
                  style={{ border: 0 }}
                  loading="lazy"
                  referrerPolicy="no-referrer-when-downgrade"
                  allowFullScreen
                />
              </div>
            </div>
          </Reveal>
        </div>
      </Section>

      {/* FAQ */}
      <Section eyebrow="FAQ" title="Questions, answered." align="center">
        <div className="mx-auto max-w-3xl space-y-3">
          {faq.map((item, i) => {
            const open = openFaq === i;
            return (
              <Reveal key={item.q} delay={i * 0.04}>
                <div className="overflow-hidden rounded-2xl border border-ink-900/5 bg-white">
                  <button
                    type="button"
                    aria-expanded={open}
                    onClick={() => setOpenFaq(open ? null : i)}
                    className="flex w-full items-center justify-between gap-4 px-6 py-5 text-left"
                  >
                    <span className="font-display text-[17px] font-semibold text-ink-900">
                      {item.q}
                    </span>
                    <span
                      className={`inline-flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-teal-100 text-teal-700 transition-transform ${open ? "rotate-45" : ""}`}
                    >
                      +
                    </span>
                  </button>
                  <div
                    className={`grid transition-all duration-300 ${open ? "grid-rows-[1fr] opacity-100" : "grid-rows-[0fr] opacity-0"}`}
                  >
                    <div className="overflow-hidden">
                      <p className="px-6 pb-6 text-[15px] leading-relaxed text-ink-600">
                        {item.a}
                      </p>
                    </div>
                  </div>
                </div>
              </Reveal>
            );
          })}
        </div>
      </Section>
    </>
  );
}
