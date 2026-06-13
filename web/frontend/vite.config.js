import { defineConfig } from 'vite'
import { createVuePlugin } from 'vite-plugin-vue2'

export default defineConfig({
  plugins: [createVuePlugin()],
  server: {
    host: '127.0.0.1',
    port: 40211,
    strictPort: true,
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:28932',
        changeOrigin: false
      }
    }
  },
  build: {
    outDir: 'dist',
    emptyOutDir: true
  }
})
