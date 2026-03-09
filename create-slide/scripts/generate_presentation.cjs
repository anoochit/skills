const fs = require('fs');
const path = require('path');

function generateHtml(data, templatePath) {
    let template = fs.readFileSync(templatePath, 'utf8');

    const slidesHtml = data.slides.map(slide => {
        let content = '';
        if (slide.type === 'title') {
            content = `<h1>${slide.title}</h1>`;
            if (slide.subtitle) {
                content += `<h3>${slide.subtitle}</h3>`;
            }
        } else if (slide.type === 'bullets') {
            content = `<h2>${slide.title}</h2>`;
            content += '<ul>' + slide.bullets.map(b => `<li>${b}</li>`).join('') + '</ul>';
        } else if (slide.type === 'chart') {
            content = `<h2>${slide.title}</h2>`;
            const chartId = `chart-${Math.random().toString(36).substr(2, 9)}`;
            content += `<div class="chart-container"><canvas id="${chartId}"></canvas></div>`;
            const chartConfig = JSON.stringify(slide.chartConfig);
            content += `<script>
                (function() {
                    const ctx = document.getElementById('${chartId}').getContext('2d');
                    new Chart(ctx, ${chartConfig});
                })();
            </script>`;
        } else if (slide.type === 'content') {
            content = `<h2>${slide.title}</h2>`;
            content += `<p>${slide.content}</p>`;
        } else if (slide.type === 'raw') {
            content = slide.content;
        }

        return `<section>${content}</section>`;
    }).join('\n');

    template = template.replace('<!-- Slides will be injected here -->', slidesHtml);
    template = template.replace('<title>Reveal.js Presentation</title>', `<title>${data.title || 'Presentation'}</title>`);

    return template;
}

if (require.main === module) {
    const args = process.argv.slice(2);
    if (args.length < 2) {
        console.error('Usage: node generate_presentation.cjs <json-data-path> <output-path>');
        process.exit(1);
    }

    const dataPath = args[0];
    const outputPath = args[1];
    const templatePath = path.join(__dirname, '..', 'references', 'template.html');

    try {
        const data = JSON.parse(fs.readFileSync(dataPath, 'utf8'));
        const html = generateHtml(data, templatePath);
        fs.writeFileSync(outputPath, html);
        console.log(`Successfully generated presentation: ${outputPath}`);
    } catch (err) {
        console.error(`Error: ${err.message}`);
        process.exit(1);
    }
}
