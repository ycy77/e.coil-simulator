---
entity_id: "gene.b1064"
entity_type: "gene"
name: "grxB"
source_database: "NCBI RefSeq"
source_id: "gene-b1064"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1064"
  - "grxB"
---

# grxB

`gene.b1064`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1064`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

grxB (gene.b1064) is a gene entity. It encodes grxB (protein.P0AC59). Encoded protein function: FUNCTION: Involved in reducing some disulfide bonds in a coupled system with glutathione reductase. Does not act as hydrogen donor for ribonucleotide reductase. EcoCyc product frame: OX-GLUTAREDOXIN-B. Genomic coordinates: 1123407-1124054. EcoCyc protein note: Glutaredoxins are ubiquitous proteins that catalyze the reduction of disulfides via reduced glutathione (GSH). Escherichia coli has three glutaredoxins (Grx1, Grx2, and Grx3) containing the classic dithiol active site CPYC, and a fourth one which contains a monothiol (CGFS) potential active site . The glutaredoxins do not act as enzymes, but rather as a cofactor, enabling intracellular redox reactions through a disulfide/dithiol enzymatic mechanism involving the active site cysteines. There is almost no similarity between the amino acid sequence of Grx2 (an approximately 27 kDa protein) and Grx1 or Grx3 (both 9-kDa proteins), with the exception of the active site which is identical in all three glutaredoxins. In contrast to glutaredoxin 1 and 3, Grx 2 is not a hydrogen donor for ribonucleotide reductase. On the other hand, Grx2 is the primary hydrogen donor to ArsC-catalyzed arsenate reduction (RXN-982) . It is also the most abundant glutaredoxin in the cell, with an intracellular concentration of 5 µM, compared with 0...

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC59|protein.P0AC59]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003615,ECOCYC:EG12688,GeneID:946926`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1123407-1124054:-; feature_type=gene
