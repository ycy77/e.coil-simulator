---
entity_id: "gene.b2934"
entity_type: "gene"
name: "cmtB"
source_database: "NCBI RefSeq"
source_id: "gene-b2934"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2934"
  - "cmtB"
---

# cmtB

`gene.b2934`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2934`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cmtB (gene.b2934) is a gene entity. It encodes cmtB (protein.P69824). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II CmtAB PTS system is involved in D-mannitol transport. {ECO:0000250|UniProtKB:P0A0E0}. EcoCyc product frame: CMTB-MONOMER. EcoCyc synonyms: tolM. Genomic coordinates: 3078887-3079330. EcoCyc protein note: cmtB encodes a hydrophilic protein with seqence similarity to the EIIA domain of MltA, the mannitol PTS permease . Expression of cmtB from a lac promoter partially complements the growth defect of an E. coli mtlA C-terminal deletion mutant . A solution structure of CmtB shows high similarity with that of the MltA IIA domain although structural differences around the active site are present. Histidine residue 67 is predicted to be the site of phosphorylation .

## Biological Role

Activated by nac (protein.Q47005).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69824|protein.P69824]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=cmtB; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009623,ECOCYC:EG11791,GeneID:945125`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3078887-3079330:-; feature_type=gene
