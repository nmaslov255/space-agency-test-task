import { resolve } from 'path';
import { defineConfig } from 'vite';


export default defineConfig({
  root: resolve(__dirname, 'src'),
  build: {
    manifest: true,
    outDir: resolve(__dirname, '../staticfiles'),
    rollupOptions: {
      input: resolve(__dirname, 'src/js/main.js'),
    },
  },
  css: {
    preprocessorOptions: {
      scss: {
        silenceDeprecations: [
          'import',
          'mixed-decls',
          'color-functions',
          'global-builtin',
        ],
      },
    },
  },
})