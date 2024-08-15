# Personal Web Page Template

This project is a customizable template for creating a personal web page using Streamlit. It is designed to showcase your portfolio, skills, and contact information in a clean and modern layout.

## Features

- **Responsive Design:** Adapts to different screen sizes for a seamless experience across devices.
- **Custom CSS:** Easily change the look and feel of your site with custom styles.
- **Portfolio Section:** Showcase your projects with descriptions and links.
- **Skills Section:** Highlight your technical skills.
- **Contact Information:** Provide your contact details and links to your social profiles.

## Dependencies

Make sure you have Python installed and the necessary libraries. You can install the required packages using pip:

```bash
pip install streamlit pillow requests beautifulsoup4
```

## How to Use

1. **Clone the Repository:**

2. **Customize the Content:**

   - Update the profile picture by replacing `DSC_6406-modified.png` with your own image.
   - Modify the title and subtitle in the main content section to reflect your own name and profession.
   - Edit the "About Me" section with your own summary.
   - Customize the skills list with your own skills in the `skills` variable.
   - Add or modify the portfolio items in the "My Portfolio" section by updating the GitHub repository URLs.

3. **Run the Web Page:**

   Launch the Streamlit app by running the following command in your terminal:

   ```bash
   streamlit run app.py
   ```

   This will open your personal web page in your default web browser.

## Customization

You can further customize the appearance and content of your web page by editing the Streamlit code:

- **Page Configuration:** Change the page title, icon, and layout by modifying the `st.set_page_config` function.
- **CSS Styling:** Adjust the visual styling in the `st.markdown` block containing the custom CSS.
- **Sidebar:** Add, remove, or modify the navigation links in the sidebar to match your sections.
- **Portfolio Section:** Update the `fetch_github_repo_info` and `scrape_pinned_repos` functions to automatically fetch your latest GitHub projects.

## Deploying

To share your personal web page with others, you can deploy it using Streamlit Cloud:

1. **Deploy to Streamlit Cloud:**
   
   - Commit and push your changes to GitHub.
   - Sign in to [Streamlit Cloud](https://share.streamlit.io/) and connect your repository.
   - Deploy your app directly from Streamlit Cloud.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This version reflects that the project was deployed using Streamlit Cloud. You can paste this directly into a Markdown cell.
