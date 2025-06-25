// wall paper 
const fs = require("fs");
const { createCanvas } = require("canvas");

// Wallpaper settings
const width = 1080;
const height = 1920;
const outputDir = "output";
const totalWallpapers = 10;

// Ensure output directory exists
if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir);
}

function getRandomColor(hueOffset = 0) {
  const hue = Math.floor(Math.random() * 360 + hueOffset);
  return `hsl(${hue}, 70%, 50%)`;
}

function drawWallpaper(index) {
  const canvas = createCanvas(width, height);
  const ctx = canvas.getContext("2d");

  // Gradient background
  const gradient = ctx.createLinearGradient(0, 0, 0, height);
  gradient.addColorStop(0, getRandomColor());
  gradient.addColorStop(1, getRandomColor(180));
  ctx.fillStyle = gradient;
  ctx.fillRect(0, 0, width, height);

  // Decorative glowing circles
  for (let i = 0; i < 40; i++) {
    const x = Math.random() * width;
    const y = Math.random() * height;
    const radius = Math.random() * 80 + 30;
    ctx.beginPath();
    ctx.arc(x, y, radius, 0, Math.PI * 2);
    ctx.fillStyle = `hsla(${Math.random() * 360}, 100%, 75%, 0.05)`;
    ctx.fill();
  }

  // Centered text
  ctx.fillStyle = "white";
  ctx.font = "bold 72px Sans";
  ctx.textAlign = "center";
  ctx.fillText(`Wallpaper #${index + 1}`, width / 2, height / 2);

  // Export to file
  const buffer = canvas.toBuffer("image/png");
  fs.writeFileSync(`${outputDir}/wallpaper_${index + 1}.png`, buffer);
  console.log(`✅ Saved: wallpaper_${index + 1}.png`);
}

// Generate batch
for (let i = 0; i < totalWallpapers; i++) {
  drawWallpaper(i);
}
