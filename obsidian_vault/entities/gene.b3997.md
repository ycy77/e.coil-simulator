---
entity_id: "gene.b3997"
entity_type: "gene"
name: "hemE"
source_database: "NCBI RefSeq"
source_id: "gene-b3997"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3997"
  - "hemE"
---

# hemE

`gene.b3997`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3997`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hemE (gene.b3997) is a gene entity. It encodes hemE (protein.P29680). Encoded protein function: FUNCTION: Catalyzes the decarboxylation of four acetate groups of uroporphyrinogen-III to yield coproporphyrinogen-III. {ECO:0000255|HAMAP-Rule:MF_00218}. EcoCyc product frame: UROGENDECARBOX-MONOMER. Genomic coordinates: 4197716-4198780. EcoCyc protein note: Uroporphyrinogen decarboxylase catalyzes the decarboxylation of all four acetate residues of uroporphyrinogen III to generate coproporphyrinogen III. This is the first committed step after the branch point between heme and siroheme biosynthesis. The E. coli enzyme has not been biochemically studied. A hemE mutant accumulates uroporphyrinogen III .

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P29680|protein.P29680]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013066,ECOCYC:EG11543,GeneID:948497`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4197716-4198780:+; feature_type=gene
