/** Tailwind build for the UTS prototype. Run: python build.py */
module.exports = {
  content: ["./src/index.src.html"],
  theme: {
    extend: {
      fontFamily: { sans: ["Roboto", "Segoe UI", "Arial", "sans-serif"] },
      // Blue scale tuned to the Bayt.com brand blue (#007AFF) so every component picks it up.
      colors: {
        blue: {
          50: "#EEF6FF", 100: "#DCEBFF", 200: "#B9D8FF", 300: "#8CC0FF", 400: "#4DA0FF",
          500: "#1F88FF", 600: "#007AFF", 700: "#0062CC", 800: "#004FA3", 900: "#003A78",
        },
        bayt: { yellow: "#F6BB2D" },
      },
    },
  },
};
