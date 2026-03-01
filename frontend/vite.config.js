import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    manifest: true,
    outDir: '../staticfiles',
    lib: {
      entry: 'js/app.js',
      name: 'app',
      fileName: 'app'
    },
    rollupOptions: {
      external: []
    }
  }
})