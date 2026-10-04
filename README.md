# Sudhir Varanasi - Professional Resume Website

A clean, professional, and responsive HTML resume website optimized for GitHub Pages with an integrated AI projects portfolio.

## 📁 Files Overview

- **`index.html`** - Main resume page with professional experience, skills, education, and contact information
- **`ai-projects.html`** - Dedicated portfolio page for AI/ML projects (easily extensible)
- **`README.md`** - This file with setup and maintenance instructions

## ✨ Features

### Design & Usability
- **Responsive Design**: Adapts perfectly to desktop, tablet, and mobile devices
- **Dark Mode Support**: Automatically respects system color scheme preferences
- **Professional Typography**: Clean, readable fonts with optimal spacing
- **Print-Friendly**: Both pages print beautifully for traditional resumes
- **Fast Loading**: Pure HTML & CSS with no external dependencies

### Content Organization
- **Main Resume**: Comprehensive professional history from ISRO to Rolls-Royce
- **Skills Dashboard**: Organized technical skills across 4 major categories
- **AI Projects Portfolio**: Dedicated space for showcasing ML and AI work
- **Easy Navigation**: Cross-linking between main resume and AI projects page

### Maintainability
- **Template-Based Updates**: Clear structure for adding/removing content
- **No Build Tools Required**: Edit directly with any text editor
- **Self-Documenting**: Instructions included in HTML for adding projects
- **Easy Customization**: Centralized CSS variables for quick color/style changes

## 🚀 Getting Started with GitHub Pages

### Option 1: Using GitHub Web Interface
1. Create a new GitHub repository named `sudhir-varanasi.github.io` (replace with your GitHub username)
2. Go to your repository settings
3. Upload `index.html` and `ai-projects.html` files
4. Your site will be live at `https://sudhir-varanasi.github.io`

### Option 2: Using Git Command Line
```bash
# Clone your GitHub Pages repository
git clone https://github.com/yourusername/yourusername.github.io
cd yourusername.github.io

# Copy the HTML files
cp path/to/index.html .
cp path/to/ai-projects.html .

# Commit and push
git add .
git commit -m "Add resume website"
git push origin main
```

### Option 3: Using GitHub Desktop
1. Clone your GitHub Pages repository to your computer
2. Copy `index.html` and `ai-projects.html` into the repository folder
3. Open GitHub Desktop, commit the changes with a message like "Add resume website"
4. Click "Push to origin"
5. Your site goes live in 1-2 minutes

## 📝 How to Update Your Resume

### Editing Content in `index.html`

The structure is organized into clear sections:

```html
<!-- Professional Summary Section -->
<section id="professional-summary">
    <h2>Professional Summary</h2>
    <p class="summary-text">Your summary here...</p>
</section>

<!-- Experience Section -->
<div class="job">
    <div class="job-header">
        <div class="job-company">Company Name</div>
        <div class="job-title">Your Job Title</div>
    </div>
    <div class="job-description">
        <ul>
            <li>Achievement or responsibility</li>
        </ul>
    </div>
</div>
```

### Common Updates

**Update Contact Information:**
```html
<div class="contact-info">
    <div>📍 Your Location</div>
    <div>📞 Your Phone</div>
    <div><a href="mailto:your.email@gmail.com">✉️ Your Email</a></div>
    <div><a href="https://linkedin.com/in/your-profile" target="_blank">💼 LinkedIn</a></div>
</div>
```

**Add a New Job Experience:**
```html
<div class="job">
    <div class="job-header">
        <div>
            <div class="job-company">Company Name</div>
            <div class="job-title">Job Title</div>
        </div>
        <div class="job-dates">Start Month Year – End Month Year</div>
    </div>
    <p style="color: var(--text-light); font-size: 0.95em;">Location</p>
    <div class="job-description">
        <ul>
            <li>Key accomplishment or responsibility</li>
            <li>Another achievement</li>
        </ul>
    </div>
</div>
```

**Update Education:**
```html
<div class="education-item">
    <div class="degree">Degree Name</div>
    <div class="institution">University Name — Year</div>
    <div class="grade">GPA or Score</div>
</div>
```

## 🤖 How to Add AI Projects

See the **AI Projects Portfolio** section in `ai-projects.html` for detailed instructions. Quick summary:

### Project Card Template

```html
<div class="project-card">
    <div class="project-header">
        <div class="project-title">Your Project Title</div>
        <div class="project-date">2024 - 2025</div>
    </div>
    <p class="project-description">
        Describe your project in 2-3 sentences. What problem did it solve? 
        What techniques or approaches did you use?
    </p>
    <div class="tech-stack">
        <strong>Technologies:</strong>
        <div class="tags">
            <span class="tag">Technology 1</span>
            <span class="tag">Technology 2</span>
            <span class="tag secondary">Category Tag</span>
            <span class="tag highlight">Important Tag</span>
        </div>
    </div>
    <div class="project-links">
        <a href="https://github.com/yourrepo" target="_blank">GitHub</a>
        <a href="https://yourproject.com" target="_blank">Demo</a>
    </div>
</div>
```

### Tag Styles
- `.tag` - Blue, for technologies (PyTorch, Python, LangChain, etc.)
- `.tag.secondary` - Green, for categories (RAG, SciML, Agentic AI, etc.)
- `.tag.highlight` - Amber, for important concepts (Multi-Agent, Optimization, etc.)

## 🎨 Customizing Appearance

All colors are defined as CSS variables at the top of each HTML file. To change the color scheme, edit the `:root` section:

```css
:root {
    --primary-color: #1a3a52;      /* Dark blue for headings */
    --accent-color: #2563eb;       /* Blue for links and highlights */
    --success-color: #10b981;      /* Green for secondary tags */
    --warning-color: #f59e0b;      /* Amber for highlight tags */
    --text-dark: #1f2937;
    --text-light: #6b7280;
    --border-color: #e5e7eb;
    --bg-light: #ffffff;
    --bg-darker: #f9fafb;
}
```

## 💻 Local Preview

To preview your changes locally before pushing to GitHub:

1. **Windows**: Double-click the HTML file to open it in your default browser
2. **Mac/Linux**: Open Terminal and run:
   ```bash
   # Navigate to the directory
   cd path/to/resume
   
   # Start a local server (Python 3)
   python -m http.server 8000
   
   # Then visit http://localhost:8000 in your browser
   ```
3. **VS Code**: Use the "Live Server" extension for instant preview with auto-reload

## 🔍 Browser Compatibility

- ✅ Chrome/Edge (Latest)
- ✅ Firefox (Latest)
- ✅ Safari (Latest)
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)
- ✅ Print to PDF

## 📱 Mobile Optimization

The design is fully responsive:
- **Desktop** (900px+): Multi-column layouts, full navigation
- **Tablet** (768px-900px): Adjusted spacing and font sizes
- **Mobile** (<768px): Single-column layout, touch-friendly buttons

## ⚡ Performance

- **No External Dependencies**: Pure HTML & CSS (no jQuery, Bootstrap, etc.)
- **Fast Load Time**: All-in-one file, minimal CSS
- **SEO Friendly**: Proper semantic HTML structure
- **Accessibility**: Semantic headings, readable color contrast, proper alt attributes

## 🔐 Privacy & Security

- No tracking or analytics code
- No external resources loaded from CDNs
- No cookies or local storage
- Safe to use on any device

## 📊 SEO Optimization

To improve search engine visibility, update the meta tags in the `<head>` section:

```html
<meta name="description" content="Your professional summary">
<meta name="keywords" content="software engineer, CAE, automation, AI, machine learning">
<meta name="author" content="Sudhir Varanasi">
```

## 🆘 Troubleshooting

### Site not appearing on GitHub
- Ensure your repository is named `yourusername.github.io`
- Wait 1-2 minutes for GitHub to build the site
- Check repository settings > Pages to ensure it's enabled

### Links not working
- Ensure both `index.html` and `ai-projects.html` are in the same directory
- Test links locally before pushing to GitHub

### Dark mode not working
- This is system-dependent (Settings > Display > Dark Mode)
- Both light and dark versions are automatically applied

## 📧 Contact & Support

For issues or questions about the resume website, refer to the main `index.html` file for contact information.

---

**Version**: 1.0  
**Last Updated**: October 2026  
**Status**: Ready for Production
