---
entity_id: "protein.P29131"
entity_type: "protein"
name: "ftsN"
source_database: "UniProt"
source_id: "P29131"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:8631709}; Single-pass type II membrane protein {ECO:0000269|PubMed:8631709}. Note=Localizes to the septum (PubMed:19684127, PubMed:24750258, PubMed:9282742). Localizes to the midcell via interaction with the early cell division protein FtsA and via the periplasmic SPOR domain (PubMed:19684127, PubMed:24750258, PubMed:9282742). FtsA-dependent localization precedes SPOR-dependent localization, and both are needed for efficient localization (PubMed:24750258). Localization depends upon FtsZ, FtsA, ZipA, FtsQ and FtsI (PubMed:11948172, PubMed:9282742). {ECO:0000269|PubMed:11948172, ECO:0000269|PubMed:19684127, ECO:0000269|PubMed:24750258, ECO:0000269|PubMed:9282742}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ftsN msgA b3933 JW3904"
---

# ftsN

`protein.P29131`

## Static

- Type: `protein`
- Source: `UniProt:P29131`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:8631709}; Single-pass type II membrane protein {ECO:0000269|PubMed:8631709}. Note=Localizes to the septum (PubMed:19684127, PubMed:24750258, PubMed:9282742). Localizes to the midcell via interaction with the early cell division protein FtsA and via the periplasmic SPOR domain (PubMed:19684127, PubMed:24750258, PubMed:9282742). FtsA-dependent localization precedes SPOR-dependent localization, and both are needed for efficient localization (PubMed:24750258). Localization depends upon FtsZ, FtsA, ZipA, FtsQ and FtsI (PubMed:11948172, PubMed:9282742). {ECO:0000269|PubMed:11948172, ECO:0000269|PubMed:19684127, ECO:0000269|PubMed:24750258, ECO:0000269|PubMed:9282742}.

## Enriched Summary

FUNCTION: Essential cell division protein that activates septal peptidoglycan synthesis and constriction of the cell. Acts on both sides of the membrane, via interaction with FtsA in the cytoplasm and interaction with the FtsQBL complex in the periplasm. These interactions may induce a conformational switch in both FtsA and FtsQBL, leading to septal peptidoglycan synthesis by FtsI and associated synthases (Probable) (PubMed:25496160). Required for full FtsI activity (PubMed:25496160). Required for recruitment of AmiC to the septal ring (PubMed:12787347). {ECO:0000269|PubMed:12787347, ECO:0000269|PubMed:25496160, ECO:0000305|PubMed:25496050, ECO:0000305|PubMed:25571948}. FtsN is an essential cell division protein present at 3000-6000 molecules per cell; inactivation of ftsN results in filamentation and cell death . FtsN contains a small N-terminal cytoplasmic domain, a membrane-spanning region and a large periplasmic C-terminal domain . FtsN localizes to the septum during division; the periplasmic domain of FtsN is sufficient for correct localization . The cytoplasmic domain and membrane spanning region determine membrane localization, but are not otherwise required for FtsN function...

## Annotation

FUNCTION: Essential cell division protein that activates septal peptidoglycan synthesis and constriction of the cell. Acts on both sides of the membrane, via interaction with FtsA in the cytoplasm and interaction with the FtsQBL complex in the periplasm. These interactions may induce a conformational switch in both FtsA and FtsQBL, leading to septal peptidoglycan synthesis by FtsI and associated synthases (Probable) (PubMed:25496160). Required for full FtsI activity (PubMed:25496160). Required for recruitment of AmiC to the septal ring (PubMed:12787347). {ECO:0000269|PubMed:12787347, ECO:0000269|PubMed:25496160, ECO:0000305|PubMed:25496050, ECO:0000305|PubMed:25571948}.

## Outgoing Edges (1)

- `activates` --> [[reaction.ecocyc.RXN-16650|reaction.ecocyc.RXN-16650]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `encodes` <-- [[gene.b3933|gene.b3933]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P29131`
- `KEGG:ecj:JW3904;eco:b3933;`
- `GeneID:948428;`
- `GO:GO:0000917; GO:0000935; GO:0005886; GO:0030428; GO:0032153; GO:0042834; GO:0043093; GO:0051301; GO:1990586`

## Notes

Cell division protein FtsN
