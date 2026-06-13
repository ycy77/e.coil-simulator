---
entity_id: "gene.b3492"
entity_type: "gene"
name: "yhiN"
source_database: "NCBI RefSeq"
source_id: "gene-b3492"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3492"
  - "yhiN"
---

# yhiN

`gene.b3492`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3492`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhiN (gene.b3492) is a gene entity. It encodes rdsA (protein.P37631). Encoded protein function: FUNCTION: Catalyzes the synthesis of 5,6-dihydrouridine (D) at position 2449 in 23S rRNA (PubMed:39078675). Can use NADH as a source of reducing equivalents but not NADPH (PubMed:39078675). {ECO:0000269|PubMed:39078675}. EcoCyc product frame: EG12229-MONOMER. EcoCyc synonyms: yhiN. Genomic coordinates: 3636208-3637410. EcoCyc protein note: The RdsA is responsible for the dihydrouridylation of uridine 2449 in 23S-rRNAs. Using the rhodamine labelling method (Rho-seq) for detecting dihydrouridine (D) in position 2449 of 23S rRNAs and rRNA from various mutant E. coli strains, only the ΔrdsA BW25113 strain lacked D2449. Characterization of RdsA using an AlphaFold model and homologous structures found it to be a flavoprotein with a conserved FAD binding pocket that binds FAD noncovalently . Kinetic analyses measured NADH rather than NADPH oxidase activity with hydride transfer being the likely chemical mechanism . RdsA = ribosomal dihydrouridine synthase A

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37631|protein.P37631]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011402,ECOCYC:EG12229,GeneID:947996`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3636208-3637410:-; feature_type=gene
