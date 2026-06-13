---
entity_id: "gene.b3425"
entity_type: "gene"
name: "glpE"
source_database: "NCBI RefSeq"
source_id: "gene-b3425"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3425"
  - "glpE"
---

# glpE

`gene.b3425`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3425`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glpE (gene.b3425) is a gene entity. It encodes glpE (protein.P0A6V5). Encoded protein function: FUNCTION: Transferase that catalyzes the transfer of sulfur from thiosulfate to thiophilic acceptors such as cyanide or dithiols (PubMed:10735872). May function in a CysM-independent thiosulfate assimilation pathway by catalyzing the conversion of thiosulfate to sulfite, which can then be used for L-cysteine biosynthesis (PubMed:28756590). The relatively low affinity of GlpE for both thiosulfate and cyanide suggests that these compounds may not be physiological substrates (PubMed:10735872). Thioredoxin 1 or related dithiol proteins could be the physiological sulfur acceptor (PubMed:10735872). {ECO:0000269|PubMed:10735872, ECO:0000269|PubMed:28756590}. EcoCyc product frame: EG10395-MONOMER. Genomic coordinates: 3561497-3561823.

## Biological Role

Repressed by arcA (protein.P0A9Q1). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6V5|protein.P0A6V5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=glpE; function=+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=glpE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011182,ECOCYC:EG10395,GeneID:947935`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3561497-3561823:-; feature_type=gene
