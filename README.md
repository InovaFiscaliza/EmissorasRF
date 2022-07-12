# Anatel - Consulta e Processamento do Banco de Dados
> Este repositório concentra um conjunto de scripts para navegar e baixar informações dos principais bancos de dados da Anatel e as bases públicas da Aeronáutica como o AISWEB, GEOAISWEB e ICAO cruzadas com documentações técnicas internas. Cujo dados serão utilizados em tarefas fiscalizatórias. O público alvo são os servidores do órgão, uma vez que a maioria dos sistemas utilizados aqui necessitam de autenticação cujo acesso é restrito aos servidores da ANATEL.


<a href="https://gitmoji.dev">
  <img src="https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67.svg?style=flat-square" alt="Gitmoji">
</a>

[![scraper: gazpacho](https://img.shields.io/badge/scraper-gazpacho-C6422C)](https://github.com/maxhumber/gazpacho)

## Instalação

<code>pip install anateldb</code>

## Como utilizar

### Consulta à base de dados formatada para o AppAnalise de Anatel

A motivação original para a presente biblioteca foi disponibilizar os dados de diferentes fontes da Anatel - e posteriormente da Aeronáutica - programaticamente, para serem utilizadas pelo [AppAnalise](https://github.com/EricMagalhaesDelgado/appAnalise/releases/) na identificação de emissões captadas pelos planos de monitoração e também em fiscalização de campo.

Os dados no formato atual em excel são disponibilizados na forma de releases neste repositório juntamente com a versão de código https://github.com/ronaldokun/anateldb/releases. 

Os dados em formato otimizado `.parquet.gzip` são disponibilizados junto ao repositório na pasta `dados` juntamente com as versões das bases individuais. Futuramente o objetivo é descontinuar a liberação de arquivos em formato excel e disponibilizar apenas os dados em formato otimizado. 

```python
import pandas as pd
from fastcore.xtras import Path

pasta = Path.cwd().parent / 'dados'
anateldb = pd.read_parquet(pasta / 'AnatelDB.parquet.gzip')
```

```python
anateldb['Frequency'] = anateldb['Frequency'].astype('category')
profile = ProfileReport(anateldb, config_file='report_config.yaml')
profile.to_notebook_iframe()
```


<iframe width="100%" height="800px" srcdoc="&lt;!doctype html&gt;&lt;html lang=en&gt;&lt;head&gt;&lt;meta charset=utf-8&gt;&lt;meta name=viewport content=&quot;width=device-width, initial-scale=1, shrink-to-fit=no&quot;&gt;&lt;meta name=description content=&quot;Profile report generated with the `pandas-profiling` Python package&quot;&gt;&lt;meta name=author content=&quot;Simon Brugman and the open source community.&quot;&gt;&lt;meta name=generator content=&quot;Pandas Profiling v3.2.0&quot;&gt;&lt;meta name=url content=https://github.com/pandas-profiling/pandas-profiling&gt;&lt;meta name=date content=&quot;2022-07-12 16:06:35.364667&quot;&gt;&lt;title&gt;Pandas Profiling Report&lt;/title&gt;&lt;style&gt;
@import url(&quot;https://fonts.googleapis.com/css?family=Lato:400,700,400italic&quot;);/*!
 * bootswatch v3.3.7
 * Homepage: http://bootswatch.com
 * Copyright 2012-2016 Thomas Park
 * Licensed under MIT
 * Based on Bootstrap
*//*!
 * Bootstrap v3.3.7 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 *//*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */html{font-family:sans-serif;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%}body{margin:0}article,aside,details,figcaption,figure,footer,header,hgroup,main,menu,nav,section,summary{display:block}audio,canvas,progress,video{display:inline-block;vertical-align:baseline}audio:not([controls]){display:none;height:0}[hidden],template{display:none}a{background-color:transparent}a:active,a:hover{outline:0}abbr[title]{border-bottom:1px dotted}b,strong{font-weight:bold}dfn{font-style:italic}h1{font-size:2em;margin:0.67em 0}mark{background:#ff0;color:#000}small{font-size:80%}sub,sup{font-size:75%;line-height:0;position:relative;vertical-align:baseline}sup{top:-0.5em}sub{bottom:-0.25em}img{border:0}svg:not(:root){overflow:hidden}figure{margin:1em 40px}hr{-webkit-box-sizing:content-box;-moz-box-sizing:content-box;box-sizing:content-box;height:0}pre{overflow:auto}code,kbd,pre,samp{font-family:monospace, monospace;font-size:1em}button,input,optgroup,select,textarea{color:inherit;font:inherit;margin:0}button{overflow:visible}button,select{text-transform:none}button,html input[type=&quot;button&quot;],input[type=&quot;reset&quot;],input[type=&quot;submit&quot;]{-webkit-appearance:button;cursor:pointer}button[disabled],html input[disabled]{cursor:default}button::-moz-focus-inner,input::-moz-focus-inner{border:0;padding:0}input{line-height:normal}input[type=&quot;checkbox&quot;],input[type=&quot;radio&quot;]{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;padding:0}input[type=&quot;number&quot;]::-webkit-inner-spin-button,input[type=&quot;number&quot;]::-webkit-outer-spin-button{height:auto}input[type=&quot;search&quot;]{-webkit-appearance:textfield;-webkit-box-sizing:content-box;-moz-box-sizing:content-box;box-sizing:content-box}input[type=&quot;search&quot;]::-webkit-search-cancel-button,input[type=&quot;search&quot;]::-webkit-search-decoration{-webkit-appearance:none}fieldset{border:1px solid #c0c0c0;margin:0 2px;padding:0.35em 0.625em 0.75em}legend{border:0;padding:0}textarea{overflow:auto}optgroup{font-weight:bold}table{border-collapse:collapse;border-spacing:0}td,th{padding:0}/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */@media print{*,*:before,*:after{background:transparent !important;color:#000 !important;-webkit-box-shadow:none !important;box-shadow:none !important;text-shadow:none !important}a,a:visited{text-decoration:underline}a[href]:after{content:&quot; (&quot; attr(href) &quot;)&quot;}abbr[title]:after{content:&quot; (&quot; attr(title) &quot;)&quot;}a[href^=&quot;#&quot;]:after,a[href^=&quot;javascript:&quot;]:after{content:&quot;&quot;}pre,blockquote{border:1px solid #999;page-break-inside:avoid}thead{display:table-header-group}tr,img{page-break-inside:avoid}img{max-width:100% !important}p,h2,h3{orphans:3;widows:3}h2,h3{page-break-after:avoid}.navbar{display:none}.btn&gt;.caret,.dropup&gt;.btn&gt;.caret{border-top-color:#000 !important}.label{border:1px solid #000}.table{border-collapse:collapse !important}.table td,.table th{background-color:#fff !important}.table-bordered th,.table-bordered td{border:1px solid #ddd !important}}@font-face{font-family:&#x27;Glyphicons Halflings&#x27;;src:url(&#x27;../fonts/glyphicons-halflings-regular.eot&#x27;);src:url(&#x27;../fonts/glyphicons-halflings-regular.eot?#iefix&#x27;) format(&#x27;embedded-opentype&#x27;),url(&#x27;../fonts/glyphicons-halflings-regular.woff2&#x27;) format(&#x27;woff2&#x27;),url(&#x27;../fonts/glyphicons-halflings-regular.woff&#x27;) format(&#x27;woff&#x27;),url(&#x27;../fonts/glyphicons-halflings-regular.ttf&#x27;) format(&#x27;truetype&#x27;),url(&#x27;../fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular&#x27;) format(&#x27;svg&#x27;)}.glyphicon{position:relative;top:1px;display:inline-block;font-family:&#x27;Glyphicons Halflings&#x27;;font-style:normal;font-weight:normal;line-height:1;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.glyphicon-asterisk:before{content:&quot;\002a&quot;}.glyphicon-plus:before{content:&quot;\002b&quot;}.glyphicon-euro:before,.glyphicon-eur:before{content:&quot;\20ac&quot;}.glyphicon-minus:before{content:&quot;\2212&quot;}.glyphicon-cloud:before{content:&quot;\2601&quot;}.glyphicon-envelope:before{content:&quot;\2709&quot;}.glyphicon-pencil:before{content:&quot;\270f&quot;}.glyphicon-glass:before{content:&quot;\e001&quot;}.glyphicon-music:before{content:&quot;\e002&quot;}.glyphicon-search:before{content:&quot;\e003&quot;}.glyphicon-heart:before{content:&quot;\e005&quot;}.glyphicon-star:before{content:&quot;\e006&quot;}.glyphicon-star-empty:before{content:&quot;\e007&quot;}.glyphicon-user:before{content:&quot;\e008&quot;}.glyphicon-film:before{content:&quot;\e009&quot;}.glyphicon-th-large:before{content:&quot;\e010&quot;}.glyphicon-th:before{content:&quot;\e011&quot;}.glyphicon-th-list:before{content:&quot;\e012&quot;}.glyphicon-ok:before{content:&quot;\e013&quot;}.glyphicon-remove:before{content:&quot;\e014&quot;}.glyphicon-zoom-in:before{content:&quot;\e015&quot;}.glyphicon-zoom-out:before{content:&quot;\e016&quot;}.glyphicon-off:before{content:&quot;\e017&quot;}.glyphicon-signal:before{content:&quot;\e018&quot;}.glyphicon-cog:before{content:&quot;\e019&quot;}.glyphicon-trash:before{content:&quot;\e020&quot;}.glyphicon-home:before{content:&quot;\e021&quot;}.glyphicon-file:before{content:&quot;\e022&quot;}.glyphicon-time:before{content:&quot;\e023&quot;}.glyphicon-road:before{content:&quot;\e024&quot;}.glyphicon-download-alt:before{content:&quot;\e025&quot;}.glyphicon-download:before{content:&quot;\e026&quot;}.glyphicon-upload:before{content:&quot;\e027&quot;}.glyphicon-inbox:before{content:&quot;\e028&quot;}.glyphicon-play-circle:before{content:&quot;\e029&quot;}.glyphicon-repeat:before{content:&quot;\e030&quot;}.glyphicon-refresh:before{content:&quot;\e031&quot;}.glyphicon-list-alt:before{content:&quot;\e032&quot;}.glyphicon-lock:before{content:&quot;\e033&quot;}.glyphicon-flag:before{content:&quot;\e034&quot;}.glyphicon-headphones:before{content:&quot;\e035&quot;}.glyphicon-volume-off:before{content:&quot;\e036&quot;}.glyphicon-volume-down:before{content:&quot;\e037&quot;}.glyphicon-volume-up:before{content:&quot;\e038&quot;}.glyphicon-qrcode:before{content:&quot;\e039&quot;}.glyphicon-barcode:before{content:&quot;\e040&quot;}.glyphicon-tag:before{content:&quot;\e041&quot;}.glyphicon-tags:before{content:&quot;\e042&quot;}.glyphicon-book:before{content:&quot;\e043&quot;}.glyphicon-bookmark:before{content:&quot;\e044&quot;}.glyphicon-print:before{content:&quot;\e045&quot;}.glyphicon-camera:before{content:&quot;\e046&quot;}.glyphicon-font:before{content:&quot;\e047&quot;}.glyphicon-bold:before{content:&quot;\e048&quot;}.glyphicon-italic:before{content:&quot;\e049&quot;}.glyphicon-text-height:before{content:&quot;\e050&quot;}.glyphicon-text-width:before{content:&quot;\e051&quot;}.glyphicon-align-left:before{content:&quot;\e052&quot;}.glyphicon-align-center:before{content:&quot;\e053&quot;}.glyphicon-align-right:before{content:&quot;\e054&quot;}.glyphicon-align-justify:before{content:&quot;\e055&quot;}.glyphicon-list:before{content:&quot;\e056&quot;}.glyphicon-indent-left:before{content:&quot;\e057&quot;}.glyphicon-indent-right:before{content:&quot;\e058&quot;}.glyphicon-facetime-video:before{content:&quot;\e059&quot;}.glyphicon-picture:before{content:&quot;\e060&quot;}.glyphicon-map-marker:before{content:&quot;\e062&quot;}.glyphicon-adjust:before{content:&quot;\e063&quot;}.glyphicon-tint:before{content:&quot;\e064&quot;}.glyphicon-edit:before{content:&quot;\e065&quot;}.glyphicon-share:before{content:&quot;\e066&quot;}.glyphicon-check:before{content:&quot;\e067&quot;}.glyphicon-move:before{content:&quot;\e068&quot;}.glyphicon-step-backward:before{content:&quot;\e069&quot;}.glyphicon-fast-backward:before{content:&quot;\e070&quot;}.glyphicon-backward:before{content:&quot;\e071&quot;}.glyphicon-play:before{content:&quot;\e072&quot;}.glyphicon-pause:before{content:&quot;\e073&quot;}.glyphicon-stop:before{content:&quot;\e074&quot;}.glyphicon-forward:before{content:&quot;\e075&quot;}.glyphicon-fast-forward:before{content:&quot;\e076&quot;}.glyphicon-step-forward:before{content:&quot;\e077&quot;}.glyphicon-eject:before{content:&quot;\e078&quot;}.glyphicon-chevron-left:before{content:&quot;\e079&quot;}.glyphicon-chevron-right:before{content:&quot;\e080&quot;}.glyphicon-plus-sign:before{content:&quot;\e081&quot;}.glyphicon-minus-sign:before{content:&quot;\e082&quot;}.glyphicon-remove-sign:before{content:&quot;\e083&quot;}.glyphicon-ok-sign:before{content:&quot;\e084&quot;}.glyphicon-question-sign:before{content:&quot;\e085&quot;}.glyphicon-info-sign:before{content:&quot;\e086&quot;}.glyphicon-screenshot:before{content:&quot;\e087&quot;}.glyphicon-remove-circle:before{content:&quot;\e088&quot;}.glyphicon-ok-circle:before{content:&quot;\e089&quot;}.glyphicon-ban-circle:before{content:&quot;\e090&quot;}.glyphicon-arrow-left:before{content:&quot;\e091&quot;}.glyphicon-arrow-right:before{content:&quot;\e092&quot;}.glyphicon-arrow-up:before{content:&quot;\e093&quot;}.glyphicon-arrow-down:before{content:&quot;\e094&quot;}.glyphicon-share-alt:before{content:&quot;\e095&quot;}.glyphicon-resize-full:before{content:&quot;\e096&quot;}.glyphicon-resize-small:before{content:&quot;\e097&quot;}.glyphicon-exclamation-sign:before{content:&quot;\e101&quot;}.glyphicon-gift:before{content:&quot;\e102&quot;}.glyphicon-leaf:before{content:&quot;\e103&quot;}.glyphicon-fire:before{content:&quot;\e104&quot;}.glyphicon-eye-open:before{content:&quot;\e105&quot;}.glyphicon-eye-close:before{content:&quot;\e106&quot;}.glyphicon-warning-sign:before{content:&quot;\e107&quot;}.glyphicon-plane:before{content:&quot;\e108&quot;}.glyphicon-calendar:before{content:&quot;\e109&quot;}.glyphicon-random:before{content:&quot;\e110&quot;}.glyphicon-comment:before{content:&quot;\e111&quot;}.glyphicon-magnet:before{content:&quot;\e112&quot;}.glyphicon-chevron-up:before{content:&quot;\e113&quot;}.glyphicon-chevron-down:before{content:&quot;\e114&quot;}.glyphicon-retweet:before{content:&quot;\e115&quot;}.glyphicon-shopping-cart:before{content:&quot;\e116&quot;}.glyphicon-folder-close:before{content:&quot;\e117&quot;}.glyphicon-folder-open:before{content:&quot;\e118&quot;}.glyphicon-resize-vertical:before{content:&quot;\e119&quot;}.glyphicon-resize-horizontal:before{content:&quot;\e120&quot;}.glyphicon-hdd:before{content:&quot;\e121&quot;}.glyphicon-bullhorn:before{content:&quot;\e122&quot;}.glyphicon-bell:before{content:&quot;\e123&quot;}.glyphicon-certificate:before{content:&quot;\e124&quot;}.glyphicon-thumbs-up:before{content:&quot;\e125&quot;}.glyphicon-thumbs-down:before{content:&quot;\e126&quot;}.glyphicon-hand-right:before{content:&quot;\e127&quot;}.glyphicon-hand-left:before{content:&quot;\e128&quot;}.glyphicon-hand-up:before{content:&quot;\e129&quot;}.glyphicon-hand-down:before{content:&quot;\e130&quot;}.glyphicon-circle-arrow-right:before{content:&quot;\e131&quot;}.glyphicon-circle-arrow-left:before{content:&quot;\e132&quot;}.glyphicon-circle-arrow-up:before{content:&quot;\e133&quot;}.glyphicon-circle-arrow-down:before{content:&quot;\e134&quot;}.glyphicon-globe:before{content:&quot;\e135&quot;}.glyphicon-wrench:before{content:&quot;\e136&quot;}.glyphicon-tasks:before{content:&quot;\e137&quot;}.glyphicon-filter:before{content:&quot;\e138&quot;}.glyphicon-briefcase:before{content:&quot;\e139&quot;}.glyphicon-fullscreen:before{content:&quot;\e140&quot;}.glyphicon-dashboard:before{content:&quot;\e141&quot;}.glyphicon-paperclip:before{content:&quot;\e142&quot;}.glyphicon-heart-empty:before{content:&quot;\e143&quot;}.glyphicon-link:before{content:&quot;\e144&quot;}.glyphicon-phone:before{content:&quot;\e145&quot;}.glyphicon-pushpin:before{content:&quot;\e146&quot;}.glyphicon-usd:before{content:&quot;\e148&quot;}.glyphicon-gbp:before{content:&quot;\e149&quot;}.glyphicon-sort:before{content:&quot;\e150&quot;}.glyphicon-sort-by-alphabet:before{content:&quot;\e151&quot;}.glyphicon-sort-by-alphabet-alt:before{content:&quot;\e152&quot;}.glyphicon-sort-by-order:before{content:&quot;\e153&quot;}.glyphicon-sort-by-order-alt:before{content:&quot;\e154&quot;}.glyphicon-sort-by-attributes:before{content:&quot;\e155&quot;}.glyphicon-sort-by-attributes-alt:before{content:&quot;\e156&quot;}.glyphicon-unchecked:before{content:&quot;\e157&quot;}.glyphicon-expand:before{content:&quot;\e158&quot;}.glyphicon-collapse-down:before{content:&quot;\e159&quot;}.glyphicon-collapse-up:before{content:&quot;\e160&quot;}.glyphicon-log-in:before{content:&quot;\e161&quot;}.glyphicon-flash:before{content:&quot;\e162&quot;}.glyphicon-log-out:before{content:&quot;\e163&quot;}.glyphicon-new-window:before{content:&quot;\e164&quot;}.glyphicon-record:before{content:&quot;\e165&quot;}.glyphicon-save:before{content:&quot;\e166&quot;}.glyphicon-open:before{content:&quot;\e167&quot;}.glyphicon-saved:before{content:&quot;\e168&quot;}.glyphicon-import:before{content:&quot;\e169&quot;}.glyphicon-export:before{content:&quot;\e170&quot;}.glyphicon-send:before{content:&quot;\e171&quot;}.glyphicon-floppy-disk:before{content:&quot;\e172&quot;}.glyphicon-floppy-saved:before{content:&quot;\e173&quot;}.glyphicon-floppy-remove:before{content:&quot;\e174&quot;}.glyphicon-floppy-save:before{content:&quot;\e175&quot;}.glyphicon-floppy-open:before{content:&quot;\e176&quot;}.glyphicon-credit-card:before{content:&quot;\e177&quot;}.glyphicon-transfer:before{content:&quot;\e178&quot;}.glyphicon-cutlery:before{content:&quot;\e179&quot;}.glyphicon-header:before{content:&quot;\e180&quot;}.glyphicon-compressed:before{content:&quot;\e181&quot;}.glyphicon-earphone:before{content:&quot;\e182&quot;}.glyphicon-phone-alt:before{content:&quot;\e183&quot;}.glyphicon-tower:before{content:&quot;\e184&quot;}.glyphicon-stats:before{content:&quot;\e185&quot;}.glyphicon-sd-video:before{content:&quot;\e186&quot;}.glyphicon-hd-video:before{content:&quot;\e187&quot;}.glyphicon-subtitles:before{content:&quot;\e188&quot;}.glyphicon-sound-stereo:before{content:&quot;\e189&quot;}.glyphicon-sound-dolby:before{content:&quot;\e190&quot;}.glyphicon-sound-5-1:before{content:&quot;\e191&quot;}.glyphicon-sound-6-1:before{content:&quot;\e192&quot;}.glyphicon-sound-7-1:before{content:&quot;\e193&quot;}.glyphicon-copyright-mark:before{content:&quot;\e194&quot;}.glyphicon-registration-mark:before{content:&quot;\e195&quot;}.glyphicon-cloud-download:before{content:&quot;\e197&quot;}.glyphicon-cloud-upload:before{content:&quot;\e198&quot;}.glyphicon-tree-conifer:before{content:&quot;\e199&quot;}.glyphicon-tree-deciduous:before{content:&quot;\e200&quot;}.glyphicon-cd:before{content:&quot;\e201&quot;}.glyphicon-save-file:before{content:&quot;\e202&quot;}.glyphicon-open-file:before{content:&quot;\e203&quot;}.glyphicon-level-up:before{content:&quot;\e204&quot;}.glyphicon-copy:before{content:&quot;\e205&quot;}.glyphicon-paste:before{content:&quot;\e206&quot;}.glyphicon-alert:before{content:&quot;\e209&quot;}.glyphicon-equalizer:before{content:&quot;\e210&quot;}.glyphicon-king:before{content:&quot;\e211&quot;}.glyphicon-queen:before{content:&quot;\e212&quot;}.glyphicon-pawn:before{content:&quot;\e213&quot;}.glyphicon-bishop:before{content:&quot;\e214&quot;}.glyphicon-knight:before{content:&quot;\e215&quot;}.glyphicon-baby-formula:before{content:&quot;\e216&quot;}.glyphicon-tent:before{content:&quot;\26fa&quot;}.glyphicon-blackboard:before{content:&quot;\e218&quot;}.glyphicon-bed:before{content:&quot;\e219&quot;}.glyphicon-apple:before{content:&quot;\f8ff&quot;}.glyphicon-erase:before{content:&quot;\e221&quot;}.glyphicon-hourglass:before{content:&quot;\231b&quot;}.glyphicon-lamp:before{content:&quot;\e223&quot;}.glyphicon-duplicate:before{content:&quot;\e224&quot;}.glyphicon-piggy-bank:before{content:&quot;\e225&quot;}.glyphicon-scissors:before{content:&quot;\e226&quot;}.glyphicon-bitcoin:before{content:&quot;\e227&quot;}.glyphicon-btc:before{content:&quot;\e227&quot;}.glyphicon-xbt:before{content:&quot;\e227&quot;}.glyphicon-yen:before{content:&quot;\00a5&quot;}.glyphicon-jpy:before{content:&quot;\00a5&quot;}.glyphicon-ruble:before{content:&quot;\20bd&quot;}.glyphicon-rub:before{content:&quot;\20bd&quot;}.glyphicon-scale:before{content:&quot;\e230&quot;}.glyphicon-ice-lolly:before{content:&quot;\e231&quot;}.glyphicon-ice-lolly-tasted:before{content:&quot;\e232&quot;}.glyphicon-education:before{content:&quot;\e233&quot;}.glyphicon-option-horizontal:before{content:&quot;\e234&quot;}.glyphicon-option-vertical:before{content:&quot;\e235&quot;}.glyphicon-menu-hamburger:before{content:&quot;\e236&quot;}.glyphicon-modal-window:before{content:&quot;\e237&quot;}.glyphicon-oil:before{content:&quot;\e238&quot;}.glyphicon-grain:before{content:&quot;\e239&quot;}.glyphicon-sunglasses:before{content:&quot;\e240&quot;}.glyphicon-text-size:before{content:&quot;\e241&quot;}.glyphicon-text-color:before{content:&quot;\e242&quot;}.glyphicon-text-background:before{content:&quot;\e243&quot;}.glyphicon-object-align-top:before{content:&quot;\e244&quot;}.glyphicon-object-align-bottom:before{content:&quot;\e245&quot;}.glyphicon-object-align-horizontal:before{content:&quot;\e246&quot;}.glyphicon-object-align-left:before{content:&quot;\e247&quot;}.glyphicon-object-align-vertical:before{content:&quot;\e248&quot;}.glyphicon-object-align-right:before{content:&quot;\e249&quot;}.glyphicon-triangle-right:before{content:&quot;\e250&quot;}.glyphicon-triangle-left:before{content:&quot;\e251&quot;}.glyphicon-triangle-bottom:before{content:&quot;\e252&quot;}.glyphicon-triangle-top:before{content:&quot;\e253&quot;}.glyphicon-console:before{content:&quot;\e254&quot;}.glyphicon-superscript:before{content:&quot;\e255&quot;}.glyphicon-subscript:before{content:&quot;\e256&quot;}.glyphicon-menu-left:before{content:&quot;\e257&quot;}.glyphicon-menu-right:before{content:&quot;\e258&quot;}.glyphicon-menu-down:before{content:&quot;\e259&quot;}.glyphicon-menu-up:before{content:&quot;\e260&quot;}*{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box}*:before,*:after{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box}html{font-size:10px;-webkit-tap-highlight-color:rgba(0,0,0,0)}body{font-family:&quot;Lato&quot;,&quot;Helvetica Neue&quot;,Helvetica,Arial,sans-serif;font-size:15px;line-height:1.42857143;color:#2c3e50;background-color:#ffffff}input,button,select,textarea{font-family:inherit;font-size:inherit;line-height:inherit}a{color:#18bc9c;text-decoration:none}a:hover,a:focus{color:#18bc9c;text-decoration:underline}a:focus{outline:5px auto -webkit-focus-ring-color;outline-offset:-2px}figure{margin:0}img{vertical-align:middle}.img-responsive,.thumbnail&gt;img,.thumbnail a&gt;img,.carousel-inner&gt;.item&gt;img,.carousel-inner&gt;.item&gt;a&gt;img{display:block;max-width:100%;height:auto}.img-rounded{border-radius:6px}.img-thumbnail{padding:4px;line-height:1.42857143;background-color:#ffffff;border:1px solid #ecf0f1;border-radius:4px;-webkit-transition:all .2s ease-in-out;-o-transition:all .2s ease-in-out;transition:all .2s ease-in-out;display:inline-block;max-width:100%;height:auto}.img-circle{border-radius:50%}hr{margin-top:21px;margin-bottom:21px;border:0;border-top:1px solid #ecf0f1}.sr-only{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0, 0, 0, 0);border:0}.sr-only-focusable:active,.sr-only-focusable:focus{position:static;width:auto;height:auto;margin:0;overflow:visible;clip:auto}[role=&quot;button&quot;]{cursor:pointer}h1,h2,h3,h4,h5,h6,.h1,.h2,.h3,.h4,.h5,.h6{font-family:&quot;Lato&quot;,&quot;Helvetica Neue&quot;,Helvetica,Arial,sans-serif;font-weight:400;line-height:1.1;color:inherit}h1 small,h2 small,h3 small,h4 small,h5 small,h6 small,.h1 small,.h2 small,.h3 small,.h4 small,.h5 small,.h6 small,h1 .small,h2 .small,h3 .small,h4 .small,h5 .small,h6 .small,.h1 .small,.h2 .small,.h3 .small,.h4 .small,.h5 .small,.h6 .small{font-weight:normal;line-height:1;color:#b4bcc2}h1,.h1,h2,.h2,h3,.h3{margin-top:21px;margin-bottom:10.5px}h1 small,.h1 small,h2 small,.h2 small,h3 small,.h3 small,h1 .small,.h1 .small,h2 .small,.h2 .small,h3 .small,.h3 .small{font-size:65%}h4,.h4,h5,.h5,h6,.h6{margin-top:10.5px;margin-bottom:10.5px}h4 small,.h4 small,h5 small,.h5 small,h6 small,.h6 small,h4 .small,.h4 .small,h5 .small,.h5 .small,h6 .small,.h6 .small{font-size:75%}h1,.h1{font-size:39px}h2,.h2{font-size:32px}h3,.h3{font-size:26px}h4,.h4{font-size:19px}h5,.h5{font-size:15px}h6,.h6{font-size:13px}p{margin:0 0 10.5px}.lead{margin-bottom:21px;font-size:17px;font-weight:300;line-height:1.4}@media (min-width:768px){.lead{font-size:22.5px}}small,.small{font-size:86%}mark,.mark{background-color:#f39c12;padding:.2em}.text-left{text-align:left}.text-right{text-align:right}.text-center{text-align:center}.text-justify{text-align:justify}.text-nowrap{white-space:nowrap}.text-lowercase{text-transform:lowercase}.text-uppercase{text-transform:uppercase}.text-capitalize{text-transform:capitalize}.text-muted{color:#b4bcc2}.text-primary{color:#2c3e50}a.text-primary:hover,a.text-primary:focus{color:#1a242f}.text-success{color:#ffffff}a.text-success:hover,a.text-success:focus{color:#e6e6e6}.text-info{color:#ffffff}a.text-info:hover,a.text-info:focus{color:#e6e6e6}.text-warning{color:#ffffff}a.text-warning:hover,a.text-warning:focus{color:#e6e6e6}.text-danger{color:#ffffff}a.text-danger:hover,a.text-danger:focus{color:#e6e6e6}.bg-primary{color:#fff;background-color:#2c3e50}a.bg-primary:hover,a.bg-primary:focus{background-color:#1a242f}.bg-success{background-color:#18bc9c}a.bg-success:hover,a.bg-success:focus{background-color:#128f76}.bg-info{background-color:#3498db}a.bg-info:hover,a.bg-info:focus{background-color:#217dbb}.bg-warning{background-color:#f39c12}a.bg-warning:hover,a.bg-warning:focus{background-color:#c87f0a}.bg-danger{background-color:#e74c3c}a.bg-danger:hover,a.bg-danger:focus{background-color:#d62c1a}.page-header{padding-bottom:9.5px;margin:42px 0 21px;border-bottom:1px solid transparent}ul,ol{margin-top:0;margin-bottom:10.5px}ul ul,ol ul,ul ol,ol ol{margin-bottom:0}.list-unstyled{padding-left:0;list-style:none}.list-inline{padding-left:0;list-style:none;margin-left:-5px}.list-inline&gt;li{display:inline-block;padding-left:5px;padding-right:5px}dl{margin-top:0;margin-bottom:21px}dt,dd{line-height:1.42857143}dt{font-weight:bold}dd{margin-left:0}@media (min-width:768px){.dl-horizontal dt{float:left;width:160px;clear:left;text-align:right;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.dl-horizontal dd{margin-left:180px}}abbr[title],abbr[data-original-title]{cursor:help;border-bottom:1px dotted #b4bcc2}.initialism{font-size:90%;text-transform:uppercase}blockquote{padding:10.5px 21px;margin:0 0 21px;font-size:18.75px;border-left:5px solid #ecf0f1}blockquote p:last-child,blockquote ul:last-child,blockquote ol:last-child{margin-bottom:0}blockquote footer,blockquote small,blockquote .small{display:block;font-size:80%;line-height:1.42857143;color:#b4bcc2}blockquote footer:before,blockquote small:before,blockquote .small:before{content:&#x27;\2014 \00A0&#x27;}.blockquote-reverse,blockquote.pull-right{padding-right:15px;padding-left:0;border-right:5px solid #ecf0f1;border-left:0;text-align:right}.blockquote-reverse footer:before,blockquote.pull-right footer:before,.blockquote-reverse small:before,blockquote.pull-right small:before,.blockquote-reverse .small:before,blockquote.pull-right .small:before{content:&#x27;&#x27;}.blockquote-reverse footer:after,blockquote.pull-right footer:after,.blockquote-reverse small:after,blockquote.pull-right small:after,.blockquote-reverse .small:after,blockquote.pull-right .small:after{content:&#x27;\00A0 \2014&#x27;}address{margin-bottom:21px;font-style:normal;line-height:1.42857143}code,kbd,pre,samp{font-family:Menlo,Monaco,Consolas,&quot;Courier New&quot;,monospace}code{padding:2px 4px;font-size:90%;color:#c7254e;background-color:#f9f2f4;border-radius:4px}kbd{padding:2px 4px;font-size:90%;color:#ffffff;background-color:#333333;border-radius:3px;-webkit-box-shadow:inset 0 -1px 0 rgba(0,0,0,0.25);box-shadow:inset 0 -1px 0 rgba(0,0,0,0.25)}kbd kbd{padding:0;font-size:100%;font-weight:bold;-webkit-box-shadow:none;box-shadow:none}pre{display:block;padding:10px;margin:0 0 10.5px;font-size:14px;line-height:1.42857143;word-break:break-all;word-wrap:break-word;color:#7b8a8b;background-color:#ecf0f1;border:1px solid #cccccc;border-radius:4px}pre code{padding:0;font-size:inherit;color:inherit;white-space:pre-wrap;background-color:transparent;border-radius:0}.pre-scrollable{max-height:340px;overflow-y:scroll}.container{margin-right:auto;margin-left:auto;padding-left:15px;padding-right:15px}@media (min-width:768px){.container{width:750px}}@media (min-width:992px){.container{width:970px}}@media (min-width:1200px){.container{width:1170px}}.container-fluid{margin-right:auto;margin-left:auto;padding-left:15px;padding-right:15px}.row{margin-left:-15px;margin-right:-15px}.col-xs-1,.col-sm-1,.col-md-1,.col-lg-1,.col-xs-2,.col-sm-2,.col-md-2,.col-lg-2,.col-xs-3,.col-sm-3,.col-md-3,.col-lg-3,.col-xs-4,.col-sm-4,.col-md-4,.col-lg-4,.col-xs-5,.col-sm-5,.col-md-5,.col-lg-5,.col-xs-6,.col-sm-6,.col-md-6,.col-lg-6,.col-xs-7,.col-sm-7,.col-md-7,.col-lg-7,.col-xs-8,.col-sm-8,.col-md-8,.col-lg-8,.col-xs-9,.col-sm-9,.col-md-9,.col-lg-9,.col-xs-10,.col-sm-10,.col-md-10,.col-lg-10,.col-xs-11,.col-sm-11,.col-md-11,.col-lg-11,.col-xs-12,.col-sm-12,.col-md-12,.col-lg-12{position:relative;min-height:1px;padding-left:15px;padding-right:15px}.col-xs-1,.col-xs-2,.col-xs-3,.col-xs-4,.col-xs-5,.col-xs-6,.col-xs-7,.col-xs-8,.col-xs-9,.col-xs-10,.col-xs-11,.col-xs-12{float:left}.col-xs-12{width:100%}.col-xs-11{width:91.66666667%}.col-xs-10{width:83.33333333%}.col-xs-9{width:75%}.col-xs-8{width:66.66666667%}.col-xs-7{width:58.33333333%}.col-xs-6{width:50%}.col-xs-5{width:41.66666667%}.col-xs-4{width:33.33333333%}.col-xs-3{width:25%}.col-xs-2{width:16.66666667%}.col-xs-1{width:8.33333333%}.col-xs-pull-12{right:100%}.col-xs-pull-11{right:91.66666667%}.col-xs-pull-10{right:83.33333333%}.col-xs-pull-9{right:75%}.col-xs-pull-8{right:66.66666667%}.col-xs-pull-7{right:58.33333333%}.col-xs-pull-6{right:50%}.col-xs-pull-5{right:41.66666667%}.col-xs-pull-4{right:33.33333333%}.col-xs-pull-3{right:25%}.col-xs-pull-2{right:16.66666667%}.col-xs-pull-1{right:8.33333333%}.col-xs-pull-0{right:auto}.col-xs-push-12{left:100%}.col-xs-push-11{left:91.66666667%}.col-xs-push-10{left:83.33333333%}.col-xs-push-9{left:75%}.col-xs-push-8{left:66.66666667%}.col-xs-push-7{left:58.33333333%}.col-xs-push-6{left:50%}.col-xs-push-5{left:41.66666667%}.col-xs-push-4{left:33.33333333%}.col-xs-push-3{left:25%}.col-xs-push-2{left:16.66666667%}.col-xs-push-1{left:8.33333333%}.col-xs-push-0{left:auto}.col-xs-offset-12{margin-left:100%}.col-xs-offset-11{margin-left:91.66666667%}.col-xs-offset-10{margin-left:83.33333333%}.col-xs-offset-9{margin-left:75%}.col-xs-offset-8{margin-left:66.66666667%}.col-xs-offset-7{margin-left:58.33333333%}.col-xs-offset-6{margin-left:50%}.col-xs-offset-5{margin-left:41.66666667%}.col-xs-offset-4{margin-left:33.33333333%}.col-xs-offset-3{margin-left:25%}.col-xs-offset-2{margin-left:16.66666667%}.col-xs-offset-1{margin-left:8.33333333%}.col-xs-offset-0{margin-left:0%}@media (min-width:768px){.col-sm-1,.col-sm-2,.col-sm-3,.col-sm-4,.col-sm-5,.col-sm-6,.col-sm-7,.col-sm-8,.col-sm-9,.col-sm-10,.col-sm-11,.col-sm-12{float:left}.col-sm-12{width:100%}.col-sm-11{width:91.66666667%}.col-sm-10{width:83.33333333%}.col-sm-9{width:75%}.col-sm-8{width:66.66666667%}.col-sm-7{width:58.33333333%}.col-sm-6{width:50%}.col-sm-5{width:41.66666667%}.col-sm-4{width:33.33333333%}.col-sm-3{width:25%}.col-sm-2{width:16.66666667%}.col-sm-1{width:8.33333333%}.col-sm-pull-12{right:100%}.col-sm-pull-11{right:91.66666667%}.col-sm-pull-10{right:83.33333333%}.col-sm-pull-9{right:75%}.col-sm-pull-8{right:66.66666667%}.col-sm-pull-7{right:58.33333333%}.col-sm-pull-6{right:50%}.col-sm-pull-5{right:41.66666667%}.col-sm-pull-4{right:33.33333333%}.col-sm-pull-3{right:25%}.col-sm-pull-2{right:16.66666667%}.col-sm-pull-1{right:8.33333333%}.col-sm-pull-0{right:auto}.col-sm-push-12{left:100%}.col-sm-push-11{left:91.66666667%}.col-sm-push-10{left:83.33333333%}.col-sm-push-9{left:75%}.col-sm-push-8{left:66.66666667%}.col-sm-push-7{left:58.33333333%}.col-sm-push-6{left:50%}.col-sm-push-5{left:41.66666667%}.col-sm-push-4{left:33.33333333%}.col-sm-push-3{left:25%}.col-sm-push-2{left:16.66666667%}.col-sm-push-1{left:8.33333333%}.col-sm-push-0{left:auto}.col-sm-offset-12{margin-left:100%}.col-sm-offset-11{margin-left:91.66666667%}.col-sm-offset-10{margin-left:83.33333333%}.col-sm-offset-9{margin-left:75%}.col-sm-offset-8{margin-left:66.66666667%}.col-sm-offset-7{margin-left:58.33333333%}.col-sm-offset-6{margin-left:50%}.col-sm-offset-5{margin-left:41.66666667%}.col-sm-offset-4{margin-left:33.33333333%}.col-sm-offset-3{margin-left:25%}.col-sm-offset-2{margin-left:16.66666667%}.col-sm-offset-1{margin-left:8.33333333%}.col-sm-offset-0{margin-left:0%}}@media (min-width:992px){.col-md-1,.col-md-2,.col-md-3,.col-md-4,.col-md-5,.col-md-6,.col-md-7,.col-md-8,.col-md-9,.col-md-10,.col-md-11,.col-md-12{float:left}.col-md-12{width:100%}.col-md-11{width:91.66666667%}.col-md-10{width:83.33333333%}.col-md-9{width:75%}.col-md-8{width:66.66666667%}.col-md-7{width:58.33333333%}.col-md-6{width:50%}.col-md-5{width:41.66666667%}.col-md-4{width:33.33333333%}.col-md-3{width:25%}.col-md-2{width:16.66666667%}.col-md-1{width:8.33333333%}.col-md-pull-12{right:100%}.col-md-pull-11{right:91.66666667%}.col-md-pull-10{right:83.33333333%}.col-md-pull-9{right:75%}.col-md-pull-8{right:66.66666667%}.col-md-pull-7{right:58.33333333%}.col-md-pull-6{right:50%}.col-md-pull-5{right:41.66666667%}.col-md-pull-4{right:33.33333333%}.col-md-pull-3{right:25%}.col-md-pull-2{right:16.66666667%}.col-md-pull-1{right:8.33333333%}.col-md-pull-0{right:auto}.col-md-push-12{left:100%}.col-md-push-11{left:91.66666667%}.col-md-push-10{left:83.33333333%}.col-md-push-9{left:75%}.col-md-push-8{left:66.66666667%}.col-md-push-7{left:58.33333333%}.col-md-push-6{left:50%}.col-md-push-5{left:41.66666667%}.col-md-push-4{left:33.33333333%}.col-md-push-3{left:25%}.col-md-push-2{left:16.66666667%}.col-md-push-1{left:8.33333333%}.col-md-push-0{left:auto}.col-md-offset-12{margin-left:100%}.col-md-offset-11{margin-left:91.66666667%}.col-md-offset-10{margin-left:83.33333333%}.col-md-offset-9{margin-left:75%}.col-md-offset-8{margin-left:66.66666667%}.col-md-offset-7{margin-left:58.33333333%}.col-md-offset-6{margin-left:50%}.col-md-offset-5{margin-left:41.66666667%}.col-md-offset-4{margin-left:33.33333333%}.col-md-offset-3{margin-left:25%}.col-md-offset-2{margin-left:16.66666667%}.col-md-offset-1{margin-left:8.33333333%}.col-md-offset-0{margin-left:0%}}@media (min-width:1200px){.col-lg-1,.col-lg-2,.col-lg-3,.col-lg-4,.col-lg-5,.col-lg-6,.col-lg-7,.col-lg-8,.col-lg-9,.col-lg-10,.col-lg-11,.col-lg-12{float:left}.col-lg-12{width:100%}.col-lg-11{width:91.66666667%}.col-lg-10{width:83.33333333%}.col-lg-9{width:75%}.col-lg-8{width:66.66666667%}.col-lg-7{width:58.33333333%}.col-lg-6{width:50%}.col-lg-5{width:41.66666667%}.col-lg-4{width:33.33333333%}.col-lg-3{width:25%}.col-lg-2{width:16.66666667%}.col-lg-1{width:8.33333333%}.col-lg-pull-12{right:100%}.col-lg-pull-11{right:91.66666667%}.col-lg-pull-10{right:83.33333333%}.col-lg-pull-9{right:75%}.col-lg-pull-8{right:66.66666667%}.col-lg-pull-7{right:58.33333333%}.col-lg-pull-6{right:50%}.col-lg-pull-5{right:41.66666667%}.col-lg-pull-4{right:33.33333333%}.col-lg-pull-3{right:25%}.col-lg-pull-2{right:16.66666667%}.col-lg-pull-1{right:8.33333333%}.col-lg-pull-0{right:auto}.col-lg-push-12{left:100%}.col-lg-push-11{left:91.66666667%}.col-lg-push-10{left:83.33333333%}.col-lg-push-9{left:75%}.col-lg-push-8{left:66.66666667%}.col-lg-push-7{left:58.33333333%}.col-lg-push-6{left:50%}.col-lg-push-5{left:41.66666667%}.col-lg-push-4{left:33.33333333%}.col-lg-push-3{left:25%}.col-lg-push-2{left:16.66666667%}.col-lg-push-1{left:8.33333333%}.col-lg-push-0{left:auto}.col-lg-offset-12{margin-left:100%}.col-lg-offset-11{margin-left:91.66666667%}.col-lg-offset-10{margin-left:83.33333333%}.col-lg-offset-9{margin-left:75%}.col-lg-offset-8{margin-left:66.66666667%}.col-lg-offset-7{margin-left:58.33333333%}.col-lg-offset-6{margin-left:50%}.col-lg-offset-5{margin-left:41.66666667%}.col-lg-offset-4{margin-left:33.33333333%}.col-lg-offset-3{margin-left:25%}.col-lg-offset-2{margin-left:16.66666667%}.col-lg-offset-1{margin-left:8.33333333%}.col-lg-offset-0{margin-left:0%}}table{background-color:transparent}caption{padding-top:8px;padding-bottom:8px;color:#b4bcc2;text-align:left}th{text-align:left}.table{width:100%;max-width:100%;margin-bottom:21px}.table&gt;thead&gt;tr&gt;th,.table&gt;tbody&gt;tr&gt;th,.table&gt;tfoot&gt;tr&gt;th,.table&gt;thead&gt;tr&gt;td,.table&gt;tbody&gt;tr&gt;td,.table&gt;tfoot&gt;tr&gt;td{padding:8px;line-height:1.42857143;vertical-align:top;border-top:1px solid #ecf0f1}.table&gt;thead&gt;tr&gt;th{vertical-align:bottom;border-bottom:2px solid #ecf0f1}.table&gt;caption+thead&gt;tr:first-child&gt;th,.table&gt;colgroup+thead&gt;tr:first-child&gt;th,.table&gt;thead:first-child&gt;tr:first-child&gt;th,.table&gt;caption+thead&gt;tr:first-child&gt;td,.table&gt;colgroup+thead&gt;tr:first-child&gt;td,.table&gt;thead:first-child&gt;tr:first-child&gt;td{border-top:0}.table&gt;tbody+tbody{border-top:2px solid #ecf0f1}.table .table{background-color:#ffffff}.table-condensed&gt;thead&gt;tr&gt;th,.table-condensed&gt;tbody&gt;tr&gt;th,.table-condensed&gt;tfoot&gt;tr&gt;th,.table-condensed&gt;thead&gt;tr&gt;td,.table-condensed&gt;tbody&gt;tr&gt;td,.table-condensed&gt;tfoot&gt;tr&gt;td{padding:5px}.table-bordered{border:1px solid #ecf0f1}.table-bordered&gt;thead&gt;tr&gt;th,.table-bordered&gt;tbody&gt;tr&gt;th,.table-bordered&gt;tfoot&gt;tr&gt;th,.table-bordered&gt;thead&gt;tr&gt;td,.table-bordered&gt;tbody&gt;tr&gt;td,.table-bordered&gt;tfoot&gt;tr&gt;td{border:1px solid #ecf0f1}.table-bordered&gt;thead&gt;tr&gt;th,.table-bordered&gt;thead&gt;tr&gt;td{border-bottom-width:2px}.table-striped&gt;tbody&gt;tr:nth-of-type(odd){background-color:#f9f9f9}.table-hover&gt;tbody&gt;tr:hover{background-color:#ecf0f1}table col[class*=&quot;col-&quot;]{position:static;float:none;display:table-column}table td[class*=&quot;col-&quot;],table th[class*=&quot;col-&quot;]{position:static;float:none;display:table-cell}.table&gt;thead&gt;tr&gt;td.active,.table&gt;tbody&gt;tr&gt;td.active,.table&gt;tfoot&gt;tr&gt;td.active,.table&gt;thead&gt;tr&gt;th.active,.table&gt;tbody&gt;tr&gt;th.active,.table&gt;tfoot&gt;tr&gt;th.active,.table&gt;thead&gt;tr.active&gt;td,.table&gt;tbody&gt;tr.active&gt;td,.table&gt;tfoot&gt;tr.active&gt;td,.table&gt;thead&gt;tr.active&gt;th,.table&gt;tbody&gt;tr.active&gt;th,.table&gt;tfoot&gt;tr.active&gt;th{background-color:#ecf0f1}.table-hover&gt;tbody&gt;tr&gt;td.active:hover,.table-hover&gt;tbody&gt;tr&gt;th.active:hover,.table-hover&gt;tbody&gt;tr.active:hover&gt;td,.table-hover&gt;tbody&gt;tr:hover&gt;.active,.table-hover&gt;tbody&gt;tr.active:hover&gt;th{background-color:#dde4e6}.table&gt;thead&gt;tr&gt;td.success,.table&gt;tbody&gt;tr&gt;td.success,.table&gt;tfoot&gt;tr&gt;td.success,.table&gt;thead&gt;tr&gt;th.success,.table&gt;tbody&gt;tr&gt;th.success,.table&gt;tfoot&gt;tr&gt;th.success,.table&gt;thead&gt;tr.success&gt;td,.table&gt;tbody&gt;tr.success&gt;td,.table&gt;tfoot&gt;tr.success&gt;td,.table&gt;thead&gt;tr.success&gt;th,.table&gt;tbody&gt;tr.success&gt;th,.table&gt;tfoot&gt;tr.success&gt;th{background-color:#18bc9c}.table-hover&gt;tbody&gt;tr&gt;td.success:hover,.table-hover&gt;tbody&gt;tr&gt;th.success:hover,.table-hover&gt;tbody&gt;tr.success:hover&gt;td,.table-hover&gt;tbody&gt;tr:hover&gt;.success,.table-hover&gt;tbody&gt;tr.success:hover&gt;th{background-color:#15a589}.table&gt;thead&gt;tr&gt;td.info,.table&gt;tbody&gt;tr&gt;td.info,.table&gt;tfoot&gt;tr&gt;td.info,.table&gt;thead&gt;tr&gt;th.info,.table&gt;tbody&gt;tr&gt;th.info,.table&gt;tfoot&gt;tr&gt;th.info,.table&gt;thead&gt;tr.info&gt;td,.table&gt;tbody&gt;tr.info&gt;td,.table&gt;tfoot&gt;tr.info&gt;td,.table&gt;thead&gt;tr.info&gt;th,.table&gt;tbody&gt;tr.info&gt;th,.table&gt;tfoot&gt;tr.info&gt;th{background-color:#3498db}.table-hover&gt;tbody&gt;tr&gt;td.info:hover,.table-hover&gt;tbody&gt;tr&gt;th.info:hover,.table-hover&gt;tbody&gt;tr.info:hover&gt;td,.table-hover&gt;tbody&gt;tr:hover&gt;.info,.table-hover&gt;tbody&gt;tr.info:hover&gt;th{background-color:#258cd1}.table&gt;thead&gt;tr&gt;td.warning,.table&gt;tbody&gt;tr&gt;td.warning,.table&gt;tfoot&gt;tr&gt;td.warning,.table&gt;thead&gt;tr&gt;th.warning,.table&gt;tbody&gt;tr&gt;th.warning,.table&gt;tfoot&gt;tr&gt;th.warning,.table&gt;thead&gt;tr.warning&gt;td,.table&gt;tbody&gt;tr.warning&gt;td,.table&gt;tfoot&gt;tr.warning&gt;td,.table&gt;thead&gt;tr.warning&gt;th,.table&gt;tbody&gt;tr.warning&gt;th,.table&gt;tfoot&gt;tr.warning&gt;th{background-color:#f39c12}.table-hover&gt;tbody&gt;tr&gt;td.warning:hover,.table-hover&gt;tbody&gt;tr&gt;th.warning:hover,.table-hover&gt;tbody&gt;tr.warning:hover&gt;td,.table-hover&gt;tbody&gt;tr:hover&gt;.warning,.table-hover&gt;tbody&gt;tr.warning:hover&gt;th{background-color:#e08e0b}.table&gt;thead&gt;tr&gt;td.danger,.table&gt;tbody&gt;tr&gt;td.danger,.table&gt;tfoot&gt;tr&gt;td.danger,.table&gt;thead&gt;tr&gt;th.danger,.table&gt;tbody&gt;tr&gt;th.danger,.table&gt;tfoot&gt;tr&gt;th.danger,.table&gt;thead&gt;tr.danger&gt;td,.table&gt;tbody&gt;tr.danger&gt;td,.table&gt;tfoot&gt;tr.danger&gt;td,.table&gt;thead&gt;tr.danger&gt;th,.table&gt;tbody&gt;tr.danger&gt;th,.table&gt;tfoot&gt;tr.danger&gt;th{background-color:#e74c3c}.table-hover&gt;tbody&gt;tr&gt;td.danger:hover,.table-hover&gt;tbody&gt;tr&gt;th.danger:hover,.table-hover&gt;tbody&gt;tr.danger:hover&gt;td,.table-hover&gt;tbody&gt;tr:hover&gt;.danger,.table-hover&gt;tbody&gt;tr.danger:hover&gt;th{background-color:#e43725}.table-responsive{overflow-x:auto;min-height:0.01%}@media screen and (max-width:767px){.table-responsive{width:100%;margin-bottom:15.75px;overflow-y:hidden;-ms-overflow-style:-ms-autohiding-scrollbar;border:1px solid #ecf0f1}.table-responsive&gt;.table{margin-bottom:0}.table-responsive&gt;.table&gt;thead&gt;tr&gt;th,.table-responsive&gt;.table&gt;tbody&gt;tr&gt;th,.table-responsive&gt;.table&gt;tfoot&gt;tr&gt;th,.table-responsive&gt;.table&gt;thead&gt;tr&gt;td,.table-responsive&gt;.table&gt;tbody&gt;tr&gt;td,.table-responsive&gt;.table&gt;tfoot&gt;tr&gt;td{white-space:nowrap}.table-responsive&gt;.table-bordered{border:0}.table-responsive&gt;.table-bordered&gt;thead&gt;tr&gt;th:first-child,.table-responsive&gt;.table-bordered&gt;tbody&gt;tr&gt;th:first-child,.table-responsive&gt;.table-bordered&gt;tfoot&gt;tr&gt;th:first-child,.table-responsive&gt;.table-bordered&gt;thead&gt;tr&gt;td:first-child,.table-responsive&gt;.table-bordered&gt;tbody&gt;tr&gt;td:first-child,.table-responsive&gt;.table-bordered&gt;tfoot&gt;tr&gt;td:first-child{border-left:0}.table-responsive&gt;.table-bordered&gt;thead&gt;tr&gt;th:last-child,.table-responsive&gt;.table-bordered&gt;tbody&gt;tr&gt;th:last-child,.table-responsive&gt;.table-bordered&gt;tfoot&gt;tr&gt;th:last-child,.table-responsive&gt;.table-bordered&gt;thead&gt;tr&gt;td:last-child,.table-responsive&gt;.table-bordered&gt;tbody&gt;tr&gt;td:last-child,.table-responsive&gt;.table-bordered&gt;tfoot&gt;tr&gt;td:last-child{border-right:0}.table-responsive&gt;.table-bordered&gt;tbody&gt;tr:last-child&gt;th,.table-responsive&gt;.table-bordered&gt;tfoot&gt;tr:last-child&gt;th,.table-responsive&gt;.table-bordered&gt;tbody&gt;tr:last-child&gt;td,.table-responsive&gt;.table-bordered&gt;tfoot&gt;tr:last-child&gt;td{border-bottom:0}}fieldset{padding:0;margin:0;border:0;min-width:0}legend{display:block;width:100%;padding:0;margin-bottom:21px;font-size:22.5px;line-height:inherit;color:#2c3e50;border:0;border-bottom:1px solid transparent}label{display:inline-block;max-width:100%;margin-bottom:5px;font-weight:bold}input[type=&quot;search&quot;]{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box}input[type=&quot;radio&quot;],input[type=&quot;checkbox&quot;]{margin:4px 0 0;margin-top:1px \9;line-height:normal}input[type=&quot;file&quot;]{display:block}input[type=&quot;range&quot;]{display:block;width:100%}select[multiple],select[size]{height:auto}input[type=&quot;file&quot;]:focus,input[type=&quot;radio&quot;]:focus,input[type=&quot;checkbox&quot;]:focus{outline:5px auto -webkit-focus-ring-color;outline-offset:-2px}output{display:block;padding-top:11px;font-size:15px;line-height:1.42857143;color:#2c3e50}.form-control{display:block;width:100%;height:45px;padding:10px 15px;font-size:15px;line-height:1.42857143;color:#2c3e50;background-color:#ffffff;background-image:none;border:1px solid #dce4ec;border-radius:4px;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075);box-shadow:inset 0 1px 1px rgba(0,0,0,0.075);-webkit-transition:border-color ease-in-out .15s,-webkit-box-shadow ease-in-out .15s;-o-transition:border-color ease-in-out .15s,box-shadow ease-in-out .15s;transition:border-color ease-in-out .15s,box-shadow ease-in-out .15s}.form-control:focus{border-color:#2c3e50;outline:0;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 8px rgba(44,62,80,0.6);box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 8px rgba(44,62,80,0.6)}.form-control::-moz-placeholder{color:#acb6c0;opacity:1}.form-control:-ms-input-placeholder{color:#acb6c0}.form-control::-webkit-input-placeholder{color:#acb6c0}.form-control::-ms-expand{border:0;background-color:transparent}.form-control[disabled],.form-control[readonly],fieldset[disabled] .form-control{background-color:#ecf0f1;opacity:1}.form-control[disabled],fieldset[disabled] .form-control{cursor:not-allowed}textarea.form-control{height:auto}input[type=&quot;search&quot;]{-webkit-appearance:none}@media screen and (-webkit-min-device-pixel-ratio:0){input[type=&quot;date&quot;].form-control,input[type=&quot;time&quot;].form-control,input[type=&quot;datetime-local&quot;].form-control,input[type=&quot;month&quot;].form-control{line-height:45px}input[type=&quot;date&quot;].input-sm,input[type=&quot;time&quot;].input-sm,input[type=&quot;datetime-local&quot;].input-sm,input[type=&quot;month&quot;].input-sm,.input-group-sm input[type=&quot;date&quot;],.input-group-sm input[type=&quot;time&quot;],.input-group-sm input[type=&quot;datetime-local&quot;],.input-group-sm input[type=&quot;month&quot;]{line-height:35px}input[type=&quot;date&quot;].input-lg,input[type=&quot;time&quot;].input-lg,input[type=&quot;datetime-local&quot;].input-lg,input[type=&quot;month&quot;].input-lg,.input-group-lg input[type=&quot;date&quot;],.input-group-lg input[type=&quot;time&quot;],.input-group-lg input[type=&quot;datetime-local&quot;],.input-group-lg input[type=&quot;month&quot;]{line-height:66px}}.form-group{margin-bottom:15px}.radio,.checkbox{position:relative;display:block;margin-top:10px;margin-bottom:10px}.radio label,.checkbox label{min-height:21px;padding-left:20px;margin-bottom:0;font-weight:normal;cursor:pointer}.radio input[type=&quot;radio&quot;],.radio-inline input[type=&quot;radio&quot;],.checkbox input[type=&quot;checkbox&quot;],.checkbox-inline input[type=&quot;checkbox&quot;]{position:absolute;margin-left:-20px;margin-top:4px \9}.radio+.radio,.checkbox+.checkbox{margin-top:-5px}.radio-inline,.checkbox-inline{position:relative;display:inline-block;padding-left:20px;margin-bottom:0;vertical-align:middle;font-weight:normal;cursor:pointer}.radio-inline+.radio-inline,.checkbox-inline+.checkbox-inline{margin-top:0;margin-left:10px}input[type=&quot;radio&quot;][disabled],input[type=&quot;checkbox&quot;][disabled],input[type=&quot;radio&quot;].disabled,input[type=&quot;checkbox&quot;].disabled,fieldset[disabled] input[type=&quot;radio&quot;],fieldset[disabled] input[type=&quot;checkbox&quot;]{cursor:not-allowed}.radio-inline.disabled,.checkbox-inline.disabled,fieldset[disabled] .radio-inline,fieldset[disabled] .checkbox-inline{cursor:not-allowed}.radio.disabled label,.checkbox.disabled label,fieldset[disabled] .radio label,fieldset[disabled] .checkbox label{cursor:not-allowed}.form-control-static{padding-top:11px;padding-bottom:11px;margin-bottom:0;min-height:36px}.form-control-static.input-lg,.form-control-static.input-sm{padding-left:0;padding-right:0}.input-sm{height:35px;padding:6px 9px;font-size:13px;line-height:1.5;border-radius:3px}select.input-sm{height:35px;line-height:35px}textarea.input-sm,select[multiple].input-sm{height:auto}.form-group-sm .form-control{height:35px;padding:6px 9px;font-size:13px;line-height:1.5;border-radius:3px}.form-group-sm select.form-control{height:35px;line-height:35px}.form-group-sm textarea.form-control,.form-group-sm select[multiple].form-control{height:auto}.form-group-sm .form-control-static{height:35px;min-height:34px;padding:7px 9px;font-size:13px;line-height:1.5}.input-lg{height:66px;padding:18px 27px;font-size:19px;line-height:1.3333333;border-radius:6px}select.input-lg{height:66px;line-height:66px}textarea.input-lg,select[multiple].input-lg{height:auto}.form-group-lg .form-control{height:66px;padding:18px 27px;font-size:19px;line-height:1.3333333;border-radius:6px}.form-group-lg select.form-control{height:66px;line-height:66px}.form-group-lg textarea.form-control,.form-group-lg select[multiple].form-control{height:auto}.form-group-lg .form-control-static{height:66px;min-height:40px;padding:19px 27px;font-size:19px;line-height:1.3333333}.has-feedback{position:relative}.has-feedback .form-control{padding-right:56.25px}.form-control-feedback{position:absolute;top:0;right:0;z-index:2;display:block;width:45px;height:45px;line-height:45px;text-align:center;pointer-events:none}.input-lg+.form-control-feedback,.input-group-lg+.form-control-feedback,.form-group-lg .form-control+.form-control-feedback{width:66px;height:66px;line-height:66px}.input-sm+.form-control-feedback,.input-group-sm+.form-control-feedback,.form-group-sm .form-control+.form-control-feedback{width:35px;height:35px;line-height:35px}.has-success .help-block,.has-success .control-label,.has-success .radio,.has-success .checkbox,.has-success .radio-inline,.has-success .checkbox-inline,.has-success.radio label,.has-success.checkbox label,.has-success.radio-inline label,.has-success.checkbox-inline label{color:#ffffff}.has-success .form-control{border-color:#ffffff;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075);box-shadow:inset 0 1px 1px rgba(0,0,0,0.075)}.has-success .form-control:focus{border-color:#e6e6e6;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 6px #fff;box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 6px #fff}.has-success .input-group-addon{color:#ffffff;border-color:#ffffff;background-color:#18bc9c}.has-success .form-control-feedback{color:#ffffff}.has-warning .help-block,.has-warning .control-label,.has-warning .radio,.has-warning .checkbox,.has-warning .radio-inline,.has-warning .checkbox-inline,.has-warning.radio label,.has-warning.checkbox label,.has-warning.radio-inline label,.has-warning.checkbox-inline label{color:#ffffff}.has-warning .form-control{border-color:#ffffff;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075);box-shadow:inset 0 1px 1px rgba(0,0,0,0.075)}.has-warning .form-control:focus{border-color:#e6e6e6;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 6px #fff;box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 6px #fff}.has-warning .input-group-addon{color:#ffffff;border-color:#ffffff;background-color:#f39c12}.has-warning .form-control-feedback{color:#ffffff}.has-error .help-block,.has-error .control-label,.has-error .radio,.has-error .checkbox,.has-error .radio-inline,.has-error .checkbox-inline,.has-error.radio label,.has-error.checkbox label,.has-error.radio-inline label,.has-error.checkbox-inline label{color:#ffffff}.has-error .form-control{border-color:#ffffff;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075);box-shadow:inset 0 1px 1px rgba(0,0,0,0.075)}.has-error .form-control:focus{border-color:#e6e6e6;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 6px #fff;box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 6px #fff}.has-error .input-group-addon{color:#ffffff;border-color:#ffffff;background-color:#e74c3c}.has-error .form-control-feedback{color:#ffffff}.has-feedback label~.form-control-feedback{top:26px}.has-feedback label.sr-only~.form-control-feedback{top:0}.help-block{display:block;margin-top:5px;margin-bottom:10px;color:#597ea2}@media (min-width:768px){.form-inline .form-group{display:inline-block;margin-bottom:0;vertical-align:middle}.form-inline .form-control{display:inline-block;width:auto;vertical-align:middle}.form-inline .form-control-static{display:inline-block}.form-inline .input-group{display:inline-table;vertical-align:middle}.form-inline .input-group .input-group-addon,.form-inline .input-group .input-group-btn,.form-inline .input-group .form-control{width:auto}.form-inline .input-group&gt;.form-control{width:100%}.form-inline .control-label{margin-bottom:0;vertical-align:middle}.form-inline .radio,.form-inline .checkbox{display:inline-block;margin-top:0;margin-bottom:0;vertical-align:middle}.form-inline .radio label,.form-inline .checkbox label{padding-left:0}.form-inline .radio input[type=&quot;radio&quot;],.form-inline .checkbox input[type=&quot;checkbox&quot;]{position:relative;margin-left:0}.form-inline .has-feedback .form-control-feedback{top:0}}.form-horizontal .radio,.form-horizontal .checkbox,.form-horizontal .radio-inline,.form-horizontal .checkbox-inline{margin-top:0;margin-bottom:0;padding-top:11px}.form-horizontal .radio,.form-horizontal .checkbox{min-height:32px}.form-horizontal .form-group{margin-left:-15px;margin-right:-15px}@media (min-width:768px){.form-horizontal .control-label{text-align:right;margin-bottom:0;padding-top:11px}}.form-horizontal .has-feedback .form-control-feedback{right:15px}@media (min-width:768px){.form-horizontal .form-group-lg .control-label{padding-top:19px;font-size:19px}}@media (min-width:768px){.form-horizontal .form-group-sm .control-label{padding-top:7px;font-size:13px}}.btn{display:inline-block;margin-bottom:0;font-weight:normal;text-align:center;vertical-align:middle;-ms-touch-action:manipulation;touch-action:manipulation;cursor:pointer;background-image:none;border:1px solid transparent;white-space:nowrap;padding:10px 15px;font-size:15px;line-height:1.42857143;border-radius:4px;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.btn:focus,.btn:active:focus,.btn.active:focus,.btn.focus,.btn:active.focus,.btn.active.focus{outline:5px auto -webkit-focus-ring-color;outline-offset:-2px}.btn:hover,.btn:focus,.btn.focus{color:#ffffff;text-decoration:none}.btn:active,.btn.active{outline:0;background-image:none;-webkit-box-shadow:inset 0 3px 5px rgba(0,0,0,0.125);box-shadow:inset 0 3px 5px rgba(0,0,0,0.125)}.btn.disabled,.btn[disabled],fieldset[disabled] .btn{cursor:not-allowed;opacity:0.65;filter:alpha(opacity=65);-webkit-box-shadow:none;box-shadow:none}a.btn.disabled,fieldset[disabled] a.btn{pointer-events:none}.btn-default{color:#ffffff;background-color:#95a5a6;border-color:#95a5a6}.btn-default:focus,.btn-default.focus{color:#ffffff;background-color:#798d8f;border-color:#566566}.btn-default:hover{color:#ffffff;background-color:#798d8f;border-color:#74898a}.btn-default:active,.btn-default.active,.open&gt;.dropdown-toggle.btn-default{color:#ffffff;background-color:#798d8f;border-color:#74898a}.btn-default:active:hover,.btn-default.active:hover,.open&gt;.dropdown-toggle.btn-default:hover,.btn-default:active:focus,.btn-default.active:focus,.open&gt;.dropdown-toggle.btn-default:focus,.btn-default:active.focus,.btn-default.active.focus,.open&gt;.dropdown-toggle.btn-default.focus{color:#ffffff;background-color:#687b7c;border-color:#566566}.btn-default:active,.btn-default.active,.open&gt;.dropdown-toggle.btn-default{background-image:none}.btn-default.disabled:hover,.btn-default[disabled]:hover,fieldset[disabled] .btn-default:hover,.btn-default.disabled:focus,.btn-default[disabled]:focus,fieldset[disabled] .btn-default:focus,.btn-default.disabled.focus,.btn-default[disabled].focus,fieldset[disabled] .btn-default.focus{background-color:#95a5a6;border-color:#95a5a6}.btn-default .badge{color:#95a5a6;background-color:#ffffff}.btn-primary{color:#ffffff;background-color:#2c3e50;border-color:#2c3e50}.btn-primary:focus,.btn-primary.focus{color:#ffffff;background-color:#1a242f;border-color:#000000}.btn-primary:hover{color:#ffffff;background-color:#1a242f;border-color:#161f29}.btn-primary:active,.btn-primary.active,.open&gt;.dropdown-toggle.btn-primary{color:#ffffff;background-color:#1a242f;border-color:#161f29}.btn-primary:active:hover,.btn-primary.active:hover,.open&gt;.dropdown-toggle.btn-primary:hover,.btn-primary:active:focus,.btn-primary.active:focus,.open&gt;.dropdown-toggle.btn-primary:focus,.btn-primary:active.focus,.btn-primary.active.focus,.open&gt;.dropdown-toggle.btn-primary.focus{color:#ffffff;background-color:#0d1318;border-color:#000000}.btn-primary:active,.btn-primary.active,.open&gt;.dropdown-toggle.btn-primary{background-image:none}.btn-primary.disabled:hover,.btn-primary[disabled]:hover,fieldset[disabled] .btn-primary:hover,.btn-primary.disabled:focus,.btn-primary[disabled]:focus,fieldset[disabled] .btn-primary:focus,.btn-primary.disabled.focus,.btn-primary[disabled].focus,fieldset[disabled] .btn-primary.focus{background-color:#2c3e50;border-color:#2c3e50}.btn-primary .badge{color:#2c3e50;background-color:#ffffff}.btn-success{color:#ffffff;background-color:#18bc9c;border-color:#18bc9c}.btn-success:focus,.btn-success.focus{color:#ffffff;background-color:#128f76;border-color:#0a4b3e}.btn-success:hover{color:#ffffff;background-color:#128f76;border-color:#11866f}.btn-success:active,.btn-success.active,.open&gt;.dropdown-toggle.btn-success{color:#ffffff;background-color:#128f76;border-color:#11866f}.btn-success:active:hover,.btn-success.active:hover,.open&gt;.dropdown-toggle.btn-success:hover,.btn-success:active:focus,.btn-success.active:focus,.open&gt;.dropdown-toggle.btn-success:focus,.btn-success:active.focus,.btn-success.active.focus,.open&gt;.dropdown-toggle.btn-success.focus{color:#ffffff;background-color:#0e6f5c;border-color:#0a4b3e}.btn-success:active,.btn-success.active,.open&gt;.dropdown-toggle.btn-success{background-image:none}.btn-success.disabled:hover,.btn-success[disabled]:hover,fieldset[disabled] .btn-success:hover,.btn-success.disabled:focus,.btn-success[disabled]:focus,fieldset[disabled] .btn-success:focus,.btn-success.disabled.focus,.btn-success[disabled].focus,fieldset[disabled] .btn-success.focus{background-color:#18bc9c;border-color:#18bc9c}.btn-success .badge{color:#18bc9c;background-color:#ffffff}.btn-info{color:#ffffff;background-color:#3498db;border-color:#3498db}.btn-info:focus,.btn-info.focus{color:#ffffff;background-color:#217dbb;border-color:#16527a}.btn-info:hover{color:#ffffff;background-color:#217dbb;border-color:#2077b2}.btn-info:active,.btn-info.active,.open&gt;.dropdown-toggle.btn-info{color:#ffffff;background-color:#217dbb;border-color:#2077b2}.btn-info:active:hover,.btn-info.active:hover,.open&gt;.dropdown-toggle.btn-info:hover,.btn-info:active:focus,.btn-info.active:focus,.open&gt;.dropdown-toggle.btn-info:focus,.btn-info:active.focus,.btn-info.active.focus,.open&gt;.dropdown-toggle.btn-info.focus{color:#ffffff;background-color:#1c699d;border-color:#16527a}.btn-info:active,.btn-info.active,.open&gt;.dropdown-toggle.btn-info{background-image:none}.btn-info.disabled:hover,.btn-info[disabled]:hover,fieldset[disabled] .btn-info:hover,.btn-info.disabled:focus,.btn-info[disabled]:focus,fieldset[disabled] .btn-info:focus,.btn-info.disabled.focus,.btn-info[disabled].focus,fieldset[disabled] .btn-info.focus{background-color:#3498db;border-color:#3498db}.btn-info .badge{color:#3498db;background-color:#ffffff}.btn-warning{color:#ffffff;background-color:#f39c12;border-color:#f39c12}.btn-warning:focus,.btn-warning.focus{color:#ffffff;background-color:#c87f0a;border-color:#7f5006}.btn-warning:hover{color:#ffffff;background-color:#c87f0a;border-color:#be780a}.btn-warning:active,.btn-warning.active,.open&gt;.dropdown-toggle.btn-warning{color:#ffffff;background-color:#c87f0a;border-color:#be780a}.btn-warning:active:hover,.btn-warning.active:hover,.open&gt;.dropdown-toggle.btn-warning:hover,.btn-warning:active:focus,.btn-warning.active:focus,.open&gt;.dropdown-toggle.btn-warning:focus,.btn-warning:active.focus,.btn-warning.active.focus,.open&gt;.dropdown-toggle.btn-warning.focus{color:#ffffff;background-color:#a66908;border-color:#7f5006}.btn-warning:active,.btn-warning.active,.open&gt;.dropdown-toggle.btn-warning{background-image:none}.btn-warning.disabled:hover,.btn-warning[disabled]:hover,fieldset[disabled] .btn-warning:hover,.btn-warning.disabled:focus,.btn-warning[disabled]:focus,fieldset[disabled] .btn-warning:focus,.btn-warning.disabled.focus,.btn-warning[disabled].focus,fieldset[disabled] .btn-warning.focus{background-color:#f39c12;border-color:#f39c12}.btn-warning .badge{color:#f39c12;background-color:#ffffff}.btn-danger{color:#ffffff;background-color:#e74c3c;border-color:#e74c3c}.btn-danger:focus,.btn-danger.focus{color:#ffffff;background-color:#d62c1a;border-color:#921e12}.btn-danger:hover{color:#ffffff;background-color:#d62c1a;border-color:#cd2a19}.btn-danger:active,.btn-danger.active,.open&gt;.dropdown-toggle.btn-danger{color:#ffffff;background-color:#d62c1a;border-color:#cd2a19}.btn-danger:active:hover,.btn-danger.active:hover,.open&gt;.dropdown-toggle.btn-danger:hover,.btn-danger:active:focus,.btn-danger.active:focus,.open&gt;.dropdown-toggle.btn-danger:focus,.btn-danger:active.focus,.btn-danger.active.focus,.open&gt;.dropdown-toggle.btn-danger.focus{color:#ffffff;background-color:#b62516;border-color:#921e12}.btn-danger:active,.btn-danger.active,.open&gt;.dropdown-toggle.btn-danger{background-image:none}.btn-danger.disabled:hover,.btn-danger[disabled]:hover,fieldset[disabled] .btn-danger:hover,.btn-danger.disabled:focus,.btn-danger[disabled]:focus,fieldset[disabled] .btn-danger:focus,.btn-danger.disabled.focus,.btn-danger[disabled].focus,fieldset[disabled] .btn-danger.focus{background-color:#e74c3c;border-color:#e74c3c}.btn-danger .badge{color:#e74c3c;background-color:#ffffff}.btn-link{color:#18bc9c;font-weight:normal;border-radius:0}.btn-link,.btn-link:active,.btn-link.active,.btn-link[disabled],fieldset[disabled] .btn-link{background-color:transparent;-webkit-box-shadow:none;box-shadow:none}.btn-link,.btn-link:hover,.btn-link:focus,.btn-link:active{border-color:transparent}.btn-link:hover,.btn-link:focus{color:#18bc9c;text-decoration:underline;background-color:transparent}.btn-link[disabled]:hover,fieldset[disabled] .btn-link:hover,.btn-link[disabled]:focus,fieldset[disabled] .btn-link:focus{color:#b4bcc2;text-decoration:none}.btn-lg,.btn-group-lg&gt;.btn{padding:18px 27px;font-size:19px;line-height:1.3333333;border-radius:6px}.btn-sm,.btn-group-sm&gt;.btn{padding:6px 9px;font-size:13px;line-height:1.5;border-radius:3px}.btn-xs,.btn-group-xs&gt;.btn{padding:1px 5px;font-size:13px;line-height:1.5;border-radius:3px}.btn-block{display:block;width:100%}.btn-block+.btn-block{margin-top:5px}input[type=&quot;submit&quot;].btn-block,input[type=&quot;reset&quot;].btn-block,input[type=&quot;button&quot;].btn-block{width:100%}.fade{opacity:0;-webkit-transition:opacity 0.15s linear;-o-transition:opacity 0.15s linear;transition:opacity 0.15s linear}.fade.in{opacity:1}.collapse{display:none}.collapse.in{display:block}tr.collapse.in{display:table-row}tbody.collapse.in{display:table-row-group}.collapsing{position:relative;height:0;overflow:hidden;-webkit-transition-property:height, visibility;-o-transition-property:height, visibility;transition-property:height, visibility;-webkit-transition-duration:0.35s;-o-transition-duration:0.35s;transition-duration:0.35s;-webkit-transition-timing-function:ease;-o-transition-timing-function:ease;transition-timing-function:ease}.caret{display:inline-block;width:0;height:0;margin-left:2px;vertical-align:middle;border-top:4px dashed;border-top:4px solid \9;border-right:4px solid transparent;border-left:4px solid transparent}.dropup,.dropdown{position:relative}.dropdown-toggle:focus{outline:0}.dropdown-menu{position:absolute;top:100%;left:0;z-index:1000;display:none;float:left;min-width:160px;padding:5px 0;margin:2px 0 0;list-style:none;font-size:15px;text-align:left;background-color:#ffffff;border:1px solid #cccccc;border:1px solid rgba(0,0,0,0.15);border-radius:4px;-webkit-box-shadow:0 6px 12px rgba(0,0,0,0.175);box-shadow:0 6px 12px rgba(0,0,0,0.175);-webkit-background-clip:padding-box;background-clip:padding-box}.dropdown-menu.pull-right{right:0;left:auto}.dropdown-menu .divider{height:1px;margin:9.5px 0;overflow:hidden;background-color:#e5e5e5}.dropdown-menu&gt;li&gt;a{display:block;padding:3px 20px;clear:both;font-weight:normal;line-height:1.42857143;color:#7b8a8b;white-space:nowrap}.dropdown-menu&gt;li&gt;a:hover,.dropdown-menu&gt;li&gt;a:focus{text-decoration:none;color:#ffffff;background-color:#2c3e50}.dropdown-menu&gt;.active&gt;a,.dropdown-menu&gt;.active&gt;a:hover,.dropdown-menu&gt;.active&gt;a:focus{color:#ffffff;text-decoration:none;outline:0;background-color:#2c3e50}.dropdown-menu&gt;.disabled&gt;a,.dropdown-menu&gt;.disabled&gt;a:hover,.dropdown-menu&gt;.disabled&gt;a:focus{color:#b4bcc2}.dropdown-menu&gt;.disabled&gt;a:hover,.dropdown-menu&gt;.disabled&gt;a:focus{text-decoration:none;background-color:transparent;background-image:none;filter:progid:DXImageTransform.Microsoft.gradient(enabled=false);cursor:not-allowed}.open&gt;.dropdown-menu{display:block}.open&gt;a{outline:0}.dropdown-menu-right{left:auto;right:0}.dropdown-menu-left{left:0;right:auto}.dropdown-header{display:block;padding:3px 20px;font-size:13px;line-height:1.42857143;color:#b4bcc2;white-space:nowrap}.dropdown-backdrop{position:fixed;left:0;right:0;bottom:0;top:0;z-index:990}.pull-right&gt;.dropdown-menu{right:0;left:auto}.dropup .caret,.navbar-fixed-bottom .dropdown .caret{border-top:0;border-bottom:4px dashed;border-bottom:4px solid \9;content:&quot;&quot;}.dropup .dropdown-menu,.navbar-fixed-bottom .dropdown .dropdown-menu{top:auto;bottom:100%;margin-bottom:2px}@media (min-width:768px){.navbar-right .dropdown-menu{left:auto;right:0}.navbar-right .dropdown-menu-left{left:0;right:auto}}.btn-group,.btn-group-vertical{position:relative;display:inline-block;vertical-align:middle}.btn-group&gt;.btn,.btn-group-vertical&gt;.btn{position:relative;float:left}.btn-group&gt;.btn:hover,.btn-group-vertical&gt;.btn:hover,.btn-group&gt;.btn:focus,.btn-group-vertical&gt;.btn:focus,.btn-group&gt;.btn:active,.btn-group-vertical&gt;.btn:active,.btn-group&gt;.btn.active,.btn-group-vertical&gt;.btn.active{z-index:2}.btn-group .btn+.btn,.btn-group .btn+.btn-group,.btn-group .btn-group+.btn,.btn-group .btn-group+.btn-group{margin-left:-1px}.btn-toolbar{margin-left:-5px}.btn-toolbar .btn,.btn-toolbar .btn-group,.btn-toolbar .input-group{float:left}.btn-toolbar&gt;.btn,.btn-toolbar&gt;.btn-group,.btn-toolbar&gt;.input-group{margin-left:5px}.btn-group&gt;.btn:not(:first-child):not(:last-child):not(.dropdown-toggle){border-radius:0}.btn-group&gt;.btn:first-child{margin-left:0}.btn-group&gt;.btn:first-child:not(:last-child):not(.dropdown-toggle){border-bottom-right-radius:0;border-top-right-radius:0}.btn-group&gt;.btn:last-child:not(:first-child),.btn-group&gt;.dropdown-toggle:not(:first-child){border-bottom-left-radius:0;border-top-left-radius:0}.btn-group&gt;.btn-group{float:left}.btn-group&gt;.btn-group:not(:first-child):not(:last-child)&gt;.btn{border-radius:0}.btn-group&gt;.btn-group:first-child:not(:last-child)&gt;.btn:last-child,.btn-group&gt;.btn-group:first-child:not(:last-child)&gt;.dropdown-toggle{border-bottom-right-radius:0;border-top-right-radius:0}.btn-group&gt;.btn-group:last-child:not(:first-child)&gt;.btn:first-child{border-bottom-left-radius:0;border-top-left-radius:0}.btn-group .dropdown-toggle:active,.btn-group.open .dropdown-toggle{outline:0}.btn-group&gt;.btn+.dropdown-toggle{padding-left:8px;padding-right:8px}.btn-group&gt;.btn-lg+.dropdown-toggle{padding-left:12px;padding-right:12px}.btn-group.open .dropdown-toggle{-webkit-box-shadow:inset 0 3px 5px rgba(0,0,0,0.125);box-shadow:inset 0 3px 5px rgba(0,0,0,0.125)}.btn-group.open .dropdown-toggle.btn-link{-webkit-box-shadow:none;box-shadow:none}.btn .caret{margin-left:0}.btn-lg .caret{border-width:5px 5px 0;border-bottom-width:0}.dropup .btn-lg .caret{border-width:0 5px 5px}.btn-group-vertical&gt;.btn,.btn-group-vertical&gt;.btn-group,.btn-group-vertical&gt;.btn-group&gt;.btn{display:block;float:none;width:100%;max-width:100%}.btn-group-vertical&gt;.btn-group&gt;.btn{float:none}.btn-group-vertical&gt;.btn+.btn,.btn-group-vertical&gt;.btn+.btn-group,.btn-group-vertical&gt;.btn-group+.btn,.btn-group-vertical&gt;.btn-group+.btn-group{margin-top:-1px;margin-left:0}.btn-group-vertical&gt;.btn:not(:first-child):not(:last-child){border-radius:0}.btn-group-vertical&gt;.btn:first-child:not(:last-child){border-top-right-radius:4px;border-top-left-radius:4px;border-bottom-right-radius:0;border-bottom-left-radius:0}.btn-group-vertical&gt;.btn:last-child:not(:first-child){border-top-right-radius:0;border-top-left-radius:0;border-bottom-right-radius:4px;border-bottom-left-radius:4px}.btn-group-vertical&gt;.btn-group:not(:first-child):not(:last-child)&gt;.btn{border-radius:0}.btn-group-vertical&gt;.btn-group:first-child:not(:last-child)&gt;.btn:last-child,.btn-group-vertical&gt;.btn-group:first-child:not(:last-child)&gt;.dropdown-toggle{border-bottom-right-radius:0;border-bottom-left-radius:0}.btn-group-vertical&gt;.btn-group:last-child:not(:first-child)&gt;.btn:first-child{border-top-right-radius:0;border-top-left-radius:0}.btn-group-justified{display:table;width:100%;table-layout:fixed;border-collapse:separate}.btn-group-justified&gt;.btn,.btn-group-justified&gt;.btn-group{float:none;display:table-cell;width:1%}.btn-group-justified&gt;.btn-group .btn{width:100%}.btn-group-justified&gt;.btn-group .dropdown-menu{left:auto}[data-toggle=&quot;buttons&quot;]&gt;.btn input[type=&quot;radio&quot;],[data-toggle=&quot;buttons&quot;]&gt;.btn-group&gt;.btn input[type=&quot;radio&quot;],[data-toggle=&quot;buttons&quot;]&gt;.btn input[type=&quot;checkbox&quot;],[data-toggle=&quot;buttons&quot;]&gt;.btn-group&gt;.btn input[type=&quot;checkbox&quot;]{position:absolute;clip:rect(0, 0, 0, 0);pointer-events:none}.input-group{position:relative;display:table;border-collapse:separate}.input-group[class*=&quot;col-&quot;]{float:none;padding-left:0;padding-right:0}.input-group .form-control{position:relative;z-index:2;float:left;width:100%;margin-bottom:0}.input-group .form-control:focus{z-index:3}.input-group-lg&gt;.form-control,.input-group-lg&gt;.input-group-addon,.input-group-lg&gt;.input-group-btn&gt;.btn{height:66px;padding:18px 27px;font-size:19px;line-height:1.3333333;border-radius:6px}select.input-group-lg&gt;.form-control,select.input-group-lg&gt;.input-group-addon,select.input-group-lg&gt;.input-group-btn&gt;.btn{height:66px;line-height:66px}textarea.input-group-lg&gt;.form-control,textarea.input-group-lg&gt;.input-group-addon,textarea.input-group-lg&gt;.input-group-btn&gt;.btn,select[multiple].input-group-lg&gt;.form-control,select[multiple].input-group-lg&gt;.input-group-addon,select[multiple].input-group-lg&gt;.input-group-btn&gt;.btn{height:auto}.input-group-sm&gt;.form-control,.input-group-sm&gt;.input-group-addon,.input-group-sm&gt;.input-group-btn&gt;.btn{height:35px;padding:6px 9px;font-size:13px;line-height:1.5;border-radius:3px}select.input-group-sm&gt;.form-control,select.input-group-sm&gt;.input-group-addon,select.input-group-sm&gt;.input-group-btn&gt;.btn{height:35px;line-height:35px}textarea.input-group-sm&gt;.form-control,textarea.input-group-sm&gt;.input-group-addon,textarea.input-group-sm&gt;.input-group-btn&gt;.btn,select[multiple].input-group-sm&gt;.form-control,select[multiple].input-group-sm&gt;.input-group-addon,select[multiple].input-group-sm&gt;.input-group-btn&gt;.btn{height:auto}.input-group-addon,.input-group-btn,.input-group .form-control{display:table-cell}.input-group-addon:not(:first-child):not(:last-child),.input-group-btn:not(:first-child):not(:last-child),.input-group .form-control:not(:first-child):not(:last-child){border-radius:0}.input-group-addon,.input-group-btn{width:1%;white-space:nowrap;vertical-align:middle}.input-group-addon{padding:10px 15px;font-size:15px;font-weight:normal;line-height:1;color:#2c3e50;text-align:center;background-color:#ecf0f1;border:1px solid #dce4ec;border-radius:4px}.input-group-addon.input-sm{padding:6px 9px;font-size:13px;border-radius:3px}.input-group-addon.input-lg{padding:18px 27px;font-size:19px;border-radius:6px}.input-group-addon input[type=&quot;radio&quot;],.input-group-addon input[type=&quot;checkbox&quot;]{margin-top:0}.input-group .form-control:first-child,.input-group-addon:first-child,.input-group-btn:first-child&gt;.btn,.input-group-btn:first-child&gt;.btn-group&gt;.btn,.input-group-btn:first-child&gt;.dropdown-toggle,.input-group-btn:last-child&gt;.btn:not(:last-child):not(.dropdown-toggle),.input-group-btn:last-child&gt;.btn-group:not(:last-child)&gt;.btn{border-bottom-right-radius:0;border-top-right-radius:0}.input-group-addon:first-child{border-right:0}.input-group .form-control:last-child,.input-group-addon:last-child,.input-group-btn:last-child&gt;.btn,.input-group-btn:last-child&gt;.btn-group&gt;.btn,.input-group-btn:last-child&gt;.dropdown-toggle,.input-group-btn:first-child&gt;.btn:not(:first-child),.input-group-btn:first-child&gt;.btn-group:not(:first-child)&gt;.btn{border-bottom-left-radius:0;border-top-left-radius:0}.input-group-addon:last-child{border-left:0}.input-group-btn{position:relative;font-size:0;white-space:nowrap}.input-group-btn&gt;.btn{position:relative}.input-group-btn&gt;.btn+.btn{margin-left:-1px}.input-group-btn&gt;.btn:hover,.input-group-btn&gt;.btn:focus,.input-group-btn&gt;.btn:active{z-index:2}.input-group-btn:first-child&gt;.btn,.input-group-btn:first-child&gt;.btn-group{margin-right:-1px}.input-group-btn:last-child&gt;.btn,.input-group-btn:last-child&gt;.btn-group{z-index:2;margin-left:-1px}.nav{margin-bottom:0;padding-left:0;list-style:none}.nav&gt;li{position:relative;display:block}.nav&gt;li&gt;a{position:relative;display:block;padding:10px 15px}.nav&gt;li&gt;a:hover,.nav&gt;li&gt;a:focus{text-decoration:none;background-color:#ecf0f1}.nav&gt;li.disabled&gt;a{color:#b4bcc2}.nav&gt;li.disabled&gt;a:hover,.nav&gt;li.disabled&gt;a:focus{color:#b4bcc2;text-decoration:none;background-color:transparent;cursor:not-allowed}.nav .open&gt;a,.nav .open&gt;a:hover,.nav .open&gt;a:focus{background-color:#ecf0f1;border-color:#18bc9c}.nav .nav-divider{height:1px;margin:9.5px 0;overflow:hidden;background-color:#e5e5e5}.nav&gt;li&gt;a&gt;img{max-width:none}.nav-tabs{border-bottom:1px solid #ecf0f1}.nav-tabs&gt;li{float:left;margin-bottom:-1px}.nav-tabs&gt;li&gt;a{margin-right:2px;line-height:1.42857143;border:1px solid transparent;border-radius:4px 4px 0 0}.nav-tabs&gt;li&gt;a:hover{border-color:#ecf0f1 #ecf0f1 #ecf0f1}.nav-tabs&gt;li.active&gt;a,.nav-tabs&gt;li.active&gt;a:hover,.nav-tabs&gt;li.active&gt;a:focus{color:#2c3e50;background-color:#ffffff;border:1px solid #ecf0f1;border-bottom-color:transparent;cursor:default}.nav-tabs.nav-justified{width:100%;border-bottom:0}.nav-tabs.nav-justified&gt;li{float:none}.nav-tabs.nav-justified&gt;li&gt;a{text-align:center;margin-bottom:5px}.nav-tabs.nav-justified&gt;.dropdown .dropdown-menu{top:auto;left:auto}@media (min-width:768px){.nav-tabs.nav-justified&gt;li{display:table-cell;width:1%}.nav-tabs.nav-justified&gt;li&gt;a{margin-bottom:0}}.nav-tabs.nav-justified&gt;li&gt;a{margin-right:0;border-radius:4px}.nav-tabs.nav-justified&gt;.active&gt;a,.nav-tabs.nav-justified&gt;.active&gt;a:hover,.nav-tabs.nav-justified&gt;.active&gt;a:focus{border:1px solid #ecf0f1}@media (min-width:768px){.nav-tabs.nav-justified&gt;li&gt;a{border-bottom:1px solid #ecf0f1;border-radius:4px 4px 0 0}.nav-tabs.nav-justified&gt;.active&gt;a,.nav-tabs.nav-justified&gt;.active&gt;a:hover,.nav-tabs.nav-justified&gt;.active&gt;a:focus{border-bottom-color:#ffffff}}.nav-pills&gt;li{float:left}.nav-pills&gt;li&gt;a{border-radius:4px}.nav-pills&gt;li+li{margin-left:2px}.nav-pills&gt;li.active&gt;a,.nav-pills&gt;li.active&gt;a:hover,.nav-pills&gt;li.active&gt;a:focus{color:#ffffff;background-color:#2c3e50}.nav-stacked&gt;li{float:none}.nav-stacked&gt;li+li{margin-top:2px;margin-left:0}.nav-justified{width:100%}.nav-justified&gt;li{float:none}.nav-justified&gt;li&gt;a{text-align:center;margin-bottom:5px}.nav-justified&gt;.dropdown .dropdown-menu{top:auto;left:auto}@media (min-width:768px){.nav-justified&gt;li{display:table-cell;width:1%}.nav-justified&gt;li&gt;a{margin-bottom:0}}.nav-tabs-justified{border-bottom:0}.nav-tabs-justified&gt;li&gt;a{margin-right:0;border-radius:4px}.nav-tabs-justified&gt;.active&gt;a,.nav-tabs-justified&gt;.active&gt;a:hover,.nav-tabs-justified&gt;.active&gt;a:focus{border:1px solid #ecf0f1}@media (min-width:768px){.nav-tabs-justified&gt;li&gt;a{border-bottom:1px solid #ecf0f1;border-radius:4px 4px 0 0}.nav-tabs-justified&gt;.active&gt;a,.nav-tabs-justified&gt;.active&gt;a:hover,.nav-tabs-justified&gt;.active&gt;a:focus{border-bottom-color:#ffffff}}.tab-content&gt;.tab-pane{display:none}.tab-content&gt;.active{display:block}.nav-tabs .dropdown-menu{margin-top:-1px;border-top-right-radius:0;border-top-left-radius:0}.navbar{position:relative;min-height:60px;margin-bottom:21px;border:1px solid transparent}@media (min-width:768px){.navbar{border-radius:4px}}@media (min-width:768px){.navbar-header{float:left}}.navbar-collapse{overflow-x:visible;padding-right:15px;padding-left:15px;border-top:1px solid transparent;-webkit-box-shadow:inset 0 1px 0 rgba(255,255,255,0.1);box-shadow:inset 0 1px 0 rgba(255,255,255,0.1);-webkit-overflow-scrolling:touch}.navbar-collapse.in{overflow-y:auto}@media (min-width:768px){.navbar-collapse{width:auto;border-top:0;-webkit-box-shadow:none;box-shadow:none}.navbar-collapse.collapse{display:block !important;height:auto !important;padding-bottom:0;overflow:visible !important}.navbar-collapse.in{overflow-y:visible}.navbar-fixed-top .navbar-collapse,.navbar-static-top .navbar-collapse,.navbar-fixed-bottom .navbar-collapse{padding-left:0;padding-right:0}}.navbar-fixed-top .navbar-collapse,.navbar-fixed-bottom .navbar-collapse{max-height:340px}@media (max-device-width:480px) and (orientation:landscape){.navbar-fixed-top .navbar-collapse,.navbar-fixed-bottom .navbar-collapse{max-height:200px}}.container&gt;.navbar-header,.container-fluid&gt;.navbar-header,.container&gt;.navbar-collapse,.container-fluid&gt;.navbar-collapse{margin-right:-15px;margin-left:-15px}@media (min-width:768px){.container&gt;.navbar-header,.container-fluid&gt;.navbar-header,.container&gt;.navbar-collapse,.container-fluid&gt;.navbar-collapse{margin-right:0;margin-left:0}}.navbar-static-top{z-index:1000;border-width:0 0 1px}@media (min-width:768px){.navbar-static-top{border-radius:0}}.navbar-fixed-top,.navbar-fixed-bottom{position:fixed;right:0;left:0;z-index:1030}@media (min-width:768px){.navbar-fixed-top,.navbar-fixed-bottom{border-radius:0}}.navbar-fixed-top{top:0;border-width:0 0 1px}.navbar-fixed-bottom{bottom:0;margin-bottom:0;border-width:1px 0 0}.navbar-brand{float:left;padding:19.5px 15px;font-size:19px;line-height:21px;height:60px}.navbar-brand:hover,.navbar-brand:focus{text-decoration:none}.navbar-brand&gt;img{display:block}@media (min-width:768px){.navbar&gt;.container .navbar-brand,.navbar&gt;.container-fluid .navbar-brand{margin-left:-15px}}.navbar-toggle{position:relative;float:right;margin-right:15px;padding:9px 10px;margin-top:13px;margin-bottom:13px;background-color:transparent;background-image:none;border:1px solid transparent;border-radius:4px}.navbar-toggle:focus{outline:0}.navbar-toggle .icon-bar{display:block;width:22px;height:2px;border-radius:1px}.navbar-toggle .icon-bar+.icon-bar{margin-top:4px}@media (min-width:768px){.navbar-toggle{display:none}}.navbar-nav{margin:9.75px -15px}.navbar-nav&gt;li&gt;a{padding-top:10px;padding-bottom:10px;line-height:21px}@media (max-width:767px){.navbar-nav .open .dropdown-menu{position:static;float:none;width:auto;margin-top:0;background-color:transparent;border:0;-webkit-box-shadow:none;box-shadow:none}.navbar-nav .open .dropdown-menu&gt;li&gt;a,.navbar-nav .open .dropdown-menu .dropdown-header{padding:5px 15px 5px 25px}.navbar-nav .open .dropdown-menu&gt;li&gt;a{line-height:21px}.navbar-nav .open .dropdown-menu&gt;li&gt;a:hover,.navbar-nav .open .dropdown-menu&gt;li&gt;a:focus{background-image:none}}@media (min-width:768px){.navbar-nav{float:left;margin:0}.navbar-nav&gt;li{float:left}.navbar-nav&gt;li&gt;a{padding-top:19.5px;padding-bottom:19.5px}}.navbar-form{margin-left:-15px;margin-right:-15px;padding:10px 15px;border-top:1px solid transparent;border-bottom:1px solid transparent;-webkit-box-shadow:inset 0 1px 0 rgba(255,255,255,0.1),0 1px 0 rgba(255,255,255,0.1);box-shadow:inset 0 1px 0 rgba(255,255,255,0.1),0 1px 0 rgba(255,255,255,0.1);margin-top:7.5px;margin-bottom:7.5px}@media (min-width:768px){.navbar-form .form-group{display:inline-block;margin-bottom:0;vertical-align:middle}.navbar-form .form-control{display:inline-block;width:auto;vertical-align:middle}.navbar-form .form-control-static{display:inline-block}.navbar-form .input-group{display:inline-table;vertical-align:middle}.navbar-form .input-group .input-group-addon,.navbar-form .input-group .input-group-btn,.navbar-form .input-group .form-control{width:auto}.navbar-form .input-group&gt;.form-control{width:100%}.navbar-form .control-label{margin-bottom:0;vertical-align:middle}.navbar-form .radio,.navbar-form .checkbox{display:inline-block;margin-top:0;margin-bottom:0;vertical-align:middle}.navbar-form .radio label,.navbar-form .checkbox label{padding-left:0}.navbar-form .radio input[type=&quot;radio&quot;],.navbar-form .checkbox input[type=&quot;checkbox&quot;]{position:relative;margin-left:0}.navbar-form .has-feedback .form-control-feedback{top:0}}@media (max-width:767px){.navbar-form .form-group{margin-bottom:5px}.navbar-form .form-group:last-child{margin-bottom:0}}@media (min-width:768px){.navbar-form{width:auto;border:0;margin-left:0;margin-right:0;padding-top:0;padding-bottom:0;-webkit-box-shadow:none;box-shadow:none}}.navbar-nav&gt;li&gt;.dropdown-menu{margin-top:0;border-top-right-radius:0;border-top-left-radius:0}.navbar-fixed-bottom .navbar-nav&gt;li&gt;.dropdown-menu{margin-bottom:0;border-top-right-radius:4px;border-top-left-radius:4px;border-bottom-right-radius:0;border-bottom-left-radius:0}.navbar-btn{margin-top:7.5px;margin-bottom:7.5px}.navbar-btn.btn-sm{margin-top:12.5px;margin-bottom:12.5px}.navbar-btn.btn-xs{margin-top:19px;margin-bottom:19px}.navbar-text{margin-top:19.5px;margin-bottom:19.5px}@media (min-width:768px){.navbar-text{float:left;margin-left:15px;margin-right:15px}}@media (min-width:768px){.navbar-left{float:left !important}.navbar-right{float:right !important;margin-right:-15px}.navbar-right~.navbar-right{margin-right:0}}.navbar-default{background-color:#2c3e50;border-color:transparent}.navbar-default .navbar-brand{color:#ffffff}.navbar-default .navbar-brand:hover,.navbar-default .navbar-brand:focus{color:#18bc9c;background-color:transparent}.navbar-default .navbar-text{color:#ffffff}.navbar-default .navbar-nav&gt;li&gt;a{color:#ffffff}.navbar-default .navbar-nav&gt;li&gt;a:hover,.navbar-default .navbar-nav&gt;li&gt;a:focus{color:#18bc9c;background-color:transparent}.navbar-default .navbar-nav&gt;.active&gt;a,.navbar-default .navbar-nav&gt;.active&gt;a:hover,.navbar-default .navbar-nav&gt;.active&gt;a:focus{color:#ffffff;background-color:#1a242f}.navbar-default .navbar-nav&gt;.disabled&gt;a,.navbar-default .navbar-nav&gt;.disabled&gt;a:hover,.navbar-default .navbar-nav&gt;.disabled&gt;a:focus{color:#cccccc;background-color:transparent}.navbar-default .navbar-toggle{border-color:#1a242f}.navbar-default .navbar-toggle:hover,.navbar-default .navbar-toggle:focus{background-color:#1a242f}.navbar-default .navbar-toggle .icon-bar{background-color:#ffffff}.navbar-default .navbar-collapse,.navbar-default .navbar-form{border-color:transparent}.navbar-default .navbar-nav&gt;.open&gt;a,.navbar-default .navbar-nav&gt;.open&gt;a:hover,.navbar-default .navbar-nav&gt;.open&gt;a:focus{background-color:#1a242f;color:#ffffff}@media (max-width:767px){.navbar-default .navbar-nav .open .dropdown-menu&gt;li&gt;a{color:#ffffff}.navbar-default .navbar-nav .open .dropdown-menu&gt;li&gt;a:hover,.navbar-default .navbar-nav .open .dropdown-menu&gt;li&gt;a:focus{color:#18bc9c;background-color:transparent}.navbar-default .navbar-nav .open .dropdown-menu&gt;.active&gt;a,.navbar-default .navbar-nav .open .dropdown-menu&gt;.active&gt;a:hover,.navbar-default .navbar-nav .open .dropdown-menu&gt;.active&gt;a:focus{color:#ffffff;background-color:#1a242f}.navbar-default .navbar-nav .open .dropdown-menu&gt;.disabled&gt;a,.navbar-default .navbar-nav .open .dropdown-menu&gt;.disabled&gt;a:hover,.navbar-default .navbar-nav .open .dropdown-menu&gt;.disabled&gt;a:focus{color:#cccccc;background-color:transparent}}.navbar-default .navbar-link{color:#ffffff}.navbar-default .navbar-link:hover{color:#18bc9c}.navbar-default .btn-link{color:#ffffff}.navbar-default .btn-link:hover,.navbar-default .btn-link:focus{color:#18bc9c}.navbar-default .btn-link[disabled]:hover,fieldset[disabled] .navbar-default .btn-link:hover,.navbar-default .btn-link[disabled]:focus,fieldset[disabled] .navbar-default .btn-link:focus{color:#cccccc}.navbar-inverse{background-color:#18bc9c;border-color:transparent}.navbar-inverse .navbar-brand{color:#ffffff}.navbar-inverse .navbar-brand:hover,.navbar-inverse .navbar-brand:focus{color:#2c3e50;background-color:transparent}.navbar-inverse .navbar-text{color:#ffffff}.navbar-inverse .navbar-nav&gt;li&gt;a{color:#ffffff}.navbar-inverse .navbar-nav&gt;li&gt;a:hover,.navbar-inverse .navbar-nav&gt;li&gt;a:focus{color:#2c3e50;background-color:transparent}.navbar-inverse .navbar-nav&gt;.active&gt;a,.navbar-inverse .navbar-nav&gt;.active&gt;a:hover,.navbar-inverse .navbar-nav&gt;.active&gt;a:focus{color:#ffffff;background-color:#15a589}.navbar-inverse .navbar-nav&gt;.disabled&gt;a,.navbar-inverse .navbar-nav&gt;.disabled&gt;a:hover,.navbar-inverse .navbar-nav&gt;.disabled&gt;a:focus{color:#cccccc;background-color:transparent}.navbar-inverse .navbar-toggle{border-color:#128f76}.navbar-inverse .navbar-toggle:hover,.navbar-inverse .navbar-toggle:focus{background-color:#128f76}.navbar-inverse .navbar-toggle .icon-bar{background-color:#ffffff}.navbar-inverse .navbar-collapse,.navbar-inverse .navbar-form{border-color:#149c82}.navbar-inverse .navbar-nav&gt;.open&gt;a,.navbar-inverse .navbar-nav&gt;.open&gt;a:hover,.navbar-inverse .navbar-nav&gt;.open&gt;a:focus{background-color:#15a589;color:#ffffff}@media (max-width:767px){.navbar-inverse .navbar-nav .open .dropdown-menu&gt;.dropdown-header{border-color:transparent}.navbar-inverse .navbar-nav .open .dropdown-menu .divider{background-color:transparent}.navbar-inverse .navbar-nav .open .dropdown-menu&gt;li&gt;a{color:#ffffff}.navbar-inverse .navbar-nav .open .dropdown-menu&gt;li&gt;a:hover,.navbar-inverse .navbar-nav .open .dropdown-menu&gt;li&gt;a:focus{color:#2c3e50;background-color:transparent}.navbar-inverse .navbar-nav .open .dropdown-menu&gt;.active&gt;a,.navbar-inverse .navbar-nav .open .dropdown-menu&gt;.active&gt;a:hover,.navbar-inverse .navbar-nav .open .dropdown-menu&gt;.active&gt;a:focus{color:#ffffff;background-color:#15a589}.navbar-inverse .navbar-nav .open .dropdown-menu&gt;.disabled&gt;a,.navbar-inverse .navbar-nav .open .dropdown-menu&gt;.disabled&gt;a:hover,.navbar-inverse .navbar-nav .open .dropdown-menu&gt;.disabled&gt;a:focus{color:#cccccc;background-color:transparent}}.navbar-inverse .navbar-link{color:#ffffff}.navbar-inverse .navbar-link:hover{color:#2c3e50}.navbar-inverse .btn-link{color:#ffffff}.navbar-inverse .btn-link:hover,.navbar-inverse .btn-link:focus{color:#2c3e50}.navbar-inverse .btn-link[disabled]:hover,fieldset[disabled] .navbar-inverse .btn-link:hover,.navbar-inverse .btn-link[disabled]:focus,fieldset[disabled] .navbar-inverse .btn-link:focus{color:#cccccc}.breadcrumb{padding:8px 15px;margin-bottom:21px;list-style:none;background-color:#ecf0f1;border-radius:4px}.breadcrumb&gt;li{display:inline-block}.breadcrumb&gt;li+li:before{content:&quot;/\00a0&quot;;padding:0 5px;color:#cccccc}.breadcrumb&gt;.active{color:#95a5a6}.pagination{display:inline-block;padding-left:0;margin:21px 0;border-radius:4px}.pagination&gt;li{display:inline}.pagination&gt;li&gt;a,.pagination&gt;li&gt;span{position:relative;float:left;padding:10px 15px;line-height:1.42857143;text-decoration:none;color:#ffffff;background-color:#18bc9c;border:1px solid transparent;margin-left:-1px}.pagination&gt;li:first-child&gt;a,.pagination&gt;li:first-child&gt;span{margin-left:0;border-bottom-left-radius:4px;border-top-left-radius:4px}.pagination&gt;li:last-child&gt;a,.pagination&gt;li:last-child&gt;span{border-bottom-right-radius:4px;border-top-right-radius:4px}.pagination&gt;li&gt;a:hover,.pagination&gt;li&gt;span:hover,.pagination&gt;li&gt;a:focus,.pagination&gt;li&gt;span:focus{z-index:2;color:#ffffff;background-color:#0f7864;border-color:transparent}.pagination&gt;.active&gt;a,.pagination&gt;.active&gt;span,.pagination&gt;.active&gt;a:hover,.pagination&gt;.active&gt;span:hover,.pagination&gt;.active&gt;a:focus,.pagination&gt;.active&gt;span:focus{z-index:3;color:#ffffff;background-color:#0f7864;border-color:transparent;cursor:default}.pagination&gt;.disabled&gt;span,.pagination&gt;.disabled&gt;span:hover,.pagination&gt;.disabled&gt;span:focus,.pagination&gt;.disabled&gt;a,.pagination&gt;.disabled&gt;a:hover,.pagination&gt;.disabled&gt;a:focus{color:#ecf0f1;background-color:#3be6c4;border-color:transparent;cursor:not-allowed}.pagination-lg&gt;li&gt;a,.pagination-lg&gt;li&gt;span{padding:18px 27px;font-size:19px;line-height:1.3333333}.pagination-lg&gt;li:first-child&gt;a,.pagination-lg&gt;li:first-child&gt;span{border-bottom-left-radius:6px;border-top-left-radius:6px}.pagination-lg&gt;li:last-child&gt;a,.pagination-lg&gt;li:last-child&gt;span{border-bottom-right-radius:6px;border-top-right-radius:6px}.pagination-sm&gt;li&gt;a,.pagination-sm&gt;li&gt;span{padding:6px 9px;font-size:13px;line-height:1.5}.pagination-sm&gt;li:first-child&gt;a,.pagination-sm&gt;li:first-child&gt;span{border-bottom-left-radius:3px;border-top-left-radius:3px}.pagination-sm&gt;li:last-child&gt;a,.pagination-sm&gt;li:last-child&gt;span{border-bottom-right-radius:3px;border-top-right-radius:3px}.pager{padding-left:0;margin:21px 0;list-style:none;text-align:center}.pager li{display:inline}.pager li&gt;a,.pager li&gt;span{display:inline-block;padding:5px 14px;background-color:#18bc9c;border:1px solid transparent;border-radius:15px}.pager li&gt;a:hover,.pager li&gt;a:focus{text-decoration:none;background-color:#0f7864}.pager .next&gt;a,.pager .next&gt;span{float:right}.pager .previous&gt;a,.pager .previous&gt;span{float:left}.pager .disabled&gt;a,.pager .disabled&gt;a:hover,.pager .disabled&gt;a:focus,.pager .disabled&gt;span{color:#ffffff;background-color:#18bc9c;cursor:not-allowed}.label{display:inline;padding:.2em .6em .3em;font-size:75%;font-weight:bold;line-height:1;color:#ffffff;text-align:center;white-space:nowrap;vertical-align:baseline;border-radius:.25em}a.label:hover,a.label:focus{color:#ffffff;text-decoration:none;cursor:pointer}.label:empty{display:none}.btn .label{position:relative;top:-1px}.label-default{background-color:#95a5a6}.label-default[href]:hover,.label-default[href]:focus{background-color:#798d8f}.label-primary{background-color:#2c3e50}.label-primary[href]:hover,.label-primary[href]:focus{background-color:#1a242f}.label-success{background-color:#18bc9c}.label-success[href]:hover,.label-success[href]:focus{background-color:#128f76}.label-info{background-color:#3498db}.label-info[href]:hover,.label-info[href]:focus{background-color:#217dbb}.label-warning{background-color:#f39c12}.label-warning[href]:hover,.label-warning[href]:focus{background-color:#c87f0a}.label-danger{background-color:#e74c3c}.label-danger[href]:hover,.label-danger[href]:focus{background-color:#d62c1a}.badge{display:inline-block;min-width:10px;padding:3px 7px;font-size:13px;font-weight:bold;color:#ffffff;line-height:1;vertical-align:middle;white-space:nowrap;text-align:center;background-color:#2c3e50;border-radius:10px}.badge:empty{display:none}.btn .badge{position:relative;top:-1px}.btn-xs .badge,.btn-group-xs&gt;.btn .badge{top:0;padding:1px 5px}a.badge:hover,a.badge:focus{color:#ffffff;text-decoration:none;cursor:pointer}.list-group-item.active&gt;.badge,.nav-pills&gt;.active&gt;a&gt;.badge{color:#2c3e50;background-color:#ffffff}.list-group-item&gt;.badge{float:right}.list-group-item&gt;.badge+.badge{margin-right:5px}.nav-pills&gt;li&gt;a&gt;.badge{margin-left:3px}.jumbotron{padding-top:30px;padding-bottom:30px;margin-bottom:30px;color:inherit;background-color:#ecf0f1}.jumbotron h1,.jumbotron .h1{color:inherit}.jumbotron p{margin-bottom:15px;font-size:23px;font-weight:200}.jumbotron&gt;hr{border-top-color:#cfd9db}.container .jumbotron,.container-fluid .jumbotron{border-radius:6px;padding-left:15px;padding-right:15px}.jumbotron .container{max-width:100%}@media screen and (min-width:768px){.jumbotron{padding-top:48px;padding-bottom:48px}.container .jumbotron,.container-fluid .jumbotron{padding-left:60px;padding-right:60px}.jumbotron h1,.jumbotron .h1{font-size:68px}}.thumbnail{display:block;padding:4px;margin-bottom:21px;line-height:1.42857143;background-color:#ffffff;border:1px solid #ecf0f1;border-radius:4px;-webkit-transition:border .2s ease-in-out;-o-transition:border .2s ease-in-out;transition:border .2s ease-in-out}.thumbnail&gt;img,.thumbnail a&gt;img{margin-left:auto;margin-right:auto}a.thumbnail:hover,a.thumbnail:focus,a.thumbnail.active{border-color:#18bc9c}.thumbnail .caption{padding:9px;color:#2c3e50}.alert{padding:15px;margin-bottom:21px;border:1px solid transparent;border-radius:4px}.alert h4{margin-top:0;color:inherit}.alert .alert-link{font-weight:bold}.alert&gt;p,.alert&gt;ul{margin-bottom:0}.alert&gt;p+p{margin-top:5px}.alert-dismissable,.alert-dismissible{padding-right:35px}.alert-dismissable .close,.alert-dismissible .close{position:relative;top:-2px;right:-21px;color:inherit}.alert-success{background-color:#18bc9c;border-color:#18bc9c;color:#ffffff}.alert-success hr{border-top-color:#15a589}.alert-success .alert-link{color:#e6e6e6}.alert-info{background-color:#3498db;border-color:#3498db;color:#ffffff}.alert-info hr{border-top-color:#258cd1}.alert-info .alert-link{color:#e6e6e6}.alert-warning{background-color:#f39c12;border-color:#f39c12;color:#ffffff}.alert-warning hr{border-top-color:#e08e0b}.alert-warning .alert-link{color:#e6e6e6}.alert-danger{background-color:#e74c3c;border-color:#e74c3c;color:#ffffff}.alert-danger hr{border-top-color:#e43725}.alert-danger .alert-link{color:#e6e6e6}@-webkit-keyframes progress-bar-stripes{from{background-position:40px 0}to{background-position:0 0}}@-o-keyframes progress-bar-stripes{from{background-position:40px 0}to{background-position:0 0}}@keyframes progress-bar-stripes{from{background-position:40px 0}to{background-position:0 0}}.progress{overflow:hidden;height:21px;margin-bottom:21px;background-color:#ecf0f1;border-radius:4px;-webkit-box-shadow:inset 0 1px 2px rgba(0,0,0,0.1);box-shadow:inset 0 1px 2px rgba(0,0,0,0.1)}.progress-bar{float:left;width:0%;height:100%;font-size:13px;line-height:21px;color:#ffffff;text-align:center;background-color:#2c3e50;-webkit-box-shadow:inset 0 -1px 0 rgba(0,0,0,0.15);box-shadow:inset 0 -1px 0 rgba(0,0,0,0.15);-webkit-transition:width 0.6s ease;-o-transition:width 0.6s ease;transition:width 0.6s ease}.progress-striped .progress-bar,.progress-bar-striped{background-image:-webkit-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:-o-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);-webkit-background-size:40px 40px;background-size:40px 40px}.progress.active .progress-bar,.progress-bar.active{-webkit-animation:progress-bar-stripes 2s linear infinite;-o-animation:progress-bar-stripes 2s linear infinite;animation:progress-bar-stripes 2s linear infinite}.progress-bar-success{background-color:#18bc9c}.progress-striped .progress-bar-success{background-image:-webkit-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:-o-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent)}.progress-bar-info{background-color:#3498db}.progress-striped .progress-bar-info{background-image:-webkit-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:-o-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent)}.progress-bar-warning{background-color:#f39c12}.progress-striped .progress-bar-warning{background-image:-webkit-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:-o-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent)}.progress-bar-danger{background-color:#e74c3c}.progress-striped .progress-bar-danger{background-image:-webkit-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:-o-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent)}.media{margin-top:15px}.media:first-child{margin-top:0}.media,.media-body{zoom:1;overflow:hidden}.media-body{width:10000px}.media-object{display:block}.media-object.img-thumbnail{max-width:none}.media-right,.media&gt;.pull-right{padding-left:10px}.media-left,.media&gt;.pull-left{padding-right:10px}.media-left,.media-right,.media-body{display:table-cell;vertical-align:top}.media-middle{vertical-align:middle}.media-bottom{vertical-align:bottom}.media-heading{margin-top:0;margin-bottom:5px}.media-list{padding-left:0;list-style:none}.list-group{margin-bottom:20px;padding-left:0}.list-group-item{position:relative;display:block;padding:10px 15px;margin-bottom:-1px;background-color:#ffffff;border:1px solid #ecf0f1}.list-group-item:first-child{border-top-right-radius:4px;border-top-left-radius:4px}.list-group-item:last-child{margin-bottom:0;border-bottom-right-radius:4px;border-bottom-left-radius:4px}a.list-group-item,button.list-group-item{color:#555555}a.list-group-item .list-group-item-heading,button.list-group-item .list-group-item-heading{color:#333333}a.list-group-item:hover,button.list-group-item:hover,a.list-group-item:focus,button.list-group-item:focus{text-decoration:none;color:#555555;background-color:#ecf0f1}button.list-group-item{width:100%;text-align:left}.list-group-item.disabled,.list-group-item.disabled:hover,.list-group-item.disabled:focus{background-color:#ecf0f1;color:#b4bcc2;cursor:not-allowed}.list-group-item.disabled .list-group-item-heading,.list-group-item.disabled:hover .list-group-item-heading,.list-group-item.disabled:focus .list-group-item-heading{color:inherit}.list-group-item.disabled .list-group-item-text,.list-group-item.disabled:hover .list-group-item-text,.list-group-item.disabled:focus .list-group-item-text{color:#b4bcc2}.list-group-item.active,.list-group-item.active:hover,.list-group-item.active:focus{z-index:2;color:#ffffff;background-color:#2c3e50;border-color:#2c3e50}.list-group-item.active .list-group-item-heading,.list-group-item.active:hover .list-group-item-heading,.list-group-item.active:focus .list-group-item-heading,.list-group-item.active .list-group-item-heading&gt;small,.list-group-item.active:hover .list-group-item-heading&gt;small,.list-group-item.active:focus .list-group-item-heading&gt;small,.list-group-item.active .list-group-item-heading&gt;.small,.list-group-item.active:hover .list-group-item-heading&gt;.small,.list-group-item.active:focus .list-group-item-heading&gt;.small{color:inherit}.list-group-item.active .list-group-item-text,.list-group-item.active:hover .list-group-item-text,.list-group-item.active:focus .list-group-item-text{color:#8aa4be}.list-group-item-success{color:#ffffff;background-color:#18bc9c}a.list-group-item-success,button.list-group-item-success{color:#ffffff}a.list-group-item-success .list-group-item-heading,button.list-group-item-success .list-group-item-heading{color:inherit}a.list-group-item-success:hover,button.list-group-item-success:hover,a.list-group-item-success:focus,button.list-group-item-success:focus{color:#ffffff;background-color:#15a589}a.list-group-item-success.active,button.list-group-item-success.active,a.list-group-item-success.active:hover,button.list-group-item-success.active:hover,a.list-group-item-success.active:focus,button.list-group-item-success.active:focus{color:#fff;background-color:#ffffff;border-color:#ffffff}.list-group-item-info{color:#ffffff;background-color:#3498db}a.list-group-item-info,button.list-group-item-info{color:#ffffff}a.list-group-item-info .list-group-item-heading,button.list-group-item-info .list-group-item-heading{color:inherit}a.list-group-item-info:hover,button.list-group-item-info:hover,a.list-group-item-info:focus,button.list-group-item-info:focus{color:#ffffff;background-color:#258cd1}a.list-group-item-info.active,button.list-group-item-info.active,a.list-group-item-info.active:hover,button.list-group-item-info.active:hover,a.list-group-item-info.active:focus,button.list-group-item-info.active:focus{color:#fff;background-color:#ffffff;border-color:#ffffff}.list-group-item-warning{color:#ffffff;background-color:#f39c12}a.list-group-item-warning,button.list-group-item-warning{color:#ffffff}a.list-group-item-warning .list-group-item-heading,button.list-group-item-warning .list-group-item-heading{color:inherit}a.list-group-item-warning:hover,button.list-group-item-warning:hover,a.list-group-item-warning:focus,button.list-group-item-warning:focus{color:#ffffff;background-color:#e08e0b}a.list-group-item-warning.active,button.list-group-item-warning.active,a.list-group-item-warning.active:hover,button.list-group-item-warning.active:hover,a.list-group-item-warning.active:focus,button.list-group-item-warning.active:focus{color:#fff;background-color:#ffffff;border-color:#ffffff}.list-group-item-danger{color:#ffffff;background-color:#e74c3c}a.list-group-item-danger,button.list-group-item-danger{color:#ffffff}a.list-group-item-danger .list-group-item-heading,button.list-group-item-danger .list-group-item-heading{color:inherit}a.list-group-item-danger:hover,button.list-group-item-danger:hover,a.list-group-item-danger:focus,button.list-group-item-danger:focus{color:#ffffff;background-color:#e43725}a.list-group-item-danger.active,button.list-group-item-danger.active,a.list-group-item-danger.active:hover,button.list-group-item-danger.active:hover,a.list-group-item-danger.active:focus,button.list-group-item-danger.active:focus{color:#fff;background-color:#ffffff;border-color:#ffffff}.list-group-item-heading{margin-top:0;margin-bottom:5px}.list-group-item-text{margin-bottom:0;line-height:1.3}.panel{margin-bottom:21px;background-color:#ffffff;border:1px solid transparent;border-radius:4px;-webkit-box-shadow:0 1px 1px rgba(0,0,0,0.05);box-shadow:0 1px 1px rgba(0,0,0,0.05)}.panel-body{padding:15px}.panel-heading{padding:10px 15px;border-bottom:1px solid transparent;border-top-right-radius:3px;border-top-left-radius:3px}.panel-heading&gt;.dropdown .dropdown-toggle{color:inherit}.panel-title{margin-top:0;margin-bottom:0;font-size:17px;color:inherit}.panel-title&gt;a,.panel-title&gt;small,.panel-title&gt;.small,.panel-title&gt;small&gt;a,.panel-title&gt;.small&gt;a{color:inherit}.panel-footer{padding:10px 15px;background-color:#ecf0f1;border-top:1px solid #ecf0f1;border-bottom-right-radius:3px;border-bottom-left-radius:3px}.panel&gt;.list-group,.panel&gt;.panel-collapse&gt;.list-group{margin-bottom:0}.panel&gt;.list-group .list-group-item,.panel&gt;.panel-collapse&gt;.list-group .list-group-item{border-width:1px 0;border-radius:0}.panel&gt;.list-group:first-child .list-group-item:first-child,.panel&gt;.panel-collapse&gt;.list-group:first-child .list-group-item:first-child{border-top:0;border-top-right-radius:3px;border-top-left-radius:3px}.panel&gt;.list-group:last-child .list-group-item:last-child,.panel&gt;.panel-collapse&gt;.list-group:last-child .list-group-item:last-child{border-bottom:0;border-bottom-right-radius:3px;border-bottom-left-radius:3px}.panel&gt;.panel-heading+.panel-collapse&gt;.list-group .list-group-item:first-child{border-top-right-radius:0;border-top-left-radius:0}.panel-heading+.list-group .list-group-item:first-child{border-top-width:0}.list-group+.panel-footer{border-top-width:0}.panel&gt;.table,.panel&gt;.table-responsive&gt;.table,.panel&gt;.panel-collapse&gt;.table{margin-bottom:0}.panel&gt;.table caption,.panel&gt;.table-responsive&gt;.table caption,.panel&gt;.panel-collapse&gt;.table caption{padding-left:15px;padding-right:15px}.panel&gt;.table:first-child,.panel&gt;.table-responsive:first-child&gt;.table:first-child{border-top-right-radius:3px;border-top-left-radius:3px}.panel&gt;.table:first-child&gt;thead:first-child&gt;tr:first-child,.panel&gt;.table-responsive:first-child&gt;.table:first-child&gt;thead:first-child&gt;tr:first-child,.panel&gt;.table:first-child&gt;tbody:first-child&gt;tr:first-child,.panel&gt;.table-responsive:first-child&gt;.table:first-child&gt;tbody:first-child&gt;tr:first-child{border-top-left-radius:3px;border-top-right-radius:3px}.panel&gt;.table:first-child&gt;thead:first-child&gt;tr:first-child td:first-child,.panel&gt;.table-responsive:first-child&gt;.table:first-child&gt;thead:first-child&gt;tr:first-child td:first-child,.panel&gt;.table:first-child&gt;tbody:first-child&gt;tr:first-child td:first-child,.panel&gt;.table-responsive:first-child&gt;.table:first-child&gt;tbody:first-child&gt;tr:first-child td:first-child,.panel&gt;.table:first-child&gt;thead:first-child&gt;tr:first-child th:first-child,.panel&gt;.table-responsive:first-child&gt;.table:first-child&gt;thead:first-child&gt;tr:first-child th:first-child,.panel&gt;.table:first-child&gt;tbody:first-child&gt;tr:first-child th:first-child,.panel&gt;.table-responsive:first-child&gt;.table:first-child&gt;tbody:first-child&gt;tr:first-child th:first-child{border-top-left-radius:3px}.panel&gt;.table:first-child&gt;thead:first-child&gt;tr:first-child td:last-child,.panel&gt;.table-responsive:first-child&gt;.table:first-child&gt;thead:first-child&gt;tr:first-child td:last-child,.panel&gt;.table:first-child&gt;tbody:first-child&gt;tr:first-child td:last-child,.panel&gt;.table-responsive:first-child&gt;.table:first-child&gt;tbody:first-child&gt;tr:first-child td:last-child,.panel&gt;.table:first-child&gt;thead:first-child&gt;tr:first-child th:last-child,.panel&gt;.table-responsive:first-child&gt;.table:first-child&gt;thead:first-child&gt;tr:first-child th:last-child,.panel&gt;.table:first-child&gt;tbody:first-child&gt;tr:first-child th:last-child,.panel&gt;.table-responsive:first-child&gt;.table:first-child&gt;tbody:first-child&gt;tr:first-child th:last-child{border-top-right-radius:3px}.panel&gt;.table:last-child,.panel&gt;.table-responsive:last-child&gt;.table:last-child{border-bottom-right-radius:3px;border-bottom-left-radius:3px}.panel&gt;.table:last-child&gt;tbody:last-child&gt;tr:last-child,.panel&gt;.table-responsive:last-child&gt;.table:last-child&gt;tbody:last-child&gt;tr:last-child,.panel&gt;.table:last-child&gt;tfoot:last-child&gt;tr:last-child,.panel&gt;.table-responsive:last-child&gt;.table:last-child&gt;tfoot:last-child&gt;tr:last-child{border-bottom-left-radius:3px;border-bottom-right-radius:3px}.panel&gt;.table:last-child&gt;tbody:last-child&gt;tr:last-child td:first-child,.panel&gt;.table-responsive:last-child&gt;.table:last-child&gt;tbody:last-child&gt;tr:last-child td:first-child,.panel&gt;.table:last-child&gt;tfoot:last-child&gt;tr:last-child td:first-child,.panel&gt;.table-responsive:last-child&gt;.table:last-child&gt;tfoot:last-child&gt;tr:last-child td:first-child,.panel&gt;.table:last-child&gt;tbody:last-child&gt;tr:last-child th:first-child,.panel&gt;.table-responsive:last-child&gt;.table:last-child&gt;tbody:last-child&gt;tr:last-child th:first-child,.panel&gt;.table:last-child&gt;tfoot:last-child&gt;tr:last-child th:first-child,.panel&gt;.table-responsive:last-child&gt;.table:last-child&gt;tfoot:last-child&gt;tr:last-child th:first-child{border-bottom-left-radius:3px}.panel&gt;.table:last-child&gt;tbody:last-child&gt;tr:last-child td:last-child,.panel&gt;.table-responsive:last-child&gt;.table:last-child&gt;tbody:last-child&gt;tr:last-child td:last-child,.panel&gt;.table:last-child&gt;tfoot:last-child&gt;tr:last-child td:last-child,.panel&gt;.table-responsive:last-child&gt;.table:last-child&gt;tfoot:last-child&gt;tr:last-child td:last-child,.panel&gt;.table:last-child&gt;tbody:last-child&gt;tr:last-child th:last-child,.panel&gt;.table-responsive:last-child&gt;.table:last-child&gt;tbody:last-child&gt;tr:last-child th:last-child,.panel&gt;.table:last-child&gt;tfoot:last-child&gt;tr:last-child th:last-child,.panel&gt;.table-responsive:last-child&gt;.table:last-child&gt;tfoot:last-child&gt;tr:last-child th:last-child{border-bottom-right-radius:3px}.panel&gt;.panel-body+.table,.panel&gt;.panel-body+.table-responsive,.panel&gt;.table+.panel-body,.panel&gt;.table-responsive+.panel-body{border-top:1px solid #ecf0f1}.panel&gt;.table&gt;tbody:first-child&gt;tr:first-child th,.panel&gt;.table&gt;tbody:first-child&gt;tr:first-child td{border-top:0}.panel&gt;.table-bordered,.panel&gt;.table-responsive&gt;.table-bordered{border:0}.panel&gt;.table-bordered&gt;thead&gt;tr&gt;th:first-child,.panel&gt;.table-responsive&gt;.table-bordered&gt;thead&gt;tr&gt;th:first-child,.panel&gt;.table-bordered&gt;tbody&gt;tr&gt;th:first-child,.panel&gt;.table-responsive&gt;.table-bordered&gt;tbody&gt;tr&gt;th:first-child,.panel&gt;.table-bordered&gt;tfoot&gt;tr&gt;th:first-child,.panel&gt;.table-responsive&gt;.table-bordered&gt;tfoot&gt;tr&gt;th:first-child,.panel&gt;.table-bordered&gt;thead&gt;tr&gt;td:first-child,.panel&gt;.table-responsive&gt;.table-bordered&gt;thead&gt;tr&gt;td:first-child,.panel&gt;.table-bordered&gt;tbody&gt;tr&gt;td:first-child,.panel&gt;.table-responsive&gt;.table-bordered&gt;tbody&gt;tr&gt;td:first-child,.panel&gt;.table-bordered&gt;tfoot&gt;tr&gt;td:first-child,.panel&gt;.table-responsive&gt;.table-bordered&gt;tfoot&gt;tr&gt;td:first-child{border-left:0}.panel&gt;.table-bordered&gt;thead&gt;tr&gt;th:last-child,.panel&gt;.table-responsive&gt;.table-bordered&gt;thead&gt;tr&gt;th:last-child,.panel&gt;.table-bordered&gt;tbody&gt;tr&gt;th:last-child,.panel&gt;.table-responsive&gt;.table-bordered&gt;tbody&gt;tr&gt;th:last-child,.panel&gt;.table-bordered&gt;tfoot&gt;tr&gt;th:last-child,.panel&gt;.table-responsive&gt;.table-bordered&gt;tfoot&gt;tr&gt;th:last-child,.panel&gt;.table-bordered&gt;thead&gt;tr&gt;td:last-child,.panel&gt;.table-responsive&gt;.table-bordered&gt;thead&gt;tr&gt;td:last-child,.panel&gt;.table-bordered&gt;tbody&gt;tr&gt;td:last-child,.panel&gt;.table-responsive&gt;.table-bordered&gt;tbody&gt;tr&gt;td:last-child,.panel&gt;.table-bordered&gt;tfoot&gt;tr&gt;td:last-child,.panel&gt;.table-responsive&gt;.table-bordered&gt;tfoot&gt;tr&gt;td:last-child{border-right:0}.panel&gt;.table-bordered&gt;thead&gt;tr:first-child&gt;td,.panel&gt;.table-responsive&gt;.table-bordered&gt;thead&gt;tr:first-child&gt;td,.panel&gt;.table-bordered&gt;tbody&gt;tr:first-child&gt;td,.panel&gt;.table-responsive&gt;.table-bordered&gt;tbody&gt;tr:first-child&gt;td,.panel&gt;.table-bordered&gt;thead&gt;tr:first-child&gt;th,.panel&gt;.table-responsive&gt;.table-bordered&gt;thead&gt;tr:first-child&gt;th,.panel&gt;.table-bordered&gt;tbody&gt;tr:first-child&gt;th,.panel&gt;.table-responsive&gt;.table-bordered&gt;tbody&gt;tr:first-child&gt;th{border-bottom:0}.panel&gt;.table-bordered&gt;tbody&gt;tr:last-child&gt;td,.panel&gt;.table-responsive&gt;.table-bordered&gt;tbody&gt;tr:last-child&gt;td,.panel&gt;.table-bordered&gt;tfoot&gt;tr:last-child&gt;td,.panel&gt;.table-responsive&gt;.table-bordered&gt;tfoot&gt;tr:last-child&gt;td,.panel&gt;.table-bordered&gt;tbody&gt;tr:last-child&gt;th,.panel&gt;.table-responsive&gt;.table-bordered&gt;tbody&gt;tr:last-child&gt;th,.panel&gt;.table-bordered&gt;tfoot&gt;tr:last-child&gt;th,.panel&gt;.table-responsive&gt;.table-bordered&gt;tfoot&gt;tr:last-child&gt;th{border-bottom:0}.panel&gt;.table-responsive{border:0;margin-bottom:0}.panel-group{margin-bottom:21px}.panel-group .panel{margin-bottom:0;border-radius:4px}.panel-group .panel+.panel{margin-top:5px}.panel-group .panel-heading{border-bottom:0}.panel-group .panel-heading+.panel-collapse&gt;.panel-body,.panel-group .panel-heading+.panel-collapse&gt;.list-group{border-top:1px solid #ecf0f1}.panel-group .panel-footer{border-top:0}.panel-group .panel-footer+.panel-collapse .panel-body{border-bottom:1px solid #ecf0f1}.panel-default{border-color:#ecf0f1}.panel-default&gt;.panel-heading{color:#2c3e50;background-color:#ecf0f1;border-color:#ecf0f1}.panel-default&gt;.panel-heading+.panel-collapse&gt;.panel-body{border-top-color:#ecf0f1}.panel-default&gt;.panel-heading .badge{color:#ecf0f1;background-color:#2c3e50}.panel-default&gt;.panel-footer+.panel-collapse&gt;.panel-body{border-bottom-color:#ecf0f1}.panel-primary{border-color:#2c3e50}.panel-primary&gt;.panel-heading{color:#ffffff;background-color:#2c3e50;border-color:#2c3e50}.panel-primary&gt;.panel-heading+.panel-collapse&gt;.panel-body{border-top-color:#2c3e50}.panel-primary&gt;.panel-heading .badge{color:#2c3e50;background-color:#ffffff}.panel-primary&gt;.panel-footer+.panel-collapse&gt;.panel-body{border-bottom-color:#2c3e50}.panel-success{border-color:#18bc9c}.panel-success&gt;.panel-heading{color:#ffffff;background-color:#18bc9c;border-color:#18bc9c}.panel-success&gt;.panel-heading+.panel-collapse&gt;.panel-body{border-top-color:#18bc9c}.panel-success&gt;.panel-heading .badge{color:#18bc9c;background-color:#ffffff}.panel-success&gt;.panel-footer+.panel-collapse&gt;.panel-body{border-bottom-color:#18bc9c}.panel-info{border-color:#3498db}.panel-info&gt;.panel-heading{color:#ffffff;background-color:#3498db;border-color:#3498db}.panel-info&gt;.panel-heading+.panel-collapse&gt;.panel-body{border-top-color:#3498db}.panel-info&gt;.panel-heading .badge{color:#3498db;background-color:#ffffff}.panel-info&gt;.panel-footer+.panel-collapse&gt;.panel-body{border-bottom-color:#3498db}.panel-warning{border-color:#f39c12}.panel-warning&gt;.panel-heading{color:#ffffff;background-color:#f39c12;border-color:#f39c12}.panel-warning&gt;.panel-heading+.panel-collapse&gt;.panel-body{border-top-color:#f39c12}.panel-warning&gt;.panel-heading .badge{color:#f39c12;background-color:#ffffff}.panel-warning&gt;.panel-footer+.panel-collapse&gt;.panel-body{border-bottom-color:#f39c12}.panel-danger{border-color:#e74c3c}.panel-danger&gt;.panel-heading{color:#ffffff;background-color:#e74c3c;border-color:#e74c3c}.panel-danger&gt;.panel-heading+.panel-collapse&gt;.panel-body{border-top-color:#e74c3c}.panel-danger&gt;.panel-heading .badge{color:#e74c3c;background-color:#ffffff}.panel-danger&gt;.panel-footer+.panel-collapse&gt;.panel-body{border-bottom-color:#e74c3c}.embed-responsive{position:relative;display:block;height:0;padding:0;overflow:hidden}.embed-responsive .embed-responsive-item,.embed-responsive iframe,.embed-responsive embed,.embed-responsive object,.embed-responsive video{position:absolute;top:0;left:0;bottom:0;height:100%;width:100%;border:0}.embed-responsive-16by9{padding-bottom:56.25%}.embed-responsive-4by3{padding-bottom:75%}.well{min-height:20px;padding:19px;margin-bottom:20px;background-color:#ecf0f1;border:1px solid transparent;border-radius:4px;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.05);box-shadow:inset 0 1px 1px rgba(0,0,0,0.05)}.well blockquote{border-color:#ddd;border-color:rgba(0,0,0,0.15)}.well-lg{padding:24px;border-radius:6px}.well-sm{padding:9px;border-radius:3px}.close{float:right;font-size:22.5px;font-weight:bold;line-height:1;color:#000000;text-shadow:none;opacity:0.2;filter:alpha(opacity=20)}.close:hover,.close:focus{color:#000000;text-decoration:none;cursor:pointer;opacity:0.5;filter:alpha(opacity=50)}button.close{padding:0;cursor:pointer;background:transparent;border:0;-webkit-appearance:none}.modal-open{overflow:hidden}.modal{display:none;overflow:hidden;position:fixed;top:0;right:0;bottom:0;left:0;z-index:1050;-webkit-overflow-scrolling:touch;outline:0}.modal.fade .modal-dialog{-webkit-transform:translate(0, -25%);-ms-transform:translate(0, -25%);-o-transform:translate(0, -25%);transform:translate(0, -25%);-webkit-transition:-webkit-transform .3s ease-out;-o-transition:-o-transform .3s ease-out;transition:transform .3s ease-out}.modal.in .modal-dialog{-webkit-transform:translate(0, 0);-ms-transform:translate(0, 0);-o-transform:translate(0, 0);transform:translate(0, 0)}.modal-open .modal{overflow-x:hidden;overflow-y:auto}.modal-dialog{position:relative;width:auto;margin:10px}.modal-content{position:relative;background-color:#ffffff;border:1px solid #999999;border:1px solid rgba(0,0,0,0.2);border-radius:6px;-webkit-box-shadow:0 3px 9px rgba(0,0,0,0.5);box-shadow:0 3px 9px rgba(0,0,0,0.5);-webkit-background-clip:padding-box;background-clip:padding-box;outline:0}.modal-backdrop{position:fixed;top:0;right:0;bottom:0;left:0;z-index:1040;background-color:#000000}.modal-backdrop.fade{opacity:0;filter:alpha(opacity=0)}.modal-backdrop.in{opacity:0.5;filter:alpha(opacity=50)}.modal-header{padding:15px;border-bottom:1px solid #e5e5e5}.modal-header .close{margin-top:-2px}.modal-title{margin:0;line-height:1.42857143}.modal-body{position:relative;padding:20px}.modal-footer{padding:20px;text-align:right;border-top:1px solid #e5e5e5}.modal-footer .btn+.btn{margin-left:5px;margin-bottom:0}.modal-footer .btn-group .btn+.btn{margin-left:-1px}.modal-footer .btn-block+.btn-block{margin-left:0}.modal-scrollbar-measure{position:absolute;top:-9999px;width:50px;height:50px;overflow:scroll}@media (min-width:768px){.modal-dialog{width:600px;margin:30px auto}.modal-content{-webkit-box-shadow:0 5px 15px rgba(0,0,0,0.5);box-shadow:0 5px 15px rgba(0,0,0,0.5)}.modal-sm{width:300px}}@media (min-width:992px){.modal-lg{width:900px}}.tooltip{position:absolute;z-index:1070;display:block;font-family:&quot;Lato&quot;,&quot;Helvetica Neue&quot;,Helvetica,Arial,sans-serif;font-style:normal;font-weight:normal;letter-spacing:normal;line-break:auto;line-height:1.42857143;text-align:left;text-align:start;text-decoration:none;text-shadow:none;text-transform:none;white-space:normal;word-break:normal;word-spacing:normal;word-wrap:normal;font-size:13px;opacity:0;filter:alpha(opacity=0)}.tooltip.in{opacity:0.9;filter:alpha(opacity=90)}.tooltip.top{margin-top:-3px;padding:5px 0}.tooltip.right{margin-left:3px;padding:0 5px}.tooltip.bottom{margin-top:3px;padding:5px 0}.tooltip.left{margin-left:-3px;padding:0 5px}.tooltip-inner{max-width:200px;padding:3px 8px;color:#ffffff;text-align:center;background-color:#000000;border-radius:4px}.tooltip-arrow{position:absolute;width:0;height:0;border-color:transparent;border-style:solid}.tooltip.top .tooltip-arrow{bottom:0;left:50%;margin-left:-5px;border-width:5px 5px 0;border-top-color:#000000}.tooltip.top-left .tooltip-arrow{bottom:0;right:5px;margin-bottom:-5px;border-width:5px 5px 0;border-top-color:#000000}.tooltip.top-right .tooltip-arrow{bottom:0;left:5px;margin-bottom:-5px;border-width:5px 5px 0;border-top-color:#000000}.tooltip.right .tooltip-arrow{top:50%;left:0;margin-top:-5px;border-width:5px 5px 5px 0;border-right-color:#000000}.tooltip.left .tooltip-arrow{top:50%;right:0;margin-top:-5px;border-width:5px 0 5px 5px;border-left-color:#000000}.tooltip.bottom .tooltip-arrow{top:0;left:50%;margin-left:-5px;border-width:0 5px 5px;border-bottom-color:#000000}.tooltip.bottom-left .tooltip-arrow{top:0;right:5px;margin-top:-5px;border-width:0 5px 5px;border-bottom-color:#000000}.tooltip.bottom-right .tooltip-arrow{top:0;left:5px;margin-top:-5px;border-width:0 5px 5px;border-bottom-color:#000000}.popover{position:absolute;top:0;left:0;z-index:1060;display:none;max-width:276px;padding:1px;font-family:&quot;Lato&quot;,&quot;Helvetica Neue&quot;,Helvetica,Arial,sans-serif;font-style:normal;font-weight:normal;letter-spacing:normal;line-break:auto;line-height:1.42857143;text-align:left;text-align:start;text-decoration:none;text-shadow:none;text-transform:none;white-space:normal;word-break:normal;word-spacing:normal;word-wrap:normal;font-size:15px;background-color:#ffffff;-webkit-background-clip:padding-box;background-clip:padding-box;border:1px solid #cccccc;border:1px solid rgba(0,0,0,0.2);border-radius:6px;-webkit-box-shadow:0 5px 10px rgba(0,0,0,0.2);box-shadow:0 5px 10px rgba(0,0,0,0.2)}.popover.top{margin-top:-10px}.popover.right{margin-left:10px}.popover.bottom{margin-top:10px}.popover.left{margin-left:-10px}.popover-title{margin:0;padding:8px 14px;font-size:15px;background-color:#f7f7f7;border-bottom:1px solid #ebebeb;border-radius:5px 5px 0 0}.popover-content{padding:9px 14px}.popover&gt;.arrow,.popover&gt;.arrow:after{position:absolute;display:block;width:0;height:0;border-color:transparent;border-style:solid}.popover&gt;.arrow{border-width:11px}.popover&gt;.arrow:after{border-width:10px;content:&quot;&quot;}.popover.top&gt;.arrow{left:50%;margin-left:-11px;border-bottom-width:0;border-top-color:#999999;border-top-color:rgba(0,0,0,0.25);bottom:-11px}.popover.top&gt;.arrow:after{content:&quot; &quot;;bottom:1px;margin-left:-10px;border-bottom-width:0;border-top-color:#ffffff}.popover.right&gt;.arrow{top:50%;left:-11px;margin-top:-11px;border-left-width:0;border-right-color:#999999;border-right-color:rgba(0,0,0,0.25)}.popover.right&gt;.arrow:after{content:&quot; &quot;;left:1px;bottom:-10px;border-left-width:0;border-right-color:#ffffff}.popover.bottom&gt;.arrow{left:50%;margin-left:-11px;border-top-width:0;border-bottom-color:#999999;border-bottom-color:rgba(0,0,0,0.25);top:-11px}.popover.bottom&gt;.arrow:after{content:&quot; &quot;;top:1px;margin-left:-10px;border-top-width:0;border-bottom-color:#ffffff}.popover.left&gt;.arrow{top:50%;right:-11px;margin-top:-11px;border-right-width:0;border-left-color:#999999;border-left-color:rgba(0,0,0,0.25)}.popover.left&gt;.arrow:after{content:&quot; &quot;;right:1px;border-right-width:0;border-left-color:#ffffff;bottom:-10px}.carousel{position:relative}.carousel-inner{position:relative;overflow:hidden;width:100%}.carousel-inner&gt;.item{display:none;position:relative;-webkit-transition:.6s ease-in-out left;-o-transition:.6s ease-in-out left;transition:.6s ease-in-out left}.carousel-inner&gt;.item&gt;img,.carousel-inner&gt;.item&gt;a&gt;img{line-height:1}@media all and (transform-3d),(-webkit-transform-3d){.carousel-inner&gt;.item{-webkit-transition:-webkit-transform .6s ease-in-out;-o-transition:-o-transform .6s ease-in-out;transition:transform .6s ease-in-out;-webkit-backface-visibility:hidden;backface-visibility:hidden;-webkit-perspective:1000px;perspective:1000px}.carousel-inner&gt;.item.next,.carousel-inner&gt;.item.active.right{-webkit-transform:translate3d(100%, 0, 0);transform:translate3d(100%, 0, 0);left:0}.carousel-inner&gt;.item.prev,.carousel-inner&gt;.item.active.left{-webkit-transform:translate3d(-100%, 0, 0);transform:translate3d(-100%, 0, 0);left:0}.carousel-inner&gt;.item.next.left,.carousel-inner&gt;.item.prev.right,.carousel-inner&gt;.item.active{-webkit-transform:translate3d(0, 0, 0);transform:translate3d(0, 0, 0);left:0}}.carousel-inner&gt;.active,.carousel-inner&gt;.next,.carousel-inner&gt;.prev{display:block}.carousel-inner&gt;.active{left:0}.carousel-inner&gt;.next,.carousel-inner&gt;.prev{position:absolute;top:0;width:100%}.carousel-inner&gt;.next{left:100%}.carousel-inner&gt;.prev{left:-100%}.carousel-inner&gt;.next.left,.carousel-inner&gt;.prev.right{left:0}.carousel-inner&gt;.active.left{left:-100%}.carousel-inner&gt;.active.right{left:100%}.carousel-control{position:absolute;top:0;left:0;bottom:0;width:15%;opacity:0.5;filter:alpha(opacity=50);font-size:20px;color:#ffffff;text-align:center;text-shadow:0 1px 2px rgba(0,0,0,0.6);background-color:rgba(0,0,0,0)}.carousel-control.left{background-image:-webkit-linear-gradient(left, rgba(0,0,0,0.5) 0, rgba(0,0,0,0.0001) 100%);background-image:-o-linear-gradient(left, rgba(0,0,0,0.5) 0, rgba(0,0,0,0.0001) 100%);background-image:-webkit-gradient(linear, left top, right top, from(rgba(0,0,0,0.5)), to(rgba(0,0,0,0.0001)));background-image:linear-gradient(to right, rgba(0,0,0,0.5) 0, rgba(0,0,0,0.0001) 100%);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=&#x27;#80000000&#x27;, endColorstr=&#x27;#00000000&#x27;, GradientType=1)}.carousel-control.right{left:auto;right:0;background-image:-webkit-linear-gradient(left, rgba(0,0,0,0.0001) 0, rgba(0,0,0,0.5) 100%);background-image:-o-linear-gradient(left, rgba(0,0,0,0.0001) 0, rgba(0,0,0,0.5) 100%);background-image:-webkit-gradient(linear, left top, right top, from(rgba(0,0,0,0.0001)), to(rgba(0,0,0,0.5)));background-image:linear-gradient(to right, rgba(0,0,0,0.0001) 0, rgba(0,0,0,0.5) 100%);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=&#x27;#00000000&#x27;, endColorstr=&#x27;#80000000&#x27;, GradientType=1)}.carousel-control:hover,.carousel-control:focus{outline:0;color:#ffffff;text-decoration:none;opacity:0.9;filter:alpha(opacity=90)}.carousel-control .icon-prev,.carousel-control .icon-next,.carousel-control .glyphicon-chevron-left,.carousel-control .glyphicon-chevron-right{position:absolute;top:50%;margin-top:-10px;z-index:5;display:inline-block}.carousel-control .icon-prev,.carousel-control .glyphicon-chevron-left{left:50%;margin-left:-10px}.carousel-control .icon-next,.carousel-control .glyphicon-chevron-right{right:50%;margin-right:-10px}.carousel-control .icon-prev,.carousel-control .icon-next{width:20px;height:20px;line-height:1;font-family:serif}.carousel-control .icon-prev:before{content:&#x27;\2039&#x27;}.carousel-control .icon-next:before{content:&#x27;\203a&#x27;}.carousel-indicators{position:absolute;bottom:10px;left:50%;z-index:15;width:60%;margin-left:-30%;padding-left:0;list-style:none;text-align:center}.carousel-indicators li{display:inline-block;width:10px;height:10px;margin:1px;text-indent:-999px;border:1px solid #ffffff;border-radius:10px;cursor:pointer;background-color:#000 \9;background-color:rgba(0,0,0,0)}.carousel-indicators .active{margin:0;width:12px;height:12px;background-color:#ffffff}.carousel-caption{position:absolute;left:15%;right:15%;bottom:20px;z-index:10;padding-top:20px;padding-bottom:20px;color:#ffffff;text-align:center;text-shadow:0 1px 2px rgba(0,0,0,0.6)}.carousel-caption .btn{text-shadow:none}@media screen and (min-width:768px){.carousel-control .glyphicon-chevron-left,.carousel-control .glyphicon-chevron-right,.carousel-control .icon-prev,.carousel-control .icon-next{width:30px;height:30px;margin-top:-10px;font-size:30px}.carousel-control .glyphicon-chevron-left,.carousel-control .icon-prev{margin-left:-10px}.carousel-control .glyphicon-chevron-right,.carousel-control .icon-next{margin-right:-10px}.carousel-caption{left:20%;right:20%;padding-bottom:30px}.carousel-indicators{bottom:20px}}.clearfix:before,.clearfix:after,.dl-horizontal dd:before,.dl-horizontal dd:after,.container:before,.container:after,.container-fluid:before,.container-fluid:after,.row:before,.row:after,.form-horizontal .form-group:before,.form-horizontal .form-group:after,.btn-toolbar:before,.btn-toolbar:after,.btn-group-vertical&gt;.btn-group:before,.btn-group-vertical&gt;.btn-group:after,.nav:before,.nav:after,.navbar:before,.navbar:after,.navbar-header:before,.navbar-header:after,.navbar-collapse:before,.navbar-collapse:after,.pager:before,.pager:after,.panel-body:before,.panel-body:after,.modal-header:before,.modal-header:after,.modal-footer:before,.modal-footer:after{content:&quot; &quot;;display:table}.clearfix:after,.dl-horizontal dd:after,.container:after,.container-fluid:after,.row:after,.form-horizontal .form-group:after,.btn-toolbar:after,.btn-group-vertical&gt;.btn-group:after,.nav:after,.navbar:after,.navbar-header:after,.navbar-collapse:after,.pager:after,.panel-body:after,.modal-header:after,.modal-footer:after{clear:both}.center-block{display:block;margin-left:auto;margin-right:auto}.pull-right{float:right !important}.pull-left{float:left !important}.hide{display:none !important}.show{display:block !important}.invisible{visibility:hidden}.text-hide{font:0/0 a;color:transparent;text-shadow:none;background-color:transparent;border:0}.hidden{display:none !important}.affix{position:fixed}@-ms-viewport{width:device-width}.visible-xs,.visible-sm,.visible-md,.visible-lg{display:none !important}.visible-xs-block,.visible-xs-inline,.visible-xs-inline-block,.visible-sm-block,.visible-sm-inline,.visible-sm-inline-block,.visible-md-block,.visible-md-inline,.visible-md-inline-block,.visible-lg-block,.visible-lg-inline,.visible-lg-inline-block{display:none !important}@media (max-width:767px){.visible-xs{display:block !important}table.visible-xs{display:table !important}tr.visible-xs{display:table-row !important}th.visible-xs,td.visible-xs{display:table-cell !important}}@media (max-width:767px){.visible-xs-block{display:block !important}}@media (max-width:767px){.visible-xs-inline{display:inline !important}}@media (max-width:767px){.visible-xs-inline-block{display:inline-block !important}}@media (min-width:768px) and (max-width:991px){.visible-sm{display:block !important}table.visible-sm{display:table !important}tr.visible-sm{display:table-row !important}th.visible-sm,td.visible-sm{display:table-cell !important}}@media (min-width:768px) and (max-width:991px){.visible-sm-block{display:block !important}}@media (min-width:768px) and (max-width:991px){.visible-sm-inline{display:inline !important}}@media (min-width:768px) and (max-width:991px){.visible-sm-inline-block{display:inline-block !important}}@media (min-width:992px) and (max-width:1199px){.visible-md{display:block !important}table.visible-md{display:table !important}tr.visible-md{display:table-row !important}th.visible-md,td.visible-md{display:table-cell !important}}@media (min-width:992px) and (max-width:1199px){.visible-md-block{display:block !important}}@media (min-width:992px) and (max-width:1199px){.visible-md-inline{display:inline !important}}@media (min-width:992px) and (max-width:1199px){.visible-md-inline-block{display:inline-block !important}}@media (min-width:1200px){.visible-lg{display:block !important}table.visible-lg{display:table !important}tr.visible-lg{display:table-row !important}th.visible-lg,td.visible-lg{display:table-cell !important}}@media (min-width:1200px){.visible-lg-block{display:block !important}}@media (min-width:1200px){.visible-lg-inline{display:inline !important}}@media (min-width:1200px){.visible-lg-inline-block{display:inline-block !important}}@media (max-width:767px){.hidden-xs{display:none !important}}@media (min-width:768px) and (max-width:991px){.hidden-sm{display:none !important}}@media (min-width:992px) and (max-width:1199px){.hidden-md{display:none !important}}@media (min-width:1200px){.hidden-lg{display:none !important}}.visible-print{display:none !important}@media print{.visible-print{display:block !important}table.visible-print{display:table !important}tr.visible-print{display:table-row !important}th.visible-print,td.visible-print{display:table-cell !important}}.visible-print-block{display:none !important}@media print{.visible-print-block{display:block !important}}.visible-print-inline{display:none !important}@media print{.visible-print-inline{display:inline !important}}.visible-print-inline-block{display:none !important}@media print{.visible-print-inline-block{display:inline-block !important}}@media print{.hidden-print{display:none !important}}.navbar{border-width:0}.navbar-default .badge{background-color:#fff;color:#2c3e50}.navbar-inverse .badge{background-color:#fff;color:#18bc9c}.navbar-brand{line-height:1}.btn{border-width:2px}.btn:active{-webkit-box-shadow:none;box-shadow:none}.btn-group.open .dropdown-toggle{-webkit-box-shadow:none;box-shadow:none}.text-primary,.text-primary:hover{color:#2c3e50}.text-success,.text-success:hover{color:#18bc9c}.text-danger,.text-danger:hover{color:#e74c3c}.text-warning,.text-warning:hover{color:#f39c12}.text-info,.text-info:hover{color:#3498db}table a:not(.btn),.table a:not(.btn){text-decoration:underline}table .dropdown-menu a,.table .dropdown-menu a{text-decoration:none}table .success,.table .success,table .warning,.table .warning,table .danger,.table .danger,table .info,.table .info{color:#fff}table .success&gt;th&gt;a,.table .success&gt;th&gt;a,table .warning&gt;th&gt;a,.table .warning&gt;th&gt;a,table .danger&gt;th&gt;a,.table .danger&gt;th&gt;a,table .info&gt;th&gt;a,.table .info&gt;th&gt;a,table .success&gt;td&gt;a,.table .success&gt;td&gt;a,table .warning&gt;td&gt;a,.table .warning&gt;td&gt;a,table .danger&gt;td&gt;a,.table .danger&gt;td&gt;a,table .info&gt;td&gt;a,.table .info&gt;td&gt;a,table .success&gt;a,.table .success&gt;a,table .warning&gt;a,.table .warning&gt;a,table .danger&gt;a,.table .danger&gt;a,table .info&gt;a,.table .info&gt;a{color:#fff}table&gt;thead&gt;tr&gt;th,.table&gt;thead&gt;tr&gt;th,table&gt;tbody&gt;tr&gt;th,.table&gt;tbody&gt;tr&gt;th,table&gt;tfoot&gt;tr&gt;th,.table&gt;tfoot&gt;tr&gt;th,table&gt;thead&gt;tr&gt;td,.table&gt;thead&gt;tr&gt;td,table&gt;tbody&gt;tr&gt;td,.table&gt;tbody&gt;tr&gt;td,table&gt;tfoot&gt;tr&gt;td,.table&gt;tfoot&gt;tr&gt;td{border:none}table-bordered&gt;thead&gt;tr&gt;th,.table-bordered&gt;thead&gt;tr&gt;th,table-bordered&gt;tbody&gt;tr&gt;th,.table-bordered&gt;tbody&gt;tr&gt;th,table-bordered&gt;tfoot&gt;tr&gt;th,.table-bordered&gt;tfoot&gt;tr&gt;th,table-bordered&gt;thead&gt;tr&gt;td,.table-bordered&gt;thead&gt;tr&gt;td,table-bordered&gt;tbody&gt;tr&gt;td,.table-bordered&gt;tbody&gt;tr&gt;td,table-bordered&gt;tfoot&gt;tr&gt;td,.table-bordered&gt;tfoot&gt;tr&gt;td{border:1px solid #ecf0f1}.form-control,input{border-width:2px;-webkit-box-shadow:none;box-shadow:none}.form-control:focus,input:focus{-webkit-box-shadow:none;box-shadow:none}.has-warning .help-block,.has-warning .control-label,.has-warning .radio,.has-warning .checkbox,.has-warning .radio-inline,.has-warning .checkbox-inline,.has-warning.radio label,.has-warning.checkbox label,.has-warning.radio-inline label,.has-warning.checkbox-inline label,.has-warning .form-control-feedback{color:#f39c12}.has-warning .form-control,.has-warning .form-control:focus{border:2px solid #f39c12}.has-warning .input-group-addon{border-color:#f39c12}.has-error .help-block,.has-error .control-label,.has-error .radio,.has-error .checkbox,.has-error .radio-inline,.has-error .checkbox-inline,.has-error.radio label,.has-error.checkbox label,.has-error.radio-inline label,.has-error.checkbox-inline label,.has-error .form-control-feedback{color:#e74c3c}.has-error .form-control,.has-error .form-control:focus{border:2px solid #e74c3c}.has-error .input-group-addon{border-color:#e74c3c}.has-success .help-block,.has-success .control-label,.has-success .radio,.has-success .checkbox,.has-success .radio-inline,.has-success .checkbox-inline,.has-success.radio label,.has-success.checkbox label,.has-success.radio-inline label,.has-success.checkbox-inline label,.has-success .form-control-feedback{color:#18bc9c}.has-success .form-control,.has-success .form-control:focus{border:2px solid #18bc9c}.has-success .input-group-addon{border-color:#18bc9c}.nav .open&gt;a,.nav .open&gt;a:hover,.nav .open&gt;a:focus{border-color:transparent}.pager a,.pager a:hover{color:#fff}.pager .disabled&gt;a,.pager .disabled&gt;a:hover,.pager .disabled&gt;a:focus,.pager .disabled&gt;span{background-color:#3be6c4}.close{color:#fff;text-decoration:none;opacity:0.4}.close:hover,.close:focus{color:#fff;opacity:1}.alert .alert-link{color:#fff;text-decoration:underline}.progress{height:10px;-webkit-box-shadow:none;box-shadow:none}.progress .progress-bar{font-size:10px;line-height:10px}.well{-webkit-box-shadow:none;box-shadow:none}a.list-group-item.active,a.list-group-item.active:hover,a.list-group-item.active:focus{border-color:#ecf0f1}a.list-group-item-success.active{background-color:#18bc9c}a.list-group-item-success.active:hover,a.list-group-item-success.active:focus{background-color:#15a589}a.list-group-item-warning.active{background-color:#f39c12}a.list-group-item-warning.active:hover,a.list-group-item-warning.active:focus{background-color:#e08e0b}a.list-group-item-danger.active{background-color:#e74c3c}a.list-group-item-danger.active:hover,a.list-group-item-danger.active:focus{background-color:#e43725}.panel-default .close{color:#2c3e50}.modal .close{color:#2c3e50}.popover{color:#2c3e50}        &lt;/style&gt;&lt;style&gt;body {
  padding-top: 80px;
}
.content .container-fluid{
    margin-left: 20px !important;
    margin-right: 20px !important;
    margin-bottom: 20px;
}

.page-header{
    border:0 !important;
}

.row.variable, .section-items &gt; .row {
    border: 1px solid #e1e1e8;
    border-top: hidden;
}

.row.spacing{
    padding: 2em 1em;
}

.row.header {
    border-bottom: 1px solid #e1e1e8;
    /*background-color: #f5f5f5;*/
    padding-left: 2em;
}


.dl-horizontal dt {
    text-align: left;
    padding-right: 1em;
    white-space: normal;
}

.dl-horizontal dd {
    margin-left: 0;
}

.col-md-12 {
    padding-left: 2em;
}

.indent {
    margin-left: 1em;
}

.center-img {
    margin-left: auto !important;
    margin-right: auto !important;
    display: block;
}

/* Table example_values */
table.example_values {
    border: 0;
}

.example_values th {
    border: 0;
    padding: 0;
    color: #555;
    font-weight: 600;
}

.example_values tr, .example_values td {
    border: 0;
    padding: 0;
    color: #555;
}

/* STATS */
table.stats, table.sample, table.duplicate{
    border: 0;
}

.stats tr, .sample tr, .duplicate tr {
    border: 0;
}

.stats th, .stats td{
    color: #555;
    border: 0;
}

.stats th {
    padding: 0 2em 0 0;
    font-weight: 600;
}

.stats td {
    padding: 1px;
}


/* Sample table */
table.sample, table.duplicate{
    margin-bottom: 2em;
    margin-left: 1em;
}

.sample td, .sample th, .duplicate td, .duplicate th {
    padding: 0.5em;
    white-space: nowrap;
    border: 0;

}

.sample thead, .duplicate thead {
    border-top: 0;
    border-bottom: 2px solid #ddd;
}

.sample td, .duplicate td {
    width: 100%;
}


/* There is no good solution available to make the divs equal height and then center ... */
.histogram {
    margin-top: 3em;
}

/* Freq table */
table.freq {
    margin-bottom: 2em;
    border: 0;
}

table.freq th, table.freq tr, table.freq td {
    border: 0;
    padding: 0;
}

.freq thead {
    font-weight: 600;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;

}

/* Freq mini */
.freq.mini td {
    width: 50%;
    padding: 1px;
    font-size: 12px;

}

table.freq.mini {
    width: 100%;
}

.freq.mini th {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    max-width: 5em;
    font-weight: 400;
    text-align: right;
    padding-right: 0.5em;
}

/* Message classes */
.missing {
    color: #a94442;
}

.alert, .alert &gt; th, .alert &gt; td {
    color: #a94442;
}

.ignore {
    opacity: 0.4;
}

/* Bars in tables */
.freq.table{
    table-layout: fixed;
}

.freq:not(.mini) tr td:nth-child(1), .freq:not(.mini) tr th:nth-child(1){
    width: auto;
    max-width: none;

    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.freq:not(.mini) tr td:nth-child(2), .freq:not(.mini) tr td:nth-child(3), .freq:not(.mini) tr th:nth-child(2), .freq:not(.mini) tr th:nth-child(3){
    width: 100px;
    text-align: right;
}
.freq:not(.mini) tr td:nth-child(4), .freq:not(.mini) tr th:nth-child(4){
    width:200px;
}

.freq .bar {
    float: left;
    width: 0;
    height: 100%;
    line-height: 20px;
    color: #fff;
    text-align: center;
    background-color: #337ab7;
    border-radius: 3px;
    margin-right: 4px;
}

.other .bar {
    background-color: #999;
}

.missing .bar {
    background-color: #a94442;
}

.tooltip-inner {
    width: 100%;
    white-space: nowrap;
    text-align: left;
}

.extrapadding {
    padding: 2em;
}

.variable .h4 {
    text-overflow: ellipsis;
    display:inline-block;
    width: calc(90%); /* The trick is here! */
    overflow:hidden;
}

.variable.ignore .h4{
    text-decoration: line-through;
}

.table-responsive{
    overflow: scroll;
    width: 100%;
    overflow-y: hidden;
}
.img-responsive{
    max-width: 99%;
}
.footer-text{
    padding:20px;
}

table.list-warnings td{
    padding-right:10px;
}

a.anchor-pos {
    display: block;
    position: relative;
    top: -70px;
    visibility: hidden;
}

a.anchor-pos-variable{
    /*top: -70px;*/
}

#sample-container, #duplicate-container{
    overflow: auto;
    width: 100%;
    overflow-y: hidden;
}

#overview-content td, #overview-content th{
    border-top: 0;
    line-height: 1;
}

.variable-description{
    color: #777;
    font-size: 10pt;
    margin-top: 10px;
    font-style: italic;
}

select.multiple{
    width: 180px;
    height: 500px;
    margin: 10px 0;
}

.named-list-item{
    padding: 1em;
}

/* not printing tabs */
@media print {
    .tab-content &gt; .tab-pane, .collapse {
        display: block !important;
        opacity: 1 !important;
        visibility: visible !important;
        /*page-break-after: always;*/
        page-break-after: right;
        page-break-before: avoid;
    }

    .nav-pills, .nav-tabs, button[data-toggle=&quot;collapse&quot;], .mini, .col-sm-3 img {
        display:none !important;
    }

    a[download=&quot;config.yml&quot;]:after {
        content: none !important;
    }

    .row {
        border: 0 !important;
    }
}

.text-placeholder {
    display: inline-block;
    background-color: #444;
    height: 12px;
    border-radius: 100px;
    margin: 5px 0;
    min-width: 200px;
    opacity: .1;
}&lt;/style&gt;&lt;/head&gt;&lt;body&gt;&lt;a class=anchor-pos id=top&gt;&lt;/a&gt;&lt;nav class=&quot;navbar navbar-default navbar-fixed-top&quot;&gt;&lt;div class=container-fluid&gt;&lt;div class=navbar-header&gt;&lt;button type=button class=&quot;navbar-toggle collapsed&quot; data-toggle=collapse data-target=#navbar aria-expanded=false aria-controls=navbar&gt;&lt;span class=sr-only&gt;Toggle navigation&lt;/span&gt;&lt;span class=icon-bar&gt;&lt;/span&gt;&lt;span class=icon-bar&gt;&lt;/span&gt;&lt;span class=icon-bar&gt;&lt;/span&gt;&lt;/button&gt;&lt;a class=&quot;navbar-brand anchor&quot; href=#top&gt;Pandas Profiling Report&lt;/a&gt;&lt;/div&gt;&lt;div id=navbar class=&quot;navbar-collapse collapse&quot;&gt;&lt;ul class=&quot;nav navbar-nav navbar-right&quot;&gt;&lt;li&gt;&lt;a class=anchor href=#overview&gt;Overview&lt;/a&gt;&lt;/li&gt;&lt;li&gt;&lt;a class=anchor href=#variables&gt;Variables&lt;/a&gt;&lt;/li&gt;&lt;li&gt;&lt;a class=anchor href=#missing&gt;Missing values&lt;/a&gt;&lt;/li&gt;&lt;li&gt;&lt;a class=anchor href=#sample&gt;Sample&lt;/a&gt;&lt;/li&gt;&lt;/ul&gt;&lt;/div&gt;&lt;/div&gt;&lt;/nav&gt;&lt;div class=content&gt;&lt;div class=container-fluid&gt;&lt;div class=&quot;row header&quot;&gt;&lt;a class=anchor-pos id=overview&gt;&lt;/a&gt;&lt;h1 class=page-header&gt;Overview&lt;/h1&gt;&lt;/div&gt;&lt;div class=section-items&gt;&lt;div class=&quot;row spacing&quot;&gt;&lt;ul class=&quot;nav nav-pills&quot; role=tablist&gt;&lt;li role=presentation class=active&gt;&lt;a href=#overview-dataset_overview aria-controls=overview-dataset_overview role=tab data-toggle=tab&gt;Overview&lt;/a&gt;&lt;/li&gt;&lt;li role=presentation&gt;&lt;a href=#overview-dataset aria-controls=overview-dataset role=tab data-toggle=tab&gt;Dataset&lt;/a&gt;&lt;/li&gt;&lt;li role=presentation&gt;&lt;a href=#overview-alerts aria-controls=overview-alerts role=tab data-toggle=tab&gt;Alerts &lt;span class=badge&gt;7&lt;/span&gt;&lt;/a&gt;&lt;/li&gt;&lt;li role=presentation&gt;&lt;a href=#overview-reproduction aria-controls=overview-reproduction role=tab data-toggle=tab&gt;Reproduction&lt;/a&gt;&lt;/li&gt;&lt;/ul&gt;&lt;div class=tab-content style=&quot;padding-top: 10px;&quot;&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12 active&quot; id=overview-dataset_overview&gt;&lt;div class=col-sm-6&gt;&lt;p class=h4&gt;Dataset statistics&lt;/p&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;Number of variables&lt;/th&gt;&lt;td&gt;9&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Number of observations&lt;/th&gt;&lt;td&gt;879159&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Missing cells&lt;/th&gt;&lt;td&gt;60960&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Missing cells (%)&lt;/th&gt;&lt;td&gt;0.8%&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Total size in memory&lt;/th&gt;&lt;td&gt;53.5 MiB&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Average record size in memory&lt;/th&gt;&lt;td&gt;63.8 B&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div class=col-sm-6&gt;&lt;p class=h4&gt;Variable types&lt;/p&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;Categorical&lt;/th&gt;&lt;td&gt;5&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Numeric&lt;/th&gt;&lt;td&gt;4&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;/div&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12&quot; id=overview-dataset&gt;&lt;div class=col-sm-12&gt;&lt;p class=h4&gt;Dataset&lt;/p&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;Description&lt;/th&gt;&lt;td&gt;Relatório Consolidado de Inspeções de Monitoração da Anatel&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Author&lt;/th&gt;&lt;td&gt;Ronaldo da Silva Alves Batista&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;URL&lt;/th&gt;&lt;td&gt;&lt;a href=https://ronaldokun.github.io/anatelreporter/ &gt;https://ronaldokun.github.io/anatelreporter/&lt;/a&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Copyright&lt;/th&gt;&lt;td&gt;(c) Anatel - Agência Nacional de Telecomunicações 2022&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;/div&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12&quot; id=overview-alerts&gt;&lt;table class=&quot;table table-condensed list-warnings&quot;&gt;&lt;p class=h4&gt;Alerts&lt;/p&gt;&lt;tr style=border-top:0&gt;&lt;td&gt;&lt;a class=anchor href=#pp_var_3402945652136267808&gt;&lt;code&gt;Frequency&lt;/code&gt;&lt;/a&gt; has a high cardinality: 12562 distinct values &lt;/td&gt;&lt;td&gt;&lt;span class=&quot;label label-primary&quot;&gt;High cardinality&lt;/span&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;a class=anchor href=#pp_var_-8438619141185252187&gt;&lt;code&gt;Description&lt;/code&gt;&lt;/a&gt; has a high cardinality: 234096 distinct values &lt;/td&gt;&lt;td&gt;&lt;span class=&quot;label label-primary&quot;&gt;High cardinality&lt;/span&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;a class=anchor href=#pp_var_3243557442294903904&gt;&lt;code&gt;Station&lt;/code&gt;&lt;/a&gt; has a high cardinality: 226569 distinct values &lt;/td&gt;&lt;td&gt;&lt;span class=&quot;label label-primary&quot;&gt;High cardinality&lt;/span&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;a class=anchor href=#pp_var_-3991132923749349832&gt;&lt;code&gt;Class&lt;/code&gt;&lt;/a&gt; has a high cardinality: 102 distinct values &lt;/td&gt;&lt;td&gt;&lt;span class=&quot;label label-primary&quot;&gt;High cardinality&lt;/span&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;a class=anchor href=#pp_var_-3991132923749349832&gt;&lt;code&gt;Class&lt;/code&gt;&lt;/a&gt; has 59068 (6.7%) missing values &lt;/td&gt;&lt;td&gt;&lt;span class=&quot;label label-info&quot;&gt;Missing&lt;/span&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;a class=anchor href=#pp_var_8124034662335410336&gt;&lt;code&gt;BW&lt;/code&gt;&lt;/a&gt; is highly skewed (γ1 = 252.8905792) &lt;/td&gt;&lt;td&gt;&lt;span class=&quot;label label-info&quot;&gt;Skewed&lt;/span&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;a class=anchor href=#pp_var_-9099077803151007301&gt;&lt;code&gt;Id&lt;/code&gt;&lt;/a&gt; has unique values &lt;/td&gt;&lt;td&gt;&lt;span class=&quot;label label-primary&quot;&gt;Unique&lt;/span&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;&lt;/div&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12&quot; id=overview-reproduction&gt;&lt;div class=col-sm-12&gt;&lt;p class=h4&gt;Reproduction&lt;/p&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;Analysis started&lt;/th&gt;&lt;td&gt;2022-07-12 16:06:35.364667&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Analysis finished&lt;/th&gt;&lt;td&gt;2022-07-12 16:06:40.938775&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Duration&lt;/th&gt;&lt;td&gt;5.57 seconds&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Software version&lt;/th&gt;&lt;td&gt;&lt;a href=https://github.com/pandas-profiling/pandas-profiling&gt;pandas-profiling v3.2.0&lt;/a&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Download configuration&lt;/th&gt;&lt;td&gt;&lt;a download=config.json href=&quot;data:text/plain;charset=utf-8,%7B%22title%22%3A%20%22Pandas%20Profiling%20Report%22%2C%20%22dataset%22%3A%20%7B%22description%22%3A%20%22Relat%5Cu00f3rio%20Consolidado%20de%20Inspe%5Cu00e7%5Cu00f5es%20de%20Monitora%5Cu00e7%5Cu00e3o%20da%20Anatel%22%2C%20%22creator%22%3A%20%22%22%2C%20%22author%22%3A%20%22Ronaldo%20da%20Silva%20Alves%20Batista%22%2C%20%22copyright_holder%22%3A%20%22Anatel%20-%20Ag%5Cu00eancia%20Nacional%20de%20Telecomunica%5Cu00e7%5Cu00f5es%22%2C%20%22copyright_year%22%3A%20%222022%22%2C%20%22url%22%3A%20%22https%3A//ronaldokun.github.io/anatelreporter/%22%7D%2C%20%22variables%22%3A%20%7B%22descriptions%22%3A%20%7B%7D%7D%2C%20%22infer_dtypes%22%3A%20false%2C%20%22show_variable_description%22%3A%20true%2C%20%22pool_size%22%3A%200%2C%20%22progress_bar%22%3A%20true%2C%20%22vars%22%3A%20%7B%22num%22%3A%20%7B%22quantiles%22%3A%20%5B0.05%2C%200.25%2C%200.5%2C%200.75%2C%200.95%5D%2C%20%22skewness_threshold%22%3A%2020%2C%20%22low_categorical_threshold%22%3A%205%2C%20%22chi_squared_threshold%22%3A%200.0%7D%2C%20%22cat%22%3A%20%7B%22length%22%3A%20false%2C%20%22characters%22%3A%20false%2C%20%22words%22%3A%20false%2C%20%22cardinality_threshold%22%3A%2050%2C%20%22n_obs%22%3A%205%2C%20%22chi_squared_threshold%22%3A%200.0%2C%20%22coerce_str_to_date%22%3A%20false%2C%20%22redact%22%3A%20false%2C%20%22histogram_largest%22%3A%2010%2C%20%22stop_words%22%3A%20%5B%5D%7D%2C%20%22image%22%3A%20%7B%22active%22%3A%20false%2C%20%22exif%22%3A%20false%2C%20%22hash%22%3A%20false%7D%2C%20%22bool%22%3A%20%7B%22n_obs%22%3A%203%2C%20%22mappings%22%3A%20%7B%22t%22%3A%20true%2C%20%22f%22%3A%20false%2C%20%22True%22%3A%20true%2C%20%22False%22%3A%20false%2C%20%22y%22%3A%20true%2C%20%22n%22%3A%20false%7D%7D%2C%20%22path%22%3A%20%7B%22active%22%3A%20false%7D%2C%20%22file%22%3A%20%7B%22active%22%3A%20false%7D%2C%20%22url%22%3A%20%7B%22active%22%3A%20true%7D%7D%2C%20%22sort%22%3A%20null%2C%20%22missing_diagrams%22%3A%20%7B%22bar%22%3A%20true%2C%20%22matrix%22%3A%20true%2C%20%22heatmap%22%3A%20false%2C%20%22dendrogram%22%3A%20false%7D%2C%20%22correlations%22%3A%20%7B%22pearson%22%3A%20%7B%22key%22%3A%20%22%22%2C%20%22calculate%22%3A%20false%2C%20%22warn_high_correlations%22%3A%201%2C%20%22threshold%22%3A%200.9%7D%2C%20%22spearman%22%3A%20%7B%22key%22%3A%20%22%22%2C%20%22calculate%22%3A%20false%2C%20%22warn_high_correlations%22%3A%200%2C%20%22threshold%22%3A%200.9%7D%2C%20%22kendall%22%3A%20%7B%22key%22%3A%20%22%22%2C%20%22calculate%22%3A%20false%2C%20%22warn_high_correlations%22%3A%200%2C%20%22threshold%22%3A%200.9%7D%2C%20%22phi_k%22%3A%20%7B%22key%22%3A%20%22%22%2C%20%22calculate%22%3A%20false%2C%20%22warn_high_correlations%22%3A%200%2C%20%22threshold%22%3A%200.9%7D%2C%20%22cramers%22%3A%20%7B%22key%22%3A%20%22%22%2C%20%22calculate%22%3A%20false%2C%20%22warn_high_correlations%22%3A%201%2C%20%22threshold%22%3A%200.9%7D%7D%2C%20%22interactions%22%3A%20%7B%22continuous%22%3A%20false%2C%20%22targets%22%3A%20%5B%5D%7D%2C%20%22categorical_maximum_correlation_distinct%22%3A%20100%2C%20%22memory_deep%22%3A%20false%2C%20%22plot%22%3A%20%7B%22missing%22%3A%20%7B%22force_labels%22%3A%20true%2C%20%22cmap%22%3A%20%22RdBu_r%22%7D%2C%20%22image_format%22%3A%20%22svg%22%2C%20%22correlation%22%3A%20%7B%22cmap%22%3A%20%22RdBu%22%2C%20%22bad%22%3A%20%22%23000000%22%7D%2C%20%22dpi%22%3A%20300%2C%20%22histogram%22%3A%20%7B%22bins%22%3A%2050%2C%20%22max_bins%22%3A%20250%2C%20%22x_axis_labels%22%3A%20true%7D%2C%20%22scatter_threshold%22%3A%201000%2C%20%22cat_freq%22%3A%20%7B%22show%22%3A%20true%2C%20%22type%22%3A%20%22bar%22%2C%20%22max_unique%22%3A%2010%2C%20%22colors%22%3A%20null%7D%7D%2C%20%22duplicates%22%3A%20%7B%22head%22%3A%200%2C%20%22key%22%3A%20%22%23%20duplicates%22%7D%2C%20%22samples%22%3A%20%7B%22head%22%3A%2010%2C%20%22tail%22%3A%2010%2C%20%22random%22%3A%2010%7D%2C%20%22reject_variables%22%3A%20false%2C%20%22n_obs_unique%22%3A%2010%2C%20%22n_freq_table_max%22%3A%20100%2C%20%22n_extreme_obs%22%3A%2010%2C%20%22report%22%3A%20%7B%22precision%22%3A%2010%7D%2C%20%22html%22%3A%20%7B%22style%22%3A%20%7B%22primary_color%22%3A%20%22%23337ab7%22%2C%20%22logo%22%3A%20%22%22%2C%20%22theme%22%3A%20%22flatly%22%7D%2C%20%22navbar_show%22%3A%20true%2C%20%22minify_html%22%3A%20true%2C%20%22use_local_assets%22%3A%20true%2C%20%22inline%22%3A%20true%2C%20%22assets_prefix%22%3A%20null%2C%20%22assets_path%22%3A%20null%2C%20%22full_width%22%3A%20true%7D%2C%20%22notebook%22%3A%20%7B%22iframe%22%3A%20%7B%22height%22%3A%20%22800px%22%2C%20%22width%22%3A%20%22100%25%22%2C%20%22attribute%22%3A%20%22srcdoc%22%7D%7D%7D&quot;&gt;config.json&lt;/a&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;div class=&quot;row header&quot;&gt;&lt;a class=anchor-pos id=variables&gt;&lt;/a&gt;&lt;h1 class=page-header&gt;Variables&lt;/h1&gt;&lt;/div&gt;&lt;div class=section-items&gt;&lt;div class=&quot;row spacing&quot;&gt;&lt;a class=&quot;anchor-pos anchor-pos-variable&quot; id=pp_var_3402945652136267808&gt;&lt;/a&gt;&lt;div class=variable&gt;&lt;div class=col-sm-3&gt;&lt;p class=h4 title=Frequency&gt;&lt;a href=#pp_var_3402945652136267808&gt;Frequency&lt;/a&gt;&lt;br&gt;&lt;small&gt;Categorical&lt;/small&gt;&lt;/p&gt;&lt;code&gt;HIGH CARDINALITY&lt;/code&gt;&lt;br&gt;&lt;p class=variable-description&gt;&lt;/p&gt;&lt;/div&gt;&lt;div class=col-sm-3&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr class=alert&gt;&lt;th&gt;Distinct&lt;/th&gt;&lt;td&gt;12562&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Distinct (%)&lt;/th&gt;&lt;td&gt;1.4%&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Missing&lt;/th&gt;&lt;td&gt;0&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Missing (%)&lt;/th&gt;&lt;td&gt;0.0%&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Memory size&lt;/th&gt;&lt;td&gt;2.0 MiB&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div class=col-sm-6&gt;&lt;div class=&quot;col-sm- collapse in&quot; id=minifreqtable&gt;&lt;table class=&quot;mini freq&quot;&gt;&lt;tr class&gt;&lt;th width=50%&gt; 246.875 &lt;/th&gt;&lt;td width=50%&gt;&lt;div class=bar style=width:0.4% data-toggle=tooltip data-placement=right data-html=true data-delay=500&gt; &amp;nbsp; &lt;/div&gt; 3804 &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;th width=50%&gt; 167.90625 &lt;/th&gt;&lt;td width=50%&gt;&lt;div class=bar style=width:0.4% data-toggle=tooltip data-placement=right data-html=true data-delay=500&gt; &amp;nbsp; &lt;/div&gt; 3677 &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;th width=50%&gt; 167.60625 &lt;/th&gt;&lt;td width=50%&gt;&lt;div class=bar style=width:0.4% data-toggle=tooltip data-placement=right data-html=true data-delay=500&gt; &amp;nbsp; &lt;/div&gt; 3625 &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;th width=50%&gt; 168.28125 &lt;/th&gt;&lt;td width=50%&gt;&lt;div class=bar style=width:0.4% data-toggle=tooltip data-placement=right data-html=true data-delay=500&gt; &amp;nbsp; &lt;/div&gt; 3617 &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;th width=50%&gt; 167.98125 &lt;/th&gt;&lt;td width=50%&gt;&lt;div class=bar style=width:0.4% data-toggle=tooltip data-placement=right data-html=true data-delay=500&gt; &amp;nbsp; &lt;/div&gt; 3614 &lt;/td&gt;&lt;/tr&gt;&lt;tr class=other&gt;&lt;th width=50%&gt; Other values (12557) &lt;/th&gt;&lt;td width=50%&gt;&lt;div class=bar style=width:100.0% data-toggle=tooltip data-placement=right data-html=true data-delay=500&gt; 860822&amp;nbsp; &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;&lt;/div&gt;&lt;/div&gt;&lt;div class=&quot;col-sm-12 text-right&quot;&gt;&lt;button class=&quot;btn btn-default btn-sm&quot; data-toggle=collapse data-target=&quot;#bottom-3402945652136267808, #minifreqtable3402945652136267808&quot; aria-expanded=true aria-controls=collapseExample&gt;Toggle details&lt;/button&gt;&lt;/div&gt;&lt;div id=bottom-3402945652136267808 class=collapse&gt;&lt;div class=&quot;row spacing&quot;&gt;&lt;ul class=&quot;nav nav-tabs&quot; role=tablist&gt;&lt;li role=presentation class=active&gt;&lt;a href=#3402945652136267808bottom-3402945652136267808overview aria-controls=3402945652136267808bottom-3402945652136267808overview role=tab data-toggle=tab&gt;Overview&lt;/a&gt;&lt;/li&gt;&lt;li role=presentation&gt;&lt;a href=#3402945652136267808bottom-3402945652136267808string aria-controls=3402945652136267808bottom-3402945652136267808string role=tab data-toggle=tab&gt;Categories&lt;/a&gt;&lt;/li&gt;&lt;/ul&gt;&lt;div class=tab-content&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12 active&quot; id=3402945652136267808bottom-3402945652136267808overview&gt;&lt;div class=row&gt;&lt;div class=col-sm-6&gt;&lt;p class=h4&gt;Unique&lt;/p&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;Unique&lt;/th&gt;&lt;td&gt;1988 &lt;span class=&quot;badge pull-right&quot; style=color:#fff;background-color:#337ab7; title=&quot;The number of unique values (all values that occur exactly once in the dataset).&quot;&gt;?&lt;/span&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Unique (%)&lt;/th&gt;&lt;td&gt;0.2%&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div class=col-sm-6&gt;&lt;p class=h4&gt;Sample&lt;/p&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;1st row&lt;/th&gt;&lt;td&gt;0.028&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;2nd row&lt;/th&gt;&lt;td&gt;0.0285&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;3rd row&lt;/th&gt;&lt;td&gt;0.03&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;4th row&lt;/th&gt;&lt;td&gt;0.03&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;5th row&lt;/th&gt;&lt;td&gt;0.03&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12&quot; id=3402945652136267808bottom-3402945652136267808string&gt;&lt;div class=row&gt;&lt;div class=col-sm-12&gt;&lt;h4&gt;Common Values&lt;/h4&gt;&lt;table class=&quot;freq table table-hover table-striped&quot;&gt;&lt;thead&gt;&lt;tr&gt;&lt;td&gt;Value&lt;/td&gt;&lt;td&gt;Count&lt;/td&gt;&lt;td&gt;Frequency (%)&lt;/td&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr class&gt;&lt;td title=246.875&gt;246.875&lt;/td&gt;&lt;td&gt;3804&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.90625&gt;167.90625&lt;/td&gt;&lt;td&gt;3677&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.60625&gt;167.60625&lt;/td&gt;&lt;td&gt;3625&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.28125&gt;168.28125&lt;/td&gt;&lt;td&gt;3617&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.98125&gt;167.98125&lt;/td&gt;&lt;td&gt;3614&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.96875&gt;167.96875&lt;/td&gt;&lt;td&gt;3573&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.83125&gt;167.83125&lt;/td&gt;&lt;td&gt;3559&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.13125&gt;168.13125&lt;/td&gt;&lt;td&gt;3549&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.68125&gt;167.68125&lt;/td&gt;&lt;td&gt;3544&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.18125&gt;168.18125&lt;/td&gt;&lt;td&gt;3539&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.38125&gt;168.38125&lt;/td&gt;&lt;td&gt;3534&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.66875&gt;167.66875&lt;/td&gt;&lt;td&gt;3531&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.20625&gt;168.20625&lt;/td&gt;&lt;td&gt;3525&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.75625&gt;167.75625&lt;/td&gt;&lt;td&gt;3524&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.69375&gt;167.69375&lt;/td&gt;&lt;td&gt;3510&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.86875&gt;167.86875&lt;/td&gt;&lt;td&gt;3508&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.05625&gt;168.05625&lt;/td&gt;&lt;td&gt;3501&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.61875&gt;167.61875&lt;/td&gt;&lt;td&gt;3485&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.73125&gt;167.73125&lt;/td&gt;&lt;td&gt;3485&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.09375&gt;168.09375&lt;/td&gt;&lt;td&gt;3478&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.30625&gt;168.30625&lt;/td&gt;&lt;td&gt;3478&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.29375&gt;168.29375&lt;/td&gt;&lt;td&gt;3469&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.84375&gt;167.84375&lt;/td&gt;&lt;td&gt;3468&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.35625&gt;168.35625&lt;/td&gt;&lt;td&gt;3466&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.79375&gt;167.79375&lt;/td&gt;&lt;td&gt;3447&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.26875&gt;168.26875&lt;/td&gt;&lt;td&gt;3435&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.95625&gt;167.95625&lt;/td&gt;&lt;td&gt;3433&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.10625&gt;168.10625&lt;/td&gt;&lt;td&gt;3430&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.65625&gt;167.65625&lt;/td&gt;&lt;td&gt;3428&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.76875&gt;167.76875&lt;/td&gt;&lt;td&gt;3423&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.16875&gt;168.16875&lt;/td&gt;&lt;td&gt;3422&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.63125&gt;167.63125&lt;/td&gt;&lt;td&gt;3420&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.33125&gt;168.33125&lt;/td&gt;&lt;td&gt;3416&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.70625&gt;167.70625&lt;/td&gt;&lt;td&gt;3412&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.89375&gt;167.89375&lt;/td&gt;&lt;td&gt;3407&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.03125&gt;168.03125&lt;/td&gt;&lt;td&gt;3406&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.31875&gt;168.31875&lt;/td&gt;&lt;td&gt;3401&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.11875&gt;168.11875&lt;/td&gt;&lt;td&gt;3399&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.94375&gt;167.94375&lt;/td&gt;&lt;td&gt;3390&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.71875&gt;167.71875&lt;/td&gt;&lt;td&gt;3385&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.39375&gt;168.39375&lt;/td&gt;&lt;td&gt;3376&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.34375&gt;168.34375&lt;/td&gt;&lt;td&gt;3372&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.64375&gt;167.64375&lt;/td&gt;&lt;td&gt;3361&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.40625&gt;168.40625&lt;/td&gt;&lt;td&gt;3357&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.80625&gt;167.80625&lt;/td&gt;&lt;td&gt;3354&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.81875&gt;167.81875&lt;/td&gt;&lt;td&gt;3354&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.21875&gt;168.21875&lt;/td&gt;&lt;td&gt;3349&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.78125&gt;167.78125&lt;/td&gt;&lt;td&gt;3344&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.91875&gt;167.91875&lt;/td&gt;&lt;td&gt;3344&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.01875&gt;168.01875&lt;/td&gt;&lt;td&gt;3340&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.85625&gt;167.85625&lt;/td&gt;&lt;td&gt;3338&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.06875&gt;168.06875&lt;/td&gt;&lt;td&gt;3337&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.74375&gt;167.74375&lt;/td&gt;&lt;td&gt;3337&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.25625&gt;168.25625&lt;/td&gt;&lt;td&gt;3335&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.00625&gt;168.00625&lt;/td&gt;&lt;td&gt;3334&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.15625&gt;168.15625&lt;/td&gt;&lt;td&gt;3333&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.24375&gt;168.24375&lt;/td&gt;&lt;td&gt;3330&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.88125&gt;167.88125&lt;/td&gt;&lt;td&gt;3330&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.93125&gt;167.93125&lt;/td&gt;&lt;td&gt;3326&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.23125&gt;168.23125&lt;/td&gt;&lt;td&gt;3325&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.14375&gt;168.14375&lt;/td&gt;&lt;td&gt;3321&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.08125&gt;168.08125&lt;/td&gt;&lt;td&gt;3317&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.19375&gt;168.19375&lt;/td&gt;&lt;td&gt;3316&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167.99375&gt;167.99375&lt;/td&gt;&lt;td&gt;3311&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.04375&gt;168.04375&lt;/td&gt;&lt;td&gt;3306&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.36875&gt;168.36875&lt;/td&gt;&lt;td&gt;3299&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=19288.0&gt;19288.0&lt;/td&gt;&lt;td&gt;2796&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.5%&gt; &amp;nbsp; &lt;/div&gt; 0.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=17727.0&gt;17727.0&lt;/td&gt;&lt;td&gt;2505&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.4%&gt; &amp;nbsp; &lt;/div&gt; 0.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=19343.0&gt;19343.0&lt;/td&gt;&lt;td&gt;2172&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.4%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=156.8&gt;156.8&lt;/td&gt;&lt;td&gt;2148&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.4%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=246.95&gt;246.95&lt;/td&gt;&lt;td&gt;2067&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=17782.0&gt;17782.0&lt;/td&gt;&lt;td&gt;2005&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=87.9&gt;87.9&lt;/td&gt;&lt;td&gt;1979&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=19398.0&gt;19398.0&lt;/td&gt;&lt;td&gt;1881&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.48125&gt;168.48125&lt;/td&gt;&lt;td&gt;1860&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.43125&gt;168.43125&lt;/td&gt;&lt;td&gt;1808&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=104.9&gt;104.9&lt;/td&gt;&lt;td&gt;1807&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=8059.02&gt;8059.02&lt;/td&gt;&lt;td&gt;1794&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=7747.7&gt;7747.7&lt;/td&gt;&lt;td&gt;1779&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=17837.0&gt;17837.0&lt;/td&gt;&lt;td&gt;1726&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=19453.0&gt;19453.0&lt;/td&gt;&lt;td&gt;1698&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.49375&gt;168.49375&lt;/td&gt;&lt;td&gt;1672&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.46875&gt;168.46875&lt;/td&gt;&lt;td&gt;1669&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.44375&gt;168.44375&lt;/td&gt;&lt;td&gt;1659&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.45625&gt;168.45625&lt;/td&gt;&lt;td&gt;1651&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=160.99&gt;160.99&lt;/td&gt;&lt;td&gt;1640&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=168.41875&gt;168.41875&lt;/td&gt;&lt;td&gt;1623&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=8088.67&gt;8088.67&lt;/td&gt;&lt;td&gt;1598&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=7777.35&gt;7777.35&lt;/td&gt;&lt;td&gt;1590&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=18058.0&gt;18058.0&lt;/td&gt;&lt;td&gt;1579&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=161.39&gt;161.39&lt;/td&gt;&lt;td&gt;1575&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=19508.0&gt;19508.0&lt;/td&gt;&lt;td&gt;1560&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=17948.0&gt;17948.0&lt;/td&gt;&lt;td&gt;1560&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=161.23&gt;161.23&lt;/td&gt;&lt;td&gt;1557&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=17892.0&gt;17892.0&lt;/td&gt;&lt;td&gt;1552&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=156.45&gt;156.45&lt;/td&gt;&lt;td&gt;1542&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=156.7&gt;156.7&lt;/td&gt;&lt;td&gt;1515&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=8412.0&gt;8412.0&lt;/td&gt;&lt;td&gt;1511&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=156.65&gt;156.65&lt;/td&gt;&lt;td&gt;1507&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=156.6&gt;156.6&lt;/td&gt;&lt;td&gt;1504&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class=other&gt;&lt;td title=&quot;Other values (12462)&quot;&gt;Other values (12462)&lt;/td&gt;&lt;td&gt;592607&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt; 67.4% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;div class=&quot;row spacing&quot;&gt;&lt;a class=&quot;anchor-pos anchor-pos-variable&quot; id=pp_var_459491982266170039&gt;&lt;/a&gt;&lt;div class=variable&gt;&lt;div class=col-sm-3&gt;&lt;p class=h4 title=Latitude&gt;&lt;a href=#pp_var_459491982266170039&gt;Latitude&lt;/a&gt;&lt;br&gt;&lt;small&gt;Real number (&amp;Ropf;)&lt;/small&gt;&lt;/p&gt;&lt;p class=variable-description&gt;&lt;/p&gt;&lt;/div&gt;&lt;div class=col-sm-3&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;Distinct&lt;/th&gt;&lt;td&gt;153257&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Distinct (%)&lt;/th&gt;&lt;td&gt;17.4%&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Missing&lt;/th&gt;&lt;td&gt;0&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Missing (%)&lt;/th&gt;&lt;td&gt;0.0%&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Infinite&lt;/th&gt;&lt;td&gt;0&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Infinite (%)&lt;/th&gt;&lt;td&gt;0.0%&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Mean&lt;/th&gt;&lt;td&gt;-18.87641821&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div class=col-sm-3&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;Minimum&lt;/th&gt;&lt;td&gt;-89.59463611&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Maximum&lt;/th&gt;&lt;td&gt;89.79706389&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Zeros&lt;/th&gt;&lt;td&gt;48&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Zeros (%)&lt;/th&gt;&lt;td&gt;&lt; 0.1%&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Negative&lt;/th&gt;&lt;td&gt;874743&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Negative (%)&lt;/th&gt;&lt;td&gt;99.5%&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Memory size&lt;/th&gt;&lt;td&gt;6.7 MiB&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div class=col-sm-3&gt;&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot; standalone=&quot;no&quot;?&gt;&lt;!DOCTYPE svg class=&quot;img-responsive center-img&quot;PUBLIC &quot;-//W3C//DTD SVG 1.1//EN&quot;
  &quot;http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd&quot;&gt;&lt;svg class=&quot;img-responsive center-img&quot; xmlns:xlink=http://www.w3.org/1999/xlink width=216pt height=162pt viewbox=&quot;0 0 216 162&quot; xmlns=http://www.w3.org/2000/svg version=1.1&gt;&lt;metadata&gt;&lt;rdf:rdf xmlns:dc=http://purl.org/dc/elements/1.1/ xmlns:cc=http://creativecommons.org/ns# xmlns:rdf=http://www.w3.org/1999/02/22-rdf-syntax-ns#&gt;&lt;cc:work&gt;&lt;dc:type rdf:resource=http://purl.org/dc/dcmitype/StillImage /&gt;&lt;dc:date&gt;2022-07-12T13:06:41.041490&lt;/dc:date&gt;&lt;dc:format&gt;image/svg+xml&lt;/dc:format&gt;&lt;dc:creator&gt;&lt;cc:agent&gt;&lt;dc:title&gt;Matplotlib v3.5.2, https://matplotlib.org/&lt;/dc:title&gt;&lt;/cc:agent&gt;&lt;/dc:creator&gt;&lt;/cc:work&gt;&lt;/rdf:rdf&gt;&lt;/metadata&gt;&lt;defs&gt;&lt;style type=text/css&gt;*{stroke-linejoin: round; stroke-linecap: butt}&lt;/style&gt;&lt;/defs&gt;&lt;g id=figure_1&gt;&lt;g id=patch_1&gt;&lt;path d=&quot;M 0 162 
L 216 162 
L 216 0 
L 0 0 
z
&quot; style=&quot;fill: #ffffff&quot;/&gt;&lt;/g&gt;&lt;g id=axes_1&gt;&lt;g id=patch_2&gt;&lt;path d=&quot;M 10.8 126.06289 
L 205.2 126.06289 
L 205.2 10.8 
L 10.8 10.8 
z
&quot; style=&quot;fill: #ffffff&quot;/&gt;&lt;/g&gt;&lt;g id=matplotlib.axis_1&gt;&lt;g id=xtick_1&gt;&lt;g id=text_1&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(55.307583 150.207399)rotate(-45)scale(0.08 -0.08)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-2212 transform=scale(0.015625) d=&quot;M 3381 1997 
L 356 1997 
L 356 2522 
L 3381 2522 
L 3381 1997 
z
&quot;/&gt;&lt;path id=ArialMT-35 transform=scale(0.015625) d=&quot;M 266 1200 
L 856 1250 
Q 922 819 1161 601 
Q 1400 384 1738 384 
Q 2144 384 2425 690 
Q 2706 997 2706 1503 
Q 2706 1984 2436 2262 
Q 2166 2541 1728 2541 
Q 1456 2541 1237 2417 
Q 1019 2294 894 2097 
L 366 2166 
L 809 4519 
L 3088 4519 
L 3088 3981 
L 1259 3981 
L 1013 2750 
Q 1425 3038 1878 3038 
Q 2478 3038 2890 2622 
Q 3303 2206 3303 1553 
Q 3303 931 2941 478 
Q 2500 -78 1738 -78 
Q 1113 -78 717 272 
Q 322 622 266 1200 
z
&quot;/&gt;&lt;path id=ArialMT-30 transform=scale(0.015625) d=&quot;M 266 2259 
Q 266 3072 433 3567 
Q 600 4063 929 4331 
Q 1259 4600 1759 4600 
Q 2128 4600 2406 4451 
Q 2684 4303 2865 4023 
Q 3047 3744 3150 3342 
Q 3253 2941 3253 2259 
Q 3253 1453 3087 958 
Q 2922 463 2592 192 
Q 2263 -78 1759 -78 
Q 1097 -78 719 397 
Q 266 969 266 2259 
z
M 844 2259 
Q 844 1131 1108 757 
Q 1372 384 1759 384 
Q 2147 384 2411 759 
Q 2675 1134 2675 2259 
Q 2675 3391 2411 3762 
Q 2147 4134 1753 4134 
Q 1366 4134 1134 3806 
Q 844 3388 844 2259 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-2212 /&gt;&lt;use xlink:href=#ArialMT-35 x=58.398438 /&gt;&lt;use xlink:href=#ArialMT-30 x=114.013672 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_2&gt;&lt;g id=text_2&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(107.789804 143.757701)rotate(-45)scale(0.08 -0.08)&quot;&gt;&lt;use xlink:href=#ArialMT-30 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_3&gt;&lt;g id=text_3&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(155.474305 146.903442)rotate(-45)scale(0.08 -0.08)&quot;&gt;&lt;use xlink:href=#ArialMT-35 /&gt;&lt;use xlink:href=#ArialMT-30 x=55.615234 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=patch_3&gt;&lt;path d=&quot;M 19.636364 126.06289 
L 23.170909 126.06289 
L 23.170909 126.061614 
L 19.636364 126.061614 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_4&gt;&lt;path d=&quot;M 23.170909 126.06289 
L 26.705455 126.06289 
L 26.705455 126.06289 
L 23.170909 126.06289 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_5&gt;&lt;path d=&quot;M 26.705455 126.06289 
L 30.24 126.06289 
L 30.24 126.06289 
L 26.705455 126.06289 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_6&gt;&lt;path d=&quot;M 30.24 126.06289 
L 33.774545 126.06289 
L 33.774545 126.06289 
L 30.24 126.06289 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_7&gt;&lt;path d=&quot;M 33.774545 126.06289 
L 37.309091 126.06289 
L 37.309091 126.062252 
L 33.774545 126.062252 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_8&gt;&lt;path d=&quot;M 37.309091 126.06289 
L 40.843636 126.06289 
L 40.843636 126.06289 
L 37.309091 126.06289 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_9&gt;&lt;path d=&quot;M 40.843636 126.06289 
L 44.378182 126.06289 
L 44.378182 126.06289 
L 40.843636 126.06289 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_10&gt;&lt;path d=&quot;M 44.378182 126.06289 
L 47.912727 126.06289 
L 47.912727 126.06289 
L 44.378182 126.06289 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_11&gt;&lt;path d=&quot;M 47.912727 126.06289 
L 51.447273 126.06289 
L 51.447273 126.06289 
L 47.912727 126.06289 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_12&gt;&lt;path d=&quot;M 51.447273 126.06289 
L 54.981818 126.06289 
L 54.981818 126.061933 
L 51.447273 126.061933 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_13&gt;&lt;path d=&quot;M 54.981818 126.06289 
L 58.516364 126.06289 
L 58.516364 126.057787 
L 54.981818 126.057787 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_14&gt;&lt;path d=&quot;M 58.516364 126.06289 
L 62.050909 126.06289 
L 62.050909 125.853371 
L 58.516364 125.853371 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_15&gt;&lt;path d=&quot;M 62.050909 126.06289 
L 65.585455 126.06289 
L 65.585455 126.053641 
L 62.050909 126.053641 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_16&gt;&lt;path d=&quot;M 65.585455 126.06289 
L 69.12 126.06289 
L 69.12 126.062252 
L 65.585455 126.062252 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_17&gt;&lt;path d=&quot;M 69.12 126.06289 
L 72.654545 126.06289 
L 72.654545 126.060338 
L 69.12 126.060338 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_18&gt;&lt;path d=&quot;M 72.654545 126.06289 
L 76.189091 126.06289 
L 76.189091 125.942345 
L 72.654545 125.942345 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_19&gt;&lt;path d=&quot;M 76.189091 126.06289 
L 79.723636 126.06289 
L 79.723636 116.62593 
L 76.189091 116.62593 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_20&gt;&lt;path d=&quot;M 79.723636 126.06289 
L 83.258182 126.06289 
L 83.258182 110.685416 
L 79.723636 110.685416 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_21&gt;&lt;path d=&quot;M 83.258182 126.06289 
L 86.792727 126.06289 
L 86.792727 50.499921 
L 83.258182 50.499921 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_22&gt;&lt;path d=&quot;M 86.792727 126.06289 
L 90.327273 126.06289 
L 90.327273 16.288709 
L 86.792727 16.288709 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_23&gt;&lt;path d=&quot;M 90.327273 126.06289 
L 93.861818 126.06289 
L 93.861818 109.523335 
L 90.327273 109.523335 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_24&gt;&lt;path d=&quot;M 93.861818 126.06289 
L 97.396364 126.06289 
L 97.396364 111.401352 
L 93.861818 111.401352 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_25&gt;&lt;path d=&quot;M 97.396364 126.06289 
L 100.930909 126.06289 
L 100.930909 111.966447 
L 97.396364 111.966447 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_26&gt;&lt;path d=&quot;M 100.930909 126.06289 
L 104.465455 126.06289 
L 104.465455 113.022651 
L 100.930909 113.022651 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_27&gt;&lt;path d=&quot;M 104.465455 126.06289 
L 108 126.06289 
L 108 115.473097 
L 104.465455 115.473097 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_28&gt;&lt;path d=&quot;M 108 126.06289 
L 111.534545 126.06289 
L 111.534545 125.270098 
L 108 125.270098 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_29&gt;&lt;path d=&quot;M 111.534545 126.06289 
L 115.069091 126.06289 
L 115.069091 125.933734 
L 111.534545 125.933734 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_30&gt;&lt;path d=&quot;M 115.069091 126.06289 
L 118.603636 126.06289 
L 118.603636 126.059063 
L 115.069091 126.059063 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_31&gt;&lt;path d=&quot;M 118.603636 126.06289 
L 122.138182 126.06289 
L 122.138182 126.062571 
L 118.603636 126.062571 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_32&gt;&lt;path d=&quot;M 122.138182 126.06289 
L 125.672727 126.06289 
L 125.672727 126.062571 
L 122.138182 126.062571 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_33&gt;&lt;path d=&quot;M 125.672727 126.06289 
L 129.207273 126.06289 
L 129.207273 126.062252 
L 125.672727 126.062252 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_34&gt;&lt;path d=&quot;M 129.207273 126.06289 
L 132.741818 126.06289 
L 132.741818 126.055236 
L 129.207273 126.055236 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_35&gt;&lt;path d=&quot;M 132.741818 126.06289 
L 136.276364 126.06289 
L 136.276364 126.062571 
L 132.741818 126.062571 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_36&gt;&lt;path d=&quot;M 136.276364 126.06289 
L 139.810909 126.06289 
L 139.810909 126.062252 
L 136.276364 126.062252 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_37&gt;&lt;path d=&quot;M 139.810909 126.06289 
L 143.345455 126.06289 
L 143.345455 126.06289 
L 139.810909 126.06289 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_38&gt;&lt;path d=&quot;M 143.345455 126.06289 
L 146.88 126.06289 
L 146.88 126.06289 
L 143.345455 126.06289 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_39&gt;&lt;path d=&quot;M 146.88 126.06289 
L 150.414545 126.06289 
L 150.414545 126.06289 
L 146.88 126.06289 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_40&gt;&lt;path d=&quot;M 150.414545 126.06289 
L 153.949091 126.06289 
L 153.949091 126.06289 
L 150.414545 126.06289 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_41&gt;&lt;path d=&quot;M 153.949091 126.06289 
L 157.483636 126.06289 
L 157.483636 126.06289 
L 153.949091 126.06289 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_42&gt;&lt;path d=&quot;M 157.483636 126.06289 
L 161.018182 126.06289 
L 161.018182 126.06289 
L 157.483636 126.06289 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_43&gt;&lt;path d=&quot;M 161.018182 126.06289 
L 164.552727 126.06289 
L 164.552727 126.06289 
L 161.018182 126.06289 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_44&gt;&lt;path d=&quot;M 164.552727 126.06289 
L 168.087273 126.06289 
L 168.087273 126.06289 
L 164.552727 126.06289 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_45&gt;&lt;path d=&quot;M 168.087273 126.06289 
L 171.621818 126.06289 
L 171.621818 126.06289 
L 168.087273 126.06289 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_46&gt;&lt;path d=&quot;M 171.621818 126.06289 
L 175.156364 126.06289 
L 175.156364 126.06289 
L 171.621818 126.06289 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_47&gt;&lt;path d=&quot;M 175.156364 126.06289 
L 178.690909 126.06289 
L 178.690909 126.06289 
L 175.156364 126.06289 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_48&gt;&lt;path d=&quot;M 178.690909 126.06289 
L 182.225455 126.06289 
L 182.225455 126.06289 
L 178.690909 126.06289 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_49&gt;&lt;path d=&quot;M 182.225455 126.06289 
L 185.76 126.06289 
L 185.76 126.06289 
L 182.225455 126.06289 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_50&gt;&lt;path d=&quot;M 185.76 126.06289 
L 189.294545 126.06289 
L 189.294545 126.06289 
L 185.76 126.06289 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_51&gt;&lt;path d=&quot;M 189.294545 126.06289 
L 192.829091 126.06289 
L 192.829091 126.06289 
L 189.294545 126.06289 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_52&gt;&lt;path d=&quot;M 192.829091 126.06289 
L 196.363636 126.06289 
L 196.363636 126.062252 
L 192.829091 126.062252 
z
&quot; clip-path=url(#ped6846cc4a) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_53&gt;&lt;path d=&quot;M 10.8 126.06289 
L 10.8 10.8 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;g id=patch_54&gt;&lt;path d=&quot;M 205.2 126.06289 
L 205.2 10.8 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;g id=patch_55&gt;&lt;path d=&quot;M 10.8 126.06289 
L 205.2 126.06289 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;g id=patch_56&gt;&lt;path d=&quot;M 10.8 10.8 
L 205.2 10.8 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;defs&gt;&lt;clippath id=ped6846cc4a&gt;&lt;rect x=10.8 y=10.8 width=194.4 height=115.26289 /&gt;&lt;/clippath&gt;&lt;/defs&gt;&lt;/svg&gt;&lt;/div&gt;&lt;div class=&quot;col-sm-12 text-right&quot;&gt;&lt;button class=&quot;btn btn-default btn-sm&quot; data-toggle=collapse data-target=&quot;#bottom-459491982266170039, #minifreqtable459491982266170039&quot; aria-expanded=true aria-controls=collapseExample&gt;Toggle details&lt;/button&gt;&lt;/div&gt;&lt;div id=bottom-459491982266170039 class=collapse&gt;&lt;div class=&quot;row spacing&quot;&gt;&lt;ul class=&quot;nav nav-tabs&quot; role=tablist&gt;&lt;li role=presentation class=active&gt;&lt;a href=#459491982266170039bottom-459491982266170039statistics aria-controls=459491982266170039bottom-459491982266170039statistics role=tab data-toggle=tab&gt;Statistics&lt;/a&gt;&lt;/li&gt;&lt;li role=presentation&gt;&lt;a href=#459491982266170039bottom-459491982266170039histogram aria-controls=459491982266170039bottom-459491982266170039histogram role=tab data-toggle=tab&gt;Histogram&lt;/a&gt;&lt;/li&gt;&lt;li role=presentation&gt;&lt;a href=#459491982266170039bottom-459491982266170039common_values aria-controls=459491982266170039bottom-459491982266170039common_values role=tab data-toggle=tab&gt;Common values&lt;/a&gt;&lt;/li&gt;&lt;li role=presentation&gt;&lt;a href=#459491982266170039bottom-459491982266170039extreme_values aria-controls=459491982266170039bottom-459491982266170039extreme_values role=tab data-toggle=tab&gt;Extreme values&lt;/a&gt;&lt;/li&gt;&lt;/ul&gt;&lt;div class=tab-content&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12 active&quot; id=459491982266170039bottom-459491982266170039statistics&gt;&lt;div class=col-sm-6&gt;&lt;p class=h4&gt;Quantile statistics&lt;/p&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;Minimum&lt;/th&gt;&lt;td&gt;-89.59463611&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;5-th percentile&lt;/th&gt;&lt;td&gt;-27.18219167&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Q1&lt;/th&gt;&lt;td&gt;-22.87916667&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;median&lt;/th&gt;&lt;td&gt;-19.96447778&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Q3&lt;/th&gt;&lt;td&gt;-17.89972222&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;95-th percentile&lt;/th&gt;&lt;td&gt;-3.827241667&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Maximum&lt;/th&gt;&lt;td&gt;89.79706389&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Range&lt;/th&gt;&lt;td&gt;179.3917&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Interquartile range (IQR)&lt;/th&gt;&lt;td&gt;4.979444444&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div class=col-sm-6&gt;&lt;p class=h4&gt;Descriptive statistics&lt;/p&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;Standard deviation&lt;/th&gt;&lt;td&gt;6.509864966&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Coefficient of variation (CV)&lt;/th&gt;&lt;td&gt;-0.3448675958&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Kurtosis&lt;/th&gt;&lt;td&gt;1.457242549&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Mean&lt;/th&gt;&lt;td&gt;-18.87641821&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Median Absolute Deviation (MAD)&lt;/th&gt;&lt;td&gt;2.838327778&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Skewness&lt;/th&gt;&lt;td&gt;1.058493343&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Sum&lt;/th&gt;&lt;td&gt;-16595372.96&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Variance&lt;/th&gt;&lt;td&gt;42.37834187&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Monotonicity&lt;/th&gt;&lt;td&gt;Not monotonic&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;/div&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12&quot; id=459491982266170039bottom-459491982266170039histogram&gt;&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot; standalone=&quot;no&quot;?&gt;&lt;!DOCTYPE svg class=&quot;img-responsive center-img&quot;PUBLIC &quot;-//W3C//DTD SVG 1.1//EN&quot;
  &quot;http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd&quot;&gt;&lt;svg class=&quot;img-responsive center-img&quot; xmlns:xlink=http://www.w3.org/1999/xlink width=432pt height=288pt viewbox=&quot;0 0 432 288&quot; xmlns=http://www.w3.org/2000/svg version=1.1&gt;&lt;metadata&gt;&lt;rdf:rdf xmlns:dc=http://purl.org/dc/elements/1.1/ xmlns:cc=http://creativecommons.org/ns# xmlns:rdf=http://www.w3.org/1999/02/22-rdf-syntax-ns#&gt;&lt;cc:work&gt;&lt;dc:type rdf:resource=http://purl.org/dc/dcmitype/StillImage /&gt;&lt;dc:date&gt;2022-07-12T13:06:41.191121&lt;/dc:date&gt;&lt;dc:format&gt;image/svg+xml&lt;/dc:format&gt;&lt;dc:creator&gt;&lt;cc:agent&gt;&lt;dc:title&gt;Matplotlib v3.5.2, https://matplotlib.org/&lt;/dc:title&gt;&lt;/cc:agent&gt;&lt;/dc:creator&gt;&lt;/cc:work&gt;&lt;/rdf:rdf&gt;&lt;/metadata&gt;&lt;defs&gt;&lt;style type=text/css&gt;*{stroke-linejoin: round; stroke-linecap: butt}&lt;/style&gt;&lt;/defs&gt;&lt;g id=figure_1&gt;&lt;g id=patch_1&gt;&lt;path d=&quot;M 0 288 
L 432 288 
L 432 0 
L 0 0 
z
&quot; style=&quot;fill: #ffffff&quot;/&gt;&lt;/g&gt;&lt;g id=axes_1&gt;&lt;g id=patch_2&gt;&lt;path d=&quot;M 68.86 248.562711 
L 421.2 248.562711 
L 421.2 10.8 
L 68.86 10.8 
z
&quot; style=&quot;fill: #ffffff&quot;/&gt;&lt;/g&gt;&lt;g id=matplotlib.axis_1&gt;&lt;g id=xtick_1&gt;&lt;g id=text_1&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(106.765433 276.118348)rotate(-45)scale(0.1 -0.1)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-2212 transform=scale(0.015625) d=&quot;M 3381 1997 
L 356 1997 
L 356 2522 
L 3381 2522 
L 3381 1997 
z
&quot;/&gt;&lt;path id=ArialMT-37 transform=scale(0.015625) d=&quot;M 303 3981 
L 303 4522 
L 3269 4522 
L 3269 4084 
Q 2831 3619 2401 2847 
Q 1972 2075 1738 1259 
Q 1569 684 1522 0 
L 944 0 
Q 953 541 1156 1306 
Q 1359 2072 1739 2783 
Q 2119 3494 2547 3981 
L 303 3981 
z
&quot;/&gt;&lt;path id=ArialMT-35 transform=scale(0.015625) d=&quot;M 266 1200 
L 856 1250 
Q 922 819 1161 601 
Q 1400 384 1738 384 
Q 2144 384 2425 690 
Q 2706 997 2706 1503 
Q 2706 1984 2436 2262 
Q 2166 2541 1728 2541 
Q 1456 2541 1237 2417 
Q 1019 2294 894 2097 
L 366 2166 
L 809 4519 
L 3088 4519 
L 3088 3981 
L 1259 3981 
L 1013 2750 
Q 1425 3038 1878 3038 
Q 2478 3038 2890 2622 
Q 3303 2206 3303 1553 
Q 3303 931 2941 478 
Q 2500 -78 1738 -78 
Q 1113 -78 717 272 
Q 322 622 266 1200 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-2212 /&gt;&lt;use xlink:href=#ArialMT-37 x=58.398438 /&gt;&lt;use xlink:href=#ArialMT-35 x=114.013672 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_2&gt;&lt;g id=text_2&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(151.40366 276.118348)rotate(-45)scale(0.1 -0.1)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-30 transform=scale(0.015625) d=&quot;M 266 2259 
Q 266 3072 433 3567 
Q 600 4063 929 4331 
Q 1259 4600 1759 4600 
Q 2128 4600 2406 4451 
Q 2684 4303 2865 4023 
Q 3047 3744 3150 3342 
Q 3253 2941 3253 2259 
Q 3253 1453 3087 958 
Q 2922 463 2592 192 
Q 2263 -78 1759 -78 
Q 1097 -78 719 397 
Q 266 969 266 2259 
z
M 844 2259 
Q 844 1131 1108 757 
Q 1372 384 1759 384 
Q 2147 384 2411 759 
Q 2675 1134 2675 2259 
Q 2675 3391 2411 3762 
Q 2147 4134 1753 4134 
Q 1366 4134 1134 3806 
Q 844 3388 844 2259 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-2212 /&gt;&lt;use xlink:href=#ArialMT-35 x=58.398438 /&gt;&lt;use xlink:href=#ArialMT-30 x=114.013672 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_3&gt;&lt;g id=text_3&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(196.041886 276.118348)rotate(-45)scale(0.1 -0.1)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-32 transform=scale(0.015625) d=&quot;M 3222 541 
L 3222 0 
L 194 0 
Q 188 203 259 391 
Q 375 700 629 1000 
Q 884 1300 1366 1694 
Q 2113 2306 2375 2664 
Q 2638 3022 2638 3341 
Q 2638 3675 2398 3904 
Q 2159 4134 1775 4134 
Q 1369 4134 1125 3890 
Q 881 3647 878 3216 
L 300 3275 
Q 359 3922 746 4261 
Q 1134 4600 1788 4600 
Q 2447 4600 2831 4234 
Q 3216 3869 3216 3328 
Q 3216 3053 3103 2787 
Q 2991 2522 2730 2228 
Q 2469 1934 1863 1422 
Q 1356 997 1212 845 
Q 1069 694 975 541 
L 3222 541 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-2212 /&gt;&lt;use xlink:href=#ArialMT-32 x=58.398438 /&gt;&lt;use xlink:href=#ArialMT-35 x=114.013672 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_4&gt;&lt;g id=text_4&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(244.711173 268.056225)rotate(-45)scale(0.1 -0.1)&quot;&gt;&lt;use xlink:href=#ArialMT-30 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_5&gt;&lt;g id=text_5&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(287.383311 271.988402)rotate(-45)scale(0.1 -0.1)&quot;&gt;&lt;use xlink:href=#ArialMT-32 /&gt;&lt;use xlink:href=#ArialMT-35 x=55.615234 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_6&gt;&lt;g id=text_6&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(332.021537 271.988402)rotate(-45)scale(0.1 -0.1)&quot;&gt;&lt;use xlink:href=#ArialMT-35 /&gt;&lt;use xlink:href=#ArialMT-30 x=55.615234 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_7&gt;&lt;g id=text_7&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(376.659763 271.988402)rotate(-45)scale(0.1 -0.1)&quot;&gt;&lt;use xlink:href=#ArialMT-37 /&gt;&lt;use xlink:href=#ArialMT-35 x=55.615234 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=matplotlib.axis_2&gt;&lt;g id=ytick_1&gt;&lt;g id=text_8&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(52.799062 252.141617)scale(0.1 -0.1)&quot;&gt;&lt;use xlink:href=#ArialMT-30 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_2&gt;&lt;g id=text_9&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(30.555312 219.250241)scale(0.1 -0.1)&quot;&gt;&lt;use xlink:href=#ArialMT-35 /&gt;&lt;use xlink:href=#ArialMT-30 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-30 x=222.460938 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_3&gt;&lt;g id=text_10&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(24.994375 186.358866)scale(0.1 -0.1)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-31 transform=scale(0.015625) d=&quot;M 2384 0 
L 1822 0 
L 1822 3584 
Q 1619 3391 1289 3197 
Q 959 3003 697 2906 
L 697 3450 
Q 1169 3672 1522 3987 
Q 1875 4303 2022 4600 
L 2384 4600 
L 2384 0 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-31 /&gt;&lt;use xlink:href=#ArialMT-30 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-30 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-30 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_4&gt;&lt;g id=text_11&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(24.994375 153.46749)scale(0.1 -0.1)&quot;&gt;&lt;use xlink:href=#ArialMT-31 /&gt;&lt;use xlink:href=#ArialMT-35 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-30 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-30 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_5&gt;&lt;g id=text_12&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(24.994375 120.576114)scale(0.1 -0.1)&quot;&gt;&lt;use xlink:href=#ArialMT-32 /&gt;&lt;use xlink:href=#ArialMT-30 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-30 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-30 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_6&gt;&lt;g id=text_13&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(24.994375 87.684738)scale(0.1 -0.1)&quot;&gt;&lt;use xlink:href=#ArialMT-32 /&gt;&lt;use xlink:href=#ArialMT-35 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-30 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-30 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_7&gt;&lt;g id=text_14&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(24.994375 54.793362)scale(0.1 -0.1)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-33 transform=scale(0.015625) d=&quot;M 269 1209 
L 831 1284 
Q 928 806 1161 595 
Q 1394 384 1728 384 
Q 2125 384 2398 659 
Q 2672 934 2672 1341 
Q 2672 1728 2419 1979 
Q 2166 2231 1775 2231 
Q 1616 2231 1378 2169 
L 1441 2663 
Q 1497 2656 1531 2656 
Q 1891 2656 2178 2843 
Q 2466 3031 2466 3422 
Q 2466 3731 2256 3934 
Q 2047 4138 1716 4138 
Q 1388 4138 1169 3931 
Q 950 3725 888 3313 
L 325 3413 
Q 428 3978 793 4289 
Q 1159 4600 1703 4600 
Q 2078 4600 2393 4439 
Q 2709 4278 2876 4000 
Q 3044 3722 3044 3409 
Q 3044 3113 2884 2869 
Q 2725 2625 2413 2481 
Q 2819 2388 3044 2092 
Q 3269 1797 3269 1353 
Q 3269 753 2831 336 
Q 2394 -81 1725 -81 
Q 1122 -81 723 278 
Q 325 638 269 1209 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-33 /&gt;&lt;use xlink:href=#ArialMT-30 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-30 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-30 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_8&gt;&lt;g id=text_15&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(24.994375 21.901986)scale(0.1 -0.1)&quot;&gt;&lt;use xlink:href=#ArialMT-33 /&gt;&lt;use xlink:href=#ArialMT-35 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-30 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-30 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=text_16&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(18.679219 155.664559)rotate(-90)scale(0.11 -0.11)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-46 transform=scale(0.015625) d=&quot;M 525 0 
L 525 4581 
L 3616 4581 
L 3616 4041 
L 1131 4041 
L 1131 2622 
L 3281 2622 
L 3281 2081 
L 1131 2081 
L 1131 0 
L 525 0 
z
&quot;/&gt;&lt;path id=ArialMT-72 transform=scale(0.015625) d=&quot;M 416 0 
L 416 3319 
L 922 3319 
L 922 2816 
Q 1116 3169 1280 3281 
Q 1444 3394 1641 3394 
Q 1925 3394 2219 3213 
L 2025 2691 
Q 1819 2813 1613 2813 
Q 1428 2813 1281 2702 
Q 1134 2591 1072 2394 
Q 978 2094 978 1738 
L 978 0 
L 416 0 
z
&quot;/&gt;&lt;path id=ArialMT-65 transform=scale(0.015625) d=&quot;M 2694 1069 
L 3275 997 
Q 3138 488 2766 206 
Q 2394 -75 1816 -75 
Q 1088 -75 661 373 
Q 234 822 234 1631 
Q 234 2469 665 2931 
Q 1097 3394 1784 3394 
Q 2450 3394 2872 2941 
Q 3294 2488 3294 1666 
Q 3294 1616 3291 1516 
L 816 1516 
Q 847 969 1125 678 
Q 1403 388 1819 388 
Q 2128 388 2347 550 
Q 2566 713 2694 1069 
z
M 847 1978 
L 2700 1978 
Q 2663 2397 2488 2606 
Q 2219 2931 1791 2931 
Q 1403 2931 1139 2672 
Q 875 2413 847 1978 
z
&quot;/&gt;&lt;path id=ArialMT-71 transform=scale(0.015625) d=&quot;M 2538 -1272 
L 2538 353 
Q 2406 169 2170 47 
Q 1934 -75 1669 -75 
Q 1078 -75 651 397 
Q 225 869 225 1691 
Q 225 2191 398 2587 
Q 572 2984 901 3189 
Q 1231 3394 1625 3394 
Q 2241 3394 2594 2875 
L 2594 3319 
L 3100 3319 
L 3100 -1272 
L 2538 -1272 
z
M 803 1669 
Q 803 1028 1072 708 
Q 1341 388 1716 388 
Q 2075 388 2334 692 
Q 2594 997 2594 1619 
Q 2594 2281 2320 2615 
Q 2047 2950 1678 2950 
Q 1313 2950 1058 2639 
Q 803 2328 803 1669 
z
&quot;/&gt;&lt;path id=ArialMT-75 transform=scale(0.015625) d=&quot;M 2597 0 
L 2597 488 
Q 2209 -75 1544 -75 
Q 1250 -75 995 37 
Q 741 150 617 320 
Q 494 491 444 738 
Q 409 903 409 1263 
L 409 3319 
L 972 3319 
L 972 1478 
Q 972 1038 1006 884 
Q 1059 663 1231 536 
Q 1403 409 1656 409 
Q 1909 409 2131 539 
Q 2353 669 2445 892 
Q 2538 1116 2538 1541 
L 2538 3319 
L 3100 3319 
L 3100 0 
L 2597 0 
z
&quot;/&gt;&lt;path id=ArialMT-6e transform=scale(0.015625) d=&quot;M 422 0 
L 422 3319 
L 928 3319 
L 928 2847 
Q 1294 3394 1984 3394 
Q 2284 3394 2536 3286 
Q 2788 3178 2913 3003 
Q 3038 2828 3088 2588 
Q 3119 2431 3119 2041 
L 3119 0 
L 2556 0 
L 2556 2019 
Q 2556 2363 2490 2533 
Q 2425 2703 2258 2804 
Q 2091 2906 1866 2906 
Q 1506 2906 1245 2678 
Q 984 2450 984 1813 
L 984 0 
L 422 0 
z
&quot;/&gt;&lt;path id=ArialMT-63 transform=scale(0.015625) d=&quot;M 2588 1216 
L 3141 1144 
Q 3050 572 2676 248 
Q 2303 -75 1759 -75 
Q 1078 -75 664 370 
Q 250 816 250 1647 
Q 250 2184 428 2587 
Q 606 2991 970 3192 
Q 1334 3394 1763 3394 
Q 2303 3394 2647 3120 
Q 2991 2847 3088 2344 
L 2541 2259 
Q 2463 2594 2264 2762 
Q 2066 2931 1784 2931 
Q 1359 2931 1093 2626 
Q 828 2322 828 1663 
Q 828 994 1084 691 
Q 1341 388 1753 388 
Q 2084 388 2306 591 
Q 2528 794 2588 1216 
z
&quot;/&gt;&lt;path id=ArialMT-79 transform=scale(0.015625) d=&quot;M 397 -1278 
L 334 -750 
Q 519 -800 656 -800 
Q 844 -800 956 -737 
Q 1069 -675 1141 -563 
Q 1194 -478 1313 -144 
Q 1328 -97 1363 -6 
L 103 3319 
L 709 3319 
L 1400 1397 
Q 1534 1031 1641 628 
Q 1738 1016 1872 1384 
L 2581 3319 
L 3144 3319 
L 1881 -56 
Q 1678 -603 1566 -809 
Q 1416 -1088 1222 -1217 
Q 1028 -1347 759 -1347 
Q 597 -1347 397 -1278 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-46 /&gt;&lt;use xlink:href=#ArialMT-72 x=61.083984 /&gt;&lt;use xlink:href=#ArialMT-65 x=94.384766 /&gt;&lt;use xlink:href=#ArialMT-71 x=150 /&gt;&lt;use xlink:href=#ArialMT-75 x=205.615234 /&gt;&lt;use xlink:href=#ArialMT-65 x=261.230469 /&gt;&lt;use xlink:href=#ArialMT-6e x=316.845703 /&gt;&lt;use xlink:href=#ArialMT-63 x=372.460938 /&gt;&lt;use xlink:href=#ArialMT-79 x=422.460938 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=patch_3&gt;&lt;path d=&quot;M 84.875455 248.562711 
L 91.281636 248.562711 
L 91.281636 248.56008 
L 84.875455 248.56008 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_4&gt;&lt;path d=&quot;M 91.281636 248.562711 
L 97.687818 248.562711 
L 97.687818 248.562711 
L 91.281636 248.562711 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_5&gt;&lt;path d=&quot;M 97.687818 248.562711 
L 104.094 248.562711 
L 104.094 248.562711 
L 97.687818 248.562711 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_6&gt;&lt;path d=&quot;M 104.094 248.562711 
L 110.500182 248.562711 
L 110.500182 248.562711 
L 104.094 248.562711 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_7&gt;&lt;path d=&quot;M 110.500182 248.562711 
L 116.906364 248.562711 
L 116.906364 248.561395 
L 110.500182 248.561395 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_8&gt;&lt;path d=&quot;M 116.906364 248.562711 
L 123.312545 248.562711 
L 123.312545 248.562711 
L 116.906364 248.562711 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_9&gt;&lt;path d=&quot;M 123.312545 248.562711 
L 129.718727 248.562711 
L 129.718727 248.562711 
L 123.312545 248.562711 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_10&gt;&lt;path d=&quot;M 129.718727 248.562711 
L 136.124909 248.562711 
L 136.124909 248.562711 
L 129.718727 248.562711 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_11&gt;&lt;path d=&quot;M 136.124909 248.562711 
L 142.531091 248.562711 
L 142.531091 248.562711 
L 136.124909 248.562711 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_12&gt;&lt;path d=&quot;M 142.531091 248.562711 
L 148.937273 248.562711 
L 148.937273 248.560738 
L 142.531091 248.560738 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_13&gt;&lt;path d=&quot;M 148.937273 248.562711 
L 155.343455 248.562711 
L 155.343455 248.552186 
L 148.937273 248.552186 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_14&gt;&lt;path d=&quot;M 155.343455 248.562711 
L 161.749636 248.562711 
L 161.749636 248.130518 
L 155.343455 248.130518 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_15&gt;&lt;path d=&quot;M 161.749636 248.562711 
L 168.155818 248.562711 
L 168.155818 248.543634 
L 161.749636 248.543634 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_16&gt;&lt;path d=&quot;M 168.155818 248.562711 
L 174.562 248.562711 
L 174.562 248.561395 
L 168.155818 248.561395 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_17&gt;&lt;path d=&quot;M 174.562 248.562711 
L 180.968182 248.562711 
L 180.968182 248.557448 
L 174.562 248.557448 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_18&gt;&lt;path d=&quot;M 180.968182 248.562711 
L 187.374364 248.562711 
L 187.374364 248.314052 
L 180.968182 248.314052 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_19&gt;&lt;path d=&quot;M 187.374364 248.562711 
L 193.780545 248.562711 
L 193.780545 229.096279 
L 187.374364 229.096279 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_20&gt;&lt;path d=&quot;M 193.780545 248.562711 
L 200.186727 248.562711 
L 200.186727 216.842268 
L 193.780545 216.842268 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_21&gt;&lt;path d=&quot;M 200.186727 248.562711 
L 206.592909 248.562711 
L 206.592909 92.692454 
L 200.186727 92.692454 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_22&gt;&lt;path d=&quot;M 206.592909 248.562711 
L 212.999091 248.562711 
L 212.999091 22.122034 
L 206.592909 22.122034 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_23&gt;&lt;path d=&quot;M 212.999091 248.562711 
L 219.405273 248.562711 
L 219.405273 214.445145 
L 212.999091 214.445145 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_24&gt;&lt;path d=&quot;M 219.405273 248.562711 
L 225.811455 248.562711 
L 225.811455 218.319091 
L 219.405273 218.319091 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_25&gt;&lt;path d=&quot;M 225.811455 248.562711 
L 232.217636 248.562711 
L 232.217636 219.484761 
L 225.811455 219.484761 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_26&gt;&lt;path d=&quot;M 232.217636 248.562711 
L 238.623818 248.562711 
L 238.623818 221.663486 
L 232.217636 221.663486 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_27&gt;&lt;path d=&quot;M 238.623818 248.562711 
L 245.03 248.562711 
L 245.03 226.718233 
L 238.623818 226.718233 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_28&gt;&lt;path d=&quot;M 245.03 248.562711 
L 251.436182 248.562711 
L 251.436182 246.927352 
L 245.03 246.927352 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_29&gt;&lt;path d=&quot;M 251.436182 248.562711 
L 257.842364 248.562711 
L 257.842364 248.296291 
L 251.436182 248.296291 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_30&gt;&lt;path d=&quot;M 257.842364 248.562711 
L 264.248545 248.562711 
L 264.248545 248.554817 
L 257.842364 248.554817 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_31&gt;&lt;path d=&quot;M 264.248545 248.562711 
L 270.654727 248.562711 
L 270.654727 248.562053 
L 264.248545 248.562053 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_32&gt;&lt;path d=&quot;M 270.654727 248.562711 
L 277.060909 248.562711 
L 277.060909 248.562053 
L 270.654727 248.562053 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_33&gt;&lt;path d=&quot;M 277.060909 248.562711 
L 283.467091 248.562711 
L 283.467091 248.561395 
L 277.060909 248.561395 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_34&gt;&lt;path d=&quot;M 283.467091 248.562711 
L 289.873273 248.562711 
L 289.873273 248.546923 
L 283.467091 248.546923 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_35&gt;&lt;path d=&quot;M 289.873273 248.562711 
L 296.279455 248.562711 
L 296.279455 248.562053 
L 289.873273 248.562053 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_36&gt;&lt;path d=&quot;M 296.279455 248.562711 
L 302.685636 248.562711 
L 302.685636 248.561395 
L 296.279455 248.561395 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_37&gt;&lt;path d=&quot;M 302.685636 248.562711 
L 309.091818 248.562711 
L 309.091818 248.562711 
L 302.685636 248.562711 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_38&gt;&lt;path d=&quot;M 309.091818 248.562711 
L 315.498 248.562711 
L 315.498 248.562711 
L 309.091818 248.562711 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_39&gt;&lt;path d=&quot;M 315.498 248.562711 
L 321.904182 248.562711 
L 321.904182 248.562711 
L 315.498 248.562711 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_40&gt;&lt;path d=&quot;M 321.904182 248.562711 
L 328.310364 248.562711 
L 328.310364 248.562711 
L 321.904182 248.562711 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_41&gt;&lt;path d=&quot;M 328.310364 248.562711 
L 334.716545 248.562711 
L 334.716545 248.562711 
L 328.310364 248.562711 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_42&gt;&lt;path d=&quot;M 334.716545 248.562711 
L 341.122727 248.562711 
L 341.122727 248.562711 
L 334.716545 248.562711 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_43&gt;&lt;path d=&quot;M 341.122727 248.562711 
L 347.528909 248.562711 
L 347.528909 248.562711 
L 341.122727 248.562711 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_44&gt;&lt;path d=&quot;M 347.528909 248.562711 
L 353.935091 248.562711 
L 353.935091 248.562711 
L 347.528909 248.562711 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_45&gt;&lt;path d=&quot;M 353.935091 248.562711 
L 360.341273 248.562711 
L 360.341273 248.562711 
L 353.935091 248.562711 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_46&gt;&lt;path d=&quot;M 360.341273 248.562711 
L 366.747455 248.562711 
L 366.747455 248.562711 
L 360.341273 248.562711 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_47&gt;&lt;path d=&quot;M 366.747455 248.562711 
L 373.153636 248.562711 
L 373.153636 248.562711 
L 366.747455 248.562711 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_48&gt;&lt;path d=&quot;M 373.153636 248.562711 
L 379.559818 248.562711 
L 379.559818 248.562711 
L 373.153636 248.562711 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_49&gt;&lt;path d=&quot;M 379.559818 248.562711 
L 385.966 248.562711 
L 385.966 248.562711 
L 379.559818 248.562711 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_50&gt;&lt;path d=&quot;M 385.966 248.562711 
L 392.372182 248.562711 
L 392.372182 248.562711 
L 385.966 248.562711 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_51&gt;&lt;path d=&quot;M 392.372182 248.562711 
L 398.778364 248.562711 
L 398.778364 248.562711 
L 392.372182 248.562711 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_52&gt;&lt;path d=&quot;M 398.778364 248.562711 
L 405.184545 248.562711 
L 405.184545 248.561395 
L 398.778364 248.561395 
z
&quot; clip-path=url(#pac80918fc5) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_53&gt;&lt;path d=&quot;M 68.86 248.562711 
L 68.86 10.8 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;g id=patch_54&gt;&lt;path d=&quot;M 421.2 248.562711 
L 421.2 10.8 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;g id=patch_55&gt;&lt;path d=&quot;M 68.86 248.562711 
L 421.2 248.562711 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;g id=patch_56&gt;&lt;path d=&quot;M 68.86 10.8 
L 421.2 10.8 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;defs&gt;&lt;clippath id=pac80918fc5&gt;&lt;rect x=68.86 y=10.8 width=352.34 height=237.762711 /&gt;&lt;/clippath&gt;&lt;/defs&gt;&lt;/svg&gt;&lt;div class=&quot;caption text-center text-muted&quot;&gt;&lt;strong&gt;Histogram with fixed size bins&lt;/strong&gt; (bins=50) &lt;/div&gt;&lt;/div&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12&quot; id=459491982266170039bottom-459491982266170039common_values&gt;&lt;table class=&quot;freq table table-hover table-striped&quot;&gt;&lt;thead&gt;&lt;tr&gt;&lt;td&gt;Value&lt;/td&gt;&lt;td&gt;Count&lt;/td&gt;&lt;td&gt;Frequency (%)&lt;/td&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr class&gt;&lt;td title=-19.93271111&gt;-19.93271111&lt;/td&gt;&lt;td&gt;4300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.5% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.93737222&gt;-19.93737222&lt;/td&gt;&lt;td&gt;2880&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.4%&gt; &amp;nbsp; &lt;/div&gt; 0.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.923625&gt;-19.923625&lt;/td&gt;&lt;td&gt;2880&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.4%&gt; &amp;nbsp; &lt;/div&gt; 0.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-20.05804444&gt;-20.05804444&lt;/td&gt;&lt;td&gt;2880&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.4%&gt; &amp;nbsp; &lt;/div&gt; 0.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.62903611&gt;-19.62903611&lt;/td&gt;&lt;td&gt;2880&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.4%&gt; &amp;nbsp; &lt;/div&gt; 0.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.79635278&gt;-19.79635278&lt;/td&gt;&lt;td&gt;2880&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.4%&gt; &amp;nbsp; &lt;/div&gt; 0.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.89859444&gt;-19.89859444&lt;/td&gt;&lt;td&gt;2880&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.4%&gt; &amp;nbsp; &lt;/div&gt; 0.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.95365278&gt;-19.95365278&lt;/td&gt;&lt;td&gt;2845&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.4%&gt; &amp;nbsp; &lt;/div&gt; 0.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.82184722&gt;-19.82184722&lt;/td&gt;&lt;td&gt;2775&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.4%&gt; &amp;nbsp; &lt;/div&gt; 0.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.90108611&gt;-19.90108611&lt;/td&gt;&lt;td&gt;2635&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.4%&gt; &amp;nbsp; &lt;/div&gt; 0.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.81412778&gt;-19.81412778&lt;/td&gt;&lt;td&gt;2600&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.4%&gt; &amp;nbsp; &lt;/div&gt; 0.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.93536667&gt;-19.93536667&lt;/td&gt;&lt;td&gt;2520&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.91590833&gt;-19.91590833&lt;/td&gt;&lt;td&gt;2160&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.92118889&gt;-19.92118889&lt;/td&gt;&lt;td&gt;1800&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.85771389&gt;-19.85771389&lt;/td&gt;&lt;td&gt;1490&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.92530556&gt;-19.92530556&lt;/td&gt;&lt;td&gt;1459&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.56222222&gt;-19.56222222&lt;/td&gt;&lt;td&gt;1445&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.97472222&gt;-19.97472222&lt;/td&gt;&lt;td&gt;1443&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.99028889&gt;-19.99028889&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.16979167&gt;-19.16979167&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-18.81025&gt;-18.81025&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.88120833&gt;-19.88120833&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-20.00695&gt;-20.00695&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.84460278&gt;-19.84460278&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.86704444&gt;-19.86704444&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.88540556&gt;-19.88540556&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.69089444&gt;-19.69089444&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.98641389&gt;-19.98641389&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.982425&gt;-19.982425&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.66623889&gt;-19.66623889&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.96272778&gt;-19.96272778&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.78800556&gt;-19.78800556&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.72388889&gt;-19.72388889&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.75702778&gt;-19.75702778&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.77558056&gt;-19.77558056&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.77011111&gt;-19.77011111&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.76018333&gt;-19.76018333&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.94885&gt;-19.94885&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.62690833&gt;-19.62690833&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.76414722&gt;-19.76414722&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-20.34209167&gt;-20.34209167&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-20.48637778&gt;-20.48637778&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-20.38252222&gt;-20.38252222&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-20.37296389&gt;-20.37296389&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.33615833&gt;-19.33615833&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.60436111&gt;-19.60436111&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-20.34821944&gt;-20.34821944&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.92395&gt;-19.92395&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.48136111&gt;-19.48136111&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-20.31325278&gt;-20.31325278&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.91814722&gt;-19.91814722&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-20.28790278&gt;-20.28790278&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-20.5357&gt;-20.5357&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.9224&gt;-19.9224&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-20.255425&gt;-20.255425&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.51805278&gt;-19.51805278&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.29285278&gt;-19.29285278&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.89125833&gt;-19.89125833&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-20.18305278&gt;-20.18305278&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-20.08834722&gt;-20.08834722&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.54919444&gt;-19.54919444&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.99896111&gt;-19.99896111&lt;/td&gt;&lt;td&gt;1435&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.43874722&gt;-19.43874722&lt;/td&gt;&lt;td&gt;1410&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.96447778&gt;-19.96447778&lt;/td&gt;&lt;td&gt;1405&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.943025&gt;-19.943025&lt;/td&gt;&lt;td&gt;1405&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.91441111&gt;-19.91441111&lt;/td&gt;&lt;td&gt;1405&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.94921667&gt;-19.94921667&lt;/td&gt;&lt;td&gt;1405&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.87666667&gt;-19.87666667&lt;/td&gt;&lt;td&gt;1372&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.82996667&gt;-19.82996667&lt;/td&gt;&lt;td&gt;1370&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.82961667&gt;-19.82961667&lt;/td&gt;&lt;td&gt;1335&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.81622222&gt;-19.81622222&lt;/td&gt;&lt;td&gt;1332&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-20.37527778&gt;-20.37527778&lt;/td&gt;&lt;td&gt;1306&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.91417222&gt;-19.91417222&lt;/td&gt;&lt;td&gt;1301&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.90810833&gt;-19.90810833&lt;/td&gt;&lt;td&gt;1301&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.92963889&gt;-19.92963889&lt;/td&gt;&lt;td&gt;1301&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.89783333&gt;-19.89783333&lt;/td&gt;&lt;td&gt;1301&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.94485556&gt;-19.94485556&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-18.86725&gt;-18.86725&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.93599722&gt;-19.93599722&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.93522778&gt;-19.93522778&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.93018056&gt;-19.93018056&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.99397778&gt;-19.99397778&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.94914722&gt;-19.94914722&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.95208333&gt;-19.95208333&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.93305833&gt;-19.93305833&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-20.46858611&gt;-20.46858611&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-20.39297222&gt;-20.39297222&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-20.38729167&gt;-20.38729167&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-20.32560833&gt;-20.32560833&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-20.19188333&gt;-20.19188333&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-20.0739&gt;-20.0739&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-20.07158056&gt;-20.07158056&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-20.050325&gt;-20.050325&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-20.04444722&gt;-20.04444722&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-20.03358889&gt;-20.03358889&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-20.02588611&gt;-20.02588611&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-20.00708611&gt;-20.00708611&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-20.00064444&gt;-20.00064444&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.98416667&gt;-19.98416667&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-19.98049167&gt;-19.98049167&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class=other&gt;&lt;td title=&quot;Other values (153157)&quot;&gt;Other values (153157)&lt;/td&gt;&lt;td&gt;720903&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt; 82.0% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12&quot; id=459491982266170039bottom-459491982266170039extreme_values&gt;&lt;div class=&quot;row spacing&quot;&gt;&lt;ul class=&quot;nav nav-tabs&quot; role=tablist&gt;&lt;li role=presentation class=active&gt;&lt;a href=#459491982266170039extreme_values-459491982266170039firstn aria-controls=459491982266170039extreme_values-459491982266170039firstn role=tab data-toggle=tab&gt;Minimum 10 values&lt;/a&gt;&lt;/li&gt;&lt;li role=presentation&gt;&lt;a href=#459491982266170039extreme_values-459491982266170039lastn aria-controls=459491982266170039extreme_values-459491982266170039lastn role=tab data-toggle=tab&gt;Maximum 10 values&lt;/a&gt;&lt;/li&gt;&lt;/ul&gt;&lt;div class=tab-content&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12 active&quot; id=459491982266170039extreme_values-459491982266170039firstn&gt;&lt;table class=&quot;freq table table-hover table-striped&quot;&gt;&lt;thead&gt;&lt;tr&gt;&lt;td&gt;Value&lt;/td&gt;&lt;td&gt;Count&lt;/td&gt;&lt;td&gt;Frequency (%)&lt;/td&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr class&gt;&lt;td title=-89.59463611&gt;-89.59463611&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:50.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-89.50650833&gt;-89.50650833&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:50.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-89.36204722&gt;-89.36204722&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:50.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-89.33016667&gt;-89.33016667&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:50.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-74.82058333&gt;-74.82058333&lt;/td&gt;&lt;td&gt;2&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-55.60524722&gt;-55.60524722&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:50.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-54.79124444&gt;-54.79124444&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:50.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-54.38005&gt;-54.38005&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:50.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-53.57383333&gt;-53.57383333&lt;/td&gt;&lt;td&gt;2&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-53.51190556&gt;-53.51190556&lt;/td&gt;&lt;td&gt;2&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12&quot; id=459491982266170039extreme_values-459491982266170039lastn&gt;&lt;table class=&quot;freq table table-hover table-striped&quot;&gt;&lt;thead&gt;&lt;tr&gt;&lt;td&gt;Value&lt;/td&gt;&lt;td&gt;Count&lt;/td&gt;&lt;td&gt;Frequency (%)&lt;/td&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr class&gt;&lt;td title=89.79706389&gt;89.79706389&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:9.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=89.70635833&gt;89.70635833&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:9.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=29.92293611&gt;29.92293611&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:9.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=29.76787222&gt;29.76787222&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:9.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=26.17722&gt;26.17722&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:9.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=23.93111038&gt;23.93111038&lt;/td&gt;&lt;td&gt;9&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:81.8%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=23.62566389&gt;23.62566389&lt;/td&gt;&lt;td&gt;3&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:27.3%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=23.60305595&gt;23.60305595&lt;/td&gt;&lt;td&gt;11&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=22.69222222&gt;22.69222222&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:9.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=19.73472222&gt;19.73472222&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:9.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;div class=&quot;row spacing&quot;&gt;&lt;a class=&quot;anchor-pos anchor-pos-variable&quot; id=pp_var_1019400858767329170&gt;&lt;/a&gt;&lt;div class=variable&gt;&lt;div class=col-sm-3&gt;&lt;p class=h4 title=Longitude&gt;&lt;a href=#pp_var_1019400858767329170&gt;Longitude&lt;/a&gt;&lt;br&gt;&lt;small&gt;Real number (&amp;Ropf;)&lt;/small&gt;&lt;/p&gt;&lt;p class=variable-description&gt;&lt;/p&gt;&lt;/div&gt;&lt;div class=col-sm-3&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;Distinct&lt;/th&gt;&lt;td&gt;153179&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Distinct (%)&lt;/th&gt;&lt;td&gt;17.4%&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Missing&lt;/th&gt;&lt;td&gt;0&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Missing (%)&lt;/th&gt;&lt;td&gt;0.0%&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Infinite&lt;/th&gt;&lt;td&gt;0&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Infinite (%)&lt;/th&gt;&lt;td&gt;0.0%&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Mean&lt;/th&gt;&lt;td&gt;-45.94317823&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div class=col-sm-3&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;Minimum&lt;/th&gt;&lt;td&gt;-79.83388889&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Maximum&lt;/th&gt;&lt;td&gt;69.93499756&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Zeros&lt;/th&gt;&lt;td&gt;16&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Zeros (%)&lt;/th&gt;&lt;td&gt;&lt; 0.1%&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Negative&lt;/th&gt;&lt;td&gt;879140&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Negative (%)&lt;/th&gt;&lt;td&gt;&gt; 99.9%&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Memory size&lt;/th&gt;&lt;td&gt;6.7 MiB&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div class=col-sm-3&gt;&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot; standalone=&quot;no&quot;?&gt;&lt;!DOCTYPE svg class=&quot;img-responsive center-img&quot;PUBLIC &quot;-//W3C//DTD SVG 1.1//EN&quot;
  &quot;http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd&quot;&gt;&lt;svg class=&quot;img-responsive center-img&quot; xmlns:xlink=http://www.w3.org/1999/xlink width=216pt height=162pt viewbox=&quot;0 0 216 162&quot; xmlns=http://www.w3.org/2000/svg version=1.1&gt;&lt;metadata&gt;&lt;rdf:rdf xmlns:dc=http://purl.org/dc/elements/1.1/ xmlns:cc=http://creativecommons.org/ns# xmlns:rdf=http://www.w3.org/1999/02/22-rdf-syntax-ns#&gt;&lt;cc:work&gt;&lt;dc:type rdf:resource=http://purl.org/dc/dcmitype/StillImage /&gt;&lt;dc:date&gt;2022-07-12T13:06:41.368615&lt;/dc:date&gt;&lt;dc:format&gt;image/svg+xml&lt;/dc:format&gt;&lt;dc:creator&gt;&lt;cc:agent&gt;&lt;dc:title&gt;Matplotlib v3.5.2, https://matplotlib.org/&lt;/dc:title&gt;&lt;/cc:agent&gt;&lt;/dc:creator&gt;&lt;/cc:work&gt;&lt;/rdf:rdf&gt;&lt;/metadata&gt;&lt;defs&gt;&lt;style type=text/css&gt;*{stroke-linejoin: round; stroke-linecap: butt}&lt;/style&gt;&lt;/defs&gt;&lt;g id=figure_1&gt;&lt;g id=patch_1&gt;&lt;path d=&quot;M 0 162 
L 216 162 
L 216 0 
L 0 0 
z
&quot; style=&quot;fill: #ffffff&quot;/&gt;&lt;/g&gt;&lt;g id=axes_1&gt;&lt;g id=patch_2&gt;&lt;path d=&quot;M 10.8 126.06289 
L 205.2 126.06289 
L 205.2 10.8 
L 10.8 10.8 
z
&quot; style=&quot;fill: #ffffff&quot;/&gt;&lt;/g&gt;&lt;g id=matplotlib.axis_1&gt;&lt;g id=xtick_1&gt;&lt;g id=text_1&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(51.505016 150.207399)rotate(-45)scale(0.08 -0.08)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-2212 transform=scale(0.015625) d=&quot;M 3381 1997 
L 356 1997 
L 356 2522 
L 3381 2522 
L 3381 1997 
z
&quot;/&gt;&lt;path id=ArialMT-35 transform=scale(0.015625) d=&quot;M 266 1200 
L 856 1250 
Q 922 819 1161 601 
Q 1400 384 1738 384 
Q 2144 384 2425 690 
Q 2706 997 2706 1503 
Q 2706 1984 2436 2262 
Q 2166 2541 1728 2541 
Q 1456 2541 1237 2417 
Q 1019 2294 894 2097 
L 366 2166 
L 809 4519 
L 3088 4519 
L 3088 3981 
L 1259 3981 
L 1013 2750 
Q 1425 3038 1878 3038 
Q 2478 3038 2890 2622 
Q 3303 2206 3303 1553 
Q 3303 931 2941 478 
Q 2500 -78 1738 -78 
Q 1113 -78 717 272 
Q 322 622 266 1200 
z
&quot;/&gt;&lt;path id=ArialMT-30 transform=scale(0.015625) d=&quot;M 266 2259 
Q 266 3072 433 3567 
Q 600 4063 929 4331 
Q 1259 4600 1759 4600 
Q 2128 4600 2406 4451 
Q 2684 4303 2865 4023 
Q 3047 3744 3150 3342 
Q 3253 2941 3253 2259 
Q 3253 1453 3087 958 
Q 2922 463 2592 192 
Q 2263 -78 1759 -78 
Q 1097 -78 719 397 
Q 266 969 266 2259 
z
M 844 2259 
Q 844 1131 1108 757 
Q 1372 384 1759 384 
Q 2147 384 2411 759 
Q 2675 1134 2675 2259 
Q 2675 3391 2411 3762 
Q 2147 4134 1753 4134 
Q 1366 4134 1134 3806 
Q 844 3388 844 2259 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-2212 /&gt;&lt;use xlink:href=#ArialMT-35 x=58.398438 /&gt;&lt;use xlink:href=#ArialMT-30 x=114.013672 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_2&gt;&lt;g id=text_2&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(113.72986 143.757701)rotate(-45)scale(0.08 -0.08)&quot;&gt;&lt;use xlink:href=#ArialMT-30 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_3&gt;&lt;g id=text_3&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(171.156985 146.903442)rotate(-45)scale(0.08 -0.08)&quot;&gt;&lt;use xlink:href=#ArialMT-35 /&gt;&lt;use xlink:href=#ArialMT-30 x=55.615234 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=patch_3&gt;&lt;path d=&quot;M 19.636364 126.06289 
L 23.170909 126.06289 
L 23.170909 126.062528 
L 19.636364 126.062528 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_4&gt;&lt;path d=&quot;M 23.170909 126.06289 
L 26.705455 126.06289 
L 26.705455 126.062166 
L 23.170909 126.062166 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_5&gt;&lt;path d=&quot;M 26.705455 126.06289 
L 30.24 126.06289 
L 30.24 125.952133 
L 26.705455 125.952133 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_6&gt;&lt;path d=&quot;M 30.24 126.06289 
L 33.774545 126.06289 
L 33.774545 125.710713 
L 30.24 125.710713 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_7&gt;&lt;path d=&quot;M 33.774545 126.06289 
L 37.309091 126.06289 
L 37.309091 125.306053 
L 33.774545 125.306053 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_8&gt;&lt;path d=&quot;M 37.309091 126.06289 
L 40.843636 126.06289 
L 40.843636 123.993625 
L 37.309091 123.993625 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_9&gt;&lt;path d=&quot;M 40.843636 126.06289 
L 44.378182 126.06289 
L 44.378182 122.346755 
L 40.843636 122.346755 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_10&gt;&lt;path d=&quot;M 44.378182 126.06289 
L 47.912727 126.06289 
L 47.912727 120.959041 
L 44.378182 120.959041 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_11&gt;&lt;path d=&quot;M 47.912727 126.06289 
L 51.447273 126.06289 
L 51.447273 112.675106 
L 47.912727 112.675106 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_12&gt;&lt;path d=&quot;M 51.447273 126.06289 
L 54.981818 126.06289 
L 54.981818 94.549043 
L 51.447273 94.549043 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_13&gt;&lt;path d=&quot;M 54.981818 126.06289 
L 58.516364 126.06289 
L 58.516364 64.932172 
L 54.981818 64.932172 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_14&gt;&lt;path d=&quot;M 58.516364 126.06289 
L 62.050909 126.06289 
L 62.050909 16.288709 
L 58.516364 16.288709 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_15&gt;&lt;path d=&quot;M 62.050909 126.06289 
L 65.585455 126.06289 
L 65.585455 77.556243 
L 62.050909 77.556243 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_16&gt;&lt;path d=&quot;M 65.585455 126.06289 
L 69.12 126.06289 
L 69.12 99.755323 
L 65.585455 99.755323 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_17&gt;&lt;path d=&quot;M 69.12 126.06289 
L 72.654545 126.06289 
L 72.654545 112.215792 
L 69.12 112.215792 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_18&gt;&lt;path d=&quot;M 72.654545 126.06289 
L 76.189091 126.06289 
L 76.189091 124.763853 
L 72.654545 124.763853 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_19&gt;&lt;path d=&quot;M 76.189091 126.06289 
L 79.723636 126.06289 
L 79.723636 126.038639 
L 76.189091 126.038639 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_20&gt;&lt;path d=&quot;M 79.723636 126.06289 
L 83.258182 126.06289 
L 83.258182 126.049859 
L 79.723636 126.049859 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_21&gt;&lt;path d=&quot;M 83.258182 126.06289 
L 86.792727 126.06289 
L 86.792727 126.031038 
L 83.258182 126.031038 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_22&gt;&lt;path d=&quot;M 86.792727 126.06289 
L 90.327273 126.06289 
L 90.327273 125.840291 
L 86.792727 125.840291 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_23&gt;&lt;path d=&quot;M 90.327273 126.06289 
L 93.861818 126.06289 
L 93.861818 126.057822 
L 90.327273 126.057822 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_24&gt;&lt;path d=&quot;M 93.861818 126.06289 
L 97.396364 126.06289 
L 97.396364 126.061442 
L 93.861818 126.061442 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_25&gt;&lt;path d=&quot;M 97.396364 126.06289 
L 100.930909 126.06289 
L 100.930909 126.062166 
L 97.396364 126.062166 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_26&gt;&lt;path d=&quot;M 100.930909 126.06289 
L 104.465455 126.06289 
L 104.465455 126.062528 
L 100.930909 126.062528 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_27&gt;&lt;path d=&quot;M 104.465455 126.06289 
L 108 126.06289 
L 108 126.050945 
L 104.465455 126.050945 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_28&gt;&lt;path d=&quot;M 108 126.06289 
L 111.534545 126.06289 
L 111.534545 126.048412 
L 108 126.048412 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_29&gt;&lt;path d=&quot;M 111.534545 126.06289 
L 115.069091 126.06289 
L 115.069091 126.055651 
L 111.534545 126.055651 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_30&gt;&lt;path d=&quot;M 115.069091 126.06289 
L 118.603636 126.06289 
L 118.603636 126.06289 
L 115.069091 126.06289 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_31&gt;&lt;path d=&quot;M 118.603636 126.06289 
L 122.138182 126.06289 
L 122.138182 126.06289 
L 118.603636 126.06289 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_32&gt;&lt;path d=&quot;M 122.138182 126.06289 
L 125.672727 126.06289 
L 125.672727 126.06289 
L 122.138182 126.06289 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_33&gt;&lt;path d=&quot;M 125.672727 126.06289 
L 129.207273 126.06289 
L 129.207273 126.06289 
L 125.672727 126.06289 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_34&gt;&lt;path d=&quot;M 129.207273 126.06289 
L 132.741818 126.06289 
L 132.741818 126.06289 
L 129.207273 126.06289 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_35&gt;&lt;path d=&quot;M 132.741818 126.06289 
L 136.276364 126.06289 
L 136.276364 126.06289 
L 132.741818 126.06289 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_36&gt;&lt;path d=&quot;M 136.276364 126.06289 
L 139.810909 126.06289 
L 139.810909 126.06289 
L 136.276364 126.06289 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_37&gt;&lt;path d=&quot;M 139.810909 126.06289 
L 143.345455 126.06289 
L 143.345455 126.06289 
L 139.810909 126.06289 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_38&gt;&lt;path d=&quot;M 143.345455 126.06289 
L 146.88 126.06289 
L 146.88 126.06289 
L 143.345455 126.06289 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_39&gt;&lt;path d=&quot;M 146.88 126.06289 
L 150.414545 126.06289 
L 150.414545 126.06289 
L 146.88 126.06289 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_40&gt;&lt;path d=&quot;M 150.414545 126.06289 
L 153.949091 126.06289 
L 153.949091 126.06289 
L 150.414545 126.06289 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_41&gt;&lt;path d=&quot;M 153.949091 126.06289 
L 157.483636 126.06289 
L 157.483636 126.06289 
L 153.949091 126.06289 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_42&gt;&lt;path d=&quot;M 157.483636 126.06289 
L 161.018182 126.06289 
L 161.018182 126.06289 
L 157.483636 126.06289 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_43&gt;&lt;path d=&quot;M 161.018182 126.06289 
L 164.552727 126.06289 
L 164.552727 126.06289 
L 161.018182 126.06289 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_44&gt;&lt;path d=&quot;M 164.552727 126.06289 
L 168.087273 126.06289 
L 168.087273 126.062528 
L 164.552727 126.062528 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_45&gt;&lt;path d=&quot;M 168.087273 126.06289 
L 171.621818 126.06289 
L 171.621818 126.06289 
L 168.087273 126.06289 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_46&gt;&lt;path d=&quot;M 171.621818 126.06289 
L 175.156364 126.06289 
L 175.156364 126.06289 
L 171.621818 126.06289 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_47&gt;&lt;path d=&quot;M 175.156364 126.06289 
L 178.690909 126.06289 
L 178.690909 126.06289 
L 175.156364 126.06289 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_48&gt;&lt;path d=&quot;M 178.690909 126.06289 
L 182.225455 126.06289 
L 182.225455 126.06289 
L 178.690909 126.06289 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_49&gt;&lt;path d=&quot;M 182.225455 126.06289 
L 185.76 126.06289 
L 185.76 126.06289 
L 182.225455 126.06289 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_50&gt;&lt;path d=&quot;M 185.76 126.06289 
L 189.294545 126.06289 
L 189.294545 126.06289 
L 185.76 126.06289 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_51&gt;&lt;path d=&quot;M 189.294545 126.06289 
L 192.829091 126.06289 
L 192.829091 126.06289 
L 189.294545 126.06289 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_52&gt;&lt;path d=&quot;M 192.829091 126.06289 
L 196.363636 126.06289 
L 196.363636 126.062166 
L 192.829091 126.062166 
z
&quot; clip-path=url(#pdae612d8b4) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_53&gt;&lt;path d=&quot;M 10.8 126.06289 
L 10.8 10.8 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;g id=patch_54&gt;&lt;path d=&quot;M 205.2 126.06289 
L 205.2 10.8 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;g id=patch_55&gt;&lt;path d=&quot;M 10.8 126.06289 
L 205.2 126.06289 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;g id=patch_56&gt;&lt;path d=&quot;M 10.8 10.8 
L 205.2 10.8 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;defs&gt;&lt;clippath id=pdae612d8b4&gt;&lt;rect x=10.8 y=10.8 width=194.4 height=115.26289 /&gt;&lt;/clippath&gt;&lt;/defs&gt;&lt;/svg&gt;&lt;/div&gt;&lt;div class=&quot;col-sm-12 text-right&quot;&gt;&lt;button class=&quot;btn btn-default btn-sm&quot; data-toggle=collapse data-target=&quot;#bottom-1019400858767329170, #minifreqtable1019400858767329170&quot; aria-expanded=true aria-controls=collapseExample&gt;Toggle details&lt;/button&gt;&lt;/div&gt;&lt;div id=bottom-1019400858767329170 class=collapse&gt;&lt;div class=&quot;row spacing&quot;&gt;&lt;ul class=&quot;nav nav-tabs&quot; role=tablist&gt;&lt;li role=presentation class=active&gt;&lt;a href=#1019400858767329170bottom-1019400858767329170statistics aria-controls=1019400858767329170bottom-1019400858767329170statistics role=tab data-toggle=tab&gt;Statistics&lt;/a&gt;&lt;/li&gt;&lt;li role=presentation&gt;&lt;a href=#1019400858767329170bottom-1019400858767329170histogram aria-controls=1019400858767329170bottom-1019400858767329170histogram role=tab data-toggle=tab&gt;Histogram&lt;/a&gt;&lt;/li&gt;&lt;li role=presentation&gt;&lt;a href=#1019400858767329170bottom-1019400858767329170common_values aria-controls=1019400858767329170bottom-1019400858767329170common_values role=tab data-toggle=tab&gt;Common values&lt;/a&gt;&lt;/li&gt;&lt;li role=presentation&gt;&lt;a href=#1019400858767329170bottom-1019400858767329170extreme_values aria-controls=1019400858767329170bottom-1019400858767329170extreme_values role=tab data-toggle=tab&gt;Extreme values&lt;/a&gt;&lt;/li&gt;&lt;/ul&gt;&lt;div class=tab-content&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12 active&quot; id=1019400858767329170bottom-1019400858767329170statistics&gt;&lt;div class=col-sm-6&gt;&lt;p class=h4&gt;Quantile statistics&lt;/p&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;Minimum&lt;/th&gt;&lt;td&gt;-79.83388889&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;5-th percentile&lt;/th&gt;&lt;td&gt;-54.70055556&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Q1&lt;/th&gt;&lt;td&gt;-48.60780278&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;median&lt;/th&gt;&lt;td&gt;-44.36204722&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Q3&lt;/th&gt;&lt;td&gt;-43.74656111&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;95-th percentile&lt;/th&gt;&lt;td&gt;-38.01861111&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Maximum&lt;/th&gt;&lt;td&gt;69.93499756&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Range&lt;/th&gt;&lt;td&gt;149.7688864&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Interquartile range (IQR)&lt;/th&gt;&lt;td&gt;4.861241667&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div class=col-sm-6&gt;&lt;p class=h4&gt;Descriptive statistics&lt;/p&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;Standard deviation&lt;/th&gt;&lt;td&gt;5.121557829&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Coefficient of variation (CV)&lt;/th&gt;&lt;td&gt;-0.111475915&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Kurtosis&lt;/th&gt;&lt;td&gt;3.388136276&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Mean&lt;/th&gt;&lt;td&gt;-45.94317823&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Median Absolute Deviation (MAD)&lt;/th&gt;&lt;td&gt;2.696286111&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Skewness&lt;/th&gt;&lt;td&gt;-0.5395493836&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Sum&lt;/th&gt;&lt;td&gt;-40391358.63&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Variance&lt;/th&gt;&lt;td&gt;26.2303546&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Monotonicity&lt;/th&gt;&lt;td&gt;Not monotonic&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;/div&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12&quot; id=1019400858767329170bottom-1019400858767329170histogram&gt;&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot; standalone=&quot;no&quot;?&gt;&lt;!DOCTYPE svg class=&quot;img-responsive center-img&quot;PUBLIC &quot;-//W3C//DTD SVG 1.1//EN&quot;
  &quot;http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd&quot;&gt;&lt;svg class=&quot;img-responsive center-img&quot; xmlns:xlink=http://www.w3.org/1999/xlink width=432pt height=288pt viewbox=&quot;0 0 432 288&quot; xmlns=http://www.w3.org/2000/svg version=1.1&gt;&lt;metadata&gt;&lt;rdf:rdf xmlns:dc=http://purl.org/dc/elements/1.1/ xmlns:cc=http://creativecommons.org/ns# xmlns:rdf=http://www.w3.org/1999/02/22-rdf-syntax-ns#&gt;&lt;cc:work&gt;&lt;dc:type rdf:resource=http://purl.org/dc/dcmitype/StillImage /&gt;&lt;dc:date&gt;2022-07-12T13:06:41.526195&lt;/dc:date&gt;&lt;dc:format&gt;image/svg+xml&lt;/dc:format&gt;&lt;dc:creator&gt;&lt;cc:agent&gt;&lt;dc:title&gt;Matplotlib v3.5.2, https://matplotlib.org/&lt;/dc:title&gt;&lt;/cc:agent&gt;&lt;/dc:creator&gt;&lt;/cc:work&gt;&lt;/rdf:rdf&gt;&lt;/metadata&gt;&lt;defs&gt;&lt;style type=text/css&gt;*{stroke-linejoin: round; stroke-linecap: butt}&lt;/style&gt;&lt;/defs&gt;&lt;g id=figure_1&gt;&lt;g id=patch_1&gt;&lt;path d=&quot;M 0 288 
L 432 288 
L 432 0 
L 0 0 
z
&quot; style=&quot;fill: #ffffff&quot;/&gt;&lt;/g&gt;&lt;g id=axes_1&gt;&lt;g id=patch_2&gt;&lt;path d=&quot;M 68.86 248.562711 
L 421.2 248.562711 
L 421.2 10.8 
L 68.86 10.8 
z
&quot; style=&quot;fill: #ffffff&quot;/&gt;&lt;/g&gt;&lt;g id=matplotlib.axis_1&gt;&lt;g id=xtick_1&gt;&lt;g id=text_1&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(80.351027 276.118348)rotate(-45)scale(0.1 -0.1)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-2212 transform=scale(0.015625) d=&quot;M 3381 1997 
L 356 1997 
L 356 2522 
L 3381 2522 
L 3381 1997 
z
&quot;/&gt;&lt;path id=ArialMT-38 transform=scale(0.015625) d=&quot;M 1131 2484 
Q 781 2613 612 2850 
Q 444 3088 444 3419 
Q 444 3919 803 4259 
Q 1163 4600 1759 4600 
Q 2359 4600 2725 4251 
Q 3091 3903 3091 3403 
Q 3091 3084 2923 2848 
Q 2756 2613 2416 2484 
Q 2838 2347 3058 2040 
Q 3278 1734 3278 1309 
Q 3278 722 2862 322 
Q 2447 -78 1769 -78 
Q 1091 -78 675 323 
Q 259 725 259 1325 
Q 259 1772 486 2073 
Q 713 2375 1131 2484 
z
M 1019 3438 
Q 1019 3113 1228 2906 
Q 1438 2700 1772 2700 
Q 2097 2700 2305 2904 
Q 2513 3109 2513 3406 
Q 2513 3716 2298 3927 
Q 2084 4138 1766 4138 
Q 1444 4138 1231 3931 
Q 1019 3725 1019 3438 
z
M 838 1322 
Q 838 1081 952 856 
Q 1066 631 1291 507 
Q 1516 384 1775 384 
Q 2178 384 2440 643 
Q 2703 903 2703 1303 
Q 2703 1709 2433 1975 
Q 2163 2241 1756 2241 
Q 1359 2241 1098 1978 
Q 838 1716 838 1322 
z
&quot;/&gt;&lt;path id=ArialMT-30 transform=scale(0.015625) d=&quot;M 266 2259 
Q 266 3072 433 3567 
Q 600 4063 929 4331 
Q 1259 4600 1759 4600 
Q 2128 4600 2406 4451 
Q 2684 4303 2865 4023 
Q 3047 3744 3150 3342 
Q 3253 2941 3253 2259 
Q 3253 1453 3087 958 
Q 2922 463 2592 192 
Q 2263 -78 1759 -78 
Q 1097 -78 719 397 
Q 266 969 266 2259 
z
M 844 2259 
Q 844 1131 1108 757 
Q 1372 384 1759 384 
Q 2147 384 2411 759 
Q 2675 1134 2675 2259 
Q 2675 3391 2411 3762 
Q 2147 4134 1753 4134 
Q 1366 4134 1134 3806 
Q 844 3388 844 2259 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-2212 /&gt;&lt;use xlink:href=#ArialMT-38 x=58.398438 /&gt;&lt;use xlink:href=#ArialMT-30 x=114.013672 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_2&gt;&lt;g id=text_2&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(123.124809 276.118348)rotate(-45)scale(0.1 -0.1)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-36 transform=scale(0.015625) d=&quot;M 3184 3459 
L 2625 3416 
Q 2550 3747 2413 3897 
Q 2184 4138 1850 4138 
Q 1581 4138 1378 3988 
Q 1113 3794 959 3422 
Q 806 3050 800 2363 
Q 1003 2672 1297 2822 
Q 1591 2972 1913 2972 
Q 2475 2972 2870 2558 
Q 3266 2144 3266 1488 
Q 3266 1056 3080 686 
Q 2894 316 2569 119 
Q 2244 -78 1831 -78 
Q 1128 -78 684 439 
Q 241 956 241 2144 
Q 241 3472 731 4075 
Q 1159 4600 1884 4600 
Q 2425 4600 2770 4297 
Q 3116 3994 3184 3459 
z
M 888 1484 
Q 888 1194 1011 928 
Q 1134 663 1356 523 
Q 1578 384 1822 384 
Q 2178 384 2434 671 
Q 2691 959 2691 1453 
Q 2691 1928 2437 2201 
Q 2184 2475 1800 2475 
Q 1419 2475 1153 2201 
Q 888 1928 888 1484 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-2212 /&gt;&lt;use xlink:href=#ArialMT-36 x=58.398438 /&gt;&lt;use xlink:href=#ArialMT-30 x=114.013672 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_3&gt;&lt;g id=text_3&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(165.898592 276.118348)rotate(-45)scale(0.1 -0.1)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-34 transform=scale(0.015625) d=&quot;M 2069 0 
L 2069 1097 
L 81 1097 
L 81 1613 
L 2172 4581 
L 2631 4581 
L 2631 1613 
L 3250 1613 
L 3250 1097 
L 2631 1097 
L 2631 0 
L 2069 0 
z
M 2069 1613 
L 2069 3678 
L 634 1613 
L 2069 1613 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-2212 /&gt;&lt;use xlink:href=#ArialMT-34 x=58.398438 /&gt;&lt;use xlink:href=#ArialMT-30 x=114.013672 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_4&gt;&lt;g id=text_4&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(208.672375 276.118348)rotate(-45)scale(0.1 -0.1)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-32 transform=scale(0.015625) d=&quot;M 3222 541 
L 3222 0 
L 194 0 
Q 188 203 259 391 
Q 375 700 629 1000 
Q 884 1300 1366 1694 
Q 2113 2306 2375 2664 
Q 2638 3022 2638 3341 
Q 2638 3675 2398 3904 
Q 2159 4134 1775 4134 
Q 1369 4134 1125 3890 
Q 881 3647 878 3216 
L 300 3275 
Q 359 3922 746 4261 
Q 1134 4600 1788 4600 
Q 2447 4600 2831 4234 
Q 3216 3869 3216 3328 
Q 3216 3053 3103 2787 
Q 2991 2522 2730 2228 
Q 2469 1934 1863 1422 
Q 1356 997 1212 845 
Q 1069 694 975 541 
L 3222 541 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-2212 /&gt;&lt;use xlink:href=#ArialMT-32 x=58.398438 /&gt;&lt;use xlink:href=#ArialMT-30 x=114.013672 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_5&gt;&lt;g id=text_5&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(255.477219 268.056225)rotate(-45)scale(0.1 -0.1)&quot;&gt;&lt;use xlink:href=#ArialMT-30 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_6&gt;&lt;g id=text_6&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(296.284913 271.988402)rotate(-45)scale(0.1 -0.1)&quot;&gt;&lt;use xlink:href=#ArialMT-32 /&gt;&lt;use xlink:href=#ArialMT-30 x=55.615234 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_7&gt;&lt;g id=text_7&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(339.058696 271.988402)rotate(-45)scale(0.1 -0.1)&quot;&gt;&lt;use xlink:href=#ArialMT-34 /&gt;&lt;use xlink:href=#ArialMT-30 x=55.615234 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_8&gt;&lt;g id=text_8&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(381.832479 271.988402)rotate(-45)scale(0.1 -0.1)&quot;&gt;&lt;use xlink:href=#ArialMT-36 /&gt;&lt;use xlink:href=#ArialMT-30 x=55.615234 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=matplotlib.axis_2&gt;&lt;g id=ytick_1&gt;&lt;g id=text_9&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(52.799062 252.141617)scale(0.1 -0.1)&quot;&gt;&lt;use xlink:href=#ArialMT-30 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_2&gt;&lt;g id=text_10&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(30.555312 214.810406)scale(0.1 -0.1)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-35 transform=scale(0.015625) d=&quot;M 266 1200 
L 856 1250 
Q 922 819 1161 601 
Q 1400 384 1738 384 
Q 2144 384 2425 690 
Q 2706 997 2706 1503 
Q 2706 1984 2436 2262 
Q 2166 2541 1728 2541 
Q 1456 2541 1237 2417 
Q 1019 2294 894 2097 
L 366 2166 
L 809 4519 
L 3088 4519 
L 3088 3981 
L 1259 3981 
L 1013 2750 
Q 1425 3038 1878 3038 
Q 2478 3038 2890 2622 
Q 3303 2206 3303 1553 
Q 3303 931 2941 478 
Q 2500 -78 1738 -78 
Q 1113 -78 717 272 
Q 322 622 266 1200 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-35 /&gt;&lt;use xlink:href=#ArialMT-30 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-30 x=222.460938 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_3&gt;&lt;g id=text_11&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(24.994375 177.479194)scale(0.1 -0.1)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-31 transform=scale(0.015625) d=&quot;M 2384 0 
L 1822 0 
L 1822 3584 
Q 1619 3391 1289 3197 
Q 959 3003 697 2906 
L 697 3450 
Q 1169 3672 1522 3987 
Q 1875 4303 2022 4600 
L 2384 4600 
L 2384 0 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-31 /&gt;&lt;use xlink:href=#ArialMT-30 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-30 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-30 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_4&gt;&lt;g id=text_12&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(24.994375 140.147982)scale(0.1 -0.1)&quot;&gt;&lt;use xlink:href=#ArialMT-31 /&gt;&lt;use xlink:href=#ArialMT-35 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-30 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-30 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_5&gt;&lt;g id=text_13&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(24.994375 102.816771)scale(0.1 -0.1)&quot;&gt;&lt;use xlink:href=#ArialMT-32 /&gt;&lt;use xlink:href=#ArialMT-30 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-30 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-30 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_6&gt;&lt;g id=text_14&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(24.994375 65.485559)scale(0.1 -0.1)&quot;&gt;&lt;use xlink:href=#ArialMT-32 /&gt;&lt;use xlink:href=#ArialMT-35 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-30 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-30 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_7&gt;&lt;g id=text_15&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(24.994375 28.154347)scale(0.1 -0.1)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-33 transform=scale(0.015625) d=&quot;M 269 1209 
L 831 1284 
Q 928 806 1161 595 
Q 1394 384 1728 384 
Q 2125 384 2398 659 
Q 2672 934 2672 1341 
Q 2672 1728 2419 1979 
Q 2166 2231 1775 2231 
Q 1616 2231 1378 2169 
L 1441 2663 
Q 1497 2656 1531 2656 
Q 1891 2656 2178 2843 
Q 2466 3031 2466 3422 
Q 2466 3731 2256 3934 
Q 2047 4138 1716 4138 
Q 1388 4138 1169 3931 
Q 950 3725 888 3313 
L 325 3413 
Q 428 3978 793 4289 
Q 1159 4600 1703 4600 
Q 2078 4600 2393 4439 
Q 2709 4278 2876 4000 
Q 3044 3722 3044 3409 
Q 3044 3113 2884 2869 
Q 2725 2625 2413 2481 
Q 2819 2388 3044 2092 
Q 3269 1797 3269 1353 
Q 3269 753 2831 336 
Q 2394 -81 1725 -81 
Q 1122 -81 723 278 
Q 325 638 269 1209 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-33 /&gt;&lt;use xlink:href=#ArialMT-30 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-30 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-30 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=text_16&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(18.679219 155.664559)rotate(-90)scale(0.11 -0.11)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-46 transform=scale(0.015625) d=&quot;M 525 0 
L 525 4581 
L 3616 4581 
L 3616 4041 
L 1131 4041 
L 1131 2622 
L 3281 2622 
L 3281 2081 
L 1131 2081 
L 1131 0 
L 525 0 
z
&quot;/&gt;&lt;path id=ArialMT-72 transform=scale(0.015625) d=&quot;M 416 0 
L 416 3319 
L 922 3319 
L 922 2816 
Q 1116 3169 1280 3281 
Q 1444 3394 1641 3394 
Q 1925 3394 2219 3213 
L 2025 2691 
Q 1819 2813 1613 2813 
Q 1428 2813 1281 2702 
Q 1134 2591 1072 2394 
Q 978 2094 978 1738 
L 978 0 
L 416 0 
z
&quot;/&gt;&lt;path id=ArialMT-65 transform=scale(0.015625) d=&quot;M 2694 1069 
L 3275 997 
Q 3138 488 2766 206 
Q 2394 -75 1816 -75 
Q 1088 -75 661 373 
Q 234 822 234 1631 
Q 234 2469 665 2931 
Q 1097 3394 1784 3394 
Q 2450 3394 2872 2941 
Q 3294 2488 3294 1666 
Q 3294 1616 3291 1516 
L 816 1516 
Q 847 969 1125 678 
Q 1403 388 1819 388 
Q 2128 388 2347 550 
Q 2566 713 2694 1069 
z
M 847 1978 
L 2700 1978 
Q 2663 2397 2488 2606 
Q 2219 2931 1791 2931 
Q 1403 2931 1139 2672 
Q 875 2413 847 1978 
z
&quot;/&gt;&lt;path id=ArialMT-71 transform=scale(0.015625) d=&quot;M 2538 -1272 
L 2538 353 
Q 2406 169 2170 47 
Q 1934 -75 1669 -75 
Q 1078 -75 651 397 
Q 225 869 225 1691 
Q 225 2191 398 2587 
Q 572 2984 901 3189 
Q 1231 3394 1625 3394 
Q 2241 3394 2594 2875 
L 2594 3319 
L 3100 3319 
L 3100 -1272 
L 2538 -1272 
z
M 803 1669 
Q 803 1028 1072 708 
Q 1341 388 1716 388 
Q 2075 388 2334 692 
Q 2594 997 2594 1619 
Q 2594 2281 2320 2615 
Q 2047 2950 1678 2950 
Q 1313 2950 1058 2639 
Q 803 2328 803 1669 
z
&quot;/&gt;&lt;path id=ArialMT-75 transform=scale(0.015625) d=&quot;M 2597 0 
L 2597 488 
Q 2209 -75 1544 -75 
Q 1250 -75 995 37 
Q 741 150 617 320 
Q 494 491 444 738 
Q 409 903 409 1263 
L 409 3319 
L 972 3319 
L 972 1478 
Q 972 1038 1006 884 
Q 1059 663 1231 536 
Q 1403 409 1656 409 
Q 1909 409 2131 539 
Q 2353 669 2445 892 
Q 2538 1116 2538 1541 
L 2538 3319 
L 3100 3319 
L 3100 0 
L 2597 0 
z
&quot;/&gt;&lt;path id=ArialMT-6e transform=scale(0.015625) d=&quot;M 422 0 
L 422 3319 
L 928 3319 
L 928 2847 
Q 1294 3394 1984 3394 
Q 2284 3394 2536 3286 
Q 2788 3178 2913 3003 
Q 3038 2828 3088 2588 
Q 3119 2431 3119 2041 
L 3119 0 
L 2556 0 
L 2556 2019 
Q 2556 2363 2490 2533 
Q 2425 2703 2258 2804 
Q 2091 2906 1866 2906 
Q 1506 2906 1245 2678 
Q 984 2450 984 1813 
L 984 0 
L 422 0 
z
&quot;/&gt;&lt;path id=ArialMT-63 transform=scale(0.015625) d=&quot;M 2588 1216 
L 3141 1144 
Q 3050 572 2676 248 
Q 2303 -75 1759 -75 
Q 1078 -75 664 370 
Q 250 816 250 1647 
Q 250 2184 428 2587 
Q 606 2991 970 3192 
Q 1334 3394 1763 3394 
Q 2303 3394 2647 3120 
Q 2991 2847 3088 2344 
L 2541 2259 
Q 2463 2594 2264 2762 
Q 2066 2931 1784 2931 
Q 1359 2931 1093 2626 
Q 828 2322 828 1663 
Q 828 994 1084 691 
Q 1341 388 1753 388 
Q 2084 388 2306 591 
Q 2528 794 2588 1216 
z
&quot;/&gt;&lt;path id=ArialMT-79 transform=scale(0.015625) d=&quot;M 397 -1278 
L 334 -750 
Q 519 -800 656 -800 
Q 844 -800 956 -737 
Q 1069 -675 1141 -563 
Q 1194 -478 1313 -144 
Q 1328 -97 1363 -6 
L 103 3319 
L 709 3319 
L 1400 1397 
Q 1534 1031 1641 628 
Q 1738 1016 1872 1384 
L 2581 3319 
L 3144 3319 
L 1881 -56 
Q 1678 -603 1566 -809 
Q 1416 -1088 1222 -1217 
Q 1028 -1347 759 -1347 
Q 597 -1347 397 -1278 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-46 /&gt;&lt;use xlink:href=#ArialMT-72 x=61.083984 /&gt;&lt;use xlink:href=#ArialMT-65 x=94.384766 /&gt;&lt;use xlink:href=#ArialMT-71 x=150 /&gt;&lt;use xlink:href=#ArialMT-75 x=205.615234 /&gt;&lt;use xlink:href=#ArialMT-65 x=261.230469 /&gt;&lt;use xlink:href=#ArialMT-6e x=316.845703 /&gt;&lt;use xlink:href=#ArialMT-63 x=372.460938 /&gt;&lt;use xlink:href=#ArialMT-79 x=422.460938 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=patch_3&gt;&lt;path d=&quot;M 84.875455 248.562711 
L 91.281636 248.562711 
L 91.281636 248.561964 
L 84.875455 248.561964 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_4&gt;&lt;path d=&quot;M 91.281636 248.562711 
L 97.687818 248.562711 
L 97.687818 248.561218 
L 91.281636 248.561218 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_5&gt;&lt;path d=&quot;M 97.687818 248.562711 
L 104.094 248.562711 
L 104.094 248.334244 
L 97.687818 248.334244 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_6&gt;&lt;path d=&quot;M 104.094 248.562711 
L 110.500182 248.562711 
L 110.500182 247.836246 
L 104.094 247.836246 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_7&gt;&lt;path d=&quot;M 110.500182 248.562711 
L 116.906364 248.562711 
L 116.906364 247.00152 
L 110.500182 247.00152 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_8&gt;&lt;path d=&quot;M 116.906364 248.562711 
L 123.312545 248.562711 
L 123.312545 244.29426 
L 116.906364 244.29426 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_9&gt;&lt;path d=&quot;M 123.312545 248.562711 
L 129.718727 248.562711 
L 129.718727 240.89712 
L 123.312545 240.89712 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_10&gt;&lt;path d=&quot;M 129.718727 248.562711 
L 136.124909 248.562711 
L 136.124909 238.034563 
L 129.718727 238.034563 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_11&gt;&lt;path d=&quot;M 136.124909 248.562711 
L 142.531091 248.562711 
L 142.531091 220.946574 
L 136.124909 220.946574 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_12&gt;&lt;path d=&quot;M 142.531091 248.562711 
L 148.937273 248.562711 
L 148.937273 183.556379 
L 142.531091 183.556379 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_13&gt;&lt;path d=&quot;M 148.937273 248.562711 
L 155.343455 248.562711 
L 155.343455 122.463104 
L 148.937273 122.463104 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_14&gt;&lt;path d=&quot;M 155.343455 248.562711 
L 161.749636 248.562711 
L 161.749636 22.122034 
L 155.343455 22.122034 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_15&gt;&lt;path d=&quot;M 161.749636 248.562711 
L 168.155818 248.562711 
L 168.155818 148.503864 
L 161.749636 148.503864 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_16&gt;&lt;path d=&quot;M 168.155818 248.562711 
L 174.562 248.562711 
L 174.562 194.295822 
L 168.155818 194.295822 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_17&gt;&lt;path d=&quot;M 174.562 248.562711 
L 180.968182 248.562711 
L 180.968182 219.999108 
L 174.562 219.999108 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_18&gt;&lt;path d=&quot;M 180.968182 248.562711 
L 187.374364 248.562711 
L 187.374364 245.883077 
L 180.968182 245.883077 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_19&gt;&lt;path d=&quot;M 187.374364 248.562711 
L 193.780545 248.562711 
L 193.780545 248.512687 
L 187.374364 248.512687 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_20&gt;&lt;path d=&quot;M 193.780545 248.562711 
L 200.186727 248.562711 
L 200.186727 248.535833 
L 193.780545 248.535833 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_21&gt;&lt;path d=&quot;M 200.186727 248.562711 
L 206.592909 248.562711 
L 206.592909 248.497008 
L 200.186727 248.497008 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_22&gt;&lt;path d=&quot;M 206.592909 248.562711 
L 212.999091 248.562711 
L 212.999091 248.103537 
L 206.592909 248.103537 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_23&gt;&lt;path d=&quot;M 212.999091 248.562711 
L 219.405273 248.562711 
L 219.405273 248.552258 
L 212.999091 248.552258 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_24&gt;&lt;path d=&quot;M 219.405273 248.562711 
L 225.811455 248.562711 
L 225.811455 248.559725 
L 219.405273 248.559725 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_25&gt;&lt;path d=&quot;M 225.811455 248.562711 
L 232.217636 248.562711 
L 232.217636 248.561218 
L 225.811455 248.561218 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_26&gt;&lt;path d=&quot;M 232.217636 248.562711 
L 238.623818 248.562711 
L 238.623818 248.561964 
L 232.217636 248.561964 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_27&gt;&lt;path d=&quot;M 238.623818 248.562711 
L 245.03 248.562711 
L 245.03 248.538072 
L 238.623818 248.538072 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_28&gt;&lt;path d=&quot;M 245.03 248.562711 
L 251.436182 248.562711 
L 251.436182 248.532846 
L 245.03 248.532846 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_29&gt;&lt;path d=&quot;M 251.436182 248.562711 
L 257.842364 248.562711 
L 257.842364 248.547779 
L 251.436182 248.547779 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_30&gt;&lt;path d=&quot;M 257.842364 248.562711 
L 264.248545 248.562711 
L 264.248545 248.562711 
L 257.842364 248.562711 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_31&gt;&lt;path d=&quot;M 264.248545 248.562711 
L 270.654727 248.562711 
L 270.654727 248.562711 
L 264.248545 248.562711 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_32&gt;&lt;path d=&quot;M 270.654727 248.562711 
L 277.060909 248.562711 
L 277.060909 248.562711 
L 270.654727 248.562711 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_33&gt;&lt;path d=&quot;M 277.060909 248.562711 
L 283.467091 248.562711 
L 283.467091 248.562711 
L 277.060909 248.562711 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_34&gt;&lt;path d=&quot;M 283.467091 248.562711 
L 289.873273 248.562711 
L 289.873273 248.562711 
L 283.467091 248.562711 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_35&gt;&lt;path d=&quot;M 289.873273 248.562711 
L 296.279455 248.562711 
L 296.279455 248.562711 
L 289.873273 248.562711 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_36&gt;&lt;path d=&quot;M 296.279455 248.562711 
L 302.685636 248.562711 
L 302.685636 248.562711 
L 296.279455 248.562711 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_37&gt;&lt;path d=&quot;M 302.685636 248.562711 
L 309.091818 248.562711 
L 309.091818 248.562711 
L 302.685636 248.562711 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_38&gt;&lt;path d=&quot;M 309.091818 248.562711 
L 315.498 248.562711 
L 315.498 248.562711 
L 309.091818 248.562711 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_39&gt;&lt;path d=&quot;M 315.498 248.562711 
L 321.904182 248.562711 
L 321.904182 248.562711 
L 315.498 248.562711 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_40&gt;&lt;path d=&quot;M 321.904182 248.562711 
L 328.310364 248.562711 
L 328.310364 248.562711 
L 321.904182 248.562711 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_41&gt;&lt;path d=&quot;M 328.310364 248.562711 
L 334.716545 248.562711 
L 334.716545 248.562711 
L 328.310364 248.562711 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_42&gt;&lt;path d=&quot;M 334.716545 248.562711 
L 341.122727 248.562711 
L 341.122727 248.562711 
L 334.716545 248.562711 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_43&gt;&lt;path d=&quot;M 341.122727 248.562711 
L 347.528909 248.562711 
L 347.528909 248.562711 
L 341.122727 248.562711 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_44&gt;&lt;path d=&quot;M 347.528909 248.562711 
L 353.935091 248.562711 
L 353.935091 248.561964 
L 347.528909 248.561964 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_45&gt;&lt;path d=&quot;M 353.935091 248.562711 
L 360.341273 248.562711 
L 360.341273 248.562711 
L 353.935091 248.562711 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_46&gt;&lt;path d=&quot;M 360.341273 248.562711 
L 366.747455 248.562711 
L 366.747455 248.562711 
L 360.341273 248.562711 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_47&gt;&lt;path d=&quot;M 366.747455 248.562711 
L 373.153636 248.562711 
L 373.153636 248.562711 
L 366.747455 248.562711 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_48&gt;&lt;path d=&quot;M 373.153636 248.562711 
L 379.559818 248.562711 
L 379.559818 248.562711 
L 373.153636 248.562711 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_49&gt;&lt;path d=&quot;M 379.559818 248.562711 
L 385.966 248.562711 
L 385.966 248.562711 
L 379.559818 248.562711 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_50&gt;&lt;path d=&quot;M 385.966 248.562711 
L 392.372182 248.562711 
L 392.372182 248.562711 
L 385.966 248.562711 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_51&gt;&lt;path d=&quot;M 392.372182 248.562711 
L 398.778364 248.562711 
L 398.778364 248.562711 
L 392.372182 248.562711 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_52&gt;&lt;path d=&quot;M 398.778364 248.562711 
L 405.184545 248.562711 
L 405.184545 248.561218 
L 398.778364 248.561218 
z
&quot; clip-path=url(#p3deda1b7ad) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_53&gt;&lt;path d=&quot;M 68.86 248.562711 
L 68.86 10.8 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;g id=patch_54&gt;&lt;path d=&quot;M 421.2 248.562711 
L 421.2 10.8 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;g id=patch_55&gt;&lt;path d=&quot;M 68.86 248.562711 
L 421.2 248.562711 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;g id=patch_56&gt;&lt;path d=&quot;M 68.86 10.8 
L 421.2 10.8 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;defs&gt;&lt;clippath id=p3deda1b7ad&gt;&lt;rect x=68.86 y=10.8 width=352.34 height=237.762711 /&gt;&lt;/clippath&gt;&lt;/defs&gt;&lt;/svg&gt;&lt;div class=&quot;caption text-center text-muted&quot;&gt;&lt;strong&gt;Histogram with fixed size bins&lt;/strong&gt; (bins=50) &lt;/div&gt;&lt;/div&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12&quot; id=1019400858767329170bottom-1019400858767329170common_values&gt;&lt;table class=&quot;freq table table-hover table-striped&quot;&gt;&lt;thead&gt;&lt;tr&gt;&lt;td&gt;Value&lt;/td&gt;&lt;td&gt;Count&lt;/td&gt;&lt;td&gt;Frequency (%)&lt;/td&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr class&gt;&lt;td title=-43.98932222&gt;-43.98932222&lt;/td&gt;&lt;td&gt;3550&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.5%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.92037778&gt;-43.92037778&lt;/td&gt;&lt;td&gt;2880&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.4%&gt; &amp;nbsp; &lt;/div&gt; 0.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.98772778&gt;-43.98772778&lt;/td&gt;&lt;td&gt;2880&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.4%&gt; &amp;nbsp; &lt;/div&gt; 0.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.89342778&gt;-43.89342778&lt;/td&gt;&lt;td&gt;2880&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.4%&gt; &amp;nbsp; &lt;/div&gt; 0.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.98421389&gt;-43.98421389&lt;/td&gt;&lt;td&gt;2880&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.4%&gt; &amp;nbsp; &lt;/div&gt; 0.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.67096944&gt;-43.67096944&lt;/td&gt;&lt;td&gt;2880&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.4%&gt; &amp;nbsp; &lt;/div&gt; 0.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.91933889&gt;-43.91933889&lt;/td&gt;&lt;td&gt;2880&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.4%&gt; &amp;nbsp; &lt;/div&gt; 0.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.94683056&gt;-43.94683056&lt;/td&gt;&lt;td&gt;2845&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.4%&gt; &amp;nbsp; &lt;/div&gt; 0.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.95258611&gt;-43.95258611&lt;/td&gt;&lt;td&gt;2775&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.4%&gt; &amp;nbsp; &lt;/div&gt; 0.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.96584167&gt;-43.96584167&lt;/td&gt;&lt;td&gt;2635&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.4%&gt; &amp;nbsp; &lt;/div&gt; 0.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.95615278&gt;-43.95615278&lt;/td&gt;&lt;td&gt;2600&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.4%&gt; &amp;nbsp; &lt;/div&gt; 0.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.98828056&gt;-43.98828056&lt;/td&gt;&lt;td&gt;2520&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.91624444&gt;-43.91624444&lt;/td&gt;&lt;td&gt;2520&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.94463056&gt;-43.94463056&lt;/td&gt;&lt;td&gt;1800&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-44.33700278&gt;-44.33700278&lt;/td&gt;&lt;td&gt;1625&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.96117222&gt;-43.96117222&lt;/td&gt;&lt;td&gt;1500&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.92029167&gt;-43.92029167&lt;/td&gt;&lt;td&gt;1490&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-40.11388889&gt;-40.11388889&lt;/td&gt;&lt;td&gt;1444&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.17646111&gt;-43.17646111&lt;/td&gt;&lt;td&gt;1443&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-44.06666667&gt;-44.06666667&lt;/td&gt;&lt;td&gt;1441&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.94632778&gt;-43.94632778&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.62953333&gt;-43.62953333&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.19884722&gt;-43.19884722&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.55045&gt;-43.55045&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.91421944&gt;-43.91421944&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.5093&gt;-43.5093&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-44.13361111&gt;-44.13361111&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.41604444&gt;-43.41604444&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.74656111&gt;-43.74656111&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-44.15366667&gt;-44.15366667&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.71584444&gt;-43.71584444&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.95032778&gt;-43.95032778&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.78903333&gt;-43.78903333&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.66944722&gt;-43.66944722&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.41554167&gt;-43.41554167&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.79594167&gt;-43.79594167&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.28615&gt;-43.28615&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.47635833&gt;-43.47635833&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.93742222&gt;-43.93742222&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.94255833&gt;-43.94255833&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-44.02788889&gt;-44.02788889&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.70961667&gt;-43.70961667&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.67327778&gt;-43.67327778&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.912675&gt;-43.912675&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.99539722&gt;-43.99539722&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.94699722&gt;-43.94699722&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-44.03476389&gt;-44.03476389&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.93149722&gt;-43.93149722&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.92573611&gt;-43.92573611&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.75389722&gt;-43.75389722&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.95459167&gt;-43.95459167&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-44.01406944&gt;-44.01406944&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.85907778&gt;-43.85907778&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.94713611&gt;-43.94713611&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.93256389&gt;-43.93256389&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-44.02120278&gt;-44.02120278&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.88041389&gt;-43.88041389&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.86638611&gt;-43.86638611&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.92937778&gt;-43.92937778&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.96291944&gt;-43.96291944&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.58318056&gt;-43.58318056&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.96173611&gt;-43.96173611&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.79990833&gt;-43.79990833&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.68671111&gt;-43.68671111&lt;/td&gt;&lt;td&gt;1440&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.89145556&gt;-43.89145556&lt;/td&gt;&lt;td&gt;1435&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.82728333&gt;-43.82728333&lt;/td&gt;&lt;td&gt;1410&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.96307222&gt;-43.96307222&lt;/td&gt;&lt;td&gt;1405&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.98224167&gt;-43.98224167&lt;/td&gt;&lt;td&gt;1405&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.91553611&gt;-43.91553611&lt;/td&gt;&lt;td&gt;1405&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.93800833&gt;-43.93800833&lt;/td&gt;&lt;td&gt;1405&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.95731667&gt;-43.95731667&lt;/td&gt;&lt;td&gt;1370&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-44.00166667&gt;-44.00166667&lt;/td&gt;&lt;td&gt;1336&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.96771111&gt;-43.96771111&lt;/td&gt;&lt;td&gt;1330&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-44.06527778&gt;-44.06527778&lt;/td&gt;&lt;td&gt;1303&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-44.03777778&gt;-44.03777778&lt;/td&gt;&lt;td&gt;1301&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.87385556&gt;-43.87385556&lt;/td&gt;&lt;td&gt;1301&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-44.43561667&gt;-44.43561667&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.84408333&gt;-43.84408333&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-44.07726111&gt;-44.07726111&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-44.19216667&gt;-44.19216667&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.92732222&gt;-43.92732222&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-44.05935556&gt;-44.05935556&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.90316111&gt;-43.90316111&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-44.03816111&gt;-44.03816111&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-44.16038889&gt;-44.16038889&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-44.19939722&gt;-44.19939722&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-44.04918056&gt;-44.04918056&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-44.19753333&gt;-44.19753333&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-44.2223&gt;-44.2223&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.91643611&gt;-43.91643611&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-44.31009722&gt;-44.31009722&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.88447222&gt;-43.88447222&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-44.43339444&gt;-44.43339444&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-44.41431944&gt;-44.41431944&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-44.02985&gt;-44.02985&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-44.31085278&gt;-44.31085278&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-44.08922222&gt;-44.08922222&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.83596111&gt;-43.83596111&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-43.66727778&gt;-43.66727778&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-44.12957778&gt;-44.12957778&lt;/td&gt;&lt;td&gt;1300&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class=other&gt;&lt;td title=&quot;Other values (153079)&quot;&gt;Other values (153079)&lt;/td&gt;&lt;td&gt;720725&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt; 82.0% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12&quot; id=1019400858767329170bottom-1019400858767329170extreme_values&gt;&lt;div class=&quot;row spacing&quot;&gt;&lt;ul class=&quot;nav nav-tabs&quot; role=tablist&gt;&lt;li role=presentation class=active&gt;&lt;a href=#1019400858767329170extreme_values-1019400858767329170firstn aria-controls=1019400858767329170extreme_values-1019400858767329170firstn role=tab data-toggle=tab&gt;Minimum 10 values&lt;/a&gt;&lt;/li&gt;&lt;li role=presentation&gt;&lt;a href=#1019400858767329170extreme_values-1019400858767329170lastn aria-controls=1019400858767329170extreme_values-1019400858767329170lastn role=tab data-toggle=tab&gt;Maximum 10 values&lt;/a&gt;&lt;/li&gt;&lt;/ul&gt;&lt;div class=tab-content&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12 active&quot; id=1019400858767329170extreme_values-1019400858767329170firstn&gt;&lt;table class=&quot;freq table table-hover table-striped&quot;&gt;&lt;thead&gt;&lt;tr&gt;&lt;td&gt;Value&lt;/td&gt;&lt;td&gt;Count&lt;/td&gt;&lt;td&gt;Frequency (%)&lt;/td&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr class&gt;&lt;td title=-79.83388889&gt;-79.83388889&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:50.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-74.90580556&gt;-74.90580556&lt;/td&gt;&lt;td&gt;2&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-72.93138889&gt;-72.93138889&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:50.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-72.92111111&gt;-72.92111111&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:50.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-72.92055556&gt;-72.92055556&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:50.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-72.9205&gt;-72.9205&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:50.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-72.92028&gt;-72.92028&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:50.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-72.91&gt;-72.91&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:50.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-72.90422222&gt;-72.90422222&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:50.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-72.90275&gt;-72.90275&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:50.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12&quot; id=1019400858767329170extreme_values-1019400858767329170lastn&gt;&lt;table class=&quot;freq table table-hover table-striped&quot;&gt;&lt;thead&gt;&lt;tr&gt;&lt;td&gt;Value&lt;/td&gt;&lt;td&gt;Count&lt;/td&gt;&lt;td&gt;Frequency (%)&lt;/td&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr class&gt;&lt;td title=69.93499756&gt;69.93499756&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:6.2%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=69.03333333&gt;69.03333333&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:6.2%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=45.95944444&gt;45.95944444&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:6.2%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=0&gt;0&lt;/td&gt;&lt;td&gt;16&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-0.37375&gt;-0.37375&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:6.2%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-0.65505&gt;-0.65505&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:6.2%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-0.7733333333&gt;-0.7733333333&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:6.2%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-1.024444444&gt;-1.024444444&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:6.2%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-4.093638889&gt;-4.093638889&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:6.2%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-4.279922222&gt;-4.279922222&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:6.2%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;div class=&quot;row spacing&quot;&gt;&lt;a class=&quot;anchor-pos anchor-pos-variable&quot; id=pp_var_-8438619141185252187&gt;&lt;/a&gt;&lt;div class=variable&gt;&lt;div class=col-sm-3&gt;&lt;p class=h4 title=Description&gt;&lt;a href=#pp_var_-8438619141185252187&gt;Description&lt;/a&gt;&lt;br&gt;&lt;small&gt;Categorical&lt;/small&gt;&lt;/p&gt;&lt;code&gt;HIGH CARDINALITY&lt;/code&gt;&lt;br&gt;&lt;p class=variable-description&gt;&lt;/p&gt;&lt;/div&gt;&lt;div class=col-sm-3&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr class=alert&gt;&lt;th&gt;Distinct&lt;/th&gt;&lt;td&gt;234096&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Distinct (%)&lt;/th&gt;&lt;td&gt;26.6%&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Missing&lt;/th&gt;&lt;td&gt;0&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Missing (%)&lt;/th&gt;&lt;td&gt;0.0%&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Memory size&lt;/th&gt;&lt;td&gt;13.2 MiB&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div class=col-sm-6&gt;&lt;div class=&quot;col-sm- collapse in&quot; id=minifreqtable&gt;&lt;table class=&quot;mini freq&quot;&gt;&lt;tr class&gt;&lt;th width=50%&gt; [STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1001758606), Belo Horizonte/MG &lt;/th&gt;&lt;td width=50%&gt;&lt;div class=bar style=width:0.0% data-toggle=tooltip data-placement=right data-html=true data-delay=500&gt; &amp;nbsp; &lt;/div&gt; 410 &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;th width=50%&gt; [STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002745745), Belo Horizonte/MG &lt;/th&gt;&lt;td width=50%&gt;&lt;div class=bar style=width:0.0% data-toggle=tooltip data-placement=right data-html=true data-delay=500&gt; &amp;nbsp; &lt;/div&gt; 375 &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;th width=50%&gt; [STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002623429), Belo Horizonte/MG &lt;/th&gt;&lt;td width=50%&gt;&lt;div class=bar style=width:0.0% data-toggle=tooltip data-placement=right data-html=true data-delay=500&gt; &amp;nbsp; &lt;/div&gt; 375 &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;th width=50%&gt; [STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002745567), Belo Horizonte/MG &lt;/th&gt;&lt;td width=50%&gt;&lt;div class=bar style=width:0.0% data-toggle=tooltip data-placement=right data-html=true data-delay=500&gt; &amp;nbsp; &lt;/div&gt; 375 &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;th width=50%&gt; [STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002745656), Belo Horizonte/MG &lt;/th&gt;&lt;td width=50%&gt;&lt;div class=bar style=width:0.0% data-toggle=tooltip data-placement=right data-html=true data-delay=500&gt; &amp;nbsp; &lt;/div&gt; 375 &lt;/td&gt;&lt;/tr&gt;&lt;tr class=other&gt;&lt;th width=50%&gt; Other values (234091) &lt;/th&gt;&lt;td width=50%&gt;&lt;div class=bar style=width:100.0% data-toggle=tooltip data-placement=right data-html=true data-delay=500&gt; 877249&amp;nbsp; &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;&lt;/div&gt;&lt;/div&gt;&lt;div class=&quot;col-sm-12 text-right&quot;&gt;&lt;button class=&quot;btn btn-default btn-sm&quot; data-toggle=collapse data-target=&quot;#bottom--8438619141185252187, #minifreqtable-8438619141185252187&quot; aria-expanded=true aria-controls=collapseExample&gt;Toggle details&lt;/button&gt;&lt;/div&gt;&lt;div id=bottom--8438619141185252187 class=collapse&gt;&lt;div class=&quot;row spacing&quot;&gt;&lt;ul class=&quot;nav nav-tabs&quot; role=tablist&gt;&lt;li role=presentation class=active&gt;&lt;a href=#-8438619141185252187bottom--8438619141185252187overview aria-controls=-8438619141185252187bottom--8438619141185252187overview role=tab data-toggle=tab&gt;Overview&lt;/a&gt;&lt;/li&gt;&lt;li role=presentation&gt;&lt;a href=#-8438619141185252187bottom--8438619141185252187string aria-controls=-8438619141185252187bottom--8438619141185252187string role=tab data-toggle=tab&gt;Categories&lt;/a&gt;&lt;/li&gt;&lt;/ul&gt;&lt;div class=tab-content&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12 active&quot; id=-8438619141185252187bottom--8438619141185252187overview&gt;&lt;div class=row&gt;&lt;div class=col-sm-6&gt;&lt;p class=h4&gt;Unique&lt;/p&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;Unique&lt;/th&gt;&lt;td&gt;144509 &lt;span class=&quot;badge pull-right&quot; style=color:#fff;background-color:#337ab7; title=&quot;The number of unique values (all values that occur exactly once in the dataset).&quot;&gt;?&lt;/span&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Unique (%)&lt;/th&gt;&lt;td&gt;16.4%&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div class=col-sm-6&gt;&lt;p class=h4&gt;Sample&lt;/p&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;1st row&lt;/th&gt;&lt;td&gt;[STEL] L, Furnas Centrais Eletricas S A (01030052263, 1557670), Nova Iguaçu/RJ&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;2nd row&lt;/th&gt;&lt;td&gt;[STEL] L, Companhia De Geração E Transmissão De Energia Elétrica Do Sul Do Brasil - Eletrobrás Cgt Eletrosul (50420217282, 1494686), Joinville/SC&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;3rd row&lt;/th&gt;&lt;td&gt;[STEL] L, Furnas Centrais Eletricas S A (01030052263, 1558412), Mogi das Cruzes/SP&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;4th row&lt;/th&gt;&lt;td&gt;[STEL] L, Furnas Centrais Eletricas S A (01030052263, 1557823), São Paulo/SP&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;5th row&lt;/th&gt;&lt;td&gt;[STEL] L, Furnas Centrais Eletricas S A (01030052263, 859761), Rio de Janeiro/RJ&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12&quot; id=-8438619141185252187bottom--8438619141185252187string&gt;&lt;div class=row&gt;&lt;div class=col-sm-12&gt;&lt;h4&gt;Common Values&lt;/h4&gt;&lt;table class=&quot;freq table table-hover table-striped&quot;&gt;&lt;thead&gt;&lt;tr&gt;&lt;td&gt;Value&lt;/td&gt;&lt;td&gt;Count&lt;/td&gt;&lt;td&gt;Frequency (%)&lt;/td&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1001758606), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1001758606), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;410&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002745745), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002745745), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;375&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002623429), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002623429), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;375&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002745567), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002745567), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;375&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002745656), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002745656), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;375&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002623445), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002623445), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;375&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002746148), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002746148), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;375&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002746180), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002746180), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;375&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002746229), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002746229), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;375&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002746385), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002746385), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;375&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002746482), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002746482), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;375&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002748531), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002748531), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;375&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002625502), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002625502), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;375&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002540965), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002540965), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002541040), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002541040), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002541490), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002541490), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002541511), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002541511), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002541589), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002541589), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002541597), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002541597), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002541627), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002541627), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002541643), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002541643), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002541686), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002541686), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002541015), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002541015), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1001948189), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1001948189), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002540930), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002540930), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002541775), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002541775), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002540914), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002540914), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002540876), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002540876), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002540809), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002540809), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002540795), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002540795), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002540485), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002540485), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002540272), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002540272), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002235305), Taquaraçu de Minas/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002235305), Taquaraçu de Minas/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002235291), Taquaraçu de Minas/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002235291), Taquaraçu de Minas/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002235283), Taquaraçu de Minas/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002235283), Taquaraçu de Minas/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002235267), Nova União/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002235267), Nova União/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002235259), Nova União/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002235259), Nova União/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002541724), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002541724), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002602480), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002602480), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002541805), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002541805), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1003871710), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1003871710), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1004040838), Santana do Riacho/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1004040838), Santana do Riacho/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1004039600), Santana do Riacho/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1004039600), Santana do Riacho/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1004020390), Santa Luzia/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1004020390), Santa Luzia/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1004019820), Rio Acima/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1004019820), Rio Acima/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1004017887), Raposos/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1004017887), Raposos/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1004015027), Nova Lima/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1004015027), Nova Lima/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1004010190), Nova Lima/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1004010190), Nova Lima/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1003951365), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1003951365), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1003944091), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1003944091), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1003874140), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1003874140), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002710135), Caeté/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002710135), Caeté/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002600518), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002600518), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002708777), Nova Lima/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002708777), Nova Lima/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002602537), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002602537), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002602529), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002602529), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002602502), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002602502), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002602499), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002602499), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002235224), Caeté/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002235224), Caeté/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002602464), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002602464), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002602448), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002602448), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002600550), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002600550), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002600534), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002600534), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002235240), Nova União/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002235240), Nova União/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002235160), Caeté/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002235160), Caeté/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1004062220), Santa Luzia/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1004062220), Santa Luzia/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209045), Vespasiano/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209045), Vespasiano/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209533), Diogo de Vasconcelos/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209533), Diogo de Vasconcelos/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209517), Diogo de Vasconcelos/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209517), Diogo de Vasconcelos/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209452), Mariana/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209452), Mariana/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209410), Mariana/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209410), Mariana/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209398), Mariana/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209398), Mariana/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209363), Itabirito/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209363), Itabirito/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209355), Itabirito/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209355), Itabirito/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209339), Itabirito/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209339), Itabirito/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209258), Ouro Preto/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209258), Ouro Preto/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209231), Ouro Preto/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209231), Ouro Preto/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209215), Ouro Preto/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209215), Ouro Preto/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209070), Vespasiano/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209070), Vespasiano/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209053), Vespasiano/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209053), Vespasiano/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002207913), Confins/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002207913), Confins/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209738), Ouro Preto/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209738), Ouro Preto/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002207905), Confins/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002207905), Confins/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002207727), Confins/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002207727), Confins/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002207387), Raposos/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002207387), Raposos/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1001967540), Vespasiano/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1001967540), Vespasiano/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1001967914), Nova Lima/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1001967914), Nova Lima/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1001967973), Nova Lima/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1001967973), Nova Lima/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1001968031), Nova Lima/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1001968031), Nova Lima/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1001970958), Nova Lima/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1001970958), Nova Lima/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1001970974), Nova Lima/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1001970974), Nova Lima/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1001971075), Nova Lima/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1001971075), Nova Lima/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1001971091), Nova Lima/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1001971091), Nova Lima/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1001971300), Nova Lima/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1001971300), Nova Lima/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1001989233), Belo Horizonte/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1001989233), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209550), Diogo de Vasconcelos/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209550), Diogo de Vasconcelos/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209746), Ouro Preto/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002209746), Ouro Preto/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002235151), Caeté/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002235151), Caeté/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002233787), Ouro Preto/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002233787), Ouro Preto/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=&quot;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002234848), Caeté/MG&quot;&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002234848), Caeté/MG&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class=other&gt;&lt;td title=&quot;Other values (233996)&quot;&gt;Other values (233996)&lt;/td&gt;&lt;td&gt;842929&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt; 95.9% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;div class=&quot;row spacing&quot;&gt;&lt;a class=&quot;anchor-pos anchor-pos-variable&quot; id=pp_var_-8827081728071359025&gt;&lt;/a&gt;&lt;div class=variable&gt;&lt;div class=col-sm-3&gt;&lt;p class=h4 title=Service&gt;&lt;a href=#pp_var_-8827081728071359025&gt;Service&lt;/a&gt;&lt;br&gt;&lt;small&gt;Categorical&lt;/small&gt;&lt;/p&gt;&lt;p class=variable-description&gt;&lt;/p&gt;&lt;/div&gt;&lt;div class=col-sm-3&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;Distinct&lt;/th&gt;&lt;td&gt;44&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Distinct (%)&lt;/th&gt;&lt;td&gt;&lt; 0.1%&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Missing&lt;/th&gt;&lt;td&gt;0&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Missing (%)&lt;/th&gt;&lt;td&gt;0.0%&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Memory size&lt;/th&gt;&lt;td&gt;860.1 KiB&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div class=col-sm-6&gt;&lt;div class=&quot;col-sm- collapse in&quot; id=minifreqtable&gt;&lt;table class=&quot;mini freq&quot;&gt;&lt;tr class&gt;&lt;th width=50%&gt; 019 &lt;/th&gt;&lt;td width=50%&gt;&lt;div class=bar style=width:100.0% data-toggle=tooltip data-placement=right data-html=true data-delay=500&gt; 600097&amp;nbsp; &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;th width=50%&gt; 053 &lt;/th&gt;&lt;td width=50%&gt;&lt;div class=bar style=width:22.5% data-toggle=tooltip data-placement=right data-html=true data-delay=500&gt; 134785&amp;nbsp; &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;th width=50%&gt; 046 &lt;/th&gt;&lt;td width=50%&gt;&lt;div class=bar style=width:5.9% data-toggle=tooltip data-placement=right data-html=true data-delay=500&gt; &amp;nbsp; &lt;/div&gt; 35521 &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;th width=50%&gt; 604 &lt;/th&gt;&lt;td width=50%&gt;&lt;div class=bar style=width:2.8% data-toggle=tooltip data-placement=right data-html=true data-delay=500&gt; &amp;nbsp; &lt;/div&gt; 16858 &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;th width=50%&gt; 011 &lt;/th&gt;&lt;td width=50%&gt;&lt;div class=bar style=width:2.6% data-toggle=tooltip data-placement=right data-html=true data-delay=500&gt; &amp;nbsp; &lt;/div&gt; 15473 &lt;/td&gt;&lt;/tr&gt;&lt;tr class=other&gt;&lt;th width=50%&gt; Other values (39) &lt;/th&gt;&lt;td width=50%&gt;&lt;div class=bar style=width:12.7% data-toggle=tooltip data-placement=right data-html=true data-delay=500&gt; 76425&amp;nbsp; &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;&lt;/div&gt;&lt;/div&gt;&lt;div class=&quot;col-sm-12 text-right&quot;&gt;&lt;button class=&quot;btn btn-default btn-sm&quot; data-toggle=collapse data-target=&quot;#bottom--8827081728071359025, #minifreqtable-8827081728071359025&quot; aria-expanded=true aria-controls=collapseExample&gt;Toggle details&lt;/button&gt;&lt;/div&gt;&lt;div id=bottom--8827081728071359025 class=collapse&gt;&lt;div class=&quot;row spacing&quot;&gt;&lt;ul class=&quot;nav nav-tabs&quot; role=tablist&gt;&lt;li role=presentation class=active&gt;&lt;a href=#-8827081728071359025bottom--8827081728071359025overview aria-controls=-8827081728071359025bottom--8827081728071359025overview role=tab data-toggle=tab&gt;Overview&lt;/a&gt;&lt;/li&gt;&lt;li role=presentation&gt;&lt;a href=#-8827081728071359025bottom--8827081728071359025string aria-controls=-8827081728071359025bottom--8827081728071359025string role=tab data-toggle=tab&gt;Categories&lt;/a&gt;&lt;/li&gt;&lt;/ul&gt;&lt;div class=tab-content&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12 active&quot; id=-8827081728071359025bottom--8827081728071359025overview&gt;&lt;div class=row&gt;&lt;div class=col-sm-6&gt;&lt;p class=h4&gt;Unique&lt;/p&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;Unique&lt;/th&gt;&lt;td&gt;0 &lt;span class=&quot;badge pull-right&quot; style=color:#fff;background-color:#337ab7; title=&quot;The number of unique values (all values that occur exactly once in the dataset).&quot;&gt;?&lt;/span&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Unique (%)&lt;/th&gt;&lt;td&gt;0.0%&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div class=col-sm-6&gt;&lt;p class=h4&gt;Sample&lt;/p&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;1st row&lt;/th&gt;&lt;td&gt;019&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;2nd row&lt;/th&gt;&lt;td&gt;019&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;3rd row&lt;/th&gt;&lt;td&gt;019&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;4th row&lt;/th&gt;&lt;td&gt;019&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;5th row&lt;/th&gt;&lt;td&gt;019&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12&quot; id=-8827081728071359025bottom--8827081728071359025string&gt;&lt;div class=row&gt;&lt;div class=col-sm-12&gt;&lt;h4&gt;Common Values&lt;/h4&gt;&lt;table class=&quot;freq table table-hover table-striped&quot;&gt;&lt;thead&gt;&lt;tr&gt;&lt;td&gt;Value&lt;/td&gt;&lt;td&gt;Count&lt;/td&gt;&lt;td&gt;Frequency (%)&lt;/td&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr class&gt;&lt;td title=019&gt;019&lt;/td&gt;&lt;td&gt;600097&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt; 68.3% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=053&gt;053&lt;/td&gt;&lt;td&gt;134785&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:22.5%&gt; &amp;nbsp; &lt;/div&gt; 15.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=046&gt;046&lt;/td&gt;&lt;td&gt;35521&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:5.9%&gt; &amp;nbsp; &lt;/div&gt; 4.0% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=604&gt;604&lt;/td&gt;&lt;td&gt;16858&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:2.8%&gt; &amp;nbsp; &lt;/div&gt; 1.9% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=011&gt;011&lt;/td&gt;&lt;td&gt;15473&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:2.6%&gt; &amp;nbsp; &lt;/div&gt; 1.8% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=023&gt;023&lt;/td&gt;&lt;td&gt;14234&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:2.4%&gt; &amp;nbsp; &lt;/div&gt; 1.6% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=801&gt;801&lt;/td&gt;&lt;td&gt;14182&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:2.4%&gt; &amp;nbsp; &lt;/div&gt; 1.6% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=800&gt;800&lt;/td&gt;&lt;td&gt;9321&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:1.6%&gt; &amp;nbsp; &lt;/div&gt; 1.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=125&gt;125&lt;/td&gt;&lt;td&gt;5537&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.9%&gt; &amp;nbsp; &lt;/div&gt; 0.6% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=231&gt;231&lt;/td&gt;&lt;td&gt;4921&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.8%&gt; &amp;nbsp; &lt;/div&gt; 0.6% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=035&gt;035&lt;/td&gt;&lt;td&gt;4534&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.8%&gt; &amp;nbsp; &lt;/div&gt; 0.5% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=230&gt;230&lt;/td&gt;&lt;td&gt;4184&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.7%&gt; &amp;nbsp; &lt;/div&gt; 0.5% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=507&gt;507&lt;/td&gt;&lt;td&gt;2295&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.4%&gt; &amp;nbsp; &lt;/div&gt; 0.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=251&gt;251&lt;/td&gt;&lt;td&gt;2293&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.4%&gt; &amp;nbsp; &lt;/div&gt; 0.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-1&gt;-1&lt;/td&gt;&lt;td&gt;1892&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=728&gt;728&lt;/td&gt;&lt;td&gt;1670&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=020&gt;020&lt;/td&gt;&lt;td&gt;1443&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=252&gt;252&lt;/td&gt;&lt;td&gt;1375&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=124&gt;124&lt;/td&gt;&lt;td&gt;1334&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=205&gt;205&lt;/td&gt;&lt;td&gt;1089&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=078&gt;078&lt;/td&gt;&lt;td&gt;973&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=017&gt;017&lt;/td&gt;&lt;td&gt;919&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=247&gt;247&lt;/td&gt;&lt;td&gt;638&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=079&gt;079&lt;/td&gt;&lt;td&gt;536&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=064&gt;064&lt;/td&gt;&lt;td&gt;522&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=034&gt;034&lt;/td&gt;&lt;td&gt;511&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=253&gt;253&lt;/td&gt;&lt;td&gt;464&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=033&gt;033&lt;/td&gt;&lt;td&gt;375&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=060&gt;060&lt;/td&gt;&lt;td&gt;343&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=108&gt;108&lt;/td&gt;&lt;td&gt;181&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=012&gt;012&lt;/td&gt;&lt;td&gt;163&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=248&gt;248&lt;/td&gt;&lt;td&gt;146&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=051&gt;051&lt;/td&gt;&lt;td&gt;96&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=805&gt;805&lt;/td&gt;&lt;td&gt;72&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=027&gt;027&lt;/td&gt;&lt;td&gt;40&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=255&gt;255&lt;/td&gt;&lt;td&gt;29&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=175&gt;175&lt;/td&gt;&lt;td&gt;26&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=167&gt;167&lt;/td&gt;&lt;td&gt;21&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=820&gt;820&lt;/td&gt;&lt;td&gt;21&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=256&gt;256&lt;/td&gt;&lt;td&gt;19&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=029&gt;029&lt;/td&gt;&lt;td&gt;10&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=026&gt;026&lt;/td&gt;&lt;td&gt;9&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=132&gt;132&lt;/td&gt;&lt;td&gt;5&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=015&gt;015&lt;/td&gt;&lt;td&gt;2&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;div class=&quot;row spacing&quot;&gt;&lt;a class=&quot;anchor-pos anchor-pos-variable&quot; id=pp_var_3243557442294903904&gt;&lt;/a&gt;&lt;div class=variable&gt;&lt;div class=col-sm-3&gt;&lt;p class=h4 title=Station&gt;&lt;a href=#pp_var_3243557442294903904&gt;Station&lt;/a&gt;&lt;br&gt;&lt;small&gt;Categorical&lt;/small&gt;&lt;/p&gt;&lt;code&gt;HIGH CARDINALITY&lt;/code&gt;&lt;br&gt;&lt;p class=variable-description&gt;&lt;/p&gt;&lt;/div&gt;&lt;div class=col-sm-3&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr class=alert&gt;&lt;th&gt;Distinct&lt;/th&gt;&lt;td&gt;226569&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Distinct (%)&lt;/th&gt;&lt;td&gt;25.8%&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Missing&lt;/th&gt;&lt;td&gt;0&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Missing (%)&lt;/th&gt;&lt;td&gt;0.0%&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Memory size&lt;/th&gt;&lt;td&gt;13.1 MiB&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div class=col-sm-6&gt;&lt;div class=&quot;col-sm- collapse in&quot; id=minifreqtable&gt;&lt;table class=&quot;mini freq&quot;&gt;&lt;tr class&gt;&lt;th width=50%&gt; -1 &lt;/th&gt;&lt;td width=50%&gt;&lt;div class=bar style=width:0.9% data-toggle=tooltip data-placement=right data-html=true data-delay=500&gt; &amp;nbsp; &lt;/div&gt; 7833 &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;th width=50%&gt; 1001758606 &lt;/th&gt;&lt;td width=50%&gt;&lt;div class=bar style=width:0.0% data-toggle=tooltip data-placement=right data-html=true data-delay=500&gt; &amp;nbsp; &lt;/div&gt; 410 &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;th width=50%&gt; 1002748531 &lt;/th&gt;&lt;td width=50%&gt;&lt;div class=bar style=width:0.0% data-toggle=tooltip data-placement=right data-html=true data-delay=500&gt; &amp;nbsp; &lt;/div&gt; 375 &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;th width=50%&gt; 1002746482 &lt;/th&gt;&lt;td width=50%&gt;&lt;div class=bar style=width:0.0% data-toggle=tooltip data-placement=right data-html=true data-delay=500&gt; &amp;nbsp; &lt;/div&gt; 375 &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;th width=50%&gt; 1002746385 &lt;/th&gt;&lt;td width=50%&gt;&lt;div class=bar style=width:0.0% data-toggle=tooltip data-placement=right data-html=true data-delay=500&gt; &amp;nbsp; &lt;/div&gt; 375 &lt;/td&gt;&lt;/tr&gt;&lt;tr class=other&gt;&lt;th width=50%&gt; Other values (226564) &lt;/th&gt;&lt;td width=50%&gt;&lt;div class=bar style=width:100.0% data-toggle=tooltip data-placement=right data-html=true data-delay=500&gt; 869791&amp;nbsp; &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;&lt;/div&gt;&lt;/div&gt;&lt;div class=&quot;col-sm-12 text-right&quot;&gt;&lt;button class=&quot;btn btn-default btn-sm&quot; data-toggle=collapse data-target=&quot;#bottom-3243557442294903904, #minifreqtable3243557442294903904&quot; aria-expanded=true aria-controls=collapseExample&gt;Toggle details&lt;/button&gt;&lt;/div&gt;&lt;div id=bottom-3243557442294903904 class=collapse&gt;&lt;div class=&quot;row spacing&quot;&gt;&lt;ul class=&quot;nav nav-tabs&quot; role=tablist&gt;&lt;li role=presentation class=active&gt;&lt;a href=#3243557442294903904bottom-3243557442294903904overview aria-controls=3243557442294903904bottom-3243557442294903904overview role=tab data-toggle=tab&gt;Overview&lt;/a&gt;&lt;/li&gt;&lt;li role=presentation&gt;&lt;a href=#3243557442294903904bottom-3243557442294903904string aria-controls=3243557442294903904bottom-3243557442294903904string role=tab data-toggle=tab&gt;Categories&lt;/a&gt;&lt;/li&gt;&lt;/ul&gt;&lt;div class=tab-content&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12 active&quot; id=3243557442294903904bottom-3243557442294903904overview&gt;&lt;div class=row&gt;&lt;div class=col-sm-6&gt;&lt;p class=h4&gt;Unique&lt;/p&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;Unique&lt;/th&gt;&lt;td&gt;136946 &lt;span class=&quot;badge pull-right&quot; style=color:#fff;background-color:#337ab7; title=&quot;The number of unique values (all values that occur exactly once in the dataset).&quot;&gt;?&lt;/span&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Unique (%)&lt;/th&gt;&lt;td&gt;15.6%&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div class=col-sm-6&gt;&lt;p class=h4&gt;Sample&lt;/p&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;1st row&lt;/th&gt;&lt;td&gt;1557670&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;2nd row&lt;/th&gt;&lt;td&gt;1494686&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;3rd row&lt;/th&gt;&lt;td&gt;1558412&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;4th row&lt;/th&gt;&lt;td&gt;1557823&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;5th row&lt;/th&gt;&lt;td&gt;859761&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12&quot; id=3243557442294903904bottom-3243557442294903904string&gt;&lt;div class=row&gt;&lt;div class=col-sm-12&gt;&lt;h4&gt;Common Values&lt;/h4&gt;&lt;table class=&quot;freq table table-hover table-striped&quot;&gt;&lt;thead&gt;&lt;tr&gt;&lt;td&gt;Value&lt;/td&gt;&lt;td&gt;Count&lt;/td&gt;&lt;td&gt;Frequency (%)&lt;/td&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr class&gt;&lt;td title=-1&gt;-1&lt;/td&gt;&lt;td&gt;7833&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.9%&gt; &amp;nbsp; &lt;/div&gt; 0.9% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001758606&gt;1001758606&lt;/td&gt;&lt;td&gt;410&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002748531&gt;1002748531&lt;/td&gt;&lt;td&gt;375&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002746482&gt;1002746482&lt;/td&gt;&lt;td&gt;375&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002746385&gt;1002746385&lt;/td&gt;&lt;td&gt;375&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002746229&gt;1002746229&lt;/td&gt;&lt;td&gt;375&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002746180&gt;1002746180&lt;/td&gt;&lt;td&gt;375&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002623429&gt;1002623429&lt;/td&gt;&lt;td&gt;375&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002623445&gt;1002623445&lt;/td&gt;&lt;td&gt;375&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002625502&gt;1002625502&lt;/td&gt;&lt;td&gt;375&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002745745&gt;1002745745&lt;/td&gt;&lt;td&gt;375&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002745656&gt;1002745656&lt;/td&gt;&lt;td&gt;375&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002745567&gt;1002745567&lt;/td&gt;&lt;td&gt;375&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002746148&gt;1002746148&lt;/td&gt;&lt;td&gt;375&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002541805&gt;1002541805&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002541775&gt;1002541775&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002541511&gt;1002541511&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002541490&gt;1002541490&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001750923&gt;1001750923&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001750931&gt;1001750931&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001750940&gt;1001750940&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001750982&gt;1001750982&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001751008&gt;1001751008&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001751059&gt;1001751059&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001751105&gt;1001751105&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001751350&gt;1001751350&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001751431&gt;1001751431&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001751555&gt;1001751555&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001751644&gt;1001751644&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001751792&gt;1001751792&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001751890&gt;1001751890&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002541589&gt;1002541589&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002541597&gt;1002541597&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002541627&gt;1002541627&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002541643&gt;1002541643&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002541724&gt;1002541724&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1003871710&gt;1003871710&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002541686&gt;1002541686&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1003874140&gt;1003874140&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1003944091&gt;1003944091&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1003951365&gt;1003951365&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1004010190&gt;1004010190&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1004039600&gt;1004039600&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1004679723&gt;1004679723&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001752373&gt;1001752373&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1004015027&gt;1004015027&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1004017887&gt;1004017887&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1004019820&gt;1004019820&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1004020390&gt;1004020390&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001752063&gt;1001752063&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002540914&gt;1002540914&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001752411&gt;1001752411&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002541040&gt;1002541040&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001757839&gt;1001757839&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001758134&gt;1001758134&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001758282&gt;1001758282&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001758533&gt;1001758533&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001758703&gt;1001758703&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001758835&gt;1001758835&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001758851&gt;1001758851&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001759068&gt;1001759068&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1004879714&gt;1004879714&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001759483&gt;1001759483&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1004884203&gt;1004884203&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001760279&gt;1001760279&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001760430&gt;1001760430&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001760490&gt;1001760490&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001760597&gt;1001760597&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001757740&gt;1001757740&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001753116&gt;1001753116&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001753043&gt;1001753043&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001752527&gt;1001752527&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002541015&gt;1002541015&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002540965&gt;1002540965&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002540930&gt;1002540930&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001752462&gt;1001752462&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1004040838&gt;1004040838&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002540876&gt;1002540876&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002540809&gt;1002540809&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001752993&gt;1001752993&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002540795&gt;1002540795&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002540485&gt;1002540485&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001752594&gt;1001752594&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002540272&gt;1002540272&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001752829&gt;1001752829&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1001752950&gt;1001752950&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1004656847&gt;1004656847&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1002602464&gt;1002602464&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1004652531&gt;1004652531&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1004131841&gt;1004131841&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1008022125&gt;1008022125&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1008022150&gt;1008022150&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1008026198&gt;1008026198&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1008026252&gt;1008026252&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1008026260&gt;1008026260&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1008026287&gt;1008026287&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1008026317&gt;1008026317&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1008026325&gt;1008026325&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1008026368&gt;1008026368&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1008028026&gt;1008028026&lt;/td&gt;&lt;td&gt;360&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class=other&gt;&lt;td title=&quot;Other values (226469)&quot;&gt;Other values (226469)&lt;/td&gt;&lt;td&gt;835456&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt; 95.0% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;div class=&quot;row spacing&quot;&gt;&lt;a class=&quot;anchor-pos anchor-pos-variable&quot; id=pp_var_-3991132923749349832&gt;&lt;/a&gt;&lt;div class=variable&gt;&lt;div class=col-sm-3&gt;&lt;p class=h4 title=Class&gt;&lt;a href=#pp_var_-3991132923749349832&gt;Class&lt;/a&gt;&lt;br&gt;&lt;small&gt;Categorical&lt;/small&gt;&lt;/p&gt;&lt;code&gt;HIGH CARDINALITY&lt;/code&gt;&lt;br&gt;&lt;code&gt;MISSING&lt;/code&gt;&lt;br&gt;&lt;p class=variable-description&gt;&lt;/p&gt;&lt;/div&gt;&lt;div class=col-sm-3&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr class=alert&gt;&lt;th&gt;Distinct&lt;/th&gt;&lt;td&gt;102&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Distinct (%)&lt;/th&gt;&lt;td&gt;&lt; 0.1%&lt;/td&gt;&lt;/tr&gt;&lt;tr class=alert&gt;&lt;th&gt;Missing&lt;/th&gt;&lt;td&gt;59068&lt;/td&gt;&lt;/tr&gt;&lt;tr class=alert&gt;&lt;th&gt;Missing (%)&lt;/th&gt;&lt;td&gt;6.7%&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Memory size&lt;/th&gt;&lt;td&gt;863.5 KiB&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div class=col-sm-6&gt;&lt;div class=&quot;col-sm- collapse in&quot; id=minifreqtable&gt;&lt;table class=&quot;mini freq&quot;&gt;&lt;tr class&gt;&lt;th width=50%&gt; F3E &lt;/th&gt;&lt;td width=50%&gt;&lt;div class=bar style=width:100.0% data-toggle=tooltip data-placement=right data-html=true data-delay=500&gt; 177885&amp;nbsp; &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;th width=50%&gt; F1W &lt;/th&gt;&lt;td width=50%&gt;&lt;div class=bar style=width:86.8% data-toggle=tooltip data-placement=right data-html=true data-delay=500&gt; 154475&amp;nbsp; &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;th width=50%&gt; D7W &lt;/th&gt;&lt;td width=50%&gt;&lt;div class=bar style=width:84.7% data-toggle=tooltip data-placement=right data-html=true data-delay=500&gt; 150679&amp;nbsp; &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;th width=50%&gt; F1E &lt;/th&gt;&lt;td width=50%&gt;&lt;div class=bar style=width:62.7% data-toggle=tooltip data-placement=right data-html=true data-delay=500&gt; 111601&amp;nbsp; &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;th width=50%&gt; G7W &lt;/th&gt;&lt;td width=50%&gt;&lt;div class=bar style=width:34.4% data-toggle=tooltip data-placement=right data-html=true data-delay=500&gt; 61174&amp;nbsp; &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class=other&gt;&lt;th width=50%&gt; Other values (97) &lt;/th&gt;&lt;td width=50%&gt;&lt;div class=bar style=width:92.4% data-toggle=tooltip data-placement=right data-html=true data-delay=500&gt; 164277&amp;nbsp; &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;&lt;/div&gt;&lt;/div&gt;&lt;div class=&quot;col-sm-12 text-right&quot;&gt;&lt;button class=&quot;btn btn-default btn-sm&quot; data-toggle=collapse data-target=&quot;#bottom--3991132923749349832, #minifreqtable-3991132923749349832&quot; aria-expanded=true aria-controls=collapseExample&gt;Toggle details&lt;/button&gt;&lt;/div&gt;&lt;div id=bottom--3991132923749349832 class=collapse&gt;&lt;div class=&quot;row spacing&quot;&gt;&lt;ul class=&quot;nav nav-tabs&quot; role=tablist&gt;&lt;li role=presentation class=active&gt;&lt;a href=#-3991132923749349832bottom--3991132923749349832overview aria-controls=-3991132923749349832bottom--3991132923749349832overview role=tab data-toggle=tab&gt;Overview&lt;/a&gt;&lt;/li&gt;&lt;li role=presentation&gt;&lt;a href=#-3991132923749349832bottom--3991132923749349832string aria-controls=-3991132923749349832bottom--3991132923749349832string role=tab data-toggle=tab&gt;Categories&lt;/a&gt;&lt;/li&gt;&lt;/ul&gt;&lt;div class=tab-content&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12 active&quot; id=-3991132923749349832bottom--3991132923749349832overview&gt;&lt;div class=row&gt;&lt;div class=col-sm-6&gt;&lt;p class=h4&gt;Unique&lt;/p&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;Unique&lt;/th&gt;&lt;td&gt;9 &lt;span class=&quot;badge pull-right&quot; style=color:#fff;background-color:#337ab7; title=&quot;The number of unique values (all values that occur exactly once in the dataset).&quot;&gt;?&lt;/span&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Unique (%)&lt;/th&gt;&lt;td&gt;&lt; 0.1%&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div class=col-sm-6&gt;&lt;p class=h4&gt;Sample&lt;/p&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;1st row&lt;/th&gt;&lt;td&gt;J9E&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;2nd row&lt;/th&gt;&lt;td&gt;R3E&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;3rd row&lt;/th&gt;&lt;td&gt;J3E&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;4th row&lt;/th&gt;&lt;td&gt;J3E&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;5th row&lt;/th&gt;&lt;td&gt;J3E&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12&quot; id=-3991132923749349832bottom--3991132923749349832string&gt;&lt;div class=row&gt;&lt;div class=col-sm-12&gt;&lt;h4&gt;Common Values&lt;/h4&gt;&lt;table class=&quot;freq table table-hover table-striped&quot;&gt;&lt;thead&gt;&lt;tr&gt;&lt;td&gt;Value&lt;/td&gt;&lt;td&gt;Count&lt;/td&gt;&lt;td&gt;Frequency (%)&lt;/td&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr class&gt;&lt;td title=F3E&gt;F3E&lt;/td&gt;&lt;td&gt;177885&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt; 20.2% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=F1W&gt;F1W&lt;/td&gt;&lt;td&gt;154475&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:86.8%&gt; 17.6% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=D7W&gt;D7W&lt;/td&gt;&lt;td&gt;150679&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:84.7%&gt; 17.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=F1E&gt;F1E&lt;/td&gt;&lt;td&gt;111601&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:62.7%&gt; 12.7% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=G7W&gt;G7W&lt;/td&gt;&lt;td&gt;61174&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:34.4%&gt; &amp;nbsp; &lt;/div&gt; 7.0% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=F1D&gt;F1D&lt;/td&gt;&lt;td&gt;60671&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:34.1%&gt; &amp;nbsp; &lt;/div&gt; 6.9% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=G1W&gt;G1W&lt;/td&gt;&lt;td&gt;47308&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:26.6%&gt; &amp;nbsp; &lt;/div&gt; 5.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=J3E&gt;J3E&lt;/td&gt;&lt;td&gt;5905&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:3.3%&gt; &amp;nbsp; &lt;/div&gt; 0.7% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=M7W&gt;M7W&lt;/td&gt;&lt;td&gt;5710&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:3.2%&gt; &amp;nbsp; &lt;/div&gt; 0.6% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=G3E&gt;G3E&lt;/td&gt;&lt;td&gt;5705&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:3.2%&gt; &amp;nbsp; &lt;/div&gt; 0.6% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=A3E&gt;A3E&lt;/td&gt;&lt;td&gt;4683&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:2.6%&gt; &amp;nbsp; &lt;/div&gt; 0.5% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=F2D&gt;F2D&lt;/td&gt;&lt;td&gt;3900&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:2.2%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=F7D&gt;F7D&lt;/td&gt;&lt;td&gt;3678&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:2.1%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=F3D&gt;F3D&lt;/td&gt;&lt;td&gt;3248&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:1.8%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=F3A&gt;F3A&lt;/td&gt;&lt;td&gt;2138&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:1.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=FXE&gt;FXE&lt;/td&gt;&lt;td&gt;2111&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:1.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=G1D&gt;G1D&lt;/td&gt;&lt;td&gt;1934&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:1.1%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=F7W&gt;F7W&lt;/td&gt;&lt;td&gt;1821&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:1.0%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=Q7W&gt;Q7W&lt;/td&gt;&lt;td&gt;1806&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:1.0%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=G1E&gt;G1E&lt;/td&gt;&lt;td&gt;1713&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:1.0%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=D1D&gt;D1D&lt;/td&gt;&lt;td&gt;1379&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.8%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=D7D&gt;D7D&lt;/td&gt;&lt;td&gt;1258&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.7%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=D1W&gt;D1W&lt;/td&gt;&lt;td&gt;1152&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=X9W&gt;X9W&lt;/td&gt;&lt;td&gt;1069&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=F7E&gt;F7E&lt;/td&gt;&lt;td&gt;823&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.5%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=C3F&gt;C3F&lt;/td&gt;&lt;td&gt;723&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.4%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=F8E&gt;F8E&lt;/td&gt;&lt;td&gt;621&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=F8W&gt;F8W&lt;/td&gt;&lt;td&gt;591&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=F3F&gt;F3F&lt;/td&gt;&lt;td&gt;474&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=V1X&gt;V1X&lt;/td&gt;&lt;td&gt;464&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=F2E&gt;F2E&lt;/td&gt;&lt;td&gt;386&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=FXD&gt;FXD&lt;/td&gt;&lt;td&gt;381&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=F9W&gt;F9W&lt;/td&gt;&lt;td&gt;325&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=J8D&gt;J8D&lt;/td&gt;&lt;td&gt;223&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=G2B&gt;G2B&lt;/td&gt;&lt;td&gt;199&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=V7W&gt;V7W&lt;/td&gt;&lt;td&gt;192&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=J9E&gt;J9E&lt;/td&gt;&lt;td&gt;172&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=R9W&gt;R9W&lt;/td&gt;&lt;td&gt;169&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=A3F&gt;A3F&lt;/td&gt;&lt;td&gt;163&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=F3W&gt;F3W&lt;/td&gt;&lt;td&gt;150&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=G7D&gt;G7D&lt;/td&gt;&lt;td&gt;80&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=FXW&gt;FXW&lt;/td&gt;&lt;td&gt;79&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=A2A&gt;A2A&lt;/td&gt;&lt;td&gt;79&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=J9W&gt;J9W&lt;/td&gt;&lt;td&gt;58&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=A1D&gt;A1D&lt;/td&gt;&lt;td&gt;55&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=J3W&gt;J3W&lt;/td&gt;&lt;td&gt;46&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=A1A&gt;A1A&lt;/td&gt;&lt;td&gt;45&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=N0N&gt;N0N&lt;/td&gt;&lt;td&gt;41&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=K7W&gt;K7W&lt;/td&gt;&lt;td&gt;37&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=F2A&gt;F2A&lt;/td&gt;&lt;td&gt;36&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=J3D&gt;J3D&lt;/td&gt;&lt;td&gt;32&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=F9X&gt;F9X&lt;/td&gt;&lt;td&gt;31&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=R3E&gt;R3E&lt;/td&gt;&lt;td&gt;28&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=A3N&gt;A3N&lt;/td&gt;&lt;td&gt;26&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=A9W&gt;A9W&lt;/td&gt;&lt;td&gt;25&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=W7W&gt;W7W&lt;/td&gt;&lt;td&gt;24&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=X7W&gt;X7W&lt;/td&gt;&lt;td&gt;21&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=P0N&gt;P0N&lt;/td&gt;&lt;td&gt;21&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=M1A&gt;M1A&lt;/td&gt;&lt;td&gt;20&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=G9W&gt;G9W&lt;/td&gt;&lt;td&gt;18&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=F8F&gt;F8F&lt;/td&gt;&lt;td&gt;16&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=J2D&gt;J2D&lt;/td&gt;&lt;td&gt;14&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=GXD&gt;GXD&lt;/td&gt;&lt;td&gt;14&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=G7E&gt;G7E&lt;/td&gt;&lt;td&gt;14&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=F1B&gt;F1B&lt;/td&gt;&lt;td&gt;13&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=G7F&gt;G7F&lt;/td&gt;&lt;td&gt;12&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=F9F&gt;F9F&lt;/td&gt;&lt;td&gt;12&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=J9D&gt;J9D&lt;/td&gt;&lt;td&gt;12&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=P1D&gt;P1D&lt;/td&gt;&lt;td&gt;10&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=B9W&gt;B9W&lt;/td&gt;&lt;td&gt;9&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=D2W&gt;D2W&lt;/td&gt;&lt;td&gt;8&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=N0D&gt;N0D&lt;/td&gt;&lt;td&gt;8&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=X9E&gt;X9E&lt;/td&gt;&lt;td&gt;7&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=M9W&gt;M9W&lt;/td&gt;&lt;td&gt;7&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=M1X&gt;M1X&lt;/td&gt;&lt;td&gt;6&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=A2B&gt;A2B&lt;/td&gt;&lt;td&gt;6&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=F8X&gt;F8X&lt;/td&gt;&lt;td&gt;6&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=GXW&gt;GXW&lt;/td&gt;&lt;td&gt;6&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=G8W&gt;G8W&lt;/td&gt;&lt;td&gt;6&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=FXX&gt;FXX&lt;/td&gt;&lt;td&gt;4&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=J7W&gt;J7W&lt;/td&gt;&lt;td&gt;4&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=D9W&gt;D9W&lt;/td&gt;&lt;td&gt;4&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=J8W&gt;J8W&lt;/td&gt;&lt;td&gt;3&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=P7E&gt;P7E&lt;/td&gt;&lt;td&gt;2&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=A3X&gt;A3X&lt;/td&gt;&lt;td&gt;2&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=F7A&gt;F7A&lt;/td&gt;&lt;td&gt;2&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=F2B&gt;F2B&lt;/td&gt;&lt;td&gt;2&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=A2N&gt;A2N&lt;/td&gt;&lt;td&gt;2&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=PXX&gt;PXX&lt;/td&gt;&lt;td&gt;2&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=J8E&gt;J8E&lt;/td&gt;&lt;td&gt;2&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=G2D&gt;G2D&lt;/td&gt;&lt;td&gt;2&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=D7E&gt;D7E&lt;/td&gt;&lt;td&gt;2&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=F9D&gt;F9D&lt;/td&gt;&lt;td&gt;2&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=P7D&gt;P7D&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=A3B&gt;A3B&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=F0W&gt;F0W&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=RXW&gt;RXW&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=A2E&gt;A2E&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=F3X&gt;F3X&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=K9W&gt;K9W&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class=other&gt;&lt;td title=&quot;Other values (2)&quot;&gt;Other values (2)&lt;/td&gt;&lt;td&gt;2&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class=missing&gt;&lt;td title=(Missing)&gt;(Missing)&lt;/td&gt;&lt;td&gt;59068&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:33.2%&gt; &amp;nbsp; &lt;/div&gt; 6.7% &lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;div class=&quot;row spacing&quot;&gt;&lt;a class=&quot;anchor-pos anchor-pos-variable&quot; id=pp_var_8124034662335410336&gt;&lt;/a&gt;&lt;div class=variable&gt;&lt;div class=col-sm-3&gt;&lt;p class=h4 title=BW&gt;&lt;a href=#pp_var_8124034662335410336&gt;BW&lt;/a&gt;&lt;br&gt;&lt;small&gt;Real number (&amp;Ropf;)&lt;/small&gt;&lt;/p&gt;&lt;code&gt;SKEWED&lt;/code&gt;&lt;br&gt;&lt;p class=variable-description&gt;&lt;/p&gt;&lt;/div&gt;&lt;div class=col-sm-3&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;Distinct&lt;/th&gt;&lt;td&gt;353&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Distinct (%)&lt;/th&gt;&lt;td&gt;&lt; 0.1%&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Missing&lt;/th&gt;&lt;td&gt;1892&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Missing (%)&lt;/th&gt;&lt;td&gt;0.2%&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Infinite&lt;/th&gt;&lt;td&gt;0&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Infinite (%)&lt;/th&gt;&lt;td&gt;0.0%&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Mean&lt;/th&gt;&lt;td&gt;8157.950919&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div class=col-sm-3&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;Minimum&lt;/th&gt;&lt;td&gt;-1&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Maximum&lt;/th&gt;&lt;td&gt;21800000&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Zeros&lt;/th&gt;&lt;td&gt;0&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Zeros (%)&lt;/th&gt;&lt;td&gt;0.0%&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Negative&lt;/th&gt;&lt;td&gt;22602&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Negative (%)&lt;/th&gt;&lt;td&gt;2.6%&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Memory size&lt;/th&gt;&lt;td&gt;3.4 MiB&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div class=col-sm-3&gt;&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot; standalone=&quot;no&quot;?&gt;&lt;!DOCTYPE svg class=&quot;img-responsive center-img&quot;PUBLIC &quot;-//W3C//DTD SVG 1.1//EN&quot;
  &quot;http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd&quot;&gt;&lt;svg class=&quot;img-responsive center-img&quot; xmlns:xlink=http://www.w3.org/1999/xlink width=216pt height=162pt viewbox=&quot;0 0 216 162&quot; xmlns=http://www.w3.org/2000/svg version=1.1&gt;&lt;metadata&gt;&lt;rdf:rdf xmlns:dc=http://purl.org/dc/elements/1.1/ xmlns:cc=http://creativecommons.org/ns# xmlns:rdf=http://www.w3.org/1999/02/22-rdf-syntax-ns#&gt;&lt;cc:work&gt;&lt;dc:type rdf:resource=http://purl.org/dc/dcmitype/StillImage /&gt;&lt;dc:date&gt;2022-07-12T13:06:41.822402&lt;/dc:date&gt;&lt;dc:format&gt;image/svg+xml&lt;/dc:format&gt;&lt;dc:creator&gt;&lt;cc:agent&gt;&lt;dc:title&gt;Matplotlib v3.5.2, https://matplotlib.org/&lt;/dc:title&gt;&lt;/cc:agent&gt;&lt;/dc:creator&gt;&lt;/cc:work&gt;&lt;/rdf:rdf&gt;&lt;/metadata&gt;&lt;defs&gt;&lt;style type=text/css&gt;*{stroke-linejoin: round; stroke-linecap: butt}&lt;/style&gt;&lt;/defs&gt;&lt;g id=figure_1&gt;&lt;g id=patch_1&gt;&lt;path d=&quot;M 0 162 
L 216 162 
L 216 0 
L 0 0 
z
&quot; style=&quot;fill: #ffffff&quot;/&gt;&lt;/g&gt;&lt;g id=axes_1&gt;&lt;g id=patch_2&gt;&lt;path d=&quot;M 10.8 116.141159 
L 205.2 116.141159 
L 205.2 10.8 
L 10.8 10.8 
z
&quot; style=&quot;fill: #ffffff&quot;/&gt;&lt;/g&gt;&lt;g id=matplotlib.axis_1&gt;&lt;g id=xtick_1&gt;&lt;g id=text_1&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(17.167243 138.553257)rotate(-45)scale(0.08 -0.08)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-30 transform=scale(0.015625) d=&quot;M 266 2259 
Q 266 3072 433 3567 
Q 600 4063 929 4331 
Q 1259 4600 1759 4600 
Q 2128 4600 2406 4451 
Q 2684 4303 2865 4023 
Q 3047 3744 3150 3342 
Q 3253 2941 3253 2259 
Q 3253 1453 3087 958 
Q 2922 463 2592 192 
Q 2263 -78 1759 -78 
Q 1097 -78 719 397 
Q 266 969 266 2259 
z
M 844 2259 
Q 844 1131 1108 757 
Q 1372 384 1759 384 
Q 2147 384 2411 759 
Q 2675 1134 2675 2259 
Q 2675 3391 2411 3762 
Q 2147 4134 1753 4134 
Q 1366 4134 1134 3806 
Q 844 3388 844 2259 
z
&quot;/&gt;&lt;path id=ArialMT-2e transform=scale(0.015625) d=&quot;M 581 0 
L 581 641 
L 1222 641 
L 1222 0 
L 581 0 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-30 /&gt;&lt;use xlink:href=#ArialMT-2e x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=83.398438 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_2&gt;&lt;g id=text_2&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(57.70102 138.553257)rotate(-45)scale(0.08 -0.08)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-35 transform=scale(0.015625) d=&quot;M 266 1200 
L 856 1250 
Q 922 819 1161 601 
Q 1400 384 1738 384 
Q 2144 384 2425 690 
Q 2706 997 2706 1503 
Q 2706 1984 2436 2262 
Q 2166 2541 1728 2541 
Q 1456 2541 1237 2417 
Q 1019 2294 894 2097 
L 366 2166 
L 809 4519 
L 3088 4519 
L 3088 3981 
L 1259 3981 
L 1013 2750 
Q 1425 3038 1878 3038 
Q 2478 3038 2890 2622 
Q 3303 2206 3303 1553 
Q 3303 931 2941 478 
Q 2500 -78 1738 -78 
Q 1113 -78 717 272 
Q 322 622 266 1200 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-30 /&gt;&lt;use xlink:href=#ArialMT-2e x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-35 x=83.398438 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_3&gt;&lt;g id=text_3&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(98.234796 138.553257)rotate(-45)scale(0.08 -0.08)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-31 transform=scale(0.015625) d=&quot;M 2384 0 
L 1822 0 
L 1822 3584 
Q 1619 3391 1289 3197 
Q 959 3003 697 2906 
L 697 3450 
Q 1169 3672 1522 3987 
Q 1875 4303 2022 4600 
L 2384 4600 
L 2384 0 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-31 /&gt;&lt;use xlink:href=#ArialMT-2e x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=83.398438 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_4&gt;&lt;g id=text_4&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(138.768572 138.553257)rotate(-45)scale(0.08 -0.08)&quot;&gt;&lt;use xlink:href=#ArialMT-31 /&gt;&lt;use xlink:href=#ArialMT-2e x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-35 x=83.398438 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_5&gt;&lt;g id=text_5&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(179.302348 138.553257)rotate(-45)scale(0.08 -0.08)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-32 transform=scale(0.015625) d=&quot;M 3222 541 
L 3222 0 
L 194 0 
Q 188 203 259 391 
Q 375 700 629 1000 
Q 884 1300 1366 1694 
Q 2113 2306 2375 2664 
Q 2638 3022 2638 3341 
Q 2638 3675 2398 3904 
Q 2159 4134 1775 4134 
Q 1369 4134 1125 3890 
Q 881 3647 878 3216 
L 300 3275 
Q 359 3922 746 4261 
Q 1134 4600 1788 4600 
Q 2447 4600 2831 4234 
Q 3216 3869 3216 3328 
Q 3216 3053 3103 2787 
Q 2991 2522 2730 2228 
Q 2469 1934 1863 1422 
Q 1356 997 1212 845 
Q 1069 694 975 541 
L 3222 541 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-32 /&gt;&lt;use xlink:href=#ArialMT-2e x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=83.398438 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=text_6&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(188.517187 149.835369)scale(0.1 -0.1)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-65 transform=scale(0.015625) d=&quot;M 2694 1069 
L 3275 997 
Q 3138 488 2766 206 
Q 2394 -75 1816 -75 
Q 1088 -75 661 373 
Q 234 822 234 1631 
Q 234 2469 665 2931 
Q 1097 3394 1784 3394 
Q 2450 3394 2872 2941 
Q 3294 2488 3294 1666 
Q 3294 1616 3291 1516 
L 816 1516 
Q 847 969 1125 678 
Q 1403 388 1819 388 
Q 2128 388 2347 550 
Q 2566 713 2694 1069 
z
M 847 1978 
L 2700 1978 
Q 2663 2397 2488 2606 
Q 2219 2931 1791 2931 
Q 1403 2931 1139 2672 
Q 875 2413 847 1978 
z
&quot;/&gt;&lt;path id=ArialMT-37 transform=scale(0.015625) d=&quot;M 303 3981 
L 303 4522 
L 3269 4522 
L 3269 4084 
Q 2831 3619 2401 2847 
Q 1972 2075 1738 1259 
Q 1569 684 1522 0 
L 944 0 
Q 953 541 1156 1306 
Q 1359 2072 1739 2783 
Q 2119 3494 2547 3981 
L 303 3981 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-31 /&gt;&lt;use xlink:href=#ArialMT-65 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-37 x=111.230469 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=patch_3&gt;&lt;path d=&quot;M 19.636364 116.141159 
L 23.170909 116.141159 
L 23.170909 15.816246 
L 19.636364 15.816246 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_4&gt;&lt;path d=&quot;M 23.170909 116.141159 
L 26.705455 116.141159 
L 26.705455 116.11267 
L 23.170909 116.11267 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_5&gt;&lt;path d=&quot;M 26.705455 116.141159 
L 30.24 116.141159 
L 30.24 116.140473 
L 26.705455 116.140473 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_6&gt;&lt;path d=&quot;M 30.24 116.141159 
L 33.774545 116.141159 
L 33.774545 116.14093 
L 30.24 116.14093 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_7&gt;&lt;path d=&quot;M 33.774545 116.141159 
L 37.309091 116.141159 
L 37.309091 116.124798 
L 33.774545 116.124798 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_8&gt;&lt;path d=&quot;M 37.309091 116.141159 
L 40.843636 116.141159 
L 40.843636 116.141159 
L 37.309091 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_9&gt;&lt;path d=&quot;M 40.843636 116.141159 
L 44.378182 116.141159 
L 44.378182 116.141159 
L 40.843636 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_10&gt;&lt;path d=&quot;M 44.378182 116.141159 
L 47.912727 116.141159 
L 47.912727 116.141159 
L 44.378182 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_11&gt;&lt;path d=&quot;M 47.912727 116.141159 
L 51.447273 116.141159 
L 51.447273 116.141159 
L 47.912727 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_12&gt;&lt;path d=&quot;M 51.447273 116.141159 
L 54.981818 116.141159 
L 54.981818 116.141159 
L 51.447273 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_13&gt;&lt;path d=&quot;M 54.981818 116.141159 
L 58.516364 116.141159 
L 58.516364 116.141159 
L 54.981818 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_14&gt;&lt;path d=&quot;M 58.516364 116.141159 
L 62.050909 116.141159 
L 62.050909 116.141159 
L 58.516364 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_15&gt;&lt;path d=&quot;M 62.050909 116.141159 
L 65.585455 116.141159 
L 65.585455 116.141159 
L 62.050909 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_16&gt;&lt;path d=&quot;M 65.585455 116.141159 
L 69.12 116.141159 
L 69.12 116.141159 
L 65.585455 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_17&gt;&lt;path d=&quot;M 69.12 116.141159 
L 72.654545 116.141159 
L 72.654545 116.141159 
L 69.12 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_18&gt;&lt;path d=&quot;M 72.654545 116.141159 
L 76.189091 116.141159 
L 76.189091 116.141159 
L 72.654545 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_19&gt;&lt;path d=&quot;M 76.189091 116.141159 
L 79.723636 116.141159 
L 79.723636 116.141159 
L 76.189091 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_20&gt;&lt;path d=&quot;M 79.723636 116.141159 
L 83.258182 116.141159 
L 83.258182 116.141159 
L 79.723636 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_21&gt;&lt;path d=&quot;M 83.258182 116.141159 
L 86.792727 116.141159 
L 86.792727 116.141159 
L 83.258182 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_22&gt;&lt;path d=&quot;M 86.792727 116.141159 
L 90.327273 116.141159 
L 90.327273 116.141159 
L 86.792727 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_23&gt;&lt;path d=&quot;M 90.327273 116.141159 
L 93.861818 116.141159 
L 93.861818 116.141159 
L 90.327273 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_24&gt;&lt;path d=&quot;M 93.861818 116.141159 
L 97.396364 116.141159 
L 97.396364 116.141159 
L 93.861818 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_25&gt;&lt;path d=&quot;M 97.396364 116.141159 
L 100.930909 116.141159 
L 100.930909 116.141159 
L 97.396364 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_26&gt;&lt;path d=&quot;M 100.930909 116.141159 
L 104.465455 116.141159 
L 104.465455 116.141159 
L 100.930909 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_27&gt;&lt;path d=&quot;M 104.465455 116.141159 
L 108 116.141159 
L 108 116.141159 
L 104.465455 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_28&gt;&lt;path d=&quot;M 108 116.141159 
L 111.534545 116.141159 
L 111.534545 116.141159 
L 108 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_29&gt;&lt;path d=&quot;M 111.534545 116.141159 
L 115.069091 116.141159 
L 115.069091 116.141159 
L 111.534545 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_30&gt;&lt;path d=&quot;M 115.069091 116.141159 
L 118.603636 116.141159 
L 118.603636 116.141159 
L 115.069091 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_31&gt;&lt;path d=&quot;M 118.603636 116.141159 
L 122.138182 116.141159 
L 122.138182 116.141159 
L 118.603636 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_32&gt;&lt;path d=&quot;M 122.138182 116.141159 
L 125.672727 116.141159 
L 125.672727 116.141159 
L 122.138182 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_33&gt;&lt;path d=&quot;M 125.672727 116.141159 
L 129.207273 116.141159 
L 129.207273 116.141159 
L 125.672727 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_34&gt;&lt;path d=&quot;M 129.207273 116.141159 
L 132.741818 116.141159 
L 132.741818 116.141159 
L 129.207273 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_35&gt;&lt;path d=&quot;M 132.741818 116.141159 
L 136.276364 116.141159 
L 136.276364 116.141159 
L 132.741818 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_36&gt;&lt;path d=&quot;M 136.276364 116.141159 
L 139.810909 116.141159 
L 139.810909 116.141159 
L 136.276364 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_37&gt;&lt;path d=&quot;M 139.810909 116.141159 
L 143.345455 116.141159 
L 143.345455 116.141159 
L 139.810909 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_38&gt;&lt;path d=&quot;M 143.345455 116.141159 
L 146.88 116.141159 
L 146.88 116.141159 
L 143.345455 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_39&gt;&lt;path d=&quot;M 146.88 116.141159 
L 150.414545 116.141159 
L 150.414545 116.141159 
L 146.88 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_40&gt;&lt;path d=&quot;M 150.414545 116.141159 
L 153.949091 116.141159 
L 153.949091 116.141159 
L 150.414545 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_41&gt;&lt;path d=&quot;M 153.949091 116.141159 
L 157.483636 116.141159 
L 157.483636 116.141159 
L 153.949091 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_42&gt;&lt;path d=&quot;M 157.483636 116.141159 
L 161.018182 116.141159 
L 161.018182 116.141159 
L 157.483636 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_43&gt;&lt;path d=&quot;M 161.018182 116.141159 
L 164.552727 116.141159 
L 164.552727 116.141159 
L 161.018182 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_44&gt;&lt;path d=&quot;M 164.552727 116.141159 
L 168.087273 116.141159 
L 168.087273 116.14093 
L 164.552727 116.14093 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_45&gt;&lt;path d=&quot;M 168.087273 116.141159 
L 171.621818 116.141159 
L 171.621818 116.141159 
L 168.087273 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_46&gt;&lt;path d=&quot;M 171.621818 116.141159 
L 175.156364 116.141159 
L 175.156364 116.141159 
L 171.621818 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_47&gt;&lt;path d=&quot;M 175.156364 116.141159 
L 178.690909 116.141159 
L 178.690909 116.141159 
L 175.156364 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_48&gt;&lt;path d=&quot;M 178.690909 116.141159 
L 182.225455 116.141159 
L 182.225455 116.141159 
L 178.690909 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_49&gt;&lt;path d=&quot;M 182.225455 116.141159 
L 185.76 116.141159 
L 185.76 116.141159 
L 182.225455 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_50&gt;&lt;path d=&quot;M 185.76 116.141159 
L 189.294545 116.141159 
L 189.294545 116.141159 
L 185.76 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_51&gt;&lt;path d=&quot;M 189.294545 116.141159 
L 192.829091 116.141159 
L 192.829091 116.141159 
L 189.294545 116.141159 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_52&gt;&lt;path d=&quot;M 192.829091 116.141159 
L 196.363636 116.141159 
L 196.363636 116.14093 
L 192.829091 116.14093 
z
&quot; clip-path=url(#pc8c9033481) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_53&gt;&lt;path d=&quot;M 10.8 116.141159 
L 10.8 10.8 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;g id=patch_54&gt;&lt;path d=&quot;M 205.2 116.141159 
L 205.2 10.8 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;g id=patch_55&gt;&lt;path d=&quot;M 10.8 116.141159 
L 205.2 116.141159 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;g id=patch_56&gt;&lt;path d=&quot;M 10.8 10.8 
L 205.2 10.8 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;defs&gt;&lt;clippath id=pc8c9033481&gt;&lt;rect x=10.8 y=10.8 width=194.4 height=105.341159 /&gt;&lt;/clippath&gt;&lt;/defs&gt;&lt;/svg&gt;&lt;/div&gt;&lt;div class=&quot;col-sm-12 text-right&quot;&gt;&lt;button class=&quot;btn btn-default btn-sm&quot; data-toggle=collapse data-target=&quot;#bottom-8124034662335410336, #minifreqtable8124034662335410336&quot; aria-expanded=true aria-controls=collapseExample&gt;Toggle details&lt;/button&gt;&lt;/div&gt;&lt;div id=bottom-8124034662335410336 class=collapse&gt;&lt;div class=&quot;row spacing&quot;&gt;&lt;ul class=&quot;nav nav-tabs&quot; role=tablist&gt;&lt;li role=presentation class=active&gt;&lt;a href=#8124034662335410336bottom-8124034662335410336statistics aria-controls=8124034662335410336bottom-8124034662335410336statistics role=tab data-toggle=tab&gt;Statistics&lt;/a&gt;&lt;/li&gt;&lt;li role=presentation&gt;&lt;a href=#8124034662335410336bottom-8124034662335410336histogram aria-controls=8124034662335410336bottom-8124034662335410336histogram role=tab data-toggle=tab&gt;Histogram&lt;/a&gt;&lt;/li&gt;&lt;li role=presentation&gt;&lt;a href=#8124034662335410336bottom-8124034662335410336common_values aria-controls=8124034662335410336bottom-8124034662335410336common_values role=tab data-toggle=tab&gt;Common values&lt;/a&gt;&lt;/li&gt;&lt;li role=presentation&gt;&lt;a href=#8124034662335410336bottom-8124034662335410336extreme_values aria-controls=8124034662335410336bottom-8124034662335410336extreme_values role=tab data-toggle=tab&gt;Extreme values&lt;/a&gt;&lt;/li&gt;&lt;/ul&gt;&lt;div class=tab-content&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12 active&quot; id=8124034662335410336bottom-8124034662335410336statistics&gt;&lt;div class=col-sm-6&gt;&lt;p class=h4&gt;Quantile statistics&lt;/p&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;Minimum&lt;/th&gt;&lt;td&gt;-1&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;5-th percentile&lt;/th&gt;&lt;td&gt;7.599999905&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Q1&lt;/th&gt;&lt;td&gt;8.100000381&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;median&lt;/th&gt;&lt;td&gt;11&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Q3&lt;/th&gt;&lt;td&gt;6000&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;95-th percentile&lt;/th&gt;&lt;td&gt;40000&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Maximum&lt;/th&gt;&lt;td&gt;21800000&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Range&lt;/th&gt;&lt;td&gt;21800001&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Interquartile range (IQR)&lt;/th&gt;&lt;td&gt;5991.9&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div class=col-sm-6&gt;&lt;p class=h4&gt;Descriptive statistics&lt;/p&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;Standard deviation&lt;/th&gt;&lt;td&gt;53298.12109&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Coefficient of variation (CV)&lt;/th&gt;&lt;td&gt;6.533273076&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Kurtosis&lt;/th&gt;&lt;td&gt;93645.08594&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Mean&lt;/th&gt;&lt;td&gt;8157.950919&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Median Absolute Deviation (MAD)&lt;/th&gt;&lt;td&gt;3.400000095&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Skewness&lt;/th&gt;&lt;td&gt;252.8905792&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Sum&lt;/th&gt;&lt;td&gt;7156701129&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Variance&lt;/th&gt;&lt;td&gt;2840689664&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Monotonicity&lt;/th&gt;&lt;td&gt;Not monotonic&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;/div&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12&quot; id=8124034662335410336bottom-8124034662335410336histogram&gt;&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot; standalone=&quot;no&quot;?&gt;&lt;!DOCTYPE svg class=&quot;img-responsive center-img&quot;PUBLIC &quot;-//W3C//DTD SVG 1.1//EN&quot;
  &quot;http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd&quot;&gt;&lt;svg class=&quot;img-responsive center-img&quot; xmlns:xlink=http://www.w3.org/1999/xlink width=432pt height=288pt viewbox=&quot;0 0 432 288&quot; xmlns=http://www.w3.org/2000/svg version=1.1&gt;&lt;metadata&gt;&lt;rdf:rdf xmlns:dc=http://purl.org/dc/elements/1.1/ xmlns:cc=http://creativecommons.org/ns# xmlns:rdf=http://www.w3.org/1999/02/22-rdf-syntax-ns#&gt;&lt;cc:work&gt;&lt;dc:type rdf:resource=http://purl.org/dc/dcmitype/StillImage /&gt;&lt;dc:date&gt;2022-07-12T13:06:41.976989&lt;/dc:date&gt;&lt;dc:format&gt;image/svg+xml&lt;/dc:format&gt;&lt;dc:creator&gt;&lt;cc:agent&gt;&lt;dc:title&gt;Matplotlib v3.5.2, https://matplotlib.org/&lt;/dc:title&gt;&lt;/cc:agent&gt;&lt;/dc:creator&gt;&lt;/cc:work&gt;&lt;/rdf:rdf&gt;&lt;/metadata&gt;&lt;defs&gt;&lt;style type=text/css&gt;*{stroke-linejoin: round; stroke-linecap: butt}&lt;/style&gt;&lt;/defs&gt;&lt;g id=figure_1&gt;&lt;g id=patch_1&gt;&lt;path d=&quot;M 0 288 
L 432 288 
L 432 0 
L 0 0 
z
&quot; style=&quot;fill: #ffffff&quot;/&gt;&lt;/g&gt;&lt;g id=axes_1&gt;&lt;g id=patch_2&gt;&lt;path d=&quot;M 68.86 239.086458 
L 421.2 239.086458 
L 421.2 10.8 
L 68.86 10.8 
z
&quot; style=&quot;fill: #ffffff&quot;/&gt;&lt;/g&gt;&lt;g id=matplotlib.axis_1&gt;&lt;g id=xtick_1&gt;&lt;g id=text_1&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(81.789059 264.47658)rotate(-45)scale(0.1 -0.1)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-30 transform=scale(0.015625) d=&quot;M 266 2259 
Q 266 3072 433 3567 
Q 600 4063 929 4331 
Q 1259 4600 1759 4600 
Q 2128 4600 2406 4451 
Q 2684 4303 2865 4023 
Q 3047 3744 3150 3342 
Q 3253 2941 3253 2259 
Q 3253 1453 3087 958 
Q 2922 463 2592 192 
Q 2263 -78 1759 -78 
Q 1097 -78 719 397 
Q 266 969 266 2259 
z
M 844 2259 
Q 844 1131 1108 757 
Q 1372 384 1759 384 
Q 2147 384 2411 759 
Q 2675 1134 2675 2259 
Q 2675 3391 2411 3762 
Q 2147 4134 1753 4134 
Q 1366 4134 1134 3806 
Q 844 3388 844 2259 
z
&quot;/&gt;&lt;path id=ArialMT-2e transform=scale(0.015625) d=&quot;M 581 0 
L 581 641 
L 1222 641 
L 1222 0 
L 581 0 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-30 /&gt;&lt;use xlink:href=#ArialMT-2e x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=83.398438 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_2&gt;&lt;g id=text_2&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(155.254443 264.47658)rotate(-45)scale(0.1 -0.1)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-35 transform=scale(0.015625) d=&quot;M 266 1200 
L 856 1250 
Q 922 819 1161 601 
Q 1400 384 1738 384 
Q 2144 384 2425 690 
Q 2706 997 2706 1503 
Q 2706 1984 2436 2262 
Q 2166 2541 1728 2541 
Q 1456 2541 1237 2417 
Q 1019 2294 894 2097 
L 366 2166 
L 809 4519 
L 3088 4519 
L 3088 3981 
L 1259 3981 
L 1013 2750 
Q 1425 3038 1878 3038 
Q 2478 3038 2890 2622 
Q 3303 2206 3303 1553 
Q 3303 931 2941 478 
Q 2500 -78 1738 -78 
Q 1113 -78 717 272 
Q 322 622 266 1200 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-30 /&gt;&lt;use xlink:href=#ArialMT-2e x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-35 x=83.398438 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_3&gt;&lt;g id=text_3&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(228.719828 264.47658)rotate(-45)scale(0.1 -0.1)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-31 transform=scale(0.015625) d=&quot;M 2384 0 
L 1822 0 
L 1822 3584 
Q 1619 3391 1289 3197 
Q 959 3003 697 2906 
L 697 3450 
Q 1169 3672 1522 3987 
Q 1875 4303 2022 4600 
L 2384 4600 
L 2384 0 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-31 /&gt;&lt;use xlink:href=#ArialMT-2e x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=83.398438 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_4&gt;&lt;g id=text_4&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(302.185212 264.47658)rotate(-45)scale(0.1 -0.1)&quot;&gt;&lt;use xlink:href=#ArialMT-31 /&gt;&lt;use xlink:href=#ArialMT-2e x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-35 x=83.398438 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_5&gt;&lt;g id=text_5&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(375.650596 264.47658)rotate(-45)scale(0.1 -0.1)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-32 transform=scale(0.015625) d=&quot;M 3222 541 
L 3222 0 
L 194 0 
Q 188 203 259 391 
Q 375 700 629 1000 
Q 884 1300 1366 1694 
Q 2113 2306 2375 2664 
Q 2638 3022 2638 3341 
Q 2638 3675 2398 3904 
Q 2159 4134 1775 4134 
Q 1369 4134 1125 3890 
Q 881 3647 878 3216 
L 300 3275 
Q 359 3922 746 4261 
Q 1134 4600 1788 4600 
Q 2447 4600 2831 4234 
Q 3216 3869 3216 3328 
Q 3216 3053 3103 2787 
Q 2991 2522 2730 2228 
Q 2469 1934 1863 1422 
Q 1356 997 1212 845 
Q 1069 694 975 541 
L 3222 541 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-32 /&gt;&lt;use xlink:href=#ArialMT-2e x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=83.398438 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=text_6&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(404.517187 276.039767)scale(0.1 -0.1)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-65 transform=scale(0.015625) d=&quot;M 2694 1069 
L 3275 997 
Q 3138 488 2766 206 
Q 2394 -75 1816 -75 
Q 1088 -75 661 373 
Q 234 822 234 1631 
Q 234 2469 665 2931 
Q 1097 3394 1784 3394 
Q 2450 3394 2872 2941 
Q 3294 2488 3294 1666 
Q 3294 1616 3291 1516 
L 816 1516 
Q 847 969 1125 678 
Q 1403 388 1819 388 
Q 2128 388 2347 550 
Q 2566 713 2694 1069 
z
M 847 1978 
L 2700 1978 
Q 2663 2397 2488 2606 
Q 2219 2931 1791 2931 
Q 1403 2931 1139 2672 
Q 875 2413 847 1978 
z
&quot;/&gt;&lt;path id=ArialMT-37 transform=scale(0.015625) d=&quot;M 303 3981 
L 303 4522 
L 3269 4522 
L 3269 4084 
Q 2831 3619 2401 2847 
Q 1972 2075 1738 1259 
Q 1569 684 1522 0 
L 944 0 
Q 953 541 1156 1306 
Q 1359 2072 1739 2783 
Q 2119 3494 2547 3981 
L 303 3981 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-31 /&gt;&lt;use xlink:href=#ArialMT-65 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-37 x=111.230469 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=matplotlib.axis_2&gt;&lt;g id=ytick_1&gt;&lt;g id=text_7&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(52.799062 242.665364)scale(0.1 -0.1)&quot;&gt;&lt;use xlink:href=#ArialMT-30 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_2&gt;&lt;g id=text_8&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(24.994375 193.075936)scale(0.1 -0.1)&quot;&gt;&lt;use xlink:href=#ArialMT-32 /&gt;&lt;use xlink:href=#ArialMT-30 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-30 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-30 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_3&gt;&lt;g id=text_9&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(24.994375 143.486508)scale(0.1 -0.1)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-34 transform=scale(0.015625) d=&quot;M 2069 0 
L 2069 1097 
L 81 1097 
L 81 1613 
L 2172 4581 
L 2631 4581 
L 2631 1613 
L 3250 1613 
L 3250 1097 
L 2631 1097 
L 2631 0 
L 2069 0 
z
M 2069 1613 
L 2069 3678 
L 634 1613 
L 2069 1613 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-34 /&gt;&lt;use xlink:href=#ArialMT-30 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-30 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-30 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_4&gt;&lt;g id=text_10&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(24.994375 93.897079)scale(0.1 -0.1)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-36 transform=scale(0.015625) d=&quot;M 3184 3459 
L 2625 3416 
Q 2550 3747 2413 3897 
Q 2184 4138 1850 4138 
Q 1581 4138 1378 3988 
Q 1113 3794 959 3422 
Q 806 3050 800 2363 
Q 1003 2672 1297 2822 
Q 1591 2972 1913 2972 
Q 2475 2972 2870 2558 
Q 3266 2144 3266 1488 
Q 3266 1056 3080 686 
Q 2894 316 2569 119 
Q 2244 -78 1831 -78 
Q 1128 -78 684 439 
Q 241 956 241 2144 
Q 241 3472 731 4075 
Q 1159 4600 1884 4600 
Q 2425 4600 2770 4297 
Q 3116 3994 3184 3459 
z
M 888 1484 
Q 888 1194 1011 928 
Q 1134 663 1356 523 
Q 1578 384 1822 384 
Q 2178 384 2434 671 
Q 2691 959 2691 1453 
Q 2691 1928 2437 2201 
Q 2184 2475 1800 2475 
Q 1419 2475 1153 2201 
Q 888 1928 888 1484 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-36 /&gt;&lt;use xlink:href=#ArialMT-30 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-30 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-30 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_5&gt;&lt;g id=text_11&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(24.994375 44.307651)scale(0.1 -0.1)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-38 transform=scale(0.015625) d=&quot;M 1131 2484 
Q 781 2613 612 2850 
Q 444 3088 444 3419 
Q 444 3919 803 4259 
Q 1163 4600 1759 4600 
Q 2359 4600 2725 4251 
Q 3091 3903 3091 3403 
Q 3091 3084 2923 2848 
Q 2756 2613 2416 2484 
Q 2838 2347 3058 2040 
Q 3278 1734 3278 1309 
Q 3278 722 2862 322 
Q 2447 -78 1769 -78 
Q 1091 -78 675 323 
Q 259 725 259 1325 
Q 259 1772 486 2073 
Q 713 2375 1131 2484 
z
M 1019 3438 
Q 1019 3113 1228 2906 
Q 1438 2700 1772 2700 
Q 2097 2700 2305 2904 
Q 2513 3109 2513 3406 
Q 2513 3716 2298 3927 
Q 2084 4138 1766 4138 
Q 1444 4138 1231 3931 
Q 1019 3725 1019 3438 
z
M 838 1322 
Q 838 1081 952 856 
Q 1066 631 1291 507 
Q 1516 384 1775 384 
Q 2178 384 2440 643 
Q 2703 903 2703 1303 
Q 2703 1709 2433 1975 
Q 2163 2241 1756 2241 
Q 1359 2241 1098 1978 
Q 838 1716 838 1322 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-38 /&gt;&lt;use xlink:href=#ArialMT-30 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-30 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-30 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=text_12&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(18.679219 150.926432)rotate(-90)scale(0.11 -0.11)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-46 transform=scale(0.015625) d=&quot;M 525 0 
L 525 4581 
L 3616 4581 
L 3616 4041 
L 1131 4041 
L 1131 2622 
L 3281 2622 
L 3281 2081 
L 1131 2081 
L 1131 0 
L 525 0 
z
&quot;/&gt;&lt;path id=ArialMT-72 transform=scale(0.015625) d=&quot;M 416 0 
L 416 3319 
L 922 3319 
L 922 2816 
Q 1116 3169 1280 3281 
Q 1444 3394 1641 3394 
Q 1925 3394 2219 3213 
L 2025 2691 
Q 1819 2813 1613 2813 
Q 1428 2813 1281 2702 
Q 1134 2591 1072 2394 
Q 978 2094 978 1738 
L 978 0 
L 416 0 
z
&quot;/&gt;&lt;path id=ArialMT-71 transform=scale(0.015625) d=&quot;M 2538 -1272 
L 2538 353 
Q 2406 169 2170 47 
Q 1934 -75 1669 -75 
Q 1078 -75 651 397 
Q 225 869 225 1691 
Q 225 2191 398 2587 
Q 572 2984 901 3189 
Q 1231 3394 1625 3394 
Q 2241 3394 2594 2875 
L 2594 3319 
L 3100 3319 
L 3100 -1272 
L 2538 -1272 
z
M 803 1669 
Q 803 1028 1072 708 
Q 1341 388 1716 388 
Q 2075 388 2334 692 
Q 2594 997 2594 1619 
Q 2594 2281 2320 2615 
Q 2047 2950 1678 2950 
Q 1313 2950 1058 2639 
Q 803 2328 803 1669 
z
&quot;/&gt;&lt;path id=ArialMT-75 transform=scale(0.015625) d=&quot;M 2597 0 
L 2597 488 
Q 2209 -75 1544 -75 
Q 1250 -75 995 37 
Q 741 150 617 320 
Q 494 491 444 738 
Q 409 903 409 1263 
L 409 3319 
L 972 3319 
L 972 1478 
Q 972 1038 1006 884 
Q 1059 663 1231 536 
Q 1403 409 1656 409 
Q 1909 409 2131 539 
Q 2353 669 2445 892 
Q 2538 1116 2538 1541 
L 2538 3319 
L 3100 3319 
L 3100 0 
L 2597 0 
z
&quot;/&gt;&lt;path id=ArialMT-6e transform=scale(0.015625) d=&quot;M 422 0 
L 422 3319 
L 928 3319 
L 928 2847 
Q 1294 3394 1984 3394 
Q 2284 3394 2536 3286 
Q 2788 3178 2913 3003 
Q 3038 2828 3088 2588 
Q 3119 2431 3119 2041 
L 3119 0 
L 2556 0 
L 2556 2019 
Q 2556 2363 2490 2533 
Q 2425 2703 2258 2804 
Q 2091 2906 1866 2906 
Q 1506 2906 1245 2678 
Q 984 2450 984 1813 
L 984 0 
L 422 0 
z
&quot;/&gt;&lt;path id=ArialMT-63 transform=scale(0.015625) d=&quot;M 2588 1216 
L 3141 1144 
Q 3050 572 2676 248 
Q 2303 -75 1759 -75 
Q 1078 -75 664 370 
Q 250 816 250 1647 
Q 250 2184 428 2587 
Q 606 2991 970 3192 
Q 1334 3394 1763 3394 
Q 2303 3394 2647 3120 
Q 2991 2847 3088 2344 
L 2541 2259 
Q 2463 2594 2264 2762 
Q 2066 2931 1784 2931 
Q 1359 2931 1093 2626 
Q 828 2322 828 1663 
Q 828 994 1084 691 
Q 1341 388 1753 388 
Q 2084 388 2306 591 
Q 2528 794 2588 1216 
z
&quot;/&gt;&lt;path id=ArialMT-79 transform=scale(0.015625) d=&quot;M 397 -1278 
L 334 -750 
Q 519 -800 656 -800 
Q 844 -800 956 -737 
Q 1069 -675 1141 -563 
Q 1194 -478 1313 -144 
Q 1328 -97 1363 -6 
L 103 3319 
L 709 3319 
L 1400 1397 
Q 1534 1031 1641 628 
Q 1738 1016 1872 1384 
L 2581 3319 
L 3144 3319 
L 1881 -56 
Q 1678 -603 1566 -809 
Q 1416 -1088 1222 -1217 
Q 1028 -1347 759 -1347 
Q 597 -1347 397 -1278 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-46 /&gt;&lt;use xlink:href=#ArialMT-72 x=61.083984 /&gt;&lt;use xlink:href=#ArialMT-65 x=94.384766 /&gt;&lt;use xlink:href=#ArialMT-71 x=150 /&gt;&lt;use xlink:href=#ArialMT-75 x=205.615234 /&gt;&lt;use xlink:href=#ArialMT-65 x=261.230469 /&gt;&lt;use xlink:href=#ArialMT-6e x=316.845703 /&gt;&lt;use xlink:href=#ArialMT-63 x=372.460938 /&gt;&lt;use xlink:href=#ArialMT-79 x=422.460938 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=patch_3&gt;&lt;path d=&quot;M 84.875455 239.086458 
L 91.281636 239.086458 
L 91.281636 21.670784 
L 84.875455 21.670784 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_4&gt;&lt;path d=&quot;M 91.281636 239.086458 
L 97.687818 239.086458 
L 97.687818 239.024719 
L 91.281636 239.024719 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_5&gt;&lt;path d=&quot;M 97.687818 239.086458 
L 104.094 239.086458 
L 104.094 239.08497 
L 97.687818 239.08497 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_6&gt;&lt;path d=&quot;M 104.094 239.086458 
L 110.500182 239.086458 
L 110.500182 239.085962 
L 104.094 239.085962 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_7&gt;&lt;path d=&quot;M 110.500182 239.086458 
L 116.906364 239.086458 
L 116.906364 239.051001 
L 110.500182 239.051001 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_8&gt;&lt;path d=&quot;M 116.906364 239.086458 
L 123.312545 239.086458 
L 123.312545 239.086458 
L 116.906364 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_9&gt;&lt;path d=&quot;M 123.312545 239.086458 
L 129.718727 239.086458 
L 129.718727 239.086458 
L 123.312545 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_10&gt;&lt;path d=&quot;M 129.718727 239.086458 
L 136.124909 239.086458 
L 136.124909 239.086458 
L 129.718727 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_11&gt;&lt;path d=&quot;M 136.124909 239.086458 
L 142.531091 239.086458 
L 142.531091 239.086458 
L 136.124909 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_12&gt;&lt;path d=&quot;M 142.531091 239.086458 
L 148.937273 239.086458 
L 148.937273 239.086458 
L 142.531091 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_13&gt;&lt;path d=&quot;M 148.937273 239.086458 
L 155.343455 239.086458 
L 155.343455 239.086458 
L 148.937273 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_14&gt;&lt;path d=&quot;M 155.343455 239.086458 
L 161.749636 239.086458 
L 161.749636 239.086458 
L 155.343455 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_15&gt;&lt;path d=&quot;M 161.749636 239.086458 
L 168.155818 239.086458 
L 168.155818 239.086458 
L 161.749636 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_16&gt;&lt;path d=&quot;M 168.155818 239.086458 
L 174.562 239.086458 
L 174.562 239.086458 
L 168.155818 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_17&gt;&lt;path d=&quot;M 174.562 239.086458 
L 180.968182 239.086458 
L 180.968182 239.086458 
L 174.562 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_18&gt;&lt;path d=&quot;M 180.968182 239.086458 
L 187.374364 239.086458 
L 187.374364 239.086458 
L 180.968182 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_19&gt;&lt;path d=&quot;M 187.374364 239.086458 
L 193.780545 239.086458 
L 193.780545 239.086458 
L 187.374364 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_20&gt;&lt;path d=&quot;M 193.780545 239.086458 
L 200.186727 239.086458 
L 200.186727 239.086458 
L 193.780545 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_21&gt;&lt;path d=&quot;M 200.186727 239.086458 
L 206.592909 239.086458 
L 206.592909 239.086458 
L 200.186727 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_22&gt;&lt;path d=&quot;M 206.592909 239.086458 
L 212.999091 239.086458 
L 212.999091 239.086458 
L 206.592909 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_23&gt;&lt;path d=&quot;M 212.999091 239.086458 
L 219.405273 239.086458 
L 219.405273 239.086458 
L 212.999091 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_24&gt;&lt;path d=&quot;M 219.405273 239.086458 
L 225.811455 239.086458 
L 225.811455 239.086458 
L 219.405273 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_25&gt;&lt;path d=&quot;M 225.811455 239.086458 
L 232.217636 239.086458 
L 232.217636 239.086458 
L 225.811455 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_26&gt;&lt;path d=&quot;M 232.217636 239.086458 
L 238.623818 239.086458 
L 238.623818 239.086458 
L 232.217636 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_27&gt;&lt;path d=&quot;M 238.623818 239.086458 
L 245.03 239.086458 
L 245.03 239.086458 
L 238.623818 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_28&gt;&lt;path d=&quot;M 245.03 239.086458 
L 251.436182 239.086458 
L 251.436182 239.086458 
L 245.03 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_29&gt;&lt;path d=&quot;M 251.436182 239.086458 
L 257.842364 239.086458 
L 257.842364 239.086458 
L 251.436182 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_30&gt;&lt;path d=&quot;M 257.842364 239.086458 
L 264.248545 239.086458 
L 264.248545 239.086458 
L 257.842364 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_31&gt;&lt;path d=&quot;M 264.248545 239.086458 
L 270.654727 239.086458 
L 270.654727 239.086458 
L 264.248545 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_32&gt;&lt;path d=&quot;M 270.654727 239.086458 
L 277.060909 239.086458 
L 277.060909 239.086458 
L 270.654727 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_33&gt;&lt;path d=&quot;M 277.060909 239.086458 
L 283.467091 239.086458 
L 283.467091 239.086458 
L 277.060909 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_34&gt;&lt;path d=&quot;M 283.467091 239.086458 
L 289.873273 239.086458 
L 289.873273 239.086458 
L 283.467091 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_35&gt;&lt;path d=&quot;M 289.873273 239.086458 
L 296.279455 239.086458 
L 296.279455 239.086458 
L 289.873273 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_36&gt;&lt;path d=&quot;M 296.279455 239.086458 
L 302.685636 239.086458 
L 302.685636 239.086458 
L 296.279455 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_37&gt;&lt;path d=&quot;M 302.685636 239.086458 
L 309.091818 239.086458 
L 309.091818 239.086458 
L 302.685636 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_38&gt;&lt;path d=&quot;M 309.091818 239.086458 
L 315.498 239.086458 
L 315.498 239.086458 
L 309.091818 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_39&gt;&lt;path d=&quot;M 315.498 239.086458 
L 321.904182 239.086458 
L 321.904182 239.086458 
L 315.498 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_40&gt;&lt;path d=&quot;M 321.904182 239.086458 
L 328.310364 239.086458 
L 328.310364 239.086458 
L 321.904182 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_41&gt;&lt;path d=&quot;M 328.310364 239.086458 
L 334.716545 239.086458 
L 334.716545 239.086458 
L 328.310364 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_42&gt;&lt;path d=&quot;M 334.716545 239.086458 
L 341.122727 239.086458 
L 341.122727 239.086458 
L 334.716545 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_43&gt;&lt;path d=&quot;M 341.122727 239.086458 
L 347.528909 239.086458 
L 347.528909 239.086458 
L 341.122727 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_44&gt;&lt;path d=&quot;M 347.528909 239.086458 
L 353.935091 239.086458 
L 353.935091 239.085962 
L 347.528909 239.085962 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_45&gt;&lt;path d=&quot;M 353.935091 239.086458 
L 360.341273 239.086458 
L 360.341273 239.086458 
L 353.935091 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_46&gt;&lt;path d=&quot;M 360.341273 239.086458 
L 366.747455 239.086458 
L 366.747455 239.086458 
L 360.341273 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_47&gt;&lt;path d=&quot;M 366.747455 239.086458 
L 373.153636 239.086458 
L 373.153636 239.086458 
L 366.747455 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_48&gt;&lt;path d=&quot;M 373.153636 239.086458 
L 379.559818 239.086458 
L 379.559818 239.086458 
L 373.153636 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_49&gt;&lt;path d=&quot;M 379.559818 239.086458 
L 385.966 239.086458 
L 385.966 239.086458 
L 379.559818 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_50&gt;&lt;path d=&quot;M 385.966 239.086458 
L 392.372182 239.086458 
L 392.372182 239.086458 
L 385.966 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_51&gt;&lt;path d=&quot;M 392.372182 239.086458 
L 398.778364 239.086458 
L 398.778364 239.086458 
L 392.372182 239.086458 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_52&gt;&lt;path d=&quot;M 398.778364 239.086458 
L 405.184545 239.086458 
L 405.184545 239.085962 
L 398.778364 239.085962 
z
&quot; clip-path=url(#p18957e8d93) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_53&gt;&lt;path d=&quot;M 68.86 239.086458 
L 68.86 10.8 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;g id=patch_54&gt;&lt;path d=&quot;M 421.2 239.086458 
L 421.2 10.8 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;g id=patch_55&gt;&lt;path d=&quot;M 68.86 239.086458 
L 421.2 239.086458 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;g id=patch_56&gt;&lt;path d=&quot;M 68.86 10.8 
L 421.2 10.8 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;defs&gt;&lt;clippath id=p18957e8d93&gt;&lt;rect x=68.86 y=10.8 width=352.34 height=228.286458 /&gt;&lt;/clippath&gt;&lt;/defs&gt;&lt;/svg&gt;&lt;div class=&quot;caption text-center text-muted&quot;&gt;&lt;strong&gt;Histogram with fixed size bins&lt;/strong&gt; (bins=50) &lt;/div&gt;&lt;/div&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12&quot; id=8124034662335410336bottom-8124034662335410336common_values&gt;&lt;table class=&quot;freq table table-hover table-striped&quot;&gt;&lt;thead&gt;&lt;tr&gt;&lt;td&gt;Value&lt;/td&gt;&lt;td&gt;Count&lt;/td&gt;&lt;td&gt;Frequency (%)&lt;/td&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr class&gt;&lt;td title=8.100000381&gt;8.100000381&lt;/td&gt;&lt;td&gt;156657&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt; 17.8% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=11&gt;11&lt;/td&gt;&lt;td&gt;130418&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:83.3%&gt; 14.8% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=7.599999905&gt;7.599999905&lt;/td&gt;&lt;td&gt;127538&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:81.4%&gt; 14.5% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=16&gt;16&lt;/td&gt;&lt;td&gt;94176&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:60.1%&gt; 10.7% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=28000&gt;28000&lt;/td&gt;&lt;td&gt;58934&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:37.6%&gt; &amp;nbsp; &lt;/div&gt; 6.7% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=12.5&gt;12.5&lt;/td&gt;&lt;td&gt;30218&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:19.3%&gt; &amp;nbsp; &lt;/div&gt; 3.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=29600&gt;29600&lt;/td&gt;&lt;td&gt;23221&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:14.8%&gt; &amp;nbsp; &lt;/div&gt; 2.6% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=14000&gt;14000&lt;/td&gt;&lt;td&gt;23161&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:14.8%&gt; &amp;nbsp; &lt;/div&gt; 2.6% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=-1&gt;-1&lt;/td&gt;&lt;td&gt;22602&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:14.4%&gt; &amp;nbsp; &lt;/div&gt; 2.6% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=40000&gt;40000&lt;/td&gt;&lt;td&gt;20842&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:13.3%&gt; &amp;nbsp; &lt;/div&gt; 2.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=27500&gt;27500&lt;/td&gt;&lt;td&gt;18542&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:11.8%&gt; &amp;nbsp; &lt;/div&gt; 2.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=25&gt;25&lt;/td&gt;&lt;td&gt;17403&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:11.1%&gt; &amp;nbsp; &lt;/div&gt; 2.0% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=56000&gt;56000&lt;/td&gt;&lt;td&gt;15825&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:10.1%&gt; &amp;nbsp; &lt;/div&gt; 1.8% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=5700&gt;5700&lt;/td&gt;&lt;td&gt;14820&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:9.5%&gt; &amp;nbsp; &lt;/div&gt; 1.7% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=55000&gt;55000&lt;/td&gt;&lt;td&gt;13554&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:8.7%&gt; &amp;nbsp; &lt;/div&gt; 1.5% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=6000&gt;6000&lt;/td&gt;&lt;td&gt;10446&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:6.7%&gt; &amp;nbsp; &lt;/div&gt; 1.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=256&gt;256&lt;/td&gt;&lt;td&gt;9272&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:5.9%&gt; &amp;nbsp; &lt;/div&gt; 1.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=7000&gt;7000&lt;/td&gt;&lt;td&gt;7512&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:4.8%&gt; &amp;nbsp; &lt;/div&gt; 0.9% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=10&gt;10&lt;/td&gt;&lt;td&gt;7065&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:4.5%&gt; &amp;nbsp; &lt;/div&gt; 0.8% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=8.300000191&gt;8.300000191&lt;/td&gt;&lt;td&gt;5683&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:3.6%&gt; &amp;nbsp; &lt;/div&gt; 0.6% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=4&gt;4&lt;/td&gt;&lt;td&gt;5621&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:3.6%&gt; &amp;nbsp; &lt;/div&gt; 0.6% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=2.700000048&gt;2.700000048&lt;/td&gt;&lt;td&gt;5411&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:3.5%&gt; &amp;nbsp; &lt;/div&gt; 0.6% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=6200&gt;6200&lt;/td&gt;&lt;td&gt;4832&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:3.1%&gt; &amp;nbsp; &lt;/div&gt; 0.5% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=29700&gt;29700&lt;/td&gt;&lt;td&gt;4483&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:2.9%&gt; &amp;nbsp; &lt;/div&gt; 0.5% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=13700&gt;13700&lt;/td&gt;&lt;td&gt;3916&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:2.5%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=30000&gt;30000&lt;/td&gt;&lt;td&gt;3549&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:2.3%&gt; &amp;nbsp; &lt;/div&gt; 0.4% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=3500&gt;3500&lt;/td&gt;&lt;td&gt;2930&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:1.9%&gt; &amp;nbsp; &lt;/div&gt; 0.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=3450&gt;3450&lt;/td&gt;&lt;td&gt;2826&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:1.8%&gt; &amp;nbsp; &lt;/div&gt; 0.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=11.10000038&gt;11.10000038&lt;/td&gt;&lt;td&gt;1921&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:1.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=3000&gt;3000&lt;/td&gt;&lt;td&gt;1811&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:1.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=10000&gt;10000&lt;/td&gt;&lt;td&gt;1746&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:1.1%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=6&gt;6&lt;/td&gt;&lt;td&gt;1716&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:1.1%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=62500&gt;62500&lt;/td&gt;&lt;td&gt;1658&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:1.1%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=6750&gt;6750&lt;/td&gt;&lt;td&gt;1596&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:1.0%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=8.329999924&gt;8.329999924&lt;/td&gt;&lt;td&gt;1578&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:1.0%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=5000&gt;5000&lt;/td&gt;&lt;td&gt;1473&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.9%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=20000&gt;20000&lt;/td&gt;&lt;td&gt;1359&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.9%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=180&gt;180&lt;/td&gt;&lt;td&gt;1229&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.8%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=29000&gt;29000&lt;/td&gt;&lt;td&gt;1092&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.7%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=20&gt;20&lt;/td&gt;&lt;td&gt;991&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.6%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=10500&gt;10500&lt;/td&gt;&lt;td&gt;845&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.5%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=8.600000381&gt;8.600000381&lt;/td&gt;&lt;td&gt;831&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.5%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=405&gt;405&lt;/td&gt;&lt;td&gt;824&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.5%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=18000&gt;18000&lt;/td&gt;&lt;td&gt;793&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.5%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=28700&gt;28700&lt;/td&gt;&lt;td&gt;580&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.4%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=8&gt;8&lt;/td&gt;&lt;td&gt;572&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.4%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=250&gt;250&lt;/td&gt;&lt;td&gt;544&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=26000&gt;26000&lt;/td&gt;&lt;td&gt;511&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=11.19999981&gt;11.19999981&lt;/td&gt;&lt;td&gt;502&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=6800&gt;6800&lt;/td&gt;&lt;td&gt;487&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=6.800000191&gt;6.800000191&lt;/td&gt;&lt;td&gt;481&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=100000&gt;100000&lt;/td&gt;&lt;td&gt;459&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.3%&gt; &amp;nbsp; &lt;/div&gt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=2&gt;2&lt;/td&gt;&lt;td&gt;386&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=5200&gt;5200&lt;/td&gt;&lt;td&gt;316&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=4000&gt;4000&lt;/td&gt;&lt;td&gt;305&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=13500&gt;13500&lt;/td&gt;&lt;td&gt;293&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=13.19999981&gt;13.19999981&lt;/td&gt;&lt;td&gt;285&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=27000&gt;27000&lt;/td&gt;&lt;td&gt;281&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1750&gt;1750&lt;/td&gt;&lt;td&gt;275&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=3&gt;3&lt;/td&gt;&lt;td&gt;259&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=24000&gt;24000&lt;/td&gt;&lt;td&gt;257&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=500&gt;500&lt;/td&gt;&lt;td&gt;249&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=15.30000019&gt;15.30000019&lt;/td&gt;&lt;td&gt;247&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.2%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=750000&gt;750000&lt;/td&gt;&lt;td&gt;226&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=2000&gt;2000&lt;/td&gt;&lt;td&gt;213&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=27700&gt;27700&lt;/td&gt;&lt;td&gt;212&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1000&gt;1000&lt;/td&gt;&lt;td&gt;195&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=700&gt;700&lt;/td&gt;&lt;td&gt;175&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=7200&gt;7200&lt;/td&gt;&lt;td&gt;173&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=200&gt;200&lt;/td&gt;&lt;td&gt;171&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=25400&gt;25400&lt;/td&gt;&lt;td&gt;160&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1080&gt;1080&lt;/td&gt;&lt;td&gt;158&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1&gt;1&lt;/td&gt;&lt;td&gt;149&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=2000000&gt;2000000&lt;/td&gt;&lt;td&gt;143&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=29500&gt;29500&lt;/td&gt;&lt;td&gt;137&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=8.399999619&gt;8.399999619&lt;/td&gt;&lt;td&gt;131&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1250&gt;1250&lt;/td&gt;&lt;td&gt;129&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=11000&gt;11000&lt;/td&gt;&lt;td&gt;126&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=0.5&gt;0.5&lt;/td&gt;&lt;td&gt;122&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=14&gt;14&lt;/td&gt;&lt;td&gt;122&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=21700&gt;21700&lt;/td&gt;&lt;td&gt;118&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=9000&gt;9000&lt;/td&gt;&lt;td&gt;114&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=15&gt;15&lt;/td&gt;&lt;td&gt;112&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=300&gt;300&lt;/td&gt;&lt;td&gt;112&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=32000&gt;32000&lt;/td&gt;&lt;td&gt;108&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=12&gt;12&lt;/td&gt;&lt;td&gt;106&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=23300&gt;23300&lt;/td&gt;&lt;td&gt;104&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=25000&gt;25000&lt;/td&gt;&lt;td&gt;97&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=25600&gt;25600&lt;/td&gt;&lt;td&gt;97&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=25800&gt;25800&lt;/td&gt;&lt;td&gt;93&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=25200&gt;25200&lt;/td&gt;&lt;td&gt;93&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=44&gt;44&lt;/td&gt;&lt;td&gt;91&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=21000&gt;21000&lt;/td&gt;&lt;td&gt;85&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=2.5&gt;2.5&lt;/td&gt;&lt;td&gt;81&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=22200&gt;22200&lt;/td&gt;&lt;td&gt;78&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=13000&gt;13000&lt;/td&gt;&lt;td&gt;76&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=2800&gt;2800&lt;/td&gt;&lt;td&gt;75&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=7500&gt;7500&lt;/td&gt;&lt;td&gt;73&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=25500&gt;25500&lt;/td&gt;&lt;td&gt;72&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=36000&gt;36000&lt;/td&gt;&lt;td&gt;71&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class=other&gt;&lt;td title=&quot;Other values (253)&quot;&gt;Other values (253)&lt;/td&gt;&lt;td&gt;2460&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:1.6%&gt; &amp;nbsp; &lt;/div&gt; 0.3% &lt;/td&gt;&lt;/tr&gt;&lt;tr class=missing&gt;&lt;td title=(Missing)&gt;(Missing)&lt;/td&gt;&lt;td&gt;1892&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:1.2%&gt; &amp;nbsp; &lt;/div&gt; 0.2% &lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12&quot; id=8124034662335410336bottom-8124034662335410336extreme_values&gt;&lt;div class=&quot;row spacing&quot;&gt;&lt;ul class=&quot;nav nav-tabs&quot; role=tablist&gt;&lt;li role=presentation class=active&gt;&lt;a href=#8124034662335410336extreme_values-8124034662335410336firstn aria-controls=8124034662335410336extreme_values-8124034662335410336firstn role=tab data-toggle=tab&gt;Minimum 10 values&lt;/a&gt;&lt;/li&gt;&lt;li role=presentation&gt;&lt;a href=#8124034662335410336extreme_values-8124034662335410336lastn aria-controls=8124034662335410336extreme_values-8124034662335410336lastn role=tab data-toggle=tab&gt;Maximum 10 values&lt;/a&gt;&lt;/li&gt;&lt;/ul&gt;&lt;div class=tab-content&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12 active&quot; id=8124034662335410336extreme_values-8124034662335410336firstn&gt;&lt;table class=&quot;freq table table-hover table-striped&quot;&gt;&lt;thead&gt;&lt;tr&gt;&lt;td&gt;Value&lt;/td&gt;&lt;td&gt;Count&lt;/td&gt;&lt;td&gt;Frequency (%)&lt;/td&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr class&gt;&lt;td title=-1&gt;-1&lt;/td&gt;&lt;td&gt;22602&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt; 2.6% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=0.01099999994&gt;0.01099999994&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=0.01600000076&gt;0.01600000076&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=0.01799999923&gt;0.01799999923&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=0.1000000015&gt;0.1000000015&lt;/td&gt;&lt;td&gt;19&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=0.200000003&gt;0.200000003&lt;/td&gt;&lt;td&gt;8&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=0.224999994&gt;0.224999994&lt;/td&gt;&lt;td&gt;14&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.1%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=0.3039999902&gt;0.3039999902&lt;/td&gt;&lt;td&gt;8&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=0.3300000131&gt;0.3300000131&lt;/td&gt;&lt;td&gt;4&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=0.400000006&gt;0.400000006&lt;/td&gt;&lt;td&gt;8&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12&quot; id=8124034662335410336extreme_values-8124034662335410336lastn&gt;&lt;table class=&quot;freq table table-hover table-striped&quot;&gt;&lt;thead&gt;&lt;tr&gt;&lt;td&gt;Value&lt;/td&gt;&lt;td&gt;Count&lt;/td&gt;&lt;td&gt;Frequency (%)&lt;/td&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr class&gt;&lt;td title=21800000&gt;21800000&lt;/td&gt;&lt;td&gt;2&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.9%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=18000000&gt;18000000&lt;/td&gt;&lt;td&gt;2&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.9%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=2000000&gt;2000000&lt;/td&gt;&lt;td&gt;143&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:63.3%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1600000&gt;1600000&lt;/td&gt;&lt;td&gt;2&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.9%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=972000&gt;972000&lt;/td&gt;&lt;td&gt;6&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:2.7%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=750000&gt;750000&lt;/td&gt;&lt;td&gt;226&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=500000&gt;500000&lt;/td&gt;&lt;td&gt;23&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:10.2%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=400000&gt;400000&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.4%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=222000&gt;222000&lt;/td&gt;&lt;td&gt;2&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.9%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=200000&gt;200000&lt;/td&gt;&lt;td&gt;13&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:5.8%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;div class=&quot;row spacing&quot;&gt;&lt;a class=&quot;anchor-pos anchor-pos-variable&quot; id=pp_var_-9099077803151007301&gt;&lt;/a&gt;&lt;div class=variable&gt;&lt;div class=col-sm-3&gt;&lt;p class=h4 title=Id&gt;&lt;a href=#pp_var_-9099077803151007301&gt;Id&lt;/a&gt;&lt;br&gt;&lt;small&gt;Real number (&amp;Ropf;&lt;sub&gt;&amp;ge;0&lt;/sub&gt;)&lt;/small&gt;&lt;/p&gt;&lt;code&gt;UNIQUE&lt;/code&gt;&lt;br&gt;&lt;p class=variable-description&gt;&lt;/p&gt;&lt;/div&gt;&lt;div class=col-sm-3&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr class=alert&gt;&lt;th&gt;Distinct&lt;/th&gt;&lt;td&gt;879159&lt;/td&gt;&lt;/tr&gt;&lt;tr class=alert&gt;&lt;th&gt;Distinct (%)&lt;/th&gt;&lt;td&gt;100.0%&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Missing&lt;/th&gt;&lt;td&gt;0&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Missing (%)&lt;/th&gt;&lt;td&gt;0.0%&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Infinite&lt;/th&gt;&lt;td&gt;0&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Infinite (%)&lt;/th&gt;&lt;td&gt;0.0%&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Mean&lt;/th&gt;&lt;td&gt;439579&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div class=col-sm-3&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;Minimum&lt;/th&gt;&lt;td&gt;0&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Maximum&lt;/th&gt;&lt;td&gt;879158&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Zeros&lt;/th&gt;&lt;td&gt;1&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Zeros (%)&lt;/th&gt;&lt;td&gt;&lt; 0.1%&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Negative&lt;/th&gt;&lt;td&gt;0&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Negative (%)&lt;/th&gt;&lt;td&gt;0.0%&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Memory size&lt;/th&gt;&lt;td&gt;6.7 MiB&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div class=col-sm-3&gt;&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot; standalone=&quot;no&quot;?&gt;&lt;!DOCTYPE svg class=&quot;img-responsive center-img&quot;PUBLIC &quot;-//W3C//DTD SVG 1.1//EN&quot;
  &quot;http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd&quot;&gt;&lt;svg class=&quot;img-responsive center-img&quot; xmlns:xlink=http://www.w3.org/1999/xlink width=216pt height=162pt viewbox=&quot;0 0 216 162&quot; xmlns=http://www.w3.org/2000/svg version=1.1&gt;&lt;metadata&gt;&lt;rdf:rdf xmlns:dc=http://purl.org/dc/elements/1.1/ xmlns:cc=http://creativecommons.org/ns# xmlns:rdf=http://www.w3.org/1999/02/22-rdf-syntax-ns#&gt;&lt;cc:work&gt;&lt;dc:type rdf:resource=http://purl.org/dc/dcmitype/StillImage /&gt;&lt;dc:date&gt;2022-07-12T13:06:42.157534&lt;/dc:date&gt;&lt;dc:format&gt;image/svg+xml&lt;/dc:format&gt;&lt;dc:creator&gt;&lt;cc:agent&gt;&lt;dc:title&gt;Matplotlib v3.5.2, https://matplotlib.org/&lt;/dc:title&gt;&lt;/cc:agent&gt;&lt;/dc:creator&gt;&lt;/cc:work&gt;&lt;/rdf:rdf&gt;&lt;/metadata&gt;&lt;defs&gt;&lt;style type=text/css&gt;*{stroke-linejoin: round; stroke-linecap: butt}&lt;/style&gt;&lt;/defs&gt;&lt;g id=figure_1&gt;&lt;g id=patch_1&gt;&lt;path d=&quot;M 0 162 
L 216 162 
L 216 0 
L 0 0 
z
&quot; style=&quot;fill: #ffffff&quot;/&gt;&lt;/g&gt;&lt;g id=axes_1&gt;&lt;g id=patch_2&gt;&lt;path d=&quot;M 10.8 116.898786 
L 205.2 116.898786 
L 205.2 10.8 
L 10.8 10.8 
z
&quot; style=&quot;fill: #ffffff&quot;/&gt;&lt;/g&gt;&lt;g id=matplotlib.axis_1&gt;&lt;g id=xtick_1&gt;&lt;g id=text_1&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(19.525878 134.593597)rotate(-45)scale(0.08 -0.08)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-30 transform=scale(0.015625) d=&quot;M 266 2259 
Q 266 3072 433 3567 
Q 600 4063 929 4331 
Q 1259 4600 1759 4600 
Q 2128 4600 2406 4451 
Q 2684 4303 2865 4023 
Q 3047 3744 3150 3342 
Q 3253 2941 3253 2259 
Q 3253 1453 3087 958 
Q 2922 463 2592 192 
Q 2263 -78 1759 -78 
Q 1097 -78 719 397 
Q 266 969 266 2259 
z
M 844 2259 
Q 844 1131 1108 757 
Q 1372 384 1759 384 
Q 2147 384 2411 759 
Q 2675 1134 2675 2259 
Q 2675 3391 2411 3762 
Q 2147 4134 1753 4134 
Q 1366 4134 1134 3806 
Q 844 3388 844 2259 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-30 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_2&gt;&lt;g id=text_2&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(51.865282 150.322304)rotate(-45)scale(0.08 -0.08)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-32 transform=scale(0.015625) d=&quot;M 3222 541 
L 3222 0 
L 194 0 
Q 188 203 259 391 
Q 375 700 629 1000 
Q 884 1300 1366 1694 
Q 2113 2306 2375 2664 
Q 2638 3022 2638 3341 
Q 2638 3675 2398 3904 
Q 2159 4134 1775 4134 
Q 1369 4134 1125 3890 
Q 881 3647 878 3216 
L 300 3275 
Q 359 3922 746 4261 
Q 1134 4600 1788 4600 
Q 2447 4600 2831 4234 
Q 3216 3869 3216 3328 
Q 3216 3053 3103 2787 
Q 2991 2522 2730 2228 
Q 2469 1934 1863 1422 
Q 1356 997 1212 845 
Q 1069 694 975 541 
L 3222 541 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-32 /&gt;&lt;use xlink:href=#ArialMT-30 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-30 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-30 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_3&gt;&lt;g id=text_3&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(92.069039 150.322304)rotate(-45)scale(0.08 -0.08)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-34 transform=scale(0.015625) d=&quot;M 2069 0 
L 2069 1097 
L 81 1097 
L 81 1613 
L 2172 4581 
L 2631 4581 
L 2631 1613 
L 3250 1613 
L 3250 1097 
L 2631 1097 
L 2631 0 
L 2069 0 
z
M 2069 1613 
L 2069 3678 
L 634 1613 
L 2069 1613 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-34 /&gt;&lt;use xlink:href=#ArialMT-30 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-30 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-30 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_4&gt;&lt;g id=text_4&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(132.272796 150.322304)rotate(-45)scale(0.08 -0.08)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-36 transform=scale(0.015625) d=&quot;M 3184 3459 
L 2625 3416 
Q 2550 3747 2413 3897 
Q 2184 4138 1850 4138 
Q 1581 4138 1378 3988 
Q 1113 3794 959 3422 
Q 806 3050 800 2363 
Q 1003 2672 1297 2822 
Q 1591 2972 1913 2972 
Q 2475 2972 2870 2558 
Q 3266 2144 3266 1488 
Q 3266 1056 3080 686 
Q 2894 316 2569 119 
Q 2244 -78 1831 -78 
Q 1128 -78 684 439 
Q 241 956 241 2144 
Q 241 3472 731 4075 
Q 1159 4600 1884 4600 
Q 2425 4600 2770 4297 
Q 3116 3994 3184 3459 
z
M 888 1484 
Q 888 1194 1011 928 
Q 1134 663 1356 523 
Q 1578 384 1822 384 
Q 2178 384 2434 671 
Q 2691 959 2691 1453 
Q 2691 1928 2437 2201 
Q 2184 2475 1800 2475 
Q 1419 2475 1153 2201 
Q 888 1928 888 1484 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-36 /&gt;&lt;use xlink:href=#ArialMT-30 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-30 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-30 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_5&gt;&lt;g id=text_5&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(172.476553 150.322304)rotate(-45)scale(0.08 -0.08)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-38 transform=scale(0.015625) d=&quot;M 1131 2484 
Q 781 2613 612 2850 
Q 444 3088 444 3419 
Q 444 3919 803 4259 
Q 1163 4600 1759 4600 
Q 2359 4600 2725 4251 
Q 3091 3903 3091 3403 
Q 3091 3084 2923 2848 
Q 2756 2613 2416 2484 
Q 2838 2347 3058 2040 
Q 3278 1734 3278 1309 
Q 3278 722 2862 322 
Q 2447 -78 1769 -78 
Q 1091 -78 675 323 
Q 259 725 259 1325 
Q 259 1772 486 2073 
Q 713 2375 1131 2484 
z
M 1019 3438 
Q 1019 3113 1228 2906 
Q 1438 2700 1772 2700 
Q 2097 2700 2305 2904 
Q 2513 3109 2513 3406 
Q 2513 3716 2298 3927 
Q 2084 4138 1766 4138 
Q 1444 4138 1231 3931 
Q 1019 3725 1019 3438 
z
M 838 1322 
Q 838 1081 952 856 
Q 1066 631 1291 507 
Q 1516 384 1775 384 
Q 2178 384 2440 643 
Q 2703 903 2703 1303 
Q 2703 1709 2433 1975 
Q 2163 2241 1756 2241 
Q 1359 2241 1098 1978 
Q 838 1716 838 1322 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-38 /&gt;&lt;use xlink:href=#ArialMT-30 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-30 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-30 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=patch_3&gt;&lt;path d=&quot;M 19.636364 116.898786 
L 23.170909 116.898786 
L 23.170909 15.852323 
L 19.636364 15.852323 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_4&gt;&lt;path d=&quot;M 23.170909 116.898786 
L 26.705455 116.898786 
L 26.705455 15.85807 
L 23.170909 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_5&gt;&lt;path d=&quot;M 26.705455 116.898786 
L 30.24 116.898786 
L 30.24 15.85807 
L 26.705455 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_6&gt;&lt;path d=&quot;M 30.24 116.898786 
L 33.774545 116.898786 
L 33.774545 15.85807 
L 30.24 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_7&gt;&lt;path d=&quot;M 33.774545 116.898786 
L 37.309091 116.898786 
L 37.309091 15.85807 
L 33.774545 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_8&gt;&lt;path d=&quot;M 37.309091 116.898786 
L 40.843636 116.898786 
L 40.843636 15.85807 
L 37.309091 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_9&gt;&lt;path d=&quot;M 40.843636 116.898786 
L 44.378182 116.898786 
L 44.378182 15.852323 
L 40.843636 15.852323 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_10&gt;&lt;path d=&quot;M 44.378182 116.898786 
L 47.912727 116.898786 
L 47.912727 15.85807 
L 44.378182 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_11&gt;&lt;path d=&quot;M 47.912727 116.898786 
L 51.447273 116.898786 
L 51.447273 15.85807 
L 47.912727 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_12&gt;&lt;path d=&quot;M 51.447273 116.898786 
L 54.981818 116.898786 
L 54.981818 15.85807 
L 51.447273 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_13&gt;&lt;path d=&quot;M 54.981818 116.898786 
L 58.516364 116.898786 
L 58.516364 15.85807 
L 54.981818 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_14&gt;&lt;path d=&quot;M 58.516364 116.898786 
L 62.050909 116.898786 
L 62.050909 15.85807 
L 58.516364 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_15&gt;&lt;path d=&quot;M 62.050909 116.898786 
L 65.585455 116.898786 
L 65.585455 15.852323 
L 62.050909 15.852323 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_16&gt;&lt;path d=&quot;M 65.585455 116.898786 
L 69.12 116.898786 
L 69.12 15.85807 
L 65.585455 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_17&gt;&lt;path d=&quot;M 69.12 116.898786 
L 72.654545 116.898786 
L 72.654545 15.85807 
L 69.12 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_18&gt;&lt;path d=&quot;M 72.654545 116.898786 
L 76.189091 116.898786 
L 76.189091 15.85807 
L 72.654545 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_19&gt;&lt;path d=&quot;M 76.189091 116.898786 
L 79.723636 116.898786 
L 79.723636 15.85807 
L 76.189091 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_20&gt;&lt;path d=&quot;M 79.723636 116.898786 
L 83.258182 116.898786 
L 83.258182 15.85807 
L 79.723636 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_21&gt;&lt;path d=&quot;M 83.258182 116.898786 
L 86.792727 116.898786 
L 86.792727 15.852323 
L 83.258182 15.852323 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_22&gt;&lt;path d=&quot;M 86.792727 116.898786 
L 90.327273 116.898786 
L 90.327273 15.85807 
L 86.792727 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_23&gt;&lt;path d=&quot;M 90.327273 116.898786 
L 93.861818 116.898786 
L 93.861818 15.85807 
L 90.327273 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_24&gt;&lt;path d=&quot;M 93.861818 116.898786 
L 97.396364 116.898786 
L 97.396364 15.85807 
L 93.861818 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_25&gt;&lt;path d=&quot;M 97.396364 116.898786 
L 100.930909 116.898786 
L 100.930909 15.85807 
L 97.396364 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_26&gt;&lt;path d=&quot;M 100.930909 116.898786 
L 104.465455 116.898786 
L 104.465455 15.85807 
L 100.930909 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_27&gt;&lt;path d=&quot;M 104.465455 116.898786 
L 108 116.898786 
L 108 15.85807 
L 104.465455 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_28&gt;&lt;path d=&quot;M 108 116.898786 
L 111.534545 116.898786 
L 111.534545 15.852323 
L 108 15.852323 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_29&gt;&lt;path d=&quot;M 111.534545 116.898786 
L 115.069091 116.898786 
L 115.069091 15.85807 
L 111.534545 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_30&gt;&lt;path d=&quot;M 115.069091 116.898786 
L 118.603636 116.898786 
L 118.603636 15.85807 
L 115.069091 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_31&gt;&lt;path d=&quot;M 118.603636 116.898786 
L 122.138182 116.898786 
L 122.138182 15.85807 
L 118.603636 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_32&gt;&lt;path d=&quot;M 122.138182 116.898786 
L 125.672727 116.898786 
L 125.672727 15.85807 
L 122.138182 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_33&gt;&lt;path d=&quot;M 125.672727 116.898786 
L 129.207273 116.898786 
L 129.207273 15.85807 
L 125.672727 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_34&gt;&lt;path d=&quot;M 129.207273 116.898786 
L 132.741818 116.898786 
L 132.741818 15.852323 
L 129.207273 15.852323 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_35&gt;&lt;path d=&quot;M 132.741818 116.898786 
L 136.276364 116.898786 
L 136.276364 15.85807 
L 132.741818 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_36&gt;&lt;path d=&quot;M 136.276364 116.898786 
L 139.810909 116.898786 
L 139.810909 15.85807 
L 136.276364 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_37&gt;&lt;path d=&quot;M 139.810909 116.898786 
L 143.345455 116.898786 
L 143.345455 15.85807 
L 139.810909 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_38&gt;&lt;path d=&quot;M 143.345455 116.898786 
L 146.88 116.898786 
L 146.88 15.85807 
L 143.345455 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_39&gt;&lt;path d=&quot;M 146.88 116.898786 
L 150.414545 116.898786 
L 150.414545 15.85807 
L 146.88 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_40&gt;&lt;path d=&quot;M 150.414545 116.898786 
L 153.949091 116.898786 
L 153.949091 15.852323 
L 150.414545 15.852323 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_41&gt;&lt;path d=&quot;M 153.949091 116.898786 
L 157.483636 116.898786 
L 157.483636 15.85807 
L 153.949091 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_42&gt;&lt;path d=&quot;M 157.483636 116.898786 
L 161.018182 116.898786 
L 161.018182 15.85807 
L 157.483636 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_43&gt;&lt;path d=&quot;M 161.018182 116.898786 
L 164.552727 116.898786 
L 164.552727 15.85807 
L 161.018182 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_44&gt;&lt;path d=&quot;M 164.552727 116.898786 
L 168.087273 116.898786 
L 168.087273 15.85807 
L 164.552727 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_45&gt;&lt;path d=&quot;M 168.087273 116.898786 
L 171.621818 116.898786 
L 171.621818 15.85807 
L 168.087273 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_46&gt;&lt;path d=&quot;M 171.621818 116.898786 
L 175.156364 116.898786 
L 175.156364 15.852323 
L 171.621818 15.852323 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_47&gt;&lt;path d=&quot;M 175.156364 116.898786 
L 178.690909 116.898786 
L 178.690909 15.85807 
L 175.156364 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_48&gt;&lt;path d=&quot;M 178.690909 116.898786 
L 182.225455 116.898786 
L 182.225455 15.85807 
L 178.690909 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_49&gt;&lt;path d=&quot;M 182.225455 116.898786 
L 185.76 116.898786 
L 185.76 15.85807 
L 182.225455 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_50&gt;&lt;path d=&quot;M 185.76 116.898786 
L 189.294545 116.898786 
L 189.294545 15.85807 
L 185.76 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_51&gt;&lt;path d=&quot;M 189.294545 116.898786 
L 192.829091 116.898786 
L 192.829091 15.85807 
L 189.294545 15.85807 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_52&gt;&lt;path d=&quot;M 192.829091 116.898786 
L 196.363636 116.898786 
L 196.363636 15.852323 
L 192.829091 15.852323 
z
&quot; clip-path=url(#p66119985e8) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_53&gt;&lt;path d=&quot;M 10.8 116.898786 
L 10.8 10.8 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;g id=patch_54&gt;&lt;path d=&quot;M 205.2 116.898786 
L 205.2 10.8 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;g id=patch_55&gt;&lt;path d=&quot;M 10.8 116.898786 
L 205.2 116.898786 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;g id=patch_56&gt;&lt;path d=&quot;M 10.8 10.8 
L 205.2 10.8 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;defs&gt;&lt;clippath id=p66119985e8&gt;&lt;rect x=10.8 y=10.8 width=194.4 height=106.098786 /&gt;&lt;/clippath&gt;&lt;/defs&gt;&lt;/svg&gt;&lt;/div&gt;&lt;div class=&quot;col-sm-12 text-right&quot;&gt;&lt;button class=&quot;btn btn-default btn-sm&quot; data-toggle=collapse data-target=&quot;#bottom--9099077803151007301, #minifreqtable-9099077803151007301&quot; aria-expanded=true aria-controls=collapseExample&gt;Toggle details&lt;/button&gt;&lt;/div&gt;&lt;div id=bottom--9099077803151007301 class=collapse&gt;&lt;div class=&quot;row spacing&quot;&gt;&lt;ul class=&quot;nav nav-tabs&quot; role=tablist&gt;&lt;li role=presentation class=active&gt;&lt;a href=#-9099077803151007301bottom--9099077803151007301statistics aria-controls=-9099077803151007301bottom--9099077803151007301statistics role=tab data-toggle=tab&gt;Statistics&lt;/a&gt;&lt;/li&gt;&lt;li role=presentation&gt;&lt;a href=#-9099077803151007301bottom--9099077803151007301histogram aria-controls=-9099077803151007301bottom--9099077803151007301histogram role=tab data-toggle=tab&gt;Histogram&lt;/a&gt;&lt;/li&gt;&lt;li role=presentation&gt;&lt;a href=#-9099077803151007301bottom--9099077803151007301common_values aria-controls=-9099077803151007301bottom--9099077803151007301common_values role=tab data-toggle=tab&gt;Common values&lt;/a&gt;&lt;/li&gt;&lt;li role=presentation&gt;&lt;a href=#-9099077803151007301bottom--9099077803151007301extreme_values aria-controls=-9099077803151007301bottom--9099077803151007301extreme_values role=tab data-toggle=tab&gt;Extreme values&lt;/a&gt;&lt;/li&gt;&lt;/ul&gt;&lt;div class=tab-content&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12 active&quot; id=-9099077803151007301bottom--9099077803151007301statistics&gt;&lt;div class=col-sm-6&gt;&lt;p class=h4&gt;Quantile statistics&lt;/p&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;Minimum&lt;/th&gt;&lt;td&gt;0&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;5-th percentile&lt;/th&gt;&lt;td&gt;43957.9&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Q1&lt;/th&gt;&lt;td&gt;219789.5&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;median&lt;/th&gt;&lt;td&gt;439579&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Q3&lt;/th&gt;&lt;td&gt;659368.5&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;95-th percentile&lt;/th&gt;&lt;td&gt;835200.1&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Maximum&lt;/th&gt;&lt;td&gt;879158&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Range&lt;/th&gt;&lt;td&gt;879158&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Interquartile range (IQR)&lt;/th&gt;&lt;td&gt;439579&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div class=col-sm-6&gt;&lt;p class=h4&gt;Descriptive statistics&lt;/p&gt;&lt;table class=&quot;table table-condensed stats&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;Standard deviation&lt;/th&gt;&lt;td&gt;253791.487&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Coefficient of variation (CV)&lt;/th&gt;&lt;td&gt;0.5773512543&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Kurtosis&lt;/th&gt;&lt;td&gt;-1.2&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Mean&lt;/th&gt;&lt;td&gt;439579&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Median Absolute Deviation (MAD)&lt;/th&gt;&lt;td&gt;219790&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Skewness&lt;/th&gt;&lt;td&gt;-1.345255732 × 10&lt;sup&gt;-16&lt;/sup&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Sum&lt;/th&gt;&lt;td&gt;3.864598341 × 10&lt;sup&gt;11&lt;/sup&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Variance&lt;/th&gt;&lt;td&gt;6.441011887 × 10&lt;sup&gt;10&lt;/sup&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;Monotonicity&lt;/th&gt;&lt;td&gt;Not monotonic&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;/div&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12&quot; id=-9099077803151007301bottom--9099077803151007301histogram&gt;&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot; standalone=&quot;no&quot;?&gt;&lt;!DOCTYPE svg class=&quot;img-responsive center-img&quot;PUBLIC &quot;-//W3C//DTD SVG 1.1//EN&quot;
  &quot;http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd&quot;&gt;&lt;svg class=&quot;img-responsive center-img&quot; xmlns:xlink=http://www.w3.org/1999/xlink width=432pt height=288pt viewbox=&quot;0 0 432 288&quot; xmlns=http://www.w3.org/2000/svg version=1.1&gt;&lt;metadata&gt;&lt;rdf:rdf xmlns:dc=http://purl.org/dc/elements/1.1/ xmlns:cc=http://creativecommons.org/ns# xmlns:rdf=http://www.w3.org/1999/02/22-rdf-syntax-ns#&gt;&lt;cc:work&gt;&lt;dc:type rdf:resource=http://purl.org/dc/dcmitype/StillImage /&gt;&lt;dc:date&gt;2022-07-12T13:06:42.334033&lt;/dc:date&gt;&lt;dc:format&gt;image/svg+xml&lt;/dc:format&gt;&lt;dc:creator&gt;&lt;cc:agent&gt;&lt;dc:title&gt;Matplotlib v3.5.2, https://matplotlib.org/&lt;/dc:title&gt;&lt;/cc:agent&gt;&lt;/dc:creator&gt;&lt;/cc:work&gt;&lt;/rdf:rdf&gt;&lt;/metadata&gt;&lt;defs&gt;&lt;style type=text/css&gt;*{stroke-linejoin: round; stroke-linecap: butt}&lt;/style&gt;&lt;/defs&gt;&lt;g id=figure_1&gt;&lt;g id=patch_1&gt;&lt;path d=&quot;M 0 288 
L 432 288 
L 432 0 
L 0 0 
z
&quot; style=&quot;fill: #ffffff&quot;/&gt;&lt;/g&gt;&lt;g id=axes_1&gt;&lt;g id=patch_2&gt;&lt;path d=&quot;M 63.28 236.916662 
L 421.2 236.916662 
L 421.2 10.8 
L 63.28 10.8 
z
&quot; style=&quot;fill: #ffffff&quot;/&gt;&lt;/g&gt;&lt;g id=matplotlib.axis_1&gt;&lt;g id=xtick_1&gt;&lt;g id=text_1&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(79.410984 256.410177)rotate(-45)scale(0.1 -0.1)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-30 transform=scale(0.015625) d=&quot;M 266 2259 
Q 266 3072 433 3567 
Q 600 4063 929 4331 
Q 1259 4600 1759 4600 
Q 2128 4600 2406 4451 
Q 2684 4303 2865 4023 
Q 3047 3744 3150 3342 
Q 3253 2941 3253 2259 
Q 3253 1453 3087 958 
Q 2922 463 2592 192 
Q 2263 -78 1759 -78 
Q 1097 -78 719 397 
Q 266 969 266 2259 
z
M 844 2259 
Q 844 1131 1108 757 
Q 1372 384 1759 384 
Q 2147 384 2411 759 
Q 2675 1134 2675 2259 
Q 2675 3391 2411 3762 
Q 2147 4134 1753 4134 
Q 1366 4134 1134 3806 
Q 844 3388 844 2259 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-30 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_2&gt;&lt;g id=text_2&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(143.601781 276.07106)rotate(-45)scale(0.1 -0.1)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-32 transform=scale(0.015625) d=&quot;M 3222 541 
L 3222 0 
L 194 0 
Q 188 203 259 391 
Q 375 700 629 1000 
Q 884 1300 1366 1694 
Q 2113 2306 2375 2664 
Q 2638 3022 2638 3341 
Q 2638 3675 2398 3904 
Q 2159 4134 1775 4134 
Q 1369 4134 1125 3890 
Q 881 3647 878 3216 
L 300 3275 
Q 359 3922 746 4261 
Q 1134 4600 1788 4600 
Q 2447 4600 2831 4234 
Q 3216 3869 3216 3328 
Q 3216 3053 3103 2787 
Q 2991 2522 2730 2228 
Q 2469 1934 1863 1422 
Q 1356 997 1212 845 
Q 1069 694 975 541 
L 3222 541 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-32 /&gt;&lt;use xlink:href=#ArialMT-30 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-30 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-30 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_3&gt;&lt;g id=text_3&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(217.623019 276.07106)rotate(-45)scale(0.1 -0.1)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-34 transform=scale(0.015625) d=&quot;M 2069 0 
L 2069 1097 
L 81 1097 
L 81 1613 
L 2172 4581 
L 2631 4581 
L 2631 1613 
L 3250 1613 
L 3250 1097 
L 2631 1097 
L 2631 0 
L 2069 0 
z
M 2069 1613 
L 2069 3678 
L 634 1613 
L 2069 1613 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-34 /&gt;&lt;use xlink:href=#ArialMT-30 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-30 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-30 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_4&gt;&lt;g id=text_4&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(291.644257 276.07106)rotate(-45)scale(0.1 -0.1)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-36 transform=scale(0.015625) d=&quot;M 3184 3459 
L 2625 3416 
Q 2550 3747 2413 3897 
Q 2184 4138 1850 4138 
Q 1581 4138 1378 3988 
Q 1113 3794 959 3422 
Q 806 3050 800 2363 
Q 1003 2672 1297 2822 
Q 1591 2972 1913 2972 
Q 2475 2972 2870 2558 
Q 3266 2144 3266 1488 
Q 3266 1056 3080 686 
Q 2894 316 2569 119 
Q 2244 -78 1831 -78 
Q 1128 -78 684 439 
Q 241 956 241 2144 
Q 241 3472 731 4075 
Q 1159 4600 1884 4600 
Q 2425 4600 2770 4297 
Q 3116 3994 3184 3459 
z
M 888 1484 
Q 888 1194 1011 928 
Q 1134 663 1356 523 
Q 1578 384 1822 384 
Q 2178 384 2434 671 
Q 2691 959 2691 1453 
Q 2691 1928 2437 2201 
Q 2184 2475 1800 2475 
Q 1419 2475 1153 2201 
Q 888 1928 888 1484 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-36 /&gt;&lt;use xlink:href=#ArialMT-30 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-30 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-30 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_5&gt;&lt;g id=text_5&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(365.665495 276.07106)rotate(-45)scale(0.1 -0.1)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-38 transform=scale(0.015625) d=&quot;M 1131 2484 
Q 781 2613 612 2850 
Q 444 3088 444 3419 
Q 444 3919 803 4259 
Q 1163 4600 1759 4600 
Q 2359 4600 2725 4251 
Q 3091 3903 3091 3403 
Q 3091 3084 2923 2848 
Q 2756 2613 2416 2484 
Q 2838 2347 3058 2040 
Q 3278 1734 3278 1309 
Q 3278 722 2862 322 
Q 2447 -78 1769 -78 
Q 1091 -78 675 323 
Q 259 725 259 1325 
Q 259 1772 486 2073 
Q 713 2375 1131 2484 
z
M 1019 3438 
Q 1019 3113 1228 2906 
Q 1438 2700 1772 2700 
Q 2097 2700 2305 2904 
Q 2513 3109 2513 3406 
Q 2513 3716 2298 3927 
Q 2084 4138 1766 4138 
Q 1444 4138 1231 3931 
Q 1019 3725 1019 3438 
z
M 838 1322 
Q 838 1081 952 856 
Q 1066 631 1291 507 
Q 1516 384 1775 384 
Q 2178 384 2440 643 
Q 2703 903 2703 1303 
Q 2703 1709 2433 1975 
Q 2163 2241 1756 2241 
Q 1359 2241 1098 1978 
Q 838 1716 838 1322 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-38 /&gt;&lt;use xlink:href=#ArialMT-30 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-30 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-30 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=matplotlib.axis_2&gt;&lt;g id=ytick_1&gt;&lt;g id=text_6&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(47.219062 240.495569)scale(0.1 -0.1)&quot;&gt;&lt;use xlink:href=#ArialMT-30 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_2&gt;&lt;g id=text_7&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(30.53625 209.878359)scale(0.1 -0.1)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-35 transform=scale(0.015625) d=&quot;M 266 1200 
L 856 1250 
Q 922 819 1161 601 
Q 1400 384 1738 384 
Q 2144 384 2425 690 
Q 2706 997 2706 1503 
Q 2706 1984 2436 2262 
Q 2166 2541 1728 2541 
Q 1456 2541 1237 2417 
Q 1019 2294 894 2097 
L 366 2166 
L 809 4519 
L 3088 4519 
L 3088 3981 
L 1259 3981 
L 1013 2750 
Q 1425 3038 1878 3038 
Q 2478 3038 2890 2622 
Q 3303 2206 3303 1553 
Q 3303 931 2941 478 
Q 2500 -78 1738 -78 
Q 1113 -78 717 272 
Q 322 622 266 1200 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-32 /&gt;&lt;use xlink:href=#ArialMT-35 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_3&gt;&lt;g id=text_8&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(30.53625 179.26115)scale(0.1 -0.1)&quot;&gt;&lt;use xlink:href=#ArialMT-35 /&gt;&lt;use xlink:href=#ArialMT-30 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_4&gt;&lt;g id=text_9&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(30.53625 148.643941)scale(0.1 -0.1)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-37 transform=scale(0.015625) d=&quot;M 303 3981 
L 303 4522 
L 3269 4522 
L 3269 4084 
Q 2831 3619 2401 2847 
Q 1972 2075 1738 1259 
Q 1569 684 1522 0 
L 944 0 
Q 953 541 1156 1306 
Q 1359 2072 1739 2783 
Q 2119 3494 2547 3981 
L 303 3981 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-37 /&gt;&lt;use xlink:href=#ArialMT-35 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_5&gt;&lt;g id=text_10&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(24.975313 118.026732)scale(0.1 -0.1)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-31 transform=scale(0.015625) d=&quot;M 2384 0 
L 1822 0 
L 1822 3584 
Q 1619 3391 1289 3197 
Q 959 3003 697 2906 
L 697 3450 
Q 1169 3672 1522 3987 
Q 1875 4303 2022 4600 
L 2384 4600 
L 2384 0 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-31 /&gt;&lt;use xlink:href=#ArialMT-30 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-30 x=222.460938 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_6&gt;&lt;g id=text_11&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(24.975313 87.409523)scale(0.1 -0.1)&quot;&gt;&lt;use xlink:href=#ArialMT-31 /&gt;&lt;use xlink:href=#ArialMT-32 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-35 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-30 x=222.460938 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_7&gt;&lt;g id=text_12&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(24.975313 56.792314)scale(0.1 -0.1)&quot;&gt;&lt;use xlink:href=#ArialMT-31 /&gt;&lt;use xlink:href=#ArialMT-35 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-30 x=222.460938 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_8&gt;&lt;g id=text_13&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(24.975313 26.175105)scale(0.1 -0.1)&quot;&gt;&lt;use xlink:href=#ArialMT-31 /&gt;&lt;use xlink:href=#ArialMT-37 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-35 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-30 x=222.460938 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=text_14&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(18.660156 149.841534)rotate(-90)scale(0.11 -0.11)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-46 transform=scale(0.015625) d=&quot;M 525 0 
L 525 4581 
L 3616 4581 
L 3616 4041 
L 1131 4041 
L 1131 2622 
L 3281 2622 
L 3281 2081 
L 1131 2081 
L 1131 0 
L 525 0 
z
&quot;/&gt;&lt;path id=ArialMT-72 transform=scale(0.015625) d=&quot;M 416 0 
L 416 3319 
L 922 3319 
L 922 2816 
Q 1116 3169 1280 3281 
Q 1444 3394 1641 3394 
Q 1925 3394 2219 3213 
L 2025 2691 
Q 1819 2813 1613 2813 
Q 1428 2813 1281 2702 
Q 1134 2591 1072 2394 
Q 978 2094 978 1738 
L 978 0 
L 416 0 
z
&quot;/&gt;&lt;path id=ArialMT-65 transform=scale(0.015625) d=&quot;M 2694 1069 
L 3275 997 
Q 3138 488 2766 206 
Q 2394 -75 1816 -75 
Q 1088 -75 661 373 
Q 234 822 234 1631 
Q 234 2469 665 2931 
Q 1097 3394 1784 3394 
Q 2450 3394 2872 2941 
Q 3294 2488 3294 1666 
Q 3294 1616 3291 1516 
L 816 1516 
Q 847 969 1125 678 
Q 1403 388 1819 388 
Q 2128 388 2347 550 
Q 2566 713 2694 1069 
z
M 847 1978 
L 2700 1978 
Q 2663 2397 2488 2606 
Q 2219 2931 1791 2931 
Q 1403 2931 1139 2672 
Q 875 2413 847 1978 
z
&quot;/&gt;&lt;path id=ArialMT-71 transform=scale(0.015625) d=&quot;M 2538 -1272 
L 2538 353 
Q 2406 169 2170 47 
Q 1934 -75 1669 -75 
Q 1078 -75 651 397 
Q 225 869 225 1691 
Q 225 2191 398 2587 
Q 572 2984 901 3189 
Q 1231 3394 1625 3394 
Q 2241 3394 2594 2875 
L 2594 3319 
L 3100 3319 
L 3100 -1272 
L 2538 -1272 
z
M 803 1669 
Q 803 1028 1072 708 
Q 1341 388 1716 388 
Q 2075 388 2334 692 
Q 2594 997 2594 1619 
Q 2594 2281 2320 2615 
Q 2047 2950 1678 2950 
Q 1313 2950 1058 2639 
Q 803 2328 803 1669 
z
&quot;/&gt;&lt;path id=ArialMT-75 transform=scale(0.015625) d=&quot;M 2597 0 
L 2597 488 
Q 2209 -75 1544 -75 
Q 1250 -75 995 37 
Q 741 150 617 320 
Q 494 491 444 738 
Q 409 903 409 1263 
L 409 3319 
L 972 3319 
L 972 1478 
Q 972 1038 1006 884 
Q 1059 663 1231 536 
Q 1403 409 1656 409 
Q 1909 409 2131 539 
Q 2353 669 2445 892 
Q 2538 1116 2538 1541 
L 2538 3319 
L 3100 3319 
L 3100 0 
L 2597 0 
z
&quot;/&gt;&lt;path id=ArialMT-6e transform=scale(0.015625) d=&quot;M 422 0 
L 422 3319 
L 928 3319 
L 928 2847 
Q 1294 3394 1984 3394 
Q 2284 3394 2536 3286 
Q 2788 3178 2913 3003 
Q 3038 2828 3088 2588 
Q 3119 2431 3119 2041 
L 3119 0 
L 2556 0 
L 2556 2019 
Q 2556 2363 2490 2533 
Q 2425 2703 2258 2804 
Q 2091 2906 1866 2906 
Q 1506 2906 1245 2678 
Q 984 2450 984 1813 
L 984 0 
L 422 0 
z
&quot;/&gt;&lt;path id=ArialMT-63 transform=scale(0.015625) d=&quot;M 2588 1216 
L 3141 1144 
Q 3050 572 2676 248 
Q 2303 -75 1759 -75 
Q 1078 -75 664 370 
Q 250 816 250 1647 
Q 250 2184 428 2587 
Q 606 2991 970 3192 
Q 1334 3394 1763 3394 
Q 2303 3394 2647 3120 
Q 2991 2847 3088 2344 
L 2541 2259 
Q 2463 2594 2264 2762 
Q 2066 2931 1784 2931 
Q 1359 2931 1093 2626 
Q 828 2322 828 1663 
Q 828 994 1084 691 
Q 1341 388 1753 388 
Q 2084 388 2306 591 
Q 2528 794 2588 1216 
z
&quot;/&gt;&lt;path id=ArialMT-79 transform=scale(0.015625) d=&quot;M 397 -1278 
L 334 -750 
Q 519 -800 656 -800 
Q 844 -800 956 -737 
Q 1069 -675 1141 -563 
Q 1194 -478 1313 -144 
Q 1328 -97 1363 -6 
L 103 3319 
L 709 3319 
L 1400 1397 
Q 1534 1031 1641 628 
Q 1738 1016 1872 1384 
L 2581 3319 
L 3144 3319 
L 1881 -56 
Q 1678 -603 1566 -809 
Q 1416 -1088 1222 -1217 
Q 1028 -1347 759 -1347 
Q 597 -1347 397 -1278 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-46 /&gt;&lt;use xlink:href=#ArialMT-72 x=61.083984 /&gt;&lt;use xlink:href=#ArialMT-65 x=94.384766 /&gt;&lt;use xlink:href=#ArialMT-71 x=150 /&gt;&lt;use xlink:href=#ArialMT-75 x=205.615234 /&gt;&lt;use xlink:href=#ArialMT-65 x=261.230469 /&gt;&lt;use xlink:href=#ArialMT-6e x=316.845703 /&gt;&lt;use xlink:href=#ArialMT-63 x=372.460938 /&gt;&lt;use xlink:href=#ArialMT-79 x=422.460938 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=patch_3&gt;&lt;path d=&quot;M 79.549091 236.916662 
L 86.056727 236.916662 
L 86.056727 21.56746 
L 79.549091 21.56746 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_4&gt;&lt;path d=&quot;M 86.056727 236.916662 
L 92.564364 236.916662 
L 92.564364 21.579707 
L 86.056727 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_5&gt;&lt;path d=&quot;M 92.564364 236.916662 
L 99.072 236.916662 
L 99.072 21.579707 
L 92.564364 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_6&gt;&lt;path d=&quot;M 99.072 236.916662 
L 105.579636 236.916662 
L 105.579636 21.579707 
L 99.072 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_7&gt;&lt;path d=&quot;M 105.579636 236.916662 
L 112.087273 236.916662 
L 112.087273 21.579707 
L 105.579636 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_8&gt;&lt;path d=&quot;M 112.087273 236.916662 
L 118.594909 236.916662 
L 118.594909 21.579707 
L 112.087273 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_9&gt;&lt;path d=&quot;M 118.594909 236.916662 
L 125.102545 236.916662 
L 125.102545 21.56746 
L 118.594909 21.56746 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_10&gt;&lt;path d=&quot;M 125.102545 236.916662 
L 131.610182 236.916662 
L 131.610182 21.579707 
L 125.102545 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_11&gt;&lt;path d=&quot;M 131.610182 236.916662 
L 138.117818 236.916662 
L 138.117818 21.579707 
L 131.610182 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_12&gt;&lt;path d=&quot;M 138.117818 236.916662 
L 144.625455 236.916662 
L 144.625455 21.579707 
L 138.117818 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_13&gt;&lt;path d=&quot;M 144.625455 236.916662 
L 151.133091 236.916662 
L 151.133091 21.579707 
L 144.625455 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_14&gt;&lt;path d=&quot;M 151.133091 236.916662 
L 157.640727 236.916662 
L 157.640727 21.579707 
L 151.133091 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_15&gt;&lt;path d=&quot;M 157.640727 236.916662 
L 164.148364 236.916662 
L 164.148364 21.56746 
L 157.640727 21.56746 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_16&gt;&lt;path d=&quot;M 164.148364 236.916662 
L 170.656 236.916662 
L 170.656 21.579707 
L 164.148364 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_17&gt;&lt;path d=&quot;M 170.656 236.916662 
L 177.163636 236.916662 
L 177.163636 21.579707 
L 170.656 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_18&gt;&lt;path d=&quot;M 177.163636 236.916662 
L 183.671273 236.916662 
L 183.671273 21.579707 
L 177.163636 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_19&gt;&lt;path d=&quot;M 183.671273 236.916662 
L 190.178909 236.916662 
L 190.178909 21.579707 
L 183.671273 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_20&gt;&lt;path d=&quot;M 190.178909 236.916662 
L 196.686545 236.916662 
L 196.686545 21.579707 
L 190.178909 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_21&gt;&lt;path d=&quot;M 196.686545 236.916662 
L 203.194182 236.916662 
L 203.194182 21.56746 
L 196.686545 21.56746 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_22&gt;&lt;path d=&quot;M 203.194182 236.916662 
L 209.701818 236.916662 
L 209.701818 21.579707 
L 203.194182 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_23&gt;&lt;path d=&quot;M 209.701818 236.916662 
L 216.209455 236.916662 
L 216.209455 21.579707 
L 209.701818 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_24&gt;&lt;path d=&quot;M 216.209455 236.916662 
L 222.717091 236.916662 
L 222.717091 21.579707 
L 216.209455 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_25&gt;&lt;path d=&quot;M 222.717091 236.916662 
L 229.224727 236.916662 
L 229.224727 21.579707 
L 222.717091 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_26&gt;&lt;path d=&quot;M 229.224727 236.916662 
L 235.732364 236.916662 
L 235.732364 21.579707 
L 229.224727 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_27&gt;&lt;path d=&quot;M 235.732364 236.916662 
L 242.24 236.916662 
L 242.24 21.579707 
L 235.732364 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_28&gt;&lt;path d=&quot;M 242.24 236.916662 
L 248.747636 236.916662 
L 248.747636 21.56746 
L 242.24 21.56746 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_29&gt;&lt;path d=&quot;M 248.747636 236.916662 
L 255.255273 236.916662 
L 255.255273 21.579707 
L 248.747636 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_30&gt;&lt;path d=&quot;M 255.255273 236.916662 
L 261.762909 236.916662 
L 261.762909 21.579707 
L 255.255273 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_31&gt;&lt;path d=&quot;M 261.762909 236.916662 
L 268.270545 236.916662 
L 268.270545 21.579707 
L 261.762909 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_32&gt;&lt;path d=&quot;M 268.270545 236.916662 
L 274.778182 236.916662 
L 274.778182 21.579707 
L 268.270545 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_33&gt;&lt;path d=&quot;M 274.778182 236.916662 
L 281.285818 236.916662 
L 281.285818 21.579707 
L 274.778182 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_34&gt;&lt;path d=&quot;M 281.285818 236.916662 
L 287.793455 236.916662 
L 287.793455 21.56746 
L 281.285818 21.56746 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_35&gt;&lt;path d=&quot;M 287.793455 236.916662 
L 294.301091 236.916662 
L 294.301091 21.579707 
L 287.793455 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_36&gt;&lt;path d=&quot;M 294.301091 236.916662 
L 300.808727 236.916662 
L 300.808727 21.579707 
L 294.301091 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_37&gt;&lt;path d=&quot;M 300.808727 236.916662 
L 307.316364 236.916662 
L 307.316364 21.579707 
L 300.808727 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_38&gt;&lt;path d=&quot;M 307.316364 236.916662 
L 313.824 236.916662 
L 313.824 21.579707 
L 307.316364 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_39&gt;&lt;path d=&quot;M 313.824 236.916662 
L 320.331636 236.916662 
L 320.331636 21.579707 
L 313.824 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_40&gt;&lt;path d=&quot;M 320.331636 236.916662 
L 326.839273 236.916662 
L 326.839273 21.56746 
L 320.331636 21.56746 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_41&gt;&lt;path d=&quot;M 326.839273 236.916662 
L 333.346909 236.916662 
L 333.346909 21.579707 
L 326.839273 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_42&gt;&lt;path d=&quot;M 333.346909 236.916662 
L 339.854545 236.916662 
L 339.854545 21.579707 
L 333.346909 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_43&gt;&lt;path d=&quot;M 339.854545 236.916662 
L 346.362182 236.916662 
L 346.362182 21.579707 
L 339.854545 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_44&gt;&lt;path d=&quot;M 346.362182 236.916662 
L 352.869818 236.916662 
L 352.869818 21.579707 
L 346.362182 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_45&gt;&lt;path d=&quot;M 352.869818 236.916662 
L 359.377455 236.916662 
L 359.377455 21.579707 
L 352.869818 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_46&gt;&lt;path d=&quot;M 359.377455 236.916662 
L 365.885091 236.916662 
L 365.885091 21.56746 
L 359.377455 21.56746 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_47&gt;&lt;path d=&quot;M 365.885091 236.916662 
L 372.392727 236.916662 
L 372.392727 21.579707 
L 365.885091 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_48&gt;&lt;path d=&quot;M 372.392727 236.916662 
L 378.900364 236.916662 
L 378.900364 21.579707 
L 372.392727 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_49&gt;&lt;path d=&quot;M 378.900364 236.916662 
L 385.408 236.916662 
L 385.408 21.579707 
L 378.900364 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_50&gt;&lt;path d=&quot;M 385.408 236.916662 
L 391.915636 236.916662 
L 391.915636 21.579707 
L 385.408 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_51&gt;&lt;path d=&quot;M 391.915636 236.916662 
L 398.423273 236.916662 
L 398.423273 21.579707 
L 391.915636 21.579707 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_52&gt;&lt;path d=&quot;M 398.423273 236.916662 
L 404.930909 236.916662 
L 404.930909 21.56746 
L 398.423273 21.56746 
z
&quot; clip-path=url(#pab09f53fc0) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_53&gt;&lt;path d=&quot;M 63.28 236.916662 
L 63.28 10.8 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;g id=patch_54&gt;&lt;path d=&quot;M 421.2 236.916662 
L 421.2 10.8 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;g id=patch_55&gt;&lt;path d=&quot;M 63.28 236.916662 
L 421.2 236.916662 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;g id=patch_56&gt;&lt;path d=&quot;M 63.28 10.8 
L 421.2 10.8 
&quot; style=&quot;fill: none&quot;/&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;defs&gt;&lt;clippath id=pab09f53fc0&gt;&lt;rect x=63.28 y=10.8 width=357.92 height=226.116662 /&gt;&lt;/clippath&gt;&lt;/defs&gt;&lt;/svg&gt;&lt;div class=&quot;caption text-center text-muted&quot;&gt;&lt;strong&gt;Histogram with fixed size bins&lt;/strong&gt; (bins=50) &lt;/div&gt;&lt;/div&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12&quot; id=-9099077803151007301bottom--9099077803151007301common_values&gt;&lt;table class=&quot;freq table table-hover table-striped&quot;&gt;&lt;thead&gt;&lt;tr&gt;&lt;td&gt;Value&lt;/td&gt;&lt;td&gt;Count&lt;/td&gt;&lt;td&gt;Frequency (%)&lt;/td&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr class&gt;&lt;td title=0&gt;0&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585962&gt;585962&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585916&gt;585916&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585917&gt;585917&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585915&gt;585915&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585914&gt;585914&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585913&gt;585913&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585912&gt;585912&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585911&gt;585911&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585910&gt;585910&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585909&gt;585909&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585908&gt;585908&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585907&gt;585907&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585906&gt;585906&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585905&gt;585905&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585920&gt;585920&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585922&gt;585922&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585939&gt;585939&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585923&gt;585923&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585938&gt;585938&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585937&gt;585937&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585936&gt;585936&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585935&gt;585935&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585934&gt;585934&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585932&gt;585932&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585918&gt;585918&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585942&gt;585942&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585928&gt;585928&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585941&gt;585941&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585943&gt;585943&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585958&gt;585958&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585959&gt;585959&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585960&gt;585960&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585961&gt;585961&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585972&gt;585972&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585973&gt;585973&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585974&gt;585974&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585975&gt;585975&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585976&gt;585976&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585977&gt;585977&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585971&gt;585971&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585978&gt;585978&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585970&gt;585970&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585968&gt;585968&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585965&gt;585965&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585966&gt;585966&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585967&gt;585967&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585963&gt;585963&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585964&gt;585964&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585919&gt;585919&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585921&gt;585921&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585940&gt;585940&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585933&gt;585933&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585929&gt;585929&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586291&gt;586291&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586242&gt;586242&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586222&gt;586222&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586223&gt;586223&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586224&gt;586224&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586225&gt;586225&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586226&gt;586226&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586227&gt;586227&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586228&gt;586228&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586229&gt;586229&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586230&gt;586230&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586240&gt;586240&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586231&gt;586231&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586232&gt;586232&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586233&gt;586233&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586234&gt;586234&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586235&gt;586235&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586236&gt;586236&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586237&gt;586237&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586238&gt;586238&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586239&gt;586239&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586241&gt;586241&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586264&gt;586264&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586265&gt;586265&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586266&gt;586266&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586221&gt;586221&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586263&gt;586263&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585930&gt;585930&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586262&gt;586262&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585931&gt;585931&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585927&gt;585927&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585926&gt;585926&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=585925&gt;585925&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586244&gt;586244&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586245&gt;586245&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586246&gt;586246&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586247&gt;586247&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586248&gt;586248&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586249&gt;586249&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586250&gt;586250&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586251&gt;586251&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586252&gt;586252&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586253&gt;586253&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586254&gt;586254&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586255&gt;586255&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=586256&gt;586256&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:0.0%&gt; &amp;nbsp; &lt;/div&gt;&lt; 0.1% &lt;/td&gt;&lt;/tr&gt;&lt;tr class=other&gt;&lt;td title=&quot;Other values (879059)&quot;&gt;Other values (879059)&lt;/td&gt;&lt;td&gt;879059&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt; &gt; 99.9% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12&quot; id=-9099077803151007301bottom--9099077803151007301extreme_values&gt;&lt;div class=&quot;row spacing&quot;&gt;&lt;ul class=&quot;nav nav-tabs&quot; role=tablist&gt;&lt;li role=presentation class=active&gt;&lt;a href=#-9099077803151007301extreme_values--9099077803151007301firstn aria-controls=-9099077803151007301extreme_values--9099077803151007301firstn role=tab data-toggle=tab&gt;Minimum 10 values&lt;/a&gt;&lt;/li&gt;&lt;li role=presentation&gt;&lt;a href=#-9099077803151007301extreme_values--9099077803151007301lastn aria-controls=-9099077803151007301extreme_values--9099077803151007301lastn role=tab data-toggle=tab&gt;Maximum 10 values&lt;/a&gt;&lt;/li&gt;&lt;/ul&gt;&lt;div class=tab-content&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12 active&quot; id=-9099077803151007301extreme_values--9099077803151007301firstn&gt;&lt;table class=&quot;freq table table-hover table-striped&quot;&gt;&lt;thead&gt;&lt;tr&gt;&lt;td&gt;Value&lt;/td&gt;&lt;td&gt;Count&lt;/td&gt;&lt;td&gt;Frequency (%)&lt;/td&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr class&gt;&lt;td title=0&gt;0&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=1&gt;1&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=2&gt;2&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=3&gt;3&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=4&gt;4&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=5&gt;5&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=6&gt;6&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=7&gt;7&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=8&gt;8&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=9&gt;9&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12&quot; id=-9099077803151007301extreme_values--9099077803151007301lastn&gt;&lt;table class=&quot;freq table table-hover table-striped&quot;&gt;&lt;thead&gt;&lt;tr&gt;&lt;td&gt;Value&lt;/td&gt;&lt;td&gt;Count&lt;/td&gt;&lt;td&gt;Frequency (%)&lt;/td&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr class&gt;&lt;td title=879158&gt;879158&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=879157&gt;879157&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=879156&gt;879156&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=879155&gt;879155&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=879154&gt;879154&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=879153&gt;879153&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=879152&gt;879152&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=879151&gt;879151&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=879150&gt;879150&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class&gt;&lt;td title=879149&gt;879149&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;&lt;div class=bar style=width:100.0%&gt;&lt; 0.1% &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;div class=&quot;row header&quot;&gt;&lt;a class=anchor-pos id=missing&gt;&lt;/a&gt;&lt;h1 class=page-header&gt;Missing values&lt;/h1&gt;&lt;/div&gt;&lt;div class=section-items&gt;&lt;div class=&quot;row spacing&quot;&gt;&lt;ul class=&quot;nav nav-tabs&quot; role=tablist&gt;&lt;li role=presentation class=active&gt;&lt;a href=#missing-bar aria-controls=missing-bar role=tab data-toggle=tab&gt;Count&lt;/a&gt;&lt;/li&gt;&lt;li role=presentation&gt;&lt;a href=#missing-matrix aria-controls=missing-matrix role=tab data-toggle=tab&gt;Matrix&lt;/a&gt;&lt;/li&gt;&lt;/ul&gt;&lt;div class=tab-content&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12 active&quot; id=missing-bar&gt;&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot; standalone=&quot;no&quot;?&gt;&lt;!DOCTYPE svg class=&quot;img-responsive center-img&quot;PUBLIC &quot;-//W3C//DTD SVG 1.1//EN&quot;
  &quot;http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd&quot;&gt;&lt;svg class=&quot;img-responsive center-img&quot; xmlns:xlink=http://www.w3.org/1999/xlink width=720pt height=360pt viewbox=&quot;0 0 720 360&quot; xmlns=http://www.w3.org/2000/svg version=1.1&gt;&lt;metadata&gt;&lt;rdf:rdf xmlns:dc=http://purl.org/dc/elements/1.1/ xmlns:cc=http://creativecommons.org/ns# xmlns:rdf=http://www.w3.org/1999/02/22-rdf-syntax-ns#&gt;&lt;cc:work&gt;&lt;dc:type rdf:resource=http://purl.org/dc/dcmitype/StillImage /&gt;&lt;dc:date&gt;2022-07-12T13:06:39.439802&lt;/dc:date&gt;&lt;dc:format&gt;image/svg+xml&lt;/dc:format&gt;&lt;dc:creator&gt;&lt;cc:agent&gt;&lt;dc:title&gt;Matplotlib v3.5.2, https://matplotlib.org/&lt;/dc:title&gt;&lt;/cc:agent&gt;&lt;/dc:creator&gt;&lt;/cc:work&gt;&lt;/rdf:rdf&gt;&lt;/metadata&gt;&lt;defs&gt;&lt;style type=text/css&gt;*{stroke-linejoin: round; stroke-linecap: butt}&lt;/style&gt;&lt;/defs&gt;&lt;g id=figure_1&gt;&lt;g id=patch_1&gt;&lt;path d=&quot;M 0 360 
L 720 360 
L 720 0 
L 0 0 
z
&quot; style=&quot;fill: #ffffff&quot;/&gt;&lt;/g&gt;&lt;g id=axes_1&gt;&lt;g id=patch_2&gt;&lt;path d=&quot;M 72 252 
L 648 252 
L 648 72 
L 72 72 
z
&quot; style=&quot;fill: #ffffff&quot;/&gt;&lt;/g&gt;&lt;g id=matplotlib.axis_1&gt;&lt;g id=xtick_1&gt;&lt;g id=text_1&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(58.638437 312.506592)rotate(-45)scale(0.13 -0.13)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-46 transform=scale(0.015625) d=&quot;M 525 0 
L 525 4581 
L 3616 4581 
L 3616 4041 
L 1131 4041 
L 1131 2622 
L 3281 2622 
L 3281 2081 
L 1131 2081 
L 1131 0 
L 525 0 
z
&quot;/&gt;&lt;path id=ArialMT-72 transform=scale(0.015625) d=&quot;M 416 0 
L 416 3319 
L 922 3319 
L 922 2816 
Q 1116 3169 1280 3281 
Q 1444 3394 1641 3394 
Q 1925 3394 2219 3213 
L 2025 2691 
Q 1819 2813 1613 2813 
Q 1428 2813 1281 2702 
Q 1134 2591 1072 2394 
Q 978 2094 978 1738 
L 978 0 
L 416 0 
z
&quot;/&gt;&lt;path id=ArialMT-65 transform=scale(0.015625) d=&quot;M 2694 1069 
L 3275 997 
Q 3138 488 2766 206 
Q 2394 -75 1816 -75 
Q 1088 -75 661 373 
Q 234 822 234 1631 
Q 234 2469 665 2931 
Q 1097 3394 1784 3394 
Q 2450 3394 2872 2941 
Q 3294 2488 3294 1666 
Q 3294 1616 3291 1516 
L 816 1516 
Q 847 969 1125 678 
Q 1403 388 1819 388 
Q 2128 388 2347 550 
Q 2566 713 2694 1069 
z
M 847 1978 
L 2700 1978 
Q 2663 2397 2488 2606 
Q 2219 2931 1791 2931 
Q 1403 2931 1139 2672 
Q 875 2413 847 1978 
z
&quot;/&gt;&lt;path id=ArialMT-71 transform=scale(0.015625) d=&quot;M 2538 -1272 
L 2538 353 
Q 2406 169 2170 47 
Q 1934 -75 1669 -75 
Q 1078 -75 651 397 
Q 225 869 225 1691 
Q 225 2191 398 2587 
Q 572 2984 901 3189 
Q 1231 3394 1625 3394 
Q 2241 3394 2594 2875 
L 2594 3319 
L 3100 3319 
L 3100 -1272 
L 2538 -1272 
z
M 803 1669 
Q 803 1028 1072 708 
Q 1341 388 1716 388 
Q 2075 388 2334 692 
Q 2594 997 2594 1619 
Q 2594 2281 2320 2615 
Q 2047 2950 1678 2950 
Q 1313 2950 1058 2639 
Q 803 2328 803 1669 
z
&quot;/&gt;&lt;path id=ArialMT-75 transform=scale(0.015625) d=&quot;M 2597 0 
L 2597 488 
Q 2209 -75 1544 -75 
Q 1250 -75 995 37 
Q 741 150 617 320 
Q 494 491 444 738 
Q 409 903 409 1263 
L 409 3319 
L 972 3319 
L 972 1478 
Q 972 1038 1006 884 
Q 1059 663 1231 536 
Q 1403 409 1656 409 
Q 1909 409 2131 539 
Q 2353 669 2445 892 
Q 2538 1116 2538 1541 
L 2538 3319 
L 3100 3319 
L 3100 0 
L 2597 0 
z
&quot;/&gt;&lt;path id=ArialMT-6e transform=scale(0.015625) d=&quot;M 422 0 
L 422 3319 
L 928 3319 
L 928 2847 
Q 1294 3394 1984 3394 
Q 2284 3394 2536 3286 
Q 2788 3178 2913 3003 
Q 3038 2828 3088 2588 
Q 3119 2431 3119 2041 
L 3119 0 
L 2556 0 
L 2556 2019 
Q 2556 2363 2490 2533 
Q 2425 2703 2258 2804 
Q 2091 2906 1866 2906 
Q 1506 2906 1245 2678 
Q 984 2450 984 1813 
L 984 0 
L 422 0 
z
&quot;/&gt;&lt;path id=ArialMT-63 transform=scale(0.015625) d=&quot;M 2588 1216 
L 3141 1144 
Q 3050 572 2676 248 
Q 2303 -75 1759 -75 
Q 1078 -75 664 370 
Q 250 816 250 1647 
Q 250 2184 428 2587 
Q 606 2991 970 3192 
Q 1334 3394 1763 3394 
Q 2303 3394 2647 3120 
Q 2991 2847 3088 2344 
L 2541 2259 
Q 2463 2594 2264 2762 
Q 2066 2931 1784 2931 
Q 1359 2931 1093 2626 
Q 828 2322 828 1663 
Q 828 994 1084 691 
Q 1341 388 1753 388 
Q 2084 388 2306 591 
Q 2528 794 2588 1216 
z
&quot;/&gt;&lt;path id=ArialMT-79 transform=scale(0.015625) d=&quot;M 397 -1278 
L 334 -750 
Q 519 -800 656 -800 
Q 844 -800 956 -737 
Q 1069 -675 1141 -563 
Q 1194 -478 1313 -144 
Q 1328 -97 1363 -6 
L 103 3319 
L 709 3319 
L 1400 1397 
Q 1534 1031 1641 628 
Q 1738 1016 1872 1384 
L 2581 3319 
L 3144 3319 
L 1881 -56 
Q 1678 -603 1566 -809 
Q 1416 -1088 1222 -1217 
Q 1028 -1347 759 -1347 
Q 597 -1347 397 -1278 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-46 /&gt;&lt;use xlink:href=#ArialMT-72 x=61.083984 /&gt;&lt;use xlink:href=#ArialMT-65 x=94.384766 /&gt;&lt;use xlink:href=#ArialMT-71 x=150 /&gt;&lt;use xlink:href=#ArialMT-75 x=205.615234 /&gt;&lt;use xlink:href=#ArialMT-65 x=261.230469 /&gt;&lt;use xlink:href=#ArialMT-6e x=316.845703 /&gt;&lt;use xlink:href=#ArialMT-63 x=372.460938 /&gt;&lt;use xlink:href=#ArialMT-79 x=422.460938 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_2&gt;&lt;g id=text_2&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(133.46391 301.788842)rotate(-45)scale(0.13 -0.13)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-4c transform=scale(0.015625) d=&quot;M 469 0 
L 469 4581 
L 1075 4581 
L 1075 541 
L 3331 541 
L 3331 0 
L 469 0 
z
&quot;/&gt;&lt;path id=ArialMT-61 transform=scale(0.015625) d=&quot;M 2588 409 
Q 2275 144 1986 34 
Q 1697 -75 1366 -75 
Q 819 -75 525 192 
Q 231 459 231 875 
Q 231 1119 342 1320 
Q 453 1522 633 1644 
Q 813 1766 1038 1828 
Q 1203 1872 1538 1913 
Q 2219 1994 2541 2106 
Q 2544 2222 2544 2253 
Q 2544 2597 2384 2738 
Q 2169 2928 1744 2928 
Q 1347 2928 1158 2789 
Q 969 2650 878 2297 
L 328 2372 
Q 403 2725 575 2942 
Q 747 3159 1072 3276 
Q 1397 3394 1825 3394 
Q 2250 3394 2515 3294 
Q 2781 3194 2906 3042 
Q 3031 2891 3081 2659 
Q 3109 2516 3109 2141 
L 3109 1391 
Q 3109 606 3145 398 
Q 3181 191 3288 0 
L 2700 0 
Q 2613 175 2588 409 
z
M 2541 1666 
Q 2234 1541 1622 1453 
Q 1275 1403 1131 1340 
Q 988 1278 909 1158 
Q 831 1038 831 891 
Q 831 666 1001 516 
Q 1172 366 1500 366 
Q 1825 366 2078 508 
Q 2331 650 2450 897 
Q 2541 1088 2541 1459 
L 2541 1666 
z
&quot;/&gt;&lt;path id=ArialMT-74 transform=scale(0.015625) d=&quot;M 1650 503 
L 1731 6 
Q 1494 -44 1306 -44 
Q 1000 -44 831 53 
Q 663 150 594 308 
Q 525 466 525 972 
L 525 2881 
L 113 2881 
L 113 3319 
L 525 3319 
L 525 4141 
L 1084 4478 
L 1084 3319 
L 1650 3319 
L 1650 2881 
L 1084 2881 
L 1084 941 
Q 1084 700 1114 631 
Q 1144 563 1211 522 
Q 1278 481 1403 481 
Q 1497 481 1650 503 
z
&quot;/&gt;&lt;path id=ArialMT-69 transform=scale(0.015625) d=&quot;M 425 3934 
L 425 4581 
L 988 4581 
L 988 3934 
L 425 3934 
z
M 425 0 
L 425 3319 
L 988 3319 
L 988 0 
L 425 0 
z
&quot;/&gt;&lt;path id=ArialMT-64 transform=scale(0.015625) d=&quot;M 2575 0 
L 2575 419 
Q 2259 -75 1647 -75 
Q 1250 -75 917 144 
Q 584 363 401 755 
Q 219 1147 219 1656 
Q 219 2153 384 2558 
Q 550 2963 881 3178 
Q 1213 3394 1622 3394 
Q 1922 3394 2156 3267 
Q 2391 3141 2538 2938 
L 2538 4581 
L 3097 4581 
L 3097 0 
L 2575 0 
z
M 797 1656 
Q 797 1019 1065 703 
Q 1334 388 1700 388 
Q 2069 388 2326 689 
Q 2584 991 2584 1609 
Q 2584 2291 2321 2609 
Q 2059 2928 1675 2928 
Q 1300 2928 1048 2622 
Q 797 2316 797 1656 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-4c /&gt;&lt;use xlink:href=#ArialMT-61 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-74 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-69 x=139.013672 /&gt;&lt;use xlink:href=#ArialMT-74 x=161.230469 /&gt;&lt;use xlink:href=#ArialMT-75 x=189.013672 /&gt;&lt;use xlink:href=#ArialMT-64 x=244.628906 /&gt;&lt;use xlink:href=#ArialMT-65 x=300.244141 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_3&gt;&lt;g id=text_3&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(189.686288 309.45874)rotate(-45)scale(0.13 -0.13)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-6f transform=scale(0.015625) d=&quot;M 213 1659 
Q 213 2581 725 3025 
Q 1153 3394 1769 3394 
Q 2453 3394 2887 2945 
Q 3322 2497 3322 1706 
Q 3322 1066 3130 698 
Q 2938 331 2570 128 
Q 2203 -75 1769 -75 
Q 1072 -75 642 372 
Q 213 819 213 1659 
z
M 791 1659 
Q 791 1022 1069 705 
Q 1347 388 1769 388 
Q 2188 388 2466 706 
Q 2744 1025 2744 1678 
Q 2744 2294 2464 2611 
Q 2184 2928 1769 2928 
Q 1347 2928 1069 2612 
Q 791 2297 791 1659 
z
&quot;/&gt;&lt;path id=ArialMT-67 transform=scale(0.015625) d=&quot;M 319 -275 
L 866 -356 
Q 900 -609 1056 -725 
Q 1266 -881 1628 -881 
Q 2019 -881 2231 -725 
Q 2444 -569 2519 -288 
Q 2563 -116 2559 434 
Q 2191 0 1641 0 
Q 956 0 581 494 
Q 206 988 206 1678 
Q 206 2153 378 2554 
Q 550 2956 876 3175 
Q 1203 3394 1644 3394 
Q 2231 3394 2613 2919 
L 2613 3319 
L 3131 3319 
L 3131 450 
Q 3131 -325 2973 -648 
Q 2816 -972 2473 -1159 
Q 2131 -1347 1631 -1347 
Q 1038 -1347 672 -1080 
Q 306 -813 319 -275 
z
M 784 1719 
Q 784 1066 1043 766 
Q 1303 466 1694 466 
Q 2081 466 2343 764 
Q 2606 1063 2606 1700 
Q 2606 2309 2336 2618 
Q 2066 2928 1684 2928 
Q 1309 2928 1046 2623 
Q 784 2319 784 1719 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-4c /&gt;&lt;use xlink:href=#ArialMT-6f x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-6e x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-67 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-69 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-74 x=244.677734 /&gt;&lt;use xlink:href=#ArialMT-75 x=272.460938 /&gt;&lt;use xlink:href=#ArialMT-64 x=328.076172 /&gt;&lt;use xlink:href=#ArialMT-65 x=383.691406 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_4&gt;&lt;g id=text_4&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(248.195273 315.057479)rotate(-45)scale(0.13 -0.13)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-44 transform=scale(0.015625) d=&quot;M 494 0 
L 494 4581 
L 2072 4581 
Q 2606 4581 2888 4516 
Q 3281 4425 3559 4188 
Q 3922 3881 4101 3404 
Q 4281 2928 4281 2316 
Q 4281 1794 4159 1391 
Q 4038 988 3847 723 
Q 3656 459 3429 307 
Q 3203 156 2883 78 
Q 2563 0 2147 0 
L 494 0 
z
M 1100 541 
L 2078 541 
Q 2531 541 2789 625 
Q 3047 709 3200 863 
Q 3416 1078 3536 1442 
Q 3656 1806 3656 2325 
Q 3656 3044 3420 3430 
Q 3184 3816 2847 3947 
Q 2603 4041 2063 4041 
L 1100 4041 
L 1100 541 
z
&quot;/&gt;&lt;path id=ArialMT-73 transform=scale(0.015625) d=&quot;M 197 991 
L 753 1078 
Q 800 744 1014 566 
Q 1228 388 1613 388 
Q 2000 388 2187 545 
Q 2375 703 2375 916 
Q 2375 1106 2209 1216 
Q 2094 1291 1634 1406 
Q 1016 1563 777 1677 
Q 538 1791 414 1992 
Q 291 2194 291 2438 
Q 291 2659 392 2848 
Q 494 3038 669 3163 
Q 800 3259 1026 3326 
Q 1253 3394 1513 3394 
Q 1903 3394 2198 3281 
Q 2494 3169 2634 2976 
Q 2775 2784 2828 2463 
L 2278 2388 
Q 2241 2644 2061 2787 
Q 1881 2931 1553 2931 
Q 1166 2931 1000 2803 
Q 834 2675 834 2503 
Q 834 2394 903 2306 
Q 972 2216 1119 2156 
Q 1203 2125 1616 2013 
Q 2213 1853 2448 1751 
Q 2684 1650 2818 1456 
Q 2953 1263 2953 975 
Q 2953 694 2789 445 
Q 2625 197 2315 61 
Q 2006 -75 1616 -75 
Q 969 -75 630 194 
Q 291 463 197 991 
z
&quot;/&gt;&lt;path id=ArialMT-70 transform=scale(0.015625) d=&quot;M 422 -1272 
L 422 3319 
L 934 3319 
L 934 2888 
Q 1116 3141 1344 3267 
Q 1572 3394 1897 3394 
Q 2322 3394 2647 3175 
Q 2972 2956 3137 2557 
Q 3303 2159 3303 1684 
Q 3303 1175 3120 767 
Q 2938 359 2589 142 
Q 2241 -75 1856 -75 
Q 1575 -75 1351 44 
Q 1128 163 984 344 
L 984 -1272 
L 422 -1272 
z
M 931 1641 
Q 931 1000 1190 694 
Q 1450 388 1819 388 
Q 2194 388 2461 705 
Q 2728 1022 2728 1688 
Q 2728 2322 2467 2637 
Q 2206 2953 1844 2953 
Q 1484 2953 1207 2617 
Q 931 2281 931 1641 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-44 /&gt;&lt;use xlink:href=#ArialMT-65 x=72.216797 /&gt;&lt;use xlink:href=#ArialMT-73 x=127.832031 /&gt;&lt;use xlink:href=#ArialMT-63 x=177.832031 /&gt;&lt;use xlink:href=#ArialMT-72 x=227.832031 /&gt;&lt;use xlink:href=#ArialMT-69 x=261.132812 /&gt;&lt;use xlink:href=#ArialMT-70 x=283.349609 /&gt;&lt;use xlink:href=#ArialMT-74 x=338.964844 /&gt;&lt;use xlink:href=#ArialMT-69 x=366.748047 /&gt;&lt;use xlink:href=#ArialMT-6f x=388.964844 /&gt;&lt;use xlink:href=#ArialMT-6e x=444.580078 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_5&gt;&lt;g id=text_5&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(327.522144 299.730608)rotate(-45)scale(0.13 -0.13)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-53 transform=scale(0.015625) d=&quot;M 288 1472 
L 859 1522 
Q 900 1178 1048 958 
Q 1197 738 1509 602 
Q 1822 466 2213 466 
Q 2559 466 2825 569 
Q 3091 672 3220 851 
Q 3350 1031 3350 1244 
Q 3350 1459 3225 1620 
Q 3100 1781 2813 1891 
Q 2628 1963 1997 2114 
Q 1366 2266 1113 2400 
Q 784 2572 623 2826 
Q 463 3081 463 3397 
Q 463 3744 659 4045 
Q 856 4347 1234 4503 
Q 1613 4659 2075 4659 
Q 2584 4659 2973 4495 
Q 3363 4331 3572 4012 
Q 3781 3694 3797 3291 
L 3216 3247 
Q 3169 3681 2898 3903 
Q 2628 4125 2100 4125 
Q 1550 4125 1298 3923 
Q 1047 3722 1047 3438 
Q 1047 3191 1225 3031 
Q 1400 2872 2139 2705 
Q 2878 2538 3153 2413 
Q 3553 2228 3743 1945 
Q 3934 1663 3934 1294 
Q 3934 928 3725 604 
Q 3516 281 3123 101 
Q 2731 -78 2241 -78 
Q 1619 -78 1198 103 
Q 778 284 539 648 
Q 300 1013 288 1472 
z
&quot;/&gt;&lt;path id=ArialMT-76 transform=scale(0.015625) d=&quot;M 1344 0 
L 81 3319 
L 675 3319 
L 1388 1331 
Q 1503 1009 1600 663 
Q 1675 925 1809 1294 
L 2547 3319 
L 3125 3319 
L 1869 0 
L 1344 0 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-53 /&gt;&lt;use xlink:href=#ArialMT-65 x=66.699219 /&gt;&lt;use xlink:href=#ArialMT-72 x=122.314453 /&gt;&lt;use xlink:href=#ArialMT-76 x=155.615234 /&gt;&lt;use xlink:href=#ArialMT-69 x=205.615234 /&gt;&lt;use xlink:href=#ArialMT-63 x=227.832031 /&gt;&lt;use xlink:href=#ArialMT-65 x=277.832031 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_6&gt;&lt;g id=text_6&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(393.555959 297.696792)rotate(-45)scale(0.13 -0.13)&quot;&gt;&lt;use xlink:href=#ArialMT-53 /&gt;&lt;use xlink:href=#ArialMT-74 x=66.699219 /&gt;&lt;use xlink:href=#ArialMT-61 x=94.482422 /&gt;&lt;use xlink:href=#ArialMT-74 x=150.097656 /&gt;&lt;use xlink:href=#ArialMT-69 x=177.880859 /&gt;&lt;use xlink:href=#ArialMT-6f x=200.097656 /&gt;&lt;use xlink:href=#ArialMT-6e x=255.712891 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_7&gt;&lt;g id=text_7&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(463.187734 292.065018)rotate(-45)scale(0.13 -0.13)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-43 transform=scale(0.015625) d=&quot;M 3763 1606 
L 4369 1453 
Q 4178 706 3683 314 
Q 3188 -78 2472 -78 
Q 1731 -78 1267 223 
Q 803 525 561 1097 
Q 319 1669 319 2325 
Q 319 3041 592 3573 
Q 866 4106 1370 4382 
Q 1875 4659 2481 4659 
Q 3169 4659 3637 4309 
Q 4106 3959 4291 3325 
L 3694 3184 
Q 3534 3684 3231 3912 
Q 2928 4141 2469 4141 
Q 1941 4141 1586 3887 
Q 1231 3634 1087 3207 
Q 944 2781 944 2328 
Q 944 1744 1114 1308 
Q 1284 872 1643 656 
Q 2003 441 2422 441 
Q 2931 441 3284 734 
Q 3638 1028 3763 1606 
z
&quot;/&gt;&lt;path id=ArialMT-6c transform=scale(0.015625) d=&quot;M 409 0 
L 409 4581 
L 972 4581 
L 972 0 
L 409 0 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-43 /&gt;&lt;use xlink:href=#ArialMT-6c x=72.216797 /&gt;&lt;use xlink:href=#ArialMT-61 x=94.433594 /&gt;&lt;use xlink:href=#ArialMT-73 x=150.048828 /&gt;&lt;use xlink:href=#ArialMT-73 x=200.048828 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_8&gt;&lt;g id=text_8&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(535.36465 283.888102)rotate(-45)scale(0.13 -0.13)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-42 transform=scale(0.015625) d=&quot;M 469 0 
L 469 4581 
L 2188 4581 
Q 2713 4581 3030 4442 
Q 3347 4303 3526 4014 
Q 3706 3725 3706 3409 
Q 3706 3116 3547 2856 
Q 3388 2597 3066 2438 
Q 3481 2316 3704 2022 
Q 3928 1728 3928 1328 
Q 3928 1006 3792 729 
Q 3656 453 3456 303 
Q 3256 153 2954 76 
Q 2653 0 2216 0 
L 469 0 
z
M 1075 2656 
L 2066 2656 
Q 2469 2656 2644 2709 
Q 2875 2778 2992 2937 
Q 3109 3097 3109 3338 
Q 3109 3566 3000 3739 
Q 2891 3913 2687 3977 
Q 2484 4041 1991 4041 
L 1075 4041 
L 1075 2656 
z
M 1075 541 
L 2216 541 
Q 2509 541 2628 563 
Q 2838 600 2978 687 
Q 3119 775 3209 942 
Q 3300 1109 3300 1328 
Q 3300 1584 3169 1773 
Q 3038 1963 2805 2039 
Q 2572 2116 2134 2116 
L 1075 2116 
L 1075 541 
z
&quot;/&gt;&lt;path id=ArialMT-57 transform=scale(0.015625) d=&quot;M 1294 0 
L 78 4581 
L 700 4581 
L 1397 1578 
Q 1509 1106 1591 641 
Q 1766 1375 1797 1488 
L 2669 4581 
L 3400 4581 
L 4056 2263 
Q 4303 1400 4413 641 
Q 4500 1075 4641 1638 
L 5359 4581 
L 5969 4581 
L 4713 0 
L 4128 0 
L 3163 3491 
Q 3041 3928 3019 4028 
Q 2947 3713 2884 3491 
L 1913 0 
L 1294 0 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-42 /&gt;&lt;use xlink:href=#ArialMT-57 x=66.699219 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_9&gt;&lt;g id=text_9&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(606.507423 276.745329)rotate(-45)scale(0.13 -0.13)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-49 transform=scale(0.015625) d=&quot;M 597 0 
L 597 4581 
L 1203 4581 
L 1203 0 
L 597 0 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-49 /&gt;&lt;use xlink:href=#ArialMT-64 x=27.783203 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=matplotlib.axis_2&gt;&lt;g id=ytick_1&gt;&lt;g id=text_10&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(43.43 256.652578)scale(0.13 -0.13)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-30 transform=scale(0.015625) d=&quot;M 266 2259 
Q 266 3072 433 3567 
Q 600 4063 929 4331 
Q 1259 4600 1759 4600 
Q 2128 4600 2406 4451 
Q 2684 4303 2865 4023 
Q 3047 3744 3150 3342 
Q 3253 2941 3253 2259 
Q 3253 1453 3087 958 
Q 2922 463 2592 192 
Q 2263 -78 1759 -78 
Q 1097 -78 719 397 
Q 266 969 266 2259 
z
M 844 2259 
Q 844 1131 1108 757 
Q 1372 384 1759 384 
Q 2147 384 2411 759 
Q 2675 1134 2675 2259 
Q 2675 3391 2411 3762 
Q 2147 4134 1753 4134 
Q 1366 4134 1134 3806 
Q 844 3388 844 2259 
z
&quot;/&gt;&lt;path id=ArialMT-2e transform=scale(0.015625) d=&quot;M 581 0 
L 581 641 
L 1222 641 
L 1222 0 
L 581 0 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-30 /&gt;&lt;use xlink:href=#ArialMT-2e x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=83.398438 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_2&gt;&lt;g id=text_11&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(43.43 220.652578)scale(0.13 -0.13)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-32 transform=scale(0.015625) d=&quot;M 3222 541 
L 3222 0 
L 194 0 
Q 188 203 259 391 
Q 375 700 629 1000 
Q 884 1300 1366 1694 
Q 2113 2306 2375 2664 
Q 2638 3022 2638 3341 
Q 2638 3675 2398 3904 
Q 2159 4134 1775 4134 
Q 1369 4134 1125 3890 
Q 881 3647 878 3216 
L 300 3275 
Q 359 3922 746 4261 
Q 1134 4600 1788 4600 
Q 2447 4600 2831 4234 
Q 3216 3869 3216 3328 
Q 3216 3053 3103 2787 
Q 2991 2522 2730 2228 
Q 2469 1934 1863 1422 
Q 1356 997 1212 845 
Q 1069 694 975 541 
L 3222 541 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-30 /&gt;&lt;use xlink:href=#ArialMT-2e x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-32 x=83.398438 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_3&gt;&lt;g id=text_12&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(43.43 184.652578)scale(0.13 -0.13)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-34 transform=scale(0.015625) d=&quot;M 2069 0 
L 2069 1097 
L 81 1097 
L 81 1613 
L 2172 4581 
L 2631 4581 
L 2631 1613 
L 3250 1613 
L 3250 1097 
L 2631 1097 
L 2631 0 
L 2069 0 
z
M 2069 1613 
L 2069 3678 
L 634 1613 
L 2069 1613 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-30 /&gt;&lt;use xlink:href=#ArialMT-2e x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-34 x=83.398438 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_4&gt;&lt;g id=text_13&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(43.43 148.652578)scale(0.13 -0.13)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-36 transform=scale(0.015625) d=&quot;M 3184 3459 
L 2625 3416 
Q 2550 3747 2413 3897 
Q 2184 4138 1850 4138 
Q 1581 4138 1378 3988 
Q 1113 3794 959 3422 
Q 806 3050 800 2363 
Q 1003 2672 1297 2822 
Q 1591 2972 1913 2972 
Q 2475 2972 2870 2558 
Q 3266 2144 3266 1488 
Q 3266 1056 3080 686 
Q 2894 316 2569 119 
Q 2244 -78 1831 -78 
Q 1128 -78 684 439 
Q 241 956 241 2144 
Q 241 3472 731 4075 
Q 1159 4600 1884 4600 
Q 2425 4600 2770 4297 
Q 3116 3994 3184 3459 
z
M 888 1484 
Q 888 1194 1011 928 
Q 1134 663 1356 523 
Q 1578 384 1822 384 
Q 2178 384 2434 671 
Q 2691 959 2691 1453 
Q 2691 1928 2437 2201 
Q 2184 2475 1800 2475 
Q 1419 2475 1153 2201 
Q 888 1928 888 1484 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-30 /&gt;&lt;use xlink:href=#ArialMT-2e x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-36 x=83.398438 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_5&gt;&lt;g id=text_14&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(43.43 112.652578)scale(0.13 -0.13)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-38 transform=scale(0.015625) d=&quot;M 1131 2484 
Q 781 2613 612 2850 
Q 444 3088 444 3419 
Q 444 3919 803 4259 
Q 1163 4600 1759 4600 
Q 2359 4600 2725 4251 
Q 3091 3903 3091 3403 
Q 3091 3084 2923 2848 
Q 2756 2613 2416 2484 
Q 2838 2347 3058 2040 
Q 3278 1734 3278 1309 
Q 3278 722 2862 322 
Q 2447 -78 1769 -78 
Q 1091 -78 675 323 
Q 259 725 259 1325 
Q 259 1772 486 2073 
Q 713 2375 1131 2484 
z
M 1019 3438 
Q 1019 3113 1228 2906 
Q 1438 2700 1772 2700 
Q 2097 2700 2305 2904 
Q 2513 3109 2513 3406 
Q 2513 3716 2298 3927 
Q 2084 4138 1766 4138 
Q 1444 4138 1231 3931 
Q 1019 3725 1019 3438 
z
M 838 1322 
Q 838 1081 952 856 
Q 1066 631 1291 507 
Q 1516 384 1775 384 
Q 2178 384 2440 643 
Q 2703 903 2703 1303 
Q 2703 1709 2433 1975 
Q 2163 2241 1756 2241 
Q 1359 2241 1098 1978 
Q 838 1716 838 1322 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-30 /&gt;&lt;use xlink:href=#ArialMT-2e x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-38 x=83.398438 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_6&gt;&lt;g id=text_15&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(43.43 76.652578)scale(0.13 -0.13)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-31 transform=scale(0.015625) d=&quot;M 2384 0 
L 1822 0 
L 1822 3584 
Q 1619 3391 1289 3197 
Q 959 3003 697 2906 
L 697 3450 
Q 1169 3672 1522 3987 
Q 1875 4303 2022 4600 
L 2384 4600 
L 2384 0 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-31 /&gt;&lt;use xlink:href=#ArialMT-2e x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=83.398438 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=patch_3&gt;&lt;path d=&quot;M 88 252 
L 120 252 
L 120 72 
L 88 72 
z
&quot; clip-path=url(#p5018df5d43) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_4&gt;&lt;path d=&quot;M 152 252 
L 184 252 
L 184 72 
L 152 72 
z
&quot; clip-path=url(#p5018df5d43) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_5&gt;&lt;path d=&quot;M 216 252 
L 248 252 
L 248 72 
L 216 72 
z
&quot; clip-path=url(#p5018df5d43) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_6&gt;&lt;path d=&quot;M 280 252 
L 312 252 
L 312 72 
L 280 72 
z
&quot; clip-path=url(#p5018df5d43) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_7&gt;&lt;path d=&quot;M 344 252 
L 376 252 
L 376 72 
L 344 72 
z
&quot; clip-path=url(#p5018df5d43) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_8&gt;&lt;path d=&quot;M 408 252 
L 440 252 
L 440 72 
L 408 72 
z
&quot; clip-path=url(#p5018df5d43) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_9&gt;&lt;path d=&quot;M 472 252 
L 504 252 
L 504 84.093649 
L 472 84.093649 
z
&quot; clip-path=url(#p5018df5d43) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_10&gt;&lt;path d=&quot;M 536 252 
L 568 252 
L 568 72.38737 
L 536 72.38737 
z
&quot; clip-path=url(#p5018df5d43) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;g id=patch_11&gt;&lt;path d=&quot;M 600 252 
L 632 252 
L 632 72 
L 600 72 
z
&quot; clip-path=url(#p5018df5d43) style=&quot;fill: #337ab7; stroke: #ffffff; stroke-width: 0.3; stroke-linejoin: miter&quot;/&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=axes_2&gt;&lt;g id=matplotlib.axis_3&gt;&lt;g id=ytick_7&gt;&lt;g id=text_16&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(658.5 256.652578)scale(0.13 -0.13)&quot;&gt;&lt;use xlink:href=#ArialMT-30 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_8&gt;&lt;g id=text_17&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(658.5 220.652578)scale(0.13 -0.13)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-37 transform=scale(0.015625) d=&quot;M 303 3981 
L 303 4522 
L 3269 4522 
L 3269 4084 
Q 2831 3619 2401 2847 
Q 1972 2075 1738 1259 
Q 1569 684 1522 0 
L 944 0 
Q 953 541 1156 1306 
Q 1359 2072 1739 2783 
Q 2119 3494 2547 3981 
L 303 3981 
z
&quot;/&gt;&lt;path id=ArialMT-35 transform=scale(0.015625) d=&quot;M 266 1200 
L 856 1250 
Q 922 819 1161 601 
Q 1400 384 1738 384 
Q 2144 384 2425 690 
Q 2706 997 2706 1503 
Q 2706 1984 2436 2262 
Q 2166 2541 1728 2541 
Q 1456 2541 1237 2417 
Q 1019 2294 894 2097 
L 366 2166 
L 809 4519 
L 3088 4519 
L 3088 3981 
L 1259 3981 
L 1013 2750 
Q 1425 3038 1878 3038 
Q 2478 3038 2890 2622 
Q 3303 2206 3303 1553 
Q 3303 931 2941 478 
Q 2500 -78 1738 -78 
Q 1113 -78 717 272 
Q 322 622 266 1200 
z
&quot;/&gt;&lt;path id=ArialMT-33 transform=scale(0.015625) d=&quot;M 269 1209 
L 831 1284 
Q 928 806 1161 595 
Q 1394 384 1728 384 
Q 2125 384 2398 659 
Q 2672 934 2672 1341 
Q 2672 1728 2419 1979 
Q 2166 2231 1775 2231 
Q 1616 2231 1378 2169 
L 1441 2663 
Q 1497 2656 1531 2656 
Q 1891 2656 2178 2843 
Q 2466 3031 2466 3422 
Q 2466 3731 2256 3934 
Q 2047 4138 1716 4138 
Q 1388 4138 1169 3931 
Q 950 3725 888 3313 
L 325 3413 
Q 428 3978 793 4289 
Q 1159 4600 1703 4600 
Q 2078 4600 2393 4439 
Q 2709 4278 2876 4000 
Q 3044 3722 3044 3409 
Q 3044 3113 2884 2869 
Q 2725 2625 2413 2481 
Q 2819 2388 3044 2092 
Q 3269 1797 3269 1353 
Q 3269 753 2831 336 
Q 2394 -81 1725 -81 
Q 1122 -81 723 278 
Q 325 638 269 1209 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-31 /&gt;&lt;use xlink:href=#ArialMT-37 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-35 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-38 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-33 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-31 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_9&gt;&lt;g id=text_18&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(658.5 184.652578)scale(0.13 -0.13)&quot;&gt;&lt;use xlink:href=#ArialMT-33 /&gt;&lt;use xlink:href=#ArialMT-35 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-31 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-36 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-36 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-33 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_10&gt;&lt;g id=text_19&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(658.5 148.652578)scale(0.13 -0.13)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-39 transform=scale(0.015625) d=&quot;M 350 1059 
L 891 1109 
Q 959 728 1153 556 
Q 1347 384 1650 384 
Q 1909 384 2104 503 
Q 2300 622 2425 820 
Q 2550 1019 2634 1356 
Q 2719 1694 2719 2044 
Q 2719 2081 2716 2156 
Q 2547 1888 2255 1720 
Q 1963 1553 1622 1553 
Q 1053 1553 659 1965 
Q 266 2378 266 3053 
Q 266 3750 677 4175 
Q 1088 4600 1706 4600 
Q 2153 4600 2523 4359 
Q 2894 4119 3086 3673 
Q 3278 3228 3278 2384 
Q 3278 1506 3087 986 
Q 2897 466 2520 194 
Q 2144 -78 1638 -78 
Q 1100 -78 759 220 
Q 419 519 350 1059 
z
M 2653 3081 
Q 2653 3566 2395 3850 
Q 2138 4134 1775 4134 
Q 1400 4134 1122 3828 
Q 844 3522 844 3034 
Q 844 2597 1108 2323 
Q 1372 2050 1759 2050 
Q 2150 2050 2401 2323 
Q 2653 2597 2653 3081 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-35 /&gt;&lt;use xlink:href=#ArialMT-32 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-37 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-34 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-39 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-35 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_11&gt;&lt;g id=text_20&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(658.5 112.652578)scale(0.13 -0.13)&quot;&gt;&lt;use xlink:href=#ArialMT-37 /&gt;&lt;use xlink:href=#ArialMT-30 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-33 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-33 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-32 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-37 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_12&gt;&lt;g id=text_21&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(658.5 76.652578)scale(0.13 -0.13)&quot;&gt;&lt;use xlink:href=#ArialMT-38 /&gt;&lt;use xlink:href=#ArialMT-37 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-39 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-31 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-35 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-39 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=axes_3&gt;&lt;g id=matplotlib.axis_4&gt;&lt;g id=xtick_10&gt;&lt;g id=text_22&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(110.579739 59.673013)rotate(-45)scale(0.13 -0.13)&quot;&gt;&lt;use xlink:href=#ArialMT-38 /&gt;&lt;use xlink:href=#ArialMT-37 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-39 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-31 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-35 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-39 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_11&gt;&lt;g id=text_23&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(174.579739 59.673013)rotate(-45)scale(0.13 -0.13)&quot;&gt;&lt;use xlink:href=#ArialMT-38 /&gt;&lt;use xlink:href=#ArialMT-37 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-39 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-31 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-35 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-39 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_12&gt;&lt;g id=text_24&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(238.579739 59.673013)rotate(-45)scale(0.13 -0.13)&quot;&gt;&lt;use xlink:href=#ArialMT-38 /&gt;&lt;use xlink:href=#ArialMT-37 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-39 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-31 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-35 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-39 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_13&gt;&lt;g id=text_25&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(302.579739 59.673013)rotate(-45)scale(0.13 -0.13)&quot;&gt;&lt;use xlink:href=#ArialMT-38 /&gt;&lt;use xlink:href=#ArialMT-37 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-39 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-31 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-35 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-39 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_14&gt;&lt;g id=text_26&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(366.579739 59.673013)rotate(-45)scale(0.13 -0.13)&quot;&gt;&lt;use xlink:href=#ArialMT-38 /&gt;&lt;use xlink:href=#ArialMT-37 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-39 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-31 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-35 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-39 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_15&gt;&lt;g id=text_27&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(430.579739 59.673013)rotate(-45)scale(0.13 -0.13)&quot;&gt;&lt;use xlink:href=#ArialMT-38 /&gt;&lt;use xlink:href=#ArialMT-37 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-39 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-31 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-35 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-39 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_16&gt;&lt;g id=text_28&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(494.579739 59.673013)rotate(-45)scale(0.13 -0.13)&quot;&gt;&lt;use xlink:href=#ArialMT-38 /&gt;&lt;use xlink:href=#ArialMT-32 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-30 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-30 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-39 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-31 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_17&gt;&lt;g id=text_29&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(558.579739 59.673013)rotate(-45)scale(0.13 -0.13)&quot;&gt;&lt;use xlink:href=#ArialMT-38 /&gt;&lt;use xlink:href=#ArialMT-37 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-37 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-32 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-36 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-37 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_18&gt;&lt;g id=text_30&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(622.579739 59.673013)rotate(-45)scale(0.13 -0.13)&quot;&gt;&lt;use xlink:href=#ArialMT-38 /&gt;&lt;use xlink:href=#ArialMT-37 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-39 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-31 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-35 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-39 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;defs&gt;&lt;clippath id=p5018df5d43&gt;&lt;rect x=72 y=72 width=576 height=180 /&gt;&lt;/clippath&gt;&lt;/defs&gt;&lt;/svg&gt;&lt;div class=&quot;caption text-center text-muted&quot;&gt; A simple visualization of nullity by column. &lt;/div&gt;&lt;/div&gt;&lt;div role=tabpanel class=&quot;tab-pane col-sm-12&quot; id=missing-matrix&gt;&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot; standalone=&quot;no&quot;?&gt;&lt;!DOCTYPE svg class=&quot;img-responsive center-img&quot;PUBLIC &quot;-//W3C//DTD SVG 1.1//EN&quot;
  &quot;http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd&quot;&gt;&lt;svg class=&quot;img-responsive center-img&quot; xmlns:xlink=http://www.w3.org/1999/xlink width=720pt height=288pt viewbox=&quot;0 0 720 288&quot; xmlns=http://www.w3.org/2000/svg version=1.1&gt;&lt;metadata&gt;&lt;rdf:rdf xmlns:dc=http://purl.org/dc/elements/1.1/ xmlns:cc=http://creativecommons.org/ns# xmlns:rdf=http://www.w3.org/1999/02/22-rdf-syntax-ns#&gt;&lt;cc:work&gt;&lt;dc:type rdf:resource=http://purl.org/dc/dcmitype/StillImage /&gt;&lt;dc:date&gt;2022-07-12T13:06:40.022219&lt;/dc:date&gt;&lt;dc:format&gt;image/svg+xml&lt;/dc:format&gt;&lt;dc:creator&gt;&lt;cc:agent&gt;&lt;dc:title&gt;Matplotlib v3.5.2, https://matplotlib.org/&lt;/dc:title&gt;&lt;/cc:agent&gt;&lt;/dc:creator&gt;&lt;/cc:work&gt;&lt;/rdf:rdf&gt;&lt;/metadata&gt;&lt;defs&gt;&lt;style type=text/css&gt;*{stroke-linejoin: round; stroke-linecap: butt}&lt;/style&gt;&lt;/defs&gt;&lt;g id=figure_1&gt;&lt;g id=patch_1&gt;&lt;path d=&quot;M 0 288 
L 720 288 
L 720 0 
L 0 0 
z
&quot; style=&quot;fill: #ffffff&quot;/&gt;&lt;/g&gt;&lt;g id=axes_1&gt;&lt;g id=patch_2&gt;&lt;path d=&quot;M 72 230.4 
L 648 230.4 
L 648 86.4 
L 72 86.4 
z
&quot; style=&quot;fill: #ffffff&quot;/&gt;&lt;/g&gt;&lt;g clip-path=url(#p494c45c964)&gt;&lt;image xlink:href=&quot;data:image/png;base64,
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QRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAETUP3uT9H23FVxgRBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBUFN0n/tztB1XZUwQBEEQBEEQBEHQGsg9JwRBEARNR0ZzCIIgCIJ+HKF5QV5yZhgQBEEQBEGtUfHsMIRMIaEgWvvmRuOEBqOO1RfSgiEIgr6A1p5n5qGxQ/7YHA+hscVSjNauBRAEQRAEfQRy3wJloo43EiodBEFhlNeJ6XogqCnyQVxLpFggCIIej4fuEIIgCIIgCIIg6E+H2yQIgqA4yuszPTFtiTq+jTMWqZkQBEEQ9BFo7PzJXAWCIOjxeOjHHz2zwCgFQRAEvQV1HBTXRob8aqSOL440KQiCIAiCoA9B9u6CypHbSagnWvtZWUdkRIAg6A1IFz2391V2c8uuGHX8qtdtdyLSFyxewBAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAE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BI1C97k/R9txVcYEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEvRPd5550pu24ks4EQYNRqElpLRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRA0F9l0DIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIKgNZC/t0MQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQ9HJU/GFzXnK+yJ6LlB0EQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQfXIG4wQBEEQBEEQ9NNhggxBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARB0OLI7xshaDLSgiEIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgp4ir1hAEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEPRNdJ/7c7QdV2VMEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEAS9Cd3n/hxtx1UZUx4KXV1ech3R2LKDIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiC1kH3uSedaTuupDNBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEPQB6D73yuRCaDuuyuSKUV6Or51PEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEPTjCO3pabtOCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIL+cPhTOgRBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBn4RCezPnJZeH7BcNQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEzUf3uVcmB0EQ9Aa0HVdlclAiCo1SeQVcnBwEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQTFkqzAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAI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EARBEARBEARBEARBEARBEARBEARBEARBEARBEJSH7nOvTK4j2o6rMjkIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiDo09B97kln2o4r6UwQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEF/ddzn/hxtx1UZEwRBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBM9B97s/RdlyVMUEQBEEQBEEQBEEvQm4CIQiCoOHIUAZBEDQb6ccXRwoYgiAIgiAIgiAIgiDow1DHBaGOMUEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQ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BEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEFfhnbOzroR63YzlVBp8HN1EARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEPTv0R3vmDYjZ1MhCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIKgL0KlP4r8cwNBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEAQ9HpU2cZaSrOuEIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCoL9FO+ehpBHrUBIEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQdBrtHN21p1DI1ZnHQRBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARB0Kdo5+ysG7E66yAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIejLaOa/RiNU5EwRBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEAT1otJ1v1KSE4AQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBL2Fds5rNGJ1zgRBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARB0PNQaZdJKcnCEwiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCfj9HFyEIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgqA7onMHfZuR3V0QBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEGNaOe8RiNW50wQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEE/7N3LlSNHrgDQlE2iEbRJXNMm0Qj6pLcYtV4fzUhEdYMggLzc1j0ZUZEIxCd/EARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARB0BfQ835NOtLl9kg6EgRBEARBEARBEARBEARBEARBEARB0E+j0MXQ4uucHesEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRD0Co2952FsxSEIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAI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/sjqdTlygqGeSGRCEARBEARB0FtQ3mNHEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEPRFdLk9XqPn/VpZJwiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIOh//S63R2Vxxeh5v75Gu5tgNwqd4NCRRAEEQV2RoQwajPIG6o5Iv4MgCIKgUyDzcQiCICgb5Y0tRikIgiAIgiAIegsy1YYgCIIgCIIg6MvIQgIajIrv9NQRoCAaew+yGIcgCIIg6EvIcjKGtFMi0pgQBEEQBEEQBEEQBEEQ9KPI7hoEHTrCeuQEQxAEQRAEQRAEQRAE7UH2eiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgqCfQ55chyAIgiAIgiDoy8hCAoIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCPo68lQKBEEQBEEQ9DFkMgpBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEASdAD3v18rioBi63B6VxUEtUahzChVoO9IRIAiCjuPYng7zliTFTbD7tECJqDhURCYEQRAEQflo7HWE0Kwnb/40dnEDQdBkZBEIQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQdAL5DUlEARBEARBEARBEARBJ0M2hCAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgqAw8hI7CIIgCIIgCIIgCIIgCIIgCIIgCIKgncj1YAiCIAiCIAiCIAiCIAiCIOgnkG1mCIIgCIIg6B3IPBOCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAj6NPKsGwRBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBUAP0vF//evCzuE6//Prb73/UFVfcBD/3331fp93t1BHlnbtRobLiBI9tAhVvGU/QciR8W6JOs56XyFtRoGCo5BUXCrriOoVQccWLO+fYiofQ2HSYV/GOJ3h3nYpRx/DNQ8UdoWOXGtsEuyNzLOrYEUKoY+cMHaljbxmbxEJ1giAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiDoP7/n/VpZXDG63B6VxUHQYBTKBboUBB16CwQlo92T0RCSMFqivMgce4Lzxrvd3XzsCYbmRqZ+V43yWrz4SN//IAiCIAiCIAiCIAiKoo77KrYCIAiCIAiCIAhagVwMhSAIgiAIgiAIgqAfQVbUEHToCBAE9UUd7zWCliPjHQRBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARB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IAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCMtDzfn2NLrdHZZ0gCIIg6AzIGAxtR6EYzytOb4EgCIIg6Esob64SmoaY/kMQBEEQBEHQdz8TZGg7sj8OQRAEQRAEQRAEQRAEQRAEQRAEQRAEtUJu1oAgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCCpEz/u1sjgohi63R2VxEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEATtQM/79TW63B6VdYIgCIIgCIIgCIIgCIKgd6LQnljoSDbOIAiCIOgzKG80z0PmBS1RcaiIAgiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAjKQt6EAEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQ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HVHHxjQZrUYuiUNQPZKfqtHYsaVjivYSlhja/VLp4oqPbac8pAmgwajjsAFVo44DNQRtf4i440ysYy4wtlSj3fEEVaOOmS6vuNCRIAiCoDjancfNnyAIgiAIgiAIgiDob7+Oi+WOdQqhjt+/G1scBEHQaOQWCwiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiC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oeKKj+2cHTtCHhp7WiAIgo5jcIoeOxPbjfJOi+EVKkfFi8DiJNZxwdWxm8tPkMlDFHUc8vXguajjZt7uXKAjtESCLrG43ajjfHzsGNxxAMorDoIgCIIgCIKg736m/xAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAElaPn/foaXW6PyjpBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEPRz6Hm/vkaX26OyThAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQVAFet6vr9Hl9qisEwRBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBUBF63q+VxUEQBEEnQJfb4zUyAEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEHQQhR660BeccXI6xIgCIIgCIIgCIIgCDoXytvrsa8CQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRD095/39SQWB0EQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEHQfJT30lYvSIUgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIJOjrzUB4IgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIKganS5PV6j5/1aWScIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIWoUut0fSkZ73a9KRIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCRqLL7fEaPe/XyjpBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBUD663B6v0fN+rawTBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBL0JXW6PyuLy0PN+rSwOgiAIgiAI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CIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCPpH9LxfX6PL7TGzOAiCIAiCIAiCIAiCIAiCIAiCIGgUet6vf11R6lInCIL+9vvl199+/6OuOAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAj6V/S8X1+jy+2RdKRQnULFhY4EQRAEQRAEQRAEQRAEQRAEQRAEQRAEQWdG7gqAIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCTozyXr9RXKfQkbzIA4IgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIJ8rAuCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCICgLPe/X1+hye1TWCYIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIg6J/R8359jS63R2WdIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiCIAiC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giAIgiAIgiAIgiAIgiAIgiAIgiAIgiDo79Dzfn2NLrfHyjRBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARB0Dz0vF9fo8vt4XGBx0EQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBO2BfGoVgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiCoPvK/6SEIgiAIgt5DefHT4khM4ActRyodBEWR1gJBEARBELQDWjyBD6UpDy1eeah4p6/XgrKbnSYIgsajikNZCLUdqENIPw5BEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARB0Lvoeb++RpfbY+XjQnfKSxMEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQdCxaPGLXhAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEnRE979fX6HJ7rEwTBEEQBEEQBEEQBEEQBEFQF2SNFYIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIg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&quot; id=image6503cd116a style=image-rendering:crisp-edges;image-rendering:pixelated width=9 height=879159 transform=&quot;matrix(64 0 0 0.000164 72 86.4)&quot;/&gt;&lt;/g&gt;&lt;g id=matplotlib.axis_1&gt;&lt;g id=xtick_1&gt;&lt;g id=text_1&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(109.263791 74.352232)rotate(-45)scale(0.104 -0.104)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-46 transform=scale(0.015625) d=&quot;M 525 0 
L 525 4581 
L 3616 4581 
L 3616 4041 
L 1131 4041 
L 1131 2622 
L 3281 2622 
L 3281 2081 
L 1131 2081 
L 1131 0 
L 525 0 
z
&quot;/&gt;&lt;path id=ArialMT-72 transform=scale(0.015625) d=&quot;M 416 0 
L 416 3319 
L 922 3319 
L 922 2816 
Q 1116 3169 1280 3281 
Q 1444 3394 1641 3394 
Q 1925 3394 2219 3213 
L 2025 2691 
Q 1819 2813 1613 2813 
Q 1428 2813 1281 2702 
Q 1134 2591 1072 2394 
Q 978 2094 978 1738 
L 978 0 
L 416 0 
z
&quot;/&gt;&lt;path id=ArialMT-65 transform=scale(0.015625) d=&quot;M 2694 1069 
L 3275 997 
Q 3138 488 2766 206 
Q 2394 -75 1816 -75 
Q 1088 -75 661 373 
Q 234 822 234 1631 
Q 234 2469 665 2931 
Q 1097 3394 1784 3394 
Q 2450 3394 2872 2941 
Q 3294 2488 3294 1666 
Q 3294 1616 3291 1516 
L 816 1516 
Q 847 969 1125 678 
Q 1403 388 1819 388 
Q 2128 388 2347 550 
Q 2566 713 2694 1069 
z
M 847 1978 
L 2700 1978 
Q 2663 2397 2488 2606 
Q 2219 2931 1791 2931 
Q 1403 2931 1139 2672 
Q 875 2413 847 1978 
z
&quot;/&gt;&lt;path id=ArialMT-71 transform=scale(0.015625) d=&quot;M 2538 -1272 
L 2538 353 
Q 2406 169 2170 47 
Q 1934 -75 1669 -75 
Q 1078 -75 651 397 
Q 225 869 225 1691 
Q 225 2191 398 2587 
Q 572 2984 901 3189 
Q 1231 3394 1625 3394 
Q 2241 3394 2594 2875 
L 2594 3319 
L 3100 3319 
L 3100 -1272 
L 2538 -1272 
z
M 803 1669 
Q 803 1028 1072 708 
Q 1341 388 1716 388 
Q 2075 388 2334 692 
Q 2594 997 2594 1619 
Q 2594 2281 2320 2615 
Q 2047 2950 1678 2950 
Q 1313 2950 1058 2639 
Q 803 2328 803 1669 
z
&quot;/&gt;&lt;path id=ArialMT-75 transform=scale(0.015625) d=&quot;M 2597 0 
L 2597 488 
Q 2209 -75 1544 -75 
Q 1250 -75 995 37 
Q 741 150 617 320 
Q 494 491 444 738 
Q 409 903 409 1263 
L 409 3319 
L 972 3319 
L 972 1478 
Q 972 1038 1006 884 
Q 1059 663 1231 536 
Q 1403 409 1656 409 
Q 1909 409 2131 539 
Q 2353 669 2445 892 
Q 2538 1116 2538 1541 
L 2538 3319 
L 3100 3319 
L 3100 0 
L 2597 0 
z
&quot;/&gt;&lt;path id=ArialMT-6e transform=scale(0.015625) d=&quot;M 422 0 
L 422 3319 
L 928 3319 
L 928 2847 
Q 1294 3394 1984 3394 
Q 2284 3394 2536 3286 
Q 2788 3178 2913 3003 
Q 3038 2828 3088 2588 
Q 3119 2431 3119 2041 
L 3119 0 
L 2556 0 
L 2556 2019 
Q 2556 2363 2490 2533 
Q 2425 2703 2258 2804 
Q 2091 2906 1866 2906 
Q 1506 2906 1245 2678 
Q 984 2450 984 1813 
L 984 0 
L 422 0 
z
&quot;/&gt;&lt;path id=ArialMT-63 transform=scale(0.015625) d=&quot;M 2588 1216 
L 3141 1144 
Q 3050 572 2676 248 
Q 2303 -75 1759 -75 
Q 1078 -75 664 370 
Q 250 816 250 1647 
Q 250 2184 428 2587 
Q 606 2991 970 3192 
Q 1334 3394 1763 3394 
Q 2303 3394 2647 3120 
Q 2991 2847 3088 2344 
L 2541 2259 
Q 2463 2594 2264 2762 
Q 2066 2931 1784 2931 
Q 1359 2931 1093 2626 
Q 828 2322 828 1663 
Q 828 994 1084 691 
Q 1341 388 1753 388 
Q 2084 388 2306 591 
Q 2528 794 2588 1216 
z
&quot;/&gt;&lt;path id=ArialMT-79 transform=scale(0.015625) d=&quot;M 397 -1278 
L 334 -750 
Q 519 -800 656 -800 
Q 844 -800 956 -737 
Q 1069 -675 1141 -563 
Q 1194 -478 1313 -144 
Q 1328 -97 1363 -6 
L 103 3319 
L 709 3319 
L 1400 1397 
Q 1534 1031 1641 628 
Q 1738 1016 1872 1384 
L 2581 3319 
L 3144 3319 
L 1881 -56 
Q 1678 -603 1566 -809 
Q 1416 -1088 1222 -1217 
Q 1028 -1347 759 -1347 
Q 597 -1347 397 -1278 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-46 /&gt;&lt;use xlink:href=#ArialMT-72 x=61.083984 /&gt;&lt;use xlink:href=#ArialMT-65 x=94.384766 /&gt;&lt;use xlink:href=#ArialMT-71 x=150 /&gt;&lt;use xlink:href=#ArialMT-75 x=205.615234 /&gt;&lt;use xlink:href=#ArialMT-65 x=261.230469 /&gt;&lt;use xlink:href=#ArialMT-6e x=316.845703 /&gt;&lt;use xlink:href=#ArialMT-63 x=372.460938 /&gt;&lt;use xlink:href=#ArialMT-79 x=422.460938 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_2&gt;&lt;g id=text_2&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(173.263791 74.43841)rotate(-45)scale(0.104 -0.104)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-4c transform=scale(0.015625) d=&quot;M 469 0 
L 469 4581 
L 1075 4581 
L 1075 541 
L 3331 541 
L 3331 0 
L 469 0 
z
&quot;/&gt;&lt;path id=ArialMT-61 transform=scale(0.015625) d=&quot;M 2588 409 
Q 2275 144 1986 34 
Q 1697 -75 1366 -75 
Q 819 -75 525 192 
Q 231 459 231 875 
Q 231 1119 342 1320 
Q 453 1522 633 1644 
Q 813 1766 1038 1828 
Q 1203 1872 1538 1913 
Q 2219 1994 2541 2106 
Q 2544 2222 2544 2253 
Q 2544 2597 2384 2738 
Q 2169 2928 1744 2928 
Q 1347 2928 1158 2789 
Q 969 2650 878 2297 
L 328 2372 
Q 403 2725 575 2942 
Q 747 3159 1072 3276 
Q 1397 3394 1825 3394 
Q 2250 3394 2515 3294 
Q 2781 3194 2906 3042 
Q 3031 2891 3081 2659 
Q 3109 2516 3109 2141 
L 3109 1391 
Q 3109 606 3145 398 
Q 3181 191 3288 0 
L 2700 0 
Q 2613 175 2588 409 
z
M 2541 1666 
Q 2234 1541 1622 1453 
Q 1275 1403 1131 1340 
Q 988 1278 909 1158 
Q 831 1038 831 891 
Q 831 666 1001 516 
Q 1172 366 1500 366 
Q 1825 366 2078 508 
Q 2331 650 2450 897 
Q 2541 1088 2541 1459 
L 2541 1666 
z
&quot;/&gt;&lt;path id=ArialMT-74 transform=scale(0.015625) d=&quot;M 1650 503 
L 1731 6 
Q 1494 -44 1306 -44 
Q 1000 -44 831 53 
Q 663 150 594 308 
Q 525 466 525 972 
L 525 2881 
L 113 2881 
L 113 3319 
L 525 3319 
L 525 4141 
L 1084 4478 
L 1084 3319 
L 1650 3319 
L 1650 2881 
L 1084 2881 
L 1084 941 
Q 1084 700 1114 631 
Q 1144 563 1211 522 
Q 1278 481 1403 481 
Q 1497 481 1650 503 
z
&quot;/&gt;&lt;path id=ArialMT-69 transform=scale(0.015625) d=&quot;M 425 3934 
L 425 4581 
L 988 4581 
L 988 3934 
L 425 3934 
z
M 425 0 
L 425 3319 
L 988 3319 
L 988 0 
L 425 0 
z
&quot;/&gt;&lt;path id=ArialMT-64 transform=scale(0.015625) d=&quot;M 2575 0 
L 2575 419 
Q 2259 -75 1647 -75 
Q 1250 -75 917 144 
Q 584 363 401 755 
Q 219 1147 219 1656 
Q 219 2153 384 2558 
Q 550 2963 881 3178 
Q 1213 3394 1622 3394 
Q 1922 3394 2156 3267 
Q 2391 3141 2538 2938 
L 2538 4581 
L 3097 4581 
L 3097 0 
L 2575 0 
z
M 797 1656 
Q 797 1019 1065 703 
Q 1334 388 1700 388 
Q 2069 388 2326 689 
Q 2584 991 2584 1609 
Q 2584 2291 2321 2609 
Q 2059 2928 1675 2928 
Q 1300 2928 1048 2622 
Q 797 2316 797 1656 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-4c /&gt;&lt;use xlink:href=#ArialMT-61 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-74 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-69 x=139.013672 /&gt;&lt;use xlink:href=#ArialMT-74 x=161.230469 /&gt;&lt;use xlink:href=#ArialMT-75 x=189.013672 /&gt;&lt;use xlink:href=#ArialMT-64 x=244.628906 /&gt;&lt;use xlink:href=#ArialMT-65 x=300.244141 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_3&gt;&lt;g id=text_3&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(237.263791 74.352232)rotate(-45)scale(0.104 -0.104)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-6f transform=scale(0.015625) d=&quot;M 213 1659 
Q 213 2581 725 3025 
Q 1153 3394 1769 3394 
Q 2453 3394 2887 2945 
Q 3322 2497 3322 1706 
Q 3322 1066 3130 698 
Q 2938 331 2570 128 
Q 2203 -75 1769 -75 
Q 1072 -75 642 372 
Q 213 819 213 1659 
z
M 791 1659 
Q 791 1022 1069 705 
Q 1347 388 1769 388 
Q 2188 388 2466 706 
Q 2744 1025 2744 1678 
Q 2744 2294 2464 2611 
Q 2184 2928 1769 2928 
Q 1347 2928 1069 2612 
Q 791 2297 791 1659 
z
&quot;/&gt;&lt;path id=ArialMT-67 transform=scale(0.015625) d=&quot;M 319 -275 
L 866 -356 
Q 900 -609 1056 -725 
Q 1266 -881 1628 -881 
Q 2019 -881 2231 -725 
Q 2444 -569 2519 -288 
Q 2563 -116 2559 434 
Q 2191 0 1641 0 
Q 956 0 581 494 
Q 206 988 206 1678 
Q 206 2153 378 2554 
Q 550 2956 876 3175 
Q 1203 3394 1644 3394 
Q 2231 3394 2613 2919 
L 2613 3319 
L 3131 3319 
L 3131 450 
Q 3131 -325 2973 -648 
Q 2816 -972 2473 -1159 
Q 2131 -1347 1631 -1347 
Q 1038 -1347 672 -1080 
Q 306 -813 319 -275 
z
M 784 1719 
Q 784 1066 1043 766 
Q 1303 466 1694 466 
Q 2081 466 2343 764 
Q 2606 1063 2606 1700 
Q 2606 2309 2336 2618 
Q 2066 2928 1684 2928 
Q 1309 2928 1046 2623 
Q 784 2319 784 1719 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-4c /&gt;&lt;use xlink:href=#ArialMT-6f x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-6e x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-67 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-69 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-74 x=244.677734 /&gt;&lt;use xlink:href=#ArialMT-75 x=272.460938 /&gt;&lt;use xlink:href=#ArialMT-64 x=328.076172 /&gt;&lt;use xlink:href=#ArialMT-65 x=383.691406 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_4&gt;&lt;g id=text_4&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(301.263791 74.43841)rotate(-45)scale(0.104 -0.104)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-44 transform=scale(0.015625) d=&quot;M 494 0 
L 494 4581 
L 2072 4581 
Q 2606 4581 2888 4516 
Q 3281 4425 3559 4188 
Q 3922 3881 4101 3404 
Q 4281 2928 4281 2316 
Q 4281 1794 4159 1391 
Q 4038 988 3847 723 
Q 3656 459 3429 307 
Q 3203 156 2883 78 
Q 2563 0 2147 0 
L 494 0 
z
M 1100 541 
L 2078 541 
Q 2531 541 2789 625 
Q 3047 709 3200 863 
Q 3416 1078 3536 1442 
Q 3656 1806 3656 2325 
Q 3656 3044 3420 3430 
Q 3184 3816 2847 3947 
Q 2603 4041 2063 4041 
L 1100 4041 
L 1100 541 
z
&quot;/&gt;&lt;path id=ArialMT-73 transform=scale(0.015625) d=&quot;M 197 991 
L 753 1078 
Q 800 744 1014 566 
Q 1228 388 1613 388 
Q 2000 388 2187 545 
Q 2375 703 2375 916 
Q 2375 1106 2209 1216 
Q 2094 1291 1634 1406 
Q 1016 1563 777 1677 
Q 538 1791 414 1992 
Q 291 2194 291 2438 
Q 291 2659 392 2848 
Q 494 3038 669 3163 
Q 800 3259 1026 3326 
Q 1253 3394 1513 3394 
Q 1903 3394 2198 3281 
Q 2494 3169 2634 2976 
Q 2775 2784 2828 2463 
L 2278 2388 
Q 2241 2644 2061 2787 
Q 1881 2931 1553 2931 
Q 1166 2931 1000 2803 
Q 834 2675 834 2503 
Q 834 2394 903 2306 
Q 972 2216 1119 2156 
Q 1203 2125 1616 2013 
Q 2213 1853 2448 1751 
Q 2684 1650 2818 1456 
Q 2953 1263 2953 975 
Q 2953 694 2789 445 
Q 2625 197 2315 61 
Q 2006 -75 1616 -75 
Q 969 -75 630 194 
Q 291 463 197 991 
z
&quot;/&gt;&lt;path id=ArialMT-70 transform=scale(0.015625) d=&quot;M 422 -1272 
L 422 3319 
L 934 3319 
L 934 2888 
Q 1116 3141 1344 3267 
Q 1572 3394 1897 3394 
Q 2322 3394 2647 3175 
Q 2972 2956 3137 2557 
Q 3303 2159 3303 1684 
Q 3303 1175 3120 767 
Q 2938 359 2589 142 
Q 2241 -75 1856 -75 
Q 1575 -75 1351 44 
Q 1128 163 984 344 
L 984 -1272 
L 422 -1272 
z
M 931 1641 
Q 931 1000 1190 694 
Q 1450 388 1819 388 
Q 2194 388 2461 705 
Q 2728 1022 2728 1688 
Q 2728 2322 2467 2637 
Q 2206 2953 1844 2953 
Q 1484 2953 1207 2617 
Q 931 2281 931 1641 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-44 /&gt;&lt;use xlink:href=#ArialMT-65 x=72.216797 /&gt;&lt;use xlink:href=#ArialMT-73 x=127.832031 /&gt;&lt;use xlink:href=#ArialMT-63 x=177.832031 /&gt;&lt;use xlink:href=#ArialMT-72 x=227.832031 /&gt;&lt;use xlink:href=#ArialMT-69 x=261.132812 /&gt;&lt;use xlink:href=#ArialMT-70 x=283.349609 /&gt;&lt;use xlink:href=#ArialMT-74 x=338.964844 /&gt;&lt;use xlink:href=#ArialMT-69 x=366.748047 /&gt;&lt;use xlink:href=#ArialMT-6f x=388.964844 /&gt;&lt;use xlink:href=#ArialMT-6e x=444.580078 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_5&gt;&lt;g id=text_5&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(365.263791 74.43841)rotate(-45)scale(0.104 -0.104)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-53 transform=scale(0.015625) d=&quot;M 288 1472 
L 859 1522 
Q 900 1178 1048 958 
Q 1197 738 1509 602 
Q 1822 466 2213 466 
Q 2559 466 2825 569 
Q 3091 672 3220 851 
Q 3350 1031 3350 1244 
Q 3350 1459 3225 1620 
Q 3100 1781 2813 1891 
Q 2628 1963 1997 2114 
Q 1366 2266 1113 2400 
Q 784 2572 623 2826 
Q 463 3081 463 3397 
Q 463 3744 659 4045 
Q 856 4347 1234 4503 
Q 1613 4659 2075 4659 
Q 2584 4659 2973 4495 
Q 3363 4331 3572 4012 
Q 3781 3694 3797 3291 
L 3216 3247 
Q 3169 3681 2898 3903 
Q 2628 4125 2100 4125 
Q 1550 4125 1298 3923 
Q 1047 3722 1047 3438 
Q 1047 3191 1225 3031 
Q 1400 2872 2139 2705 
Q 2878 2538 3153 2413 
Q 3553 2228 3743 1945 
Q 3934 1663 3934 1294 
Q 3934 928 3725 604 
Q 3516 281 3123 101 
Q 2731 -78 2241 -78 
Q 1619 -78 1198 103 
Q 778 284 539 648 
Q 300 1013 288 1472 
z
&quot;/&gt;&lt;path id=ArialMT-76 transform=scale(0.015625) d=&quot;M 1344 0 
L 81 3319 
L 675 3319 
L 1388 1331 
Q 1503 1009 1600 663 
Q 1675 925 1809 1294 
L 2547 3319 
L 3125 3319 
L 1869 0 
L 1344 0 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-53 /&gt;&lt;use xlink:href=#ArialMT-65 x=66.699219 /&gt;&lt;use xlink:href=#ArialMT-72 x=122.314453 /&gt;&lt;use xlink:href=#ArialMT-76 x=155.615234 /&gt;&lt;use xlink:href=#ArialMT-69 x=205.615234 /&gt;&lt;use xlink:href=#ArialMT-63 x=227.832031 /&gt;&lt;use xlink:href=#ArialMT-65 x=277.832031 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_6&gt;&lt;g id=text_6&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(429.263791 74.43841)rotate(-45)scale(0.104 -0.104)&quot;&gt;&lt;use xlink:href=#ArialMT-53 /&gt;&lt;use xlink:href=#ArialMT-74 x=66.699219 /&gt;&lt;use xlink:href=#ArialMT-61 x=94.482422 /&gt;&lt;use xlink:href=#ArialMT-74 x=150.097656 /&gt;&lt;use xlink:href=#ArialMT-69 x=177.880859 /&gt;&lt;use xlink:href=#ArialMT-6f x=200.097656 /&gt;&lt;use xlink:href=#ArialMT-6e x=255.712891 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_7&gt;&lt;g id=text_7&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(493.263791 74.43841)rotate(-45)scale(0.104 -0.104)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-43 transform=scale(0.015625) d=&quot;M 3763 1606 
L 4369 1453 
Q 4178 706 3683 314 
Q 3188 -78 2472 -78 
Q 1731 -78 1267 223 
Q 803 525 561 1097 
Q 319 1669 319 2325 
Q 319 3041 592 3573 
Q 866 4106 1370 4382 
Q 1875 4659 2481 4659 
Q 3169 4659 3637 4309 
Q 4106 3959 4291 3325 
L 3694 3184 
Q 3534 3684 3231 3912 
Q 2928 4141 2469 4141 
Q 1941 4141 1586 3887 
Q 1231 3634 1087 3207 
Q 944 2781 944 2328 
Q 944 1744 1114 1308 
Q 1284 872 1643 656 
Q 2003 441 2422 441 
Q 2931 441 3284 734 
Q 3638 1028 3763 1606 
z
&quot;/&gt;&lt;path id=ArialMT-6c transform=scale(0.015625) d=&quot;M 409 0 
L 409 4581 
L 972 4581 
L 972 0 
L 409 0 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-43 /&gt;&lt;use xlink:href=#ArialMT-6c x=72.216797 /&gt;&lt;use xlink:href=#ArialMT-61 x=94.433594 /&gt;&lt;use xlink:href=#ArialMT-73 x=150.048828 /&gt;&lt;use xlink:href=#ArialMT-73 x=200.048828 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_8&gt;&lt;g id=text_8&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(557.263791 74.43841)rotate(-45)scale(0.104 -0.104)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-42 transform=scale(0.015625) d=&quot;M 469 0 
L 469 4581 
L 2188 4581 
Q 2713 4581 3030 4442 
Q 3347 4303 3526 4014 
Q 3706 3725 3706 3409 
Q 3706 3116 3547 2856 
Q 3388 2597 3066 2438 
Q 3481 2316 3704 2022 
Q 3928 1728 3928 1328 
Q 3928 1006 3792 729 
Q 3656 453 3456 303 
Q 3256 153 2954 76 
Q 2653 0 2216 0 
L 469 0 
z
M 1075 2656 
L 2066 2656 
Q 2469 2656 2644 2709 
Q 2875 2778 2992 2937 
Q 3109 3097 3109 3338 
Q 3109 3566 3000 3739 
Q 2891 3913 2687 3977 
Q 2484 4041 1991 4041 
L 1075 4041 
L 1075 2656 
z
M 1075 541 
L 2216 541 
Q 2509 541 2628 563 
Q 2838 600 2978 687 
Q 3119 775 3209 942 
Q 3300 1109 3300 1328 
Q 3300 1584 3169 1773 
Q 3038 1963 2805 2039 
Q 2572 2116 2134 2116 
L 1075 2116 
L 1075 541 
z
&quot;/&gt;&lt;path id=ArialMT-57 transform=scale(0.015625) d=&quot;M 1294 0 
L 78 4581 
L 700 4581 
L 1397 1578 
Q 1509 1106 1591 641 
Q 1766 1375 1797 1488 
L 2669 4581 
L 3400 4581 
L 4056 2263 
Q 4303 1400 4413 641 
Q 4500 1075 4641 1638 
L 5359 4581 
L 5969 4581 
L 4713 0 
L 4128 0 
L 3163 3491 
Q 3041 3928 3019 4028 
Q 2947 3713 2884 3491 
L 1913 0 
L 1294 0 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-42 /&gt;&lt;use xlink:href=#ArialMT-57 x=66.699219 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=xtick_9&gt;&lt;g id=text_9&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(621.263791 74.43841)rotate(-45)scale(0.104 -0.104)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-49 transform=scale(0.015625) d=&quot;M 597 0 
L 597 4581 
L 1203 4581 
L 1203 0 
L 597 0 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-49 /&gt;&lt;use xlink:href=#ArialMT-64 x=27.783203 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=matplotlib.axis_2&gt;&lt;g id=ytick_1&gt;&lt;g id=text_10&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(54.270781 91.05266)scale(0.13 -0.13)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-31 transform=scale(0.015625) d=&quot;M 2384 0 
L 1822 0 
L 1822 3584 
Q 1619 3391 1289 3197 
Q 959 3003 697 2906 
L 697 3450 
Q 1169 3672 1522 3987 
Q 1875 4303 2022 4600 
L 2384 4600 
L 2384 0 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-31 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=ytick_2&gt;&lt;g id=text_11&gt;&lt;g style=&quot;fill: #262626&quot; transform=&quot;translate(18.124688 235.052496)scale(0.13 -0.13)&quot;&gt;&lt;defs&gt;&lt;path id=ArialMT-38 transform=scale(0.015625) d=&quot;M 1131 2484 
Q 781 2613 612 2850 
Q 444 3088 444 3419 
Q 444 3919 803 4259 
Q 1163 4600 1759 4600 
Q 2359 4600 2725 4251 
Q 3091 3903 3091 3403 
Q 3091 3084 2923 2848 
Q 2756 2613 2416 2484 
Q 2838 2347 3058 2040 
Q 3278 1734 3278 1309 
Q 3278 722 2862 322 
Q 2447 -78 1769 -78 
Q 1091 -78 675 323 
Q 259 725 259 1325 
Q 259 1772 486 2073 
Q 713 2375 1131 2484 
z
M 1019 3438 
Q 1019 3113 1228 2906 
Q 1438 2700 1772 2700 
Q 2097 2700 2305 2904 
Q 2513 3109 2513 3406 
Q 2513 3716 2298 3927 
Q 2084 4138 1766 4138 
Q 1444 4138 1231 3931 
Q 1019 3725 1019 3438 
z
M 838 1322 
Q 838 1081 952 856 
Q 1066 631 1291 507 
Q 1516 384 1775 384 
Q 2178 384 2440 643 
Q 2703 903 2703 1303 
Q 2703 1709 2433 1975 
Q 2163 2241 1756 2241 
Q 1359 2241 1098 1978 
Q 838 1716 838 1322 
z
&quot;/&gt;&lt;path id=ArialMT-37 transform=scale(0.015625) d=&quot;M 303 3981 
L 303 4522 
L 3269 4522 
L 3269 4084 
Q 2831 3619 2401 2847 
Q 1972 2075 1738 1259 
Q 1569 684 1522 0 
L 944 0 
Q 953 541 1156 1306 
Q 1359 2072 1739 2783 
Q 2119 3494 2547 3981 
L 303 3981 
z
&quot;/&gt;&lt;path id=ArialMT-39 transform=scale(0.015625) d=&quot;M 350 1059 
L 891 1109 
Q 959 728 1153 556 
Q 1347 384 1650 384 
Q 1909 384 2104 503 
Q 2300 622 2425 820 
Q 2550 1019 2634 1356 
Q 2719 1694 2719 2044 
Q 2719 2081 2716 2156 
Q 2547 1888 2255 1720 
Q 1963 1553 1622 1553 
Q 1053 1553 659 1965 
Q 266 2378 266 3053 
Q 266 3750 677 4175 
Q 1088 4600 1706 4600 
Q 2153 4600 2523 4359 
Q 2894 4119 3086 3673 
Q 3278 3228 3278 2384 
Q 3278 1506 3087 986 
Q 2897 466 2520 194 
Q 2144 -78 1638 -78 
Q 1100 -78 759 220 
Q 419 519 350 1059 
z
M 2653 3081 
Q 2653 3566 2395 3850 
Q 2138 4134 1775 4134 
Q 1400 4134 1122 3828 
Q 844 3522 844 3034 
Q 844 2597 1108 2323 
Q 1372 2050 1759 2050 
Q 2150 2050 2401 2323 
Q 2653 2597 2653 3081 
z
&quot;/&gt;&lt;path id=ArialMT-35 transform=scale(0.015625) d=&quot;M 266 1200 
L 856 1250 
Q 922 819 1161 601 
Q 1400 384 1738 384 
Q 2144 384 2425 690 
Q 2706 997 2706 1503 
Q 2706 1984 2436 2262 
Q 2166 2541 1728 2541 
Q 1456 2541 1237 2417 
Q 1019 2294 894 2097 
L 366 2166 
L 809 4519 
L 3088 4519 
L 3088 3981 
L 1259 3981 
L 1013 2750 
Q 1425 3038 1878 3038 
Q 2478 3038 2890 2622 
Q 3303 2206 3303 1553 
Q 3303 931 2941 478 
Q 2500 -78 1738 -78 
Q 1113 -78 717 272 
Q 322 622 266 1200 
z
&quot;/&gt;&lt;/defs&gt;&lt;use xlink:href=#ArialMT-38 /&gt;&lt;use xlink:href=#ArialMT-37 x=55.615234 /&gt;&lt;use xlink:href=#ArialMT-39 x=111.230469 /&gt;&lt;use xlink:href=#ArialMT-31 x=166.845703 /&gt;&lt;use xlink:href=#ArialMT-35 x=222.460938 /&gt;&lt;use xlink:href=#ArialMT-39 x=278.076172 /&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;g id=line2d_1&gt;&lt;path d=&quot;M 136 230.4 
L 136 86.4 
&quot; clip-path=url(#p494c45c964) style=&quot;fill: none; stroke: #ffffff; stroke-width: 1.75; stroke-linecap: round&quot;/&gt;&lt;/g&gt;&lt;g id=line2d_2&gt;&lt;path d=&quot;M 200 230.4 
L 200 86.4 
&quot; clip-path=url(#p494c45c964) style=&quot;fill: none; stroke: #ffffff; stroke-width: 1.75; stroke-linecap: round&quot;/&gt;&lt;/g&gt;&lt;g id=line2d_3&gt;&lt;path d=&quot;M 264 230.4 
L 264 86.4 
&quot; clip-path=url(#p494c45c964) style=&quot;fill: none; stroke: #ffffff; stroke-width: 1.75; stroke-linecap: round&quot;/&gt;&lt;/g&gt;&lt;g id=line2d_4&gt;&lt;path d=&quot;M 328 230.4 
L 328 86.4 
&quot; clip-path=url(#p494c45c964) style=&quot;fill: none; stroke: #ffffff; stroke-width: 1.75; stroke-linecap: round&quot;/&gt;&lt;/g&gt;&lt;g id=line2d_5&gt;&lt;path d=&quot;M 392 230.4 
L 392 86.4 
&quot; clip-path=url(#p494c45c964) style=&quot;fill: none; stroke: #ffffff; stroke-width: 1.75; stroke-linecap: round&quot;/&gt;&lt;/g&gt;&lt;g id=line2d_6&gt;&lt;path d=&quot;M 456 230.4 
L 456 86.4 
&quot; clip-path=url(#p494c45c964) style=&quot;fill: none; stroke: #ffffff; stroke-width: 1.75; stroke-linecap: round&quot;/&gt;&lt;/g&gt;&lt;g id=line2d_7&gt;&lt;path d=&quot;M 520 230.4 
L 520 86.4 
&quot; clip-path=url(#p494c45c964) style=&quot;fill: none; stroke: #ffffff; stroke-width: 1.75; stroke-linecap: round&quot;/&gt;&lt;/g&gt;&lt;g id=line2d_8&gt;&lt;path d=&quot;M 584 230.4 
L 584 86.4 
&quot; clip-path=url(#p494c45c964) style=&quot;fill: none; stroke: #ffffff; stroke-width: 1.75; stroke-linecap: round&quot;/&gt;&lt;/g&gt;&lt;/g&gt;&lt;/g&gt;&lt;defs&gt;&lt;clippath id=p494c45c964&gt;&lt;rect x=72 y=86.4 width=576 height=144 /&gt;&lt;/clippath&gt;&lt;/defs&gt;&lt;/svg&gt;&lt;div class=&quot;caption text-center text-muted&quot;&gt; Nullity matrix is a data-dense display which lets you quickly visually pick out patterns in data completion. &lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;div class=&quot;row header&quot;&gt;&lt;a class=anchor-pos id=sample&gt;&lt;/a&gt;&lt;h1 class=page-header&gt;Sample&lt;/h1&gt;&lt;/div&gt;&lt;div class=section-items&gt;&lt;div class=&quot;row spacing&quot;&gt;&lt;h2 class=indent&gt;First rows&lt;/h2&gt;&lt;div id=sample-container class=col-sm-12&gt;&lt;table border=1 class=&quot;dataframe sample table table-striped&quot;&gt;&lt;thead&gt;&lt;tr style=&quot;text-align: right;&quot;&gt;&lt;th&gt;&lt;/th&gt;&lt;th&gt;Frequency&lt;/th&gt;&lt;th&gt;Latitude&lt;/th&gt;&lt;th&gt;Longitude&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;th&gt;Service&lt;/th&gt;&lt;th&gt;Station&lt;/th&gt;&lt;th&gt;Class&lt;/th&gt;&lt;th&gt;BW&lt;/th&gt;&lt;th&gt;Id&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;0&lt;/th&gt;&lt;td&gt;0.0280&lt;/td&gt;&lt;td&gt;-22.662778&lt;/td&gt;&lt;td&gt;-43.476389&lt;/td&gt;&lt;td&gt;[STEL] L, Furnas Centrais Eletricas S A (01030052263, 1557670), Nova Iguaçu/RJ&lt;/td&gt;&lt;td&gt;019&lt;/td&gt;&lt;td&gt;1557670&lt;/td&gt;&lt;td&gt;J9E&lt;/td&gt;&lt;td&gt;8.0&lt;/td&gt;&lt;td&gt;0&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;1&lt;/th&gt;&lt;td&gt;0.0285&lt;/td&gt;&lt;td&gt;-26.292500&lt;/td&gt;&lt;td&gt;-48.887222&lt;/td&gt;&lt;td&gt;[STEL] L, Companhia De Geração E Transmissão De Energia Elétrica Do Sul Do Brasil - Eletrobrás Cgt Eletrosul (50420217282, 1494686), Joinville/SC&lt;/td&gt;&lt;td&gt;019&lt;/td&gt;&lt;td&gt;1494686&lt;/td&gt;&lt;td&gt;R3E&lt;/td&gt;&lt;td&gt;2.5&lt;/td&gt;&lt;td&gt;1&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;2&lt;/th&gt;&lt;td&gt;0.0300&lt;/td&gt;&lt;td&gt;-23.710000&lt;/td&gt;&lt;td&gt;-46.273333&lt;/td&gt;&lt;td&gt;[STEL] L, Furnas Centrais Eletricas S A (01030052263, 1558412), Mogi das Cruzes/SP&lt;/td&gt;&lt;td&gt;019&lt;/td&gt;&lt;td&gt;1558412&lt;/td&gt;&lt;td&gt;J3E&lt;/td&gt;&lt;td&gt;2.0&lt;/td&gt;&lt;td&gt;2&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;3&lt;/th&gt;&lt;td&gt;0.0300&lt;/td&gt;&lt;td&gt;-23.441667&lt;/td&gt;&lt;td&gt;-46.590833&lt;/td&gt;&lt;td&gt;[STEL] L, Furnas Centrais Eletricas S A (01030052263, 1557823), São Paulo/SP&lt;/td&gt;&lt;td&gt;019&lt;/td&gt;&lt;td&gt;1557823&lt;/td&gt;&lt;td&gt;J3E&lt;/td&gt;&lt;td&gt;1.0&lt;/td&gt;&lt;td&gt;3&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;4&lt;/th&gt;&lt;td&gt;0.0300&lt;/td&gt;&lt;td&gt;-22.926667&lt;/td&gt;&lt;td&gt;-43.265000&lt;/td&gt;&lt;td&gt;[STEL] L, Furnas Centrais Eletricas S A (01030052263, 859761), Rio de Janeiro/RJ&lt;/td&gt;&lt;td&gt;019&lt;/td&gt;&lt;td&gt;859761&lt;/td&gt;&lt;td&gt;J3E&lt;/td&gt;&lt;td&gt;0.5&lt;/td&gt;&lt;td&gt;4&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;5&lt;/th&gt;&lt;td&gt;0.0300&lt;/td&gt;&lt;td&gt;-22.774167&lt;/td&gt;&lt;td&gt;-47.004444&lt;/td&gt;&lt;td&gt;[STEL] L, Furnas Centrais Eletricas S A (01030052263, 859753), Campinas/SP&lt;/td&gt;&lt;td&gt;019&lt;/td&gt;&lt;td&gt;859753&lt;/td&gt;&lt;td&gt;J3E&lt;/td&gt;&lt;td&gt;1.0&lt;/td&gt;&lt;td&gt;5&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;6&lt;/th&gt;&lt;td&gt;0.0300&lt;/td&gt;&lt;td&gt;-18.410000&lt;/td&gt;&lt;td&gt;-49.100000&lt;/td&gt;&lt;td&gt;[STEL] L, Furnas Centrais Eletricas S A (01030052263, 859966), Araporã/MG&lt;/td&gt;&lt;td&gt;019&lt;/td&gt;&lt;td&gt;859966&lt;/td&gt;&lt;td&gt;J3E&lt;/td&gt;&lt;td&gt;1.0&lt;/td&gt;&lt;td&gt;6&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;7&lt;/th&gt;&lt;td&gt;0.0315&lt;/td&gt;&lt;td&gt;-19.928889&lt;/td&gt;&lt;td&gt;-43.865278&lt;/td&gt;&lt;td&gt;[STEL] L, Cemig Geracao E Transmissao S.A (50402658671, 990060), Nova Lima/MG&lt;/td&gt;&lt;td&gt;019&lt;/td&gt;&lt;td&gt;990060&lt;/td&gt;&lt;td&gt;NaN&lt;/td&gt;&lt;td&gt;-1.0&lt;/td&gt;&lt;td&gt;7&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;8&lt;/th&gt;&lt;td&gt;0.0315&lt;/td&gt;&lt;td&gt;-19.595833&lt;/td&gt;&lt;td&gt;-43.198889&lt;/td&gt;&lt;td&gt;[STEL] L, Cemig Distribuicao S.A (50402659058, 1028375), Itabira/MG&lt;/td&gt;&lt;td&gt;019&lt;/td&gt;&lt;td&gt;1028375&lt;/td&gt;&lt;td&gt;NaN&lt;/td&gt;&lt;td&gt;-1.0&lt;/td&gt;&lt;td&gt;8&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;9&lt;/th&gt;&lt;td&gt;0.0320&lt;/td&gt;&lt;td&gt;-22.630278&lt;/td&gt;&lt;td&gt;-45.045833&lt;/td&gt;&lt;td&gt;[STEL] L, Furnas Centrais Eletricas S A (01030052263, 1558358), Cachoeira Paulista/SP&lt;/td&gt;&lt;td&gt;019&lt;/td&gt;&lt;td&gt;1558358&lt;/td&gt;&lt;td&gt;J3E&lt;/td&gt;&lt;td&gt;2.0&lt;/td&gt;&lt;td&gt;9&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;/div&gt;&lt;div class=&quot;row spacing&quot;&gt;&lt;h2 class=indent&gt;Last rows&lt;/h2&gt;&lt;div id=sample-container class=col-sm-12&gt;&lt;table border=1 class=&quot;dataframe sample table table-striped&quot;&gt;&lt;thead&gt;&lt;tr style=&quot;text-align: right;&quot;&gt;&lt;th&gt;&lt;/th&gt;&lt;th&gt;Frequency&lt;/th&gt;&lt;th&gt;Latitude&lt;/th&gt;&lt;th&gt;Longitude&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;th&gt;Service&lt;/th&gt;&lt;th&gt;Station&lt;/th&gt;&lt;th&gt;Class&lt;/th&gt;&lt;th&gt;BW&lt;/th&gt;&lt;th&gt;Id&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;879149&lt;/th&gt;&lt;td&gt;84844.0&lt;/td&gt;&lt;td&gt;2.842917&lt;/td&gt;&lt;td&gt;-60.668583&lt;/td&gt;&lt;td&gt;[STEL] L, Tim S A (50417425295, 1009657370), Boa Vista/RR&lt;/td&gt;&lt;td&gt;019&lt;/td&gt;&lt;td&gt;1009657370&lt;/td&gt;&lt;td&gt;Q7W&lt;/td&gt;&lt;td&gt;62500.0&lt;/td&gt;&lt;td&gt;879149&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;879150&lt;/th&gt;&lt;td&gt;84875.0&lt;/td&gt;&lt;td&gt;-18.909806&lt;/td&gt;&lt;td&gt;-48.258583&lt;/td&gt;&lt;td&gt;[STEL] L, Tim S A (50417425295, 1005312408), Uberlândia/MG&lt;/td&gt;&lt;td&gt;019&lt;/td&gt;&lt;td&gt;1005312408&lt;/td&gt;&lt;td&gt;G7W&lt;/td&gt;&lt;td&gt;2000000.0&lt;/td&gt;&lt;td&gt;879151&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;879151&lt;/th&gt;&lt;td&gt;84875.0&lt;/td&gt;&lt;td&gt;-11.014361&lt;/td&gt;&lt;td&gt;-37.076556&lt;/td&gt;&lt;td&gt;[STEL] L, Tim S A (50417425295, 1005320656), Aracaju/SE&lt;/td&gt;&lt;td&gt;019&lt;/td&gt;&lt;td&gt;1005320656&lt;/td&gt;&lt;td&gt;D7W&lt;/td&gt;&lt;td&gt;56000.0&lt;/td&gt;&lt;td&gt;879150&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;879152&lt;/th&gt;&lt;td&gt;85469.0&lt;/td&gt;&lt;td&gt;-23.624083&lt;/td&gt;&lt;td&gt;-46.623944&lt;/td&gt;&lt;td&gt;[STEL] L, Tim S A (50417425295, 1007183141), São Paulo/SP&lt;/td&gt;&lt;td&gt;019&lt;/td&gt;&lt;td&gt;1007183141&lt;/td&gt;&lt;td&gt;Q7W&lt;/td&gt;&lt;td&gt;62500.0&lt;/td&gt;&lt;td&gt;879152&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;879153&lt;/th&gt;&lt;td&gt;85469.0&lt;/td&gt;&lt;td&gt;-19.857389&lt;/td&gt;&lt;td&gt;-44.616111&lt;/td&gt;&lt;td&gt;[STEL] L, Tim S A (50417425295, 1009125734), Pará de Minas/MG&lt;/td&gt;&lt;td&gt;019&lt;/td&gt;&lt;td&gt;1009125734&lt;/td&gt;&lt;td&gt;Q7W&lt;/td&gt;&lt;td&gt;62500.0&lt;/td&gt;&lt;td&gt;879153&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;879154&lt;/th&gt;&lt;td&gt;85469.0&lt;/td&gt;&lt;td&gt;-16.592700&lt;/td&gt;&lt;td&gt;-49.267800&lt;/td&gt;&lt;td&gt;[STEL] L, Tim S A (50417425295, 1008754061), Goiânia/GO&lt;/td&gt;&lt;td&gt;019&lt;/td&gt;&lt;td&gt;1008754061&lt;/td&gt;&lt;td&gt;Q7W&lt;/td&gt;&lt;td&gt;62500.0&lt;/td&gt;&lt;td&gt;879154&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;879155&lt;/th&gt;&lt;td&gt;85469.0&lt;/td&gt;&lt;td&gt;-9.937444&lt;/td&gt;&lt;td&gt;-67.827750&lt;/td&gt;&lt;td&gt;[STEL] L, Tim S A (50417425295, 1005059940), Rio Branco/AC&lt;/td&gt;&lt;td&gt;019&lt;/td&gt;&lt;td&gt;1005059940&lt;/td&gt;&lt;td&gt;Q7W&lt;/td&gt;&lt;td&gt;62500.0&lt;/td&gt;&lt;td&gt;879155&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;879156&lt;/th&gt;&lt;td&gt;85469.0&lt;/td&gt;&lt;td&gt;-8.266858&lt;/td&gt;&lt;td&gt;-36.006025&lt;/td&gt;&lt;td&gt;[STEL] L, Tim S A (50417425295, 1009131726), Caruaru/PE&lt;/td&gt;&lt;td&gt;019&lt;/td&gt;&lt;td&gt;1009131726&lt;/td&gt;&lt;td&gt;Q7W&lt;/td&gt;&lt;td&gt;62500.0&lt;/td&gt;&lt;td&gt;879156&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;879157&lt;/th&gt;&lt;td&gt;85469.0&lt;/td&gt;&lt;td&gt;-3.734861&lt;/td&gt;&lt;td&gt;-38.462750&lt;/td&gt;&lt;td&gt;[STEL] L, Tim S A (50417425295, 1008775875), Fortaleza/CE&lt;/td&gt;&lt;td&gt;019&lt;/td&gt;&lt;td&gt;1008775875&lt;/td&gt;&lt;td&gt;Q7W&lt;/td&gt;&lt;td&gt;62500.0&lt;/td&gt;&lt;td&gt;879157&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;879158&lt;/th&gt;&lt;td&gt;85469.0&lt;/td&gt;&lt;td&gt;-1.358931&lt;/td&gt;&lt;td&gt;-48.385669&lt;/td&gt;&lt;td&gt;[STEL] L, Tim S A (50417425295, 1009786951), Ananindeua/PA&lt;/td&gt;&lt;td&gt;019&lt;/td&gt;&lt;td&gt;1009786951&lt;/td&gt;&lt;td&gt;Q7W&lt;/td&gt;&lt;td&gt;750000.0&lt;/td&gt;&lt;td&gt;879158&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;/div&gt;&lt;div class=&quot;row spacing&quot;&gt;&lt;h2 class=indent&gt;Random sample&lt;/h2&gt;&lt;div id=sample-container class=col-sm-12&gt;&lt;table border=1 class=&quot;dataframe sample table table-striped&quot;&gt;&lt;thead&gt;&lt;tr style=&quot;text-align: right;&quot;&gt;&lt;th&gt;&lt;/th&gt;&lt;th&gt;Frequency&lt;/th&gt;&lt;th&gt;Latitude&lt;/th&gt;&lt;th&gt;Longitude&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;th&gt;Service&lt;/th&gt;&lt;th&gt;Station&lt;/th&gt;&lt;th&gt;Class&lt;/th&gt;&lt;th&gt;BW&lt;/th&gt;&lt;th&gt;Id&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;202915&lt;/th&gt;&lt;td&gt;162.84375&lt;/td&gt;&lt;td&gt;-22.013889&lt;/td&gt;&lt;td&gt;-47.890889&lt;/td&gt;&lt;td&gt;[STEL] L, Engefort Sistema Avancado De Seguranca Ltda (50001587927, 697541185), São Carlos/SP&lt;/td&gt;&lt;td&gt;019&lt;/td&gt;&lt;td&gt;697541185&lt;/td&gt;&lt;td&gt;F1W&lt;/td&gt;&lt;td&gt;7.6&lt;/td&gt;&lt;td&gt;202964&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;488665&lt;/th&gt;&lt;td&gt;169.63000&lt;/td&gt;&lt;td&gt;-15.847500&lt;/td&gt;&lt;td&gt;-48.116389&lt;/td&gt;&lt;td&gt;[STEL] L, Policia Civil Do Distrito Federal (50004158687, 535728131), Brasília/DF&lt;/td&gt;&lt;td&gt;019&lt;/td&gt;&lt;td&gt;535728131&lt;/td&gt;&lt;td&gt;F3E&lt;/td&gt;&lt;td&gt;16.0&lt;/td&gt;&lt;td&gt;488639&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;66940&lt;/th&gt;&lt;td&gt;149.13000&lt;/td&gt;&lt;td&gt;-20.083889&lt;/td&gt;&lt;td&gt;-48.818056&lt;/td&gt;&lt;td&gt;[STEL] L, Usina Frutal Açucar E Alcool S/A (50402591313, 687987385), Frutal/MG&lt;/td&gt;&lt;td&gt;019&lt;/td&gt;&lt;td&gt;687987385&lt;/td&gt;&lt;td&gt;F1W&lt;/td&gt;&lt;td&gt;7.6&lt;/td&gt;&lt;td&gt;66881&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;496626&lt;/th&gt;&lt;td&gt;171.41875&lt;/td&gt;&lt;td&gt;-18.848825&lt;/td&gt;&lt;td&gt;-41.980036&lt;/td&gt;&lt;td&gt;[STEL] L, Cemig Geracao E Transmissao S.A (50402658671, 1009210871), Governador Valadares/MG&lt;/td&gt;&lt;td&gt;019&lt;/td&gt;&lt;td&gt;1009210871&lt;/td&gt;&lt;td&gt;F1W&lt;/td&gt;&lt;td&gt;7.6&lt;/td&gt;&lt;td&gt;496604&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;844315&lt;/th&gt;&lt;td&gt;21991.00000&lt;/td&gt;&lt;td&gt;-23.608200&lt;/td&gt;&lt;td&gt;-46.750000&lt;/td&gt;&lt;td&gt;[STEL] L, Claro S.A. (50001392751, 422386669), São Paulo/SP&lt;/td&gt;&lt;td&gt;053&lt;/td&gt;&lt;td&gt;422386669&lt;/td&gt;&lt;td&gt;D7W&lt;/td&gt;&lt;td&gt;28000.0&lt;/td&gt;&lt;td&gt;844412&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;180160&lt;/th&gt;&lt;td&gt;161.19000&lt;/td&gt;&lt;td&gt;-20.895278&lt;/td&gt;&lt;td&gt;-46.716389&lt;/td&gt;&lt;td&gt;[STEL] L, Votorantim Metais Zinco S.A. (50414569253, 1224166), Fortaleza de Minas/MG&lt;/td&gt;&lt;td&gt;019&lt;/td&gt;&lt;td&gt;1224166&lt;/td&gt;&lt;td&gt;F1E&lt;/td&gt;&lt;td&gt;7.6&lt;/td&gt;&lt;td&gt;180196&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;13178&lt;/th&gt;&lt;td&gt;48.40000&lt;/td&gt;&lt;td&gt;-28.796944&lt;/td&gt;&lt;td&gt;-52.516944&lt;/td&gt;&lt;td&gt;[STEL] L, Ministério Da Justiça - Departamento De Policia Rod. Federal (50401653404, 686788818), Soledade/RS&lt;/td&gt;&lt;td&gt;019&lt;/td&gt;&lt;td&gt;686788818&lt;/td&gt;&lt;td&gt;F3E&lt;/td&gt;&lt;td&gt;16.0&lt;/td&gt;&lt;td&gt;13205&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;839491&lt;/th&gt;&lt;td&gt;21847.00000&lt;/td&gt;&lt;td&gt;-22.934000&lt;/td&gt;&lt;td&gt;-47.164900&lt;/td&gt;&lt;td&gt;[STEL] L, Oi Móvel S.A. - Em Recuperação Judicial (50011385235, 691348138), Campinas/SP&lt;/td&gt;&lt;td&gt;053&lt;/td&gt;&lt;td&gt;691348138&lt;/td&gt;&lt;td&gt;G7W&lt;/td&gt;&lt;td&gt;28000.0&lt;/td&gt;&lt;td&gt;839757&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;216684&lt;/th&gt;&lt;td&gt;165.65000&lt;/td&gt;&lt;td&gt;-29.760278&lt;/td&gt;&lt;td&gt;-51.147222&lt;/td&gt;&lt;td&gt;[STEL] L, Empresa De Trens Urbanos De Porto Alegre S/A (03030055302, 47112), São Leopoldo/RS&lt;/td&gt;&lt;td&gt;019&lt;/td&gt;&lt;td&gt;47112&lt;/td&gt;&lt;td&gt;F3E&lt;/td&gt;&lt;td&gt;16.0&lt;/td&gt;&lt;td&gt;216705&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th&gt;313015&lt;/th&gt;&lt;td&gt;167.84375&lt;/td&gt;&lt;td&gt;-19.929639&lt;/td&gt;&lt;td&gt;-43.983850&lt;/td&gt;&lt;td&gt;[STEL] L, Policia Militar Do Estado De Minas Gerais (50401288943, 1002108397), Belo Horizonte/MG&lt;/td&gt;&lt;td&gt;019&lt;/td&gt;&lt;td&gt;1002108397&lt;/td&gt;&lt;td&gt;F1W&lt;/td&gt;&lt;td&gt;8.1&lt;/td&gt;&lt;td&gt;314660&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;footer&gt;&lt;div class=container-fluid&gt;&lt;div class=&quot;row center-block footer-text&quot;&gt;&lt;p class=&quot;text-muted text-center&quot;&gt;Report generated with &lt;a href=https://github.com/pandas-profiling/pandas-profiling&gt;pandas-profiling&lt;/a&gt;.&lt;/p&gt;&lt;/div&gt;&lt;/div&gt;&lt;/footer&gt;&lt;script&gt;
/*! jQuery v1.12.4 | (c) jQuery Foundation | jquery.org/license */
!function(a,b){&quot;object&quot;==typeof module&amp;&amp;&quot;object&quot;==typeof module.exports?module.exports=a.document?b(a,!0):function(a){if(!a.document)throw new Error(&quot;jQuery requires a window with a document&quot;);return b(a)}:b(a)}(&quot;undefined&quot;!=typeof window?window:this,function(a,b){var c=[],d=a.document,e=c.slice,f=c.concat,g=c.push,h=c.indexOf,i={},j=i.toString,k=i.hasOwnProperty,l={},m=&quot;1.12.4&quot;,n=function(a,b){return new n.fn.init(a,b)},o=/^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g,p=/^-ms-/,q=/-([\da-z])/gi,r=function(a,b){return b.toUpperCase()};n.fn=n.prototype={jquery:m,constructor:n,selector:&quot;&quot;,length:0,toArray:function(){return e.call(this)},get:function(a){return null!=a?0&gt;a?this[a+this.length]:this[a]:e.call(this)},pushStack:function(a){var b=n.merge(this.constructor(),a);return b.prevObject=this,b.context=this.context,b},each:function(a){return n.each(this,a)},map:function(a){return this.pushStack(n.map(this,function(b,c){return a.call(b,c,b)}))},slice:function(){return this.pushStack(e.apply(this,arguments))},first:function(){return this.eq(0)},last:function(){return this.eq(-1)},eq:function(a){var b=this.length,c=+a+(0&gt;a?b:0);return this.pushStack(c&gt;=0&amp;&amp;b&gt;c?[this[c]]:[])},end:function(){return this.prevObject||this.constructor()},push:g,sort:c.sort,splice:c.splice},n.extend=n.fn.extend=function(){var a,b,c,d,e,f,g=arguments[0]||{},h=1,i=arguments.length,j=!1;for(&quot;boolean&quot;==typeof g&amp;&amp;(j=g,g=arguments[h]||{},h++),&quot;object&quot;==typeof g||n.isFunction(g)||(g={}),h===i&amp;&amp;(g=this,h--);i&gt;h;h++)if(null!=(e=arguments[h]))for(d in e)a=g[d],c=e[d],g!==c&amp;&amp;(j&amp;&amp;c&amp;&amp;(n.isPlainObject(c)||(b=n.isArray(c)))?(b?(b=!1,f=a&amp;&amp;n.isArray(a)?a:[]):f=a&amp;&amp;n.isPlainObject(a)?a:{},g[d]=n.extend(j,f,c)):void 0!==c&amp;&amp;(g[d]=c));return g},n.extend({expando:&quot;jQuery&quot;+(m+Math.random()).replace(/\D/g,&quot;&quot;),isReady:!0,error:function(a){throw new Error(a)},noop:function(){},isFunction:function(a){return&quot;function&quot;===n.type(a)},isArray:Array.isArray||function(a){return&quot;array&quot;===n.type(a)},isWindow:function(a){return null!=a&amp;&amp;a==a.window},isNumeric:function(a){var b=a&amp;&amp;a.toString();return!n.isArray(a)&amp;&amp;b-parseFloat(b)+1&gt;=0},isEmptyObject:function(a){var b;for(b in a)return!1;return!0},isPlainObject:function(a){var b;if(!a||&quot;object&quot;!==n.type(a)||a.nodeType||n.isWindow(a))return!1;try{if(a.constructor&amp;&amp;!k.call(a,&quot;constructor&quot;)&amp;&amp;!k.call(a.constructor.prototype,&quot;isPrototypeOf&quot;))return!1}catch(c){return!1}if(!l.ownFirst)for(b in a)return k.call(a,b);for(b in a);return void 0===b||k.call(a,b)},type:function(a){return null==a?a+&quot;&quot;:&quot;object&quot;==typeof a||&quot;function&quot;==typeof a?i[j.call(a)]||&quot;object&quot;:typeof a},globalEval:function(b){b&amp;&amp;n.trim(b)&amp;&amp;(a.execScript||function(b){a.eval.call(a,b)})(b)},camelCase:function(a){return a.replace(p,&quot;ms-&quot;).replace(q,r)},nodeName:function(a,b){return a.nodeName&amp;&amp;a.nodeName.toLowerCase()===b.toLowerCase()},each:function(a,b){var c,d=0;if(s(a)){for(c=a.length;c&gt;d;d++)if(b.call(a[d],d,a[d])===!1)break}else for(d in a)if(b.call(a[d],d,a[d])===!1)break;return a},trim:function(a){return null==a?&quot;&quot;:(a+&quot;&quot;).replace(o,&quot;&quot;)},makeArray:function(a,b){var c=b||[];return null!=a&amp;&amp;(s(Object(a))?n.merge(c,&quot;string&quot;==typeof a?[a]:a):g.call(c,a)),c},inArray:function(a,b,c){var d;if(b){if(h)return h.call(b,a,c);for(d=b.length,c=c?0&gt;c?Math.max(0,d+c):c:0;d&gt;c;c++)if(c in b&amp;&amp;b[c]===a)return c}return-1},merge:function(a,b){var c=+b.length,d=0,e=a.length;while(c&gt;d)a[e++]=b[d++];if(c!==c)while(void 0!==b[d])a[e++]=b[d++];return a.length=e,a},grep:function(a,b,c){for(var d,e=[],f=0,g=a.length,h=!c;g&gt;f;f++)d=!b(a[f],f),d!==h&amp;&amp;e.push(a[f]);return e},map:function(a,b,c){var d,e,g=0,h=[];if(s(a))for(d=a.length;d&gt;g;g++)e=b(a[g],g,c),null!=e&amp;&amp;h.push(e);else for(g in a)e=b(a[g],g,c),null!=e&amp;&amp;h.push(e);return f.apply([],h)},guid:1,proxy:function(a,b){var c,d,f;return&quot;string&quot;==typeof b&amp;&amp;(f=a[b],b=a,a=f),n.isFunction(a)?(c=e.call(arguments,2),d=function(){return a.apply(b||this,c.concat(e.call(arguments)))},d.guid=a.guid=a.guid||n.guid++,d):void 0},now:function(){return+new Date},support:l}),&quot;function&quot;==typeof Symbol&amp;&amp;(n.fn[Symbol.iterator]=c[Symbol.iterator]),n.each(&quot;Boolean Number String Function Array Date RegExp Object Error Symbol&quot;.split(&quot; &quot;),function(a,b){i[&quot;[object &quot;+b+&quot;]&quot;]=b.toLowerCase()});function s(a){var b=!!a&amp;&amp;&quot;length&quot;in a&amp;&amp;a.length,c=n.type(a);return&quot;function&quot;===c||n.isWindow(a)?!1:&quot;array&quot;===c||0===b||&quot;number&quot;==typeof b&amp;&amp;b&gt;0&amp;&amp;b-1 in a}var t=function(a){var b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u=&quot;sizzle&quot;+1*new Date,v=a.document,w=0,x=0,y=ga(),z=ga(),A=ga(),B=function(a,b){return a===b&amp;&amp;(l=!0),0},C=1&lt;&lt;31,D={}.hasOwnProperty,E=[],F=E.pop,G=E.push,H=E.push,I=E.slice,J=function(a,b){for(var c=0,d=a.length;d&gt;c;c++)if(a[c]===b)return c;return-1},K=&quot;checked|selected|async|autofocus|autoplay|controls|defer|disabled|hidden|ismap|loop|multiple|open|readonly|required|scoped&quot;,L=&quot;[\\x20\\t\\r\\n\\f]&quot;,M=&quot;(?:\\\\.|[\\w-]|[^\\x00-\\xa0])+&quot;,N=&quot;\\[&quot;+L+&quot;*(&quot;+M+&quot;)(?:&quot;+L+&quot;*([*^$|!~]?=)&quot;+L+&quot;*(?:&#x27;((?:\\\\.|[^\\\\&#x27;])*)&#x27;|\&quot;((?:\\\\.|[^\\\\\&quot;])*)\&quot;|(&quot;+M+&quot;))|)&quot;+L+&quot;*\\]&quot;,O=&quot;:(&quot;+M+&quot;)(?:\\(((&#x27;((?:\\\\.|[^\\\\&#x27;])*)&#x27;|\&quot;((?:\\\\.|[^\\\\\&quot;])*)\&quot;)|((?:\\\\.|[^\\\\()[\\]]|&quot;+N+&quot;)*)|.*)\\)|)&quot;,P=new RegExp(L+&quot;+&quot;,&quot;g&quot;),Q=new RegExp(&quot;^&quot;+L+&quot;+|((?:^|[^\\\\])(?:\\\\.)*)&quot;+L+&quot;+$&quot;,&quot;g&quot;),R=new RegExp(&quot;^&quot;+L+&quot;*,&quot;+L+&quot;*&quot;),S=new RegExp(&quot;^&quot;+L+&quot;*([&gt;+~]|&quot;+L+&quot;)&quot;+L+&quot;*&quot;),T=new RegExp(&quot;=&quot;+L+&quot;*([^\\]&#x27;\&quot;]*?)&quot;+L+&quot;*\\]&quot;,&quot;g&quot;),U=new RegExp(O),V=new RegExp(&quot;^&quot;+M+&quot;$&quot;),W={ID:new RegExp(&quot;^#(&quot;+M+&quot;)&quot;),CLASS:new RegExp(&quot;^\\.(&quot;+M+&quot;)&quot;),TAG:new RegExp(&quot;^(&quot;+M+&quot;|[*])&quot;),ATTR:new RegExp(&quot;^&quot;+N),PSEUDO:new RegExp(&quot;^&quot;+O),CHILD:new RegExp(&quot;^:(only|first|last|nth|nth-last)-(child|of-type)(?:\\(&quot;+L+&quot;*(even|odd|(([+-]|)(\\d*)n|)&quot;+L+&quot;*(?:([+-]|)&quot;+L+&quot;*(\\d+)|))&quot;+L+&quot;*\\)|)&quot;,&quot;i&quot;),bool:new RegExp(&quot;^(?:&quot;+K+&quot;)$&quot;,&quot;i&quot;),needsContext:new RegExp(&quot;^&quot;+L+&quot;*[&gt;+~]|:(even|odd|eq|gt|lt|nth|first|last)(?:\\(&quot;+L+&quot;*((?:-\\d)?\\d*)&quot;+L+&quot;*\\)|)(?=[^-]|$)&quot;,&quot;i&quot;)},X=/^(?:input|select|textarea|button)$/i,Y=/^h\d$/i,Z=/^[^{]+\{\s*\[native \w/,$=/^(?:#([\w-]+)|(\w+)|\.([\w-]+))$/,_=/[+~]/,aa=/&#x27;|\\/g,ba=new RegExp(&quot;\\\\([\\da-f]{1,6}&quot;+L+&quot;?|(&quot;+L+&quot;)|.)&quot;,&quot;ig&quot;),ca=function(a,b,c){var d=&quot;0x&quot;+b-65536;return d!==d||c?b:0&gt;d?String.fromCharCode(d+65536):String.fromCharCode(d&gt;&gt;10|55296,1023&amp;d|56320)},da=function(){m()};try{H.apply(E=I.call(v.childNodes),v.childNodes),E[v.childNodes.length].nodeType}catch(ea){H={apply:E.length?function(a,b){G.apply(a,I.call(b))}:function(a,b){var c=a.length,d=0;while(a[c++]=b[d++]);a.length=c-1}}}function fa(a,b,d,e){var f,h,j,k,l,o,r,s,w=b&amp;&amp;b.ownerDocument,x=b?b.nodeType:9;if(d=d||[],&quot;string&quot;!=typeof a||!a||1!==x&amp;&amp;9!==x&amp;&amp;11!==x)return d;if(!e&amp;&amp;((b?b.ownerDocument||b:v)!==n&amp;&amp;m(b),b=b||n,p)){if(11!==x&amp;&amp;(o=$.exec(a)))if(f=o[1]){if(9===x){if(!(j=b.getElementById(f)))return d;if(j.id===f)return d.push(j),d}else if(w&amp;&amp;(j=w.getElementById(f))&amp;&amp;t(b,j)&amp;&amp;j.id===f)return d.push(j),d}else{if(o[2])return H.apply(d,b.getElementsByTagName(a)),d;if((f=o[3])&amp;&amp;c.getElementsByClassName&amp;&amp;b.getElementsByClassName)return H.apply(d,b.getElementsByClassName(f)),d}if(c.qsa&amp;&amp;!A[a+&quot; &quot;]&amp;&amp;(!q||!q.test(a))){if(1!==x)w=b,s=a;else if(&quot;object&quot;!==b.nodeName.toLowerCase()){(k=b.getAttribute(&quot;id&quot;))?k=k.replace(aa,&quot;\\$&amp;&quot;):b.setAttribute(&quot;id&quot;,k=u),r=g(a),h=r.length,l=V.test(k)?&quot;#&quot;+k:&quot;[id=&#x27;&quot;+k+&quot;&#x27;]&quot;;while(h--)r[h]=l+&quot; &quot;+qa(r[h]);s=r.join(&quot;,&quot;),w=_.test(a)&amp;&amp;oa(b.parentNode)||b}if(s)try{return H.apply(d,w.querySelectorAll(s)),d}catch(y){}finally{k===u&amp;&amp;b.removeAttribute(&quot;id&quot;)}}}return i(a.replace(Q,&quot;$1&quot;),b,d,e)}function ga(){var a=[];function b(c,e){return a.push(c+&quot; &quot;)&gt;d.cacheLength&amp;&amp;delete b[a.shift()],b[c+&quot; &quot;]=e}return b}function ha(a){return a[u]=!0,a}function ia(a){var b=n.createElement(&quot;div&quot;);try{return!!a(b)}catch(c){return!1}finally{b.parentNode&amp;&amp;b.parentNode.removeChild(b),b=null}}function ja(a,b){var c=a.split(&quot;|&quot;),e=c.length;while(e--)d.attrHandle[c[e]]=b}function ka(a,b){var c=b&amp;&amp;a,d=c&amp;&amp;1===a.nodeType&amp;&amp;1===b.nodeType&amp;&amp;(~b.sourceIndex||C)-(~a.sourceIndex||C);if(d)return d;if(c)while(c=c.nextSibling)if(c===b)return-1;return a?1:-1}function la(a){return function(b){var c=b.nodeName.toLowerCase();return&quot;input&quot;===c&amp;&amp;b.type===a}}function ma(a){return function(b){var c=b.nodeName.toLowerCase();return(&quot;input&quot;===c||&quot;button&quot;===c)&amp;&amp;b.type===a}}function na(a){return ha(function(b){return b=+b,ha(function(c,d){var e,f=a([],c.length,b),g=f.length;while(g--)c[e=f[g]]&amp;&amp;(c[e]=!(d[e]=c[e]))})})}function oa(a){return a&amp;&amp;&quot;undefined&quot;!=typeof a.getElementsByTagName&amp;&amp;a}c=fa.support={},f=fa.isXML=function(a){var b=a&amp;&amp;(a.ownerDocument||a).documentElement;return b?&quot;HTML&quot;!==b.nodeName:!1},m=fa.setDocument=function(a){var b,e,g=a?a.ownerDocument||a:v;return g!==n&amp;&amp;9===g.nodeType&amp;&amp;g.documentElement?(n=g,o=n.documentElement,p=!f(n),(e=n.defaultView)&amp;&amp;e.top!==e&amp;&amp;(e.addEventListener?e.addEventListener(&quot;unload&quot;,da,!1):e.attachEvent&amp;&amp;e.attachEvent(&quot;onunload&quot;,da)),c.attributes=ia(function(a){return a.className=&quot;i&quot;,!a.getAttribute(&quot;className&quot;)}),c.getElementsByTagName=ia(function(a){return a.appendChild(n.createComment(&quot;&quot;)),!a.getElementsByTagName(&quot;*&quot;).length}),c.getElementsByClassName=Z.test(n.getElementsByClassName),c.getById=ia(function(a){return o.appendChild(a).id=u,!n.getElementsByName||!n.getElementsByName(u).length}),c.getById?(d.find.ID=function(a,b){if(&quot;undefined&quot;!=typeof b.getElementById&amp;&amp;p){var c=b.getElementById(a);return c?[c]:[]}},d.filter.ID=function(a){var b=a.replace(ba,ca);return function(a){return a.getAttribute(&quot;id&quot;)===b}}):(delete d.find.ID,d.filter.ID=function(a){var b=a.replace(ba,ca);return function(a){var c=&quot;undefined&quot;!=typeof a.getAttributeNode&amp;&amp;a.getAttributeNode(&quot;id&quot;);return c&amp;&amp;c.value===b}}),d.find.TAG=c.getElementsByTagName?function(a,b){return&quot;undefined&quot;!=typeof b.getElementsByTagName?b.getElementsByTagName(a):c.qsa?b.querySelectorAll(a):void 0}:function(a,b){var c,d=[],e=0,f=b.getElementsByTagName(a);if(&quot;*&quot;===a){while(c=f[e++])1===c.nodeType&amp;&amp;d.push(c);return d}return f},d.find.CLASS=c.getElementsByClassName&amp;&amp;function(a,b){return&quot;undefined&quot;!=typeof b.getElementsByClassName&amp;&amp;p?b.getElementsByClassName(a):void 0},r=[],q=[],(c.qsa=Z.test(n.querySelectorAll))&amp;&amp;(ia(function(a){o.appendChild(a).innerHTML=&quot;&lt;a id=&#x27;&quot;+u+&quot;&#x27;&gt;&lt;/a&gt;&lt;select id=&#x27;&quot;+u+&quot;-\r\\&#x27; msallowcapture=&#x27;&#x27;&gt;&lt;option selected=&#x27;&#x27;&gt;&lt;/option&gt;&lt;/select&gt;&quot;,a.querySelectorAll(&quot;[msallowcapture^=&#x27;&#x27;]&quot;).length&amp;&amp;q.push(&quot;[*^$]=&quot;+L+&quot;*(?:&#x27;&#x27;|\&quot;\&quot;)&quot;),a.querySelectorAll(&quot;[selected]&quot;).length||q.push(&quot;\\[&quot;+L+&quot;*(?:value|&quot;+K+&quot;)&quot;),a.querySelectorAll(&quot;[id~=&quot;+u+&quot;-]&quot;).length||q.push(&quot;~=&quot;),a.querySelectorAll(&quot;:checked&quot;).length||q.push(&quot;:checked&quot;),a.querySelectorAll(&quot;a#&quot;+u+&quot;+*&quot;).length||q.push(&quot;.#.+[+~]&quot;)}),ia(function(a){var b=n.createElement(&quot;input&quot;);b.setAttribute(&quot;type&quot;,&quot;hidden&quot;),a.appendChild(b).setAttribute(&quot;name&quot;,&quot;D&quot;),a.querySelectorAll(&quot;[name=d]&quot;).length&amp;&amp;q.push(&quot;name&quot;+L+&quot;*[*^$|!~]?=&quot;),a.querySelectorAll(&quot;:enabled&quot;).length||q.push(&quot;:enabled&quot;,&quot;:disabled&quot;),a.querySelectorAll(&quot;*,:x&quot;),q.push(&quot;,.*:&quot;)})),(c.matchesSelector=Z.test(s=o.matches||o.webkitMatchesSelector||o.mozMatchesSelector||o.oMatchesSelector||o.msMatchesSelector))&amp;&amp;ia(function(a){c.disconnectedMatch=s.call(a,&quot;div&quot;),s.call(a,&quot;[s!=&#x27;&#x27;]:x&quot;),r.push(&quot;!=&quot;,O)}),q=q.length&amp;&amp;new RegExp(q.join(&quot;|&quot;)),r=r.length&amp;&amp;new RegExp(r.join(&quot;|&quot;)),b=Z.test(o.compareDocumentPosition),t=b||Z.test(o.contains)?function(a,b){var c=9===a.nodeType?a.documentElement:a,d=b&amp;&amp;b.parentNode;return a===d||!(!d||1!==d.nodeType||!(c.contains?c.contains(d):a.compareDocumentPosition&amp;&amp;16&amp;a.compareDocumentPosition(d)))}:function(a,b){if(b)while(b=b.parentNode)if(b===a)return!0;return!1},B=b?function(a,b){if(a===b)return l=!0,0;var d=!a.compareDocumentPosition-!b.compareDocumentPosition;return d?d:(d=(a.ownerDocument||a)===(b.ownerDocument||b)?a.compareDocumentPosition(b):1,1&amp;d||!c.sortDetached&amp;&amp;b.compareDocumentPosition(a)===d?a===n||a.ownerDocument===v&amp;&amp;t(v,a)?-1:b===n||b.ownerDocument===v&amp;&amp;t(v,b)?1:k?J(k,a)-J(k,b):0:4&amp;d?-1:1)}:function(a,b){if(a===b)return l=!0,0;var c,d=0,e=a.parentNode,f=b.parentNode,g=[a],h=[b];if(!e||!f)return a===n?-1:b===n?1:e?-1:f?1:k?J(k,a)-J(k,b):0;if(e===f)return ka(a,b);c=a;while(c=c.parentNode)g.unshift(c);c=b;while(c=c.parentNode)h.unshift(c);while(g[d]===h[d])d++;return d?ka(g[d],h[d]):g[d]===v?-1:h[d]===v?1:0},n):n},fa.matches=function(a,b){return fa(a,null,null,b)},fa.matchesSelector=function(a,b){if((a.ownerDocument||a)!==n&amp;&amp;m(a),b=b.replace(T,&quot;=&#x27;$1&#x27;]&quot;),c.matchesSelector&amp;&amp;p&amp;&amp;!A[b+&quot; &quot;]&amp;&amp;(!r||!r.test(b))&amp;&amp;(!q||!q.test(b)))try{var d=s.call(a,b);if(d||c.disconnectedMatch||a.document&amp;&amp;11!==a.document.nodeType)return d}catch(e){}return fa(b,n,null,[a]).length&gt;0},fa.contains=function(a,b){return(a.ownerDocument||a)!==n&amp;&amp;m(a),t(a,b)},fa.attr=function(a,b){(a.ownerDocument||a)!==n&amp;&amp;m(a);var e=d.attrHandle[b.toLowerCase()],f=e&amp;&amp;D.call(d.attrHandle,b.toLowerCase())?e(a,b,!p):void 0;return void 0!==f?f:c.attributes||!p?a.getAttribute(b):(f=a.getAttributeNode(b))&amp;&amp;f.specified?f.value:null},fa.error=function(a){throw new Error(&quot;Syntax error, unrecognized expression: &quot;+a)},fa.uniqueSort=function(a){var b,d=[],e=0,f=0;if(l=!c.detectDuplicates,k=!c.sortStable&amp;&amp;a.slice(0),a.sort(B),l){while(b=a[f++])b===a[f]&amp;&amp;(e=d.push(f));while(e--)a.splice(d[e],1)}return k=null,a},e=fa.getText=function(a){var b,c=&quot;&quot;,d=0,f=a.nodeType;if(f){if(1===f||9===f||11===f){if(&quot;string&quot;==typeof a.textContent)return a.textContent;for(a=a.firstChild;a;a=a.nextSibling)c+=e(a)}else if(3===f||4===f)return a.nodeValue}else while(b=a[d++])c+=e(b);return c},d=fa.selectors={cacheLength:50,createPseudo:ha,match:W,attrHandle:{},find:{},relative:{&quot;&gt;&quot;:{dir:&quot;parentNode&quot;,first:!0},&quot; &quot;:{dir:&quot;parentNode&quot;},&quot;+&quot;:{dir:&quot;previousSibling&quot;,first:!0},&quot;~&quot;:{dir:&quot;previousSibling&quot;}},preFilter:{ATTR:function(a){return a[1]=a[1].replace(ba,ca),a[3]=(a[3]||a[4]||a[5]||&quot;&quot;).replace(ba,ca),&quot;~=&quot;===a[2]&amp;&amp;(a[3]=&quot; &quot;+a[3]+&quot; &quot;),a.slice(0,4)},CHILD:function(a){return a[1]=a[1].toLowerCase(),&quot;nth&quot;===a[1].slice(0,3)?(a[3]||fa.error(a[0]),a[4]=+(a[4]?a[5]+(a[6]||1):2*(&quot;even&quot;===a[3]||&quot;odd&quot;===a[3])),a[5]=+(a[7]+a[8]||&quot;odd&quot;===a[3])):a[3]&amp;&amp;fa.error(a[0]),a},PSEUDO:function(a){var b,c=!a[6]&amp;&amp;a[2];return W.CHILD.test(a[0])?null:(a[3]?a[2]=a[4]||a[5]||&quot;&quot;:c&amp;&amp;U.test(c)&amp;&amp;(b=g(c,!0))&amp;&amp;(b=c.indexOf(&quot;)&quot;,c.length-b)-c.length)&amp;&amp;(a[0]=a[0].slice(0,b),a[2]=c.slice(0,b)),a.slice(0,3))}},filter:{TAG:function(a){var b=a.replace(ba,ca).toLowerCase();return&quot;*&quot;===a?function(){return!0}:function(a){return a.nodeName&amp;&amp;a.nodeName.toLowerCase()===b}},CLASS:function(a){var b=y[a+&quot; &quot;];return b||(b=new RegExp(&quot;(^|&quot;+L+&quot;)&quot;+a+&quot;(&quot;+L+&quot;|$)&quot;))&amp;&amp;y(a,function(a){return b.test(&quot;string&quot;==typeof a.className&amp;&amp;a.className||&quot;undefined&quot;!=typeof a.getAttribute&amp;&amp;a.getAttribute(&quot;class&quot;)||&quot;&quot;)})},ATTR:function(a,b,c){return function(d){var e=fa.attr(d,a);return null==e?&quot;!=&quot;===b:b?(e+=&quot;&quot;,&quot;=&quot;===b?e===c:&quot;!=&quot;===b?e!==c:&quot;^=&quot;===b?c&amp;&amp;0===e.indexOf(c):&quot;*=&quot;===b?c&amp;&amp;e.indexOf(c)&gt;-1:&quot;$=&quot;===b?c&amp;&amp;e.slice(-c.length)===c:&quot;~=&quot;===b?(&quot; &quot;+e.replace(P,&quot; &quot;)+&quot; &quot;).indexOf(c)&gt;-1:&quot;|=&quot;===b?e===c||e.slice(0,c.length+1)===c+&quot;-&quot;:!1):!0}},CHILD:function(a,b,c,d,e){var f=&quot;nth&quot;!==a.slice(0,3),g=&quot;last&quot;!==a.slice(-4),h=&quot;of-type&quot;===b;return 1===d&amp;&amp;0===e?function(a){return!!a.parentNode}:function(b,c,i){var j,k,l,m,n,o,p=f!==g?&quot;nextSibling&quot;:&quot;previousSibling&quot;,q=b.parentNode,r=h&amp;&amp;b.nodeName.toLowerCase(),s=!i&amp;&amp;!h,t=!1;if(q){if(f){while(p){m=b;while(m=m[p])if(h?m.nodeName.toLowerCase()===r:1===m.nodeType)return!1;o=p=&quot;only&quot;===a&amp;&amp;!o&amp;&amp;&quot;nextSibling&quot;}return!0}if(o=[g?q.firstChild:q.lastChild],g&amp;&amp;s){m=q,l=m[u]||(m[u]={}),k=l[m.uniqueID]||(l[m.uniqueID]={}),j=k[a]||[],n=j[0]===w&amp;&amp;j[1],t=n&amp;&amp;j[2],m=n&amp;&amp;q.childNodes[n];while(m=++n&amp;&amp;m&amp;&amp;m[p]||(t=n=0)||o.pop())if(1===m.nodeType&amp;&amp;++t&amp;&amp;m===b){k[a]=[w,n,t];break}}else if(s&amp;&amp;(m=b,l=m[u]||(m[u]={}),k=l[m.uniqueID]||(l[m.uniqueID]={}),j=k[a]||[],n=j[0]===w&amp;&amp;j[1],t=n),t===!1)while(m=++n&amp;&amp;m&amp;&amp;m[p]||(t=n=0)||o.pop())if((h?m.nodeName.toLowerCase()===r:1===m.nodeType)&amp;&amp;++t&amp;&amp;(s&amp;&amp;(l=m[u]||(m[u]={}),k=l[m.uniqueID]||(l[m.uniqueID]={}),k[a]=[w,t]),m===b))break;return t-=e,t===d||t%d===0&amp;&amp;t/d&gt;=0}}},PSEUDO:function(a,b){var c,e=d.pseudos[a]||d.setFilters[a.toLowerCase()]||fa.error(&quot;unsupported pseudo: &quot;+a);return e[u]?e(b):e.length&gt;1?(c=[a,a,&quot;&quot;,b],d.setFilters.hasOwnProperty(a.toLowerCase())?ha(function(a,c){var d,f=e(a,b),g=f.length;while(g--)d=J(a,f[g]),a[d]=!(c[d]=f[g])}):function(a){return e(a,0,c)}):e}},pseudos:{not:ha(function(a){var b=[],c=[],d=h(a.replace(Q,&quot;$1&quot;));return d[u]?ha(function(a,b,c,e){var f,g=d(a,null,e,[]),h=a.length;while(h--)(f=g[h])&amp;&amp;(a[h]=!(b[h]=f))}):function(a,e,f){return b[0]=a,d(b,null,f,c),b[0]=null,!c.pop()}}),has:ha(function(a){return function(b){return fa(a,b).length&gt;0}}),contains:ha(function(a){return a=a.replace(ba,ca),function(b){return(b.textContent||b.innerText||e(b)).indexOf(a)&gt;-1}}),lang:ha(function(a){return V.test(a||&quot;&quot;)||fa.error(&quot;unsupported lang: &quot;+a),a=a.replace(ba,ca).toLowerCase(),function(b){var c;do if(c=p?b.lang:b.getAttribute(&quot;xml:lang&quot;)||b.getAttribute(&quot;lang&quot;))return c=c.toLowerCase(),c===a||0===c.indexOf(a+&quot;-&quot;);while((b=b.parentNode)&amp;&amp;1===b.nodeType);return!1}}),target:function(b){var c=a.location&amp;&amp;a.location.hash;return c&amp;&amp;c.slice(1)===b.id},root:function(a){return a===o},focus:function(a){return a===n.activeElement&amp;&amp;(!n.hasFocus||n.hasFocus())&amp;&amp;!!(a.type||a.href||~a.tabIndex)},enabled:function(a){return a.disabled===!1},disabled:function(a){return a.disabled===!0},checked:function(a){var b=a.nodeName.toLowerCase();return&quot;input&quot;===b&amp;&amp;!!a.checked||&quot;option&quot;===b&amp;&amp;!!a.selected},selected:function(a){return a.parentNode&amp;&amp;a.parentNode.selectedIndex,a.selected===!0},empty:function(a){for(a=a.firstChild;a;a=a.nextSibling)if(a.nodeType&lt;6)return!1;return!0},parent:function(a){return!d.pseudos.empty(a)},header:function(a){return Y.test(a.nodeName)},input:function(a){return X.test(a.nodeName)},button:function(a){var b=a.nodeName.toLowerCase();return&quot;input&quot;===b&amp;&amp;&quot;button&quot;===a.type||&quot;button&quot;===b},text:function(a){var b;return&quot;input&quot;===a.nodeName.toLowerCase()&amp;&amp;&quot;text&quot;===a.type&amp;&amp;(null==(b=a.getAttribute(&quot;type&quot;))||&quot;text&quot;===b.toLowerCase())},first:na(function(){return[0]}),last:na(function(a,b){return[b-1]}),eq:na(function(a,b,c){return[0&gt;c?c+b:c]}),even:na(function(a,b){for(var c=0;b&gt;c;c+=2)a.push(c);return a}),odd:na(function(a,b){for(var c=1;b&gt;c;c+=2)a.push(c);return a}),lt:na(function(a,b,c){for(var d=0&gt;c?c+b:c;--d&gt;=0;)a.push(d);return a}),gt:na(function(a,b,c){for(var d=0&gt;c?c+b:c;++d&lt;b;)a.push(d);return a})}},d.pseudos.nth=d.pseudos.eq;for(b in{radio:!0,checkbox:!0,file:!0,password:!0,image:!0})d.pseudos[b]=la(b);for(b in{submit:!0,reset:!0})d.pseudos[b]=ma(b);function pa(){}pa.prototype=d.filters=d.pseudos,d.setFilters=new pa,g=fa.tokenize=function(a,b){var c,e,f,g,h,i,j,k=z[a+&quot; &quot;];if(k)return b?0:k.slice(0);h=a,i=[],j=d.preFilter;while(h){c&amp;&amp;!(e=R.exec(h))||(e&amp;&amp;(h=h.slice(e[0].length)||h),i.push(f=[])),c=!1,(e=S.exec(h))&amp;&amp;(c=e.shift(),f.push({value:c,type:e[0].replace(Q,&quot; &quot;)}),h=h.slice(c.length));for(g in d.filter)!(e=W[g].exec(h))||j[g]&amp;&amp;!(e=j[g](e))||(c=e.shift(),f.push({value:c,type:g,matches:e}),h=h.slice(c.length));if(!c)break}return b?h.length:h?fa.error(a):z(a,i).slice(0)};function qa(a){for(var b=0,c=a.length,d=&quot;&quot;;c&gt;b;b++)d+=a[b].value;return d}function ra(a,b,c){var d=b.dir,e=c&amp;&amp;&quot;parentNode&quot;===d,f=x++;return b.first?function(b,c,f){while(b=b[d])if(1===b.nodeType||e)return a(b,c,f)}:function(b,c,g){var h,i,j,k=[w,f];if(g){while(b=b[d])if((1===b.nodeType||e)&amp;&amp;a(b,c,g))return!0}else while(b=b[d])if(1===b.nodeType||e){if(j=b[u]||(b[u]={}),i=j[b.uniqueID]||(j[b.uniqueID]={}),(h=i[d])&amp;&amp;h[0]===w&amp;&amp;h[1]===f)return k[2]=h[2];if(i[d]=k,k[2]=a(b,c,g))return!0}}}function sa(a){return a.length&gt;1?function(b,c,d){var e=a.length;while(e--)if(!a[e](b,c,d))return!1;return!0}:a[0]}function ta(a,b,c){for(var d=0,e=b.length;e&gt;d;d++)fa(a,b[d],c);return c}function ua(a,b,c,d,e){for(var f,g=[],h=0,i=a.length,j=null!=b;i&gt;h;h++)(f=a[h])&amp;&amp;(c&amp;&amp;!c(f,d,e)||(g.push(f),j&amp;&amp;b.push(h)));return g}function va(a,b,c,d,e,f){return d&amp;&amp;!d[u]&amp;&amp;(d=va(d)),e&amp;&amp;!e[u]&amp;&amp;(e=va(e,f)),ha(function(f,g,h,i){var j,k,l,m=[],n=[],o=g.length,p=f||ta(b||&quot;*&quot;,h.nodeType?[h]:h,[]),q=!a||!f&amp;&amp;b?p:ua(p,m,a,h,i),r=c?e||(f?a:o||d)?[]:g:q;if(c&amp;&amp;c(q,r,h,i),d){j=ua(r,n),d(j,[],h,i),k=j.length;while(k--)(l=j[k])&amp;&amp;(r[n[k]]=!(q[n[k]]=l))}if(f){if(e||a){if(e){j=[],k=r.length;while(k--)(l=r[k])&amp;&amp;j.push(q[k]=l);e(null,r=[],j,i)}k=r.length;while(k--)(l=r[k])&amp;&amp;(j=e?J(f,l):m[k])&gt;-1&amp;&amp;(f[j]=!(g[j]=l))}}else r=ua(r===g?r.splice(o,r.length):r),e?e(null,g,r,i):H.apply(g,r)})}function wa(a){for(var b,c,e,f=a.length,g=d.relative[a[0].type],h=g||d.relative[&quot; &quot;],i=g?1:0,k=ra(function(a){return a===b},h,!0),l=ra(function(a){return J(b,a)&gt;-1},h,!0),m=[function(a,c,d){var e=!g&amp;&amp;(d||c!==j)||((b=c).nodeType?k(a,c,d):l(a,c,d));return b=null,e}];f&gt;i;i++)if(c=d.relative[a[i].type])m=[ra(sa(m),c)];else{if(c=d.filter[a[i].type].apply(null,a[i].matches),c[u]){for(e=++i;f&gt;e;e++)if(d.relative[a[e].type])break;return va(i&gt;1&amp;&amp;sa(m),i&gt;1&amp;&amp;qa(a.slice(0,i-1).concat({value:&quot; &quot;===a[i-2].type?&quot;*&quot;:&quot;&quot;})).replace(Q,&quot;$1&quot;),c,e&gt;i&amp;&amp;wa(a.slice(i,e)),f&gt;e&amp;&amp;wa(a=a.slice(e)),f&gt;e&amp;&amp;qa(a))}m.push(c)}return sa(m)}function xa(a,b){var c=b.length&gt;0,e=a.length&gt;0,f=function(f,g,h,i,k){var l,o,q,r=0,s=&quot;0&quot;,t=f&amp;&amp;[],u=[],v=j,x=f||e&amp;&amp;d.find.TAG(&quot;*&quot;,k),y=w+=null==v?1:Math.random()||.1,z=x.length;for(k&amp;&amp;(j=g===n||g||k);s!==z&amp;&amp;null!=(l=x[s]);s++){if(e&amp;&amp;l){o=0,g||l.ownerDocument===n||(m(l),h=!p);while(q=a[o++])if(q(l,g||n,h)){i.push(l);break}k&amp;&amp;(w=y)}c&amp;&amp;((l=!q&amp;&amp;l)&amp;&amp;r--,f&amp;&amp;t.push(l))}if(r+=s,c&amp;&amp;s!==r){o=0;while(q=b[o++])q(t,u,g,h);if(f){if(r&gt;0)while(s--)t[s]||u[s]||(u[s]=F.call(i));u=ua(u)}H.apply(i,u),k&amp;&amp;!f&amp;&amp;u.length&gt;0&amp;&amp;r+b.length&gt;1&amp;&amp;fa.uniqueSort(i)}return k&amp;&amp;(w=y,j=v),t};return c?ha(f):f}return h=fa.compile=function(a,b){var c,d=[],e=[],f=A[a+&quot; &quot;];if(!f){b||(b=g(a)),c=b.length;while(c--)f=wa(b[c]),f[u]?d.push(f):e.push(f);f=A(a,xa(e,d)),f.selector=a}return f},i=fa.select=function(a,b,e,f){var i,j,k,l,m,n=&quot;function&quot;==typeof a&amp;&amp;a,o=!f&amp;&amp;g(a=n.selector||a);if(e=e||[],1===o.length){if(j=o[0]=o[0].slice(0),j.length&gt;2&amp;&amp;&quot;ID&quot;===(k=j[0]).type&amp;&amp;c.getById&amp;&amp;9===b.nodeType&amp;&amp;p&amp;&amp;d.relative[j[1].type]){if(b=(d.find.ID(k.matches[0].replace(ba,ca),b)||[])[0],!b)return e;n&amp;&amp;(b=b.parentNode),a=a.slice(j.shift().value.length)}i=W.needsContext.test(a)?0:j.length;while(i--){if(k=j[i],d.relative[l=k.type])break;if((m=d.find[l])&amp;&amp;(f=m(k.matches[0].replace(ba,ca),_.test(j[0].type)&amp;&amp;oa(b.parentNode)||b))){if(j.splice(i,1),a=f.length&amp;&amp;qa(j),!a)return H.apply(e,f),e;break}}}return(n||h(a,o))(f,b,!p,e,!b||_.test(a)&amp;&amp;oa(b.parentNode)||b),e},c.sortStable=u.split(&quot;&quot;).sort(B).join(&quot;&quot;)===u,c.detectDuplicates=!!l,m(),c.sortDetached=ia(function(a){return 1&amp;a.compareDocumentPosition(n.createElement(&quot;div&quot;))}),ia(function(a){return a.innerHTML=&quot;&lt;a href=&#x27;#&#x27;&gt;&lt;/a&gt;&quot;,&quot;#&quot;===a.firstChild.getAttribute(&quot;href&quot;)})||ja(&quot;type|href|height|width&quot;,function(a,b,c){return c?void 0:a.getAttribute(b,&quot;type&quot;===b.toLowerCase()?1:2)}),c.attributes&amp;&amp;ia(function(a){return a.innerHTML=&quot;&lt;input/&gt;&quot;,a.firstChild.setAttribute(&quot;value&quot;,&quot;&quot;),&quot;&quot;===a.firstChild.getAttribute(&quot;value&quot;)})||ja(&quot;value&quot;,function(a,b,c){return c||&quot;input&quot;!==a.nodeName.toLowerCase()?void 0:a.defaultValue}),ia(function(a){return null==a.getAttribute(&quot;disabled&quot;)})||ja(K,function(a,b,c){var d;return c?void 0:a[b]===!0?b.toLowerCase():(d=a.getAttributeNode(b))&amp;&amp;d.specified?d.value:null}),fa}(a);n.find=t,n.expr=t.selectors,n.expr[&quot;:&quot;]=n.expr.pseudos,n.uniqueSort=n.unique=t.uniqueSort,n.text=t.getText,n.isXMLDoc=t.isXML,n.contains=t.contains;var u=function(a,b,c){var d=[],e=void 0!==c;while((a=a[b])&amp;&amp;9!==a.nodeType)if(1===a.nodeType){if(e&amp;&amp;n(a).is(c))break;d.push(a)}return d},v=function(a,b){for(var c=[];a;a=a.nextSibling)1===a.nodeType&amp;&amp;a!==b&amp;&amp;c.push(a);return c},w=n.expr.match.needsContext,x=/^&lt;([\w-]+)\s*\/?&gt;(?:&lt;\/\1&gt;|)$/,y=/^.[^:#\[\.,]*$/;function z(a,b,c){if(n.isFunction(b))return n.grep(a,function(a,d){return!!b.call(a,d,a)!==c});if(b.nodeType)return n.grep(a,function(a){return a===b!==c});if(&quot;string&quot;==typeof b){if(y.test(b))return n.filter(b,a,c);b=n.filter(b,a)}return n.grep(a,function(a){return n.inArray(a,b)&gt;-1!==c})}n.filter=function(a,b,c){var d=b[0];return c&amp;&amp;(a=&quot;:not(&quot;+a+&quot;)&quot;),1===b.length&amp;&amp;1===d.nodeType?n.find.matchesSelector(d,a)?[d]:[]:n.find.matches(a,n.grep(b,function(a){return 1===a.nodeType}))},n.fn.extend({find:function(a){var b,c=[],d=this,e=d.length;if(&quot;string&quot;!=typeof a)return this.pushStack(n(a).filter(function(){for(b=0;e&gt;b;b++)if(n.contains(d[b],this))return!0}));for(b=0;e&gt;b;b++)n.find(a,d[b],c);return c=this.pushStack(e&gt;1?n.unique(c):c),c.selector=this.selector?this.selector+&quot; &quot;+a:a,c},filter:function(a){return this.pushStack(z(this,a||[],!1))},not:function(a){return this.pushStack(z(this,a||[],!0))},is:function(a){return!!z(this,&quot;string&quot;==typeof a&amp;&amp;w.test(a)?n(a):a||[],!1).length}});var A,B=/^(?:\s*(&lt;[\w\W]+&gt;)[^&gt;]*|#([\w-]*))$/,C=n.fn.init=function(a,b,c){var e,f;if(!a)return this;if(c=c||A,&quot;string&quot;==typeof a){if(e=&quot;&lt;&quot;===a.charAt(0)&amp;&amp;&quot;&gt;&quot;===a.charAt(a.length-1)&amp;&amp;a.length&gt;=3?[null,a,null]:B.exec(a),!e||!e[1]&amp;&amp;b)return!b||b.jquery?(b||c).find(a):this.constructor(b).find(a);if(e[1]){if(b=b instanceof n?b[0]:b,n.merge(this,n.parseHTML(e[1],b&amp;&amp;b.nodeType?b.ownerDocument||b:d,!0)),x.test(e[1])&amp;&amp;n.isPlainObject(b))for(e in b)n.isFunction(this[e])?this[e](b[e]):this.attr(e,b[e]);return this}if(f=d.getElementById(e[2]),f&amp;&amp;f.parentNode){if(f.id!==e[2])return A.find(a);this.length=1,this[0]=f}return this.context=d,this.selector=a,this}return a.nodeType?(this.context=this[0]=a,this.length=1,this):n.isFunction(a)?&quot;undefined&quot;!=typeof c.ready?c.ready(a):a(n):(void 0!==a.selector&amp;&amp;(this.selector=a.selector,this.context=a.context),n.makeArray(a,this))};C.prototype=n.fn,A=n(d);var D=/^(?:parents|prev(?:Until|All))/,E={children:!0,contents:!0,next:!0,prev:!0};n.fn.extend({has:function(a){var b,c=n(a,this),d=c.length;return this.filter(function(){for(b=0;d&gt;b;b++)if(n.contains(this,c[b]))return!0})},closest:function(a,b){for(var c,d=0,e=this.length,f=[],g=w.test(a)||&quot;string&quot;!=typeof a?n(a,b||this.context):0;e&gt;d;d++)for(c=this[d];c&amp;&amp;c!==b;c=c.parentNode)if(c.nodeType&lt;11&amp;&amp;(g?g.index(c)&gt;-1:1===c.nodeType&amp;&amp;n.find.matchesSelector(c,a))){f.push(c);break}return this.pushStack(f.length&gt;1?n.uniqueSort(f):f)},index:function(a){return a?&quot;string&quot;==typeof a?n.inArray(this[0],n(a)):n.inArray(a.jquery?a[0]:a,this):this[0]&amp;&amp;this[0].parentNode?this.first().prevAll().length:-1},add:function(a,b){return this.pushStack(n.uniqueSort(n.merge(this.get(),n(a,b))))},addBack:function(a){return this.add(null==a?this.prevObject:this.prevObject.filter(a))}});function F(a,b){do a=a[b];while(a&amp;&amp;1!==a.nodeType);return a}n.each({parent:function(a){var b=a.parentNode;return b&amp;&amp;11!==b.nodeType?b:null},parents:function(a){return u(a,&quot;parentNode&quot;)},parentsUntil:function(a,b,c){return u(a,&quot;parentNode&quot;,c)},next:function(a){return F(a,&quot;nextSibling&quot;)},prev:function(a){return F(a,&quot;previousSibling&quot;)},nextAll:function(a){return u(a,&quot;nextSibling&quot;)},prevAll:function(a){return u(a,&quot;previousSibling&quot;)},nextUntil:function(a,b,c){return u(a,&quot;nextSibling&quot;,c)},prevUntil:function(a,b,c){return u(a,&quot;previousSibling&quot;,c)},siblings:function(a){return v((a.parentNode||{}).firstChild,a)},children:function(a){return v(a.firstChild)},contents:function(a){return n.nodeName(a,&quot;iframe&quot;)?a.contentDocument||a.contentWindow.document:n.merge([],a.childNodes)}},function(a,b){n.fn[a]=function(c,d){var e=n.map(this,b,c);return&quot;Until&quot;!==a.slice(-5)&amp;&amp;(d=c),d&amp;&amp;&quot;string&quot;==typeof d&amp;&amp;(e=n.filter(d,e)),this.length&gt;1&amp;&amp;(E[a]||(e=n.uniqueSort(e)),D.test(a)&amp;&amp;(e=e.reverse())),this.pushStack(e)}});var G=/\S+/g;function H(a){var b={};return n.each(a.match(G)||[],function(a,c){b[c]=!0}),b}n.Callbacks=function(a){a=&quot;string&quot;==typeof a?H(a):n.extend({},a);var b,c,d,e,f=[],g=[],h=-1,i=function(){for(e=a.once,d=b=!0;g.length;h=-1){c=g.shift();while(++h&lt;f.length)f[h].apply(c[0],c[1])===!1&amp;&amp;a.stopOnFalse&amp;&amp;(h=f.length,c=!1)}a.memory||(c=!1),b=!1,e&amp;&amp;(f=c?[]:&quot;&quot;)},j={add:function(){return f&amp;&amp;(c&amp;&amp;!b&amp;&amp;(h=f.length-1,g.push(c)),function d(b){n.each(b,function(b,c){n.isFunction(c)?a.unique&amp;&amp;j.has(c)||f.push(c):c&amp;&amp;c.length&amp;&amp;&quot;string&quot;!==n.type(c)&amp;&amp;d(c)})}(arguments),c&amp;&amp;!b&amp;&amp;i()),this},remove:function(){return n.each(arguments,function(a,b){var c;while((c=n.inArray(b,f,c))&gt;-1)f.splice(c,1),h&gt;=c&amp;&amp;h--}),this},has:function(a){return a?n.inArray(a,f)&gt;-1:f.length&gt;0},empty:function(){return f&amp;&amp;(f=[]),this},disable:function(){return e=g=[],f=c=&quot;&quot;,this},disabled:function(){return!f},lock:function(){return e=!0,c||j.disable(),this},locked:function(){return!!e},fireWith:function(a,c){return e||(c=c||[],c=[a,c.slice?c.slice():c],g.push(c),b||i()),this},fire:function(){return j.fireWith(this,arguments),this},fired:function(){return!!d}};return j},n.extend({Deferred:function(a){var b=[[&quot;resolve&quot;,&quot;done&quot;,n.Callbacks(&quot;once memory&quot;),&quot;resolved&quot;],[&quot;reject&quot;,&quot;fail&quot;,n.Callbacks(&quot;once memory&quot;),&quot;rejected&quot;],[&quot;notify&quot;,&quot;progress&quot;,n.Callbacks(&quot;memory&quot;)]],c=&quot;pending&quot;,d={state:function(){return c},always:function(){return e.done(arguments).fail(arguments),this},then:function(){var a=arguments;return n.Deferred(function(c){n.each(b,function(b,f){var g=n.isFunction(a[b])&amp;&amp;a[b];e[f[1]](function(){var a=g&amp;&amp;g.apply(this,arguments);a&amp;&amp;n.isFunction(a.promise)?a.promise().progress(c.notify).done(c.resolve).fail(c.reject):c[f[0]+&quot;With&quot;](this===d?c.promise():this,g?[a]:arguments)})}),a=null}).promise()},promise:function(a){return null!=a?n.extend(a,d):d}},e={};return d.pipe=d.then,n.each(b,function(a,f){var g=f[2],h=f[3];d[f[1]]=g.add,h&amp;&amp;g.add(function(){c=h},b[1^a][2].disable,b[2][2].lock),e[f[0]]=function(){return e[f[0]+&quot;With&quot;](this===e?d:this,arguments),this},e[f[0]+&quot;With&quot;]=g.fireWith}),d.promise(e),a&amp;&amp;a.call(e,e),e},when:function(a){var b=0,c=e.call(arguments),d=c.length,f=1!==d||a&amp;&amp;n.isFunction(a.promise)?d:0,g=1===f?a:n.Deferred(),h=function(a,b,c){return function(d){b[a]=this,c[a]=arguments.length&gt;1?e.call(arguments):d,c===i?g.notifyWith(b,c):--f||g.resolveWith(b,c)}},i,j,k;if(d&gt;1)for(i=new Array(d),j=new Array(d),k=new Array(d);d&gt;b;b++)c[b]&amp;&amp;n.isFunction(c[b].promise)?c[b].promise().progress(h(b,j,i)).done(h(b,k,c)).fail(g.reject):--f;return f||g.resolveWith(k,c),g.promise()}});var I;n.fn.ready=function(a){return n.ready.promise().done(a),this},n.extend({isReady:!1,readyWait:1,holdReady:function(a){a?n.readyWait++:n.ready(!0)},ready:function(a){(a===!0?--n.readyWait:n.isReady)||(n.isReady=!0,a!==!0&amp;&amp;--n.readyWait&gt;0||(I.resolveWith(d,[n]),n.fn.triggerHandler&amp;&amp;(n(d).triggerHandler(&quot;ready&quot;),n(d).off(&quot;ready&quot;))))}});function J(){d.addEventListener?(d.removeEventListener(&quot;DOMContentLoaded&quot;,K),a.removeEventListener(&quot;load&quot;,K)):(d.detachEvent(&quot;onreadystatechange&quot;,K),a.detachEvent(&quot;onload&quot;,K))}function K(){(d.addEventListener||&quot;load&quot;===a.event.type||&quot;complete&quot;===d.readyState)&amp;&amp;(J(),n.ready())}n.ready.promise=function(b){if(!I)if(I=n.Deferred(),&quot;complete&quot;===d.readyState||&quot;loading&quot;!==d.readyState&amp;&amp;!d.documentElement.doScroll)a.setTimeout(n.ready);else if(d.addEventListener)d.addEventListener(&quot;DOMContentLoaded&quot;,K),a.addEventListener(&quot;load&quot;,K);else{d.attachEvent(&quot;onreadystatechange&quot;,K),a.attachEvent(&quot;onload&quot;,K);var c=!1;try{c=null==a.frameElement&amp;&amp;d.documentElement}catch(e){}c&amp;&amp;c.doScroll&amp;&amp;!function f(){if(!n.isReady){try{c.doScroll(&quot;left&quot;)}catch(b){return a.setTimeout(f,50)}J(),n.ready()}}()}return I.promise(b)},n.ready.promise();var L;for(L in n(l))break;l.ownFirst=&quot;0&quot;===L,l.inlineBlockNeedsLayout=!1,n(function(){var a,b,c,e;c=d.getElementsByTagName(&quot;body&quot;)[0],c&amp;&amp;c.style&amp;&amp;(b=d.createElement(&quot;div&quot;),e=d.createElement(&quot;div&quot;),e.style.cssText=&quot;position:absolute;border:0;width:0;height:0;top:0;left:-9999px&quot;,c.appendChild(e).appendChild(b),&quot;undefined&quot;!=typeof b.style.zoom&amp;&amp;(b.style.cssText=&quot;display:inline;margin:0;border:0;padding:1px;width:1px;zoom:1&quot;,l.inlineBlockNeedsLayout=a=3===b.offsetWidth,a&amp;&amp;(c.style.zoom=1)),c.removeChild(e))}),function(){var a=d.createElement(&quot;div&quot;);l.deleteExpando=!0;try{delete a.test}catch(b){l.deleteExpando=!1}a=null}();var M=function(a){var b=n.noData[(a.nodeName+&quot; &quot;).toLowerCase()],c=+a.nodeType||1;return 1!==c&amp;&amp;9!==c?!1:!b||b!==!0&amp;&amp;a.getAttribute(&quot;classid&quot;)===b},N=/^(?:\{[\w\W]*\}|\[[\w\W]*\])$/,O=/([A-Z])/g;function P(a,b,c){if(void 0===c&amp;&amp;1===a.nodeType){var d=&quot;data-&quot;+b.replace(O,&quot;-$1&quot;).toLowerCase();if(c=a.getAttribute(d),&quot;string&quot;==typeof c){try{c=&quot;true&quot;===c?!0:&quot;false&quot;===c?!1:&quot;null&quot;===c?null:+c+&quot;&quot;===c?+c:N.test(c)?n.parseJSON(c):c}catch(e){}n.data(a,b,c)}else c=void 0;
}return c}function Q(a){var b;for(b in a)if((&quot;data&quot;!==b||!n.isEmptyObject(a[b]))&amp;&amp;&quot;toJSON&quot;!==b)return!1;return!0}function R(a,b,d,e){if(M(a)){var f,g,h=n.expando,i=a.nodeType,j=i?n.cache:a,k=i?a[h]:a[h]&amp;&amp;h;if(k&amp;&amp;j[k]&amp;&amp;(e||j[k].data)||void 0!==d||&quot;string&quot;!=typeof b)return k||(k=i?a[h]=c.pop()||n.guid++:h),j[k]||(j[k]=i?{}:{toJSON:n.noop}),&quot;object&quot;!=typeof b&amp;&amp;&quot;function&quot;!=typeof b||(e?j[k]=n.extend(j[k],b):j[k].data=n.extend(j[k].data,b)),g=j[k],e||(g.data||(g.data={}),g=g.data),void 0!==d&amp;&amp;(g[n.camelCase(b)]=d),&quot;string&quot;==typeof b?(f=g[b],null==f&amp;&amp;(f=g[n.camelCase(b)])):f=g,f}}function S(a,b,c){if(M(a)){var d,e,f=a.nodeType,g=f?n.cache:a,h=f?a[n.expando]:n.expando;if(g[h]){if(b&amp;&amp;(d=c?g[h]:g[h].data)){n.isArray(b)?b=b.concat(n.map(b,n.camelCase)):b in d?b=[b]:(b=n.camelCase(b),b=b in d?[b]:b.split(&quot; &quot;)),e=b.length;while(e--)delete d[b[e]];if(c?!Q(d):!n.isEmptyObject(d))return}(c||(delete g[h].data,Q(g[h])))&amp;&amp;(f?n.cleanData([a],!0):l.deleteExpando||g!=g.window?delete g[h]:g[h]=void 0)}}}n.extend({cache:{},noData:{&quot;applet &quot;:!0,&quot;embed &quot;:!0,&quot;object &quot;:&quot;clsid:D27CDB6E-AE6D-11cf-96B8-444553540000&quot;},hasData:function(a){return a=a.nodeType?n.cache[a[n.expando]]:a[n.expando],!!a&amp;&amp;!Q(a)},data:function(a,b,c){return R(a,b,c)},removeData:function(a,b){return S(a,b)},_data:function(a,b,c){return R(a,b,c,!0)},_removeData:function(a,b){return S(a,b,!0)}}),n.fn.extend({data:function(a,b){var c,d,e,f=this[0],g=f&amp;&amp;f.attributes;if(void 0===a){if(this.length&amp;&amp;(e=n.data(f),1===f.nodeType&amp;&amp;!n._data(f,&quot;parsedAttrs&quot;))){c=g.length;while(c--)g[c]&amp;&amp;(d=g[c].name,0===d.indexOf(&quot;data-&quot;)&amp;&amp;(d=n.camelCase(d.slice(5)),P(f,d,e[d])));n._data(f,&quot;parsedAttrs&quot;,!0)}return e}return&quot;object&quot;==typeof a?this.each(function(){n.data(this,a)}):arguments.length&gt;1?this.each(function(){n.data(this,a,b)}):f?P(f,a,n.data(f,a)):void 0},removeData:function(a){return this.each(function(){n.removeData(this,a)})}}),n.extend({queue:function(a,b,c){var d;return a?(b=(b||&quot;fx&quot;)+&quot;queue&quot;,d=n._data(a,b),c&amp;&amp;(!d||n.isArray(c)?d=n._data(a,b,n.makeArray(c)):d.push(c)),d||[]):void 0},dequeue:function(a,b){b=b||&quot;fx&quot;;var c=n.queue(a,b),d=c.length,e=c.shift(),f=n._queueHooks(a,b),g=function(){n.dequeue(a,b)};&quot;inprogress&quot;===e&amp;&amp;(e=c.shift(),d--),e&amp;&amp;(&quot;fx&quot;===b&amp;&amp;c.unshift(&quot;inprogress&quot;),delete f.stop,e.call(a,g,f)),!d&amp;&amp;f&amp;&amp;f.empty.fire()},_queueHooks:function(a,b){var c=b+&quot;queueHooks&quot;;return n._data(a,c)||n._data(a,c,{empty:n.Callbacks(&quot;once memory&quot;).add(function(){n._removeData(a,b+&quot;queue&quot;),n._removeData(a,c)})})}}),n.fn.extend({queue:function(a,b){var c=2;return&quot;string&quot;!=typeof a&amp;&amp;(b=a,a=&quot;fx&quot;,c--),arguments.length&lt;c?n.queue(this[0],a):void 0===b?this:this.each(function(){var c=n.queue(this,a,b);n._queueHooks(this,a),&quot;fx&quot;===a&amp;&amp;&quot;inprogress&quot;!==c[0]&amp;&amp;n.dequeue(this,a)})},dequeue:function(a){return this.each(function(){n.dequeue(this,a)})},clearQueue:function(a){return this.queue(a||&quot;fx&quot;,[])},promise:function(a,b){var c,d=1,e=n.Deferred(),f=this,g=this.length,h=function(){--d||e.resolveWith(f,[f])};&quot;string&quot;!=typeof a&amp;&amp;(b=a,a=void 0),a=a||&quot;fx&quot;;while(g--)c=n._data(f[g],a+&quot;queueHooks&quot;),c&amp;&amp;c.empty&amp;&amp;(d++,c.empty.add(h));return h(),e.promise(b)}}),function(){var a;l.shrinkWrapBlocks=function(){if(null!=a)return a;a=!1;var b,c,e;return c=d.getElementsByTagName(&quot;body&quot;)[0],c&amp;&amp;c.style?(b=d.createElement(&quot;div&quot;),e=d.createElement(&quot;div&quot;),e.style.cssText=&quot;position:absolute;border:0;width:0;height:0;top:0;left:-9999px&quot;,c.appendChild(e).appendChild(b),&quot;undefined&quot;!=typeof b.style.zoom&amp;&amp;(b.style.cssText=&quot;-webkit-box-sizing:content-box;-moz-box-sizing:content-box;box-sizing:content-box;display:block;margin:0;border:0;padding:1px;width:1px;zoom:1&quot;,b.appendChild(d.createElement(&quot;div&quot;)).style.width=&quot;5px&quot;,a=3!==b.offsetWidth),c.removeChild(e),a):void 0}}();var T=/[+-]?(?:\d*\.|)\d+(?:[eE][+-]?\d+|)/.source,U=new RegExp(&quot;^(?:([+-])=|)(&quot;+T+&quot;)([a-z%]*)$&quot;,&quot;i&quot;),V=[&quot;Top&quot;,&quot;Right&quot;,&quot;Bottom&quot;,&quot;Left&quot;],W=function(a,b){return a=b||a,&quot;none&quot;===n.css(a,&quot;display&quot;)||!n.contains(a.ownerDocument,a)};function X(a,b,c,d){var e,f=1,g=20,h=d?function(){return d.cur()}:function(){return n.css(a,b,&quot;&quot;)},i=h(),j=c&amp;&amp;c[3]||(n.cssNumber[b]?&quot;&quot;:&quot;px&quot;),k=(n.cssNumber[b]||&quot;px&quot;!==j&amp;&amp;+i)&amp;&amp;U.exec(n.css(a,b));if(k&amp;&amp;k[3]!==j){j=j||k[3],c=c||[],k=+i||1;do f=f||&quot;.5&quot;,k/=f,n.style(a,b,k+j);while(f!==(f=h()/i)&amp;&amp;1!==f&amp;&amp;--g)}return c&amp;&amp;(k=+k||+i||0,e=c[1]?k+(c[1]+1)*c[2]:+c[2],d&amp;&amp;(d.unit=j,d.start=k,d.end=e)),e}var Y=function(a,b,c,d,e,f,g){var h=0,i=a.length,j=null==c;if(&quot;object&quot;===n.type(c)){e=!0;for(h in c)Y(a,b,h,c[h],!0,f,g)}else if(void 0!==d&amp;&amp;(e=!0,n.isFunction(d)||(g=!0),j&amp;&amp;(g?(b.call(a,d),b=null):(j=b,b=function(a,b,c){return j.call(n(a),c)})),b))for(;i&gt;h;h++)b(a[h],c,g?d:d.call(a[h],h,b(a[h],c)));return e?a:j?b.call(a):i?b(a[0],c):f},Z=/^(?:checkbox|radio)$/i,$=/&lt;([\w:-]+)/,_=/^$|\/(?:java|ecma)script/i,aa=/^\s+/,ba=&quot;abbr|article|aside|audio|bdi|canvas|data|datalist|details|dialog|figcaption|figure|footer|header|hgroup|main|mark|meter|nav|output|picture|progress|section|summary|template|time|video&quot;;function ca(a){var b=ba.split(&quot;|&quot;),c=a.createDocumentFragment();if(c.createElement)while(b.length)c.createElement(b.pop());return c}!function(){var a=d.createElement(&quot;div&quot;),b=d.createDocumentFragment(),c=d.createElement(&quot;input&quot;);a.innerHTML=&quot;  &lt;link/&gt;&lt;table&gt;&lt;/table&gt;&lt;a href=&#x27;/a&#x27;&gt;a&lt;/a&gt;&lt;input type=&#x27;checkbox&#x27;/&gt;&quot;,l.leadingWhitespace=3===a.firstChild.nodeType,l.tbody=!a.getElementsByTagName(&quot;tbody&quot;).length,l.htmlSerialize=!!a.getElementsByTagName(&quot;link&quot;).length,l.html5Clone=&quot;&lt;:nav&gt;&lt;/:nav&gt;&quot;!==d.createElement(&quot;nav&quot;).cloneNode(!0).outerHTML,c.type=&quot;checkbox&quot;,c.checked=!0,b.appendChild(c),l.appendChecked=c.checked,a.innerHTML=&quot;&lt;textarea&gt;x&lt;/textarea&gt;&quot;,l.noCloneChecked=!!a.cloneNode(!0).lastChild.defaultValue,b.appendChild(a),c=d.createElement(&quot;input&quot;),c.setAttribute(&quot;type&quot;,&quot;radio&quot;),c.setAttribute(&quot;checked&quot;,&quot;checked&quot;),c.setAttribute(&quot;name&quot;,&quot;t&quot;),a.appendChild(c),l.checkClone=a.cloneNode(!0).cloneNode(!0).lastChild.checked,l.noCloneEvent=!!a.addEventListener,a[n.expando]=1,l.attributes=!a.getAttribute(n.expando)}();var da={option:[1,&quot;&lt;select multiple=&#x27;multiple&#x27;&gt;&quot;,&quot;&lt;/select&gt;&quot;],legend:[1,&quot;&lt;fieldset&gt;&quot;,&quot;&lt;/fieldset&gt;&quot;],area:[1,&quot;&lt;map&gt;&quot;,&quot;&lt;/map&gt;&quot;],param:[1,&quot;&lt;object&gt;&quot;,&quot;&lt;/object&gt;&quot;],thead:[1,&quot;&lt;table&gt;&quot;,&quot;&lt;/table&gt;&quot;],tr:[2,&quot;&lt;table&gt;&lt;tbody&gt;&quot;,&quot;&lt;/tbody&gt;&lt;/table&gt;&quot;],col:[2,&quot;&lt;table&gt;&lt;tbody&gt;&lt;/tbody&gt;&lt;colgroup&gt;&quot;,&quot;&lt;/colgroup&gt;&lt;/table&gt;&quot;],td:[3,&quot;&lt;table&gt;&lt;tbody&gt;&lt;tr&gt;&quot;,&quot;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&quot;],_default:l.htmlSerialize?[0,&quot;&quot;,&quot;&quot;]:[1,&quot;X&lt;div&gt;&quot;,&quot;&lt;/div&gt;&quot;]};da.optgroup=da.option,da.tbody=da.tfoot=da.colgroup=da.caption=da.thead,da.th=da.td;function ea(a,b){var c,d,e=0,f=&quot;undefined&quot;!=typeof a.getElementsByTagName?a.getElementsByTagName(b||&quot;*&quot;):&quot;undefined&quot;!=typeof a.querySelectorAll?a.querySelectorAll(b||&quot;*&quot;):void 0;if(!f)for(f=[],c=a.childNodes||a;null!=(d=c[e]);e++)!b||n.nodeName(d,b)?f.push(d):n.merge(f,ea(d,b));return void 0===b||b&amp;&amp;n.nodeName(a,b)?n.merge([a],f):f}function fa(a,b){for(var c,d=0;null!=(c=a[d]);d++)n._data(c,&quot;globalEval&quot;,!b||n._data(b[d],&quot;globalEval&quot;))}var ga=/&lt;|&amp;#?\w+;/,ha=/&lt;tbody/i;function ia(a){Z.test(a.type)&amp;&amp;(a.defaultChecked=a.checked)}function ja(a,b,c,d,e){for(var f,g,h,i,j,k,m,o=a.length,p=ca(b),q=[],r=0;o&gt;r;r++)if(g=a[r],g||0===g)if(&quot;object&quot;===n.type(g))n.merge(q,g.nodeType?[g]:g);else if(ga.test(g)){i=i||p.appendChild(b.createElement(&quot;div&quot;)),j=($.exec(g)||[&quot;&quot;,&quot;&quot;])[1].toLowerCase(),m=da[j]||da._default,i.innerHTML=m[1]+n.htmlPrefilter(g)+m[2],f=m[0];while(f--)i=i.lastChild;if(!l.leadingWhitespace&amp;&amp;aa.test(g)&amp;&amp;q.push(b.createTextNode(aa.exec(g)[0])),!l.tbody){g=&quot;table&quot;!==j||ha.test(g)?&quot;&lt;table&gt;&quot;!==m[1]||ha.test(g)?0:i:i.firstChild,f=g&amp;&amp;g.childNodes.length;while(f--)n.nodeName(k=g.childNodes[f],&quot;tbody&quot;)&amp;&amp;!k.childNodes.length&amp;&amp;g.removeChild(k)}n.merge(q,i.childNodes),i.textContent=&quot;&quot;;while(i.firstChild)i.removeChild(i.firstChild);i=p.lastChild}else q.push(b.createTextNode(g));i&amp;&amp;p.removeChild(i),l.appendChecked||n.grep(ea(q,&quot;input&quot;),ia),r=0;while(g=q[r++])if(d&amp;&amp;n.inArray(g,d)&gt;-1)e&amp;&amp;e.push(g);else if(h=n.contains(g.ownerDocument,g),i=ea(p.appendChild(g),&quot;script&quot;),h&amp;&amp;fa(i),c){f=0;while(g=i[f++])_.test(g.type||&quot;&quot;)&amp;&amp;c.push(g)}return i=null,p}!function(){var b,c,e=d.createElement(&quot;div&quot;);for(b in{submit:!0,change:!0,focusin:!0})c=&quot;on&quot;+b,(l[b]=c in a)||(e.setAttribute(c,&quot;t&quot;),l[b]=e.attributes[c].expando===!1);e=null}();var ka=/^(?:input|select|textarea)$/i,la=/^key/,ma=/^(?:mouse|pointer|contextmenu|drag|drop)|click/,na=/^(?:focusinfocus|focusoutblur)$/,oa=/^([^.]*)(?:\.(.+)|)/;function pa(){return!0}function qa(){return!1}function ra(){try{return d.activeElement}catch(a){}}function sa(a,b,c,d,e,f){var g,h;if(&quot;object&quot;==typeof b){&quot;string&quot;!=typeof c&amp;&amp;(d=d||c,c=void 0);for(h in b)sa(a,h,c,d,b[h],f);return a}if(null==d&amp;&amp;null==e?(e=c,d=c=void 0):null==e&amp;&amp;(&quot;string&quot;==typeof c?(e=d,d=void 0):(e=d,d=c,c=void 0)),e===!1)e=qa;else if(!e)return a;return 1===f&amp;&amp;(g=e,e=function(a){return n().off(a),g.apply(this,arguments)},e.guid=g.guid||(g.guid=n.guid++)),a.each(function(){n.event.add(this,b,e,d,c)})}n.event={global:{},add:function(a,b,c,d,e){var f,g,h,i,j,k,l,m,o,p,q,r=n._data(a);if(r){c.handler&amp;&amp;(i=c,c=i.handler,e=i.selector),c.guid||(c.guid=n.guid++),(g=r.events)||(g=r.events={}),(k=r.handle)||(k=r.handle=function(a){return&quot;undefined&quot;==typeof n||a&amp;&amp;n.event.triggered===a.type?void 0:n.event.dispatch.apply(k.elem,arguments)},k.elem=a),b=(b||&quot;&quot;).match(G)||[&quot;&quot;],h=b.length;while(h--)f=oa.exec(b[h])||[],o=q=f[1],p=(f[2]||&quot;&quot;).split(&quot;.&quot;).sort(),o&amp;&amp;(j=n.event.special[o]||{},o=(e?j.delegateType:j.bindType)||o,j=n.event.special[o]||{},l=n.extend({type:o,origType:q,data:d,handler:c,guid:c.guid,selector:e,needsContext:e&amp;&amp;n.expr.match.needsContext.test(e),namespace:p.join(&quot;.&quot;)},i),(m=g[o])||(m=g[o]=[],m.delegateCount=0,j.setup&amp;&amp;j.setup.call(a,d,p,k)!==!1||(a.addEventListener?a.addEventListener(o,k,!1):a.attachEvent&amp;&amp;a.attachEvent(&quot;on&quot;+o,k))),j.add&amp;&amp;(j.add.call(a,l),l.handler.guid||(l.handler.guid=c.guid)),e?m.splice(m.delegateCount++,0,l):m.push(l),n.event.global[o]=!0);a=null}},remove:function(a,b,c,d,e){var f,g,h,i,j,k,l,m,o,p,q,r=n.hasData(a)&amp;&amp;n._data(a);if(r&amp;&amp;(k=r.events)){b=(b||&quot;&quot;).match(G)||[&quot;&quot;],j=b.length;while(j--)if(h=oa.exec(b[j])||[],o=q=h[1],p=(h[2]||&quot;&quot;).split(&quot;.&quot;).sort(),o){l=n.event.special[o]||{},o=(d?l.delegateType:l.bindType)||o,m=k[o]||[],h=h[2]&amp;&amp;new RegExp(&quot;(^|\\.)&quot;+p.join(&quot;\\.(?:.*\\.|)&quot;)+&quot;(\\.|$)&quot;),i=f=m.length;while(f--)g=m[f],!e&amp;&amp;q!==g.origType||c&amp;&amp;c.guid!==g.guid||h&amp;&amp;!h.test(g.namespace)||d&amp;&amp;d!==g.selector&amp;&amp;(&quot;**&quot;!==d||!g.selector)||(m.splice(f,1),g.selector&amp;&amp;m.delegateCount--,l.remove&amp;&amp;l.remove.call(a,g));i&amp;&amp;!m.length&amp;&amp;(l.teardown&amp;&amp;l.teardown.call(a,p,r.handle)!==!1||n.removeEvent(a,o,r.handle),delete k[o])}else for(o in k)n.event.remove(a,o+b[j],c,d,!0);n.isEmptyObject(k)&amp;&amp;(delete r.handle,n._removeData(a,&quot;events&quot;))}},trigger:function(b,c,e,f){var g,h,i,j,l,m,o,p=[e||d],q=k.call(b,&quot;type&quot;)?b.type:b,r=k.call(b,&quot;namespace&quot;)?b.namespace.split(&quot;.&quot;):[];if(i=m=e=e||d,3!==e.nodeType&amp;&amp;8!==e.nodeType&amp;&amp;!na.test(q+n.event.triggered)&amp;&amp;(q.indexOf(&quot;.&quot;)&gt;-1&amp;&amp;(r=q.split(&quot;.&quot;),q=r.shift(),r.sort()),h=q.indexOf(&quot;:&quot;)&lt;0&amp;&amp;&quot;on&quot;+q,b=b[n.expando]?b:new n.Event(q,&quot;object&quot;==typeof b&amp;&amp;b),b.isTrigger=f?2:3,b.namespace=r.join(&quot;.&quot;),b.rnamespace=b.namespace?new RegExp(&quot;(^|\\.)&quot;+r.join(&quot;\\.(?:.*\\.|)&quot;)+&quot;(\\.|$)&quot;):null,b.result=void 0,b.target||(b.target=e),c=null==c?[b]:n.makeArray(c,[b]),l=n.event.special[q]||{},f||!l.trigger||l.trigger.apply(e,c)!==!1)){if(!f&amp;&amp;!l.noBubble&amp;&amp;!n.isWindow(e)){for(j=l.delegateType||q,na.test(j+q)||(i=i.parentNode);i;i=i.parentNode)p.push(i),m=i;m===(e.ownerDocument||d)&amp;&amp;p.push(m.defaultView||m.parentWindow||a)}o=0;while((i=p[o++])&amp;&amp;!b.isPropagationStopped())b.type=o&gt;1?j:l.bindType||q,g=(n._data(i,&quot;events&quot;)||{})[b.type]&amp;&amp;n._data(i,&quot;handle&quot;),g&amp;&amp;g.apply(i,c),g=h&amp;&amp;i[h],g&amp;&amp;g.apply&amp;&amp;M(i)&amp;&amp;(b.result=g.apply(i,c),b.result===!1&amp;&amp;b.preventDefault());if(b.type=q,!f&amp;&amp;!b.isDefaultPrevented()&amp;&amp;(!l._default||l._default.apply(p.pop(),c)===!1)&amp;&amp;M(e)&amp;&amp;h&amp;&amp;e[q]&amp;&amp;!n.isWindow(e)){m=e[h],m&amp;&amp;(e[h]=null),n.event.triggered=q;try{e[q]()}catch(s){}n.event.triggered=void 0,m&amp;&amp;(e[h]=m)}return b.result}},dispatch:function(a){a=n.event.fix(a);var b,c,d,f,g,h=[],i=e.call(arguments),j=(n._data(this,&quot;events&quot;)||{})[a.type]||[],k=n.event.special[a.type]||{};if(i[0]=a,a.delegateTarget=this,!k.preDispatch||k.preDispatch.call(this,a)!==!1){h=n.event.handlers.call(this,a,j),b=0;while((f=h[b++])&amp;&amp;!a.isPropagationStopped()){a.currentTarget=f.elem,c=0;while((g=f.handlers[c++])&amp;&amp;!a.isImmediatePropagationStopped())a.rnamespace&amp;&amp;!a.rnamespace.test(g.namespace)||(a.handleObj=g,a.data=g.data,d=((n.event.special[g.origType]||{}).handle||g.handler).apply(f.elem,i),void 0!==d&amp;&amp;(a.result=d)===!1&amp;&amp;(a.preventDefault(),a.stopPropagation()))}return k.postDispatch&amp;&amp;k.postDispatch.call(this,a),a.result}},handlers:function(a,b){var c,d,e,f,g=[],h=b.delegateCount,i=a.target;if(h&amp;&amp;i.nodeType&amp;&amp;(&quot;click&quot;!==a.type||isNaN(a.button)||a.button&lt;1))for(;i!=this;i=i.parentNode||this)if(1===i.nodeType&amp;&amp;(i.disabled!==!0||&quot;click&quot;!==a.type)){for(d=[],c=0;h&gt;c;c++)f=b[c],e=f.selector+&quot; &quot;,void 0===d[e]&amp;&amp;(d[e]=f.needsContext?n(e,this).index(i)&gt;-1:n.find(e,this,null,[i]).length),d[e]&amp;&amp;d.push(f);d.length&amp;&amp;g.push({elem:i,handlers:d})}return h&lt;b.length&amp;&amp;g.push({elem:this,handlers:b.slice(h)}),g},fix:function(a){if(a[n.expando])return a;var b,c,e,f=a.type,g=a,h=this.fixHooks[f];h||(this.fixHooks[f]=h=ma.test(f)?this.mouseHooks:la.test(f)?this.keyHooks:{}),e=h.props?this.props.concat(h.props):this.props,a=new n.Event(g),b=e.length;while(b--)c=e[b],a[c]=g[c];return a.target||(a.target=g.srcElement||d),3===a.target.nodeType&amp;&amp;(a.target=a.target.parentNode),a.metaKey=!!a.metaKey,h.filter?h.filter(a,g):a},props:&quot;altKey bubbles cancelable ctrlKey currentTarget detail eventPhase metaKey relatedTarget shiftKey target timeStamp view which&quot;.split(&quot; &quot;),fixHooks:{},keyHooks:{props:&quot;char charCode key keyCode&quot;.split(&quot; &quot;),filter:function(a,b){return null==a.which&amp;&amp;(a.which=null!=b.charCode?b.charCode:b.keyCode),a}},mouseHooks:{props:&quot;button buttons clientX clientY fromElement offsetX offsetY pageX pageY screenX screenY toElement&quot;.split(&quot; &quot;),filter:function(a,b){var c,e,f,g=b.button,h=b.fromElement;return null==a.pageX&amp;&amp;null!=b.clientX&amp;&amp;(e=a.target.ownerDocument||d,f=e.documentElement,c=e.body,a.pageX=b.clientX+(f&amp;&amp;f.scrollLeft||c&amp;&amp;c.scrollLeft||0)-(f&amp;&amp;f.clientLeft||c&amp;&amp;c.clientLeft||0),a.pageY=b.clientY+(f&amp;&amp;f.scrollTop||c&amp;&amp;c.scrollTop||0)-(f&amp;&amp;f.clientTop||c&amp;&amp;c.clientTop||0)),!a.relatedTarget&amp;&amp;h&amp;&amp;(a.relatedTarget=h===a.target?b.toElement:h),a.which||void 0===g||(a.which=1&amp;g?1:2&amp;g?3:4&amp;g?2:0),a}},special:{load:{noBubble:!0},focus:{trigger:function(){if(this!==ra()&amp;&amp;this.focus)try{return this.focus(),!1}catch(a){}},delegateType:&quot;focusin&quot;},blur:{trigger:function(){return this===ra()&amp;&amp;this.blur?(this.blur(),!1):void 0},delegateType:&quot;focusout&quot;},click:{trigger:function(){return n.nodeName(this,&quot;input&quot;)&amp;&amp;&quot;checkbox&quot;===this.type&amp;&amp;this.click?(this.click(),!1):void 0},_default:function(a){return n.nodeName(a.target,&quot;a&quot;)}},beforeunload:{postDispatch:function(a){void 0!==a.result&amp;&amp;a.originalEvent&amp;&amp;(a.originalEvent.returnValue=a.result)}}},simulate:function(a,b,c){var d=n.extend(new n.Event,c,{type:a,isSimulated:!0});n.event.trigger(d,null,b),d.isDefaultPrevented()&amp;&amp;c.preventDefault()}},n.removeEvent=d.removeEventListener?function(a,b,c){a.removeEventListener&amp;&amp;a.removeEventListener(b,c)}:function(a,b,c){var d=&quot;on&quot;+b;a.detachEvent&amp;&amp;(&quot;undefined&quot;==typeof a[d]&amp;&amp;(a[d]=null),a.detachEvent(d,c))},n.Event=function(a,b){return this instanceof n.Event?(a&amp;&amp;a.type?(this.originalEvent=a,this.type=a.type,this.isDefaultPrevented=a.defaultPrevented||void 0===a.defaultPrevented&amp;&amp;a.returnValue===!1?pa:qa):this.type=a,b&amp;&amp;n.extend(this,b),this.timeStamp=a&amp;&amp;a.timeStamp||n.now(),void(this[n.expando]=!0)):new n.Event(a,b)},n.Event.prototype={constructor:n.Event,isDefaultPrevented:qa,isPropagationStopped:qa,isImmediatePropagationStopped:qa,preventDefault:function(){var a=this.originalEvent;this.isDefaultPrevented=pa,a&amp;&amp;(a.preventDefault?a.preventDefault():a.returnValue=!1)},stopPropagation:function(){var a=this.originalEvent;this.isPropagationStopped=pa,a&amp;&amp;!this.isSimulated&amp;&amp;(a.stopPropagation&amp;&amp;a.stopPropagation(),a.cancelBubble=!0)},stopImmediatePropagation:function(){var a=this.originalEvent;this.isImmediatePropagationStopped=pa,a&amp;&amp;a.stopImmediatePropagation&amp;&amp;a.stopImmediatePropagation(),this.stopPropagation()}},n.each({mouseenter:&quot;mouseover&quot;,mouseleave:&quot;mouseout&quot;,pointerenter:&quot;pointerover&quot;,pointerleave:&quot;pointerout&quot;},function(a,b){n.event.special[a]={delegateType:b,bindType:b,handle:function(a){var c,d=this,e=a.relatedTarget,f=a.handleObj;return e&amp;&amp;(e===d||n.contains(d,e))||(a.type=f.origType,c=f.handler.apply(this,arguments),a.type=b),c}}}),l.submit||(n.event.special.submit={setup:function(){return n.nodeName(this,&quot;form&quot;)?!1:void n.event.add(this,&quot;click._submit keypress._submit&quot;,function(a){var b=a.target,c=n.nodeName(b,&quot;input&quot;)||n.nodeName(b,&quot;button&quot;)?n.prop(b,&quot;form&quot;):void 0;c&amp;&amp;!n._data(c,&quot;submit&quot;)&amp;&amp;(n.event.add(c,&quot;submit._submit&quot;,function(a){a._submitBubble=!0}),n._data(c,&quot;submit&quot;,!0))})},postDispatch:function(a){a._submitBubble&amp;&amp;(delete a._submitBubble,this.parentNode&amp;&amp;!a.isTrigger&amp;&amp;n.event.simulate(&quot;submit&quot;,this.parentNode,a))},teardown:function(){return n.nodeName(this,&quot;form&quot;)?!1:void n.event.remove(this,&quot;._submit&quot;)}}),l.change||(n.event.special.change={setup:function(){return ka.test(this.nodeName)?(&quot;checkbox&quot;!==this.type&amp;&amp;&quot;radio&quot;!==this.type||(n.event.add(this,&quot;propertychange._change&quot;,function(a){&quot;checked&quot;===a.originalEvent.propertyName&amp;&amp;(this._justChanged=!0)}),n.event.add(this,&quot;click._change&quot;,function(a){this._justChanged&amp;&amp;!a.isTrigger&amp;&amp;(this._justChanged=!1),n.event.simulate(&quot;change&quot;,this,a)})),!1):void n.event.add(this,&quot;beforeactivate._change&quot;,function(a){var b=a.target;ka.test(b.nodeName)&amp;&amp;!n._data(b,&quot;change&quot;)&amp;&amp;(n.event.add(b,&quot;change._change&quot;,function(a){!this.parentNode||a.isSimulated||a.isTrigger||n.event.simulate(&quot;change&quot;,this.parentNode,a)}),n._data(b,&quot;change&quot;,!0))})},handle:function(a){var b=a.target;return this!==b||a.isSimulated||a.isTrigger||&quot;radio&quot;!==b.type&amp;&amp;&quot;checkbox&quot;!==b.type?a.handleObj.handler.apply(this,arguments):void 0},teardown:function(){return n.event.remove(this,&quot;._change&quot;),!ka.test(this.nodeName)}}),l.focusin||n.each({focus:&quot;focusin&quot;,blur:&quot;focusout&quot;},function(a,b){var c=function(a){n.event.simulate(b,a.target,n.event.fix(a))};n.event.special[b]={setup:function(){var d=this.ownerDocument||this,e=n._data(d,b);e||d.addEventListener(a,c,!0),n._data(d,b,(e||0)+1)},teardown:function(){var d=this.ownerDocument||this,e=n._data(d,b)-1;e?n._data(d,b,e):(d.removeEventListener(a,c,!0),n._removeData(d,b))}}}),n.fn.extend({on:function(a,b,c,d){return sa(this,a,b,c,d)},one:function(a,b,c,d){return sa(this,a,b,c,d,1)},off:function(a,b,c){var d,e;if(a&amp;&amp;a.preventDefault&amp;&amp;a.handleObj)return d=a.handleObj,n(a.delegateTarget).off(d.namespace?d.origType+&quot;.&quot;+d.namespace:d.origType,d.selector,d.handler),this;if(&quot;object&quot;==typeof a){for(e in a)this.off(e,b,a[e]);return this}return b!==!1&amp;&amp;&quot;function&quot;!=typeof b||(c=b,b=void 0),c===!1&amp;&amp;(c=qa),this.each(function(){n.event.remove(this,a,c,b)})},trigger:function(a,b){return this.each(function(){n.event.trigger(a,b,this)})},triggerHandler:function(a,b){var c=this[0];return c?n.event.trigger(a,b,c,!0):void 0}});var ta=/ jQuery\d+=&quot;(?:null|\d+)&quot;/g,ua=new RegExp(&quot;&lt;(?:&quot;+ba+&quot;)[\\s/&gt;]&quot;,&quot;i&quot;),va=/&lt;(?!area|br|col|embed|hr|img|input|link|meta|param)(([\w:-]+)[^&gt;]*)\/&gt;/gi,wa=/&lt;script|&lt;style|&lt;link/i,xa=/checked\s*(?:[^=]|=\s*.checked.)/i,ya=/^true\/(.*)/,za=/^\s*&lt;!(?:\[CDATA\[|--)|(?:\]\]|--)&gt;\s*$/g,Aa=ca(d),Ba=Aa.appendChild(d.createElement(&quot;div&quot;));function Ca(a,b){return n.nodeName(a,&quot;table&quot;)&amp;&amp;n.nodeName(11!==b.nodeType?b:b.firstChild,&quot;tr&quot;)?a.getElementsByTagName(&quot;tbody&quot;)[0]||a.appendChild(a.ownerDocument.createElement(&quot;tbody&quot;)):a}function Da(a){return a.type=(null!==n.find.attr(a,&quot;type&quot;))+&quot;/&quot;+a.type,a}function Ea(a){var b=ya.exec(a.type);return b?a.type=b[1]:a.removeAttribute(&quot;type&quot;),a}function Fa(a,b){if(1===b.nodeType&amp;&amp;n.hasData(a)){var c,d,e,f=n._data(a),g=n._data(b,f),h=f.events;if(h){delete g.handle,g.events={};for(c in h)for(d=0,e=h[c].length;e&gt;d;d++)n.event.add(b,c,h[c][d])}g.data&amp;&amp;(g.data=n.extend({},g.data))}}function Ga(a,b){var c,d,e;if(1===b.nodeType){if(c=b.nodeName.toLowerCase(),!l.noCloneEvent&amp;&amp;b[n.expando]){e=n._data(b);for(d in e.events)n.removeEvent(b,d,e.handle);b.removeAttribute(n.expando)}&quot;script&quot;===c&amp;&amp;b.text!==a.text?(Da(b).text=a.text,Ea(b)):&quot;object&quot;===c?(b.parentNode&amp;&amp;(b.outerHTML=a.outerHTML),l.html5Clone&amp;&amp;a.innerHTML&amp;&amp;!n.trim(b.innerHTML)&amp;&amp;(b.innerHTML=a.innerHTML)):&quot;input&quot;===c&amp;&amp;Z.test(a.type)?(b.defaultChecked=b.checked=a.checked,b.value!==a.value&amp;&amp;(b.value=a.value)):&quot;option&quot;===c?b.defaultSelected=b.selected=a.defaultSelected:&quot;input&quot;!==c&amp;&amp;&quot;textarea&quot;!==c||(b.defaultValue=a.defaultValue)}}function Ha(a,b,c,d){b=f.apply([],b);var e,g,h,i,j,k,m=0,o=a.length,p=o-1,q=b[0],r=n.isFunction(q);if(r||o&gt;1&amp;&amp;&quot;string&quot;==typeof q&amp;&amp;!l.checkClone&amp;&amp;xa.test(q))return a.each(function(e){var f=a.eq(e);r&amp;&amp;(b[0]=q.call(this,e,f.html())),Ha(f,b,c,d)});if(o&amp;&amp;(k=ja(b,a[0].ownerDocument,!1,a,d),e=k.firstChild,1===k.childNodes.length&amp;&amp;(k=e),e||d)){for(i=n.map(ea(k,&quot;script&quot;),Da),h=i.length;o&gt;m;m++)g=k,m!==p&amp;&amp;(g=n.clone(g,!0,!0),h&amp;&amp;n.merge(i,ea(g,&quot;script&quot;))),c.call(a[m],g,m);if(h)for(j=i[i.length-1].ownerDocument,n.map(i,Ea),m=0;h&gt;m;m++)g=i[m],_.test(g.type||&quot;&quot;)&amp;&amp;!n._data(g,&quot;globalEval&quot;)&amp;&amp;n.contains(j,g)&amp;&amp;(g.src?n._evalUrl&amp;&amp;n._evalUrl(g.src):n.globalEval((g.text||g.textContent||g.innerHTML||&quot;&quot;).replace(za,&quot;&quot;)));k=e=null}return a}function Ia(a,b,c){for(var d,e=b?n.filter(b,a):a,f=0;null!=(d=e[f]);f++)c||1!==d.nodeType||n.cleanData(ea(d)),d.parentNode&amp;&amp;(c&amp;&amp;n.contains(d.ownerDocument,d)&amp;&amp;fa(ea(d,&quot;script&quot;)),d.parentNode.removeChild(d));return a}n.extend({htmlPrefilter:function(a){return a.replace(va,&quot;&lt;$1&gt;&lt;/$2&gt;&quot;)},clone:function(a,b,c){var d,e,f,g,h,i=n.contains(a.ownerDocument,a);if(l.html5Clone||n.isXMLDoc(a)||!ua.test(&quot;&lt;&quot;+a.nodeName+&quot;&gt;&quot;)?f=a.cloneNode(!0):(Ba.innerHTML=a.outerHTML,Ba.removeChild(f=Ba.firstChild)),!(l.noCloneEvent&amp;&amp;l.noCloneChecked||1!==a.nodeType&amp;&amp;11!==a.nodeType||n.isXMLDoc(a)))for(d=ea(f),h=ea(a),g=0;null!=(e=h[g]);++g)d[g]&amp;&amp;Ga(e,d[g]);if(b)if(c)for(h=h||ea(a),d=d||ea(f),g=0;null!=(e=h[g]);g++)Fa(e,d[g]);else Fa(a,f);return d=ea(f,&quot;script&quot;),d.length&gt;0&amp;&amp;fa(d,!i&amp;&amp;ea(a,&quot;script&quot;)),d=h=e=null,f},cleanData:function(a,b){for(var d,e,f,g,h=0,i=n.expando,j=n.cache,k=l.attributes,m=n.event.special;null!=(d=a[h]);h++)if((b||M(d))&amp;&amp;(f=d[i],g=f&amp;&amp;j[f])){if(g.events)for(e in g.events)m[e]?n.event.remove(d,e):n.removeEvent(d,e,g.handle);j[f]&amp;&amp;(delete j[f],k||&quot;undefined&quot;==typeof d.removeAttribute?d[i]=void 0:d.removeAttribute(i),c.push(f))}}}),n.fn.extend({domManip:Ha,detach:function(a){return Ia(this,a,!0)},remove:function(a){return Ia(this,a)},text:function(a){return Y(this,function(a){return void 0===a?n.text(this):this.empty().append((this[0]&amp;&amp;this[0].ownerDocument||d).createTextNode(a))},null,a,arguments.length)},append:function(){return Ha(this,arguments,function(a){if(1===this.nodeType||11===this.nodeType||9===this.nodeType){var b=Ca(this,a);b.appendChild(a)}})},prepend:function(){return Ha(this,arguments,function(a){if(1===this.nodeType||11===this.nodeType||9===this.nodeType){var b=Ca(this,a);b.insertBefore(a,b.firstChild)}})},before:function(){return Ha(this,arguments,function(a){this.parentNode&amp;&amp;this.parentNode.insertBefore(a,this)})},after:function(){return Ha(this,arguments,function(a){this.parentNode&amp;&amp;this.parentNode.insertBefore(a,this.nextSibling)})},empty:function(){for(var a,b=0;null!=(a=this[b]);b++){1===a.nodeType&amp;&amp;n.cleanData(ea(a,!1));while(a.firstChild)a.removeChild(a.firstChild);a.options&amp;&amp;n.nodeName(a,&quot;select&quot;)&amp;&amp;(a.options.length=0)}return this},clone:function(a,b){return a=null==a?!1:a,b=null==b?a:b,this.map(function(){return n.clone(this,a,b)})},html:function(a){return Y(this,function(a){var b=this[0]||{},c=0,d=this.length;if(void 0===a)return 1===b.nodeType?b.innerHTML.replace(ta,&quot;&quot;):void 0;if(&quot;string&quot;==typeof a&amp;&amp;!wa.test(a)&amp;&amp;(l.htmlSerialize||!ua.test(a))&amp;&amp;(l.leadingWhitespace||!aa.test(a))&amp;&amp;!da[($.exec(a)||[&quot;&quot;,&quot;&quot;])[1].toLowerCase()]){a=n.htmlPrefilter(a);try{for(;d&gt;c;c++)b=this[c]||{},1===b.nodeType&amp;&amp;(n.cleanData(ea(b,!1)),b.innerHTML=a);b=0}catch(e){}}b&amp;&amp;this.empty().append(a)},null,a,arguments.length)},replaceWith:function(){var a=[];return Ha(this,arguments,function(b){var c=this.parentNode;n.inArray(this,a)&lt;0&amp;&amp;(n.cleanData(ea(this)),c&amp;&amp;c.replaceChild(b,this))},a)}}),n.each({appendTo:&quot;append&quot;,prependTo:&quot;prepend&quot;,insertBefore:&quot;before&quot;,insertAfter:&quot;after&quot;,replaceAll:&quot;replaceWith&quot;},function(a,b){n.fn[a]=function(a){for(var c,d=0,e=[],f=n(a),h=f.length-1;h&gt;=d;d++)c=d===h?this:this.clone(!0),n(f[d])[b](c),g.apply(e,c.get());return this.pushStack(e)}});var Ja,Ka={HTML:&quot;block&quot;,BODY:&quot;block&quot;};function La(a,b){var c=n(b.createElement(a)).appendTo(b.body),d=n.css(c[0],&quot;display&quot;);return c.detach(),d}function Ma(a){var b=d,c=Ka[a];return c||(c=La(a,b),&quot;none&quot;!==c&amp;&amp;c||(Ja=(Ja||n(&quot;&lt;iframe frameborder=&#x27;0&#x27; width=&#x27;0&#x27; height=&#x27;0&#x27;/&gt;&quot;)).appendTo(b.documentElement),b=(Ja[0].contentWindow||Ja[0].contentDocument).document,b.write(),b.close(),c=La(a,b),Ja.detach()),Ka[a]=c),c}var Na=/^margin/,Oa=new RegExp(&quot;^(&quot;+T+&quot;)(?!px)[a-z%]+$&quot;,&quot;i&quot;),Pa=function(a,b,c,d){var e,f,g={};for(f in b)g[f]=a.style[f],a.style[f]=b[f];e=c.apply(a,d||[]);for(f in b)a.style[f]=g[f];return e},Qa=d.documentElement;!function(){var b,c,e,f,g,h,i=d.createElement(&quot;div&quot;),j=d.createElement(&quot;div&quot;);if(j.style){j.style.cssText=&quot;float:left;opacity:.5&quot;,l.opacity=&quot;0.5&quot;===j.style.opacity,l.cssFloat=!!j.style.cssFloat,j.style.backgroundClip=&quot;content-box&quot;,j.cloneNode(!0).style.backgroundClip=&quot;&quot;,l.clearCloneStyle=&quot;content-box&quot;===j.style.backgroundClip,i=d.createElement(&quot;div&quot;),i.style.cssText=&quot;border:0;width:8px;height:0;top:0;left:-9999px;padding:0;margin-top:1px;position:absolute&quot;,j.innerHTML=&quot;&quot;,i.appendChild(j),l.boxSizing=&quot;&quot;===j.style.boxSizing||&quot;&quot;===j.style.MozBoxSizing||&quot;&quot;===j.style.WebkitBoxSizing,n.extend(l,{reliableHiddenOffsets:function(){return null==b&amp;&amp;k(),f},boxSizingReliable:function(){return null==b&amp;&amp;k(),e},pixelMarginRight:function(){return null==b&amp;&amp;k(),c},pixelPosition:function(){return null==b&amp;&amp;k(),b},reliableMarginRight:function(){return null==b&amp;&amp;k(),g},reliableMarginLeft:function(){return null==b&amp;&amp;k(),h}});function k(){var k,l,m=d.documentElement;m.appendChild(i),j.style.cssText=&quot;-webkit-box-sizing:border-box;box-sizing:border-box;position:relative;display:block;margin:auto;border:1px;padding:1px;top:1%;width:50%&quot;,b=e=h=!1,c=g=!0,a.getComputedStyle&amp;&amp;(l=a.getComputedStyle(j),b=&quot;1%&quot;!==(l||{}).top,h=&quot;2px&quot;===(l||{}).marginLeft,e=&quot;4px&quot;===(l||{width:&quot;4px&quot;}).width,j.style.marginRight=&quot;50%&quot;,c=&quot;4px&quot;===(l||{marginRight:&quot;4px&quot;}).marginRight,k=j.appendChild(d.createElement(&quot;div&quot;)),k.style.cssText=j.style.cssText=&quot;-webkit-box-sizing:content-box;-moz-box-sizing:content-box;box-sizing:content-box;display:block;margin:0;border:0;padding:0&quot;,k.style.marginRight=k.style.width=&quot;0&quot;,j.style.width=&quot;1px&quot;,g=!parseFloat((a.getComputedStyle(k)||{}).marginRight),j.removeChild(k)),j.style.display=&quot;none&quot;,f=0===j.getClientRects().length,f&amp;&amp;(j.style.display=&quot;&quot;,j.innerHTML=&quot;&lt;table&gt;&lt;tr&gt;&lt;td&gt;&lt;/td&gt;&lt;td&gt;t&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;&quot;,j.childNodes[0].style.borderCollapse=&quot;separate&quot;,k=j.getElementsByTagName(&quot;td&quot;),k[0].style.cssText=&quot;margin:0;border:0;padding:0;display:none&quot;,f=0===k[0].offsetHeight,f&amp;&amp;(k[0].style.display=&quot;&quot;,k[1].style.display=&quot;none&quot;,f=0===k[0].offsetHeight)),m.removeChild(i)}}}();var Ra,Sa,Ta=/^(top|right|bottom|left)$/;a.getComputedStyle?(Ra=function(b){var c=b.ownerDocument.defaultView;return c&amp;&amp;c.opener||(c=a),c.getComputedStyle(b)},Sa=function(a,b,c){var d,e,f,g,h=a.style;return c=c||Ra(a),g=c?c.getPropertyValue(b)||c[b]:void 0,&quot;&quot;!==g&amp;&amp;void 0!==g||n.contains(a.ownerDocument,a)||(g=n.style(a,b)),c&amp;&amp;!l.pixelMarginRight()&amp;&amp;Oa.test(g)&amp;&amp;Na.test(b)&amp;&amp;(d=h.width,e=h.minWidth,f=h.maxWidth,h.minWidth=h.maxWidth=h.width=g,g=c.width,h.width=d,h.minWidth=e,h.maxWidth=f),void 0===g?g:g+&quot;&quot;}):Qa.currentStyle&amp;&amp;(Ra=function(a){return a.currentStyle},Sa=function(a,b,c){var d,e,f,g,h=a.style;return c=c||Ra(a),g=c?c[b]:void 0,null==g&amp;&amp;h&amp;&amp;h[b]&amp;&amp;(g=h[b]),Oa.test(g)&amp;&amp;!Ta.test(b)&amp;&amp;(d=h.left,e=a.runtimeStyle,f=e&amp;&amp;e.left,f&amp;&amp;(e.left=a.currentStyle.left),h.left=&quot;fontSize&quot;===b?&quot;1em&quot;:g,g=h.pixelLeft+&quot;px&quot;,h.left=d,f&amp;&amp;(e.left=f)),void 0===g?g:g+&quot;&quot;||&quot;auto&quot;});function Ua(a,b){return{get:function(){return a()?void delete this.get:(this.get=b).apply(this,arguments)}}}var Va=/alpha\([^)]*\)/i,Wa=/opacity\s*=\s*([^)]*)/i,Xa=/^(none|table(?!-c[ea]).+)/,Ya=new RegExp(&quot;^(&quot;+T+&quot;)(.*)$&quot;,&quot;i&quot;),Za={position:&quot;absolute&quot;,visibility:&quot;hidden&quot;,display:&quot;block&quot;},$a={letterSpacing:&quot;0&quot;,fontWeight:&quot;400&quot;},_a=[&quot;Webkit&quot;,&quot;O&quot;,&quot;Moz&quot;,&quot;ms&quot;],ab=d.createElement(&quot;div&quot;).style;function bb(a){if(a in ab)return a;var b=a.charAt(0).toUpperCase()+a.slice(1),c=_a.length;while(c--)if(a=_a[c]+b,a in ab)return a}function cb(a,b){for(var c,d,e,f=[],g=0,h=a.length;h&gt;g;g++)d=a[g],d.style&amp;&amp;(f[g]=n._data(d,&quot;olddisplay&quot;),c=d.style.display,b?(f[g]||&quot;none&quot;!==c||(d.style.display=&quot;&quot;),&quot;&quot;===d.style.display&amp;&amp;W(d)&amp;&amp;(f[g]=n._data(d,&quot;olddisplay&quot;,Ma(d.nodeName)))):(e=W(d),(c&amp;&amp;&quot;none&quot;!==c||!e)&amp;&amp;n._data(d,&quot;olddisplay&quot;,e?c:n.css(d,&quot;display&quot;))));for(g=0;h&gt;g;g++)d=a[g],d.style&amp;&amp;(b&amp;&amp;&quot;none&quot;!==d.style.display&amp;&amp;&quot;&quot;!==d.style.display||(d.style.display=b?f[g]||&quot;&quot;:&quot;none&quot;));return a}function db(a,b,c){var d=Ya.exec(b);return d?Math.max(0,d[1]-(c||0))+(d[2]||&quot;px&quot;):b}function eb(a,b,c,d,e){for(var f=c===(d?&quot;border&quot;:&quot;content&quot;)?4:&quot;width&quot;===b?1:0,g=0;4&gt;f;f+=2)&quot;margin&quot;===c&amp;&amp;(g+=n.css(a,c+V[f],!0,e)),d?(&quot;content&quot;===c&amp;&amp;(g-=n.css(a,&quot;padding&quot;+V[f],!0,e)),&quot;margin&quot;!==c&amp;&amp;(g-=n.css(a,&quot;border&quot;+V[f]+&quot;Width&quot;,!0,e))):(g+=n.css(a,&quot;padding&quot;+V[f],!0,e),&quot;padding&quot;!==c&amp;&amp;(g+=n.css(a,&quot;border&quot;+V[f]+&quot;Width&quot;,!0,e)));return g}function fb(a,b,c){var d=!0,e=&quot;width&quot;===b?a.offsetWidth:a.offsetHeight,f=Ra(a),g=l.boxSizing&amp;&amp;&quot;border-box&quot;===n.css(a,&quot;boxSizing&quot;,!1,f);if(0&gt;=e||null==e){if(e=Sa(a,b,f),(0&gt;e||null==e)&amp;&amp;(e=a.style[b]),Oa.test(e))return e;d=g&amp;&amp;(l.boxSizingReliable()||e===a.style[b]),e=parseFloat(e)||0}return e+eb(a,b,c||(g?&quot;border&quot;:&quot;content&quot;),d,f)+&quot;px&quot;}n.extend({cssHooks:{opacity:{get:function(a,b){if(b){var c=Sa(a,&quot;opacity&quot;);return&quot;&quot;===c?&quot;1&quot;:c}}}},cssNumber:{animationIterationCount:!0,columnCount:!0,fillOpacity:!0,flexGrow:!0,flexShrink:!0,fontWeight:!0,lineHeight:!0,opacity:!0,order:!0,orphans:!0,widows:!0,zIndex:!0,zoom:!0},cssProps:{&quot;float&quot;:l.cssFloat?&quot;cssFloat&quot;:&quot;styleFloat&quot;},style:function(a,b,c,d){if(a&amp;&amp;3!==a.nodeType&amp;&amp;8!==a.nodeType&amp;&amp;a.style){var e,f,g,h=n.camelCase(b),i=a.style;if(b=n.cssProps[h]||(n.cssProps[h]=bb(h)||h),g=n.cssHooks[b]||n.cssHooks[h],void 0===c)return g&amp;&amp;&quot;get&quot;in g&amp;&amp;void 0!==(e=g.get(a,!1,d))?e:i[b];if(f=typeof c,&quot;string&quot;===f&amp;&amp;(e=U.exec(c))&amp;&amp;e[1]&amp;&amp;(c=X(a,b,e),f=&quot;number&quot;),null!=c&amp;&amp;c===c&amp;&amp;(&quot;number&quot;===f&amp;&amp;(c+=e&amp;&amp;e[3]||(n.cssNumber[h]?&quot;&quot;:&quot;px&quot;)),l.clearCloneStyle||&quot;&quot;!==c||0!==b.indexOf(&quot;background&quot;)||(i[b]=&quot;inherit&quot;),!(g&amp;&amp;&quot;set&quot;in g&amp;&amp;void 0===(c=g.set(a,c,d)))))try{i[b]=c}catch(j){}}},css:function(a,b,c,d){var e,f,g,h=n.camelCase(b);return b=n.cssProps[h]||(n.cssProps[h]=bb(h)||h),g=n.cssHooks[b]||n.cssHooks[h],g&amp;&amp;&quot;get&quot;in g&amp;&amp;(f=g.get(a,!0,c)),void 0===f&amp;&amp;(f=Sa(a,b,d)),&quot;normal&quot;===f&amp;&amp;b in $a&amp;&amp;(f=$a[b]),&quot;&quot;===c||c?(e=parseFloat(f),c===!0||isFinite(e)?e||0:f):f}}),n.each([&quot;height&quot;,&quot;width&quot;],function(a,b){n.cssHooks[b]={get:function(a,c,d){return c?Xa.test(n.css(a,&quot;display&quot;))&amp;&amp;0===a.offsetWidth?Pa(a,Za,function(){return fb(a,b,d)}):fb(a,b,d):void 0},set:function(a,c,d){var e=d&amp;&amp;Ra(a);return db(a,c,d?eb(a,b,d,l.boxSizing&amp;&amp;&quot;border-box&quot;===n.css(a,&quot;boxSizing&quot;,!1,e),e):0)}}}),l.opacity||(n.cssHooks.opacity={get:function(a,b){return Wa.test((b&amp;&amp;a.currentStyle?a.currentStyle.filter:a.style.filter)||&quot;&quot;)?.01*parseFloat(RegExp.$1)+&quot;&quot;:b?&quot;1&quot;:&quot;&quot;},set:function(a,b){var c=a.style,d=a.currentStyle,e=n.isNumeric(b)?&quot;alpha(opacity=&quot;+100*b+&quot;)&quot;:&quot;&quot;,f=d&amp;&amp;d.filter||c.filter||&quot;&quot;;c.zoom=1,(b&gt;=1||&quot;&quot;===b)&amp;&amp;&quot;&quot;===n.trim(f.replace(Va,&quot;&quot;))&amp;&amp;c.removeAttribute&amp;&amp;(c.removeAttribute(&quot;filter&quot;),&quot;&quot;===b||d&amp;&amp;!d.filter)||(c.filter=Va.test(f)?f.replace(Va,e):f+&quot; &quot;+e)}}),n.cssHooks.marginRight=Ua(l.reliableMarginRight,function(a,b){return b?Pa(a,{display:&quot;inline-block&quot;},Sa,[a,&quot;marginRight&quot;]):void 0}),n.cssHooks.marginLeft=Ua(l.reliableMarginLeft,function(a,b){return b?(parseFloat(Sa(a,&quot;marginLeft&quot;))||(n.contains(a.ownerDocument,a)?a.getBoundingClientRect().left-Pa(a,{
marginLeft:0},function(){return a.getBoundingClientRect().left}):0))+&quot;px&quot;:void 0}),n.each({margin:&quot;&quot;,padding:&quot;&quot;,border:&quot;Width&quot;},function(a,b){n.cssHooks[a+b]={expand:function(c){for(var d=0,e={},f=&quot;string&quot;==typeof c?c.split(&quot; &quot;):[c];4&gt;d;d++)e[a+V[d]+b]=f[d]||f[d-2]||f[0];return e}},Na.test(a)||(n.cssHooks[a+b].set=db)}),n.fn.extend({css:function(a,b){return Y(this,function(a,b,c){var d,e,f={},g=0;if(n.isArray(b)){for(d=Ra(a),e=b.length;e&gt;g;g++)f[b[g]]=n.css(a,b[g],!1,d);return f}return void 0!==c?n.style(a,b,c):n.css(a,b)},a,b,arguments.length&gt;1)},show:function(){return cb(this,!0)},hide:function(){return cb(this)},toggle:function(a){return&quot;boolean&quot;==typeof a?a?this.show():this.hide():this.each(function(){W(this)?n(this).show():n(this).hide()})}});function gb(a,b,c,d,e){return new gb.prototype.init(a,b,c,d,e)}n.Tween=gb,gb.prototype={constructor:gb,init:function(a,b,c,d,e,f){this.elem=a,this.prop=c,this.easing=e||n.easing._default,this.options=b,this.start=this.now=this.cur(),this.end=d,this.unit=f||(n.cssNumber[c]?&quot;&quot;:&quot;px&quot;)},cur:function(){var a=gb.propHooks[this.prop];return a&amp;&amp;a.get?a.get(this):gb.propHooks._default.get(this)},run:function(a){var b,c=gb.propHooks[this.prop];return this.options.duration?this.pos=b=n.easing[this.easing](a,this.options.duration*a,0,1,this.options.duration):this.pos=b=a,this.now=(this.end-this.start)*b+this.start,this.options.step&amp;&amp;this.options.step.call(this.elem,this.now,this),c&amp;&amp;c.set?c.set(this):gb.propHooks._default.set(this),this}},gb.prototype.init.prototype=gb.prototype,gb.propHooks={_default:{get:function(a){var b;return 1!==a.elem.nodeType||null!=a.elem[a.prop]&amp;&amp;null==a.elem.style[a.prop]?a.elem[a.prop]:(b=n.css(a.elem,a.prop,&quot;&quot;),b&amp;&amp;&quot;auto&quot;!==b?b:0)},set:function(a){n.fx.step[a.prop]?n.fx.step[a.prop](a):1!==a.elem.nodeType||null==a.elem.style[n.cssProps[a.prop]]&amp;&amp;!n.cssHooks[a.prop]?a.elem[a.prop]=a.now:n.style(a.elem,a.prop,a.now+a.unit)}}},gb.propHooks.scrollTop=gb.propHooks.scrollLeft={set:function(a){a.elem.nodeType&amp;&amp;a.elem.parentNode&amp;&amp;(a.elem[a.prop]=a.now)}},n.easing={linear:function(a){return a},swing:function(a){return.5-Math.cos(a*Math.PI)/2},_default:&quot;swing&quot;},n.fx=gb.prototype.init,n.fx.step={};var hb,ib,jb=/^(?:toggle|show|hide)$/,kb=/queueHooks$/;function lb(){return a.setTimeout(function(){hb=void 0}),hb=n.now()}function mb(a,b){var c,d={height:a},e=0;for(b=b?1:0;4&gt;e;e+=2-b)c=V[e],d[&quot;margin&quot;+c]=d[&quot;padding&quot;+c]=a;return b&amp;&amp;(d.opacity=d.width=a),d}function nb(a,b,c){for(var d,e=(qb.tweeners[b]||[]).concat(qb.tweeners[&quot;*&quot;]),f=0,g=e.length;g&gt;f;f++)if(d=e[f].call(c,b,a))return d}function ob(a,b,c){var d,e,f,g,h,i,j,k,m=this,o={},p=a.style,q=a.nodeType&amp;&amp;W(a),r=n._data(a,&quot;fxshow&quot;);c.queue||(h=n._queueHooks(a,&quot;fx&quot;),null==h.unqueued&amp;&amp;(h.unqueued=0,i=h.empty.fire,h.empty.fire=function(){h.unqueued||i()}),h.unqueued++,m.always(function(){m.always(function(){h.unqueued--,n.queue(a,&quot;fx&quot;).length||h.empty.fire()})})),1===a.nodeType&amp;&amp;(&quot;height&quot;in b||&quot;width&quot;in b)&amp;&amp;(c.overflow=[p.overflow,p.overflowX,p.overflowY],j=n.css(a,&quot;display&quot;),k=&quot;none&quot;===j?n._data(a,&quot;olddisplay&quot;)||Ma(a.nodeName):j,&quot;inline&quot;===k&amp;&amp;&quot;none&quot;===n.css(a,&quot;float&quot;)&amp;&amp;(l.inlineBlockNeedsLayout&amp;&amp;&quot;inline&quot;!==Ma(a.nodeName)?p.zoom=1:p.display=&quot;inline-block&quot;)),c.overflow&amp;&amp;(p.overflow=&quot;hidden&quot;,l.shrinkWrapBlocks()||m.always(function(){p.overflow=c.overflow[0],p.overflowX=c.overflow[1],p.overflowY=c.overflow[2]}));for(d in b)if(e=b[d],jb.exec(e)){if(delete b[d],f=f||&quot;toggle&quot;===e,e===(q?&quot;hide&quot;:&quot;show&quot;)){if(&quot;show&quot;!==e||!r||void 0===r[d])continue;q=!0}o[d]=r&amp;&amp;r[d]||n.style(a,d)}else j=void 0;if(n.isEmptyObject(o))&quot;inline&quot;===(&quot;none&quot;===j?Ma(a.nodeName):j)&amp;&amp;(p.display=j);else{r?&quot;hidden&quot;in r&amp;&amp;(q=r.hidden):r=n._data(a,&quot;fxshow&quot;,{}),f&amp;&amp;(r.hidden=!q),q?n(a).show():m.done(function(){n(a).hide()}),m.done(function(){var b;n._removeData(a,&quot;fxshow&quot;);for(b in o)n.style(a,b,o[b])});for(d in o)g=nb(q?r[d]:0,d,m),d in r||(r[d]=g.start,q&amp;&amp;(g.end=g.start,g.start=&quot;width&quot;===d||&quot;height&quot;===d?1:0))}}function pb(a,b){var c,d,e,f,g;for(c in a)if(d=n.camelCase(c),e=b[d],f=a[c],n.isArray(f)&amp;&amp;(e=f[1],f=a[c]=f[0]),c!==d&amp;&amp;(a[d]=f,delete a[c]),g=n.cssHooks[d],g&amp;&amp;&quot;expand&quot;in g){f=g.expand(f),delete a[d];for(c in f)c in a||(a[c]=f[c],b[c]=e)}else b[d]=e}function qb(a,b,c){var d,e,f=0,g=qb.prefilters.length,h=n.Deferred().always(function(){delete i.elem}),i=function(){if(e)return!1;for(var b=hb||lb(),c=Math.max(0,j.startTime+j.duration-b),d=c/j.duration||0,f=1-d,g=0,i=j.tweens.length;i&gt;g;g++)j.tweens[g].run(f);return h.notifyWith(a,[j,f,c]),1&gt;f&amp;&amp;i?c:(h.resolveWith(a,[j]),!1)},j=h.promise({elem:a,props:n.extend({},b),opts:n.extend(!0,{specialEasing:{},easing:n.easing._default},c),originalProperties:b,originalOptions:c,startTime:hb||lb(),duration:c.duration,tweens:[],createTween:function(b,c){var d=n.Tween(a,j.opts,b,c,j.opts.specialEasing[b]||j.opts.easing);return j.tweens.push(d),d},stop:function(b){var c=0,d=b?j.tweens.length:0;if(e)return this;for(e=!0;d&gt;c;c++)j.tweens[c].run(1);return b?(h.notifyWith(a,[j,1,0]),h.resolveWith(a,[j,b])):h.rejectWith(a,[j,b]),this}}),k=j.props;for(pb(k,j.opts.specialEasing);g&gt;f;f++)if(d=qb.prefilters[f].call(j,a,k,j.opts))return n.isFunction(d.stop)&amp;&amp;(n._queueHooks(j.elem,j.opts.queue).stop=n.proxy(d.stop,d)),d;return n.map(k,nb,j),n.isFunction(j.opts.start)&amp;&amp;j.opts.start.call(a,j),n.fx.timer(n.extend(i,{elem:a,anim:j,queue:j.opts.queue})),j.progress(j.opts.progress).done(j.opts.done,j.opts.complete).fail(j.opts.fail).always(j.opts.always)}n.Animation=n.extend(qb,{tweeners:{&quot;*&quot;:[function(a,b){var c=this.createTween(a,b);return X(c.elem,a,U.exec(b),c),c}]},tweener:function(a,b){n.isFunction(a)?(b=a,a=[&quot;*&quot;]):a=a.match(G);for(var c,d=0,e=a.length;e&gt;d;d++)c=a[d],qb.tweeners[c]=qb.tweeners[c]||[],qb.tweeners[c].unshift(b)},prefilters:[ob],prefilter:function(a,b){b?qb.prefilters.unshift(a):qb.prefilters.push(a)}}),n.speed=function(a,b,c){var d=a&amp;&amp;&quot;object&quot;==typeof a?n.extend({},a):{complete:c||!c&amp;&amp;b||n.isFunction(a)&amp;&amp;a,duration:a,easing:c&amp;&amp;b||b&amp;&amp;!n.isFunction(b)&amp;&amp;b};return d.duration=n.fx.off?0:&quot;number&quot;==typeof d.duration?d.duration:d.duration in n.fx.speeds?n.fx.speeds[d.duration]:n.fx.speeds._default,null!=d.queue&amp;&amp;d.queue!==!0||(d.queue=&quot;fx&quot;),d.old=d.complete,d.complete=function(){n.isFunction(d.old)&amp;&amp;d.old.call(this),d.queue&amp;&amp;n.dequeue(this,d.queue)},d},n.fn.extend({fadeTo:function(a,b,c,d){return this.filter(W).css(&quot;opacity&quot;,0).show().end().animate({opacity:b},a,c,d)},animate:function(a,b,c,d){var e=n.isEmptyObject(a),f=n.speed(b,c,d),g=function(){var b=qb(this,n.extend({},a),f);(e||n._data(this,&quot;finish&quot;))&amp;&amp;b.stop(!0)};return g.finish=g,e||f.queue===!1?this.each(g):this.queue(f.queue,g)},stop:function(a,b,c){var d=function(a){var b=a.stop;delete a.stop,b(c)};return&quot;string&quot;!=typeof a&amp;&amp;(c=b,b=a,a=void 0),b&amp;&amp;a!==!1&amp;&amp;this.queue(a||&quot;fx&quot;,[]),this.each(function(){var b=!0,e=null!=a&amp;&amp;a+&quot;queueHooks&quot;,f=n.timers,g=n._data(this);if(e)g[e]&amp;&amp;g[e].stop&amp;&amp;d(g[e]);else for(e in g)g[e]&amp;&amp;g[e].stop&amp;&amp;kb.test(e)&amp;&amp;d(g[e]);for(e=f.length;e--;)f[e].elem!==this||null!=a&amp;&amp;f[e].queue!==a||(f[e].anim.stop(c),b=!1,f.splice(e,1));!b&amp;&amp;c||n.dequeue(this,a)})},finish:function(a){return a!==!1&amp;&amp;(a=a||&quot;fx&quot;),this.each(function(){var b,c=n._data(this),d=c[a+&quot;queue&quot;],e=c[a+&quot;queueHooks&quot;],f=n.timers,g=d?d.length:0;for(c.finish=!0,n.queue(this,a,[]),e&amp;&amp;e.stop&amp;&amp;e.stop.call(this,!0),b=f.length;b--;)f[b].elem===this&amp;&amp;f[b].queue===a&amp;&amp;(f[b].anim.stop(!0),f.splice(b,1));for(b=0;g&gt;b;b++)d[b]&amp;&amp;d[b].finish&amp;&amp;d[b].finish.call(this);delete c.finish})}}),n.each([&quot;toggle&quot;,&quot;show&quot;,&quot;hide&quot;],function(a,b){var c=n.fn[b];n.fn[b]=function(a,d,e){return null==a||&quot;boolean&quot;==typeof a?c.apply(this,arguments):this.animate(mb(b,!0),a,d,e)}}),n.each({slideDown:mb(&quot;show&quot;),slideUp:mb(&quot;hide&quot;),slideToggle:mb(&quot;toggle&quot;),fadeIn:{opacity:&quot;show&quot;},fadeOut:{opacity:&quot;hide&quot;},fadeToggle:{opacity:&quot;toggle&quot;}},function(a,b){n.fn[a]=function(a,c,d){return this.animate(b,a,c,d)}}),n.timers=[],n.fx.tick=function(){var a,b=n.timers,c=0;for(hb=n.now();c&lt;b.length;c++)a=b[c],a()||b[c]!==a||b.splice(c--,1);b.length||n.fx.stop(),hb=void 0},n.fx.timer=function(a){n.timers.push(a),a()?n.fx.start():n.timers.pop()},n.fx.interval=13,n.fx.start=function(){ib||(ib=a.setInterval(n.fx.tick,n.fx.interval))},n.fx.stop=function(){a.clearInterval(ib),ib=null},n.fx.speeds={slow:600,fast:200,_default:400},n.fn.delay=function(b,c){return b=n.fx?n.fx.speeds[b]||b:b,c=c||&quot;fx&quot;,this.queue(c,function(c,d){var e=a.setTimeout(c,b);d.stop=function(){a.clearTimeout(e)}})},function(){var a,b=d.createElement(&quot;input&quot;),c=d.createElement(&quot;div&quot;),e=d.createElement(&quot;select&quot;),f=e.appendChild(d.createElement(&quot;option&quot;));c=d.createElement(&quot;div&quot;),c.setAttribute(&quot;className&quot;,&quot;t&quot;),c.innerHTML=&quot;  &lt;link/&gt;&lt;table&gt;&lt;/table&gt;&lt;a href=&#x27;/a&#x27;&gt;a&lt;/a&gt;&lt;input type=&#x27;checkbox&#x27;/&gt;&quot;,a=c.getElementsByTagName(&quot;a&quot;)[0],b.setAttribute(&quot;type&quot;,&quot;checkbox&quot;),c.appendChild(b),a=c.getElementsByTagName(&quot;a&quot;)[0],a.style.cssText=&quot;top:1px&quot;,l.getSetAttribute=&quot;t&quot;!==c.className,l.style=/top/.test(a.getAttribute(&quot;style&quot;)),l.hrefNormalized=&quot;/a&quot;===a.getAttribute(&quot;href&quot;),l.checkOn=!!b.value,l.optSelected=f.selected,l.enctype=!!d.createElement(&quot;form&quot;).enctype,e.disabled=!0,l.optDisabled=!f.disabled,b=d.createElement(&quot;input&quot;),b.setAttribute(&quot;value&quot;,&quot;&quot;),l.input=&quot;&quot;===b.getAttribute(&quot;value&quot;),b.value=&quot;t&quot;,b.setAttribute(&quot;type&quot;,&quot;radio&quot;),l.radioValue=&quot;t&quot;===b.value}();var rb=/\r/g,sb=/[\x20\t\r\n\f]+/g;n.fn.extend({val:function(a){var b,c,d,e=this[0];{if(arguments.length)return d=n.isFunction(a),this.each(function(c){var e;1===this.nodeType&amp;&amp;(e=d?a.call(this,c,n(this).val()):a,null==e?e=&quot;&quot;:&quot;number&quot;==typeof e?e+=&quot;&quot;:n.isArray(e)&amp;&amp;(e=n.map(e,function(a){return null==a?&quot;&quot;:a+&quot;&quot;})),b=n.valHooks[this.type]||n.valHooks[this.nodeName.toLowerCase()],b&amp;&amp;&quot;set&quot;in b&amp;&amp;void 0!==b.set(this,e,&quot;value&quot;)||(this.value=e))});if(e)return b=n.valHooks[e.type]||n.valHooks[e.nodeName.toLowerCase()],b&amp;&amp;&quot;get&quot;in b&amp;&amp;void 0!==(c=b.get(e,&quot;value&quot;))?c:(c=e.value,&quot;string&quot;==typeof c?c.replace(rb,&quot;&quot;):null==c?&quot;&quot;:c)}}}),n.extend({valHooks:{option:{get:function(a){var b=n.find.attr(a,&quot;value&quot;);return null!=b?b:n.trim(n.text(a)).replace(sb,&quot; &quot;)}},select:{get:function(a){for(var b,c,d=a.options,e=a.selectedIndex,f=&quot;select-one&quot;===a.type||0&gt;e,g=f?null:[],h=f?e+1:d.length,i=0&gt;e?h:f?e:0;h&gt;i;i++)if(c=d[i],(c.selected||i===e)&amp;&amp;(l.optDisabled?!c.disabled:null===c.getAttribute(&quot;disabled&quot;))&amp;&amp;(!c.parentNode.disabled||!n.nodeName(c.parentNode,&quot;optgroup&quot;))){if(b=n(c).val(),f)return b;g.push(b)}return g},set:function(a,b){var c,d,e=a.options,f=n.makeArray(b),g=e.length;while(g--)if(d=e[g],n.inArray(n.valHooks.option.get(d),f)&gt;-1)try{d.selected=c=!0}catch(h){d.scrollHeight}else d.selected=!1;return c||(a.selectedIndex=-1),e}}}}),n.each([&quot;radio&quot;,&quot;checkbox&quot;],function(){n.valHooks[this]={set:function(a,b){return n.isArray(b)?a.checked=n.inArray(n(a).val(),b)&gt;-1:void 0}},l.checkOn||(n.valHooks[this].get=function(a){return null===a.getAttribute(&quot;value&quot;)?&quot;on&quot;:a.value})});var tb,ub,vb=n.expr.attrHandle,wb=/^(?:checked|selected)$/i,xb=l.getSetAttribute,yb=l.input;n.fn.extend({attr:function(a,b){return Y(this,n.attr,a,b,arguments.length&gt;1)},removeAttr:function(a){return this.each(function(){n.removeAttr(this,a)})}}),n.extend({attr:function(a,b,c){var d,e,f=a.nodeType;if(3!==f&amp;&amp;8!==f&amp;&amp;2!==f)return&quot;undefined&quot;==typeof a.getAttribute?n.prop(a,b,c):(1===f&amp;&amp;n.isXMLDoc(a)||(b=b.toLowerCase(),e=n.attrHooks[b]||(n.expr.match.bool.test(b)?ub:tb)),void 0!==c?null===c?void n.removeAttr(a,b):e&amp;&amp;&quot;set&quot;in e&amp;&amp;void 0!==(d=e.set(a,c,b))?d:(a.setAttribute(b,c+&quot;&quot;),c):e&amp;&amp;&quot;get&quot;in e&amp;&amp;null!==(d=e.get(a,b))?d:(d=n.find.attr(a,b),null==d?void 0:d))},attrHooks:{type:{set:function(a,b){if(!l.radioValue&amp;&amp;&quot;radio&quot;===b&amp;&amp;n.nodeName(a,&quot;input&quot;)){var c=a.value;return a.setAttribute(&quot;type&quot;,b),c&amp;&amp;(a.value=c),b}}}},removeAttr:function(a,b){var c,d,e=0,f=b&amp;&amp;b.match(G);if(f&amp;&amp;1===a.nodeType)while(c=f[e++])d=n.propFix[c]||c,n.expr.match.bool.test(c)?yb&amp;&amp;xb||!wb.test(c)?a[d]=!1:a[n.camelCase(&quot;default-&quot;+c)]=a[d]=!1:n.attr(a,c,&quot;&quot;),a.removeAttribute(xb?c:d)}}),ub={set:function(a,b,c){return b===!1?n.removeAttr(a,c):yb&amp;&amp;xb||!wb.test(c)?a.setAttribute(!xb&amp;&amp;n.propFix[c]||c,c):a[n.camelCase(&quot;default-&quot;+c)]=a[c]=!0,c}},n.each(n.expr.match.bool.source.match(/\w+/g),function(a,b){var c=vb[b]||n.find.attr;yb&amp;&amp;xb||!wb.test(b)?vb[b]=function(a,b,d){var e,f;return d||(f=vb[b],vb[b]=e,e=null!=c(a,b,d)?b.toLowerCase():null,vb[b]=f),e}:vb[b]=function(a,b,c){return c?void 0:a[n.camelCase(&quot;default-&quot;+b)]?b.toLowerCase():null}}),yb&amp;&amp;xb||(n.attrHooks.value={set:function(a,b,c){return n.nodeName(a,&quot;input&quot;)?void(a.defaultValue=b):tb&amp;&amp;tb.set(a,b,c)}}),xb||(tb={set:function(a,b,c){var d=a.getAttributeNode(c);return d||a.setAttributeNode(d=a.ownerDocument.createAttribute(c)),d.value=b+=&quot;&quot;,&quot;value&quot;===c||b===a.getAttribute(c)?b:void 0}},vb.id=vb.name=vb.coords=function(a,b,c){var d;return c?void 0:(d=a.getAttributeNode(b))&amp;&amp;&quot;&quot;!==d.value?d.value:null},n.valHooks.button={get:function(a,b){var c=a.getAttributeNode(b);return c&amp;&amp;c.specified?c.value:void 0},set:tb.set},n.attrHooks.contenteditable={set:function(a,b,c){tb.set(a,&quot;&quot;===b?!1:b,c)}},n.each([&quot;width&quot;,&quot;height&quot;],function(a,b){n.attrHooks[b]={set:function(a,c){return&quot;&quot;===c?(a.setAttribute(b,&quot;auto&quot;),c):void 0}}})),l.style||(n.attrHooks.style={get:function(a){return a.style.cssText||void 0},set:function(a,b){return a.style.cssText=b+&quot;&quot;}});var zb=/^(?:input|select|textarea|button|object)$/i,Ab=/^(?:a|area)$/i;n.fn.extend({prop:function(a,b){return Y(this,n.prop,a,b,arguments.length&gt;1)},removeProp:function(a){return a=n.propFix[a]||a,this.each(function(){try{this[a]=void 0,delete this[a]}catch(b){}})}}),n.extend({prop:function(a,b,c){var d,e,f=a.nodeType;if(3!==f&amp;&amp;8!==f&amp;&amp;2!==f)return 1===f&amp;&amp;n.isXMLDoc(a)||(b=n.propFix[b]||b,e=n.propHooks[b]),void 0!==c?e&amp;&amp;&quot;set&quot;in e&amp;&amp;void 0!==(d=e.set(a,c,b))?d:a[b]=c:e&amp;&amp;&quot;get&quot;in e&amp;&amp;null!==(d=e.get(a,b))?d:a[b]},propHooks:{tabIndex:{get:function(a){var b=n.find.attr(a,&quot;tabindex&quot;);return b?parseInt(b,10):zb.test(a.nodeName)||Ab.test(a.nodeName)&amp;&amp;a.href?0:-1}}},propFix:{&quot;for&quot;:&quot;htmlFor&quot;,&quot;class&quot;:&quot;className&quot;}}),l.hrefNormalized||n.each([&quot;href&quot;,&quot;src&quot;],function(a,b){n.propHooks[b]={get:function(a){return a.getAttribute(b,4)}}}),l.optSelected||(n.propHooks.selected={get:function(a){var b=a.parentNode;return b&amp;&amp;(b.selectedIndex,b.parentNode&amp;&amp;b.parentNode.selectedIndex),null},set:function(a){var b=a.parentNode;b&amp;&amp;(b.selectedIndex,b.parentNode&amp;&amp;b.parentNode.selectedIndex)}}),n.each([&quot;tabIndex&quot;,&quot;readOnly&quot;,&quot;maxLength&quot;,&quot;cellSpacing&quot;,&quot;cellPadding&quot;,&quot;rowSpan&quot;,&quot;colSpan&quot;,&quot;useMap&quot;,&quot;frameBorder&quot;,&quot;contentEditable&quot;],function(){n.propFix[this.toLowerCase()]=this}),l.enctype||(n.propFix.enctype=&quot;encoding&quot;);var Bb=/[\t\r\n\f]/g;function Cb(a){return n.attr(a,&quot;class&quot;)||&quot;&quot;}n.fn.extend({addClass:function(a){var b,c,d,e,f,g,h,i=0;if(n.isFunction(a))return this.each(function(b){n(this).addClass(a.call(this,b,Cb(this)))});if(&quot;string&quot;==typeof a&amp;&amp;a){b=a.match(G)||[];while(c=this[i++])if(e=Cb(c),d=1===c.nodeType&amp;&amp;(&quot; &quot;+e+&quot; &quot;).replace(Bb,&quot; &quot;)){g=0;while(f=b[g++])d.indexOf(&quot; &quot;+f+&quot; &quot;)&lt;0&amp;&amp;(d+=f+&quot; &quot;);h=n.trim(d),e!==h&amp;&amp;n.attr(c,&quot;class&quot;,h)}}return this},removeClass:function(a){var b,c,d,e,f,g,h,i=0;if(n.isFunction(a))return this.each(function(b){n(this).removeClass(a.call(this,b,Cb(this)))});if(!arguments.length)return this.attr(&quot;class&quot;,&quot;&quot;);if(&quot;string&quot;==typeof a&amp;&amp;a){b=a.match(G)||[];while(c=this[i++])if(e=Cb(c),d=1===c.nodeType&amp;&amp;(&quot; &quot;+e+&quot; &quot;).replace(Bb,&quot; &quot;)){g=0;while(f=b[g++])while(d.indexOf(&quot; &quot;+f+&quot; &quot;)&gt;-1)d=d.replace(&quot; &quot;+f+&quot; &quot;,&quot; &quot;);h=n.trim(d),e!==h&amp;&amp;n.attr(c,&quot;class&quot;,h)}}return this},toggleClass:function(a,b){var c=typeof a;return&quot;boolean&quot;==typeof b&amp;&amp;&quot;string&quot;===c?b?this.addClass(a):this.removeClass(a):n.isFunction(a)?this.each(function(c){n(this).toggleClass(a.call(this,c,Cb(this),b),b)}):this.each(function(){var b,d,e,f;if(&quot;string&quot;===c){d=0,e=n(this),f=a.match(G)||[];while(b=f[d++])e.hasClass(b)?e.removeClass(b):e.addClass(b)}else void 0!==a&amp;&amp;&quot;boolean&quot;!==c||(b=Cb(this),b&amp;&amp;n._data(this,&quot;__className__&quot;,b),n.attr(this,&quot;class&quot;,b||a===!1?&quot;&quot;:n._data(this,&quot;__className__&quot;)||&quot;&quot;))})},hasClass:function(a){var b,c,d=0;b=&quot; &quot;+a+&quot; &quot;;while(c=this[d++])if(1===c.nodeType&amp;&amp;(&quot; &quot;+Cb(c)+&quot; &quot;).replace(Bb,&quot; &quot;).indexOf(b)&gt;-1)return!0;return!1}}),n.each(&quot;blur focus focusin focusout load resize scroll unload click dblclick mousedown mouseup mousemove mouseover mouseout mouseenter mouseleave change select submit keydown keypress keyup error contextmenu&quot;.split(&quot; &quot;),function(a,b){n.fn[b]=function(a,c){return arguments.length&gt;0?this.on(b,null,a,c):this.trigger(b)}}),n.fn.extend({hover:function(a,b){return this.mouseenter(a).mouseleave(b||a)}});var Db=a.location,Eb=n.now(),Fb=/\?/,Gb=/(,)|(\[|{)|(}|])|&quot;(?:[^&quot;\\\r\n]|\\[&quot;\\\/bfnrt]|\\u[\da-fA-F]{4})*&quot;\s*:?|true|false|null|-?(?!0\d)\d+(?:\.\d+|)(?:[eE][+-]?\d+|)/g;n.parseJSON=function(b){if(a.JSON&amp;&amp;a.JSON.parse)return a.JSON.parse(b+&quot;&quot;);var c,d=null,e=n.trim(b+&quot;&quot;);return e&amp;&amp;!n.trim(e.replace(Gb,function(a,b,e,f){return c&amp;&amp;b&amp;&amp;(d=0),0===d?a:(c=e||b,d+=!f-!e,&quot;&quot;)}))?Function(&quot;return &quot;+e)():n.error(&quot;Invalid JSON: &quot;+b)},n.parseXML=function(b){var c,d;if(!b||&quot;string&quot;!=typeof b)return null;try{a.DOMParser?(d=new a.DOMParser,c=d.parseFromString(b,&quot;text/xml&quot;)):(c=new a.ActiveXObject(&quot;Microsoft.XMLDOM&quot;),c.async=&quot;false&quot;,c.loadXML(b))}catch(e){c=void 0}return c&amp;&amp;c.documentElement&amp;&amp;!c.getElementsByTagName(&quot;parsererror&quot;).length||n.error(&quot;Invalid XML: &quot;+b),c};var Hb=/#.*$/,Ib=/([?&amp;])_=[^&amp;]*/,Jb=/^(.*?):[ \t]*([^\r\n]*)\r?$/gm,Kb=/^(?:about|app|app-storage|.+-extension|file|res|widget):$/,Lb=/^(?:GET|HEAD)$/,Mb=/^\/\//,Nb=/^([\w.+-]+:)(?:\/\/(?:[^\/?#]*@|)([^\/?#:]*)(?::(\d+)|)|)/,Ob={},Pb={},Qb=&quot;*/&quot;.concat(&quot;*&quot;),Rb=Db.href,Sb=Nb.exec(Rb.toLowerCase())||[];function Tb(a){return function(b,c){&quot;string&quot;!=typeof b&amp;&amp;(c=b,b=&quot;*&quot;);var d,e=0,f=b.toLowerCase().match(G)||[];if(n.isFunction(c))while(d=f[e++])&quot;+&quot;===d.charAt(0)?(d=d.slice(1)||&quot;*&quot;,(a[d]=a[d]||[]).unshift(c)):(a[d]=a[d]||[]).push(c)}}function Ub(a,b,c,d){var e={},f=a===Pb;function g(h){var i;return e[h]=!0,n.each(a[h]||[],function(a,h){var j=h(b,c,d);return&quot;string&quot;!=typeof j||f||e[j]?f?!(i=j):void 0:(b.dataTypes.unshift(j),g(j),!1)}),i}return g(b.dataTypes[0])||!e[&quot;*&quot;]&amp;&amp;g(&quot;*&quot;)}function Vb(a,b){var c,d,e=n.ajaxSettings.flatOptions||{};for(d in b)void 0!==b[d]&amp;&amp;((e[d]?a:c||(c={}))[d]=b[d]);return c&amp;&amp;n.extend(!0,a,c),a}function Wb(a,b,c){var d,e,f,g,h=a.contents,i=a.dataTypes;while(&quot;*&quot;===i[0])i.shift(),void 0===e&amp;&amp;(e=a.mimeType||b.getResponseHeader(&quot;Content-Type&quot;));if(e)for(g in h)if(h[g]&amp;&amp;h[g].test(e)){i.unshift(g);break}if(i[0]in c)f=i[0];else{for(g in c){if(!i[0]||a.converters[g+&quot; &quot;+i[0]]){f=g;break}d||(d=g)}f=f||d}return f?(f!==i[0]&amp;&amp;i.unshift(f),c[f]):void 0}function Xb(a,b,c,d){var e,f,g,h,i,j={},k=a.dataTypes.slice();if(k[1])for(g in a.converters)j[g.toLowerCase()]=a.converters[g];f=k.shift();while(f)if(a.responseFields[f]&amp;&amp;(c[a.responseFields[f]]=b),!i&amp;&amp;d&amp;&amp;a.dataFilter&amp;&amp;(b=a.dataFilter(b,a.dataType)),i=f,f=k.shift())if(&quot;*&quot;===f)f=i;else if(&quot;*&quot;!==i&amp;&amp;i!==f){if(g=j[i+&quot; &quot;+f]||j[&quot;* &quot;+f],!g)for(e in j)if(h=e.split(&quot; &quot;),h[1]===f&amp;&amp;(g=j[i+&quot; &quot;+h[0]]||j[&quot;* &quot;+h[0]])){g===!0?g=j[e]:j[e]!==!0&amp;&amp;(f=h[0],k.unshift(h[1]));break}if(g!==!0)if(g&amp;&amp;a[&quot;throws&quot;])b=g(b);else try{b=g(b)}catch(l){return{state:&quot;parsererror&quot;,error:g?l:&quot;No conversion from &quot;+i+&quot; to &quot;+f}}}return{state:&quot;success&quot;,data:b}}n.extend({active:0,lastModified:{},etag:{},ajaxSettings:{url:Rb,type:&quot;GET&quot;,isLocal:Kb.test(Sb[1]),global:!0,processData:!0,async:!0,contentType:&quot;application/x-www-form-urlencoded; charset=UTF-8&quot;,accepts:{&quot;*&quot;:Qb,text:&quot;text/plain&quot;,html:&quot;text/html&quot;,xml:&quot;application/xml, text/xml&quot;,json:&quot;application/json, text/javascript&quot;},contents:{xml:/\bxml\b/,html:/\bhtml/,json:/\bjson\b/},responseFields:{xml:&quot;responseXML&quot;,text:&quot;responseText&quot;,json:&quot;responseJSON&quot;},converters:{&quot;* text&quot;:String,&quot;text html&quot;:!0,&quot;text json&quot;:n.parseJSON,&quot;text xml&quot;:n.parseXML},flatOptions:{url:!0,context:!0}},ajaxSetup:function(a,b){return b?Vb(Vb(a,n.ajaxSettings),b):Vb(n.ajaxSettings,a)},ajaxPrefilter:Tb(Ob),ajaxTransport:Tb(Pb),ajax:function(b,c){&quot;object&quot;==typeof b&amp;&amp;(c=b,b=void 0),c=c||{};var d,e,f,g,h,i,j,k,l=n.ajaxSetup({},c),m=l.context||l,o=l.context&amp;&amp;(m.nodeType||m.jquery)?n(m):n.event,p=n.Deferred(),q=n.Callbacks(&quot;once memory&quot;),r=l.statusCode||{},s={},t={},u=0,v=&quot;canceled&quot;,w={readyState:0,getResponseHeader:function(a){var b;if(2===u){if(!k){k={};while(b=Jb.exec(g))k[b[1].toLowerCase()]=b[2]}b=k[a.toLowerCase()]}return null==b?null:b},getAllResponseHeaders:function(){return 2===u?g:null},setRequestHeader:function(a,b){var c=a.toLowerCase();return u||(a=t[c]=t[c]||a,s[a]=b),this},overrideMimeType:function(a){return u||(l.mimeType=a),this},statusCode:function(a){var b;if(a)if(2&gt;u)for(b in a)r[b]=[r[b],a[b]];else w.always(a[w.status]);return this},abort:function(a){var b=a||v;return j&amp;&amp;j.abort(b),y(0,b),this}};if(p.promise(w).complete=q.add,w.success=w.done,w.error=w.fail,l.url=((b||l.url||Rb)+&quot;&quot;).replace(Hb,&quot;&quot;).replace(Mb,Sb[1]+&quot;//&quot;),l.type=c.method||c.type||l.method||l.type,l.dataTypes=n.trim(l.dataType||&quot;*&quot;).toLowerCase().match(G)||[&quot;&quot;],null==l.crossDomain&amp;&amp;(d=Nb.exec(l.url.toLowerCase()),l.crossDomain=!(!d||d[1]===Sb[1]&amp;&amp;d[2]===Sb[2]&amp;&amp;(d[3]||(&quot;http:&quot;===d[1]?&quot;80&quot;:&quot;443&quot;))===(Sb[3]||(&quot;http:&quot;===Sb[1]?&quot;80&quot;:&quot;443&quot;)))),l.data&amp;&amp;l.processData&amp;&amp;&quot;string&quot;!=typeof l.data&amp;&amp;(l.data=n.param(l.data,l.traditional)),Ub(Ob,l,c,w),2===u)return w;i=n.event&amp;&amp;l.global,i&amp;&amp;0===n.active++&amp;&amp;n.event.trigger(&quot;ajaxStart&quot;),l.type=l.type.toUpperCase(),l.hasContent=!Lb.test(l.type),f=l.url,l.hasContent||(l.data&amp;&amp;(f=l.url+=(Fb.test(f)?&quot;&amp;&quot;:&quot;?&quot;)+l.data,delete l.data),l.cache===!1&amp;&amp;(l.url=Ib.test(f)?f.replace(Ib,&quot;$1_=&quot;+Eb++):f+(Fb.test(f)?&quot;&amp;&quot;:&quot;?&quot;)+&quot;_=&quot;+Eb++)),l.ifModified&amp;&amp;(n.lastModified[f]&amp;&amp;w.setRequestHeader(&quot;If-Modified-Since&quot;,n.lastModified[f]),n.etag[f]&amp;&amp;w.setRequestHeader(&quot;If-None-Match&quot;,n.etag[f])),(l.data&amp;&amp;l.hasContent&amp;&amp;l.contentType!==!1||c.contentType)&amp;&amp;w.setRequestHeader(&quot;Content-Type&quot;,l.contentType),w.setRequestHeader(&quot;Accept&quot;,l.dataTypes[0]&amp;&amp;l.accepts[l.dataTypes[0]]?l.accepts[l.dataTypes[0]]+(&quot;*&quot;!==l.dataTypes[0]?&quot;, &quot;+Qb+&quot;; q=0.01&quot;:&quot;&quot;):l.accepts[&quot;*&quot;]);for(e in l.headers)w.setRequestHeader(e,l.headers[e]);if(l.beforeSend&amp;&amp;(l.beforeSend.call(m,w,l)===!1||2===u))return w.abort();v=&quot;abort&quot;;for(e in{success:1,error:1,complete:1})w[e](l[e]);if(j=Ub(Pb,l,c,w)){if(w.readyState=1,i&amp;&amp;o.trigger(&quot;ajaxSend&quot;,[w,l]),2===u)return w;l.async&amp;&amp;l.timeout&gt;0&amp;&amp;(h=a.setTimeout(function(){w.abort(&quot;timeout&quot;)},l.timeout));try{u=1,j.send(s,y)}catch(x){if(!(2&gt;u))throw x;y(-1,x)}}else y(-1,&quot;No Transport&quot;);function y(b,c,d,e){var k,s,t,v,x,y=c;2!==u&amp;&amp;(u=2,h&amp;&amp;a.clearTimeout(h),j=void 0,g=e||&quot;&quot;,w.readyState=b&gt;0?4:0,k=b&gt;=200&amp;&amp;300&gt;b||304===b,d&amp;&amp;(v=Wb(l,w,d)),v=Xb(l,v,w,k),k?(l.ifModified&amp;&amp;(x=w.getResponseHeader(&quot;Last-Modified&quot;),x&amp;&amp;(n.lastModified[f]=x),x=w.getResponseHeader(&quot;etag&quot;),x&amp;&amp;(n.etag[f]=x)),204===b||&quot;HEAD&quot;===l.type?y=&quot;nocontent&quot;:304===b?y=&quot;notmodified&quot;:(y=v.state,s=v.data,t=v.error,k=!t)):(t=y,!b&amp;&amp;y||(y=&quot;error&quot;,0&gt;b&amp;&amp;(b=0))),w.status=b,w.statusText=(c||y)+&quot;&quot;,k?p.resolveWith(m,[s,y,w]):p.rejectWith(m,[w,y,t]),w.statusCode(r),r=void 0,i&amp;&amp;o.trigger(k?&quot;ajaxSuccess&quot;:&quot;ajaxError&quot;,[w,l,k?s:t]),q.fireWith(m,[w,y]),i&amp;&amp;(o.trigger(&quot;ajaxComplete&quot;,[w,l]),--n.active||n.event.trigger(&quot;ajaxStop&quot;)))}return w},getJSON:function(a,b,c){return n.get(a,b,c,&quot;json&quot;)},getScript:function(a,b){return n.get(a,void 0,b,&quot;script&quot;)}}),n.each([&quot;get&quot;,&quot;post&quot;],function(a,b){n[b]=function(a,c,d,e){return n.isFunction(c)&amp;&amp;(e=e||d,d=c,c=void 0),n.ajax(n.extend({url:a,type:b,dataType:e,data:c,success:d},n.isPlainObject(a)&amp;&amp;a))}}),n._evalUrl=function(a){return n.ajax({url:a,type:&quot;GET&quot;,dataType:&quot;script&quot;,cache:!0,async:!1,global:!1,&quot;throws&quot;:!0})},n.fn.extend({wrapAll:function(a){if(n.isFunction(a))return this.each(function(b){n(this).wrapAll(a.call(this,b))});if(this[0]){var b=n(a,this[0].ownerDocument).eq(0).clone(!0);this[0].parentNode&amp;&amp;b.insertBefore(this[0]),b.map(function(){var a=this;while(a.firstChild&amp;&amp;1===a.firstChild.nodeType)a=a.firstChild;return a}).append(this)}return this},wrapInner:function(a){return n.isFunction(a)?this.each(function(b){n(this).wrapInner(a.call(this,b))}):this.each(function(){var b=n(this),c=b.contents();c.length?c.wrapAll(a):b.append(a)})},wrap:function(a){var b=n.isFunction(a);return this.each(function(c){n(this).wrapAll(b?a.call(this,c):a)})},unwrap:function(){return this.parent().each(function(){n.nodeName(this,&quot;body&quot;)||n(this).replaceWith(this.childNodes)}).end()}});function Yb(a){return a.style&amp;&amp;a.style.display||n.css(a,&quot;display&quot;)}function Zb(a){if(!n.contains(a.ownerDocument||d,a))return!0;while(a&amp;&amp;1===a.nodeType){if(&quot;none&quot;===Yb(a)||&quot;hidden&quot;===a.type)return!0;a=a.parentNode}return!1}n.expr.filters.hidden=function(a){return l.reliableHiddenOffsets()?a.offsetWidth&lt;=0&amp;&amp;a.offsetHeight&lt;=0&amp;&amp;!a.getClientRects().length:Zb(a)},n.expr.filters.visible=function(a){return!n.expr.filters.hidden(a)};var $b=/%20/g,_b=/\[\]$/,ac=/\r?\n/g,bc=/^(?:submit|button|image|reset|file)$/i,cc=/^(?:input|select|textarea|keygen)/i;function dc(a,b,c,d){var e;if(n.isArray(b))n.each(b,function(b,e){c||_b.test(a)?d(a,e):dc(a+&quot;[&quot;+(&quot;object&quot;==typeof e&amp;&amp;null!=e?b:&quot;&quot;)+&quot;]&quot;,e,c,d)});else if(c||&quot;object&quot;!==n.type(b))d(a,b);else for(e in b)dc(a+&quot;[&quot;+e+&quot;]&quot;,b[e],c,d)}n.param=function(a,b){var c,d=[],e=function(a,b){b=n.isFunction(b)?b():null==b?&quot;&quot;:b,d[d.length]=encodeURIComponent(a)+&quot;=&quot;+encodeURIComponent(b)};if(void 0===b&amp;&amp;(b=n.ajaxSettings&amp;&amp;n.ajaxSettings.traditional),n.isArray(a)||a.jquery&amp;&amp;!n.isPlainObject(a))n.each(a,function(){e(this.name,this.value)});else for(c in a)dc(c,a[c],b,e);return d.join(&quot;&amp;&quot;).replace($b,&quot;+&quot;)},n.fn.extend({serialize:function(){return n.param(this.serializeArray())},serializeArray:function(){return this.map(function(){var a=n.prop(this,&quot;elements&quot;);return a?n.makeArray(a):this}).filter(function(){var a=this.type;return this.name&amp;&amp;!n(this).is(&quot;:disabled&quot;)&amp;&amp;cc.test(this.nodeName)&amp;&amp;!bc.test(a)&amp;&amp;(this.checked||!Z.test(a))}).map(function(a,b){var c=n(this).val();return null==c?null:n.isArray(c)?n.map(c,function(a){return{name:b.name,value:a.replace(ac,&quot;\r\n&quot;)}}):{name:b.name,value:c.replace(ac,&quot;\r\n&quot;)}}).get()}}),n.ajaxSettings.xhr=void 0!==a.ActiveXObject?function(){return this.isLocal?ic():d.documentMode&gt;8?hc():/^(get|post|head|put|delete|options)$/i.test(this.type)&amp;&amp;hc()||ic()}:hc;var ec=0,fc={},gc=n.ajaxSettings.xhr();a.attachEvent&amp;&amp;a.attachEvent(&quot;onunload&quot;,function(){for(var a in fc)fc[a](void 0,!0)}),l.cors=!!gc&amp;&amp;&quot;withCredentials&quot;in gc,gc=l.ajax=!!gc,gc&amp;&amp;n.ajaxTransport(function(b){if(!b.crossDomain||l.cors){var c;return{send:function(d,e){var f,g=b.xhr(),h=++ec;if(g.open(b.type,b.url,b.async,b.username,b.password),b.xhrFields)for(f in b.xhrFields)g[f]=b.xhrFields[f];b.mimeType&amp;&amp;g.overrideMimeType&amp;&amp;g.overrideMimeType(b.mimeType),b.crossDomain||d[&quot;X-Requested-With&quot;]||(d[&quot;X-Requested-With&quot;]=&quot;XMLHttpRequest&quot;);for(f in d)void 0!==d[f]&amp;&amp;g.setRequestHeader(f,d[f]+&quot;&quot;);g.send(b.hasContent&amp;&amp;b.data||null),c=function(a,d){var f,i,j;if(c&amp;&amp;(d||4===g.readyState))if(delete fc[h],c=void 0,g.onreadystatechange=n.noop,d)4!==g.readyState&amp;&amp;g.abort();else{j={},f=g.status,&quot;string&quot;==typeof g.responseText&amp;&amp;(j.text=g.responseText);try{i=g.statusText}catch(k){i=&quot;&quot;}f||!b.isLocal||b.crossDomain?1223===f&amp;&amp;(f=204):f=j.text?200:404}j&amp;&amp;e(f,i,j,g.getAllResponseHeaders())},b.async?4===g.readyState?a.setTimeout(c):g.onreadystatechange=fc[h]=c:c()},abort:function(){c&amp;&amp;c(void 0,!0)}}}});function hc(){try{return new a.XMLHttpRequest}catch(b){}}function ic(){try{return new a.ActiveXObject(&quot;Microsoft.XMLHTTP&quot;)}catch(b){}}n.ajaxSetup({accepts:{script:&quot;text/javascript, application/javascript, application/ecmascript, application/x-ecmascript&quot;},contents:{script:/\b(?:java|ecma)script\b/},converters:{&quot;text script&quot;:function(a){return n.globalEval(a),a}}}),n.ajaxPrefilter(&quot;script&quot;,function(a){void 0===a.cache&amp;&amp;(a.cache=!1),a.crossDomain&amp;&amp;(a.type=&quot;GET&quot;,a.global=!1)}),n.ajaxTransport(&quot;script&quot;,function(a){if(a.crossDomain){var b,c=d.head||n(&quot;head&quot;)[0]||d.documentElement;return{send:function(e,f){b=d.createElement(&quot;script&quot;),b.async=!0,a.scriptCharset&amp;&amp;(b.charset=a.scriptCharset),b.src=a.url,b.onload=b.onreadystatechange=function(a,c){(c||!b.readyState||/loaded|complete/.test(b.readyState))&amp;&amp;(b.onload=b.onreadystatechange=null,b.parentNode&amp;&amp;b.parentNode.removeChild(b),b=null,c||f(200,&quot;success&quot;))},c.insertBefore(b,c.firstChild)},abort:function(){b&amp;&amp;b.onload(void 0,!0)}}}});var jc=[],kc=/(=)\?(?=&amp;|$)|\?\?/;n.ajaxSetup({jsonp:&quot;callback&quot;,jsonpCallback:function(){var a=jc.pop()||n.expando+&quot;_&quot;+Eb++;return this[a]=!0,a}}),n.ajaxPrefilter(&quot;json jsonp&quot;,function(b,c,d){var e,f,g,h=b.jsonp!==!1&amp;&amp;(kc.test(b.url)?&quot;url&quot;:&quot;string&quot;==typeof b.data&amp;&amp;0===(b.contentType||&quot;&quot;).indexOf(&quot;application/x-www-form-urlencoded&quot;)&amp;&amp;kc.test(b.data)&amp;&amp;&quot;data&quot;);return h||&quot;jsonp&quot;===b.dataTypes[0]?(e=b.jsonpCallback=n.isFunction(b.jsonpCallback)?b.jsonpCallback():b.jsonpCallback,h?b[h]=b[h].replace(kc,&quot;$1&quot;+e):b.jsonp!==!1&amp;&amp;(b.url+=(Fb.test(b.url)?&quot;&amp;&quot;:&quot;?&quot;)+b.jsonp+&quot;=&quot;+e),b.converters[&quot;script json&quot;]=function(){return g||n.error(e+&quot; was not called&quot;),g[0]},b.dataTypes[0]=&quot;json&quot;,f=a[e],a[e]=function(){g=arguments},d.always(function(){void 0===f?n(a).removeProp(e):a[e]=f,b[e]&amp;&amp;(b.jsonpCallback=c.jsonpCallback,jc.push(e)),g&amp;&amp;n.isFunction(f)&amp;&amp;f(g[0]),g=f=void 0}),&quot;script&quot;):void 0}),n.parseHTML=function(a,b,c){if(!a||&quot;string&quot;!=typeof a)return null;&quot;boolean&quot;==typeof b&amp;&amp;(c=b,b=!1),b=b||d;var e=x.exec(a),f=!c&amp;&amp;[];return e?[b.createElement(e[1])]:(e=ja([a],b,f),f&amp;&amp;f.length&amp;&amp;n(f).remove(),n.merge([],e.childNodes))};var lc=n.fn.load;n.fn.load=function(a,b,c){if(&quot;string&quot;!=typeof a&amp;&amp;lc)return lc.apply(this,arguments);var d,e,f,g=this,h=a.indexOf(&quot; &quot;);return h&gt;-1&amp;&amp;(d=n.trim(a.slice(h,a.length)),a=a.slice(0,h)),n.isFunction(b)?(c=b,b=void 0):b&amp;&amp;&quot;object&quot;==typeof b&amp;&amp;(e=&quot;POST&quot;),g.length&gt;0&amp;&amp;n.ajax({url:a,type:e||&quot;GET&quot;,dataType:&quot;html&quot;,data:b}).done(function(a){f=arguments,g.html(d?n(&quot;&lt;div&gt;&quot;).append(n.parseHTML(a)).find(d):a)}).always(c&amp;&amp;function(a,b){g.each(function(){c.apply(this,f||[a.responseText,b,a])})}),this},n.each([&quot;ajaxStart&quot;,&quot;ajaxStop&quot;,&quot;ajaxComplete&quot;,&quot;ajaxError&quot;,&quot;ajaxSuccess&quot;,&quot;ajaxSend&quot;],function(a,b){n.fn[b]=function(a){return this.on(b,a)}}),n.expr.filters.animated=function(a){return n.grep(n.timers,function(b){return a===b.elem}).length};function mc(a){return n.isWindow(a)?a:9===a.nodeType?a.defaultView||a.parentWindow:!1}n.offset={setOffset:function(a,b,c){var d,e,f,g,h,i,j,k=n.css(a,&quot;position&quot;),l=n(a),m={};&quot;static&quot;===k&amp;&amp;(a.style.position=&quot;relative&quot;),h=l.offset(),f=n.css(a,&quot;top&quot;),i=n.css(a,&quot;left&quot;),j=(&quot;absolute&quot;===k||&quot;fixed&quot;===k)&amp;&amp;n.inArray(&quot;auto&quot;,[f,i])&gt;-1,j?(d=l.position(),g=d.top,e=d.left):(g=parseFloat(f)||0,e=parseFloat(i)||0),n.isFunction(b)&amp;&amp;(b=b.call(a,c,n.extend({},h))),null!=b.top&amp;&amp;(m.top=b.top-h.top+g),null!=b.left&amp;&amp;(m.left=b.left-h.left+e),&quot;using&quot;in b?b.using.call(a,m):l.css(m)}},n.fn.extend({offset:function(a){if(arguments.length)return void 0===a?this:this.each(function(b){n.offset.setOffset(this,a,b)});var b,c,d={top:0,left:0},e=this[0],f=e&amp;&amp;e.ownerDocument;if(f)return b=f.documentElement,n.contains(b,e)?(&quot;undefined&quot;!=typeof e.getBoundingClientRect&amp;&amp;(d=e.getBoundingClientRect()),c=mc(f),{top:d.top+(c.pageYOffset||b.scrollTop)-(b.clientTop||0),left:d.left+(c.pageXOffset||b.scrollLeft)-(b.clientLeft||0)}):d},position:function(){if(this[0]){var a,b,c={top:0,left:0},d=this[0];return&quot;fixed&quot;===n.css(d,&quot;position&quot;)?b=d.getBoundingClientRect():(a=this.offsetParent(),b=this.offset(),n.nodeName(a[0],&quot;html&quot;)||(c=a.offset()),c.top+=n.css(a[0],&quot;borderTopWidth&quot;,!0),c.left+=n.css(a[0],&quot;borderLeftWidth&quot;,!0)),{top:b.top-c.top-n.css(d,&quot;marginTop&quot;,!0),left:b.left-c.left-n.css(d,&quot;marginLeft&quot;,!0)}}},offsetParent:function(){return this.map(function(){var a=this.offsetParent;while(a&amp;&amp;!n.nodeName(a,&quot;html&quot;)&amp;&amp;&quot;static&quot;===n.css(a,&quot;position&quot;))a=a.offsetParent;return a||Qa})}}),n.each({scrollLeft:&quot;pageXOffset&quot;,scrollTop:&quot;pageYOffset&quot;},function(a,b){var c=/Y/.test(b);n.fn[a]=function(d){return Y(this,function(a,d,e){var f=mc(a);return void 0===e?f?b in f?f[b]:f.document.documentElement[d]:a[d]:void(f?f.scrollTo(c?n(f).scrollLeft():e,c?e:n(f).scrollTop()):a[d]=e)},a,d,arguments.length,null)}}),n.each([&quot;top&quot;,&quot;left&quot;],function(a,b){n.cssHooks[b]=Ua(l.pixelPosition,function(a,c){return c?(c=Sa(a,b),Oa.test(c)?n(a).position()[b]+&quot;px&quot;:c):void 0})}),n.each({Height:&quot;height&quot;,Width:&quot;width&quot;},function(a,b){n.each({
padding:&quot;inner&quot;+a,content:b,&quot;&quot;:&quot;outer&quot;+a},function(c,d){n.fn[d]=function(d,e){var f=arguments.length&amp;&amp;(c||&quot;boolean&quot;!=typeof d),g=c||(d===!0||e===!0?&quot;margin&quot;:&quot;border&quot;);return Y(this,function(b,c,d){var e;return n.isWindow(b)?b.document.documentElement[&quot;client&quot;+a]:9===b.nodeType?(e=b.documentElement,Math.max(b.body[&quot;scroll&quot;+a],e[&quot;scroll&quot;+a],b.body[&quot;offset&quot;+a],e[&quot;offset&quot;+a],e[&quot;client&quot;+a])):void 0===d?n.css(b,c,g):n.style(b,c,d,g)},b,f?d:void 0,f,null)}})}),n.fn.extend({bind:function(a,b,c){return this.on(a,null,b,c)},unbind:function(a,b){return this.off(a,null,b)},delegate:function(a,b,c,d){return this.on(b,a,c,d)},undelegate:function(a,b,c){return 1===arguments.length?this.off(a,&quot;**&quot;):this.off(b,a||&quot;**&quot;,c)}}),n.fn.size=function(){return this.length},n.fn.andSelf=n.fn.addBack,&quot;function&quot;==typeof define&amp;&amp;define.amd&amp;&amp;define(&quot;jquery&quot;,[],function(){return n});var nc=a.jQuery,oc=a.$;return n.noConflict=function(b){return a.$===n&amp;&amp;(a.$=oc),b&amp;&amp;a.jQuery===n&amp;&amp;(a.jQuery=nc),n},b||(a.jQuery=a.$=n),n});/*!
 * Bootstrap v3.3.7 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under the MIT license
 */
if(&quot;undefined&quot;==typeof jQuery)throw new Error(&quot;Bootstrap&#x27;s JavaScript requires jQuery&quot;);+function(a){&quot;use strict&quot;;var b=a.fn.jquery.split(&quot; &quot;)[0].split(&quot;.&quot;);if(b[0]&lt;2&amp;&amp;b[1]&lt;9||1==b[0]&amp;&amp;9==b[1]&amp;&amp;b[2]&lt;1||b[0]&gt;3)throw new Error(&quot;Bootstrap&#x27;s JavaScript requires jQuery version 1.9.1 or higher, but lower than version 4&quot;)}(jQuery),+function(a){&quot;use strict&quot;;function b(){var a=document.createElement(&quot;bootstrap&quot;),b={WebkitTransition:&quot;webkitTransitionEnd&quot;,MozTransition:&quot;transitionend&quot;,OTransition:&quot;oTransitionEnd otransitionend&quot;,transition:&quot;transitionend&quot;};for(var c in b)if(void 0!==a.style[c])return{end:b[c]};return!1}a.fn.emulateTransitionEnd=function(b){var c=!1,d=this;a(this).one(&quot;bsTransitionEnd&quot;,function(){c=!0});var e=function(){c||a(d).trigger(a.support.transition.end)};return setTimeout(e,b),this},a(function(){a.support.transition=b(),a.support.transition&amp;&amp;(a.event.special.bsTransitionEnd={bindType:a.support.transition.end,delegateType:a.support.transition.end,handle:function(b){if(a(b.target).is(this))return b.handleObj.handler.apply(this,arguments)}})})}(jQuery),+function(a){&quot;use strict&quot;;function b(b){return this.each(function(){var c=a(this),e=c.data(&quot;bs.alert&quot;);e||c.data(&quot;bs.alert&quot;,e=new d(this)),&quot;string&quot;==typeof b&amp;&amp;e[b].call(c)})}var c=&#x27;[data-dismiss=&quot;alert&quot;]&#x27;,d=function(b){a(b).on(&quot;click&quot;,c,this.close)};d.VERSION=&quot;3.3.7&quot;,d.TRANSITION_DURATION=150,d.prototype.close=function(b){function c(){g.detach().trigger(&quot;closed.bs.alert&quot;).remove()}var e=a(this),f=e.attr(&quot;data-target&quot;);f||(f=e.attr(&quot;href&quot;),f=f&amp;&amp;f.replace(/.*(?=#[^\s]*$)/,&quot;&quot;));var g=a(&quot;#&quot;===f?[]:f);b&amp;&amp;b.preventDefault(),g.length||(g=e.closest(&quot;.alert&quot;)),g.trigger(b=a.Event(&quot;close.bs.alert&quot;)),b.isDefaultPrevented()||(g.removeClass(&quot;in&quot;),a.support.transition&amp;&amp;g.hasClass(&quot;fade&quot;)?g.one(&quot;bsTransitionEnd&quot;,c).emulateTransitionEnd(d.TRANSITION_DURATION):c())};var e=a.fn.alert;a.fn.alert=b,a.fn.alert.Constructor=d,a.fn.alert.noConflict=function(){return a.fn.alert=e,this},a(document).on(&quot;click.bs.alert.data-api&quot;,c,d.prototype.close)}(jQuery),+function(a){&quot;use strict&quot;;function b(b){return this.each(function(){var d=a(this),e=d.data(&quot;bs.button&quot;),f=&quot;object&quot;==typeof b&amp;&amp;b;e||d.data(&quot;bs.button&quot;,e=new c(this,f)),&quot;toggle&quot;==b?e.toggle():b&amp;&amp;e.setState(b)})}var c=function(b,d){this.$element=a(b),this.options=a.extend({},c.DEFAULTS,d),this.isLoading=!1};c.VERSION=&quot;3.3.7&quot;,c.DEFAULTS={loadingText:&quot;loading...&quot;},c.prototype.setState=function(b){var c=&quot;disabled&quot;,d=this.$element,e=d.is(&quot;input&quot;)?&quot;val&quot;:&quot;html&quot;,f=d.data();b+=&quot;Text&quot;,null==f.resetText&amp;&amp;d.data(&quot;resetText&quot;,d[e]()),setTimeout(a.proxy(function(){d[e](null==f[b]?this.options[b]:f[b]),&quot;loadingText&quot;==b?(this.isLoading=!0,d.addClass(c).attr(c,c).prop(c,!0)):this.isLoading&amp;&amp;(this.isLoading=!1,d.removeClass(c).removeAttr(c).prop(c,!1))},this),0)},c.prototype.toggle=function(){var a=!0,b=this.$element.closest(&#x27;[data-toggle=&quot;buttons&quot;]&#x27;);if(b.length){var c=this.$element.find(&quot;input&quot;);&quot;radio&quot;==c.prop(&quot;type&quot;)?(c.prop(&quot;checked&quot;)&amp;&amp;(a=!1),b.find(&quot;.active&quot;).removeClass(&quot;active&quot;),this.$element.addClass(&quot;active&quot;)):&quot;checkbox&quot;==c.prop(&quot;type&quot;)&amp;&amp;(c.prop(&quot;checked&quot;)!==this.$element.hasClass(&quot;active&quot;)&amp;&amp;(a=!1),this.$element.toggleClass(&quot;active&quot;)),c.prop(&quot;checked&quot;,this.$element.hasClass(&quot;active&quot;)),a&amp;&amp;c.trigger(&quot;change&quot;)}else this.$element.attr(&quot;aria-pressed&quot;,!this.$element.hasClass(&quot;active&quot;)),this.$element.toggleClass(&quot;active&quot;)};var d=a.fn.button;a.fn.button=b,a.fn.button.Constructor=c,a.fn.button.noConflict=function(){return a.fn.button=d,this},a(document).on(&quot;click.bs.button.data-api&quot;,&#x27;[data-toggle^=&quot;button&quot;]&#x27;,function(c){var d=a(c.target).closest(&quot;.btn&quot;);b.call(d,&quot;toggle&quot;),a(c.target).is(&#x27;input[type=&quot;radio&quot;], input[type=&quot;checkbox&quot;]&#x27;)||(c.preventDefault(),d.is(&quot;input,button&quot;)?d.trigger(&quot;focus&quot;):d.find(&quot;input:visible,button:visible&quot;).first().trigger(&quot;focus&quot;))}).on(&quot;focus.bs.button.data-api blur.bs.button.data-api&quot;,&#x27;[data-toggle^=&quot;button&quot;]&#x27;,function(b){a(b.target).closest(&quot;.btn&quot;).toggleClass(&quot;focus&quot;,/^focus(in)?$/.test(b.type))})}(jQuery),+function(a){&quot;use strict&quot;;function b(b){return this.each(function(){var d=a(this),e=d.data(&quot;bs.carousel&quot;),f=a.extend({},c.DEFAULTS,d.data(),&quot;object&quot;==typeof b&amp;&amp;b),g=&quot;string&quot;==typeof b?b:f.slide;e||d.data(&quot;bs.carousel&quot;,e=new c(this,f)),&quot;number&quot;==typeof b?e.to(b):g?e[g]():f.interval&amp;&amp;e.pause().cycle()})}var c=function(b,c){this.$element=a(b),this.$indicators=this.$element.find(&quot;.carousel-indicators&quot;),this.options=c,this.paused=null,this.sliding=null,this.interval=null,this.$active=null,this.$items=null,this.options.keyboard&amp;&amp;this.$element.on(&quot;keydown.bs.carousel&quot;,a.proxy(this.keydown,this)),&quot;hover&quot;==this.options.pause&amp;&amp;!(&quot;ontouchstart&quot;in document.documentElement)&amp;&amp;this.$element.on(&quot;mouseenter.bs.carousel&quot;,a.proxy(this.pause,this)).on(&quot;mouseleave.bs.carousel&quot;,a.proxy(this.cycle,this))};c.VERSION=&quot;3.3.7&quot;,c.TRANSITION_DURATION=600,c.DEFAULTS={interval:5e3,pause:&quot;hover&quot;,wrap:!0,keyboard:!0},c.prototype.keydown=function(a){if(!/input|textarea/i.test(a.target.tagName)){switch(a.which){case 37:this.prev();break;case 39:this.next();break;default:return}a.preventDefault()}},c.prototype.cycle=function(b){return b||(this.paused=!1),this.interval&amp;&amp;clearInterval(this.interval),this.options.interval&amp;&amp;!this.paused&amp;&amp;(this.interval=setInterval(a.proxy(this.next,this),this.options.interval)),this},c.prototype.getItemIndex=function(a){return this.$items=a.parent().children(&quot;.item&quot;),this.$items.index(a||this.$active)},c.prototype.getItemForDirection=function(a,b){var c=this.getItemIndex(b),d=&quot;prev&quot;==a&amp;&amp;0===c||&quot;next&quot;==a&amp;&amp;c==this.$items.length-1;if(d&amp;&amp;!this.options.wrap)return b;var e=&quot;prev&quot;==a?-1:1,f=(c+e)%this.$items.length;return this.$items.eq(f)},c.prototype.to=function(a){var b=this,c=this.getItemIndex(this.$active=this.$element.find(&quot;.item.active&quot;));if(!(a&gt;this.$items.length-1||a&lt;0))return this.sliding?this.$element.one(&quot;slid.bs.carousel&quot;,function(){b.to(a)}):c==a?this.pause().cycle():this.slide(a&gt;c?&quot;next&quot;:&quot;prev&quot;,this.$items.eq(a))},c.prototype.pause=function(b){return b||(this.paused=!0),this.$element.find(&quot;.next, .prev&quot;).length&amp;&amp;a.support.transition&amp;&amp;(this.$element.trigger(a.support.transition.end),this.cycle(!0)),this.interval=clearInterval(this.interval),this},c.prototype.next=function(){if(!this.sliding)return this.slide(&quot;next&quot;)},c.prototype.prev=function(){if(!this.sliding)return this.slide(&quot;prev&quot;)},c.prototype.slide=function(b,d){var e=this.$element.find(&quot;.item.active&quot;),f=d||this.getItemForDirection(b,e),g=this.interval,h=&quot;next&quot;==b?&quot;left&quot;:&quot;right&quot;,i=this;if(f.hasClass(&quot;active&quot;))return this.sliding=!1;var j=f[0],k=a.Event(&quot;slide.bs.carousel&quot;,{relatedTarget:j,direction:h});if(this.$element.trigger(k),!k.isDefaultPrevented()){if(this.sliding=!0,g&amp;&amp;this.pause(),this.$indicators.length){this.$indicators.find(&quot;.active&quot;).removeClass(&quot;active&quot;);var l=a(this.$indicators.children()[this.getItemIndex(f)]);l&amp;&amp;l.addClass(&quot;active&quot;)}var m=a.Event(&quot;slid.bs.carousel&quot;,{relatedTarget:j,direction:h});return a.support.transition&amp;&amp;this.$element.hasClass(&quot;slide&quot;)?(f.addClass(b),f[0].offsetWidth,e.addClass(h),f.addClass(h),e.one(&quot;bsTransitionEnd&quot;,function(){f.removeClass([b,h].join(&quot; &quot;)).addClass(&quot;active&quot;),e.removeClass([&quot;active&quot;,h].join(&quot; &quot;)),i.sliding=!1,setTimeout(function(){i.$element.trigger(m)},0)}).emulateTransitionEnd(c.TRANSITION_DURATION)):(e.removeClass(&quot;active&quot;),f.addClass(&quot;active&quot;),this.sliding=!1,this.$element.trigger(m)),g&amp;&amp;this.cycle(),this}};var d=a.fn.carousel;a.fn.carousel=b,a.fn.carousel.Constructor=c,a.fn.carousel.noConflict=function(){return a.fn.carousel=d,this};var e=function(c){var d,e=a(this),f=a(e.attr(&quot;data-target&quot;)||(d=e.attr(&quot;href&quot;))&amp;&amp;d.replace(/.*(?=#[^\s]+$)/,&quot;&quot;));if(f.hasClass(&quot;carousel&quot;)){var g=a.extend({},f.data(),e.data()),h=e.attr(&quot;data-slide-to&quot;);h&amp;&amp;(g.interval=!1),b.call(f,g),h&amp;&amp;f.data(&quot;bs.carousel&quot;).to(h),c.preventDefault()}};a(document).on(&quot;click.bs.carousel.data-api&quot;,&quot;[data-slide]&quot;,e).on(&quot;click.bs.carousel.data-api&quot;,&quot;[data-slide-to]&quot;,e),a(window).on(&quot;load&quot;,function(){a(&#x27;[data-ride=&quot;carousel&quot;]&#x27;).each(function(){var c=a(this);b.call(c,c.data())})})}(jQuery),+function(a){&quot;use strict&quot;;function b(b){var c,d=b.attr(&quot;data-target&quot;)||(c=b.attr(&quot;href&quot;))&amp;&amp;c.replace(/.*(?=#[^\s]+$)/,&quot;&quot;);return a(d)}function c(b){return this.each(function(){var c=a(this),e=c.data(&quot;bs.collapse&quot;),f=a.extend({},d.DEFAULTS,c.data(),&quot;object&quot;==typeof b&amp;&amp;b);!e&amp;&amp;f.toggle&amp;&amp;/show|hide/.test(b)&amp;&amp;(f.toggle=!1),e||c.data(&quot;bs.collapse&quot;,e=new d(this,f)),&quot;string&quot;==typeof b&amp;&amp;e[b]()})}var d=function(b,c){this.$element=a(b),this.options=a.extend({},d.DEFAULTS,c),this.$trigger=a(&#x27;[data-toggle=&quot;collapse&quot;][href=&quot;#&#x27;+b.id+&#x27;&quot;],[data-toggle=&quot;collapse&quot;][data-target=&quot;#&#x27;+b.id+&#x27;&quot;]&#x27;),this.transitioning=null,this.options.parent?this.$parent=this.getParent():this.addAriaAndCollapsedClass(this.$element,this.$trigger),this.options.toggle&amp;&amp;this.toggle()};d.VERSION=&quot;3.3.7&quot;,d.TRANSITION_DURATION=350,d.DEFAULTS={toggle:!0},d.prototype.dimension=function(){var a=this.$element.hasClass(&quot;width&quot;);return a?&quot;width&quot;:&quot;height&quot;},d.prototype.show=function(){if(!this.transitioning&amp;&amp;!this.$element.hasClass(&quot;in&quot;)){var b,e=this.$parent&amp;&amp;this.$parent.children(&quot;.panel&quot;).children(&quot;.in, .collapsing&quot;);if(!(e&amp;&amp;e.length&amp;&amp;(b=e.data(&quot;bs.collapse&quot;),b&amp;&amp;b.transitioning))){var f=a.Event(&quot;show.bs.collapse&quot;);if(this.$element.trigger(f),!f.isDefaultPrevented()){e&amp;&amp;e.length&amp;&amp;(c.call(e,&quot;hide&quot;),b||e.data(&quot;bs.collapse&quot;,null));var g=this.dimension();this.$element.removeClass(&quot;collapse&quot;).addClass(&quot;collapsing&quot;)[g](0).attr(&quot;aria-expanded&quot;,!0),this.$trigger.removeClass(&quot;collapsed&quot;).attr(&quot;aria-expanded&quot;,!0),this.transitioning=1;var h=function(){this.$element.removeClass(&quot;collapsing&quot;).addClass(&quot;collapse in&quot;)[g](&quot;&quot;),this.transitioning=0,this.$element.trigger(&quot;shown.bs.collapse&quot;)};if(!a.support.transition)return h.call(this);var i=a.camelCase([&quot;scroll&quot;,g].join(&quot;-&quot;));this.$element.one(&quot;bsTransitionEnd&quot;,a.proxy(h,this)).emulateTransitionEnd(d.TRANSITION_DURATION)[g](this.$element[0][i])}}}},d.prototype.hide=function(){if(!this.transitioning&amp;&amp;this.$element.hasClass(&quot;in&quot;)){var b=a.Event(&quot;hide.bs.collapse&quot;);if(this.$element.trigger(b),!b.isDefaultPrevented()){var c=this.dimension();this.$element[c](this.$element[c]())[0].offsetHeight,this.$element.addClass(&quot;collapsing&quot;).removeClass(&quot;collapse in&quot;).attr(&quot;aria-expanded&quot;,!1),this.$trigger.addClass(&quot;collapsed&quot;).attr(&quot;aria-expanded&quot;,!1),this.transitioning=1;var e=function(){this.transitioning=0,this.$element.removeClass(&quot;collapsing&quot;).addClass(&quot;collapse&quot;).trigger(&quot;hidden.bs.collapse&quot;)};return a.support.transition?void this.$element[c](0).one(&quot;bsTransitionEnd&quot;,a.proxy(e,this)).emulateTransitionEnd(d.TRANSITION_DURATION):e.call(this)}}},d.prototype.toggle=function(){this[this.$element.hasClass(&quot;in&quot;)?&quot;hide&quot;:&quot;show&quot;]()},d.prototype.getParent=function(){return a(this.options.parent).find(&#x27;[data-toggle=&quot;collapse&quot;][data-parent=&quot;&#x27;+this.options.parent+&#x27;&quot;]&#x27;).each(a.proxy(function(c,d){var e=a(d);this.addAriaAndCollapsedClass(b(e),e)},this)).end()},d.prototype.addAriaAndCollapsedClass=function(a,b){var c=a.hasClass(&quot;in&quot;);a.attr(&quot;aria-expanded&quot;,c),b.toggleClass(&quot;collapsed&quot;,!c).attr(&quot;aria-expanded&quot;,c)};var e=a.fn.collapse;a.fn.collapse=c,a.fn.collapse.Constructor=d,a.fn.collapse.noConflict=function(){return a.fn.collapse=e,this},a(document).on(&quot;click.bs.collapse.data-api&quot;,&#x27;[data-toggle=&quot;collapse&quot;]&#x27;,function(d){var e=a(this);e.attr(&quot;data-target&quot;)||d.preventDefault();var f=b(e),g=f.data(&quot;bs.collapse&quot;),h=g?&quot;toggle&quot;:e.data();c.call(f,h)})}(jQuery),+function(a){&quot;use strict&quot;;function b(b){var c=b.attr(&quot;data-target&quot;);c||(c=b.attr(&quot;href&quot;),c=c&amp;&amp;/#[A-Za-z]/.test(c)&amp;&amp;c.replace(/.*(?=#[^\s]*$)/,&quot;&quot;));var d=c&amp;&amp;a(c);return d&amp;&amp;d.length?d:b.parent()}function c(c){c&amp;&amp;3===c.which||(a(e).remove(),a(f).each(function(){var d=a(this),e=b(d),f={relatedTarget:this};e.hasClass(&quot;open&quot;)&amp;&amp;(c&amp;&amp;&quot;click&quot;==c.type&amp;&amp;/input|textarea/i.test(c.target.tagName)&amp;&amp;a.contains(e[0],c.target)||(e.trigger(c=a.Event(&quot;hide.bs.dropdown&quot;,f)),c.isDefaultPrevented()||(d.attr(&quot;aria-expanded&quot;,&quot;false&quot;),e.removeClass(&quot;open&quot;).trigger(a.Event(&quot;hidden.bs.dropdown&quot;,f)))))}))}function d(b){return this.each(function(){var c=a(this),d=c.data(&quot;bs.dropdown&quot;);d||c.data(&quot;bs.dropdown&quot;,d=new g(this)),&quot;string&quot;==typeof b&amp;&amp;d[b].call(c)})}var e=&quot;.dropdown-backdrop&quot;,f=&#x27;[data-toggle=&quot;dropdown&quot;]&#x27;,g=function(b){a(b).on(&quot;click.bs.dropdown&quot;,this.toggle)};g.VERSION=&quot;3.3.7&quot;,g.prototype.toggle=function(d){var e=a(this);if(!e.is(&quot;.disabled, :disabled&quot;)){var f=b(e),g=f.hasClass(&quot;open&quot;);if(c(),!g){&quot;ontouchstart&quot;in document.documentElement&amp;&amp;!f.closest(&quot;.navbar-nav&quot;).length&amp;&amp;a(document.createElement(&quot;div&quot;)).addClass(&quot;dropdown-backdrop&quot;).insertAfter(a(this)).on(&quot;click&quot;,c);var h={relatedTarget:this};if(f.trigger(d=a.Event(&quot;show.bs.dropdown&quot;,h)),d.isDefaultPrevented())return;e.trigger(&quot;focus&quot;).attr(&quot;aria-expanded&quot;,&quot;true&quot;),f.toggleClass(&quot;open&quot;).trigger(a.Event(&quot;shown.bs.dropdown&quot;,h))}return!1}},g.prototype.keydown=function(c){if(/(38|40|27|32)/.test(c.which)&amp;&amp;!/input|textarea/i.test(c.target.tagName)){var d=a(this);if(c.preventDefault(),c.stopPropagation(),!d.is(&quot;.disabled, :disabled&quot;)){var e=b(d),g=e.hasClass(&quot;open&quot;);if(!g&amp;&amp;27!=c.which||g&amp;&amp;27==c.which)return 27==c.which&amp;&amp;e.find(f).trigger(&quot;focus&quot;),d.trigger(&quot;click&quot;);var h=&quot; li:not(.disabled):visible a&quot;,i=e.find(&quot;.dropdown-menu&quot;+h);if(i.length){var j=i.index(c.target);38==c.which&amp;&amp;j&gt;0&amp;&amp;j--,40==c.which&amp;&amp;j&lt;i.length-1&amp;&amp;j++,~j||(j=0),i.eq(j).trigger(&quot;focus&quot;)}}}};var h=a.fn.dropdown;a.fn.dropdown=d,a.fn.dropdown.Constructor=g,a.fn.dropdown.noConflict=function(){return a.fn.dropdown=h,this},a(document).on(&quot;click.bs.dropdown.data-api&quot;,c).on(&quot;click.bs.dropdown.data-api&quot;,&quot;.dropdown form&quot;,function(a){a.stopPropagation()}).on(&quot;click.bs.dropdown.data-api&quot;,f,g.prototype.toggle).on(&quot;keydown.bs.dropdown.data-api&quot;,f,g.prototype.keydown).on(&quot;keydown.bs.dropdown.data-api&quot;,&quot;.dropdown-menu&quot;,g.prototype.keydown)}(jQuery),+function(a){&quot;use strict&quot;;function b(b,d){return this.each(function(){var e=a(this),f=e.data(&quot;bs.modal&quot;),g=a.extend({},c.DEFAULTS,e.data(),&quot;object&quot;==typeof b&amp;&amp;b);f||e.data(&quot;bs.modal&quot;,f=new c(this,g)),&quot;string&quot;==typeof b?f[b](d):g.show&amp;&amp;f.show(d)})}var c=function(b,c){this.options=c,this.$body=a(document.body),this.$element=a(b),this.$dialog=this.$element.find(&quot;.modal-dialog&quot;),this.$backdrop=null,this.isShown=null,this.originalBodyPad=null,this.scrollbarWidth=0,this.ignoreBackdropClick=!1,this.options.remote&amp;&amp;this.$element.find(&quot;.modal-content&quot;).load(this.options.remote,a.proxy(function(){this.$element.trigger(&quot;loaded.bs.modal&quot;)},this))};c.VERSION=&quot;3.3.7&quot;,c.TRANSITION_DURATION=300,c.BACKDROP_TRANSITION_DURATION=150,c.DEFAULTS={backdrop:!0,keyboard:!0,show:!0},c.prototype.toggle=function(a){return this.isShown?this.hide():this.show(a)},c.prototype.show=function(b){var d=this,e=a.Event(&quot;show.bs.modal&quot;,{relatedTarget:b});this.$element.trigger(e),this.isShown||e.isDefaultPrevented()||(this.isShown=!0,this.checkScrollbar(),this.setScrollbar(),this.$body.addClass(&quot;modal-open&quot;),this.escape(),this.resize(),this.$element.on(&quot;click.dismiss.bs.modal&quot;,&#x27;[data-dismiss=&quot;modal&quot;]&#x27;,a.proxy(this.hide,this)),this.$dialog.on(&quot;mousedown.dismiss.bs.modal&quot;,function(){d.$element.one(&quot;mouseup.dismiss.bs.modal&quot;,function(b){a(b.target).is(d.$element)&amp;&amp;(d.ignoreBackdropClick=!0)})}),this.backdrop(function(){var e=a.support.transition&amp;&amp;d.$element.hasClass(&quot;fade&quot;);d.$element.parent().length||d.$element.appendTo(d.$body),d.$element.show().scrollTop(0),d.adjustDialog(),e&amp;&amp;d.$element[0].offsetWidth,d.$element.addClass(&quot;in&quot;),d.enforceFocus();var f=a.Event(&quot;shown.bs.modal&quot;,{relatedTarget:b});e?d.$dialog.one(&quot;bsTransitionEnd&quot;,function(){d.$element.trigger(&quot;focus&quot;).trigger(f)}).emulateTransitionEnd(c.TRANSITION_DURATION):d.$element.trigger(&quot;focus&quot;).trigger(f)}))},c.prototype.hide=function(b){b&amp;&amp;b.preventDefault(),b=a.Event(&quot;hide.bs.modal&quot;),this.$element.trigger(b),this.isShown&amp;&amp;!b.isDefaultPrevented()&amp;&amp;(this.isShown=!1,this.escape(),this.resize(),a(document).off(&quot;focusin.bs.modal&quot;),this.$element.removeClass(&quot;in&quot;).off(&quot;click.dismiss.bs.modal&quot;).off(&quot;mouseup.dismiss.bs.modal&quot;),this.$dialog.off(&quot;mousedown.dismiss.bs.modal&quot;),a.support.transition&amp;&amp;this.$element.hasClass(&quot;fade&quot;)?this.$element.one(&quot;bsTransitionEnd&quot;,a.proxy(this.hideModal,this)).emulateTransitionEnd(c.TRANSITION_DURATION):this.hideModal())},c.prototype.enforceFocus=function(){a(document).off(&quot;focusin.bs.modal&quot;).on(&quot;focusin.bs.modal&quot;,a.proxy(function(a){document===a.target||this.$element[0]===a.target||this.$element.has(a.target).length||this.$element.trigger(&quot;focus&quot;)},this))},c.prototype.escape=function(){this.isShown&amp;&amp;this.options.keyboard?this.$element.on(&quot;keydown.dismiss.bs.modal&quot;,a.proxy(function(a){27==a.which&amp;&amp;this.hide()},this)):this.isShown||this.$element.off(&quot;keydown.dismiss.bs.modal&quot;)},c.prototype.resize=function(){this.isShown?a(window).on(&quot;resize.bs.modal&quot;,a.proxy(this.handleUpdate,this)):a(window).off(&quot;resize.bs.modal&quot;)},c.prototype.hideModal=function(){var a=this;this.$element.hide(),this.backdrop(function(){a.$body.removeClass(&quot;modal-open&quot;),a.resetAdjustments(),a.resetScrollbar(),a.$element.trigger(&quot;hidden.bs.modal&quot;)})},c.prototype.removeBackdrop=function(){this.$backdrop&amp;&amp;this.$backdrop.remove(),this.$backdrop=null},c.prototype.backdrop=function(b){var d=this,e=this.$element.hasClass(&quot;fade&quot;)?&quot;fade&quot;:&quot;&quot;;if(this.isShown&amp;&amp;this.options.backdrop){var f=a.support.transition&amp;&amp;e;if(this.$backdrop=a(document.createElement(&quot;div&quot;)).addClass(&quot;modal-backdrop &quot;+e).appendTo(this.$body),this.$element.on(&quot;click.dismiss.bs.modal&quot;,a.proxy(function(a){return this.ignoreBackdropClick?void(this.ignoreBackdropClick=!1):void(a.target===a.currentTarget&amp;&amp;(&quot;static&quot;==this.options.backdrop?this.$element[0].focus():this.hide()))},this)),f&amp;&amp;this.$backdrop[0].offsetWidth,this.$backdrop.addClass(&quot;in&quot;),!b)return;f?this.$backdrop.one(&quot;bsTransitionEnd&quot;,b).emulateTransitionEnd(c.BACKDROP_TRANSITION_DURATION):b()}else if(!this.isShown&amp;&amp;this.$backdrop){this.$backdrop.removeClass(&quot;in&quot;);var g=function(){d.removeBackdrop(),b&amp;&amp;b()};a.support.transition&amp;&amp;this.$element.hasClass(&quot;fade&quot;)?this.$backdrop.one(&quot;bsTransitionEnd&quot;,g).emulateTransitionEnd(c.BACKDROP_TRANSITION_DURATION):g()}else b&amp;&amp;b()},c.prototype.handleUpdate=function(){this.adjustDialog()},c.prototype.adjustDialog=function(){var a=this.$element[0].scrollHeight&gt;document.documentElement.clientHeight;this.$element.css({paddingLeft:!this.bodyIsOverflowing&amp;&amp;a?this.scrollbarWidth:&quot;&quot;,paddingRight:this.bodyIsOverflowing&amp;&amp;!a?this.scrollbarWidth:&quot;&quot;})},c.prototype.resetAdjustments=function(){this.$element.css({paddingLeft:&quot;&quot;,paddingRight:&quot;&quot;})},c.prototype.checkScrollbar=function(){var a=window.innerWidth;if(!a){var b=document.documentElement.getBoundingClientRect();a=b.right-Math.abs(b.left)}this.bodyIsOverflowing=document.body.clientWidth&lt;a,this.scrollbarWidth=this.measureScrollbar()},c.prototype.setScrollbar=function(){var a=parseInt(this.$body.css(&quot;padding-right&quot;)||0,10);this.originalBodyPad=document.body.style.paddingRight||&quot;&quot;,this.bodyIsOverflowing&amp;&amp;this.$body.css(&quot;padding-right&quot;,a+this.scrollbarWidth)},c.prototype.resetScrollbar=function(){this.$body.css(&quot;padding-right&quot;,this.originalBodyPad)},c.prototype.measureScrollbar=function(){var a=document.createElement(&quot;div&quot;);a.className=&quot;modal-scrollbar-measure&quot;,this.$body.append(a);var b=a.offsetWidth-a.clientWidth;return this.$body[0].removeChild(a),b};var d=a.fn.modal;a.fn.modal=b,a.fn.modal.Constructor=c,a.fn.modal.noConflict=function(){return a.fn.modal=d,this},a(document).on(&quot;click.bs.modal.data-api&quot;,&#x27;[data-toggle=&quot;modal&quot;]&#x27;,function(c){var d=a(this),e=d.attr(&quot;href&quot;),f=a(d.attr(&quot;data-target&quot;)||e&amp;&amp;e.replace(/.*(?=#[^\s]+$)/,&quot;&quot;)),g=f.data(&quot;bs.modal&quot;)?&quot;toggle&quot;:a.extend({remote:!/#/.test(e)&amp;&amp;e},f.data(),d.data());d.is(&quot;a&quot;)&amp;&amp;c.preventDefault(),f.one(&quot;show.bs.modal&quot;,function(a){a.isDefaultPrevented()||f.one(&quot;hidden.bs.modal&quot;,function(){d.is(&quot;:visible&quot;)&amp;&amp;d.trigger(&quot;focus&quot;)})}),b.call(f,g,this)})}(jQuery),+function(a){&quot;use strict&quot;;function b(b){return this.each(function(){var d=a(this),e=d.data(&quot;bs.tooltip&quot;),f=&quot;object&quot;==typeof b&amp;&amp;b;!e&amp;&amp;/destroy|hide/.test(b)||(e||d.data(&quot;bs.tooltip&quot;,e=new c(this,f)),&quot;string&quot;==typeof b&amp;&amp;e[b]())})}var c=function(a,b){this.type=null,this.options=null,this.enabled=null,this.timeout=null,this.hoverState=null,this.$element=null,this.inState=null,this.init(&quot;tooltip&quot;,a,b)};c.VERSION=&quot;3.3.7&quot;,c.TRANSITION_DURATION=150,c.DEFAULTS={animation:!0,placement:&quot;top&quot;,selector:!1,template:&#x27;&lt;div class=&quot;tooltip&quot; role=&quot;tooltip&quot;&gt;&lt;div class=&quot;tooltip-arrow&quot;&gt;&lt;/div&gt;&lt;div class=&quot;tooltip-inner&quot;&gt;&lt;/div&gt;&lt;/div&gt;&#x27;,trigger:&quot;hover focus&quot;,title:&quot;&quot;,delay:0,html:!1,container:!1,viewport:{selector:&quot;body&quot;,padding:0}},c.prototype.init=function(b,c,d){if(this.enabled=!0,this.type=b,this.$element=a(c),this.options=this.getOptions(d),this.$viewport=this.options.viewport&amp;&amp;a(a.isFunction(this.options.viewport)?this.options.viewport.call(this,this.$element):this.options.viewport.selector||this.options.viewport),this.inState={click:!1,hover:!1,focus:!1},this.$element[0]instanceof document.constructor&amp;&amp;!this.options.selector)throw new Error(&quot;`selector` option must be specified when initializing &quot;+this.type+&quot; on the window.document object!&quot;);for(var e=this.options.trigger.split(&quot; &quot;),f=e.length;f--;){var g=e[f];if(&quot;click&quot;==g)this.$element.on(&quot;click.&quot;+this.type,this.options.selector,a.proxy(this.toggle,this));else if(&quot;manual&quot;!=g){var h=&quot;hover&quot;==g?&quot;mouseenter&quot;:&quot;focusin&quot;,i=&quot;hover&quot;==g?&quot;mouseleave&quot;:&quot;focusout&quot;;this.$element.on(h+&quot;.&quot;+this.type,this.options.selector,a.proxy(this.enter,this)),this.$element.on(i+&quot;.&quot;+this.type,this.options.selector,a.proxy(this.leave,this))}}this.options.selector?this._options=a.extend({},this.options,{trigger:&quot;manual&quot;,selector:&quot;&quot;}):this.fixTitle()},c.prototype.getDefaults=function(){return c.DEFAULTS},c.prototype.getOptions=function(b){return b=a.extend({},this.getDefaults(),this.$element.data(),b),b.delay&amp;&amp;&quot;number&quot;==typeof b.delay&amp;&amp;(b.delay={show:b.delay,hide:b.delay}),b},c.prototype.getDelegateOptions=function(){var b={},c=this.getDefaults();return this._options&amp;&amp;a.each(this._options,function(a,d){c[a]!=d&amp;&amp;(b[a]=d)}),b},c.prototype.enter=function(b){var c=b instanceof this.constructor?b:a(b.currentTarget).data(&quot;bs.&quot;+this.type);return c||(c=new this.constructor(b.currentTarget,this.getDelegateOptions()),a(b.currentTarget).data(&quot;bs.&quot;+this.type,c)),b instanceof a.Event&amp;&amp;(c.inState[&quot;focusin&quot;==b.type?&quot;focus&quot;:&quot;hover&quot;]=!0),c.tip().hasClass(&quot;in&quot;)||&quot;in&quot;==c.hoverState?void(c.hoverState=&quot;in&quot;):(clearTimeout(c.timeout),c.hoverState=&quot;in&quot;,c.options.delay&amp;&amp;c.options.delay.show?void(c.timeout=setTimeout(function(){&quot;in&quot;==c.hoverState&amp;&amp;c.show()},c.options.delay.show)):c.show())},c.prototype.isInStateTrue=function(){for(var a in this.inState)if(this.inState[a])return!0;return!1},c.prototype.leave=function(b){var c=b instanceof this.constructor?b:a(b.currentTarget).data(&quot;bs.&quot;+this.type);if(c||(c=new this.constructor(b.currentTarget,this.getDelegateOptions()),a(b.currentTarget).data(&quot;bs.&quot;+this.type,c)),b instanceof a.Event&amp;&amp;(c.inState[&quot;focusout&quot;==b.type?&quot;focus&quot;:&quot;hover&quot;]=!1),!c.isInStateTrue())return clearTimeout(c.timeout),c.hoverState=&quot;out&quot;,c.options.delay&amp;&amp;c.options.delay.hide?void(c.timeout=setTimeout(function(){&quot;out&quot;==c.hoverState&amp;&amp;c.hide()},c.options.delay.hide)):c.hide()},c.prototype.show=function(){var b=a.Event(&quot;show.bs.&quot;+this.type);if(this.hasContent()&amp;&amp;this.enabled){this.$element.trigger(b);var d=a.contains(this.$element[0].ownerDocument.documentElement,this.$element[0]);if(b.isDefaultPrevented()||!d)return;var e=this,f=this.tip(),g=this.getUID(this.type);this.setContent(),f.attr(&quot;id&quot;,g),this.$element.attr(&quot;aria-describedby&quot;,g),this.options.animation&amp;&amp;f.addClass(&quot;fade&quot;);var h=&quot;function&quot;==typeof this.options.placement?this.options.placement.call(this,f[0],this.$element[0]):this.options.placement,i=/\s?auto?\s?/i,j=i.test(h);j&amp;&amp;(h=h.replace(i,&quot;&quot;)||&quot;top&quot;),f.detach().css({top:0,left:0,display:&quot;block&quot;}).addClass(h).data(&quot;bs.&quot;+this.type,this),this.options.container?f.appendTo(this.options.container):f.insertAfter(this.$element),this.$element.trigger(&quot;inserted.bs.&quot;+this.type);var k=this.getPosition(),l=f[0].offsetWidth,m=f[0].offsetHeight;if(j){var n=h,o=this.getPosition(this.$viewport);h=&quot;bottom&quot;==h&amp;&amp;k.bottom+m&gt;o.bottom?&quot;top&quot;:&quot;top&quot;==h&amp;&amp;k.top-m&lt;o.top?&quot;bottom&quot;:&quot;right&quot;==h&amp;&amp;k.right+l&gt;o.width?&quot;left&quot;:&quot;left&quot;==h&amp;&amp;k.left-l&lt;o.left?&quot;right&quot;:h,f.removeClass(n).addClass(h)}var p=this.getCalculatedOffset(h,k,l,m);this.applyPlacement(p,h);var q=function(){var a=e.hoverState;e.$element.trigger(&quot;shown.bs.&quot;+e.type),e.hoverState=null,&quot;out&quot;==a&amp;&amp;e.leave(e)};a.support.transition&amp;&amp;this.$tip.hasClass(&quot;fade&quot;)?f.one(&quot;bsTransitionEnd&quot;,q).emulateTransitionEnd(c.TRANSITION_DURATION):q()}},c.prototype.applyPlacement=function(b,c){var d=this.tip(),e=d[0].offsetWidth,f=d[0].offsetHeight,g=parseInt(d.css(&quot;margin-top&quot;),10),h=parseInt(d.css(&quot;margin-left&quot;),10);isNaN(g)&amp;&amp;(g=0),isNaN(h)&amp;&amp;(h=0),b.top+=g,b.left+=h,a.offset.setOffset(d[0],a.extend({using:function(a){d.css({top:Math.round(a.top),left:Math.round(a.left)})}},b),0),d.addClass(&quot;in&quot;);var i=d[0].offsetWidth,j=d[0].offsetHeight;&quot;top&quot;==c&amp;&amp;j!=f&amp;&amp;(b.top=b.top+f-j);var k=this.getViewportAdjustedDelta(c,b,i,j);k.left?b.left+=k.left:b.top+=k.top;var l=/top|bottom/.test(c),m=l?2*k.left-e+i:2*k.top-f+j,n=l?&quot;offsetWidth&quot;:&quot;offsetHeight&quot;;d.offset(b),this.replaceArrow(m,d[0][n],l)},c.prototype.replaceArrow=function(a,b,c){this.arrow().css(c?&quot;left&quot;:&quot;top&quot;,50*(1-a/b)+&quot;%&quot;).css(c?&quot;top&quot;:&quot;left&quot;,&quot;&quot;)},c.prototype.setContent=function(){var a=this.tip(),b=this.getTitle();a.find(&quot;.tooltip-inner&quot;)[this.options.html?&quot;html&quot;:&quot;text&quot;](b),a.removeClass(&quot;fade in top bottom left right&quot;)},c.prototype.hide=function(b){function d(){&quot;in&quot;!=e.hoverState&amp;&amp;f.detach(),e.$element&amp;&amp;e.$element.removeAttr(&quot;aria-describedby&quot;).trigger(&quot;hidden.bs.&quot;+e.type),b&amp;&amp;b()}var e=this,f=a(this.$tip),g=a.Event(&quot;hide.bs.&quot;+this.type);if(this.$element.trigger(g),!g.isDefaultPrevented())return f.removeClass(&quot;in&quot;),a.support.transition&amp;&amp;f.hasClass(&quot;fade&quot;)?f.one(&quot;bsTransitionEnd&quot;,d).emulateTransitionEnd(c.TRANSITION_DURATION):d(),this.hoverState=null,this},c.prototype.fixTitle=function(){var a=this.$element;(a.attr(&quot;title&quot;)||&quot;string&quot;!=typeof a.attr(&quot;data-original-title&quot;))&amp;&amp;a.attr(&quot;data-original-title&quot;,a.attr(&quot;title&quot;)||&quot;&quot;).attr(&quot;title&quot;,&quot;&quot;)},c.prototype.hasContent=function(){return this.getTitle()},c.prototype.getPosition=function(b){b=b||this.$element;var c=b[0],d=&quot;BODY&quot;==c.tagName,e=c.getBoundingClientRect();null==e.width&amp;&amp;(e=a.extend({},e,{width:e.right-e.left,height:e.bottom-e.top}));var f=window.SVGElement&amp;&amp;c instanceof window.SVGElement,g=d?{top:0,left:0}:f?null:b.offset(),h={scroll:d?document.documentElement.scrollTop||document.body.scrollTop:b.scrollTop()},i=d?{width:a(window).width(),height:a(window).height()}:null;return a.extend({},e,h,i,g)},c.prototype.getCalculatedOffset=function(a,b,c,d){return&quot;bottom&quot;==a?{top:b.top+b.height,left:b.left+b.width/2-c/2}:&quot;top&quot;==a?{top:b.top-d,left:b.left+b.width/2-c/2}:&quot;left&quot;==a?{top:b.top+b.height/2-d/2,left:b.left-c}:{top:b.top+b.height/2-d/2,left:b.left+b.width}},c.prototype.getViewportAdjustedDelta=function(a,b,c,d){var e={top:0,left:0};if(!this.$viewport)return e;var f=this.options.viewport&amp;&amp;this.options.viewport.padding||0,g=this.getPosition(this.$viewport);if(/right|left/.test(a)){var h=b.top-f-g.scroll,i=b.top+f-g.scroll+d;h&lt;g.top?e.top=g.top-h:i&gt;g.top+g.height&amp;&amp;(e.top=g.top+g.height-i)}else{var j=b.left-f,k=b.left+f+c;j&lt;g.left?e.left=g.left-j:k&gt;g.right&amp;&amp;(e.left=g.left+g.width-k)}return e},c.prototype.getTitle=function(){var a,b=this.$element,c=this.options;return a=b.attr(&quot;data-original-title&quot;)||(&quot;function&quot;==typeof c.title?c.title.call(b[0]):c.title)},c.prototype.getUID=function(a){do a+=~~(1e6*Math.random());while(document.getElementById(a));return a},c.prototype.tip=function(){if(!this.$tip&amp;&amp;(this.$tip=a(this.options.template),1!=this.$tip.length))throw new Error(this.type+&quot; `template` option must consist of exactly 1 top-level element!&quot;);return this.$tip},c.prototype.arrow=function(){return this.$arrow=this.$arrow||this.tip().find(&quot;.tooltip-arrow&quot;)},c.prototype.enable=function(){this.enabled=!0},c.prototype.disable=function(){this.enabled=!1},c.prototype.toggleEnabled=function(){this.enabled=!this.enabled},c.prototype.toggle=function(b){var c=this;b&amp;&amp;(c=a(b.currentTarget).data(&quot;bs.&quot;+this.type),c||(c=new this.constructor(b.currentTarget,this.getDelegateOptions()),a(b.currentTarget).data(&quot;bs.&quot;+this.type,c))),b?(c.inState.click=!c.inState.click,c.isInStateTrue()?c.enter(c):c.leave(c)):c.tip().hasClass(&quot;in&quot;)?c.leave(c):c.enter(c)},c.prototype.destroy=function(){var a=this;clearTimeout(this.timeout),this.hide(function(){a.$element.off(&quot;.&quot;+a.type).removeData(&quot;bs.&quot;+a.type),a.$tip&amp;&amp;a.$tip.detach(),a.$tip=null,a.$arrow=null,a.$viewport=null,a.$element=null})};var d=a.fn.tooltip;a.fn.tooltip=b,a.fn.tooltip.Constructor=c,a.fn.tooltip.noConflict=function(){return a.fn.tooltip=d,this}}(jQuery),+function(a){&quot;use strict&quot;;function b(b){return this.each(function(){var d=a(this),e=d.data(&quot;bs.popover&quot;),f=&quot;object&quot;==typeof b&amp;&amp;b;!e&amp;&amp;/destroy|hide/.test(b)||(e||d.data(&quot;bs.popover&quot;,e=new c(this,f)),&quot;string&quot;==typeof b&amp;&amp;e[b]())})}var c=function(a,b){this.init(&quot;popover&quot;,a,b)};if(!a.fn.tooltip)throw new Error(&quot;Popover requires tooltip.js&quot;);c.VERSION=&quot;3.3.7&quot;,c.DEFAULTS=a.extend({},a.fn.tooltip.Constructor.DEFAULTS,{placement:&quot;right&quot;,trigger:&quot;click&quot;,content:&quot;&quot;,template:&#x27;&lt;div class=&quot;popover&quot; role=&quot;tooltip&quot;&gt;&lt;div class=&quot;arrow&quot;&gt;&lt;/div&gt;&lt;h3 class=&quot;popover-title&quot;&gt;&lt;/h3&gt;&lt;div class=&quot;popover-content&quot;&gt;&lt;/div&gt;&lt;/div&gt;&#x27;}),c.prototype=a.extend({},a.fn.tooltip.Constructor.prototype),c.prototype.constructor=c,c.prototype.getDefaults=function(){return c.DEFAULTS},c.prototype.setContent=function(){var a=this.tip(),b=this.getTitle(),c=this.getContent();a.find(&quot;.popover-title&quot;)[this.options.html?&quot;html&quot;:&quot;text&quot;](b),a.find(&quot;.popover-content&quot;).children().detach().end()[this.options.html?&quot;string&quot;==typeof c?&quot;html&quot;:&quot;append&quot;:&quot;text&quot;](c),a.removeClass(&quot;fade top bottom left right in&quot;),a.find(&quot;.popover-title&quot;).html()||a.find(&quot;.popover-title&quot;).hide()},c.prototype.hasContent=function(){return this.getTitle()||this.getContent()},c.prototype.getContent=function(){var a=this.$element,b=this.options;return a.attr(&quot;data-content&quot;)||(&quot;function&quot;==typeof b.content?b.content.call(a[0]):b.content)},c.prototype.arrow=function(){return this.$arrow=this.$arrow||this.tip().find(&quot;.arrow&quot;)};var d=a.fn.popover;a.fn.popover=b,a.fn.popover.Constructor=c,a.fn.popover.noConflict=function(){return a.fn.popover=d,this}}(jQuery),+function(a){&quot;use strict&quot;;function b(c,d){this.$body=a(document.body),this.$scrollElement=a(a(c).is(document.body)?window:c),this.options=a.extend({},b.DEFAULTS,d),this.selector=(this.options.target||&quot;&quot;)+&quot; .nav li &gt; a&quot;,this.offsets=[],this.targets=[],this.activeTarget=null,this.scrollHeight=0,this.$scrollElement.on(&quot;scroll.bs.scrollspy&quot;,a.proxy(this.process,this)),this.refresh(),this.process()}function c(c){return this.each(function(){var d=a(this),e=d.data(&quot;bs.scrollspy&quot;),f=&quot;object&quot;==typeof c&amp;&amp;c;e||d.data(&quot;bs.scrollspy&quot;,e=new b(this,f)),&quot;string&quot;==typeof c&amp;&amp;e[c]()})}b.VERSION=&quot;3.3.7&quot;,b.DEFAULTS={offset:10},b.prototype.getScrollHeight=function(){return this.$scrollElement[0].scrollHeight||Math.max(this.$body[0].scrollHeight,document.documentElement.scrollHeight)},b.prototype.refresh=function(){var b=this,c=&quot;offset&quot;,d=0;this.offsets=[],this.targets=[],this.scrollHeight=this.getScrollHeight(),a.isWindow(this.$scrollElement[0])||(c=&quot;position&quot;,d=this.$scrollElement.scrollTop()),this.$body.find(this.selector).map(function(){var b=a(this),e=b.data(&quot;target&quot;)||b.attr(&quot;href&quot;),f=/^#./.test(e)&amp;&amp;a(e);return f&amp;&amp;f.length&amp;&amp;f.is(&quot;:visible&quot;)&amp;&amp;[[f[c]().top+d,e]]||null}).sort(function(a,b){return a[0]-b[0]}).each(function(){b.offsets.push(this[0]),b.targets.push(this[1])})},b.prototype.process=function(){var a,b=this.$scrollElement.scrollTop()+this.options.offset,c=this.getScrollHeight(),d=this.options.offset+c-this.$scrollElement.height(),e=this.offsets,f=this.targets,g=this.activeTarget;if(this.scrollHeight!=c&amp;&amp;this.refresh(),b&gt;=d)return g!=(a=f[f.length-1])&amp;&amp;this.activate(a);if(g&amp;&amp;b&lt;e[0])return this.activeTarget=null,this.clear();for(a=e.length;a--;)g!=f[a]&amp;&amp;b&gt;=e[a]&amp;&amp;(void 0===e[a+1]||b&lt;e[a+1])&amp;&amp;this.activate(f[a])},b.prototype.activate=function(b){
this.activeTarget=b,this.clear();var c=this.selector+&#x27;[data-target=&quot;&#x27;+b+&#x27;&quot;],&#x27;+this.selector+&#x27;[href=&quot;&#x27;+b+&#x27;&quot;]&#x27;,d=a(c).parents(&quot;li&quot;).addClass(&quot;active&quot;);d.parent(&quot;.dropdown-menu&quot;).length&amp;&amp;(d=d.closest(&quot;li.dropdown&quot;).addClass(&quot;active&quot;)),d.trigger(&quot;activate.bs.scrollspy&quot;)},b.prototype.clear=function(){a(this.selector).parentsUntil(this.options.target,&quot;.active&quot;).removeClass(&quot;active&quot;)};var d=a.fn.scrollspy;a.fn.scrollspy=c,a.fn.scrollspy.Constructor=b,a.fn.scrollspy.noConflict=function(){return a.fn.scrollspy=d,this},a(window).on(&quot;load.bs.scrollspy.data-api&quot;,function(){a(&#x27;[data-spy=&quot;scroll&quot;]&#x27;).each(function(){var b=a(this);c.call(b,b.data())})})}(jQuery),+function(a){&quot;use strict&quot;;function b(b){return this.each(function(){var d=a(this),e=d.data(&quot;bs.tab&quot;);e||d.data(&quot;bs.tab&quot;,e=new c(this)),&quot;string&quot;==typeof b&amp;&amp;e[b]()})}var c=function(b){this.element=a(b)};c.VERSION=&quot;3.3.7&quot;,c.TRANSITION_DURATION=150,c.prototype.show=function(){var b=this.element,c=b.closest(&quot;ul:not(.dropdown-menu)&quot;),d=b.data(&quot;target&quot;);if(d||(d=b.attr(&quot;href&quot;),d=d&amp;&amp;d.replace(/.*(?=#[^\s]*$)/,&quot;&quot;)),!b.parent(&quot;li&quot;).hasClass(&quot;active&quot;)){var e=c.find(&quot;.active:last a&quot;),f=a.Event(&quot;hide.bs.tab&quot;,{relatedTarget:b[0]}),g=a.Event(&quot;show.bs.tab&quot;,{relatedTarget:e[0]});if(e.trigger(f),b.trigger(g),!g.isDefaultPrevented()&amp;&amp;!f.isDefaultPrevented()){var h=a(d);this.activate(b.closest(&quot;li&quot;),c),this.activate(h,h.parent(),function(){e.trigger({type:&quot;hidden.bs.tab&quot;,relatedTarget:b[0]}),b.trigger({type:&quot;shown.bs.tab&quot;,relatedTarget:e[0]})})}}},c.prototype.activate=function(b,d,e){function f(){g.removeClass(&quot;active&quot;).find(&quot;&gt; .dropdown-menu &gt; .active&quot;).removeClass(&quot;active&quot;).end().find(&#x27;[data-toggle=&quot;tab&quot;]&#x27;).attr(&quot;aria-expanded&quot;,!1),b.addClass(&quot;active&quot;).find(&#x27;[data-toggle=&quot;tab&quot;]&#x27;).attr(&quot;aria-expanded&quot;,!0),h?(b[0].offsetWidth,b.addClass(&quot;in&quot;)):b.removeClass(&quot;fade&quot;),b.parent(&quot;.dropdown-menu&quot;).length&amp;&amp;b.closest(&quot;li.dropdown&quot;).addClass(&quot;active&quot;).end().find(&#x27;[data-toggle=&quot;tab&quot;]&#x27;).attr(&quot;aria-expanded&quot;,!0),e&amp;&amp;e()}var g=d.find(&quot;&gt; .active&quot;),h=e&amp;&amp;a.support.transition&amp;&amp;(g.length&amp;&amp;g.hasClass(&quot;fade&quot;)||!!d.find(&quot;&gt; .fade&quot;).length);g.length&amp;&amp;h?g.one(&quot;bsTransitionEnd&quot;,f).emulateTransitionEnd(c.TRANSITION_DURATION):f(),g.removeClass(&quot;in&quot;)};var d=a.fn.tab;a.fn.tab=b,a.fn.tab.Constructor=c,a.fn.tab.noConflict=function(){return a.fn.tab=d,this};var e=function(c){c.preventDefault(),b.call(a(this),&quot;show&quot;)};a(document).on(&quot;click.bs.tab.data-api&quot;,&#x27;[data-toggle=&quot;tab&quot;]&#x27;,e).on(&quot;click.bs.tab.data-api&quot;,&#x27;[data-toggle=&quot;pill&quot;]&#x27;,e)}(jQuery),+function(a){&quot;use strict&quot;;function b(b){return this.each(function(){var d=a(this),e=d.data(&quot;bs.affix&quot;),f=&quot;object&quot;==typeof b&amp;&amp;b;e||d.data(&quot;bs.affix&quot;,e=new c(this,f)),&quot;string&quot;==typeof b&amp;&amp;e[b]()})}var c=function(b,d){this.options=a.extend({},c.DEFAULTS,d),this.$target=a(this.options.target).on(&quot;scroll.bs.affix.data-api&quot;,a.proxy(this.checkPosition,this)).on(&quot;click.bs.affix.data-api&quot;,a.proxy(this.checkPositionWithEventLoop,this)),this.$element=a(b),this.affixed=null,this.unpin=null,this.pinnedOffset=null,this.checkPosition()};c.VERSION=&quot;3.3.7&quot;,c.RESET=&quot;affix affix-top affix-bottom&quot;,c.DEFAULTS={offset:0,target:window},c.prototype.getState=function(a,b,c,d){var e=this.$target.scrollTop(),f=this.$element.offset(),g=this.$target.height();if(null!=c&amp;&amp;&quot;top&quot;==this.affixed)return e&lt;c&amp;&amp;&quot;top&quot;;if(&quot;bottom&quot;==this.affixed)return null!=c?!(e+this.unpin&lt;=f.top)&amp;&amp;&quot;bottom&quot;:!(e+g&lt;=a-d)&amp;&amp;&quot;bottom&quot;;var h=null==this.affixed,i=h?e:f.top,j=h?g:b;return null!=c&amp;&amp;e&lt;=c?&quot;top&quot;:null!=d&amp;&amp;i+j&gt;=a-d&amp;&amp;&quot;bottom&quot;},c.prototype.getPinnedOffset=function(){if(this.pinnedOffset)return this.pinnedOffset;this.$element.removeClass(c.RESET).addClass(&quot;affix&quot;);var a=this.$target.scrollTop(),b=this.$element.offset();return this.pinnedOffset=b.top-a},c.prototype.checkPositionWithEventLoop=function(){setTimeout(a.proxy(this.checkPosition,this),1)},c.prototype.checkPosition=function(){if(this.$element.is(&quot;:visible&quot;)){var b=this.$element.height(),d=this.options.offset,e=d.top,f=d.bottom,g=Math.max(a(document).height(),a(document.body).height());&quot;object&quot;!=typeof d&amp;&amp;(f=e=d),&quot;function&quot;==typeof e&amp;&amp;(e=d.top(this.$element)),&quot;function&quot;==typeof f&amp;&amp;(f=d.bottom(this.$element));var h=this.getState(g,b,e,f);if(this.affixed!=h){null!=this.unpin&amp;&amp;this.$element.css(&quot;top&quot;,&quot;&quot;);var i=&quot;affix&quot;+(h?&quot;-&quot;+h:&quot;&quot;),j=a.Event(i+&quot;.bs.affix&quot;);if(this.$element.trigger(j),j.isDefaultPrevented())return;this.affixed=h,this.unpin=&quot;bottom&quot;==h?this.getPinnedOffset():null,this.$element.removeClass(c.RESET).addClass(i).trigger(i.replace(&quot;affix&quot;,&quot;affixed&quot;)+&quot;.bs.affix&quot;)}&quot;bottom&quot;==h&amp;&amp;this.$element.offset({top:g-b-f})}};var d=a.fn.affix;a.fn.affix=b,a.fn.affix.Constructor=c,a.fn.affix.noConflict=function(){return a.fn.affix=d,this},a(window).on(&quot;load&quot;,function(){a(&#x27;[data-spy=&quot;affix&quot;]&#x27;).each(function(){var c=a(this),d=c.data();d.offset=d.offset||{},null!=d.offsetBottom&amp;&amp;(d.offset.bottom=d.offsetBottom),null!=d.offsetTop&amp;&amp;(d.offset.top=d.offsetTop),b.call(c,d)})})}(jQuery);        &lt;/script&gt;&lt;script&gt;
$(function () {
    $(&#x27;[data-toggle=&quot;tooltip&quot;]&#x27;).tooltip();
});

$(&quot;a[href^=&#x27;#&#x27;].anchor&quot;).on(&#x27;click&#x27;, function (e) {

    // prevent default anchor click behavior
    e.preventDefault();

    // store hash
    var hash = this.hash;

    // animate
    $(&#x27;html, body&#x27;).animate({
        scrollTop: $(hash).offset().top
    }, 300, function () {

        // when done, add hash to url
        // (default click behaviour)
        window.location.hash = hash;
    });

});        &lt;/script&gt;&lt;/body&gt;&lt;/html&gt;" frameborder="0" allowfullscreen></iframe>


### Métodos para baixar ou atualizar os arquivos das bases de dados

```python
from anateldb.query import update_mosaico, update_radcom, update_stel, update_base
```

A função seguinte baixa os dados diretamente da interface pública online do [Spectrum E](http://sistemas.anatel.gov.br/se/public/view/b/srd.php) 

```python
%%time
update_mosaico(pasta='D:\OneDrive - ANATEL\GR01FI3\BaseDados')
```

    Baixando as Estações do Mosaico...
    Baixando o Plano Básico das Estações...
    Baixando o Histórico de Atualizações...
    Kbô
    Wall time: 8.12 s


```python
%%time
update_radcom('D:\OneDrive - ANATEL\GR01FI3\BaseDados')
```

    Lendo o Banco de Dados de Radcom
    Wall time: 1 s

A função <code>update_stel</code> é bem mais lenta que as demais, dado que o banco de dados do STEL é antigo e abarca todos os registros de outorga de serviços de telecomunicações da ANATEL, com mais de **400.000** registros ativos. Esse banco de dados é atualizado 1 vez ao dia à meia-noite e remete ao estado do dia anterior, portanto não faz sentido atualizá-lo mais de 1 vez por dia.

```python
%%time
update_stel('D:\OneDrive - ANATEL\GR01FI3\BaseDados')
```


A função `update_base` combina as 3 bases anteriores e uniformiza os campos:
```python
update_base('D:\OneDrive - ANATEL\GR01FI3\BaseDados')
```


### Métodos para ler as Bases de Dados


```python
from anateldb.read import read_radcom, read_stel, read_mosaico, read_base
radcom = read_radcom(pasta='D:\OneDrive - ANATEL\GR01FI3\BaseDados') ; radcom.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Frequência</th>
      <th>Unidade</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Fase</th>
      <th>Situação</th>
      <th>Numero da Estação</th>
      <th>CNPJ</th>
      <th>Fistel</th>
      <th>Entidade</th>
      <th>Município</th>
      <th>UF</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>104.9</td>
      <td>MHz</td>
      <td>-24.861389</td>
      <td>-54.334722</td>
      <td>3</td>
      <td>A</td>
      <td>641168764</td>
      <td>00104477000117</td>
      <td>50011685115</td>
      <td>ACADEMIA CULTURAL DE SANTA HELENA - ACULT - ST...</td>
      <td>Santa Helena</td>
      <td>PR</td>
    </tr>
    <tr>
      <th>1</th>
      <td>87.9</td>
      <td>MHz</td>
      <td>-7.074444</td>
      <td>-36.731111</td>
      <td>3</td>
      <td>M</td>
      <td>682699349</td>
      <td>00284576000128</td>
      <td>50012524409</td>
      <td>ASSOCIACAO DOS MORADORES E PRODUT. RURAIS DE A...</td>
      <td>Assunção</td>
      <td>PB</td>
    </tr>
    <tr>
      <th>2</th>
      <td>87.9</td>
      <td>MHz</td>
      <td>-20.323611</td>
      <td>-44.246944</td>
      <td>3</td>
      <td>H</td>
      <td>659028590</td>
      <td>00575697000129</td>
      <td>50011824689</td>
      <td>ASSOCIACAO BONFIM ESPERANCA- ABESPE</td>
      <td>Bonfim</td>
      <td>MG</td>
    </tr>
    <tr>
      <th>3</th>
      <td>104.9</td>
      <td>MHz</td>
      <td>-18.843611</td>
      <td>-46.792778</td>
      <td>3</td>
      <td>B</td>
      <td>631410937</td>
      <td>00792795000118</td>
      <td>50011398132</td>
      <td>ASSOCIACAO DOS TRABALHADORES DE GUIMARANIA (ATG)</td>
      <td>Guimarânia</td>
      <td>MG</td>
    </tr>
    <tr>
      <th>4</th>
      <td>87.9</td>
      <td>MHz</td>
      <td>-19.466667</td>
      <td>-45.600000</td>
      <td>3</td>
      <td>M</td>
      <td>631412301</td>
      <td>00794510000188</td>
      <td>50011398990</td>
      <td>FUNDACAO ASSISTENCIAL LAR DA PAZ - FALP</td>
      <td>Dores do Indaiá</td>
      <td>MG</td>
    </tr>
  </tbody>
</table>
</div>


Se o argumento <code>update=True</code> for fornecido ou arquivo local não existir, a base de dados é atualizada por meio da função <code>update_radcom</code>. 

> *A função <code>update_radcom</code> somente irá funcionar caso o PC estiver plugado na rede interna cabeada da Anatel.*

```python
radcom = read_radcom(pasta='D:\OneDrive - ANATEL\GR01FI3\BaseDados', update=True) ; radcom.tail()
```

    Lendo o Banco de Dados de Radcom





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Frequência</th>
      <th>Unidade</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Fase</th>
      <th>Situação</th>
      <th>Numero da Estação</th>
      <th>CNPJ</th>
      <th>Fistel</th>
      <th>Entidade</th>
      <th>Município</th>
      <th>UF</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4639</th>
      <td>87.9</td>
      <td>MHz</td>
      <td>-10.311667</td>
      <td>-48.162222</td>
      <td>1</td>
      <td>K</td>
      <td>1011036964</td>
      <td>08931976000190</td>
      <td>50411347829</td>
      <td>ASSOCIACAO AMIGOS DA CULTURA E DO MEIO AMBIENT...</td>
      <td>Palmas</td>
      <td>TO</td>
    </tr>
    <tr>
      <th>4640</th>
      <td>104.9</td>
      <td>MHz</td>
      <td>-10.005000</td>
      <td>-48.988889</td>
      <td>1</td>
      <td>A</td>
      <td>1011037472</td>
      <td>19001721000144</td>
      <td>50416345301</td>
      <td>ASSOCIACAO RADIO COMUNITARIA MONTE SANTO FM</td>
      <td>Monte Santo do Tocantins</td>
      <td>TO</td>
    </tr>
    <tr>
      <th>4641</th>
      <td>104.9</td>
      <td>MHz</td>
      <td>-5.586389</td>
      <td>-48.061111</td>
      <td>P</td>
      <td>M</td>
      <td>1011044797</td>
      <td>19332116000156</td>
      <td>50416480004</td>
      <td>ASSOCIACAO RADIO COMUNITARIA TOP FM</td>
      <td>Araguatins</td>
      <td>TO</td>
    </tr>
    <tr>
      <th>4642</th>
      <td>98.3</td>
      <td>MHz</td>
      <td>-28.682222</td>
      <td>-53.610278</td>
      <td>2</td>
      <td>K</td>
      <td>1011044940</td>
      <td>97538346000180</td>
      <td>50416390609</td>
      <td>ASSOCIACAO DE RADIODIFUSAO CIDADE DE CRUZ ALTA</td>
      <td>Cruz Alta</td>
      <td>RS</td>
    </tr>
    <tr>
      <th>4643</th>
      <td>104.9</td>
      <td>MHz</td>
      <td>-6.594722</td>
      <td>-35.055278</td>
      <td>1</td>
      <td>K</td>
      <td>1011110250</td>
      <td>10877144000184</td>
      <td>50411382063</td>
      <td>ASSOCIAÇÃO DE DESENVOLVIMENTO CULTURAL DA RÁDI...</td>
      <td>Mataraca</td>
      <td>PB</td>
    </tr>
  </tbody>
</table>
</div>


```python
stel = read_stel(pasta='D:\OneDrive - ANATEL\GR01FI3\BaseDados', update=True)
```
**Os dados do Stel não serão ilustrados aqui por se tratar de dados de telecomunicação privados, os demais dados de radiodifusão são públicos e disponíveis para qualquer interessado consultar**

Se o argumento <code>update=True</code> for fornecido ou arquivo local não existir, a base de dados é atualizada por meio da função <code>update_stel</code>. 

> *A função  <code>update_stel</code> somente irá funcionar caso o PC estiver plugado na rede interna cabeada da Anatel.*

```python
mosaico = read_mosaico(pasta='D:\OneDrive - ANATEL\GR01FI3\BaseDados') ; mosaico.tail()
```

    Baixando as Estações do Mosaico...
    Baixando o Plano Básico das Estações...
    Baixando o Histórico de Atualizações...
    Kbô





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Serviço</th>
      <th>Situação</th>
      <th>Entidade</th>
      <th>Fistel</th>
      <th>CNPJ</th>
      <th>Município</th>
      <th>UF</th>
      <th>Id</th>
      <th>Número da Estação</th>
      <th>Classe</th>
      <th>Frequência</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Num_Ato</th>
      <th>Órgao</th>
      <th>Data_Ato</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>21146</th>
      <td>RTVD</td>
      <td>TV-C2</td>
      <td>M. V. L - COMMUNICARE TELECOMUNICACOES LTDA</td>
      <td>50419656170</td>
      <td>12071310000186</td>
      <td>Parauapebas</td>
      <td>PA</td>
      <td>5f2068e65ace5</td>
      <td></td>
      <td>C</td>
      <td>503</td>
      <td>-6,0678</td>
      <td>-49,9037</td>
      <td>7588</td>
      <td>ORLE</td>
      <td>2020-12-10 18:21:09</td>
    </tr>
    <tr>
      <th>21147</th>
      <td>RTVD</td>
      <td>TV-C1</td>
      <td>MERCES COMUNICACOES LTDA</td>
      <td>50419663118</td>
      <td>11322505000199</td>
      <td>Delmiro Gouveia</td>
      <td>AL</td>
      <td>5f218fcfb0d84</td>
      <td></td>
      <td>C</td>
      <td>545</td>
      <td>-9,3853</td>
      <td>-37,9987</td>
      <td>9430</td>
      <td>ORLE</td>
      <td>2017-06-09 00:00:00</td>
    </tr>
    <tr>
      <th>21148</th>
      <td>RTVD</td>
      <td>TV-C1</td>
      <td>FUNDACAO EDUCACIONAL E CULTURAL DE IPANEMA</td>
      <td>50433856696</td>
      <td>04608796000110</td>
      <td>Sabará</td>
      <td>MG</td>
      <td>5f32c1c918e6b</td>
      <td></td>
      <td>C</td>
      <td>207</td>
      <td>-19,89667</td>
      <td>-43,80722</td>
      <td>3301</td>
      <td>ORLE</td>
      <td>2020-06-23 00:00:00</td>
    </tr>
    <tr>
      <th>21149</th>
      <td>FM</td>
      <td>FM-C2</td>
      <td>RADIO ITAPIRANGA LTDA</td>
      <td>50433860456</td>
      <td>84375872000124</td>
      <td>Itapiranga</td>
      <td>SC</td>
      <td>5f68d432841a5</td>
      <td></td>
      <td>B1</td>
      <td>105,1</td>
      <td>-27,15778</td>
      <td>-53,69583</td>
      <td>567</td>
      <td>ORLE</td>
      <td>2021-01-26 17:20:30</td>
    </tr>
    <tr>
      <th>21150</th>
      <td>FM</td>
      <td>FM-C1</td>
      <td>EMISSORAS SUL BRASILEIRAS LTDA</td>
      <td>50433937009</td>
      <td>95818506000119</td>
      <td>Horizontina</td>
      <td>RS</td>
      <td>5f8dcc96f23f9</td>
      <td></td>
      <td>B1</td>
      <td>100,3</td>
      <td>-27,62833</td>
      <td>-54,30528</td>
      <td>3166</td>
      <td>ORLE</td>
      <td>2020-06-13 00:00:00</td>
    </tr>
  </tbody>
</table>
</div>


Se o argumento <code>update=True</code> for fornecido ou o arquivo local não existir, a base de dados é atualizada por meio da função <code>update_mosaico</code>. 

> A função <code>update_mosaico</code> usa a base de dados Pública do Spectrum E, portanto basta somente estar conectado na internet &#x1F60E;.

A função `update_base` combina as 3 atualizações de base anteriormente descritas.
