module.exports = {
  content: [
    "./src/**/*.{html,js,vue}",  // Adjust paths to match your files
  ],
  safelist: [
    {
      pattern: /^sheet-/ // Keeps all classes starting with "sheet-"
    }
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
