---
entity_id: "gene.b2747"
entity_type: "gene"
name: "ispD"
source_database: "NCBI RefSeq"
source_id: "gene-b2747"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2747"
  - "ispD"
---

# ispD

`gene.b2747`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2747`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ispD (gene.b2747) is a gene entity. It encodes ispD (protein.Q46893). Encoded protein function: FUNCTION: Catalyzes the formation of 4-diphosphocytidyl-2-C-methyl-D-erythritol from CTP and 2-C-methyl-D-erythritol 4-phosphate (MEP). EcoCyc product frame: G7423-MONOMER. EcoCyc synonyms: ygbP. Genomic coordinates: 2871780-2872490.

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46893|protein.Q46893]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ispD; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009017,ECOCYC:G7423,GeneID:948269`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2871780-2872490:-; feature_type=gene
