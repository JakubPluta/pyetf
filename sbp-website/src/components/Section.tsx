import type { HTMLAttributes, ReactNode } from "react";

type Props = Omit<HTMLAttributes<HTMLElement>, "title"> & {
  eyebrow?: string;
  title?: ReactNode;
  subtitle?: ReactNode;
  align?: "left" | "center";
  children: ReactNode;
};

export default function Section({
  eyebrow,
  title,
  subtitle,
  align = "left",
  children,
  className = "",
  ...rest
}: Props) {
  return (
    <section className={`relative py-20 md:py-28 ${className}`} {...rest}>
      <div className="container-xl">
        {(eyebrow || title || subtitle) && (
          <header
            className={`mb-12 flex flex-col gap-4 md:mb-16 ${
              align === "center" ? "items-center text-center" : ""
            } max-w-3xl ${align === "center" ? "mx-auto" : ""}`}
          >
            {eyebrow && (
              <span className="inline-flex items-center gap-2 rounded-full border border-teal-200 bg-teal-50 px-3.5 py-1.5 text-[11px] font-semibold uppercase tracking-[0.14em] text-teal-700">
                <span className="h-1.5 w-1.5 rounded-full bg-teal-500" />
                {eyebrow}
              </span>
            )}
            {title && (
              <h2 className="font-display text-3xl leading-[1.1] tracking-tight text-ink-900 md:text-5xl">
                {title}
              </h2>
            )}
            {subtitle && (
              <p className="text-base leading-relaxed text-ink-600 md:text-lg">
                {subtitle}
              </p>
            )}
          </header>
        )}
        {children}
      </div>
    </section>
  );
}
