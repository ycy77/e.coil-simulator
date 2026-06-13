---
entity_id: "gene.b4197"
entity_type: "gene"
name: "ulaE"
source_database: "NCBI RefSeq"
source_id: "gene-b4197"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4197"
  - "ulaE"
---

# ulaE

`gene.b4197`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4197`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ulaE (gene.b4197) is a gene entity. It encodes ulaE (protein.P39305). Encoded protein function: FUNCTION: Catalyzes the isomerization of L-xylulose-5-phosphate to L-ribulose-5-phosphate. Is involved in the anaerobic L-ascorbate utilization. {ECO:0000255|HAMAP-Rule:MF_01951, ECO:0000269|PubMed:11741871}. EcoCyc product frame: G7859-MONOMER. EcoCyc synonyms: sgaU, yjfW. Genomic coordinates: 4422846-4423700. EcoCyc protein note: L-xylulose 5-phosphate 3-epimerase is an enzyme in the pathway of anaerobic L-ascorbate degradation. The crystal structure of the enzyme from E. coli O157:H7 has been solved, showing a dimeric enzyme with a TIM-barrel fold . UlaE: "utilization of L-ascorbate"

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

- `encodes` --> [[protein.P39305|protein.P39305]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=ulaE; function=+
- `represses` <-- [[protein.P0A9W0|protein.P0A9W0]] `RegulonDB` `S` - regulator=UlaR; target=ulaE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013732,ECOCYC:G7859,GeneID:948712`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4422846-4423700:+; feature_type=gene
