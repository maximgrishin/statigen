katex="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist"
wget $katex/katex.min.css -P css -N
wget $katex/fonts -P css/fonts -r -nd --accept woff2 -N
wget $katex/katex.min.js -P statigen -N
highlight="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0"
wget $highlight/styles/stackoverflow-dark.min.css -P css -N
wget $highlight/highlight.min.js -P statigen -N
cp statigen/default.css css/default.css
