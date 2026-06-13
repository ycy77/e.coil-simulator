---
entity_id: "gene.b4198"
entity_type: "gene"
name: "ulaF"
source_database: "NCBI RefSeq"
source_id: "gene-b4198"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4198"
  - "ulaF"
---

# ulaF

`gene.b4198`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4198`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ulaF (gene.b4198) is a gene entity. It encodes ulaF (protein.P39306). Encoded protein function: FUNCTION: Catalyzes the isomerization of L-ribulose 5-phosphate to D-xylulose 5-phosphate. Is involved in the anaerobic L-ascorbate utilization. {ECO:0000255|HAMAP-Rule:MF_01952, ECO:0000269|PubMed:11741871}. EcoCyc product frame: G7860-MONOMER. EcoCyc synonyms: yjfX, sgaE. Genomic coordinates: 4423700-4424386. EcoCyc protein note: L-ribulose 5-phosphate 4-epimerase is an enzyme in the pathway of anaerobic L-ascorbate degradation . UlaF: "utilization of L-ascorbate"

## Biological Role

Repressed by ulaR (protein.P0A9W0). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39306|protein.P39306]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=ulaF; function=+
- `represses` <-- [[protein.P0A9W0|protein.P0A9W0]] `RegulonDB` `S` - regulator=UlaR; target=ulaF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013734,ECOCYC:G7860,GeneID:948711`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4423700-4424386:+; feature_type=gene
