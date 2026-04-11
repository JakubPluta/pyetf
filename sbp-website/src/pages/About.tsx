import { Link } from "react-router-dom";
import { ArrowRight, CheckCircle2 } from "lucide-react";
import Section from "../components/Section";
import Reveal from "../components/Reveal";
import IllustrationCard from "../components/IllustrationCard";
import CtaBand from "../components/CtaBand";
import { site, milestones, impactStats } from "../data/site";

export default function About() {
  return (
    <>
      <section className="relative overflow-hidden py-16 md:py-24">
        <div aria-hidden className="blob absolute -top-10 left-10 h-72 w-72 bg-teal-200" />
        <div aria-hidden className="blob absolute -top-20 right-10 h-72 w-72 bg-ochre-200" />
        <div className="container-xl relative">
          <Reveal>
            <span className="inline-flex items-center gap-2 rounded-full border border-teal-200 bg-white/70 px-3.5 py-1.5 text-[11px] font-semibold uppercase tracking-[0.14em] text-teal-700 backdrop-blur">
              About SBP
            </span>
          </Reveal>
          <Reveal delay={0.05}>
            <h1 className="mt-5 max-w-4xl font-display text-[40px] leading-[1.05] tracking-tight text-ink-900 md:text-[68px]">
              Three decades of believing every child{" "}
              <span className="gradient-text italic">belongs</span>.
            </h1>
          </Reveal>
          <Reveal delay={0.12}>
            <p className="mt-6 max-w-2xl text-lg leading-relaxed text-ink-600">
              {site.description}
            </p>
          </Reveal>
        </div>
      </section>

      {/* MISSION + VISION */}
      <Section className="pt-0 md:pt-0">
        <div className="grid gap-6 lg:grid-cols-2">
          <Reveal>
            <div className="h-full rounded-[1.75rem] border border-ink-900/5 bg-white p-10 shadow-card">
              <span className="text-[11px] font-semibold uppercase tracking-[0.14em] text-teal-700">
                Our mission
              </span>
              <h2 className="mt-3 font-display text-3xl text-ink-900 md:text-4xl">
                Independence, dignity, joy.
              </h2>
              <p className="mt-5 text-[17px] leading-relaxed text-ink-600">
                {site.mission}
              </p>
            </div>
          </Reveal>
          <Reveal delay={0.08}>
            <div className="h-full rounded-[1.75rem] bg-ink-900 p-10 text-cream-100 shadow-card">
              <span className="text-[11px] font-semibold uppercase tracking-[0.14em] text-ochre-300">
                Our vision
              </span>
              <h2 className="mt-3 font-display text-3xl text-cream-50 md:text-4xl">
                A world that makes room.
              </h2>
              <p className="mt-5 text-[17px] leading-relaxed text-cream-100/85">
                {site.vision}
              </p>
            </div>
          </Reveal>
        </div>
      </Section>

      {/* STATS */}
      <Section className="pt-0 md:pt-0">
        <div className="rounded-[2rem] border border-ink-900/5 bg-gradient-to-br from-cream-50 to-white p-8 md:p-14">
          <div className="grid gap-8 md:grid-cols-2 lg:grid-cols-4">
            {impactStats.map((s, i) => (
              <Reveal key={s.label} delay={i * 0.06}>
                <div>
                  <p className="font-display text-5xl font-semibold text-ink-900 md:text-6xl">
                    {s.value}
                  </p>
                  <p className="mt-2 whitespace-pre-line text-sm font-semibold uppercase tracking-wider text-ink-600">
                    {s.label}
                  </p>
                  <p className="mt-1 text-sm text-ink-500">{s.sub}</p>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </Section>

      {/* TIMELINE */}
      <Section
        eyebrow="Our journey"
        title={
          <>
            Milestones that made us{" "}
            <span className="italic text-teal-700">who we are.</span>
          </>
        }
      >
        <div className="relative grid gap-6 lg:grid-cols-[1fr_1.1fr]">
          <Reveal>
            <IllustrationCard
              variant="music"
              label="Music class at SBP"
              className="aspect-square shadow-[0_30px_80px_-30px_rgba(11,29,34,0.3)] lg:sticky lg:top-28"
            />
          </Reveal>
          <ol className="relative space-y-6 border-l-2 border-dashed border-teal-300 pl-8">
            {milestones.map((m, i) => (
              <Reveal key={m.year} delay={i * 0.06}>
                <li className="relative">
                  <span className="absolute -left-[2.4rem] top-2 inline-flex h-6 w-6 items-center justify-center rounded-full bg-teal-500 text-[10px] font-semibold text-white shadow-[0_0_0_4px_rgba(20,167,162,0.2)]">
                    {i + 1}
                  </span>
                  <div className="rounded-[1.25rem] border border-ink-900/5 bg-white p-6 shadow-[0_10px_30px_-20px_rgba(11,29,34,0.2)]">
                    <p className="text-[11px] font-semibold uppercase tracking-[0.14em] text-ochre-600">
                      {m.year}
                    </p>
                    <h3 className="mt-2 font-display text-xl text-ink-900">
                      {m.title}
                    </h3>
                    <p className="mt-2 text-[15px] leading-relaxed text-ink-600">
                      {m.body}
                    </p>
                  </div>
                </li>
              </Reveal>
            ))}
          </ol>
        </div>
      </Section>

      {/* APPROACH */}
      <Section
        eyebrow="How we teach"
        title={
          <>
            Eight levels.{" "}
            <span className="italic text-teal-700">One child at a time.</span>
          </>
        }
        subtitle="Every child at SBP has an Individualised Education Plan (IEP) built around their current ability and their next possibility. We review the plan with parents twice a year and update it as the child grows."
      >
        <div className="grid gap-6 md:grid-cols-2">
          {[
            {
              title: "Assessment & listening",
              body:
                "Before we teach, we observe. Our therapists and teachers spend time with every new child to understand how they learn, what they love, and what makes them feel safe.",
            },
            {
              title: "Individualised learning plan",
              body:
                "We write a plan that reflects the child — not the other way round. Reading, writing, motor skills, social skills, therapy, art and play are woven together.",
            },
            {
              title: "Practical life skills",
              body:
                "From tying shoelaces to taking the bus, our curriculum teaches skills that turn into independence — the kind that shows up at home, at work, in life.",
            },
            {
              title: "Family partnership",
              body:
                "Parents are our co‑teachers. Regular counselling, home visits and open days make sure what we teach at school continues at home.",
            },
          ].map((b, i) => (
            <Reveal key={b.title} delay={i * 0.06}>
              <div className="flex gap-4 rounded-[1.25rem] border border-ink-900/5 bg-white p-6">
                <CheckCircle2 className="mt-1 h-6 w-6 shrink-0 text-teal-600" />
                <div>
                  <h3 className="font-display text-xl text-ink-900">{b.title}</h3>
                  <p className="mt-2 text-[15px] leading-relaxed text-ink-600">
                    {b.body}
                  </p>
                </div>
              </div>
            </Reveal>
          ))}
        </div>
        <div className="mt-10">
          <Link
            to="/programs"
            className="inline-flex items-center gap-1 text-sm font-semibold text-teal-700 hover:gap-2"
          >
            See our programs in detail <ArrowRight className="h-4 w-4" />
          </Link>
        </div>
      </Section>

      <CtaBand />
    </>
  );
}
