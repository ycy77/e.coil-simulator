---
entity_id: "gene.b1946"
entity_type: "gene"
name: "fliN"
source_database: "NCBI RefSeq"
source_id: "gene-b1946"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1946"
  - "fliN"
---

# fliN

`gene.b1946`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1946`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fliN (gene.b1946) is a gene entity. It encodes fliN (protein.P15070). Encoded protein function: FUNCTION: FliN is one of three proteins (FliG, FliN, FliM) that form a switch complex that is proposed to be located at the base of the basal body. This complex interacts with the CheY and CheZ chemotaxis proteins, in addition to contacting components of the motor that determine the direction of flagellar rotation. EcoCyc product frame: FLIN-FLAGELLAR-C-RING-SWITCH. EcoCyc synonyms: motD. Genomic coordinates: 2021088-2021501. EcoCyc protein note: FliN, is one of three components of the flagellar motor's "switch complex." The crystal structure of the C-terminal domain of the FliN protein in Thermotoga maritime has been determined to 3.4 Å resolution . For a description of flagellar gene nomenclature, including old (fla, flb) and new (flg, flh and fli) symbols, see

## Biological Role

Activated by fliA (protein.P0AEM6).

## Enriched Pathways

- `eco02030` Bacterial chemotaxis (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P15070|protein.P15070]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AEM6|protein.P0AEM6]] `RegulonDB` `S` - sigma=sigma28; target=fliN; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006471,ECOCYC:EG10324,GeneID:946423`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2021088-2021501:+; feature_type=gene
