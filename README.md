# passphrase-cracking
Wordlists and rules for offline cracking of passphrases

## Dictionaries
### Leipzig Corpora
The following dictionaries were generated using english and french files from the [Leipzig Corpora](http://wortschatz.uni-leipzig.de/en/download/).

*D. Goldhahn, T. Eckart & U. Quasthoff: Building Large Monolingual Dictionaries at the Leipzig Corpora Collection: From 100 to 200 Languages.
In: Proceedings of the 8th International Language Ressources and Evaluation (LREC'12), 2012*

| Language  | Word Count | With Spaces | Compressed Size | Uncompressed Size | File                                                                                                                    |
| :-------: | :---------:| :----------:| :--------------:| :----------------:| ------------------------------------------------------------------------------------------------------------------------|
| English   | 3          |             | 344M            | 1.6G              | [leipzig_en_passphrases_3.txt.xz](https://keybase.pub/mathgl/passphrases/leipzig_en_passphrases_3.txt.xz) |
| English   | 4          |             | 752M            | 3.4G              | [leipzig_en_passphrases_4.txt.xz](https://keybase.pub/mathgl/passphrases/leipzig_en_passphrases_4.txt.xz) |
| English   | 5          |             | 1.1G            | 4.5G              | [leipzig_en_passphrases_5.txt.xz](https://keybase.pub/mathgl/passphrases/leipzig_en_passphrases_5.txt.xz) |
| English   | 3          | X           | 391M            | 2.0G              | [leipzig_en_passphrases_spaces_3.txt.xz](https://keybase.pub/mathgl/passphrases/leipzig_en_passphrases_spaces_3.txt.xz) |
| English   | 4          | X           | 793M            | 4.0G              | [leipzig_en_passphrases_spaces_4.txt.xz](https://keybase.pub/mathgl/passphrases/leipzig_en_passphrases_spaces_4.txt.xz) |
| English   | 5          | X           | 1.1G            | 5.2G              | [leipzig_en_passphrases_spaces_5.txt.xz](https://keybase.pub/mathgl/passphrases/leipzig_en_passphrases_spaces_5.txt.xz) |
| French    | 3          |             | 243M            | 1.2G              | [leipzig_fr_passphrases_3.txt.xz](https://keybase.pub/mathgl/passphrases/leipzig_fr_passphrases_3.txt.xz) |
| French    | 4          |             | 510M            | 2.5G              | [leipzig_fr_passphrases_4.txt.xz](https://keybase.pub/mathgl/passphrases/leipzig_fr_passphrases_4.txt.xz) |
| French    | 5          |             | 711M            | 3.3G              | [leipzig_fr_passphrases_5.txt.xz](https://keybase.pub/mathgl/passphrases/leipzig_fr_passphrases_5.txt.xz) |
| French    | 3          | X           | 267M            | 1.5G              | [leipzig_fr_passphrases_spaces_3.txt.xz](https://keybase.pub/mathgl/passphrases/leipzig_fr_passphrases_spaces_3.txt.xz) |
| French    | 4          | X           | 532M            | 2.9G              | [leipzig_fr_passphrases_spaces_4.txt.xz](https://keybase.pub/mathgl/passphrases/leipzig_fr_passphrases_spaces_4.txt.xz) |
| French    | 5          | X           | 733M            | 3.8G              | [leipzig_fr_passphrases_spaces_5.txt.xz](https://keybase.pub/mathgl/passphrases/leipzig_fr_passphrases_spaces_5.txt.xz) |

### initstring's [passphrase-wordlist](https://github.com/initstring/passphrase-wordlist) dictionary
This project includes a massive wordlist of phrases (over 20 million).

* passphrases.txt - https://initstring.keybase.pub/passphrase-wordlist/passphrases.txt?dl=1

## Rules
### initstring's [passphrase-wordlist](https://github.com/initstring/passphrase-wordlist) rules
Rules created specifically for passphrases that will create over 1,000 permutations of each phase:
* passphrase-rule1.rule - https://raw.githubusercontent.com/initstring/passphrase-wordlist/master/hashcat-rules/passphrase-rule1.rule
* passphrase-rule2.rule - https://raw.githubusercontent.com/initstring/passphrase-wordlist/master/hashcat-rules/passphrase-rule2.rule

### One Rule To Rule Them All
Rules from [NotSoSecure](https://github.com/NotSoSecure/password_cracking_rules) created to crack passwords, but with which I had some success.
* OneRuleToRuleThemAll.rule - https://github.com/NotSoSecure/password_cracking_rules/raw/master/OneRuleToRuleThemAll.rule

## How the passphrases were generated
```bash
usage: sentences-to-passphrases.py [-h] [--file FILE] [--with-spaces]
                                   [--word-count WORD_COUNT]

Creates passphrases from sentences.

optional arguments:
  -h, --help            show this help message and exit
  --file FILE, -f FILE  Path to the sentences file.
  --with-spaces         Indicates if the passphrases should contain spaces or
                        not.
  --word-count WORD_COUNT, -c WORD_COUNT
                        The number of words in the passphrases.
```

The python script will generate all the possible passphrases for the given number of words.
To remove duplicates, sort -u can be used:
```bash
./sentences-to-passphrases.py -f leipzig_en.txt --with-spaces -c 5 | sort -u -S4G > leipzig_en_passphrases_spaces_5.txt
```

