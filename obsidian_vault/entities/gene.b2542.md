---
entity_id: "gene.b2542"
entity_type: "gene"
name: "hcaD"
source_database: "NCBI RefSeq"
source_id: "gene-b2542"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2542"
  - "hcaD"
---

# hcaD

`gene.b2542`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2542`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hcaD (gene.b2542) is a gene entity. It encodes hcaD (protein.P77650). Encoded protein function: FUNCTION: Part of the multicomponent 3-phenylpropionate dioxygenase, that converts 3-phenylpropionic acid (PP) and cinnamic acid (CI) into 3-phenylpropionate-dihydrodiol (PP-dihydrodiol) and cinnamic acid-dihydrodiol (CI-dihydrodiol), respectively. EcoCyc product frame: HCAD-MONOMER. EcoCyc synonyms: hcaa4, phdA, yfhY. Genomic coordinates: 2672047-2673249. EcoCyc protein note: Based on sequence similarity, HcaD is thought to encode the ferredoxin reductase component of the 3-phenylpropionate dioxygenase system . 3-phenylpropionate dioxygenase has not been biochemically characterized. E. coli is able to utilize certain aromatic acids as carbon and energy sources. A meta-cleavage pathway involving HcaD is used for the catabolism of 3-phenylpropionate . HcaD: "hydroxycinnamic acid"

## Biological Role

Activated by hcaR (protein.Q47141).

## Enriched Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77650|protein.P77650]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47141|protein.Q47141]] `RegulonDB` `S` - regulator=HcaR; target=hcaD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008363,ECOCYC:G7336,GeneID:945427`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2672047-2673249:+; feature_type=gene
