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
Full exploratory notebook of benchmark creation for the experiments can be found in `experiments/dataset_evaluation.ipynb`.

Because of a limited amount of human resources, evaluation of the generated domains has to take a more automated approach (e.g. no human evaluation or A/B testing is possible in this case). Automatic evaluation is difficult, usual scores like BLEU or ROUGE are not suitable, since they do not capture the creativity and branding aspect of domains, but evaluating purely based on "creativity" is also not suitable, as then the influence of the buisness description, on the final result will be negligible. Due to time constrains, experimentation was limited, and a combination following metric ideas were used in the final evaluation (though this part can be improved significantly by adding any sort of **human eval** or putting more time into coming up with good performance heuristics):

1. Exact match accuracy (using first and second level domain split, denoted `E`)
2. Semantic similarity (using model embeddings and cosine similarity, denoted `S`)
3. Keyword coverage (using RAKE for keyword extraction, denoted `K`)
4. "Creativity", calculated using the formula (denoted `C`):
   ```python
   length_score = max(0, 1 - (len(domain) - 5) / 10) # penalize long domains
   vowel_ratio = sum(1 for c in domain if c in "aeiou") / len(domain) # reward more vowels
   final_score = 0.5 * length_score + 0.5 * vowel_ratio
   ```

The final score is then: `Score = 0.5 * E + 0.5 * (S + K + C) / 3`.