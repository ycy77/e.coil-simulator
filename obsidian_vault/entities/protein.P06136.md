---
entity_id: "protein.P06136"
entity_type: "protein"
name: "ftsQ"
source_database: "UniProt"
source_id: "P06136"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00911, ECO:0000269|PubMed:11415986, ECO:0000269|PubMed:11703663, ECO:0000269|PubMed:11948172, ECO:0000269|PubMed:15165235, ECO:0000269|PubMed:17693520, ECO:0000269|PubMed:2007547, ECO:0000269|PubMed:9829918, ECO:0000269|PubMed:9882666}; Single-pass type II membrane protein {ECO:0000255|HAMAP-Rule:MF_00911, ECO:0000269|PubMed:11415986, ECO:0000269|PubMed:11703663, ECO:0000269|PubMed:11948172, ECO:0000269|PubMed:15165235, ECO:0000269|PubMed:17693520, ECO:0000269|PubMed:2007547, ECO:0000269|PubMed:9829918, ECO:0000269|PubMed:9882666}. Note=Localizes to the division septum. Localization requires FtsZ, FtsA, ZipA and FtsK, but not FtsL, FtsI and FtsN. Insertion into the membrane requires YidC and the Sec translocase."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ftsQ b0093 JW0091"
---

# ftsQ

`protein.P06136`

## Static

- Type: `protein`
- Source: `UniProt:P06136`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00911, ECO:0000269|PubMed:11415986, ECO:0000269|PubMed:11703663, ECO:0000269|PubMed:11948172, ECO:0000269|PubMed:15165235, ECO:0000269|PubMed:17693520, ECO:0000269|PubMed:2007547, ECO:0000269|PubMed:9829918, ECO:0000269|PubMed:9882666}; Single-pass type II membrane protein {ECO:0000255|HAMAP-Rule:MF_00911, ECO:0000269|PubMed:11415986, ECO:0000269|PubMed:11703663, ECO:0000269|PubMed:11948172, ECO:0000269|PubMed:15165235, ECO:0000269|PubMed:17693520, ECO:0000269|PubMed:2007547, ECO:0000269|PubMed:9829918, ECO:0000269|PubMed:9882666}. Note=Localizes to the division septum. Localization requires FtsZ, FtsA, ZipA and FtsK, but not FtsL, FtsI and FtsN. Insertion into the membrane requires YidC and the Sec translocase.

## Enriched Summary

FUNCTION: Essential cell division protein. May link together the upstream cell division proteins, which are predominantly cytoplasmic, with the downstream cell division proteins, which are predominantly periplasmic. May control correct divisome assembly. {ECO:0000255|HAMAP-Rule:MF_00911, ECO:0000269|PubMed:17185541, ECO:0000269|PubMed:19233928}. FtsQ is an essential cell division protein that is required throughout the process of septum formation; the protein is present in very small amounts of approximately 22 molecules per cell . FtsQ localizes to the division site; the periplasmic domain of FtsQ is necessary and sufficient for correct localization . The cytoplasmic domain and membrane spanning region determine membrane localization, but are not otherwise required for FtsQ function . Localization to the Z ring is dependent on FtsZ, FtsA, ZipA, and FtsK, but not FtsI, FtsL and FtsN . Conversely, FtsL and FtsB require FtsQ for localization to the Z ring . FtsQ, FtsL and FtsB form a complex in vivo even in the absence of FtsK and thus independently of their localization to the septal region . However, assembly of the cell division machinery is cooperative rather than linear, and FtsQ may play a central role. Different domains of FtsQ were found to be used for interactions with FtsA, FtsI, FtsL, FtsN, FtsQ, FtsX, and YmgF...

## Biological Role

Component of FtsLBQ cell division complex (complex.ecocyc.CPLX0-7934).

## Annotation

FUNCTION: Essential cell division protein. May link together the upstream cell division proteins, which are predominantly cytoplasmic, with the downstream cell division proteins, which are predominantly periplasmic. May control correct divisome assembly. {ECO:0000255|HAMAP-Rule:MF_00911, ECO:0000269|PubMed:17185541, ECO:0000269|PubMed:19233928}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7934|complex.ecocyc.CPLX0-7934]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0093|gene.b0093]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06136`
- `KEGG:ecj:JW0091;eco:b0093;ecoc:C3026_00370;`
- `GeneID:944823;`
- `GO:GO:0000917; GO:0005886; GO:0032153; GO:0042802; GO:0043093; GO:0051301; GO:1990586; GO:1990587`

## Notes

Cell division protein FtsQ
