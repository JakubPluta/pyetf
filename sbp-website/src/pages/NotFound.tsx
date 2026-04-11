import { Link } from "react-router-dom";
import { ArrowLeft, Heart } from "lucide-react";

export default function NotFound() {
  return (
    <section className="relative flex min-h-[70vh] items-center overflow-hidden">
      <div aria-hidden className="blob absolute -top-10 left-0 h-80 w-80 bg-teal-200" />
      <div aria-hidden className="blob absolute bottom-10 right-0 h-80 w-80 bg-ochre-200" />
      <div className="container-xl relative text-center">
        <p className="font-display text-[120px] leading-none text-ink-900 md:text-[200px]">
          <span className="gradient-text italic">404</span>
        </p>
        <h1 className="mt-2 font-display text-3xl text-ink-900 md:text-5xl">
          This page has gone out to play.
        </h1>
        <p className="mx-auto mt-4 max-w-md text-ink-600">
          Let's head back home — there are stories, smiles and a whole school
          waiting for you.
        </p>
        <Link
          to="/"
          className="mt-8 inline-flex items-center gap-2 rounded-full bg-ink-900 px-6 py-3.5 text-sm font-semibold text-cream-50 transition hover:bg-teal-700"
        >
          <ArrowLeft className="h-4 w-4" />
          Back to home
          <Heart className="h-4 w-4 fill-rose-accent text-rose-accent" />
        </Link>
      </div>
    </section>
  );
}
