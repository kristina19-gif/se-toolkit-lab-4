import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      // Когда фронтенд просит '/items', Vite перенаправит это на бэкенд
      '/items': {
        target: 'http://127.0.0.1:42000',
        changeOrigin: true,
        secure: false,
      },
    },
  },
})