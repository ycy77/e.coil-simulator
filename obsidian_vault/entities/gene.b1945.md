---
entity_id: "gene.b1945"
entity_type: "gene"
name: "fliM"
source_database: "NCBI RefSeq"
source_id: "gene-b1945"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1945"
  - "fliM"
---

# fliM

`gene.b1945`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1945`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fliM (gene.b1945) is a gene entity. It encodes fliM (protein.P06974). Encoded protein function: FUNCTION: FliM is one of three proteins (FliG, FliN, FliM) that forms the rotor-mounted switch complex (C ring), located at the base of the basal body. This complex interacts with the CheY and CheZ chemotaxis proteins, in addition to contacting components of the motor that determine the direction of flagellar rotation. EcoCyc product frame: FLIM-FLAGELLAR-C-RING-SWITCH. EcoCyc synonyms: flaQ, fla, flaQII, flaAII, flaA, cheC2. Genomic coordinates: 2020087-2021091. EcoCyc protein note: FliM is one of three components of the flagellar motor's "switch complex." Expression of fliM is upregulated by ZnSO4 in the medium, and a fliM mutant is hypersensitive to ZnSO4 . For a description of flagellar gene nomenclature, including old (fla, flb) and new (flg, flh and fli) symbols, see cheC: see

## Biological Role

Activated by fliA (protein.P0AEM6).

## Enriched Pathways

- `eco02030` Bacterial chemotaxis (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06974|protein.P06974]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AEM6|protein.P0AEM6]] `RegulonDB` `S` - sigma=sigma28; target=fliM; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006469,ECOCYC:EG10323,GeneID:946442`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2020087-2021091:+; feature_type=gene
