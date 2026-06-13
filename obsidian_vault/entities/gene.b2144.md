---
entity_id: "gene.b2144"
entity_type: "gene"
name: "sanA"
source_database: "NCBI RefSeq"
source_id: "gene-b2144"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2144"
  - "sanA"
---

# sanA

`gene.b2144`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2144`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sanA (gene.b2144) is a gene entity. It encodes sanA (protein.P0AFY2). Encoded protein function: FUNCTION: Participates in the barrier function of the cell envelope. EcoCyc product frame: EG12025-MONOMER. EcoCyc synonyms: sfiXSt, yeiF. Genomic coordinates: 2232878-2233597. EcoCyc protein note: Multi-copy expression of sanA complements the vancomycin sensitivity of an E. coli K-12 mutant which exhibits outer membrane permeability defects (e.g. sensitivity to SDS, ethidium bromide, vancomycin, cold); a strain carrying a sanA null mutation (sanA::Tc) exhibits growth arrest at 43°C in the presence of vancomycin (see also ). Gene interaction assays implicate SanA in peptidoglycan-associated processes; SanA likely functions during periplasmic peptidoglycan biosynthesis . sanA is implicated in the stationary phase stress reponse; sanA is necessary for RpoS-dependent SDS resistance in carbon-limited stationary phase . sanA is transiently induced upon cold shock (15°C for 1 hour) . SanA is predicted to be a periplasmic protein, anchored to the inner membrane through its amino terminus . SanA is predicted to be a bitopic inner membrane protein . SanA is the sole member of the Vancomycin-sensitivity protein (SanA) family in the Transporter Classification Database . Overexpression of sanA from an ASKA plasmid leads to a more than 3-fold increase in the MIC of hypochlorous acid...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFY2|protein.P0AFY2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007091,ECOCYC:EG12025,GeneID:949003`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2232878-2233597:+; feature_type=gene
