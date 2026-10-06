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

### Maintainability
- **Template-Based Updates**: Clear structure for adding/removing content
- **No Build Tools Required**: Edit directly with any text editor
- **Self-Documenting**: Instructions included in HTML for adding projects
- **Easy Customization**: Centralized CSS variables for quick color/style changes

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

### Update project.md file following the template syntax. ai-projects.html file will be build using project.md file content. 


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
- **Accessibility**: Semantic headings, readable color contrast, proper alt attributes

## 🔐 Privacy & Security

- No tracking or analytics code
- No external resources loaded from CDNs
- No cookies or local storage
- Safe to use on any device

