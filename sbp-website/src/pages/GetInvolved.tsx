import { useState } from "react";
import {
  Heart,
  HandHeart,
  Building2,
  Users,
  Handshake,
  CheckCircle2,
  ShieldCheck,
  FileText,
  BadgeCheck,
  Sparkles,
} from "lucide-react";
import Section from "../components/Section";
import Reveal from "../components/Reveal";
import { waysToHelp, site } from "../data/site";

const iconMap = { HandHeart, Building2, Users, Handshake };

const amounts = [500, 1000, 2500, 5000, 10000];

export default function GetInvolved() {
  const [amount, setAmount] = useState<number>(2500);
  const [custom, setCustom] = useState<string>("");
  const [frequency, setFrequency] = useState<"once" | "monthly">("monthly");

  const displayAmount = custom && Number(custom) > 0 ? Number(custom) : amount;

  return (
    <>
      <section className="relative overflow-hidden py-16 md:py-24">
        <div aria-hidden className="blob absolute -top-10 left-10 h-80 w-80 bg-ochre-200" />
        <div aria-hidden className="blob absolute -top-20 right-0 h-80 w-80 bg-teal-200" />
        <div className="container-xl relative">
          <Reveal>
            <span className="inline-flex items-center gap-2 rounded-full border border-teal-200 bg-white/70 px-3.5 py-1.5 text-[11px] font-semibold uppercase tracking-[0.14em] text-teal-700 backdrop-blur">
              <Sparkles className="h-3 w-3" />
              Stand with our children
            </span>
          </Reveal>
          <Reveal delay={0.05}>
            <h1 className="mt-5 max-w-4xl font-display text-[40px] leading-[1.05] tracking-tight text-ink-900 md:text-[68px]">
              Your kindness is how we{" "}
              <span className="gradient-text italic">keep the lights on</span>.
            </h1>
          </Reveal>
          <Reveal delay={0.12}>
            <p className="mt-6 max-w-2xl text-lg leading-relaxed text-ink-600">
              SBP is a not‑for‑profit trust and every child in our care depends
              on the generosity of people like you. Here's how you can stand
              with us.
            </p>
          </Reveal>
        </div>
      </section>

      {/* WAYS TO HELP */}
      <Section
        eyebrow="Ways to help"
        title="Give what you can, how you can."
      >
        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4">
          {waysToHelp.map((w, i) => {
            const Icon = iconMap[w.icon as keyof typeof iconMap] ?? HandHeart;
            return (
              <Reveal key={w.title} delay={i * 0.06}>
                <div className="group h-full rounded-[1.5rem] border border-ink-900/5 bg-white p-7 transition hover:-translate-y-1 hover:border-teal-200 hover:shadow-card">
                  <span className="inline-flex h-12 w-12 items-center justify-center rounded-2xl bg-ochre-100 text-ochre-700 transition group-hover:bg-ochre-400 group-hover:text-white">
                    <Icon className="h-6 w-6" />
                  </span>
                  <h3 className="mt-5 font-display text-xl text-ink-900">
                    {w.title}
                  </h3>
                  <p className="mt-2 text-[15px] leading-relaxed text-ink-600">
                    {w.body}
                  </p>
                  <a
                    href="#donate"
                    className="mt-5 inline-flex text-sm font-semibold text-teal-700 hover:underline"
                  >
                    {w.cta} →
                  </a>
                </div>
              </Reveal>
            );
          })}
        </div>
      </Section>

      {/* DONATE */}
      <Section
        id="donate"
        eyebrow="Donate"
        title={
          <>
            Give once, or walk with us{" "}
            <span className="italic text-teal-700">every month.</span>
          </>
        }
        subtitle="Every rupee goes directly to educational materials, therapy, meals and a caring teacher for one of our children."
      >
        <div className="grid gap-6 lg:grid-cols-[1.2fr_1fr]">
          <Reveal>
            <form
              onSubmit={(e) => e.preventDefault()}
              className="rounded-[1.75rem] border border-ink-900/5 bg-white p-8 shadow-card"
              aria-label="Donation form"
            >
              <fieldset>
                <legend className="text-[11px] font-semibold uppercase tracking-[0.14em] text-ink-500">
                  Frequency
                </legend>
                <div className="mt-3 grid grid-cols-2 gap-2 rounded-full bg-cream-100 p-1">
                  {(["monthly", "once"] as const).map((f) => (
                    <button
                      key={f}
                      type="button"
                      onClick={() => setFrequency(f)}
                      className={`rounded-full px-4 py-2 text-sm font-semibold transition ${
                        frequency === f
                          ? "bg-white text-ink-900 shadow-sm"
                          : "text-ink-500"
                      }`}
                    >
                      {f === "monthly" ? "Monthly" : "One time"}
                    </button>
                  ))}
                </div>
              </fieldset>

              <fieldset className="mt-7">
                <legend className="text-[11px] font-semibold uppercase tracking-[0.14em] text-ink-500">
                  Choose an amount (INR)
                </legend>
                <div className="mt-3 grid grid-cols-2 gap-2 sm:grid-cols-5">
                  {amounts.map((a) => (
                    <button
                      key={a}
                      type="button"
                      onClick={() => {
                        setAmount(a);
                        setCustom("");
                      }}
                      className={`rounded-xl border px-4 py-3 text-sm font-semibold transition ${
                        amount === a && !custom
                          ? "border-teal-500 bg-teal-50 text-teal-800"
                          : "border-ink-900/10 text-ink-700 hover:border-teal-300"
                      }`}
                    >
                      ₹{a.toLocaleString("en-IN")}
                    </button>
                  ))}
                </div>
                <label className="mt-3 block">
                  <span className="sr-only">Custom amount</span>
                  <input
                    type="number"
                    inputMode="numeric"
                    min={100}
                    placeholder="Or enter your own amount"
                    value={custom}
                    onChange={(e) => setCustom(e.target.value)}
                    className="w-full rounded-xl border border-ink-900/10 bg-cream-50 px-4 py-3 text-[15px] text-ink-900 placeholder:text-ink-300 focus:border-teal-400 focus:outline-none"
                  />
                </label>
              </fieldset>

              <fieldset className="mt-6 grid gap-4 sm:grid-cols-2">
                <label className="block">
                  <span className="text-[11px] font-semibold uppercase tracking-[0.14em] text-ink-500">
                    Your name
                  </span>
                  <input
                    type="text"
                    required
                    className="mt-1 w-full rounded-xl border border-ink-900/10 bg-cream-50 px-4 py-3 text-[15px] text-ink-900 focus:border-teal-400 focus:outline-none"
                  />
                </label>
                <label className="block">
                  <span className="text-[11px] font-semibold uppercase tracking-[0.14em] text-ink-500">
                    Email
                  </span>
                  <input
                    type="email"
                    required
                    className="mt-1 w-full rounded-xl border border-ink-900/10 bg-cream-50 px-4 py-3 text-[15px] text-ink-900 focus:border-teal-400 focus:outline-none"
                  />
                </label>
                <label className="block sm:col-span-2">
                  <span className="text-[11px] font-semibold uppercase tracking-[0.14em] text-ink-500">
                    PAN (for 80G receipt)
                  </span>
                  <input
                    type="text"
                    className="mt-1 w-full rounded-xl border border-ink-900/10 bg-cream-50 px-4 py-3 text-[15px] uppercase text-ink-900 focus:border-teal-400 focus:outline-none"
                    maxLength={10}
                  />
                </label>
              </fieldset>

              <button
                type="submit"
                className="mt-7 inline-flex w-full items-center justify-center gap-2 rounded-full bg-ink-900 px-6 py-4 text-sm font-semibold text-cream-50 shadow-[0_20px_40px_-18px_rgba(11,29,34,0.55)] transition hover:bg-teal-700"
              >
                <Heart className="h-4 w-4 fill-rose-accent text-rose-accent" />
                Donate ₹{displayAmount.toLocaleString("en-IN")}
                {frequency === "monthly" ? " / month" : ""}
              </button>

              <p className="mt-4 flex items-center justify-center gap-1.5 text-xs text-ink-500">
                <ShieldCheck className="h-3.5 w-3.5 text-teal-600" />
                Secure payment · SSL encrypted · Receipt emailed instantly
              </p>
            </form>
          </Reveal>

          <Reveal delay={0.1}>
            <aside className="flex flex-col gap-4">
              <div className="rounded-[1.5rem] bg-ink-900 p-7 text-cream-100">
                <h3 className="font-display text-2xl text-cream-50">
                  Where your gift goes
                </h3>
                <ul className="mt-5 space-y-3 text-[15px]">
                  {[
                    "₹500 — art & craft supplies for a classroom for a week",
                    "₹1,000 — a month of nutritious mid‑day meals for a child",
                    "₹2,500 — sponsors one child's fees for a full month",
                    "₹10,000 — one vocational starter kit for a young adult",
                  ].map((line) => (
                    <li key={line} className="flex items-start gap-2">
                      <CheckCircle2 className="mt-0.5 h-4 w-4 shrink-0 text-ochre-300" />
                      <span className="text-cream-100/85">{line}</span>
                    </li>
                  ))}
                </ul>
              </div>

              <div className="rounded-[1.5rem] border border-teal-200 bg-teal-50 p-6">
                <div className="flex items-center gap-2 text-teal-800">
                  <BadgeCheck className="h-5 w-5" />
                  <span className="text-[11px] font-semibold uppercase tracking-wider">
                    80G Tax exemption
                  </span>
                </div>
                <p className="mt-2 text-[14px] leading-relaxed text-teal-900/80">
                  SBP is a registered public charitable trust. All donations
                  are eligible for tax exemption under Section 80G of the
                  Income Tax Act. A receipt will be emailed to you instantly.
                </p>
              </div>

              <div className="rounded-[1.5rem] border border-ink-900/5 bg-white p-6">
                <div className="flex items-center gap-2 text-ink-700">
                  <FileText className="h-5 w-5" />
                  <span className="text-[11px] font-semibold uppercase tracking-wider">
                    Direct bank transfer
                  </span>
                </div>
                <p className="mt-2 text-[14px] leading-relaxed text-ink-600">
                  Prefer to transfer directly? Write to us at{" "}
                  <a
                    href={`mailto:${site.contact.donationEmail}`}
                    className="font-semibold text-teal-700 hover:underline"
                  >
                    {site.contact.donationEmail}
                  </a>{" "}
                  and we'll share our account details.
                </p>
              </div>
            </aside>
          </Reveal>
        </div>
      </Section>
    </>
  );
}
