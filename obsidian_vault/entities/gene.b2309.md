---
entity_id: "gene.b2309"
entity_type: "gene"
name: "hisJ"
source_database: "NCBI RefSeq"
source_id: "gene-b2309"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2309"
  - "hisJ"
---

# hisJ

`gene.b2309`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2309`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hisJ (gene.b2309) is a gene entity. It encodes hisJ (protein.P0AEU0). Encoded protein function: FUNCTION: Part of the ABC transporter complex HisPMQJ involved in histidine transport (By similarity). Binds histidine (By similarity). Interacts with HisQMP and stimulates ATPase activity of HisP, which results in histidine translocation (By similarity). {ECO:0000250|UniProtKB:P02910}. EcoCyc product frame: HISJ-MONOMER. Genomic coordinates: 2426006-2426788. EcoCyc protein note: HisJ is the periplasmic binding protein of an ATP-dependent histidine uptake system. HisJ, purified in the presence of histidine and crystallized, contains two globular domains of similar arrangement connected by a two strand hinge; histidine binds in a deep cleft between the two domains and is held in place by hydrogen bonds, Van der Waals contacts and salt links . Molecular dynamics simulations suggest that HisJ employs a 'Venus fly-trap' type movement where the protein transitions from an open to closed conformation and provide support for the contention that apo-HisJ can transition to a closed form even in the absence of ligand .

## Biological Role

Repressed by argR (protein.P0A6D0). Activated by NtrC phosphorylated dimer (complex.ecocyc.CPLX0-8566), glnG (protein.P0AFB8).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEU0|protein.P0AEU0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[complex.ecocyc.CPLX0-8566|complex.ecocyc.CPLX0-8566]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=hisJ; function=+
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `C` - regulator=ArgR; target=hisJ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007617,ECOCYC:EG12124,GeneID:945309`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2426006-2426788:-; feature_type=gene
