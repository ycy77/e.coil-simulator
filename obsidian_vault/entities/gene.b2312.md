---
entity_id: "gene.b2312"
entity_type: "gene"
name: "purF"
source_database: "NCBI RefSeq"
source_id: "gene-b2312"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2312"
  - "purF"
---

# purF

`gene.b2312`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2312`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

purF (gene.b2312) is a gene entity. It encodes purF (protein.P0AG16). Encoded protein function: FUNCTION: Catalyzes the formation of phosphoribosylamine from phosphoribosylpyrophosphate (PRPP) and glutamine. Can also use NH(3) in place of glutamine. {ECO:0000269|PubMed:372191}. EcoCyc product frame: PRPPAMIDOTRANS-MONOMER. EcoCyc synonyms: ade, purC. Genomic coordinates: 2428721-2430238.

## Biological Role

Repressed by purR (protein.P0ACP7). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG16|protein.P0AG16]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=purF; function=+
- `represses` <-- [[protein.P0ACP7|protein.P0ACP7]] `RegulonDB` `C` - regulator=PurR; target=purF; function=-

## External IDs

- `Dbxref:ECOCYC:EG10794,GeneID:946794`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2428721-2430238:-; feature_type=gene
