import { defineConfig } from 'vitepress'
import { siteConfig } from './theme/site-config.js'

const { seo, brand } = siteConfig

export default defineConfig({
  vite: {
    server: {
      allowedHosts: true,
    },
    ssr: {
      noExternal: [],
    },
    build: {
      rollupOptions: {
        external: (id) => id.startsWith('/manus-storage/'),
      },
    },
  },

  title: brand.name,
  description: brand.description,
  lang: 'en-US',

  head: [
    ['script', { async: true, src: 'https://www.googletagmanager.com/gtag/js?id=G-97MYY8GF2T' }],
    ['script', {}, `
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-97MYY8GF2T');
    `],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:title', content: seo.title }],
    ['meta', { property: 'og:description', content: seo.description }],
    ['meta', { property: 'og:image', content: '/favicon.png' }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
    ['meta', { name: 'twitter:title', content: seo.title }],
    ['meta', { name: 'twitter:description', content: seo.description }],
    ['meta', { name: 'keywords', content: seo.keywords.join(', ') }],
    ['script', { type: 'application/ld+json' }, JSON.stringify({
      '@context': 'https://schema.org',
      '@type': 'WebSite',
      name: brand.name,
      url: seo.hostname,
      description: brand.description,
    })],
  ],

  themeConfig: {
    nav: siteConfig.nav,

    notFound: {
      quote: 'The page you are looking for does not exist.',
      linkLabel: 'Back to Home',
      linkUrl: '/',
    },

    docFooter: {
      prev: false,
      next: false,
    },

    lastUpdated: false,
    editLink: undefined,
  },

  sitemap: {
    hostname: seo.hostname,
  },

  ignoreDeadLinks: [
    /^\/blog\//,
    /^http:\/\/localhost/,
    /^\/cssbuy-/,
    /^\/is-/,
  ],

  cleanUrls: 'with-subfolders',

  // Generate canonical URLs for each page
  transformPageData(pageData) {
    const canonicalUrl = `${seo.hostname}/${pageData.relativePath.replace(/\.md$/, '').replace(/index$/, '')}`
    pageData.frontmatter.head = pageData.frontmatter.head || []
    pageData.frontmatter.head.push(
      ['link', { rel: 'canonical', href: canonicalUrl }]
    )
    if (pageData.frontmatter.description) {
      pageData.frontmatter.head.push(
        ['meta', { name: 'description', content: pageData.frontmatter.description }]
      )
    }
    if (Array.isArray(pageData.frontmatter.keywords) && pageData.frontmatter.keywords.length) {
      pageData.frontmatter.head.push(
        ['meta', { name: 'keywords', content: pageData.frontmatter.keywords.join(', ') }]
      )
    }
    return pageData
  },

  srcExclude: [
    // Root-level internal documents (should not be indexed)
    'ARTICLE_PROMPT_GUIDE.md',
    'BANNED_TERMS.md',
    'BATCH_MODIFICATION_PLAN.md',
    'WEBSITE_POSITIONING.md',
    'flexible-article-generator.md',
    'ideas.md',
    // Blog-level internal documents
    'blog/cssbuy-article-prompt.md',
    'blog/cssbuy-internal-link-rules.md',
    'blog/cssbuy-product-reference.md',
    'blog/cssbuy-review-report.md',
    'blog/cssbuy-topic-list.md',
    'blog/flexible-article-generator.md',
    'blog/topic-matrix.md',
    'blog/ideas.md',
    'blog/content-checklist.md',
    'blog/local-setup.md',
    'blog/product-workflow.md',
    'blog/website-structure.md',
  ],
})
