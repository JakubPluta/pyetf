import { Link } from "react-router-dom";

type Props = {
  variant?: "light" | "dark";
  compact?: boolean;
};

export default function Logo({ variant = "light", compact = false }: Props) {
  const textColor = variant === "dark" ? "text-cream-50" : "text-ink-900";
  const subColor = variant === "dark" ? "text-teal-200" : "text-teal-700";

  return (
    <Link
      to="/"
      aria-label="Swami Brahmanand Pratishthan — Home"
      className="group inline-flex items-center gap-3"
    >
      <span className="relative inline-flex h-11 w-11 items-center justify-center">
        <svg
          viewBox="0 0 64 64"
          className="h-11 w-11 drop-shadow-[0_6px_14px_rgba(12,135,131,0.35)] transition-transform group-hover:scale-105"
        >
          <defs>
            <linearGradient id="lg1" x1="0" x2="1" y1="0" y2="1">
              <stop offset="0" stopColor="#0c8783" />
              <stop offset="1" stopColor="#14a7a2" />
            </linearGradient>
            <linearGradient id="lg2" x1="0" x2="1" y1="0" y2="1">
              <stop offset="0" stopColor="#ffbd4a" />
              <stop offset="1" stopColor="#f58104" />
            </linearGradient>
          </defs>
          <rect width="64" height="64" rx="18" fill="url(#lg1)" />
          <path
            d="M32 12c6 0 11 5 11 11 0 8-11 15-11 24 0-9-11-16-11-24 0-6 5-11 11-11z"
            fill="url(#lg2)"
          />
          <circle cx="32" cy="23" r="3.6" fill="#fdfaf3" />
        </svg>
      </span>
      {!compact && (
        <span className="flex flex-col leading-tight">
          <span
            className={`font-display text-[15px] font-semibold tracking-tight ${textColor}`}
          >
            Swami Brahmanand Pratishthan
          </span>
          <span
            className={`text-[11px] font-medium uppercase tracking-[0.14em] ${subColor}`}
          >
            A home for every child
          </span>
        </span>
      )}
    </Link>
  );
}
