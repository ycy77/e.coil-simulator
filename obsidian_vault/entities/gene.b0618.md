---
entity_id: "gene.b0618"
entity_type: "gene"
name: "citC"
source_database: "NCBI RefSeq"
source_id: "gene-b0618"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0618"
  - "citC"
---

# citC

`gene.b0618`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0618`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

citC (gene.b0618) is a gene entity. It encodes citC (protein.P77390). Encoded protein function: FUNCTION: Acetylation of prosthetic group (2-(5''-phosphoribosyl)-3'-dephosphocoenzyme-A) of the gamma subunit of citrate lyase. EcoCyc product frame: CITC-MONOMER. EcoCyc synonyms: ybeO. Genomic coordinates: 650798-651856. EcoCyc protein note: Citrate lyase synthetase activates citrate lyase by acetylation . The actual site of acetylation is the prosthetic group of the acyl-carrier protein, or γ, subunit.

## Biological Role

Activated by dpiA (protein.P0AEF4).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77390|protein.P77390]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AEF4|protein.P0AEF4]] `RegulonDB` `S` - regulator=DpiA; target=citC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0002126,ECOCYC:G6344,GeneID:945231`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:650798-651856:-; feature_type=gene
