---
entity_id: "gene.b2539"
entity_type: "gene"
name: "hcaF"
source_database: "NCBI RefSeq"
source_id: "gene-b2539"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2539"
  - "hcaF"
---

# hcaF

`gene.b2539`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2539`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hcaF (gene.b2539) is a gene entity. It encodes hcaF (protein.Q47140). Encoded protein function: FUNCTION: Part of the multicomponent 3-phenylpropionate dioxygenase. Converts 3-phenylpropionic acid (PP) and cinnamic acid (CI) into 3-phenylpropionate-dihydrodiol (PP-dihydrodiol) and cinnamic acid-dihydrodiol (CI-dihydrodiol), respectively. {ECO:0000269|PubMed:9603882}. EcoCyc product frame: HCAA2-MONOMER. EcoCyc synonyms: yfhV, hcaA, phdC2, digB, hcaB, hcaA2. Genomic coordinates: 2670390-2670908. EcoCyc protein note: Based on sequence similarity, HcaF is thought to encode the small terminal subunit of the 3-phenylpropionate dioxygenase system . 3-phenylpropionate dioxygenase has not been biochemically characterized. E. coli is able to utilize certain aromatic acids as carbon and energy sources. A meta-cleavage pathway involving HcaF is used for the catabolism of 3-phenylpropionate . HcaF: "hydroxycinnamic acid"

## Biological Role

Activated by hcaR (protein.Q47141).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47140|protein.Q47140]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47141|protein.Q47141]] `RegulonDB` `S` - regulator=HcaR; target=hcaF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008357,ECOCYC:M015,GeneID:946997`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2670390-2670908:+; feature_type=gene
