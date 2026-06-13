---
entity_id: "gene.b0269"
entity_type: "gene"
name: "yagF"
source_database: "NCBI RefSeq"
source_id: "gene-b0269"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0269"
  - "yagF"
---

# yagF

`gene.b0269`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0269`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yagF (gene.b0269) is a gene entity. It encodes yagF (protein.P77596). Encoded protein function: FUNCTION: Catalyzes the dehydration of D-xylonic acid to form 2-dehydro-3-deoxy-D-pentonate. {ECO:0000305|PubMed:23233208}. EcoCyc product frame: G6141-MONOMER. Genomic coordinates: 283201-285168. EcoCyc protein note: The YagF protein has D-xylonate dehydratase activity . A yjhG yagF double mutant can not use D-xylonate as the sole source of carbon, and crude cell extracts do not contain D-xylonate dehydratase activity . Both phenotypes are complemented by providing yjhG on a plasmid . Overexpression of yagF alleviates a bottleneck in the engineered production of glycolate . A yagF mutant is more resistant to the plant essential oil thymol than wild type .

## Biological Role

Repressed by xynR (protein.P77300).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77596|protein.P77596]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P77300|protein.P77300]] `RegulonDB` `C` - regulator=XynR; target=yagF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000923,ECOCYC:G6141,GeneID:944928`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:283201-285168:+; feature_type=gene
