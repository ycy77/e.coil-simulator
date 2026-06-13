---
entity_id: "protein.P24228"
entity_type: "protein"
name: "dacB"
source_database: "UniProt"
source_id: "P24228"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dacB b3182 JW3149"
---

# dacB

`protein.P24228`

## Static

- Type: `protein`
- Source: `UniProt:P24228`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Not involved in transpeptidation but exclusively catalyzes a DD-carboxypeptidase and DD-endopeptidase reaction. {ECO:0000269|PubMed:2046551}.

## Biological Role

Component of peptidoglycan DD endopeptidase DacB (complex.ecocyc.CPLX0-8545).

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Not involved in transpeptidation but exclusively catalyzes a DD-carboxypeptidase and DD-endopeptidase reaction. {ECO:0000269|PubMed:2046551}.

## Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8545|complex.ecocyc.CPLX0-8545]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3182|gene.b3182]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24228`
- `KEGG:ecj:JW3149;eco:b3182;ecoc:C3026_17325;`
- `GeneID:75173356;947693;`
- `GO:GO:0000270; GO:0004175; GO:0004180; GO:0004185; GO:0004252; GO:0005886; GO:0006508; GO:0008360; GO:0008658; GO:0009002; GO:0009252; GO:0042597; GO:0043093; GO:0046677; GO:0071555`
- `EC:3.4.16.4; 3.4.21.-`

## Notes

D-alanyl-D-alanine carboxypeptidase DacB (DD-carboxypeptidase) (DD-peptidase) (EC 3.4.16.4) (D-alanyl-D-alanine endopeptidase) (DD-endopeptidase) (EC 3.4.21.-) (Penicillin-binding protein 4) (PBP-4)
