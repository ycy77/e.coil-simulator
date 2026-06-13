---
entity_id: "gene.b2558"
entity_type: "gene"
name: "mltF"
source_database: "NCBI RefSeq"
source_id: "gene-b2558"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2558"
  - "mltF"
---

# mltF

`gene.b2558`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2558`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mltF (gene.b2558) is a gene entity. It encodes mltF (protein.P0AGC5). Encoded protein function: FUNCTION: Murein-degrading enzyme that degrades murein glycan strands and insoluble, high-molecular weight murein sacculi, with the concomitant formation of a 1,6-anhydromuramoyl product. Lytic transglycosylases (LTs) play an integral role in the metabolism of the peptidoglycan (PG) sacculus. Their lytic action creates space within the PG sacculus to allow for its expansion as well as for the insertion of various structures such as secretion systems and flagella. EcoCyc product frame: EG11373-MONOMER. EcoCyc synonyms: yfhD. Genomic coordinates: 2695801-2697357. EcoCyc protein note: mltF encodes a membrane bound lytic murein transglycosylase which cleaves the β-1,4 glycosidic bond between N-acetylglucosamine (GlcNAc) and N-acetylmuramic acid (MurNAc) residues of peptidoglycan (PG) with the concomitant formation of a 1,6-anhydro ring at the MurNAc residue. mtlF encodes a predicted protein with a cleavable signal sequence, an N-terminal non-glycosylase domain and a C-terminal domain with glycosyltransferase activity; MtlF is an outer membrane associated protein...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGC5|protein.P0AGC5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008417,ECOCYC:EG11373,GeneID:947028`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2695801-2697357:+; feature_type=gene
