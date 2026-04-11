type Props = {
  variant: "classroom" | "vocational" | "seabird" | "portrait" | "activity" | "crafts" | "music" | "garden";
  className?: string;
  label?: string;
};

/**
 * Lightweight SVG illustrations used in place of real photography.
 * Warm, inclusive, abstract — safe to ship before real imagery is collected.
 */
export default function IllustrationCard({ variant, className = "", label }: Props) {
  return (
    <div
      role="img"
      aria-label={label ?? variant}
      className={`relative overflow-hidden rounded-[1.5rem] ${className}`}
    >
      <svg
        viewBox="0 0 600 420"
        className="h-full w-full"
        preserveAspectRatio="xMidYMid slice"
      >
        <defs>
          <linearGradient id={`bg-${variant}`} x1="0" x2="1" y1="0" y2="1">
            {variant === "classroom" && (
              <>
                <stop offset="0" stopColor="#d1f4f2" />
                <stop offset="1" stopColor="#6fdad4" />
              </>
            )}
            {variant === "vocational" && (
              <>
                <stop offset="0" stopColor="#ffeecb" />
                <stop offset="1" stopColor="#ffa01d" />
              </>
            )}
            {variant === "seabird" && (
              <>
                <stop offset="0" stopColor="#effbfa" />
                <stop offset="1" stopColor="#33c2bd" />
              </>
            )}
            {variant === "portrait" && (
              <>
                <stop offset="0" stopColor="#fff9ed" />
                <stop offset="1" stopColor="#ffd98e" />
              </>
            )}
            {variant === "activity" && (
              <>
                <stop offset="0" stopColor="#d1f4f2" />
                <stop offset="1" stopColor="#ffd98e" />
              </>
            )}
            {variant === "crafts" && (
              <>
                <stop offset="0" stopColor="#ffeecb" />
                <stop offset="1" stopColor="#ff6b6b" />
              </>
            )}
            {variant === "music" && (
              <>
                <stop offset="0" stopColor="#a7eae6" />
                <stop offset="1" stopColor="#0c8783" />
              </>
            )}
            {variant === "garden" && (
              <>
                <stop offset="0" stopColor="#d1f4f2" />
                <stop offset="1" stopColor="#f58104" />
              </>
            )}
          </linearGradient>
          <radialGradient id={`sun-${variant}`} cx="0.8" cy="0.2" r="0.6">
            <stop offset="0" stopColor="#ffd98e" stopOpacity="0.85" />
            <stop offset="1" stopColor="#ffd98e" stopOpacity="0" />
          </radialGradient>
          <pattern
            id={`dots-${variant}`}
            x="0"
            y="0"
            width="22"
            height="22"
            patternUnits="userSpaceOnUse"
          >
            <circle cx="2" cy="2" r="1.4" fill="#0c5553" fillOpacity="0.12" />
          </pattern>
        </defs>

        <rect width="600" height="420" fill={`url(#bg-${variant})`} />
        <rect width="600" height="420" fill={`url(#sun-${variant})`} />
        <rect width="600" height="420" fill={`url(#dots-${variant})`} />

        {/* Horizon */}
        <path
          d="M0 310 C 120 280 220 300 320 295 C 420 290 520 320 600 305 L 600 420 L 0 420 Z"
          fill="#0c5553"
          fillOpacity="0.18"
        />
        <path
          d="M0 340 C 140 320 240 350 340 340 C 440 330 520 355 600 345 L 600 420 L 0 420 Z"
          fill="#0c5553"
          fillOpacity="0.28"
        />

        {/* Scene-specific shapes */}
        {variant === "classroom" && (
          <>
            <circle cx="130" cy="210" r="42" fill="#ffd98e" />
            <circle cx="130" cy="210" r="30" fill="#ff6b6b" fillOpacity="0.6" />
            <rect x="230" y="170" width="230" height="140" rx="18" fill="#fdfaf3" />
            <line x1="255" y1="210" x2="430" y2="210" stroke="#0c5553" strokeWidth="3" />
            <line x1="255" y1="240" x2="390" y2="240" stroke="#0c5553" strokeWidth="3" />
            <line x1="255" y1="270" x2="410" y2="270" stroke="#0c5553" strokeWidth="3" />
            <circle cx="485" cy="195" r="18" fill="#f58104" />
          </>
        )}
        {variant === "vocational" && (
          <>
            <rect x="80" y="170" width="180" height="140" rx="16" fill="#fdfaf3" />
            <path d="M110 220 L 230 220 M 110 245 L 210 245 M 110 270 L 220 270" stroke="#b44a07" strokeWidth="4" strokeLinecap="round" />
            <circle cx="170" cy="195" r="14" fill="#ff6b6b" />
            <circle cx="400" cy="220" r="60" fill="#0c8783" fillOpacity="0.25" />
            <circle cx="400" cy="220" r="36" fill="#0c8783" />
            <path d="M380 220 L 420 220 M 400 200 L 400 240" stroke="#fdfaf3" strokeWidth="5" strokeLinecap="round" />
          </>
        )}
        {variant === "seabird" && (
          <>
            <path d="M40 150 Q 80 110 120 150 Q 160 190 200 150" fill="none" stroke="#0c5553" strokeWidth="4" strokeLinecap="round" />
            <path d="M220 120 Q 260 80 300 120 Q 340 160 380 120" fill="none" stroke="#0c5553" strokeWidth="4" strokeLinecap="round" />
            <circle cx="500" cy="120" r="40" fill="#ffd98e" />
            <path d="M0 380 L 600 380" stroke="#0c5553" strokeOpacity="0.6" strokeWidth="3" strokeDasharray="4 8" />
          </>
        )}
        {variant === "portrait" && (
          <>
            <circle cx="300" cy="190" r="80" fill="#fdfaf3" />
            <circle cx="278" cy="180" r="5" fill="#0b1d22" />
            <circle cx="322" cy="180" r="5" fill="#0b1d22" />
            <path d="M275 210 Q 300 240 325 210" stroke="#0b1d22" strokeWidth="4" strokeLinecap="round" fill="none" />
            <circle cx="300" cy="150" r="90" fill="none" stroke="#f58104" strokeWidth="8" />
          </>
        )}
        {variant === "activity" && (
          <>
            <circle cx="150" cy="220" r="38" fill="#ff6b6b" />
            <circle cx="300" cy="200" r="48" fill="#0c8783" />
            <circle cx="440" cy="230" r="34" fill="#ffa01d" />
            <path d="M120 280 Q 300 340 480 280" fill="none" stroke="#fdfaf3" strokeWidth="6" strokeLinecap="round" />
          </>
        )}
        {variant === "crafts" && (
          <>
            <rect x="120" y="180" width="100" height="140" rx="10" fill="#fdfaf3" />
            <rect x="250" y="200" width="100" height="120" rx="10" fill="#0c8783" />
            <rect x="380" y="170" width="100" height="150" rx="10" fill="#ffa01d" />
            <circle cx="170" cy="220" r="18" fill="#ff6b6b" />
            <circle cx="300" cy="240" r="18" fill="#ffd98e" />
            <circle cx="430" cy="210" r="18" fill="#fdfaf3" />
          </>
        )}
        {variant === "music" && (
          <>
            <path d="M180 180 L 180 300 L 160 300 L 160 200 L 260 180 L 260 280 L 240 280 L 240 160 Z" fill="#fdfaf3" />
            <circle cx="160" cy="300" r="18" fill="#fdfaf3" />
            <circle cx="240" cy="280" r="18" fill="#fdfaf3" />
            <path d="M360 300 Q 400 240 440 300 T 520 300" stroke="#fdfaf3" strokeWidth="5" fill="none" strokeLinecap="round" />
          </>
        )}
        {variant === "garden" && (
          <>
            <circle cx="170" cy="240" r="34" fill="#0c5553" />
            <rect x="165" y="240" width="10" height="80" fill="#0c5553" />
            <circle cx="310" cy="220" r="40" fill="#0c8783" />
            <rect x="305" y="220" width="10" height="100" fill="#0c5553" />
            <circle cx="460" cy="250" r="28" fill="#0c5553" />
            <rect x="455" y="250" width="10" height="70" fill="#0c5553" />
            <circle cx="480" cy="110" r="38" fill="#ffd98e" />
          </>
        )}
      </svg>
    </div>
  );
}
