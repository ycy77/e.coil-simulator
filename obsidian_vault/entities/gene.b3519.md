---
entity_id: "gene.b3519"
entity_type: "gene"
name: "treF"
source_database: "NCBI RefSeq"
source_id: "gene-b3519"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3519"
  - "treF"
---

# treF

`gene.b3519`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3519`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

treF (gene.b3519) is a gene entity. It encodes treF (protein.P62601). Encoded protein function: FUNCTION: Hydrolyzes trehalose to glucose. Could be involved, in cells returning to low osmolarity conditions, in the utilization of the accumulated cytoplasmic trehalose, which was synthesized in response to high osmolarity. EcoCyc product frame: TREHALACYTO-MONOMER. Genomic coordinates: 3669592-3671241. EcoCyc protein note: E. coli contains two trehalases: the cytoplasmic TreF (discussed here) and the periplasmic TREHALAPERI-MONOMER "TreA". Both enzymes catalyze the hydrolysis of trehalose into two molecules of D-glucose. Transcription of treF is only weakly induced by high osmolarity and partially dependent on the stationary-phase alternative sigma factor RpoS . Under aerobic conditions, TreF protein is induced more than 20-fold by high osmolarity .

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P62601|protein.P62601]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011497,ECOCYC:EG12245,GeneID:948037`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3669592-3671241:+; feature_type=gene
