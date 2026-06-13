---
entity_id: "gene.b3683"
entity_type: "gene"
name: "glvC"
source_database: "NCBI RefSeq"
source_id: "gene-b3683"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3683"
  - "glvC"
---

# glvC

`gene.b3683`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3683`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glvC (gene.b3683) is a gene entity. It encodes glvC (protein.P31452). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitant with their translocation across the cell membrane. This operon may be cryptic in wild-type K12 strains (Probable). {ECO:0000250, ECO:0000305|PubMed:8019415}. EcoCyc product frame: GLVC-MONOMER. EcoCyc synonyms: ptiC. Genomic coordinates: 3862497-3863603. EcoCyc protein note: The deduced amino acid sequence of GlvC displays similarity with MALX-MONOMER "MalX" and with the IIC domains of NAGE-MONOMER "NagE" (Enzyme II of the N-acetylglucosamine PTS) and PTSG-MONOMER "PtsG" (Enzyme IIBC of the glucose PTS); the glv operon (glvCBG) may be cryptic in wild type E. coli K-12 . Expression of glvC is decreased in a luxS deletion mutant during growth in LB (no glucose) . glvC and glvB are pseudogene candidates in E. coli K-12. The genome of E. coli O157 contains a complete glvC homolog .

## Biological Role

Repressed by hns (protein.P0ACF8).

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
- `encodes` --> [[protein.P31452|protein.P31452]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012043,ECOCYC:EG11710,GeneID:2847721`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3862497-3863603:-; feature_type=gene
