---
entity_id: "gene.b3476"
entity_type: "gene"
name: "nikA"
source_database: "NCBI RefSeq"
source_id: "gene-b3476"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3476"
  - "nikA"
---

# nikA

`gene.b3476`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3476`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nikA (gene.b3476) is a gene entity. It encodes nikA (protein.P33590). Encoded protein function: FUNCTION: Involved in a nickel transport system, probably represents the nickel binder. EcoCyc product frame: NIKA-MONOMER. EcoCyc synonyms: hydD, hydC. Genomic coordinates: 3613667-3615241. EcoCyc protein note: NikA is the periplasmic binding protein of a high affinity nickel uptake system. The endogenous ligand for NikA is suggested to be a CPD0-2714 Ni-(L-His)2 complex. Purified NikA is monomeric and binds one atom of nickel per molecule of protein with a Kd of less than 0.1μM; purified NikA binds Ni2+ with at least 10-fold higher affinity than for other divalent metals . Purified NikA binds nickel selctively over cobalt with a Kd of 1µM for Ni2+ and 246µM for Co2+ . NikA mediates Tar dependent nickel-repellent chemotaxis . Purified, crystallized NikA consists of two lobes connected by a hinge; a hydrophobic pocket shaped to fit a penta-coordinate-hydrated nickel ion [Ni(H2O)52] forms the ligand binding site; nickel does not form direct contacts with NikA but hydrogen bonds to a coordinating water molecule; nickel remains accessible to solvent while bound to NikA...

## Biological Role

Repressed by nikR (protein.P0A6Z6). Activated by fnr (protein.P0A9E5).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33590|protein.P33590]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=nikA; function=+
- `represses` <-- [[protein.P0A6Z6|protein.P0A6Z6]] `RegulonDB` `S` - regulator=NikR; target=nikA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011354,ECOCYC:EG12075,GeneID:947981`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3613667-3615241:+; feature_type=gene
