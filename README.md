# codeforces_ac
1. Crawls through all the submissions of a user, which can be found on the url "http://www.codeforces.com/submissions/dragon.warrior" (for the username - dragon.warrior).
2. Multiple pages of solutions can be accessed through "http://codeforces.com/submissions/dragon.warrior/page/1" (for page 1, and so on...)
3. Uses Selenium 3.0.2 (A Python library for automation), and Google chrome webdriver.
4. Working - Saves all the solutions of the user which got an "AC" verdict, in a directory ('/home/codeforces')
5. Extension support for Python, C++, and Java is available for now. Rest of the source codes are stores with a '.txt' extension. More language support to come later.
6. Codeforces blog for the above crawler can be found on - http://codeforces.com/blog/entry/50884
