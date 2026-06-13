---
entity_id: "gene.b1552"
entity_type: "gene"
name: "cspI"
source_database: "NCBI RefSeq"
source_id: "gene-b1552"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1552"
  - "cspI"
---

# cspI

`gene.b1552`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1552`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cspI (gene.b1552) is a gene entity. It encodes cspI (protein.P0A986). Encoded protein function: Cold shock-like protein CspI (CPS-I) EcoCyc product frame: G6825-MONOMER. EcoCyc synonyms: cspJ. Genomic coordinates: 1638455-1638667. EcoCyc protein note: CspI is a cold shock protein with complex regulation. CspI protein levels are highest between 10-15°C . cspI belongs to a small set of genes whose expression is upregulated and whose absence is a competitive disadvantage in long-term stationary phase (LTSP) . Expression of cspI is transiently induced upon cold shock. In addition, at 37°C, cspI mRNA is unstable, with a half life of ~20 seconds; after 1 hour of temperature downshift, the cspI half life increases dramatically to 14 minutes. The 5' UTR of the cspI mRNA negatively affects its own expression at 37°C . In defined rich medium at 37°C, expression of cspI is highest in mid-log phase. Transcription of cspI is induced by cold shock in both defined rich and defined minimal media . Regulation of cspI expression by CRP appears to be indirect . Expression of cspI is upregulated in LTSP, and it is expressed at higher levels in LTSP than in any other growth phase. A cspI mutant has a competitive disadvantage compared to wild-type in LTSP . An in-silico comparative study of evolution, structure and function was carried out for the 9 CspA family of proteins in E. coli K-12...

## Biological Role

Activated by basR (protein.P30843).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A986|protein.P0A986]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P30843|protein.P30843]] `RegulonDB` `S` - regulator=BasR; target=cspI; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005183,ECOCYC:G6825,GeneID:946099`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1638455-1638667:-; feature_type=gene
