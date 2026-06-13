---
entity_id: "gene.b4149"
entity_type: "gene"
name: "blc"
source_database: "NCBI RefSeq"
source_id: "gene-b4149"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4149"
  - "blc"
---

# blc

`gene.b4149`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4149`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

blc (gene.b4149) is a gene entity. It encodes blc (protein.P0A901). Encoded protein function: FUNCTION: Involved in the storage or transport of lipids necessary for membrane maintenance under stressful conditions. Displays a binding preference for lysophospholipids. {ECO:0000269|PubMed:15044022}. EcoCyc product frame: G7837-MONOMER. EcoCyc synonyms: yjeL. Genomic coordinates: 4377189-4377722. EcoCyc protein note: The Blc protein is a globomycin-sensitive outer membrane lipoprotein . blc is a member of the RpoS regulon; expression is induced at the transition between exponential and stationary phase growth . Blc contains a typical lipocalin fold consisting of an 8 stranded β-barrel with an α helix at the C-terminus; the protein contains a long, flat, narrow cavity and the interior walls contain hydrophobic, semi-polar and charged residues. Blc may play a role in lipid transport or storage under stress conditions . Blc binds fatty acids (myristic, palmitoleic, palmitic, cis-vaccenic and others) and phospholipids with micromolar affinities . Blc is a functional dimer ; Blc is a monomer in both crystal form and in solution; the dimeric structure observed by may form as a consequence of the cloning strategy . Blc may bind heme blc: bacterial lipocalin

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A901|protein.P0A901]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=blc; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=blc; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013590,ECOCYC:G7837,GeneID:948670`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4377189-4377722:-; feature_type=gene
