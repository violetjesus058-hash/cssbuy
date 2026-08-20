<template>
  <header v-if="isArticle" class="article-page-header">
    <h1>{{ articleTitle }}</h1>
    <div class="article-actions" role="group" aria-label="Article actions">
      <component
        :is="shoppingLinked ? 'a' : 'span'"
        :href="shoppingLinked ? shoppingUrl : undefined"
        :target="shoppingLinked ? '_blank' : undefined"
        :rel="shoppingLinked ? 'nofollow noopener noreferrer' : undefined"
        :aria-disabled="shoppingLinked ? undefined : 'true'"
        class="article-action article-action-secondary"
        :class="{ 'is-unlinked': !shoppingLinked }"
      >
        Start shopping
      </component>
    </div>
  </header>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useData, useRoute } from 'vitepress'

const { frontmatter } = useData()
const route = useRoute()

const shoppingUrl = 'https://repsootd.com/'
const isArticle = computed(() => route.path.startsWith('/blog/') && route.path !== '/blog/' && frontmatter.value.articleHeader !== false)
const articleTitle = computed(() => frontmatter.value.title || 'CSSBuy Guide')

/* Set either field to false in an article's frontmatter to render that control without a link. */
const shoppingLinked = computed(() => frontmatter.value.shoppingLink !== false)
</script>
