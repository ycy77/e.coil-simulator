---
entity_id: "gene.b0484"
entity_type: "gene"
name: "copA"
source_database: "NCBI RefSeq"
source_id: "gene-b0484"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0484"
  - "copA"
---

# copA

`gene.b0484`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0484`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

copA (gene.b0484) is a gene entity. It encodes copA (protein.Q59385). Encoded protein function: FUNCTION: [Copper-exporting P-type ATPase]: Exports Cu(+) from the cytoplasm to the periplasm (PubMed:10639134, PubMed:11167016, PubMed:11500054, PubMed:12351646). Binds 2 Cu(+) ions per monomer, which are transferred to periplasmic copper chaperone CusF upon ATP hydrolysis (PubMed:24917681). In vitro an excess of CusF over CopA is required for efficient transfer (PubMed:24917681). May also be involved in silver export (PubMed:12351646, PubMed:12832075). {ECO:0000269|PubMed:10639134, ECO:0000269|PubMed:11167016, ECO:0000269|PubMed:11500054, ECO:0000269|PubMed:12351646, ECO:0000269|PubMed:12832075, ECO:0000269|PubMed:24917681}.; FUNCTION: [Isoform Soluble copper chaperone CopA(Z)]: mRNA is subject to programmed ribosomal frameshifting which produces a cytoplasmic copper chaperone CopA(Z) that corresponds to the first HMA domain (PubMed:28107647). The soluble form is essential for cell survivial in the presence of CuSO(4); in growth competition experiments between wild-type and a version that prevents expression of CopA(Z) after 50 generations the non-CopA(Z) version is nearly extinct (PubMed:28107647). The first HMA domain (residues 1-70) can be replaced by B.subtilis Cu chaperone CopZ (PubMed:25899340). {ECO:0000269|PubMed:25899340, ECO:0000269|PubMed:28107647}...

## Biological Role

Repressed by DNA-binding transcriptional dual regulator OmpR-phosphorylated (complex.ecocyc.PHOSPHO-OMPR). Activated by rpoD (protein.P00579), cueR (protein.P0A9G4).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q59385|protein.Q59385]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=copA; function=+
- `activates` <-- [[protein.P0A9G4|protein.P0A9G4]] `RegulonDB` `C` - regulator=CueR; target=copA; function=+
- `represses` <-- [[complex.ecocyc.PHOSPHO-OMPR|complex.ecocyc.PHOSPHO-OMPR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001681,ECOCYC:G6260,GeneID:946106`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:508875-511379:-; feature_type=gene
