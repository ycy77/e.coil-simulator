---
entity_id: "gene.b2538"
entity_type: "gene"
name: "hcaE"
source_database: "NCBI RefSeq"
source_id: "gene-b2538"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2538"
  - "hcaE"
---

# hcaE

`gene.b2538`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2538`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hcaE (gene.b2538) is a gene entity. It encodes hcaE (protein.P0ABR5). Encoded protein function: FUNCTION: Part of the multicomponent 3-phenylpropionate dioxygenase. Converts 3-phenylpropionic acid (PP) and cinnamic acid (CI) into 3-phenylpropionate-dihydrodiol (PP-dihydrodiol) and cinnamic acid-dihydrodiol (CI-dihydrodiol), respectively. {ECO:0000269|PubMed:9603882}. EcoCyc product frame: PHENYLPRODIOXY-MONOMER. EcoCyc synonyms: yfhU, digA, phdC1, hcaA, hcaA1. Genomic coordinates: 2669032-2670393. EcoCyc protein note: Based on sequence similarity, HcaE is thought to encode the large terminal subunit of the 3-phenylpropionate dioxygenase system . 3-phenylpropionate dioxygenase has not been biochemically characterized. E. coli is able to utilize certain aromatic acids as carbon and energy sources. A meta-cleavage pathway involving HcaE is used for the catabolism of 3-phenylpropionate . HcaE: "hydroxycinnamic acid"

## Biological Role

Activated by nac (protein.Q47005), hcaR (protein.Q47141).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABR5|protein.P0ABR5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=hcaE; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.Q47141|protein.Q47141]] `RegulonDB` `S` - regulator=HcaR; target=hcaE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008355,ECOCYC:M009,GeneID:946998`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2669032-2670393:+; feature_type=gene
