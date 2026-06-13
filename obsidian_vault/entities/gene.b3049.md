---
entity_id: "gene.b3049"
entity_type: "gene"
name: "glgS"
source_database: "NCBI RefSeq"
source_id: "gene-b3049"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3049"
  - "glgS"
---

# glgS

`gene.b3049`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3049`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glgS (gene.b3049) is a gene entity. It encodes glgS (protein.P26649). Encoded protein function: FUNCTION: Major determinant of cell surface composition. Negatively regulates motility, adhesion and synthesis of biofilm exopolysaccharides. {ECO:0000255|HAMAP-Rule:MF_00525, ECO:0000269|PubMed:23537328}. EcoCyc product frame: EG11381-MONOMER. EcoCyc synonyms: scoR. Genomic coordinates: 3191739-3191939. EcoCyc protein note: GlgS negatively regulates flagellar motility and production of biofilm polysaccharides . Since a glgS null mutation inhibits glycogen synthesis and overproduction of GlgS stimulates synthesis of glycogen , GlgS was thought to be involved in the regulation of glycogen biosynthesis . However, because motility and biosynthesis of extracellular polysaccharides normally compete with glycogen biosynthesis for the same metabolite pools, the effect of GlgS on glycogen biosynthesis is now thought to be indirect . Expression of glgS is dependent on RpoS and induced in stationary phase . CsrA negatively regulates glgS expression . glgS mutants accumulate high levels of AMP , are hyperflagellated and hyperfimbriated, and show elevated swarming motility and increased biofilm formation . Solution structures of GlgS have been obtained . GlgS shows similarity to proteins involved in protein-protein interactions, suggesting a similar role for GlgS...

## Biological Role

Activated by rob (protein.P0ACI0), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P26649|protein.P26649]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACI0|protein.P0ACI0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=glgS; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010007,ECOCYC:EG11381,GeneID:947533`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3191739-3191939:-; feature_type=gene
