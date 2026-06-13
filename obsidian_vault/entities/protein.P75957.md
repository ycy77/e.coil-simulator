---
entity_id: "protein.P75957"
entity_type: "protein"
name: "lolD"
source_database: "UniProt"
source_id: "P75957"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lolD ycfV b1117 JW5162"
---

# lolD

`protein.P75957`

## Static

- Type: `protein`
- Source: `UniProt:P75957`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex LolCDE involved in the translocation of mature outer membrane-directed lipoproteins, from the inner membrane to the periplasmic chaperone, LolA. Responsible for the formation of the LolA-lipoprotein complex in an ATP-dependent manner. Such a release is dependent of the sorting-signal (absence of an Asp at position 2 of the mature lipoprotein) and of LolA. LolD is the ATP-binding component of the LolCDE lipoprotein release complex. LolD contains signature motifs conserved in ATP-binding cassette domains .

## Biological Role

Component of lipoprotein release complex (complex.ecocyc.ABC-62-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex LolCDE involved in the translocation of mature outer membrane-directed lipoproteins, from the inner membrane to the periplasmic chaperone, LolA. Responsible for the formation of the LolA-lipoprotein complex in an ATP-dependent manner. Such a release is dependent of the sorting-signal (absence of an Asp at position 2 of the mature lipoprotein) and of LolA.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-62-CPLX|complex.ecocyc.ABC-62-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1117|gene.b1117]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75957`
- `KEGG:ecj:JW5162;eco:b1117;ecoc:C3026_06730;`
- `GeneID:75171241;75203703;945670;`
- `GO:GO:0005524; GO:0005886; GO:0016887; GO:0022857; GO:0043190; GO:0044874; GO:0055085; GO:0089705; GO:0098797; GO:0140306`
- `EC:7.6.2.-`

## Notes

Lipoprotein-releasing system ATP-binding protein LolD (EC 7.6.2.-)
