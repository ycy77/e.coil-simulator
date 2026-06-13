---
entity_id: "gene.b1178"
entity_type: "gene"
name: "pliG"
source_database: "NCBI RefSeq"
source_id: "gene-b1178"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1178"
  - "pliG"
---

# pliG

`gene.b1178`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1178`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pliG (gene.b1178) is a gene entity. It encodes pliG (protein.P76002). Encoded protein function: FUNCTION: Inhibits activity of g-type lysozyme, which confers increased lysozyme tolerance to the bacterium. {ECO:0000269|PubMed:20734102}. EcoCyc product frame: G6615-MONOMER. EcoCyc synonyms: ycgK. Genomic coordinates: 1227071-1227472. EcoCyc protein note: The PliG protein inhibits activity of g-type lysozyme in vitro . pliG deletion mutants show increased sensitivity to g-type lysozyme in the presence of EDTA . PliG contains a conserved bacterial prepeptidase C terminal (PPC) domain . Structural and mutational data has identified a putative lysozyme interaction interface . Targeting of YcgK to the Sec-translocase for transport across the inner membrane is SecB-dependent . pliG: periplasmic lysozme inhibitor of g-type lysozyme . Related review:

## Biological Role

Repressed by zur (protein.P0AC51). Activated by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76002|protein.P76002]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=pliG; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0AC51|protein.P0AC51]] `RegulonDB` `S` - regulator=Zur; target=pliG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003948,ECOCYC:G6615,GeneID:946963`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1227071-1227472:-; feature_type=gene
