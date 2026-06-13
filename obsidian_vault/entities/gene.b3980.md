---
entity_id: "gene.b3980"
entity_type: "gene"
name: "tufB"
source_database: "NCBI RefSeq"
source_id: "gene-b3980"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3980"
  - "tufB"
---

# tufB

`gene.b3980`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3980`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tufB (gene.b3980) is a gene entity. It encodes tufB (protein.P0CE48). Encoded protein function: FUNCTION: GTP hydrolase that promotes the GTP-dependent binding of aminoacyl-tRNA to the A-site of ribosomes during protein biosynthesis. {ECO:0000255|HAMAP-Rule:MF_00118}.; FUNCTION: May play an important regulatory role in cell growth and in the bacterial response to nutrient deprivation.; FUNCTION: Plays a stimulatory role in trans-translation, binds tmRNA. {ECO:0000269|PubMed:15069072}.; FUNCTION: Protects glycyl-tRNA(Gly) from hydrolysis by D-aminoacyl-tRNA deacylase (dtd) (By similarity). {ECO:0000250|UniProtKB:Q5SHN6}.; FUNCTION: (Microbial infection) Upon infection by bacteriophage Qbeta, part of the viral RNA-dependent RNA polymerase complex. With EF-Ts may provide a stabilizing scaffold for the beta (catalytic) subunit. Helps separate the double-stranded RNA of the template and growing RNA during elongation (PubMed:22245970). With the beta subunit helps form the exit tunnel for template RNA. The GTPase activity of this subunit is not required for viral RNA replication (PubMed:20798060). {ECO:0000269|PubMed:20534494, ECO:0000269|PubMed:20798060, ECO:0000269|PubMed:22245970, ECO:0000269|PubMed:22884418, ECO:0000269|PubMed:25122749, ECO:0000269|PubMed:816798}. EcoCyc product frame: EG11037-MONOMER. EcoCyc synonyms: pulT, kirT. Genomic coordinates: 4175944-4177128...

## Biological Role

Activated by fis (protein.P0A6R3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0CE48|protein.P0CE48]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=tufB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013020,ECOCYC:EG11037,GeneID:948482`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4175944-4177128:+; feature_type=gene
