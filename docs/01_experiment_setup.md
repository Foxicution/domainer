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

After searching, two candidate datasets were identified:

1. YCombinator companies dataset (problem, the list is a bit old (2023) and not
   full) https://www.kaggle.com/datasets/miguelcorraljr/y-combinator-directory
2. BigPicture LinkedIn companies dataset (problem, the provided dataset is only
   a sample of 105 companies)
   https://docs.bigpicture.io/docs/datasets/linkedin-companies

Since both datasets contain problems, it was decided to combine the data from
BigPicture dataset with data crawled from three startup incubator companies:
YCombinator, Enterpreneur First and Antler.

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
