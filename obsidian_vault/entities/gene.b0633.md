---
entity_id: "gene.b0633"
entity_type: "gene"
name: "rlpA"
source_database: "NCBI RefSeq"
source_id: "gene-b0633"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0633"
  - "rlpA"
---

# rlpA

`gene.b0633`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0633`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rlpA (gene.b0633) is a gene entity. It encodes rlpA (protein.P10100). Encoded protein function: FUNCTION: Lytic transglycosylase with a strong preference for naked glycan strands that lack stem peptides. {ECO:0000255|HAMAP-Rule:MF_02071}. EcoCyc product frame: EG10854-MONOMER. Genomic coordinates: 664102-665190. EcoCyc protein note: rlpA encodes a minor lipoprotein; the unprocessed protein has an apparent molecular weight of 54 kDa (by SDS-PAGE) despite a calculated molecular weight of ~36 kDa; in vitro expression of a mature protein is inhibited by treatment with the signal peptidase II inhibitor, globomycin; the protein incorporates 3H-labeled palmitate and 3H-labeled glycerol in vitro . A truncated version of RlpA (first 102 residues) suppresses the conditional lethal phenotype of a EG10760 prc null mutation by an unknown mechanism . An RlpA fluorescent fusion protein (RlpA-RFP) accumulates at cell division sites, but is also localized elsewhere in the cell envelope; the isolated, labeled SPOR domain of RlpA (residues 281-362) accumulates at division sites and not in any other nonhomogenous pattern; deletion of rlpA does not result in cell growth or division defects (see also ). The isolated, labeled SPOR domain of RlpA localizes to septal peptidoglycan in purified E...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P10100|protein.P10100]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002171,ECOCYC:EG10854,GeneID:945241`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:664102-665190:-; feature_type=gene
