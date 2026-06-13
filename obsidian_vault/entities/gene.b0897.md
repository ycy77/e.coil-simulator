---
entity_id: "gene.b0897"
entity_type: "gene"
name: "ycaC"
source_database: "NCBI RefSeq"
source_id: "gene-b0897"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0897"
  - "ycaC"
---

# ycaC

`gene.b0897`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0897`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycaC (gene.b0897) is a gene entity. It encodes ycaC (protein.P21367). Encoded protein function: Probable hydrolase YcaC (EC 4.-.-.-) EcoCyc product frame: EG11241-MONOMER. Genomic coordinates: 944931-945557. EcoCyc protein note: The crystal structure of YcaC, solved at 1.8 Å resolution, indicates that YcaC has similarity to hydrolases and forms a homooctamer (a dimer of tetrameric ring structures) . The protein shows structural similarity to the pyrazinamidase encoded by the Pyrococcus horikoshii 999 gene . Cys118 is identified as a likely catalytic residue . A ΔycaC mutant shows increased resistance to the proline-rich antimicrobial peptide (PrAMP) apidaecin 1b and the designer peptide Api88 .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P21367|protein.P21367]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ycaC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003050,ECOCYC:EG11241,GeneID:945512`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:944931-945557:-; feature_type=gene
