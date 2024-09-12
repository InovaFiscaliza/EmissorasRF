set VERSION=v2.0.3
C:\Users\rsilva\scoop\apps\mambaforge\current\envs\db\python.exe scripts\main.py --no-read-cache --reprocess-sources
gh release create %VERSION% --generate-notes .\extracao\datasources\arquivos\saida\estacoes.parquet.gzip .\extracao\datasources\arquivos\saida\log.parquet.gzip
gh release delete rfdatahub --cleanup-tag -R InovaFiscaliza/.github -y
gh release create rfdatahub -t RFDataHub --notes "%VERSION%" .\extracao\datasources\arquivos\saida\estacoes.parquet.gzip .\extracao\datasources\arquivos\saida\log.parquet.gzip .\extracao\datasources\arquivos\saida\Release.json -R InovaFiscaliza/.github