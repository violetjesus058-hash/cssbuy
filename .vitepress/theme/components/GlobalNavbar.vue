<template>
  <header class="global-navbar">
    <div class="navbar-container">
      <a href="/" class="navbar-brand">{{ brand.logoText }}</a>

      <button
        class="mobile-menu-toggle"
        type="button"
        :aria-expanded="mobileMenuOpen"
        aria-controls="primary-navigation"
        @click="mobileMenuOpen = !mobileMenuOpen"
      >
        <span>{{ mobileMenuOpen ? 'Close' : 'Menu' }}</span>
        <span aria-hidden="true">{{ mobileMenuOpen ? '×' : '☰' }}</span>
      </button>

      <nav id="primary-navigation" class="navbar-menu" :class="{ 'is-mobile-open': mobileMenuOpen }" aria-label="Primary navigation">
        <a href="/" class="nav-item" :class="{ active: isActive('/') }" @click="closeMenus">Home</a>

        <div v-for="group in menuGroups" :key="group.id" class="nav-dropdown" @mouseenter="openOnHover(group.id)" @mouseleave="scheduleClose">
          <button
            class="nav-dropdown-trigger"
            type="button"
            :aria-expanded="openMenu === group.id"
            :aria-controls="`${group.id}-menu`"
            @click="toggleMenu(group.id)"
          >
            {{ group.label }} <span class="chevron" aria-hidden="true">⌄</span>
          </button>
          <div :id="`${group.id}-menu`" class="dropdown-panel" :class="{ 'is-open': openMenu === group.id }">
            <p class="dropdown-title">{{ group.label }}</p>
            <a class="dropdown-overview" :href="group.overviewLink" @click="closeMenus">
              Explore {{ group.label }} overview
              <span aria-hidden="true">→</span>
            </a>
            <a v-for="item in group.items" :key="item.link" :href="item.link" @click="closeMenus">
              {{ item.label }}
              <span aria-hidden="true">→</span>
            </a>
          </div>
        </div>

        <a href="/blog/" class="nav-item" :class="{ active: isActive('/blog') }" @click="closeMenus">Guides</a>
      </nav>

      <a :href="links.shopping" target="_blank" rel="nofollow" class="nav-cta">Access CSSBuy <span aria-hidden="true">↗</span></a>
    </div>
  </header>
</template>

<script setup>
import { onBeforeUnmount, ref } from 'vue'
import { useData } from 'vitepress'
import { siteConfig } from '../site-config.js'

const { brand, links } = siteConfig
const { page } = useData()
const openMenu = ref(null)
const mobileMenuOpen = ref(false)
let closeTimer = null

const menuGroups = [
  {
    id: 'clothing',
    label: 'Clothing',
    overviewLink: '/clothes',
    items: [
      { label: 'Hoodies', link: '/blog/cssbuy-hoodie-2026-verified-streetwear-and-designer-hoodie-collection' },
      { label: 'T-Shirts', link: '/blog/cssbuy-t-shirt-2026-verified-streetwear-and-designer-t-shirt-collection' },
      { label: 'Shirts', link: '/blog/cssbuy-shirt-2026-complete-guide-to-verified-shirt-collection' },
      { label: 'Jackets', link: '/blog/cssbuy-jacket-2026-complete-guide-to-outerwear-and-layering-pieces' },
      { label: 'Dresses', link: '/blog/cssbuy-dress-2026-complete-guide-to-womens-fashion-collection' },
      { label: 'Vests', link: '/blog/cssbuy-vest-2026-complete-guide-to-verified-vest-collection' }
    ]
  },
  {
    id: 'bottoms',
    label: 'Pants',
    overviewLink: '/pants',
    items: [
      { label: 'Jeans', link: '/blog/cssbuy-jeans-2026-complete-guide-to-denim-and-work-pants' },
      { label: 'Pants', link: '/blog/cssbuy-pants-2026-complete-guide-to-all-styles-and-brands' },
      { label: 'Shorts', link: '/blog/cssbuy-shorts-2026-your-complete-guide-to-summer-and-streetwear-styles' },
      { label: 'Sweatpants', link: '/blog/cssbuy-sweatpants-2026-complete-guide-to-verified-joggers-and-sweatpants' },
      { label: 'Tracksuits', link: '/blog/cssbuy-tracksuit-2026-complete-collection-of-verified-tracksuits' }
    ]
  },
  {
    id: 'shoes',
    label: 'Shoes',
    overviewLink: '/shoes',
    items: [
      { label: 'Sneakers', link: '/blog/cssbuy-sneakers-2026-complete-guide-to-verified-footwear' },
      { label: 'Basketball Shoes', link: '/blog/cssbuy-basketball-shoes-2026-your-complete-guide-to-verified-kicks' },
      { label: 'Running Shoes', link: '/blog/cssbuy-running-shoes-2026-performance-footwear-with-verified-quality' },
      { label: 'Football Shoes', link: '/blog/cssbuy-football-shoes-2026-your-complete-guide-to-verified-pitch-performance' },
      { label: 'Hiking Shoes', link: '/blog/cssbuy-hiking-shoes-2026-complete-guide-to-outdoor-footwear' },
      { label: 'Boots', link: '/blog/cssbuy-football-boots-2026-complete-guide-to-verified-pitch-footwear' }
    ]
  },
  {
    id: 'hats',
    label: 'Hats',
    overviewLink: '/hats',
    items: [
      { label: 'Hats', link: '/blog/cssbuy-hats-2026-complete-guide-to-verified-headwear-collection' },
      { label: 'Caps', link: '/blog/cssbuy-caps-2026-complete-guide-to-verified-baseball-caps-and-headwear' },
      { label: 'Hats Guide', link: '/blog/cssbuy-hats-2026-complete-guide-to-verified-headwear-collection' }
    ]
  },
  {
    id: 'accessories',
    label: 'Accessories',
    overviewLink: '/accessories',
    items: [
      { label: 'Bags', link: '/blog/cssbuy-bags-2026-complete-guide-to-backpacks-crossbody-and-more' },
      { label: 'Belts', link: '/blog/cssbuy-belt-2026-complete-guide-to-affordable-style-essentials' },
      { label: 'Jewelry', link: '/blog/cssbuy-jewelry-2026-affordable-luxury-that-delivers-quality-and-style' },
      { label: 'Sunglasses', link: '/blog/cssbuy-sunglasses-2026-complete-guide-to-verified-eyewear' },
      { label: 'Watches', link: '/blog/cssbuy-watch-2026-complete-guide-to-affordable-luxury-timepieces' },
      { label: 'Wallets', link: '/blog/cssbuy-wallet-2026-complete-guide-to-verified-wallets-and-card-holders' }
    ]
  },
  {
    id: 'electronics',
    label: 'Electronics',
    overviewLink: '/electronics',
    items: [
      { label: 'Electronics', link: '/blog/cssbuy-electronics-2026-complete-guide-to-verified-tech-products' },
      { label: 'Phones', link: '/blog/cssbuy-phone-2026-complete-guide-to-mobile-devices-and-accessories' },
      { label: 'iPhone', link: '/blog/cssbuy-iphone-2026-complete-guide-to-verified-iphone-products-and-accessories' },
      { label: 'AirPods', link: '/blog/cssbuy-airpods-2026-complete-guide-to-verified-audio-deals' },
      { label: 'Tech Gadgets', link: '/blog/cssbuy-tech-gadgets-2026-complete-guide-to-electronics-and-smart-devices' }
    ]
  }
]

function isActive(link) {
  if (link === '/') return page.value?.relativePath === 'index.md'
  const path = page.value?.relativePath?.replace(/\.md$/, '') || ''
  return path === link.replace(/^\//, '') || path.startsWith(link.replace(/^\//, '') + '/')
}

function clearCloseTimer() {
  if (closeTimer) {
    clearTimeout(closeTimer)
    closeTimer = null
  }
}

function openOnHover(id) {
  clearCloseTimer()
  openMenu.value = id
}

function scheduleClose() {
  clearCloseTimer()
  closeTimer = setTimeout(() => {
    openMenu.value = null
    closeTimer = null
  }, 240)
}

function toggleMenu(id) {
  clearCloseTimer()
  openMenu.value = openMenu.value === id ? null : id
}

function closeMenus() {
  clearCloseTimer()
  openMenu.value = null
  mobileMenuOpen.value = false
}

onBeforeUnmount(clearCloseTimer)
</script>

<style scoped>
.global-navbar {
  position: sticky;
  top: 0;
  z-index: 100;
  border-bottom: 1px solid rgba(17, 17, 17, .09);
  background: rgba(255, 255, 255, .94);
  backdrop-filter: blur(14px);
}
.navbar-container {
  display: flex;
  align-items: center;
  width: min(1440px, calc(100% - 48px));
  min-height: 72px;
  margin: 0 auto;
  gap: 24px;
}
.navbar-brand {
  flex: 0 0 auto;
  color: #111;
  font-size: 17px;
  font-weight: 800;
  letter-spacing: -.045em;
  line-height: 1;
  text-decoration: none;
  white-space: nowrap;
}
.navbar-menu {
  display: flex;
  flex: 1;
  align-items: center;
  justify-content: center;
  gap: 18px;
  min-width: 0;
}
.nav-item, .nav-dropdown-trigger {
  padding: 8px 0;
  border: 0;
  background: transparent;
  color: #5e5e5e;
  font-family: inherit;
  font-size: 12px;
  font-weight: 700;
  line-height: 1;
  text-decoration: none;
  white-space: nowrap;
  cursor: pointer;
  transition: color .18s ease;
}
.nav-item:hover, .nav-item.active, .nav-dropdown-trigger:hover, .nav-dropdown-trigger[aria-expanded="true"] { color: #111; }
.nav-dropdown { position: relative; }
.chevron { display: inline-block; margin-left: 3px; color: #5b5ce2; font-size: 14px; transform: translateY(-1px); }
.dropdown-panel {
  position: absolute;
  top: 100%;
  left: 50%;
  display: none;
  width: max-content;
  min-width: 182px;
  max-width: 240px;
  padding: 9px;
  border: 1px solid #e8e8e8;
  border-radius: 11px;
  background: #fff;
  box-shadow: 0 18px 45px rgba(0,0,0,.11);
  transform: translateX(-50%);
}
.nav-dropdown:focus-within .dropdown-panel, .dropdown-panel.is-open { display: grid; }
.dropdown-title { margin: 5px 8px 7px; color: #939393; font-size: 10px; font-weight: 800; letter-spacing: .1em; text-transform: uppercase; }
.dropdown-panel a {
  display: flex;
 align-items: center; justify-content: space-between; gap: 24px; padding: 9px 8px; border-radius: 7px; color: #333; font-size: 13px; font-weight: 650; text-decoration: none; transition: background .16s ease, color .16s ease; }
.dropdown-panel a:hover { background: #f4f4ff; color: #393aa7; }
.dropdown-panel .dropdown-overview {
  margin-bottom: 5px;
  border-bottom: 1px solid #e9e9ed;
  background: #f7f7ff;
  color: #393aa7;
  font-weight: 800;
}
.dropdown-panel a span { color: #5b5ce2; }
.nav-cta {
  display: inline-flex;
  flex: 0 0 auto;
  align-items: center;
  gap: 7px;
  padding: 11px 15px;
  border-radius: 7px;
  background: #111;
  color: #fff;
  font-size: 13px;
  font-weight: 700;
  text-decoration: none;
  white-space: nowrap;
  transition: background .18s ease, transform .18s ease;
}
.nav-cta:hover { background: #5b5ce2; transform: translateY(-1px); }
.mobile-menu-toggle { display: none; }
@media (max-width: 1160px) {
  .navbar-container { width: min(100% - 36px, 1440px); gap: 15px; }
  .navbar-menu { gap: 12px; }
  .nav-item, .nav-dropdown-trigger { font-size: 11px; }
  .navbar-brand { font-size: 15px; }
  .nav-cta { padding: 10px 12px; font-size: 12px; }
}
@media (max-width: 920px) {
  .navbar-container { position: relative; min-height: 64px; }
  .mobile-menu-toggle { display: inline-flex; align-items: center; gap: 7px; margin-left: auto; padding: 8px 0; border: 0; background: transparent; color: #111; font-family: inherit; font-size: 12px; font-weight: 800; cursor: pointer; }
  .navbar-menu { position: absolute; top: calc(100% + 1px); left: 0; right: 0; display: none; max-height: calc(100vh - 78px); overflow-y: auto; padding: 12px; border: 1px solid #e8e8e8; border-radius: 0 0 12px 12px; background: #fff; box-shadow: 0 18px 35px rgba(0,0,0,.12); }
  .navbar-menu.is-mobile-open { display: flex; flex-direction: column; align-items: stretch; gap: 0; }
  .nav-item, .nav-dropdown-trigger { display: flex; align-items: center; justify-content: space-between; width: 100%; padding: 13px 10px; font-size: 14px; text-align: left; }
  .nav-dropdown { width: 100%; border-top: 1px solid #f0f0f0; }
  .dropdown-panel { position: static; width: 100%; max-width: none; margin: 0 0 8px; border: 0; border-radius: 8px; box-shadow: none; background: #f7f7f5; transform: none; }
  .dropdown-panel.is-open, .nav-dropdown:focus-within .dropdown-panel { display: grid; }
  .dropdown-panel a { padding: 10px 12px; }
  .nav-cta { margin-left: 0; }
}
@media (max-width: 520px) {
  .navbar-container { width: min(100% - 28px, 1440px); gap: 12px; }
  .navbar-brand { max-width: 170px; overflow: hidden; text-overflow: ellipsis; }
  .nav-cta { display: none; }
}
</style>
