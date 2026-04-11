import { Link } from "react-router-dom";
import {
  ArrowRight,
  GraduationCap,
  Palette,
  Bird,
  CheckCircle2,
  Users,
  Activity,
  BookOpen,
  Paintbrush,
  Music2,
} from "lucide-react";
import Section from "../components/Section";
import Reveal from "../components/Reveal";
import IllustrationCard from "../components/IllustrationCard";
import CtaBand from "../components/CtaBand";
import { programs } from "../data/site";

const iconMap = { GraduationCap, Palette, Bird };

export default function Programs() {
  return (
    <>
      <section className="relative overflow-hidden py-16 md:py-24">
        <div aria-hidden className="blob absolute -top-10 left-0 h-72 w-72 bg-ochre-200" />
        <div aria-hidden className="blob absolute -top-20 right-0 h-72 w-72 bg-teal-200" />
        <div className="container-xl relative">
          <Reveal>
            <span className="inline-flex items-center gap-2 rounded-full border border-teal-200 bg-white/70 px-3.5 py-1.5 text-[11px] font-semibold uppercase tracking-[0.14em] text-teal-700 backdrop-blur">
              What we offer
            </span>
          </Reveal>
          <Reveal delay={0.05}>
            <h1 className="mt-5 max-w-4xl font-display text-[40px] leading-[1.05] tracking-tight text-ink-900 md:text-[64px]">
              Programs{" "}
              <span className="gradient-text italic">built with love</span>{" "}
              — and backed by practice.
            </h1>
          </Reveal>
          <Reveal delay={0.12}>
            <p className="mt-6 max-w-2xl text-lg leading-relaxed text-ink-600">
              From the youngest learners to adults stepping into their first job,
              SBP meets each child where they are and walks with them to where
              they want to go.
            </p>
          </Reveal>
        </div>
      </section>

      {/* PROGRAMS DETAILED */}
      {programs.map((p, idx) => {
        const Icon = iconMap[p.icon as keyof typeof iconMap] ?? GraduationCap;
        const reverse = idx % 2 === 1;
        const accentClass =
          p.accent === "teal"
            ? "text-teal-700"
            : p.accent === "ochre"
              ? "text-ochre-700"
              : "text-[#b44a07]";
        const ring =
          p.accent === "teal"
            ? "ring-teal-200"
            : p.accent === "ochre"
              ? "ring-ochre-200"
              : "ring-[#ffd2cc]";

        return (
          <Section key={p.slug} className="pt-0 md:pt-0">
            <div
              id={p.slug}
              className={`grid items-center gap-12 lg:grid-cols-2 ${reverse ? "lg:[&>*:first-child]:order-2" : ""}`}
            >
              <Reveal>
                <IllustrationCard
                  variant={
                    p.slug === "disha"
                      ? "classroom"
                      : p.slug === "falguni"
                        ? "vocational"
                        : "seabird"
                  }
                  label={p.title}
                  className={`aspect-[5/4] ring-8 ${ring} shadow-[0_40px_80px_-40px_rgba(11,29,34,0.35)]`}
                />
              </Reveal>

              <Reveal delay={0.08}>
                <div>
                  <span
                    className={`inline-flex items-center gap-2 rounded-full bg-white px-3.5 py-1.5 text-[11px] font-semibold uppercase tracking-[0.14em] ${accentClass}`}
                  >
                    <Icon className="h-3.5 w-3.5" />
                    {p.subtitle}
                  </span>
                  <h2 className="mt-4 font-display text-3xl leading-tight text-ink-900 md:text-5xl">
                    {p.title}
                  </h2>
                  <p className="mt-4 text-[17px] leading-relaxed text-ink-600">
                    {p.summary}
                  </p>

                  <dl className="mt-6 grid grid-cols-2 gap-4">
                    <div className="rounded-xl border border-ink-900/5 bg-white px-5 py-4">
                      <dt className="text-[11px] font-semibold uppercase tracking-wider text-ink-500">
                        Ages
                      </dt>
                      <dd className="mt-1 font-display text-xl text-ink-900">
                        {p.ages}
                      </dd>
                    </div>
                    <div className="rounded-xl border border-ink-900/5 bg-white px-5 py-4">
                      <dt className="text-[11px] font-semibold uppercase tracking-wider text-ink-500">
                        Strength
                      </dt>
                      <dd className="mt-1 font-display text-xl text-ink-900">
                        {p.strength}
                      </dd>
                    </div>
                  </dl>

                  <ul className="mt-6 space-y-2.5">
                    {p.highlights.map((h) => (
                      <li key={h} className="flex items-start gap-3 text-[15px] text-ink-700">
                        <CheckCircle2 className="mt-0.5 h-5 w-5 shrink-0 text-teal-600" />
                        {h}
                      </li>
                    ))}
                  </ul>

                  <Link
                    to="/contact"
                    className="mt-7 inline-flex items-center gap-1 text-sm font-semibold text-teal-700 hover:gap-2"
                  >
                    Ask about admission <ArrowRight className="h-4 w-4" />
                  </Link>
                </div>
              </Reveal>
            </div>
          </Section>
        );
      })}

      {/* CURRICULUM PILLARS */}
      <Section
        eyebrow="Every day at SBP"
        title="A curriculum that touches every part of a child."
        subtitle="Our eight‑level individualised curriculum blends academics with therapy, art, sport and community — so every child grows in body, heart and mind."
        align="center"
      >
        <div className="grid gap-5 md:grid-cols-2 lg:grid-cols-3">
          {[
            {
              Icon: BookOpen,
              title: "Academics",
              body: "Reading, writing, numeracy and general knowledge at a pace that suits every learner.",
            },
            {
              Icon: Activity,
              title: "Therapy",
              body: "Speech, occupational and physiotherapy woven into the school day.",
            },
            {
              Icon: Paintbrush,
              title: "Art & crafts",
              body: "Drawing, painting, clay and block printing that builds fine motor skills and pride.",
            },
            {
              Icon: Music2,
              title: "Music & dance",
              body: "Rhythm, movement and song — the quickest way to a child's heart and memory.",
            },
            {
              Icon: Users,
              title: "Life skills",
              body: "Self‑care, cooking, money, travel — the everyday skills that unlock independence.",
            },
            {
              Icon: Activity,
              title: "Sport & play",
              body: "Our students compete in Special Olympics and local tournaments, and come home with medals.",
            },
          ].map((c, i) => (
            <Reveal key={c.title} delay={i * 0.05}>
              <div className="group h-full rounded-[1.25rem] border border-ink-900/5 bg-white/80 p-6 transition hover:-translate-y-0.5 hover:border-teal-200 hover:bg-white">
                <span className="inline-flex h-11 w-11 items-center justify-center rounded-xl bg-teal-100 text-teal-700 transition group-hover:bg-teal-500 group-hover:text-white">
                  <c.Icon className="h-5 w-5" />
                </span>
                <h3 className="mt-4 font-display text-xl text-ink-900">{c.title}</h3>
                <p className="mt-2 text-[15px] leading-relaxed text-ink-600">
                  {c.body}
                </p>
              </div>
            </Reveal>
          ))}
        </div>
      </Section>

      <CtaBand />
    </>
  );
}
