---
entity_id: "protein.P0AF16"
entity_type: "protein"
name: "murJ"
source_database: "UniProt"
source_id: "P0AF16"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02078, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:23935042}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_02078, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:23935042}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "murJ mviN yceN b1069 JW1056"
---

# murJ

`protein.P0AF16`

## Static

- Type: `protein`
- Source: `UniProt:P0AF16`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02078, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:23935042}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_02078, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:23935042}.

## Enriched Summary

FUNCTION: Involved in peptidoglycan biosynthesis. Transports lipid-linked peptidoglycan precursors from the inner to the outer leaflet of the cytoplasmic membrane. {ECO:0000255|HAMAP-Rule:MF_02078, ECO:0000269|PubMed:18708495, ECO:0000269|PubMed:18832143, ECO:0000269|PubMed:25013077}. MurJ is the inner membrane protein responsible for flipping lipid II from the inner face of the inner membrane to the outer face prior to peptidoglycan (PG) polymerization; MurJ is essential for PG synthesis . There are conflicting reports on MurJ binding to lipid II: MurJ does not interact directly with lipid II in vitro and does not affect MrcB mediated lipid II polymerization in vitro ; purified MurJ binds lipid II with high affinity (Kd of 2.9 µM for binding of the first lipid II) . MurJ has 14 transmembrane (TM) domains with the N and C-termini located in the cytoplasm . MurJ contains a solvent exposed central cavity located within the membrane region which is consistent with a role in transport; the central cavity is lined by TM domains 1, 2, 7 and 8 and charged residues within the cavity are critical for function...

## Biological Role

Catalyzes lipid II flippase (reaction.ecocyc.TRANS-RXN0-286). Transports hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Involved in peptidoglycan biosynthesis. Transports lipid-linked peptidoglycan precursors from the inner to the outer leaflet of the cytoplasmic membrane. {ECO:0000255|HAMAP-Rule:MF_02078, ECO:0000269|PubMed:18708495, ECO:0000269|PubMed:18832143, ECO:0000269|PubMed:25013077}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-286|reaction.ecocyc.TRANS-RXN0-286]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b1069|gene.b1069]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AF16`
- `KEGG:ecj:JW1056;eco:b1069;ecoc:C3026_06490;`
- `GeneID:75203656;945487;`
- `GO:GO:0000935; GO:0005886; GO:0008360; GO:0009252; GO:0015648; GO:0015836; GO:0034203; GO:0034204; GO:0071555; GO:1901612`

## Notes

Lipid II flippase MurJ (Peptidoglycan biosynthesis protein MurJ)
