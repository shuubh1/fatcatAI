import tailwindcss from '@tailwindcss/vite';
import react from '@vitejs/plugin-react';
import path from 'path';
import {defineConfig} from 'vite';

export default defineConfig(() => {
  return {
    plugins: [react(), tailwindcss()],
    resolve: {
      alias: {
        '@': path.resolve(__dirname, '.'),
      },
    },
    server: {
      port: 3000,
      host: '0.0.0.0',
      // HMR is disabled in AI Studio via DISABLE_HMR env var.
      hmr: process.env.DISABLE_HMR !== 'true',
      // Disable file watching when DISABLE_HMR is true to save CPU during agent edits.
      watch: process.env.DISABLE_HMR === 'true' ? null : {},
    },
    build: {
      rollupOptions: {
        input: {
          main: path.resolve(__dirname, 'index.html'),
          contact: path.resolve(__dirname, 'contact.html'),
          blogAudit: path.resolve(__dirname, 'blog-ai-visibility-audit.html'),
          blogFintech: path.resolve(__dirname, 'blog-geo-fintech.html'),
          blogCited: path.resolve(__dirname, 'blog-how-to-get-cited-by-ai.html'),
          blogSeoVsGeo: path.resolve(__dirname, 'blog-seo-vs-geo.html'),
          blogInvisible: path.resolve(__dirname, 'blog-why-invisible-to-chatgpt.html'),
          googleVerify: path.resolve(__dirname, 'googlefa06e48f95ad9e51.html'),
        },
      },
    },
  };
});
