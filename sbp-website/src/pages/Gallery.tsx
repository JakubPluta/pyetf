import Section from "../components/Section";
import Reveal from "../components/Reveal";
import IllustrationCard from "../components/IllustrationCard";
import CtaBand from "../components/CtaBand";

const items: {
  variant:
    | "classroom"
    | "vocational"
    | "seabird"
    | "portrait"
    | "activity"
    | "crafts"
    | "music"
    | "garden";
  title: string;
  caption: string;
  span?: string;
}[] = [
  {
    variant: "classroom",
    title: "Morning circle",
    caption: "Hellos, songs and the day ahead at Disha.",
    span: "lg:col-span-2 lg:row-span-2",
  },
  {
    variant: "crafts",
    title: "Candle making",
    caption: "Focus, patience and pride — one candle at a time.",
  },
  {
    variant: "music",
    title: "Rhythm class",
    caption: "Tabla, clap‑songs and a whole lot of smiles.",
  },
  {
    variant: "activity",
    title: "Playground",
    caption: "Because every child deserves a wild, happy afternoon.",
    span: "lg:col-span-2",
  },
  {
    variant: "garden",
    title: "Kitchen garden",
    caption: "Learning where food comes from, one tomato at a time.",
  },
  {
    variant: "seabird",
    title: "Morning at Uran",
    caption: "Our sister school by the sea.",
  },
  {
    variant: "portrait",
    title: "A proud moment",
    caption: "Celebrating a birthday with the whole family.",
  },
  {
    variant: "vocational",
    title: "Tailoring studio",
    caption: "Falguni's stitching class — where little stitches hold big dreams.",
    span: "lg:col-span-2",
  },
];

export default function Gallery() {
  return (
    <>
      <section className="relative overflow-hidden py-16 md:py-24">
        <div aria-hidden className="blob absolute -top-10 right-10 h-72 w-72 bg-teal-200" />
        <div aria-hidden className="blob absolute -top-20 left-10 h-72 w-72 bg-ochre-200" />
        <div className="container-xl relative">
          <Reveal>
            <span className="inline-flex items-center gap-2 rounded-full border border-teal-200 bg-white/70 px-3.5 py-1.5 text-[11px] font-semibold uppercase tracking-[0.14em] text-teal-700 backdrop-blur">
              Life at SBP
            </span>
          </Reveal>
          <Reveal delay={0.05}>
            <h1 className="mt-5 max-w-4xl font-display text-[40px] leading-[1.05] tracking-tight text-ink-900 md:text-[64px]">
              Small moments that{" "}
              <span className="gradient-text italic">make a school</span>.
            </h1>
          </Reveal>
          <Reveal delay={0.12}>
            <p className="mt-6 max-w-2xl text-lg leading-relaxed text-ink-600">
              A glimpse of a day at Disha, Falguni and Sea Bird — the learning,
              the laughter, the everyday magic that makes SBP a second home.
            </p>
          </Reveal>
        </div>
      </section>

      <Section className="pt-0 md:pt-0">
        <div className="grid auto-rows-[220px] grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4">
          {items.map((it, i) => (
            <Reveal key={it.title} delay={i * 0.04} className={it.span ?? ""}>
              <figure className="group relative h-full overflow-hidden rounded-[1.5rem] border border-ink-900/5 bg-white shadow-[0_20px_50px_-30px_rgba(11,29,34,0.3)]">
                <IllustrationCard
                  variant={it.variant}
                  label={it.title}
                  className="absolute inset-0 transition-transform duration-700 group-hover:scale-105"
                />
                <figcaption className="absolute inset-x-4 bottom-4 rounded-xl bg-white/90 p-4 backdrop-blur transition-all duration-300 group-hover:translate-y-0">
                  <p className="font-display text-base font-semibold text-ink-900">
                    {it.title}
                  </p>
                  <p className="text-[13px] text-ink-600">{it.caption}</p>
                </figcaption>
              </figure>
            </Reveal>
          ))}
        </div>

        <p className="mt-10 max-w-2xl text-[14px] text-ink-500">
          Note: The images above are illustrative. Real classroom photographs
          will replace these once we have our families' written consent — we
          take the privacy of our children very seriously.
        </p>
      </Section>

      <CtaBand />
    </>
  );
}
