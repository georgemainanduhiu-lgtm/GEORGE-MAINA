# Soccer Heroes Who Never Gave Up

**12 True Stories of Courage, Teamwork, and Big Dreams for Kids Ages 8–12**

A ~30,000-word children's nonfiction ebook, ready for Amazon Kindle (KDP).

## The 12 heroes

| # | Chapter | Never-give-up theme |
|---|---------|--------------------|
| 1 | Lionel Messi: *The Boy Who Was Too Small* | Growth-hormone treatment, four lost finals, World Cup glory |
| 2 | Cristiano Ronaldo: *The Island Boy Who Outworked Everyone* | Leaving home at 12, heart surgery, work ethic |
| 3 | Luka Modrić: *From War Refugee to the Best in the World* | War, rejection, "worst signing," Ballon d'Or |
| 4 | Mohamed Salah: *The Long Bus Ride to Glory* | Hours of bus rides, the Chelsea bench, Egyptian King |
| 5 | Kylian Mbappé: *The Kid with Posters on His Wall* | Penalty miss, 2022 final hat-trick, all-time World Cup scorer |
| 6 | Ousmane Dembélé: *The Comeback Kid* | Injuries and criticism, then the 2025 Ballon d'Or |
| 7 | Vinícius Júnior: *Keep Dancing* | "Can't shoot," standing up to racism |
| 8 | Erling Haaland: *The Late Bloomer from Bryne* | 16 games without a goal, Norway's best World Cup |
| 9 | Bukayo Saka: *The Penalty That Didn't Break Him* | Euro 2020 miss, redemption, Premier League champion |
| 10 | Jude Bellingham: *It's Never Too Late* | Playing up, shoulder injury, last-minute heroics |
| 11 | Kenan Yıldız: *Believe in Yourself When Others Don't* | Leaving Bayern, Juventus number 10, Turkey's World Cup return |
| 12 | Lamine Yamal: *The Baby in the Bathtub* | Rocafonda "304," setbacks at 17–18, world champion at 19 |

Luka Modrić is the 12th hero, added to the 11 requested players.

Every chapter has a **Fact File**, the story, a **Teamwork Spotlight**, a **Never-Give-Up Lesson**, **Fun Facts**, and **Your Turn** questions and challenges. The back matter includes a closing chapter, Hero Connections, the Never-Give-Up Playbook, a journal and practice tracker, a 36-question quiz with answers, a glossary, a guide for parents and teachers, and a note on sources.

Facts are current through **October 2026**, including the 2026 World Cup.

## Files

```
manuscript/          The book, one Markdown file per section (edit these)
  00-front-matter.md   Copyright, dedication, introduction
  01..12-*.md          The twelve hero chapters
  13-back-matter.md    Closing, playbook, quiz, glossary, guides
dist/
  soccer-heroes-who-never-gave-up.epub   Upload this to KDP (recommended format)
  soccer-heroes-who-never-gave-up.docx   Word version (editable; also accepted by KDP)
  cover.jpg                              Placeholder cover, 1600x2560
kdp/amazon-listing.md  Description, keywords, categories, pricing, cover brief, tips
build/                 Build scripts (pandoc + Python)
```

## Rebuilding after edits

Requires `pandoc` 3.x and Python 3 with `Pillow` and `python-docx`.

```bash
./build/build.sh
```

## Before you publish

1. **Preview** the EPUB in Amazon's free Kindle Previewer app (linked from the KDP Help Center).
2. **Replace the placeholder cover** with a professional one if possible (see `kdp/amazon-listing.md`).
3. **Disclose AI-generated content** when KDP asks. The text was drafted with an AI assistant.
4. **Double-check any stats** that may have changed since October 2026.
