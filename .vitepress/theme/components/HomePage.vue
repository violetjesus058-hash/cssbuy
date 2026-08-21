<template>
  <main class="modern-home">
    <section class="hero-section">
      <div class="page-container hero-content">
        <p class="eyebrow">China shopping agent · Taobao, 1688, Tmall & more</p>
        <h1>Shop from China’s Biggest Marketplaces <span>with Confidence.</span></h1>
        <p class="hero-copy">
          Buy from Taobao, 1688, Tmall and other Chinese marketplaces with practical guidance for product checks,
          warehouse storage and international shipping to Brazil and worldwide.
        </p>
        <div class="hero-actions">
          <a :href="shoppingUrl" target="_blank" rel="nofollow sponsored noopener noreferrer" class="button button-secondary cta-shopping">
            Start shopping
          </a>
        </div>
        <dl class="hero-stats" aria-label="Catalog highlights">
          <div>
            <dt>Search</dt>
            <dd>URL, keyword or photo</dd>
          </div>
          <div>
            <dt>Check</dt>
            <dd>QC and warehouse guidance</dd>
          </div>
          <div>
            <dt>Ship</dt>
            <dd>Brazil and worldwide</dd>
          </div>
        </dl>
      </div>
    </section>

    <section class="intro-section">
      <div class="page-container intro-grid">
        <div class="intro-content">
          <p class="section-kicker">A clearer route to China shopping</p>
          <h2>Search, buy, check and ship with better context.</h2>
          <p>
            Use focused guides to understand how Chinese marketplace shopping works, what to review before ordering,
            how warehouse checks fit into the process and what to confirm before international delivery.
          </p>
        </div>
      </div>
    </section>

    <section id="categories" class="section section-light">
      <div class="page-container">
        <div class="section-heading">
          <p class="section-kicker">Popular categories</p>
          <h2>Explore products people buy from China.</h2>
          <p>Start with a product category, then use the related guides to compare materials, sizing, quality checks and buying considerations.</p>
        </div>
        <div class="category-grid">
          <a v-for="cat in categoryCards" :key="cat.id" :href="cat.link" class="category-card">
            <span class="category-icon" aria-hidden="true">{{ cat.icon }}</span>
            <h3>{{ cat.name }}</h3>
            <p>{{ cat.description }}</p>
            <span class="card-link">Explore category <span aria-hidden="true">→</span></span>
          </a>
        </div>
      </div>
    </section>

    <section class="section section-muted">
      <div class="page-container">
        <div class="section-heading">
          <p class="section-kicker">How CSSBuy shopping works</p>
          <h2>From product search to international delivery.</h2>
        </div>
        <ol class="steps-grid">
          <li v-for="(step, index) in steps" :key="step.title" class="step-card">
            <span class="step-index">0{{ index + 1 }}</span>
            <h3>{{ step.title }}</h3>
            <p>{{ step.description }}</p>
          </li>
        </ol>
      </div>
    </section>

    <section id="features" class="section section-light">
      <div class="page-container feature-layout">
        <div class="feature-intro">
          <p class="section-kicker">Built for confident decisions</p>
          <h2>Know what happens after you find a product.</h2>
          <p>
            The guides explain the practical steps between a marketplace listing and a delivered parcel, while keeping
            product, seller, stock, customs and shipping claims appropriately cautious.
          </p>
          <a :href="links.shopping" target="_blank" rel="nofollow sponsored noopener noreferrer" class="text-link cta-CSSBuy">
            Open the full catalog <span aria-hidden="true">→</span>
          </a>
        </div>
        <div class="feature-grid">
          <article v-for="feature in features" :key="feature.title" class="feature-card">
            <span class="feature-mark" aria-hidden="true">{{ feature.mark }}</span>
            <h3>{{ feature.title }}</h3>
            <p>{{ feature.description }}</p>
          </article>
        </div>
      </div>
    </section>

    <section id="how-it-works" class="section section-dark">
      <div class="page-container final-cta">
        <div>
          <p class="section-kicker">Ready when you are</p>
          <h2>Start shopping from China with a clearer plan.</h2>
          <p>Open the product catalog, then return to CSSBuy guides whenever you need more context on quality checks, storage or shipping to Brazil.</p>
        </div>
      </div>
    </section>

    <section id="faq" class="section section-light">
      <div class="page-container faq-wrap">
        <div class="section-heading section-heading-left">
          <p class="section-kicker">Quick answers</p>
          <h2>Frequently asked questions.</h2>
        </div>
        <div class="faq-list">
          <details v-for="faq in faqs" :key="faq.question" class="faq-item">
            <summary>{{ faq.question }}</summary>
            <p>{{ faq.answer }}</p>
          </details>
        </div>
      </div>
    </section>
    <section id="community-research" class="section section-research">
      <div class="page-container research-card">
        <div>
          <p class="section-kicker">Brazil shopping research</p>
          <h2>A practical research path for Brazilian shoppers.</h2>
          <p class="research-card-copy">Compare product details, marketplace context, destination questions and external shopping terms before opening a listing. This guide keeps CSSBuy focused on organized product discovery for Brazil.</p>
          <a href="/blog/cssbuy-community-buying-guide/" class="research-card-link">Read the CSSBuy Brazil guide <span aria-hidden="true">→</span></a>
        </div>
        <div class="research-card-note">
          <strong>CSSBuy community research</strong>
          <span>Community discussions are treated as signals for what to verify. The guide separates reported experiences from current platform policies, live quotes and transaction terms.</span>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup>
import { computed } from 'vue'
import { siteConfig } from '../site-config.js'

const { links } = siteConfig
const shoppingUrl = 'https://repsootd.com/'

const categoryCards = computed(() => [
  { id: 'sneakers', name: 'Sneakers', description: 'Dedicated guide to sneaker styles and product discovery.', link: '/blog/cssbuy-sneakers-2026-complete-guide-to-verified-footwear', icon: '👟' },
  { id: 'shoes', name: 'Shoes', description: 'Browse footwear options beyond the main sneaker collection.', link: '/blog/cssbuy-shoes-2026-complete-collection-of-verified-footwear', icon: '👞' },
  { id: 'hoodies', name: 'Hoodies', description: 'Explore hoodies, layers and casual everyday essentials.', link: '/blog/cssbuy-hoodie-2026-verified-streetwear-and-designer-hoodie-collection', icon: '🧥' },
  { id: 't-shirts', name: 'T-Shirts', description: 'Find staple tees and graphic shirt discovery resources.', link: '/blog/cssbuy-t-shirt-2026-verified-streetwear-and-designer-t-shirt-collection', icon: '👕' },
  { id: 'jackets', name: 'Jackets', description: 'Discover jackets and outerwear guides by style.', link: '/blog/cssbuy-jacket-2026-complete-guide-to-outerwear-and-layering-pieces', icon: '🧤' },
  { id: 'jeans', name: 'Jeans', description: 'Browse denim and jeans-focused product guidance.', link: '/blog/cssbuy-jeans-2026-complete-guide-to-denim-and-work-pants', icon: '👖' },
  { id: 'pants', name: 'Pants', description: 'Explore trousers, sweatpants and everyday bottoms.', link: '/blog/cssbuy-pants-2026-complete-guide-to-all-styles-and-brands', icon: '🩳' },
  { id: 'shorts', name: 'Shorts', description: 'Find shorts for casual and warm-weather outfits.', link: '/blog/cssbuy-shorts-2026-your-complete-guide-to-summer-and-streetwear-styles', icon: '🩳' },
  { id: 'tracksuits', name: 'Tracksuits', description: 'Browse coordinated tracksuits and sport-inspired looks.', link: '/blog/cssbuy-tracksuit-2026-complete-collection-of-verified-tracksuits', icon: '🏃' },
  { id: 'dresses', name: 'Dresses', description: 'Explore dress styles and clothing discovery options.', link: '/blog/cssbuy-dress-2026-complete-guide-to-womens-fashion-collection', icon: '👗' },
  { id: 'hats', name: 'Hats & Caps', description: 'Find caps, hats and finishing pieces for your outfit.', link: '/blog/cssbuy-hats-2026-complete-guide-to-verified-headwear-collection', icon: '🧢' },
  { id: 'bags', name: 'Bags', description: 'Browse bag guides across everyday and statement styles.', link: '/blog/cssbuy-bags-2026-complete-guide-to-backpacks-crossbody-and-more', icon: '👜' },
  { id: 'accessories', name: 'Accessories', description: 'Explore belts, small goods and complementary details.', link: '/blog/cssbuy-accessories-2026-complete-guide-to-hats-jewelry-and-more', icon: '✨' },
  { id: 'watches', name: 'Watches', description: 'Discover watch guides and wearable accessory options.', link: '/blog/cssbuy-watch-2026-complete-guide-to-affordable-luxury-timepieces', icon: '⌚' },
  { id: 'sunglasses', name: 'Sunglasses', description: 'Browse eyewear and sunglasses discovery resources.', link: '/blog/cssbuy-sunglasses-2026-complete-guide-to-verified-eyewear', icon: '🕶️' }
])

const steps = [
  { title: 'Search a marketplace', description: 'Start with a product URL, keyword or image from Taobao, 1688, Tmall or another Chinese marketplace.' },
  { title: 'Buy through the agent', description: 'Review product information, price, seller details and applicable service costs before confirming.' },
  { title: 'Check and store', description: 'Use warehouse QC information and storage guidance before deciding what to keep or consolidate.' },
  { title: 'Ship internationally', description: 'Compare shipping methods, destination rules and estimated costs before sending a parcel to Brazil.' }
]

const features = [
  { mark: '01', title: 'Marketplace access', description: 'Learn how URL, keyword and image-based product discovery fits into a China shopping workflow.' },
  { mark: '02', title: 'Quality checks', description: 'Understand QC photos and inspection limits without treating them as an authenticity guarantee.' },
  { mark: '03', title: 'Warehouse storage', description: 'Review storage, consolidation and parcel preparation before international shipping.' },
  { mark: '04', title: 'Shipping guidance', description: 'Compare destination, route, customs and delivery considerations before you order.' }
]

const faqs = [
  {
    question: 'What is CSSBuy?',
    answer: 'CSSBuy is a shopping-agent and buying-guide resource that helps users understand how to source products from Chinese marketplaces and plan the steps from discovery to international delivery.'
  },
  {
    question: 'Can I buy from Taobao, 1688 and Tmall?',
    answer: 'The CSSBuy guides explain how these marketplace links fit into a China shopping-agent workflow. Product availability, seller details, service costs and shipping eligibility should be confirmed on the live platform page before ordering.'
  },
  {
    question: 'Does CSSBuy provide quality checks and shipping guidance?',
    answer: 'The resource covers QC photos, warehouse storage, parcel consolidation and international shipping considerations. QC is an inspection aid, not a guarantee of authenticity, condition or future availability.'
  }
]
</script>

<style scoped>
.modern-home {
  --ink: #111111;
  --muted-ink: #656565;
  --line: #e8e8e8;
  --surface: #f7f7f5;
  --accent: #5b5ce2;
  color: var(--ink);
  background: #fff;
}

.page-container { width: min(1180px, calc(100% - 48px)); margin: 0 auto; }
.hero-section { padding: 88px 0 72px; border-bottom: 1px solid var(--line); }
.hero-content { text-align: center; max-width: 900px; }
.eyebrow, .section-kicker { margin: 0 0 18px; color: var(--accent); font-size: 12px; font-weight: 750; letter-spacing: .12em; text-transform: uppercase; }
.hero-content h1 { max-width: 1120px; margin: 0 auto; color: var(--ink); font-size: clamp(40px, 5.1vw, 72px); font-weight: 800; letter-spacing: -.067em; line-height: 1.02; }
.hero-content h1 span { color: var(--accent); }
.hero-copy { max-width: 630px; margin: 28px auto 34px; color: var(--muted-ink); font-size: 19px; line-height: 1.7; }
.hero-actions { display: flex; justify-content: center; gap: 12px; flex-wrap: wrap; }
.button { display: inline-flex; align-items: center; justify-content: center; gap: 10px; min-height: 62px; padding: 0 34px; border: 1px solid transparent; border-radius: 10px; font-size: 16px; font-weight: 750; text-decoration: none; transition: transform .2s ease, box-shadow .2s ease, background .2s ease; }
.button:hover { transform: translateY(-2px); }
.button-primary { background: var(--ink); color: #fff; box-shadow: 0 10px 22px rgba(0,0,0,.12); }
.button-primary:hover { background: var(--accent); box-shadow: 0 12px 26px rgba(91,92,226,.22); }
.button-secondary { min-width: 230px; border-color: var(--line); background: #fff; color: var(--ink); box-shadow: 0 8px 20px rgba(0,0,0,.06); }
.button-secondary:hover { border-color: #c8c8c8; background: var(--surface); }
.hero-stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; max-width: 680px; margin: 56px auto 0; padding-top: 25px; border-top: 1px solid var(--line); }
.hero-stats div { text-align: center; }
.hero-stats dt { margin-bottom: 4px; color: var(--ink); font-size: 23px; font-weight: 800; letter-spacing: -.04em; }
.hero-stats dd { margin: 0; color: var(--muted-ink); font-size: 13px; }
.intro-section { padding: 96px 0; }
.intro-grid { display: block; max-width: 820px; text-align: center; }
.intro-content { margin: 0 auto; }
.intro-content .section-kicker { margin: 10px 0 18px; }
.intro-grid h2, .section-heading h2, .feature-intro h2, .final-cta h2 { margin: 0; font-size: clamp(30px, 4vw, 48px); font-weight: 780; letter-spacing: -.055em; line-height: 1.08; }
.intro-content > p:last-child { max-width: 700px; margin: 22px auto 0; color: var(--muted-ink); font-size: 18px; line-height: 1.75; }
.section { padding: 104px 0; }
.section-light { background: #fff; }
.section-muted { background: var(--surface); }
.section-heading { max-width: 670px; margin: 0 auto 52px; text-align: center; }
.section-heading h2 { font-size: clamp(30px, 4.3vw, 50px); }
.section-heading > p:last-child { margin: 16px auto 0; color: var(--muted-ink); font-size: 17px; line-height: 1.7; }
.category-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
.category-card { min-height: 264px; padding: 28px; border: 1px solid var(--line); border-radius: 14px; color: var(--ink); text-decoration: none; transition: border-color .2s ease, transform .2s ease, box-shadow .2s ease; }
.category-card:hover { border-color: var(--accent); transform: translateY(-5px); box-shadow: 0 20px 40px rgba(0,0,0,.07); }
.category-icon { display: grid; width: 46px; height: 46px; place-items: center; margin-bottom: 38px; border-radius: 12px; background: #f0f0fb; font-size: 23px; }
.category-card h3 { margin: 0 0 10px; font-size: 22px; letter-spacing: -.035em; }
.category-card p { min-height: 76px; margin: 0; color: var(--muted-ink); font-size: 15px; line-height: 1.7; }
.card-link, .text-link { display: inline-block; margin-top: 27px; color: var(--accent); font-size: 14px; font-weight: 750; text-decoration: none; }
.steps-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; padding: 0; margin: 0; list-style: none; counter-reset: none; }
.step-card { padding: 28px 24px; border-top: 1px solid #d7d7d4; }
.step-index { display: inline-block; margin-bottom: 50px; color: var(--accent); font-size: 13px; font-weight: 800; letter-spacing: .08em; }
.step-card h3, .feature-card h3 { margin: 0 0 10px; font-size: 20px; letter-spacing: -.03em; }
.step-card p, .feature-card p { margin: 0; color: var(--muted-ink); font-size: 15px; line-height: 1.7; }
.feature-layout { display: grid; grid-template-columns: .85fr 1.15fr; gap: 82px; align-items: start; }
.feature-intro { position: sticky; top: 96px; }
.feature-intro > p:not(.section-kicker) { margin: 22px 0 0; color: var(--muted-ink); font-size: 17px; line-height: 1.75; }
.feature-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; }
.feature-card { min-height: 225px; padding: 27px; border: 1px solid var(--line); border-radius: 12px; }
.feature-mark { display: block; margin-bottom: 47px; color: var(--accent); font-size: 12px; font-weight: 800; letter-spacing: .08em; }
.section-dark { background: var(--ink); color: #fff; }
.final-cta { display: flex; align-items: center; justify-content: space-between; gap: 40px; }
.final-cta h2 { max-width: 640px; color: #fff; }
.final-cta p:not(.section-kicker) { max-width: 600px; margin: 16px 0 0; color: rgba(255,255,255,.66); line-height: 1.7; }
.section-dark .section-kicker { color: #b6b6ff; }
.button-light { flex: 0 0 auto; background: #fff; color: var(--ink); }
.button-light:hover { background: #e8e8ff; }
.faq-wrap { display: grid; grid-template-columns: .8fr 1.2fr; gap: 72px; }
.section-heading-left { margin: 0; text-align: left; }
.faq-list { border-top: 1px solid var(--line); }
.faq-item { border-bottom: 1px solid var(--line); }
.faq-item summary { display: flex; align-items: center; justify-content: space-between; padding: 23px 0; cursor: pointer; font-size: 17px; font-weight: 700; list-style: none; }
.faq-item summary::-webkit-details-marker { display: none; }
.faq-item summary::after { content: '+'; color: var(--accent); font-size: 24px; font-weight: 400; }
.faq-item[open] summary::after { content: '−'; }
.faq-item p { max-width: 660px; margin: -3px 0 22px; color: var(--muted-ink); line-height: 1.7; }
@media (max-width: 900px) { .intro-grid, .feature-layout, .faq-wrap { grid-template-columns: 1fr; gap: 42px; } .intro-content { grid-column: auto; } .feature-intro { position: static; } .steps-grid { grid-template-columns: repeat(2, 1fr); } .category-grid { grid-template-columns: repeat(2, 1fr); } .final-cta { align-items: flex-start; flex-direction: column; } }
@media (max-width: 700px) { .page-container { width: min(100% - 32px, 1180px); } .hero-content h1 { white-space: normal; } .hero-section { padding: 76px 0 58px; } .hero-copy { font-size: 17px; } .hero-stats { margin-top: 54px; gap: 8px; } .hero-stats dt { font-size: 19px; } .intro-section, .section { padding: 72px 0; } .category-grid, .feature-grid { grid-template-columns: 1fr; } .category-card { min-height: auto; } .category-icon { margin-bottom: 38px; } .category-card p { min-height: auto; } .steps-grid { grid-template-columns: 1fr; gap: 4px; } .step-index { margin-bottom: 28px; } .section-heading { margin-bottom: 36px; } }
    .section-research { background: #f0f0fb; border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); }
    .research-card { display: grid; grid-template-columns: minmax(0, .9fr) minmax(280px, 1.1fr); gap: 48px; align-items: center; }
    .research-card h2 { max-width: 620px; margin: 0; font-size: clamp(30px, 4vw, 50px); font-weight: 780; letter-spacing: -.055em; line-height: 1.08; }
    .research-card-copy { max-width: 620px; margin: 20px 0 0; color: var(--muted-ink); font-size: 17px; line-height: 1.75; }
    .research-card-link { display: inline-flex; align-items: center; gap: 8px; margin-top: 28px; color: var(--accent); font-size: 15px; font-weight: 800; text-decoration: none; }
    .research-card-link:hover { text-decoration: underline; text-underline-offset: 4px; }
    .research-card-note { padding: 28px; border: 1px solid rgba(91,92,226,.22); border-radius: 16px; background: rgba(255,255,255,.72); color: var(--muted-ink); font-size: 15px; line-height: 1.7; }
    .research-card-note strong { display: block; margin-bottom: 8px; color: var(--ink); font-size: 17px; }
    @media (max-width: 760px) { .research-card { grid-template-columns: 1fr; gap: 26px; } .research-card-note { padding: 22px; } }
</style>
