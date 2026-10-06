#!/usr/bin/env python3
"""
Build AI Projects HTML from Markdown
This script reads projects.md and generates a static ai-projects.html file
with all projects baked in.
"""

import re
import os
from pathlib import Path


class MarkdownProjectParser:
    """Parse markdown project format and generate HTML"""

    def __init__(self, markdown_file='projects.md'):
        self.markdown_file = markdown_file
        self.projects = []

    def read_markdown(self):
        """Read the markdown file"""
        try:
            with open(self.markdown_file, 'r', encoding='utf-8') as f:
                content = f.read()
            return content
        except FileNotFoundError:
            print(f"Error: {self.markdown_file} not found")
            return None

    def parse_projects(self, markdown_content):
        """Parse markdown content into project objects"""
        # Split by project separator (---)
        sections = markdown_content.split('---')

        for section in sections:  # Skip first section (header)
            section = section.strip()
            if not section:
                continue

            project = self._parse_project_section(section)
            if project['title']:
                self.projects.append(project)

    def _parse_project_section(self, section):
        """Parse individual project section"""
        lines = section.split('\n')
        project = {
            'title': '',
            'date': '',
            'description': '',
            'technologies': [],
            'links': []
        }

        description_lines = []

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Extract title
            if line.startswith('## '):
                project['title'] = line.replace('## ', '', 1).strip()

            # Extract date
            elif line.startswith('**Date:**'):
                project['date'] = line.replace('**Date:**', '', 1).strip()

            # Extract technologies
            elif line.startswith('**Technologies:**'):
                tech_string = line.replace('**Technologies:**', '', 1).strip()
                project['technologies'] = [t.strip() for t in tech_string.split(',')]

            # Extract links
            elif line.startswith('**Links:**'):
                links_string = line.replace('**Links:**', '', 1).strip()
                # Parse markdown links: [text](url)
                link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
                matches = re.findall(link_pattern, links_string)
                project['links'] = [{'text': text, 'url': url} for text, url in matches]

            # Add to description
            elif line and not line.startswith('**'):
                description_lines.append(line)

        project['description'] = ' '.join(description_lines).strip()
        return project

    def generate_project_html(self, project):
        """Generate HTML for a single project card"""
        # Escape HTML special characters
        title = self._escape_html(project['title'])
        date = self._escape_html(project['date'])
        description = self._escape_html(project['description'])

        # Generate technology tags
        tags_html = ''
        for tech in project['technologies']:
            # Multi-word techs are secondary tags
            tag_class = 'tag secondary' if ' ' in tech else 'tag'
            tags_html += f'<span class="{tag_class}">{self._escape_html(tech)}</span>\n'

        # Generate links
        links_html = ''
        if project['links']:
            for link in project['links']:
                links_html += f'<a href="{self._escape_html(link["url"])}" target="_blank">{self._escape_html(link["text"])}</a>\n'
            links_html = f'<div class="project-links">\n{links_html}</div>\n'

        html = f'''            <div class="project-card">
                <div class="project-header">
                    <div class="project-title">{title}</div>
                    <div class="project-date">{date}</div>
                </div>
                <p class="project-description">
                    {description}
                </p>
                <div class="tech-stack">
                    <strong>Technologies:</strong>
                    <div class="tags">
{tags_html}                    </div>
                </div>
{links_html}            </div>
'''
        return html

    def generate_all_projects_html(self):
        """Generate HTML for all projects"""
        html = ''
        for project in self.projects:
            html += self.generate_project_html(project)
        return html

    @staticmethod
    def _escape_html(text):
        """Escape HTML special characters"""
        if not text:
            return text
        return (text
                .replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;')
                .replace('"', '&quot;')
                .replace("'", '&#39;'))


class HTMLBuilder:
    """Build the complete HTML file"""

    def __init__(self, html_template_file='ai-projects-template.html'):
        self.template_file = html_template_file
        self.projects_placeholder = '<!-- PROJECTS_WILL_BE_INSERTED_HERE -->'

    def get_html_template(self):
        """Get the base HTML template without projects"""
        # Return the template HTML with placeholder for projects
        return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Projects - Sudhir Varanasi</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary-color: #1a3a52;
            --accent-color: #2563eb;
            --success-color: #10b981;
            --warning-color: #f59e0b;
            --text-dark: #1f2937;
            --text-light: #6b7280;
            --border-color: #e5e7eb;
            --bg-light: #ffffff;
            --bg-darker: #f9fafb;
        }

        @media (prefers-color-scheme: dark) {
            :root {
                --text-dark: #f3f4f6;
                --text-light: #d1d5db;
                --border-color: #374151;
                --bg-light: #111827;
                --bg-darker: #1f2937;
            }
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: var(--text-dark);
            background-color: var(--bg-light);
            padding: 20px;
        }

        .container {
            max-width: 900px;
            margin: 0 auto;
        }

        /* Header */
        header {
            margin-bottom: 40px;
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 30px;
        }

        .header-top {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 20px;
            flex-wrap: wrap;
            gap: 20px;
        }

        .name-title h1 {
            font-size: 2.5em;
            color: var(--primary-color);
            margin-bottom: 5px;
        }

        .name-title p {
            font-size: 1.2em;
            color: var(--text-light);
        }

        .nav-links {
            display: flex;
            gap: 20px;
            margin-top: 15px;
            flex-wrap: wrap;
        }

        .nav-links a {
            color: var(--accent-color);
            text-decoration: none;
            padding: 8px 16px;
            border: 1px solid var(--accent-color);
            border-radius: 4px;
            transition: all 0.3s ease;
        }

        .nav-links a:hover {
            background-color: var(--accent-color);
            color: white;
        }

        /* Section Styling */
        section {
            margin-bottom: 40px;
        }

        h2 {
            font-size: 1.8em;
            color: var(--primary-color);
            margin-bottom: 25px;
            padding-bottom: 10px;
            border-bottom: 2px solid var(--accent-color);
        }

        h3 {
            font-size: 1.3em;
            color: var(--text-dark);
            margin-bottom: 10px;
        }

        /* Project Card */
        .project-card {
            background-color: var(--bg-darker);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 25px;
            margin-bottom: 25px;
            transition: all 0.3s ease;
        }

        .project-card:hover {
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.15);
            transform: translateY(-2px);
        }

        .project-header {
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            flex-wrap: wrap;
            gap: 15px;
            margin-bottom: 12px;
        }

        .project-title {
            font-size: 1.25em;
            color: var(--text-dark);
            font-weight: 600;
        }

        .project-date {
            color: var(--text-light);
            font-size: 0.95em;
            white-space: nowrap;
        }

        .project-description {
            color: var(--text-light);
            margin: 12px 0;
            line-height: 1.8;
        }

        .tech-stack {
            margin-top: 15px;
        }

        .tech-stack strong {
            color: var(--text-dark);
            display: block;
            margin-bottom: 8px;
        }

        .tags {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }

        .tag {
            display: inline-block;
            padding: 4px 12px;
            background-color: var(--accent-color);
            color: white;
            border-radius: 20px;
            font-size: 0.85em;
            font-weight: 500;
        }

        .tag.secondary {
            background-color: var(--success-color);
        }

        .tag.highlight {
            background-color: var(--warning-color);
            color: #1f2937;
        }

        .project-links {
            margin-top: 15px;
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }

        .project-links a {
            color: var(--accent-color);
            text-decoration: none;
            padding: 6px 12px;
            border: 1px solid var(--accent-color);
            border-radius: 4px;
            font-size: 0.95em;
            transition: all 0.3s ease;
        }

        .project-links a:hover {
            background-color: var(--accent-color);
            color: white;
        }

        /* Footer */
        footer {
            text-align: center;
            padding-top: 20px;
            border-top: 2px solid var(--border-color);
            color: var(--text-light);
            font-size: 0.9em;
            margin-top: 40px;
        }

        footer a {
            color: var(--accent-color);
            text-decoration: none;
        }

        footer a:hover {
            text-decoration: underline;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .header-top {
                flex-direction: column;
            }

            .name-title h1 {
                font-size: 2em;
            }

            h2 {
                font-size: 1.5em;
            }

            .project-header {
                flex-direction: column;
                align-items: flex-start;
            }
        }

        /* Print styles */
        @media print {
            body {
                padding: 0;
            }

            .nav-links {
                display: none;
            }

            a {
                color: inherit;
                text-decoration: none;
            }
        }

        .info-box {
            background-color: var(--bg-darker);
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid var(--success-color);
            margin-bottom: 20px;
        }

        .info-box strong {
            color: var(--text-dark);
        }

        .info-box p {
            color: var(--text-light);
            margin: 10px 0;
        }

        code {
            background-color: rgba(0, 0, 0, 0.1);
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <header>
            <div class="header-top">
                <div class="name-title">
                    <h1>AI Projects Portfolio</h1>
                    <p>Machine Learning & Artificial Intelligence Applications</p>
                </div>
            </div>
            <div class="nav-links">
                <a href="index.html">← Back to Main Resume</a>
                <a href="#projects">Projects</a>
            </div>
        </header>

        <!-- Introduction -->
        <section id="intro">
            <div class="info-box">
                <p>
                    <strong>Welcome to my AI Projects Portfolio.</strong> This page showcases my work in artificial intelligence,
                    machine learning, and advanced data analytics. Projects range from agentic AI systems and LLMOps implementations
                    to scientific machine learning applications and deep learning research.
                </p>
            </div>
        </section>

        <!-- Projects Section -->
        <section id="projects">
            <h2>🤖 Featured Projects</h2>
{projects_html}        </section>

        <!-- Footer -->
        <footer>
            <p>
                <a href="index.html">← Back to Main Resume</a>
            </p>
            <p style="margin-top: 15px;">
                Last updated: October 2026 | Built with HTML5 & CSS3 | Hosted on GitHub Pages
            </p>
        </footer>
    </div>
</body>
</html>'''

    def build(self, projects_html, output_file='ai-projects.html'):
        """Build the final HTML file"""
        template = self.get_html_template()
        final_html = template.replace('{projects_html}', projects_html)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(final_html)

        return output_file


def main():
    """Main function to build AI projects HTML"""
    print("🚀 Building AI Projects HTML from Markdown...")

    # Check if projects.md exists
    if not os.path.exists('projects.md'):
        print("❌ Error: projects.md not found in current directory")
        print("Please ensure projects.md is in the same directory as this script")
        return False

    # Parse markdown
    print("📖 Reading projects.md...")
    parser = MarkdownProjectParser('projects.md')
    markdown_content = parser.read_markdown()

    if markdown_content is None:
        return False

    parser.parse_projects(markdown_content)
    print(f"✅ Found {len(parser.projects)} projects")

    # Generate HTML
    print("🎨 Generating project HTML...")
    projects_html = parser.generate_all_projects_html()

    # Build final HTML file
    print("📝 Building ai-projects.html...")
    builder = HTMLBuilder()
    output_file = builder.build(projects_html)

    print(f"✅ Success! Generated {output_file}")
    print(f"\n📊 Project Summary:")
    for i, project in enumerate(parser.projects, 1):
        print(f"  {i}. {project['title']} ({project['date']})")

    return True


if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)
