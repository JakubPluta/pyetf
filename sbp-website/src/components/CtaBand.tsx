import { Link } from "react-router-dom";
import { ArrowRight, Heart } from "lucide-react";

export default function CtaBand() {
  return (
    <section className="relative py-20 md:py-28">
      <div className="container-xl">
        <div className="relative overflow-hidden rounded-[2rem] bg-ink-900 p-10 text-cream-50 md:p-16">
          <div
            aria-hidden
            className="blob absolute -left-16 -top-16 h-80 w-80 bg-teal-500"
          />
          <div
            aria-hidden
            className="blob absolute -bottom-20 -right-10 h-96 w-96 bg-ochre-500"
          />
          <div
            aria-hidden
            className="absolute inset-0 bg-[radial-gradient(circle_at_20%_20%,rgba(20,167,162,0.15),transparent_50%),radial-gradient(circle_at_80%_80%,rgba(255,189,74,0.12),transparent_55%)]"
          />
          <div className="relative grid items-center gap-8 md:grid-cols-[1.3fr_auto]">
            <div>
              <span className="inline-flex items-center gap-2 rounded-full border border-cream-50/20 bg-white/5 px-3.5 py-1.5 text-[11px] font-semibold uppercase tracking-[0.14em] text-ochre-300">
                <Heart className="h-3 w-3 fill-rose-accent text-rose-accent" />
                Join the family
              </span>
              <h3 className="mt-5 font-display text-3xl leading-tight md:text-5xl">
                A small gift can <span className="italic text-ochre-300">change everything</span> <br className="hidden md:block" />
                for a child like ours.
              </h3>
              <p className="mt-5 max-w-xl text-cream-100/80 md:text-lg">
                ₹2,500 a month sends one child to school with a full stomach,
                therapy, art, music, and teachers who believe in them.
              </p>
            </div>
            <div className="flex flex-wrap gap-3">
              <Link
                to="/get-involved#donate"
                className="group inline-flex items-center gap-2 rounded-full bg-ochre-400 px-6 py-3.5 text-sm font-semibold text-ink-900 shadow-[0_20px_40px_-18px_rgba(255,160,29,0.8)] transition hover:bg-ochre-300"
              >
                Donate now
                <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-1" />
              </Link>
              <Link
                to="/get-involved"
                className="inline-flex items-center gap-2 rounded-full border border-cream-50/30 px-6 py-3.5 text-sm font-semibold text-cream-50 transition hover:bg-white/10"
              >
                Other ways to help
              </Link>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
