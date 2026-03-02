import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    manifest: true,
    outDir: '../staticfiles',
    rollupOptions: {
      input: 'js/app.js'
    }
  }
})