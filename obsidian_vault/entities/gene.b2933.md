---
entity_id: "gene.b2933"
entity_type: "gene"
name: "cmtA"
source_database: "NCBI RefSeq"
source_id: "gene-b2933"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2933"
  - "cmtA"
---

# cmtA

`gene.b2933`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2933`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cmtA (gene.b2933) is a gene entity. It encodes cmtA (protein.P69826). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II CmtAB PTS system is involved in D-mannitol transport. {ECO:0000250|UniProtKB:P28008}. EcoCyc product frame: CMTA-MONOMER. Genomic coordinates: 3077471-3078859. EcoCyc protein note: CmtA has 52% amino acid identity with the EIICB domain of MltA, the mannitol PTS permease. cmtA may encode a protein with 6 transmembrane regions; a conserved cysteine residue at position 377 may be required for phosphoryl transfer to substrate. Expression of cmtA under the control of heterologous promoter led to mannitol transport in mtlA mutants of E. coli K-12 .

## Biological Role

Activated by nac (protein.Q47005).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69826|protein.P69826]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=cmtA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009621,ECOCYC:EG11792,GeneID:945256`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3077471-3078859:-; feature_type=gene
