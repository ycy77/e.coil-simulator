---
entity_id: "gene.b0712"
entity_type: "gene"
name: "pxpC"
source_database: "NCBI RefSeq"
source_id: "gene-b0712"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0712"
  - "pxpC"
---

# pxpC

`gene.b0712`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0712`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pxpC (gene.b0712) is a gene entity. It encodes pxpC (protein.P75745). Encoded protein function: FUNCTION: Catalyzes the cleavage of 5-oxoproline to form L-glutamate coupled to the hydrolysis of ATP to ADP and inorganic phosphate. {ECO:0000269|PubMed:28830929}. EcoCyc product frame: G6381-MONOMER. EcoCyc synonyms: ybgK. Genomic coordinates: 744243-745175. EcoCyc protein note: Overexpression of pxpBCA leads to the presence of detectable oxoprolinase activity in cell lysates. A pxpC deletion mutant grows to a lower OD than wild type in minimal medium with ammonium as the sole source of nitrogen . PxpC: "prokaryotic 5-oxoprolinase C"

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75745|protein.P75745]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002428,ECOCYC:G6381,GeneID:945317`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:744243-745175:+; feature_type=gene
