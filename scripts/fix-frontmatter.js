/**
 * Fix files that start with --- but have no closing ---
 * Remove the leading --- line from these files
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const BLOG_DIR = path.resolve(__dirname, '..', 'blog');

const brokenFiles = [
  'cssbuy-consolidation-guide.md',
  'cssbuy-dashboard-guide.md',
  'cssbuy-delivery-guide.md',
  'cssbuy-first-order.md',
  'cssbuy-getting-started.md',
  'cssbuy-how-to-buy.md',
  'cssbuy-how-to-order.md',
  'cssbuy-new-user-guide.md',
  'cssbuy-order-guide.md',
  'cssbuy-ordering-process.md',
  'cssbuy-payment-guide.md',
  'cssbuy-platform-guide.md',
  'cssbuy-purchase-guide.md',
  'cssbuy-registration-guide.md',
  'cssbuy-shipping-methods.md',
  'cssbuy-shipping-options.md',
  'cssbuy-shopping-guide.md',
  'cssbuy-top-up-guide.md',
  'cssbuy-warehouse-guide.md',
];

let fixed = 0;
for (const file of brokenFiles) {
  const filePath = path.join(BLOG_DIR, file);
  let content = fs.readFileSync(filePath, 'utf-8');

  // Remove leading ---\n
  if (content.startsWith('---\n')) {
    content = content.substring(4); // remove '---\n'
    fs.writeFileSync(filePath, content, 'utf-8');
    fixed++;
    console.log(`Fixed: ${file}`);
  }
}

console.log(`\nFixed ${fixed} files`);
