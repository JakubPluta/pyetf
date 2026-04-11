import { Link } from "react-router-dom";
import {
  ArrowRight,
  ArrowUpRight,
  GraduationCap,
  Palette,
  Bird,
  Heart,
  Hammer,
  Users,
  Shield,
  Sparkles,
  Quote,
} from "lucide-react";
import { motion, useReducedMotion } from "framer-motion";
import Section from "../components/Section";
import Reveal from "../components/Reveal";
import IllustrationCard from "../components/IllustrationCard";
import CtaBand from "../components/CtaBand";
import {
  site,
  impactStats,
  programs,
  values,
  testimonials,
  partners,
} from "../data/site";

const iconMap = {
  GraduationCap,
  Palette,
  Bird,
  Heart,
  Hammer,
  Users,
  Shield,
};

export default function Home() {
  const reduceMotion = useReducedMotion();

  return (
    <>
      {/* HERO */}
      <section className="relative overflow-hidden pt-6 pb-16 md:pt-10 md:pb-24">
        <div
          aria-hidden
          className="blob absolute -top-20 -left-20 h-[420px] w-[420px] bg-teal-300"
        />
        <div
          aria-hidden
          className="blob absolute -top-10 right-0 h-[360px] w-[360px] bg-ochre-200"
        />

        <div className="container-xl relative">
          <div className="grid items-center gap-12 lg:grid-cols-[1.15fr_1fr]">
            <div>
              <Reveal>
                <span className="inline-flex items-center gap-2 rounded-full border border-teal-200 bg-white/70 px-3.5 py-1.5 text-[11px] font-semibold uppercase tracking-[0.14em] text-teal-700 backdrop-blur">
                  <Sparkles className="h-3 w-3" />
                  Empowering special children since {site.foundedYear}
                </span>
              </Reveal>

              <Reveal delay={0.05}>
                <h1 className="mt-6 font-display text-[44px] leading-[1.02] tracking-tight text-ink-900 md:text-[72px]">
                  A home where{" "}
                  <span className="gradient-text italic">every child</span>
                  <br className="hidden md:block" /> learns to fly.
                </h1>
              </Reveal>

              <Reveal delay={0.12}>
                <p className="mt-6 max-w-xl text-lg leading-relaxed text-ink-600 md:text-xl">
                  For over three decades, Swami Brahmanand Pratishthan has
                  stood beside families of children with intellectual and
                  developmental disabilities — teaching, training and loving
                  them into their fullest selves.
                </p>
              </Reveal>

              <Reveal delay={0.2}>
                <div className="mt-8 flex flex-wrap items-center gap-3">
                  <Link
                    to="/get-involved#donate"
                    className="group inline-flex items-center gap-2 rounded-full bg-ink-900 px-6 py-3.5 text-sm font-semibold text-cream-50 shadow-[0_18px_40px_-18px_rgba(11,29,34,0.6)] transition hover:bg-teal-700 hover:shadow-[0_24px_50px_-18px_rgba(12,135,131,0.55)]"
                  >
                    <Heart className="h-4 w-4 fill-rose-accent text-rose-accent" />
                    Donate with love
                    <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-1" />
                  </Link>
                  <Link
                    to="/programs"
                    className="inline-flex items-center gap-2 rounded-full border border-ink-900/10 bg-white/70 px-6 py-3.5 text-sm font-semibold text-ink-800 backdrop-blur transition hover:border-teal-400 hover:text-teal-700"
                  >
                    Explore our programs
                    <ArrowUpRight className="h-4 w-4" />
                  </Link>
                </div>
              </Reveal>

              <Reveal delay={0.3}>
                <dl className="mt-12 grid max-w-xl grid-cols-3 gap-6">
                  {impactStats.slice(0, 3).map((s) => (
                    <div
                      key={s.label}
                      className="border-l-2 border-teal-300 pl-4"
                    >
                      <dt className="font-display text-3xl font-semibold text-ink-900 md:text-4xl">
                        {s.value}
                      </dt>
                      <dd className="mt-1 whitespace-pre-line text-[12px] font-medium uppercase tracking-wider text-ink-500">
                        {s.label}
                      </dd>
                    </div>
                  ))}
                </dl>
              </Reveal>
            </div>

            <div className="relative">
              <motion.div
                initial={reduceMotion ? false : { opacity: 0, scale: 0.96 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ duration: 0.8, ease: [0.22, 1, 0.36, 1] }}
                className="relative"
              >
                <IllustrationCard
                  variant="portrait"
                  label="A child smiling in the classroom"
                  className="aspect-[4/5] shadow-[0_40px_80px_-40px_rgba(11,29,34,0.45)]"
                />

                {/* Floating cards */}
                <motion.div
                  initial={reduceMotion ? false : { y: 20, opacity: 0 }}
                  animate={{ y: 0, opacity: 1 }}
                  transition={{ delay: 0.4, duration: 0.6 }}
                  className="absolute -left-6 top-10 hidden rounded-2xl bg-white p-4 shadow-card md:flex md:items-center md:gap-3"
                >
                  <span className="inline-flex h-10 w-10 items-center justify-center rounded-full bg-teal-100 text-teal-700">
                    <Heart className="h-5 w-5 fill-rose-accent text-rose-accent" />
                  </span>
                  <div>
                    <p className="text-[11px] font-semibold uppercase tracking-wider text-ink-500">
                      Since 1990
                    </p>
                    <p className="font-display text-base font-semibold text-ink-900">
                      165+ children &amp; counting
                    </p>
                  </div>
                </motion.div>

                <motion.div
                  initial={reduceMotion ? false : { y: 20, opacity: 0 }}
                  animate={{ y: 0, opacity: 1 }}
                  transition={{ delay: 0.55, duration: 0.6 }}
                  className="absolute -right-4 bottom-10 hidden rounded-2xl bg-white p-4 shadow-card md:flex md:items-center md:gap-3"
                >
                  <span className="inline-flex h-10 w-10 items-center justify-center rounded-full bg-ochre-100 text-ochre-600">
                    <GraduationCap className="h-5 w-5" />
                  </span>
                  <div>
                    <p className="text-[11px] font-semibold uppercase tracking-wider text-ink-500">
                      8‑level curriculum
                    </p>
                    <p className="font-display text-base font-semibold text-ink-900">
                      Built for every child
                    </p>
                  </div>
                </motion.div>

                <div
                  aria-hidden
                  className="animate-pulse-ring absolute right-6 top-6 h-3 w-3 rounded-full bg-teal-500"
                />
              </motion.div>
            </div>
          </div>
        </div>
      </section>

      {/* PARTNER MARQUEE */}
      <div className="border-y border-ink-900/5 bg-white/60 py-6">
        <div className="container-xl">
          <div className="flex items-center gap-8">
            <p className="shrink-0 text-[11px] font-semibold uppercase tracking-[0.16em] text-ink-500">
              Trusted by partners
            </p>
            <div className="relative flex-1 overflow-hidden mask-fade-b">
              <div className="animate-marquee flex gap-14 whitespace-nowrap text-ink-400">
                {[...partners, ...partners].map((p, i) => (
                  <span
                    key={`${p}-${i}`}
                    className="font-display text-xl font-semibold tracking-tight"
                  >
                    {p}
                  </span>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* MISSION */}
      <Section
        eyebrow="Our mission"
        title={
          <>
            Education shaped around{" "}
            <span className="gradient-text italic">each child</span>, not the other way round.
          </>
        }
        subtitle={site.mission}
        align="center"
      >
        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4">
          {values.map((v, i) => {
            const Icon = iconMap[v.icon as keyof typeof iconMap] ?? Heart;
            return (
              <Reveal key={v.title} delay={i * 0.06}>
                <div className="group h-full rounded-[1.5rem] border border-ink-900/5 bg-white/70 p-7 backdrop-blur transition hover:-translate-y-1 hover:border-teal-200 hover:shadow-card">
                  <span className="inline-flex h-12 w-12 items-center justify-center rounded-2xl bg-teal-100 text-teal-700 transition group-hover:bg-teal-500 group-hover:text-white">
                    <Icon className="h-6 w-6" />
                  </span>
                  <h3 className="mt-5 font-display text-xl text-ink-900">
                    {v.title}
                  </h3>
                  <p className="mt-2 text-[15px] leading-relaxed text-ink-600">
                    {v.body}
                  </p>
                </div>
              </Reveal>
            );
          })}
        </div>
      </Section>

      {/* PROGRAMS */}
      <Section
        eyebrow="Our programs"
        title={
          <>
            Three homes, one promise:{" "}
            <span className="italic">dignity for every child</span>.
          </>
        }
        subtitle="From our flagship school in Belapur to the vocational centre next door and our sister campus in Uran, we walk with children from their earliest years into confident adulthood."
      >
        <div className="grid gap-6 lg:grid-cols-3">
          {programs.map((p, i) => {
            const Icon = iconMap[p.icon as keyof typeof iconMap] ?? GraduationCap;
            const accentBg =
              p.accent === "teal"
                ? "from-teal-100 to-teal-300"
                : p.accent === "ochre"
                  ? "from-ochre-100 to-ochre-300"
                  : "from-cream-100 to-[#ffc9c2]";
            const accentText =
              p.accent === "teal"
                ? "text-teal-700"
                : p.accent === "ochre"
                  ? "text-ochre-700"
                  : "text-[#b44a07]";
            return (
              <Reveal key={p.slug} delay={i * 0.08}>
                <article className="group relative flex h-full flex-col overflow-hidden rounded-[1.75rem] border border-ink-900/5 bg-white transition hover:-translate-y-1 hover:shadow-[0_30px_60px_-20px_rgba(11,29,34,0.25)]">
                  <div
                    className={`relative aspect-[16/10] bg-gradient-to-br ${accentBg}`}
                  >
                    <IllustrationCard
                      variant={
                        p.slug === "disha"
                          ? "classroom"
                          : p.slug === "falguni"
                            ? "vocational"
                            : "seabird"
                      }
                      label={p.title}
                      className="absolute inset-0"
                    />
                    <span
                      className={`absolute left-4 top-4 inline-flex items-center gap-1.5 rounded-full bg-white/90 px-3 py-1 text-[11px] font-semibold uppercase tracking-wider backdrop-blur ${accentText}`}
                    >
                      <Icon className="h-3 w-3" /> {p.ages}
                    </span>
                  </div>
                  <div className="flex flex-1 flex-col p-7">
                    <p className="text-[11px] font-semibold uppercase tracking-wider text-ink-500">
                      {p.subtitle}
                    </p>
                    <h3 className="mt-2 font-display text-2xl text-ink-900">
                      {p.title}
                    </h3>
                    <p className="mt-3 flex-1 text-[15px] leading-relaxed text-ink-600">
                      {p.summary}
                    </p>
                    <div className="mt-6 flex items-center justify-between border-t border-ink-900/5 pt-4">
                      <span className="text-[12px] font-semibold text-ink-500">
                        {p.strength}
                      </span>
                      <Link
                        to="/programs"
                        className="inline-flex items-center gap-1 text-sm font-semibold text-teal-700 transition group-hover:gap-2"
                      >
                        Read more <ArrowRight className="h-3.5 w-3.5" />
                      </Link>
                    </div>
                  </div>
                </article>
              </Reveal>
            );
          })}
        </div>
      </Section>

      {/* STORY / QUOTE */}
      <Section className="pt-0 md:pt-0">
        <div className="grid items-center gap-12 lg:grid-cols-[1fr_1.1fr]">
          <Reveal>
            <IllustrationCard
              variant="activity"
              label="Children playing together"
              className="aspect-[5/4] shadow-[0_30px_80px_-30px_rgba(11,29,34,0.3)]"
            />
          </Reveal>
          <Reveal delay={0.1}>
            <span className="inline-flex items-center gap-2 rounded-full border border-teal-200 bg-teal-50 px-3.5 py-1.5 text-[11px] font-semibold uppercase tracking-[0.14em] text-teal-700">
              <span className="h-1.5 w-1.5 rounded-full bg-teal-500" />
              Our story
            </span>
            <h2 className="mt-4 font-display text-3xl leading-[1.1] tracking-tight text-ink-900 md:text-5xl">
              A small room in 1990.
              <br />
              <span className="italic text-teal-700">A movement today.</span>
            </h2>
            <p className="mt-6 text-[17px] leading-relaxed text-ink-600">
              SBP began in 1990 with a handful of children, a room, and a
              founder who believed that every child — no matter how the world
              labelled them — deserved an education built just for them.
              Thirty‑five years later, that belief has grown into two schools,
              a vocational centre, hundreds of alumni and thousands of moments
              of joy.
            </p>
            <Link
              to="/about"
              className="mt-6 inline-flex items-center gap-1 text-sm font-semibold text-teal-700 hover:gap-2"
            >
              Read our full story <ArrowRight className="h-4 w-4" />
            </Link>
          </Reveal>
        </div>
      </Section>

      {/* TESTIMONIALS */}
      <Section
        eyebrow="Voices of our family"
        title="The words of parents, teachers and the children we love."
        align="center"
        className="bg-white/50"
      >
        <div className="grid gap-6 md:grid-cols-3">
          {testimonials.map((t, i) => (
            <Reveal key={t.author} delay={i * 0.08}>
              <figure className="flex h-full flex-col rounded-[1.5rem] border border-ink-900/5 bg-white p-7 shadow-[0_10px_30px_-20px_rgba(11,29,34,0.25)]">
                <Quote className="h-7 w-7 text-ochre-400" />
                <blockquote className="mt-4 flex-1 text-[16px] leading-relaxed text-ink-700">
                  “{t.quote}”
                </blockquote>
                <figcaption className="mt-6 border-t border-ink-900/5 pt-4">
                  <p className="font-display text-base font-semibold text-ink-900">
                    {t.author}
                  </p>
                  <p className="text-[12px] font-medium uppercase tracking-wider text-ink-500">
                    {t.role}
                  </p>
                </figcaption>
              </figure>
            </Reveal>
          ))}
        </div>
      </Section>

      <CtaBand />
    </>
  );
}
