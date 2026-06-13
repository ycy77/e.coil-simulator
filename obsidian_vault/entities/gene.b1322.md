---
entity_id: "gene.b1322"
entity_type: "gene"
name: "ycjF"
source_database: "NCBI RefSeq"
source_id: "gene-b1322"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1322"
  - "ycjF"
---

# ycjF

`gene.b1322`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1322`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycjF (gene.b1322) is a gene entity. It encodes ycjF (protein.P0A8R7). Encoded protein function: UPF0283 membrane protein YcjF EcoCyc product frame: EG12870-MONOMER. Genomic coordinates: 1385511-1386572. EcoCyc protein note: YcjF is an inner membrane protein with two predicted transmembrane domains. The C terminus is located in the cytoplasm . The ortholog of YcjF from the E. coli septicemia strain i484 has been identified as an in vivo-induced gene expressed exclusively during disease in a mouse infection model. Mutation of ycjF resulted in an 81-fold attenuation of the mutant compared to wild-type in a mouse competition model of infection, suggesting a role for YcjF in virulence or in vivo survival . A meta-analysis of E. coli K-12 MG1655 transcriptomic data sets in response to multiple stressors found 15 uncharacterized or partially characterized genes (yqfA, yhfG, yhhA, ybgS, arpA, yqaE, yfdY, yaiY, yebE, ydiE, yjcB, yiiX, ycjF, yihF, yidX) that were upregulated under all five stressors: heat, cold, oxidative stress, nitrosative stress, and antibiotic treatment, whereas 3 uncharacterized or partially characterized genes (ymfI, ydiJ, yedE) that were downregulated under all but nitrosative stress .

## Biological Role

Repressed by pgrR (protein.P77333). Activated by rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8R7|protein.P0A8R7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=ycjF; function=+
- `represses` <-- [[protein.P77333|protein.P77333]] `RegulonDB` `S` - regulator=PgrR; target=ycjF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004436,ECOCYC:EG12870,GeneID:945878`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1385511-1386572:+; feature_type=gene
