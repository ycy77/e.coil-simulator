---
entity_id: "gene.b0566"
entity_type: "gene"
name: "envY"
source_database: "NCBI RefSeq"
source_id: "gene-b0566"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0566"
  - "envY"
---

# envY

`gene.b0566`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0566`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

envY (gene.b0566) is a gene entity. It encodes envY (protein.P10805). Encoded protein function: FUNCTION: Influences the temperature-dependent expression of several E.coli envelope proteins, most notably the porins OmpF and OmpC and the lambda receptor, LamB. EcoCyc product frame: PD00969. Genomic coordinates: 586147-586908. EcoCyc protein note: EnvY is a DNA-binding transcriptional regulator that participates in the control of several genes that encode cellular envelope proteins at low temperatures and during stationary phase . This protein is an envelope protein that contains a putative membrane-spanning region, and as for the members of the family of transcriptional regulators (AraC/XylS) that it pertains to , it also contains a helix-turn-helix motif for DNA binding in the C-terminal region . The transcriptional regulators of E. coli that show higher similarity to EnvR are AppY and AdiY . The latter, like EnvY, also has a putative transmembrane region . No research has been done to determine the DNA-binding sites for EnvY. The regulation of envY has not been described yet, but a region of dyad symmetry has been found upstream of this gene . EnvY was transcriptionally upregulated in iron excess over iron limitation at 6.3% dissolved oxygen as determined by RNA-seq...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P10805|protein.P10805]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001935,ECOCYC:EG10268,GeneID:949114`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:586147-586908:-; feature_type=gene
