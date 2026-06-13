---
entity_id: "protein.P0AD68"
entity_type: "protein"
name: "ftsI"
source_database: "UniProt"
source_id: "P0AD68"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02080, ECO:0000269|PubMed:2677607, ECO:0000269|PubMed:9614966}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_02080, ECO:0000269|PubMed:2677607, ECO:0000269|PubMed:9614966}; Periplasmic side {ECO:0000269|PubMed:2677607, ECO:0000269|PubMed:9614966}. Note=The bulk of the molecule, except for the N-terminal membrane anchor region, protrudes into the periplasmic space (PubMed:2677607, PubMed:9614966). Localizes to the division septum during the later stages of cell growth and throughout septation (PubMed:15601716, PubMed:9379897, PubMed:9603865, PubMed:9882665). Localization is dependent on FtsZ, FtsA, FtsK, FtsQ, FtsL and FtsW, but not on FtsN (PubMed:11703663, PubMed:11807049, PubMed:9603865, PubMed:9882665). {ECO:0000269|PubMed:11703663, ECO:0000269|PubMed:11807049, ECO:0000269|PubMed:15601716, ECO:0000269|PubMed:2677607, ECO:0000269|PubMed:9379897, ECO:0000269|PubMed:9603865, ECO:0000269|PubMed:9614966, ECO:0000269|PubMed:9882665}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ftsI pbpB b0084 JW0082"
---

# ftsI

`protein.P0AD68`

## Static

- Type: `protein`
- Source: `UniProt:P0AD68`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02080, ECO:0000269|PubMed:2677607, ECO:0000269|PubMed:9614966}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_02080, ECO:0000269|PubMed:2677607, ECO:0000269|PubMed:9614966}; Periplasmic side {ECO:0000269|PubMed:2677607, ECO:0000269|PubMed:9614966}. Note=The bulk of the molecule, except for the N-terminal membrane anchor region, protrudes into the periplasmic space (PubMed:2677607, PubMed:9614966). Localizes to the division septum during the later stages of cell growth and throughout septation (PubMed:15601716, PubMed:9379897, PubMed:9603865, PubMed:9882665). Localization is dependent on FtsZ, FtsA, FtsK, FtsQ, FtsL and FtsW, but not on FtsN (PubMed:11703663, PubMed:11807049, PubMed:9603865, PubMed:9882665). {ECO:0000269|PubMed:11703663, ECO:0000269|PubMed:11807049, ECO:0000269|PubMed:15601716, ECO:0000269|PubMed:2677607, ECO:0000269|PubMed:9379897, ECO:0000269|PubMed:9603865, ECO:0000269|PubMed:9614966, ECO:0000269|PubMed:9882665}.

## Enriched Summary

FUNCTION: Essential cell division protein that catalyzes cross-linking of the peptidoglycan cell wall at the division septum (PubMed:1103132, PubMed:3531167, PubMed:6450748, PubMed:7030331, PubMed:9614966). Required for localization of FtsN (PubMed:9282742). {ECO:0000269|PubMed:1103132, ECO:0000269|PubMed:3531167, ECO:0000269|PubMed:6450748, ECO:0000269|PubMed:7030331, ECO:0000269|PubMed:9282742, ECO:0000269|PubMed:9614966}. FtsI (penicillin-binding protein 3, PBP3) is believed to be the primary peptidoglycan (PG) transpeptidase which functions together with the SEDS family protein EG10344-MONOMER FtsW to synthesize septal peptidoglycan (sPG) during cell division; FtsW-FtsI are the SEDS-bPBP pair of the divisome. The spatiotemporal coordination of sPG synthesis in E. coli is currently described by a 'two-track' model (see ). FtsI is an essential cell division protein which is present at low abundance (~100 molecules per cell) . Binding of beta-lactam antibiotics to FtsI inhibits FtsI activity and is lethal . FtsI localizes to the division site; localization is dependent on FtsZ, FtsA, FtsQ, FtsL and FtsW, but not EG10341-MONOMER FtsN . Subcomplexes of class 2 penicillin binding proteins with SEDS (shape, elongation, division and sporulation) family proteins are proposed to be the primary peptidoglycan synthases in cell elongation and division...

## Biological Role

Catalyzes peptidoglycan transpeptidase (Gram-negative bacteria) (reaction.ecocyc.RXN-16659).

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01501` beta-Lactam resistance (KEGG)

## Annotation

FUNCTION: Essential cell division protein that catalyzes cross-linking of the peptidoglycan cell wall at the division septum (PubMed:1103132, PubMed:3531167, PubMed:6450748, PubMed:7030331, PubMed:9614966). Required for localization of FtsN (PubMed:9282742). {ECO:0000269|PubMed:1103132, ECO:0000269|PubMed:3531167, ECO:0000269|PubMed:6450748, ECO:0000269|PubMed:7030331, ECO:0000269|PubMed:9282742, ECO:0000269|PubMed:9614966}.

## Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01501` beta-Lactam resistance (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-16659|reaction.ecocyc.RXN-16659]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0084|gene.b0084]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AD68`
- `KEGG:ecj:JW0082;eco:b0084;ecoc:C3026_00325;`
- `GeneID:75202099;944799;`
- `GO:GO:0000917; GO:0005886; GO:0006508; GO:0008360; GO:0008658; GO:0008955; GO:0009002; GO:0009252; GO:0009410; GO:0032153; GO:0043093; GO:0051301; GO:0071555; GO:1990586`
- `EC:3.4.16.4`

## Notes

Peptidoglycan D,D-transpeptidase FtsI (EC 3.4.16.4) (Essential cell division protein FtsI) (Murein transpeptidase) (Penicillin-binding protein 3) (PBP-3) (Peptidoglycan synthase FtsI)
