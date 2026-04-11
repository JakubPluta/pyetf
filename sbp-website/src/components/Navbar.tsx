import { useEffect, useState } from "react";
import { Link, NavLink } from "react-router-dom";
import { Menu, X, Heart } from "lucide-react";
import { AnimatePresence, motion } from "framer-motion";
import Logo from "./Logo";
import { navLinks } from "../data/site";

export default function Navbar() {
  const [open, setOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 12);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  const close = () => setOpen(false);

  return (
    <header
      className={`sticky top-0 z-50 transition-all duration-300 ${
        scrolled ? "py-2" : "py-4"
      }`}
    >
      <div className="container-xl">
        <nav
          className={`flex items-center justify-between rounded-2xl px-4 py-3 transition-all duration-300 ${
            scrolled
              ? "glass shadow-[0_10px_30px_-12px_rgba(11,29,34,0.18)]"
              : "bg-transparent"
          }`}
          aria-label="Main"
        >
          <Logo />

          <ul className="hidden items-center gap-1 lg:flex">
            {navLinks.map((link) => (
              <li key={link.to}>
                <NavLink
                  to={link.to}
                  end={link.to === "/"}
                  className={({ isActive }) =>
                    `relative rounded-full px-4 py-2 text-sm font-medium transition-colors ${
                      isActive
                        ? "text-teal-800"
                        : "text-ink-700 hover:text-teal-700"
                    }`
                  }
                >
                  {({ isActive }) => (
                    <>
                      {link.label}
                      {isActive && (
                        <motion.span
                          layoutId="nav-active"
                          className="absolute inset-0 -z-10 rounded-full bg-teal-100"
                          transition={{ type: "spring", stiffness: 380, damping: 30 }}
                        />
                      )}
                    </>
                  )}
                </NavLink>
              </li>
            ))}
          </ul>

          <div className="flex items-center gap-2">
            <Link
              to="/get-involved#donate"
              className="group hidden items-center gap-2 rounded-full bg-ink-900 px-5 py-2.5 text-sm font-semibold text-cream-50 shadow-[0_8px_24px_-8px_rgba(11,29,34,0.4)] transition-all hover:bg-teal-700 hover:shadow-[0_12px_30px_-10px_rgba(12,135,131,0.5)] md:inline-flex"
            >
              <Heart className="h-4 w-4 fill-rose-accent text-rose-accent transition-transform group-hover:scale-110" />
              Donate
            </Link>
            <button
              type="button"
              aria-label={open ? "Close menu" : "Open menu"}
              aria-expanded={open}
              className="inline-flex h-11 w-11 items-center justify-center rounded-full border border-ink-900/10 bg-white/70 text-ink-800 lg:hidden"
              onClick={() => setOpen((v) => !v)}
            >
              {open ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
            </button>
          </div>
        </nav>
      </div>

      <AnimatePresence>
        {open && (
          <motion.div
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -10 }}
            transition={{ duration: 0.2 }}
            className="container-xl lg:hidden"
          >
            <ul className="glass mt-3 flex flex-col gap-1 rounded-2xl p-3 shadow-card">
              {navLinks.map((link) => (
                <li key={link.to}>
                  <NavLink
                    to={link.to}
                    end={link.to === "/"}
                    onClick={close}
                    className={({ isActive }) =>
                      `block rounded-xl px-4 py-3 text-base font-medium transition-colors ${
                        isActive
                          ? "bg-teal-100 text-teal-800"
                          : "text-ink-800 hover:bg-teal-50"
                      }`
                    }
                  >
                    {link.label}
                  </NavLink>
                </li>
              ))}
              <li className="mt-1 border-t border-ink-900/10 pt-2">
                <Link
                  to="/get-involved#donate"
                  onClick={close}
                  className="flex items-center justify-center gap-2 rounded-xl bg-ink-900 px-4 py-3 text-base font-semibold text-cream-50"
                >
                  <Heart className="h-4 w-4 fill-rose-accent text-rose-accent" />
                  Donate
                </Link>
              </li>
            </ul>
          </motion.div>
        )}
      </AnimatePresence>
    </header>
  );
}
