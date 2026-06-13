---
entity_id: "protein.P0A6S5"
entity_type: "protein"
name: "ftsB"
source_database: "UniProt"
source_id: "P0A6S5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00599, ECO:0000269|PubMed:11972052, ECO:0000269|PubMed:15165235}; Single-pass type II membrane protein {ECO:0000255|HAMAP-Rule:MF_00599, ECO:0000269|PubMed:11972052, ECO:0000269|PubMed:15165235}. Note=Localizes to the division septum. Localization requires FtsQ and FtsL, but not FtsW and FtsI. Localization of FtsB and FtsL is codependent."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ftsB ygbQ b2748 JW2718"
---

# ftsB

`protein.P0A6S5`

## Static

- Type: `protein`
- Source: `UniProt:P0A6S5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00599, ECO:0000269|PubMed:11972052, ECO:0000269|PubMed:15165235}; Single-pass type II membrane protein {ECO:0000255|HAMAP-Rule:MF_00599, ECO:0000269|PubMed:11972052, ECO:0000269|PubMed:15165235}. Note=Localizes to the division septum. Localization requires FtsQ and FtsL, but not FtsW and FtsI. Localization of FtsB and FtsL is codependent.

## Enriched Summary

FUNCTION: Essential cell division protein. May link together the upstream cell division proteins, which are predominantly cytoplasmic, with the downstream cell division proteins, which are predominantly periplasmic. {ECO:0000255|HAMAP-Rule:MF_00599, ECO:0000269|PubMed:11972052, ECO:0000269|PubMed:19233928}. FtsB is an essential cell division protein which localizes to the cell division site. Depletion of FtsB results in abnormal filamentous morphology, but does not cause a defect in segregation of replicated DNA . Localization of FtsB to the division site is dependent on FtsQ and FtsL, but does not require FtsW and FtsI. Conversely, FtsB is required for localization of FtsI and FtsW to the Z ring . Although the hierarchy of dependency in the assembly of cell division proteins is largely linear, subsequent sults showed that assembly of the cell division machinery is complex. Premature targeting of FtsB to the division site enables recruitment of FtsL, FtsW and FtsI in the absence of FtsQ . FtsB contains a small N-terminal cytoplasmic domain, a membrane-spanning region and a periplasmic C-terminal domain with a leucine zipper motif . The transmembrane domain homo-oligomerizes; the interaction is mediated by polar amino acids on one face of the helix and hydrogen bonding with Gln16...

## Biological Role

Component of FtsLBQ cell division complex (complex.ecocyc.CPLX0-7934).

## Annotation

FUNCTION: Essential cell division protein. May link together the upstream cell division proteins, which are predominantly cytoplasmic, with the downstream cell division proteins, which are predominantly periplasmic. {ECO:0000255|HAMAP-Rule:MF_00599, ECO:0000269|PubMed:11972052, ECO:0000269|PubMed:19233928}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7934|complex.ecocyc.CPLX0-7934]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2748|gene.b2748]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6S5`
- `KEGG:ecj:JW2718;eco:b2748;ecoc:C3026_15110;`
- `GeneID:86947601;93779258;946033;`
- `GO:GO:0000917; GO:0005886; GO:0030428; GO:0032153; GO:0042802; GO:0043093; GO:0051301; GO:1990586; GO:1990587; GO:1990588`

## Notes

Cell division protein FtsB
