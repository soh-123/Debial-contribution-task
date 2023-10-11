import unittest
from wiki import fetch_webpage_content, convert_to_markdown


class TestWiki(unittest.TestCase):
    def test_fetch_webpage_content(self):
        wiki_url = "https://wiki.debian.org/News"
        content_element = fetch_webpage_content(wiki_url)
        self.assertIsNotNone(content_element)
        self.assertIn('Debian has several news feeds', content_element)

    def test_convert_to_markdown(self):
        sample_html = """
        <h2 id="News_for_Debian_contributors">News for Debian contributors</h2>
        <span class="anchor" id="line-23"></span>
        <span class="anchor" id="line-24"></span>
        <dl>
            <dt>#debian-devel IRC channel topic </dt>
            <dd>
                <p class="line862">Current issues regarding Debian Project and Debian/<a
                        href="https://wiki.debian.org/DebianUnstable">Unstable</a>. <small><br />
                        <a class="ircs" href="ircs://irc.debian.org/#debian-devel">#debian-devel</a> topic is also available at
                        <a href="https://wiki.debian.org/DevelopersCorner">DevelopersCorner</a>.</small> <span class="anchor"
                        id="line-25"></span><span class="anchor" id="line-26"></span></p>
            </dd>
            <dt>debian-devel-announce </dt>
            <dd>
                <p class="line862">Announcements for <em>"developers"</em> (like policy changes, important release issues, teams
                    news). <small><br />
                        <a class="interwiki" href="https://lists.debian.org/debian-devel-announce"
                            title="DebianList">debian-devel-announce</a> (<a
                            href="https://wiki.debian.org/DeveloperNews">contribute</a>).</small> <span class="anchor"
                        id="line-27"></span><span class="anchor" id="line-28"></span></p>
        """
        file_name = "test_output"
        convert_to_markdown(sample_html, file_name)
        with open(f"{file_name}.md", "r", encoding="utf-8") as markdown_file:
            markdown_content = markdown_file.read()
            self.assertIn("#debian-devel IRC channel topic", markdown_content)
            self.assertIn(
                "[Unstable](https://wiki.debian.org/DebianUnstable)", markdown_content)


if __name__ == "__main__":
    unittest.main()
