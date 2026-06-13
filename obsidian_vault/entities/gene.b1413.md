---
entity_id: "gene.b1413"
entity_type: "gene"
name: "hrpA"
source_database: "NCBI RefSeq"
source_id: "gene-b1413"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1413"
  - "hrpA"
---

# hrpA

`gene.b1413`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1413`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hrpA (gene.b1413) is a gene entity. It encodes hrpA (protein.P43329). Encoded protein function: FUNCTION: Not yet known. EcoCyc product frame: G6732-MONOMER. Genomic coordinates: 1483061-1486963. EcoCyc protein note: HrpA belongs to the family of DEAH-box RNA helicases and has ATP-dependent 3'→5' RNA helicase activity . The helicase activity resides within the N-terminal 783 amino acids of HrpA, while the C-terminal region directly contacts the N-terminal region and appears to modulate its helicase activity . Crystal structures of apo-HrpA1-178, HrpA1-178 in complex with a ssRNA, and apo-HrpA1-178, D305A have been solved, showing that he enzyme undergoes large conformational changes upon RNA binding that are facilitated by alternative interdomain contacts involving the D305 residue. A K106A mutant within a conserved sequence motif of the RecA1-like domain of HrpA shows reduced ATPase activity. The "stacking triad" consisting of F655, P656, and F661 within the OB domain of HrpA is required for helicase activity . Further crystallization studies found functional N-terminal and C-terminal extensions. The N-terminal has an antiparallel helix-bundle domain (APHB) near the RecA-like domains that functions in ssDNA and ssRNA recognition and binding, and functions in RNA/RNA and RNA/DNA duplex unwinding...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P43329|protein.P43329]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004718,ECOCYC:G6732,GeneID:948444`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1483061-1486963:+; feature_type=gene
