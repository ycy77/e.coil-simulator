---
entity_id: "gene.b3141"
entity_type: "gene"
name: "agaI"
source_database: "NCBI RefSeq"
source_id: "gene-b3141"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3141"
  - "agaI"
---

# agaI

`gene.b3141`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3141`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

agaI (gene.b3141) is a gene entity. It encodes agaI (protein.P42912). Encoded protein function: Putative deaminase AgaI (EC 3.5.99.-) EcoCyc product frame: G7636-MONOMER. EcoCyc synonyms: yraG. Genomic coordinates: 3286270-3287025. EcoCyc protein note: Unlike other E. coli strains, K-12 is unable to grow on N-acetylgalactosamine as a source of carbon and energy. This phenotype is apparently due to a deletion of genes essential for transport and metabolism of N-acetylgalactosamine. AgaI was predicted to catalyze the deaminase step if the pathway were functional , but that reaction was later shown to be catalyzed by AgaS . AgaI was also predicted to be a galactosamine-6-phosphate isomerase by . Based on sequence similarity, AgaI might have 6-phosphogluconolactonase activity . AgaI: "N-acetylgalactosamine degradation"

## Biological Role

Repressed by agaR (protein.P0ACK2). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P42912|protein.P42912]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=agaI; function=+
- `represses` <-- [[protein.P0ACK2|protein.P0ACK2]] `RegulonDB` `S` - regulator=AgaR; target=agaI; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010317,ECOCYC:G7636,GeneID:947985`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3286270-3287025:+; feature_type=gene
