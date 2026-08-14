// ============================================================
// CSSBuy Site Configuration
// repsootd.com - Fashion Finds Resource & Buying Guide
// ============================================================

export const siteConfig = {

  // ---- Brand ----
  brand: {
    name: 'CSSBuy',
    tagline: 'Fashion Finds Resource & Buying Guide',
    description: 'Independent resource for CSSBuy shoppers. Product guides, category breakdowns, sizing tips, and CSSBuy access — organized in one place.',
    primaryColor: '#8B0000',
    accentColor: '#d4af37',
    logoText: 'CSSBuy',
  },

  // ---- Navigation ----
  nav: [
    { text: 'Home', link: '/' },
    { text: 'Clothing', link: '/clothes' },
    { text: 'Shoes', link: '/shoes' },
    { text: 'Pants', link: '/pants' },
    { text: 'Hats', link: '/hats' },
    { text: 'Accessories', link: '/accessories' },
    { text: 'Electronics', link: '/electronics' },
    { text: 'Blog', link: '/blog' },
  ],

  // ---- Main Categories ----
  categories: [
    {
      id: 'clothes',
      name: 'CSSBuy Clothing',
      icon: '',
      description: 'Hoodies, T-shirts, shirts, jackets, dresses and everyday wardrobe guides with direct article paths.',
      blogLink: '/blog/cssbuy-hoodies/',
      landingLink: '/clothes',
    },
    {
      id: 'shoes',
      name: 'CSSBuy Shoes',
      icon: '',
      description: 'Sneakers, basketball shoes, running shoes, football shoes, hiking footwear and boots.',
      blogLink: '/blog/cssbuy-sneakers/',
      landingLink: '/shoes',
    },
    {
      id: 'pants',
      name: 'CSSBuy Pants',
      icon: '',
      description: 'Jeans, pants, shorts, sweatpants and tracksuits with fit and fabric reading paths.',
      blogLink: '/blog/cssbuy-pants/',
      landingLink: '/pants',
    },
    {
      id: 'hats',
      name: 'CSSBuy Hats',
      icon: '',
      description: 'Hats, caps, beanies, bucket hats and fit guides for everyday finishing pieces.',
      blogLink: '/blog/cssbuy-hats/',
      landingLink: '/hats',
    },
    {
      id: 'accessories',
      name: 'CSSBuy Accessories',
      icon: '',
      description: 'Bags, belts, jewelry, sunglasses, watches and wallets with direct article paths.',
      blogLink: '/blog/cssbuy-accessories/',
      landingLink: '/accessories',
    },
    {
      id: 'electronics',
      name: 'CSSBuy Electronics',
      icon: '',
      description: 'Electronics, phones, iPhone resources, AirPods and tech gadget guides.',
      blogLink: '/blog/cssbuy-electronics/',
      landingLink: '/electronics',
    },
  ],

  // ---- Featured Categories (Trending) ----
  featuredCategories: [
    { name: 'Sneakers', slug: 'sneakers', image: '/images/hero-sneakers.webp' },
    { name: 'Hoodies', slug: 'hoodies', image: '/images/hero-hoodies.webp' },
    { name: 'T-Shirts', slug: 't-shirts', image: '/images/hero-tshirts.webp' },
    { name: 'Jackets', slug: 'jackets', image: '/images/hero-jackets.webp' },
    { name: 'Pants', slug: 'pants', image: '/images/hero-pants.webp' },
    { name: 'Shirts', slug: 'shirts', image: '/images/hero-shirts.webp' },
    { name: 'Bags', slug: 'bags', image: '/images/hero-bags.webp' },
    { name: 'Watches', slug: 'watches', image: '/images/hero-watches.webp' },
    { name: 'Accessories', slug: 'accessories', image: '/images/hero-accessories.webp' },
    { name: 'Streetwear', slug: 'streetwear', image: '/images/hero-streetwear.webp' },
    { name: 'Casual Wear', slug: 'casual-wear', image: '/images/hero-casual.webp' },
    { name: 'New Arrivals', slug: 'new-arrivals', image: '/images/hero-new-arrivals.webp' },
  ],

  // ---- External Links ----
  links: {
    shopping: 'https://repsootd.com/',
  },

  // ---- SEO Defaults ----
  seo: {
    hostname: 'https://repsootd.com',
    title: 'CSSBuy 2026 - CSSBuy product finds, Category Guides and Product Research',
    description: 'Explore CSSBuy 2026 through organized CSSBuy product finds, category overviews, focused guides and direct CSSBuy access.',
    keywords: ['CSSBuy 2026', 'CSSBuy', 'CSSBuy product finds', 'clothing CSSBuy', 'shoes CSSBuy', 'pants CSSBuy', 'hats CSSBuy', 'accessories CSSBuy', 'electronics CSSBuy'],
    ga4: 'G-9WJTE8DY0P',
  },

  // ---- Announcement Bar ----
  announcement: 'Product guides and CSSBuy updated regularly. Browse by category below.',
}
