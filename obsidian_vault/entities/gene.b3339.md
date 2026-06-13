---
entity_id: "gene.b3339"
entity_type: "gene"
name: "tufA"
source_database: "NCBI RefSeq"
source_id: "gene-b3339"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3339"
  - "tufA"
---

# tufA

`gene.b3339`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3339`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tufA (gene.b3339) is a gene entity. It encodes tufA (protein.P0CE47). Encoded protein function: FUNCTION: GTP hydrolase that promotes the GTP-dependent binding of aminoacyl-tRNA to the A-site of ribosomes during protein biosynthesis. {ECO:0000269|PubMed:2157708, ECO:0000269|PubMed:2684669}.; FUNCTION: May play an important regulatory role in cell growth and in the bacterial response to nutrient deprivation.; FUNCTION: Plays a stimulatory role in trans-translation; binds tmRNA. {ECO:0000269|PubMed:15069072}.; FUNCTION: Protects glycyl-tRNA(Gly) from hydrolysis by E.coli D-aminoacyl-tRNA deacylase (dtd) (By similarity). {ECO:0000250|UniProtKB:Q5SHN6}.; FUNCTION: (Microbial infection) Upon infection by bacteriophage Qbeta, part of the viral RNA-dependent RNA polymerase complex. With EF-Ts may provide a stabilizing scaffold for the beta (catalytic) subunit. Helps separate the double-stranded RNA of the template and growing RNA during elongation. With the beta subunit helps form the exit tunnel for template RNA. {ECO:0000269|PubMed:816798, ECO:0000305}.; FUNCTION: (Microbial infection) Required for the tRNase activity of CdiA-CT from E.coli strain EC869; the toxic CT module is thought to cleave tRNA in the context of translationally active GTP EF-Tu-aa-tRNA complexes. GTP is required for tRNase activity but is not hydrolyzed...

## Biological Role

Activated by rpoD (protein.P00579), rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0CE47|protein.P0CE47]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=tufA; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=tufA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010912,ECOCYC:EG11036,GeneID:947838`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3470145-3471329:-; feature_type=gene
