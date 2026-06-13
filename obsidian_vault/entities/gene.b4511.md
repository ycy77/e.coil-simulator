---
entity_id: "gene.b4511"
entity_type: "gene"
name: "ybdZ"
source_database: "NCBI RefSeq"
source_id: "gene-b4511"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4511"
  - "ybdZ"
---

# ybdZ

`gene.b4511`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4511`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybdZ (gene.b4511) is a gene entity. It encodes ybdZ (protein.P18393). Encoded protein function: FUNCTION: Involved in the biosynthesis of the siderophore enterobactin (enterochelin), which is a macrocyclic trimeric lactone of N-(2,3-dihydroxybenzoyl)-serine. Plays a role in the catalytic function of EntF. It is required for adenylation of amino acids in non-ribosomal peptide biosynthesis. {ECO:0000269|PubMed:20845982}. EcoCyc product frame: MONOMER0-2659. Genomic coordinates: 613942-614160. EcoCyc protein note: YbdZ is an MbtH-like protein (MLP) that plays a role in amino acid activation by ENTF-MONOMER EntF . MLPs are required for adenylation of amino acids in non-ribosomal peptide biosynthesis. YbdZ enhances the catalytic function of EntF by reducing its KM for serine . A crystal structure of YbdZ bound to EntF has been solved at 3 Å resolution . Alanine scanning mutagenesis of the entire YbdZ allowed identification of residues that are required for in vivo function. The effect of individual mutations on the expression of YbdZ and its ability to interact with and enhance EntF's activity varied considerably . A ybdZ in-frame deletion strain has a growth defect under iron-limiting conditions . MLPs from other organisms can rescue the growth defect to varying extents .

## Biological Role

Repressed by fur (protein.P0A9A9). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P18393|protein.P18393]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ybdZ; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=ybdZ; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=ybdZ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0285032,ECOCYC:G0-10437,GeneID:1450243`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:613942-614160:+; feature_type=gene
