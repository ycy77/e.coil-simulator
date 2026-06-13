---
entity_id: "gene.b3682"
entity_type: "gene"
name: "glvB"
source_database: "NCBI RefSeq"
source_id: "gene-b3682"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3682"
  - "glvB"
---

# glvB

`gene.b3682`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3682`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glvB (gene.b3682) is a gene entity. It encodes glvB (protein.P69789). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. This operon may be cryptic in wild-type K12 strains (Probable). {ECO:0000250, ECO:0000305|PubMed:8019415}. EcoCyc product frame: GLVB-MONOMER. EcoCyc synonyms: yidN, yidO. Genomic coordinates: 3861987-3862472. EcoCyc protein note: The deduced amino acid sequence of GlvB shows similarity with the IIB domain of various Enzyme II proteins (including NAGE-MONOMER "NagE" - Enzyme II of the N-acetylglucosamine PTS - and PTSG-MONOMER "PtsG" - Enzyme IIBC of the glucose PTS) and contains a conserved cysteine residue (Cys92); the glv operon (glvCBG) may be cryptic in wild type E. coli K-12 . glvB is a pseudogene candidate in E. coli K-12 .

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R04111|reaction.R04111]] `KEGG` `database` - via EC:2.7.1.208
- `encodes` --> [[protein.P69789|protein.P69789]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012038,ECOCYC:EG11709,GeneID:2847722`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3861987-3862472:-; feature_type=gene
