# Dataset creation

## Ideas

Since no dataset was supplied for the task, one has to be created or sourced
from outside. Ideas (ranked in terms of projected data quality):

1. **Used** Search online for a dataset relating buisness descriptions with
   their domains
2. **Used** Crawl company data from online media sources (google maps, LinkedIn,
   Facebook market, YC, etc.)
3. **Viable** Use domain generation APIs of competitors to generate domain names
   with synthetic descriptions
4. **Not tested** Use fully synthetic data

## Collection

After searching, some good candidate datasets were identified, but none contained the description and url data. Because of this, it was decided to crawl this data from three startup incubator companies: YCombinator, Enterpreneur First and Antler.

The dataset creation code is found in `domainer/dataset.py`. The final dataset
can be found under `data/final_train.csv`, `data/final_test.csv` and
`data/final_validation.csv`.

As the datasets produced by the first methods we're deemed sufficient, the third
idea was only partially explored by hitting namecheap generation apis as well as
the Hostinger API to test the potential viability of the idea (the idea was
deemed viable):

- `https://domain-suggestion.namecheapapi.com`
- `https://bng.visual.com/v1/generateWords`
- `https://www.hostinger.com/api-proxy/api/domain/generate-by-description`

# Performance evaluation/Benchmarking
