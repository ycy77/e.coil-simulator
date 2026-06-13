---
entity_id: "gene.b3426"
entity_type: "gene"
name: "glpD"
source_database: "NCBI RefSeq"
source_id: "gene-b3426"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3426"
  - "glpD"
---

# glpD

`gene.b3426`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3426`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glpD (gene.b3426) is a gene entity. It encodes glpD (protein.P13035). Encoded protein function: FUNCTION: Conversion of glycerol 3-phosphate to dihydroxyacetone. Uses molecular oxygen or nitrate as electron acceptor. EcoCyc product frame: AERGLYC3PDEHYDROG-MONOMER. EcoCyc synonyms: glyD. Genomic coordinates: 3562013-3563518.

## Biological Role

Repressed by arcA (protein.P0A9Q1), glpR (protein.P0ACL0). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P13035|protein.P13035]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=glpD; function=+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=glpD; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACL0|protein.P0ACL0]] `RegulonDB` `S` - regulator=GlpR; target=glpD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011191,ECOCYC:EG10394,GeneID:947934`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3562013-3563518:+; feature_type=gene
