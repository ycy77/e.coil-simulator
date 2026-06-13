---
entity_id: "gene.b1478"
entity_type: "gene"
name: "adhP"
source_database: "NCBI RefSeq"
source_id: "gene-b1478"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1478"
  - "adhP"
---

# adhP

`gene.b1478`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1478`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

adhP (gene.b1478) is a gene entity. It encodes adhP (protein.P39451). Encoded protein function: FUNCTION: Preferred specificity is towards 1-propanol. EcoCyc product frame: ADHP-MONOMER. EcoCyc synonyms: yddN. Genomic coordinates: 1552828-1553838.

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00071` Fatty acid degradation (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00625` Chloroalkane and chloroalkene degradation (KEGG)
- `eco00626` Naphthalene degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39451|protein.P39451]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=adhP; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004928,ECOCYC:G6775,GeneID:946036`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1552828-1553838:-; feature_type=gene
