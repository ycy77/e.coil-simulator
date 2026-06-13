---
entity_id: "gene.b0839"
entity_type: "gene"
name: "dacC"
source_database: "NCBI RefSeq"
source_id: "gene-b0839"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0839"
  - "dacC"
---

# dacC

`gene.b0839`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0839`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dacC (gene.b0839) is a gene entity. It encodes dacC (protein.P08506). Encoded protein function: FUNCTION: Removes C-terminal D-alanyl residues from sugar-peptide cell wall precursors. EcoCyc product frame: EG10203-MONOMER. Genomic coordinates: 880727-881929.

## Biological Role

Repressed by ArgR-L-arginine DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-228), argR (protein.P0A6D0).

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08506|protein.P08506]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[complex.ecocyc.CPLX0-228|complex.ecocyc.CPLX0-228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=dacC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002860,ECOCYC:EG10203,GeneID:945455`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:880727-881929:+; feature_type=gene
