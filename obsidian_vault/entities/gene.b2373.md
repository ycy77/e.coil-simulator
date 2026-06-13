---
entity_id: "gene.b2373"
entity_type: "gene"
name: "oxc"
source_database: "NCBI RefSeq"
source_id: "gene-b2373"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2373"
  - "oxc"
---

# oxc

`gene.b2373`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2373`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

oxc (gene.b2373) is a gene entity. It encodes oxc (protein.P0AFI0). Encoded protein function: FUNCTION: Involved in the catabolism of oxalate and in the adapatation to low pH via the induction of the oxalate-dependent acid tolerance response (ATR). Catalyzes the decarboxylation of oxalyl-CoA to yield carbon dioxide and formyl-CoA. {ECO:0000269|PubMed:20553497}. EcoCyc product frame: G7236-MONOMER. EcoCyc synonyms: yfdU. Genomic coordinates: 2490256-2491950.

## Biological Role

Repressed by hns (protein.P0ACF8), glaR (protein.P37338). Activated by evgA (protein.P0ACZ4).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFI0|protein.P0AFI0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACZ4|protein.P0ACZ4]] `RegulonDB` `S` - regulator=EvgA; target=oxc; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=oxc; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007826,ECOCYC:G7236,GeneID:946845`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2490256-2491950:-; feature_type=gene
