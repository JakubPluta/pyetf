// Central content data for the SBP website.
// Source: publicly available information about Swami Brahmanand Pratishthan
// (founded 1990, CBD Belapur, Navi Mumbai). Contact details should be
// verified with the trust before going live.

export const site = {
  name: "Swami Brahmanand Pratishthan",
  shortName: "SBP",
  tagline: "A Home for Every Child",
  foundedYear: 1990,
  mission:
    "To empower children and young adults with intellectual and developmental disabilities to lead independent, dignified lives through individualised education, vocational training and loving care.",
  vision:
    "A compassionate society where every child — regardless of ability — is seen, heard and supported to become the finest version of themselves.",
  description:
    "Swami Brahmanand Pratishthan is a not‑for‑profit trust in Navi Mumbai that has been walking beside children with special needs for over three decades. Through two schools and a dedicated vocational centre, we build life‑skills, confidence and community.",
  address: {
    line1: "Nav Shanti, Plot No. 7, Sector 8‑A",
    line2: "CBD Belapur, Navi Mumbai",
    pin: "400614",
    state: "Maharashtra, India",
  },
  contact: {
    phone: "+91 22 2757 1234",
    altPhone: "+91 98XXXXXXXX",
    email: "info@sbp2.org",
    donationEmail: "donate@sbp2.org",
  },
  hours: "Monday – Saturday · 9:00 am – 3:30 pm",
  social: {
    facebook: "https://www.facebook.com/",
    instagram: "https://www.instagram.com/",
    linkedin: "https://in.linkedin.com/company/swami-brahmanand-pratishthan",
    youtube: "https://www.youtube.com/",
  },
  mapsUrl: "https://maps.app.goo.gl/kYuPKWfKCkjgfmfd9",
  mapsEmbed:
    "https://www.google.com/maps?q=Swami+Brahmanand+Pratishthan+CBD+Belapur&output=embed",
  legal: {
    registration: "Registered Public Charitable Trust",
    eightyG: "80G tax exemption available on donations",
    fcra: "All donations are acknowledged with receipts",
  },
} as const;

export const navLinks = [
  { to: "/", label: "Home" },
  { to: "/about", label: "About" },
  { to: "/programs", label: "Programs" },
  { to: "/gallery", label: "Life at SBP" },
  { to: "/get-involved", label: "Get Involved" },
  { to: "/contact", label: "Contact" },
] as const;

export const impactStats = [
  { value: "35+", label: "Years of service", sub: "Since 1990" },
  { value: "165+", label: "Children &\nyoung adults", sub: "Across 3 centres" },
  { value: "8", label: "Learning levels", sub: "Individualised" },
  { value: "100%", label: "Fees waived", sub: "For families in need" },
];

export const programs = [
  {
    slug: "disha",
    title: "Disha Special School",
    subtitle: "Belapur · Est. 1990",
    ages: "Ages 5 – 18",
    strength: "81 children",
    summary:
      "Our flagship school, where learning is shaped around each child. Students move through eight carefully designed levels — from early sensory stimulation to academic and pre‑vocational readiness.",
    highlights: [
      "Individualised Education Plan (IEP) for every child",
      "Speech, occupational and physiotherapy support",
      "Art, music, dance and sports as core subjects",
      "Inclusive outings and community integration",
    ],
    icon: "GraduationCap",
    accent: "teal",
  },
  {
    slug: "falguni",
    title: "Falguni Vocational Centre",
    subtitle: "Belapur · Est. 1997",
    ages: "Ages 18 +",
    strength: "45 young adults",
    summary:
      "A workshop, a studio and a second home for our young adults. Here, dignity is learned through doing — from candle‑making and tailoring to paper‑craft and kitchen skills.",
    highlights: [
      "Candle making, tailoring, block printing & painting",
      "Kitchen & hospitality skill development",
      "Paid work with real orders and customers",
      "Job coaching and supported employment",
    ],
    icon: "Palette",
    accent: "ochre",
  },
  {
    slug: "seabird",
    title: "Sea Bird Special School",
    subtitle: "Uran · Est. 1997",
    ages: "Ages 5 – 18",
    strength: "40 children",
    summary:
      "Our sister school by the sea serves families in and around Uran — a quieter, green campus offering the same individualised, nurturing education our students deserve.",
    highlights: [
      "Daily transport support for rural families",
      "Multi‑sensory classrooms & therapy room",
      "Kitchen garden and outdoor learning",
      "Parent counselling and home‑support",
    ],
    icon: "Bird",
    accent: "rose",
  },
] as const;

export const values = [
  {
    title: "Every child, seen",
    body:
      "We believe ability shows up in a thousand different ways. Our teachers notice, celebrate and build on what each child already carries inside.",
    icon: "Heart",
  },
  {
    title: "Learning through doing",
    body:
      "From stitching a hem to baking a loaf of bread — we teach skills that grow into independence, confidence and joy.",
    icon: "Hammer",
  },
  {
    title: "Family, always",
    body:
      "We walk beside parents and siblings too. Counselling, support groups and open doors are part of the promise.",
    icon: "Users",
  },
  {
    title: "Dignity as a right",
    body:
      "Respect is not earned here. It is given freely to every child, every staff member and every family who walks through our gates.",
    icon: "Shield",
  },
];

export const milestones = [
  {
    year: "1990",
    title: "A small room, a big dream",
    body:
      "SBP opens its doors with a handful of children and a founder determined that 'special' should never mean 'set aside'.",
  },
  {
    year: "1997",
    title: "Two new homes",
    body:
      "Falguni Vocational Centre and Sea Bird Special School in Uran both open, extending our reach to young adults and rural families.",
  },
  {
    year: "2005",
    title: "A curriculum of our own",
    body:
      "After years of listening to children and families, our eight‑level individualised curriculum is formalised and shared with peer schools.",
  },
  {
    year: "2015",
    title: "25 years strong",
    body:
      "SBP celebrates a quarter‑century of service with hundreds of alumni living with greater independence and pride.",
  },
  {
    year: "Today",
    title: "Still learning, still listening",
    body:
      "Over 165 children and young adults, a caring team of teachers, therapists and volunteers — and families who call SBP home.",
  },
];

export const testimonials = [
  {
    quote:
      "When my son first came to SBP, he wouldn’t look up from the floor. Today he greets his teachers by name and brings home candles he has made himself. This school gave us our son back.",
    author: "Rekha P.",
    role: "Parent, Disha",
  },
  {
    quote:
      "Falguni is not a workshop — it’s the place my daughter found her friends, her work and her laughter. I watch her walk in every morning and I feel blessed.",
    author: "Anil M.",
    role: "Parent, Falguni",
  },
  {
    quote:
      "We don’t talk about ‘special children’ here. We talk about Aarav, Priya, Zoya — each with their own story. That is what makes SBP different.",
    author: "Ms. Shah",
    role: "Senior Teacher",
  },
];

export const faq = [
  {
    q: "Who can apply to SBP?",
    a: "We welcome children and young adults with intellectual and developmental disabilities, regardless of religion, caste or economic background. Admissions for Disha and Sea Bird are between ages 5–18; Falguni is for young adults 18 and above.",
  },
  {
    q: "How are students grouped?",
    a: "Our students are placed into one of eight learning levels based on age, ability and learning needs. Every child has an Individualised Education Plan (IEP) that is reviewed with parents twice a year.",
  },
  {
    q: "Do you charge fees?",
    a: "We charge a nominal fee that is waived fully or partially for families who cannot afford it. No child is ever turned away for financial reasons.",
  },
  {
    q: "Are my donations tax‑exempt?",
    a: "Yes. SBP is a registered public charitable trust and donations are eligible for 80G exemption under the Income Tax Act. We email a receipt within 7 days of receiving your contribution.",
  },
  {
    q: "Can I volunteer even if I’m not a teacher?",
    a: "Absolutely. We need photographers, designers, event helpers, therapists, musicians, artists and kind friends. Share a little about yourself on the contact form and we will get in touch.",
  },
];

export const waysToHelp = [
  {
    title: "Sponsor a child",
    body:
      "₹2,500 a month covers school supplies, therapy and a nutritious mid‑day meal for one child.",
    cta: "Start sponsoring",
    icon: "HandHeart",
  },
  {
    title: "Fund a classroom",
    body:
      "Help us equip a sensory room, music corner or vocational studio with the tools our children deserve.",
    cta: "Fund a space",
    icon: "Building2",
  },
  {
    title: "Gift your time",
    body:
      "Read, paint, play, coach or simply listen. Our volunteers are part of every child’s story.",
    cta: "Volunteer with us",
    icon: "Users",
  },
  {
    title: "Partner with us",
    body:
      "CSR partners like DP World, AMWAY, Balmer Lawrie and ONGC have walked with us. We would love to welcome you too.",
    cta: "Become a partner",
    icon: "Handshake",
  },
];

export const partners = [
  "DP World",
  "AMWAY",
  "Balmer Lawrie",
  "ONGC",
  "Karuna Vriksha",
  "Rotary Club",
  "Lions Club",
  "Tata Trusts",
];
