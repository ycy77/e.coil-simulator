---
entity_id: "protein.P0AEN4"
entity_type: "protein"
name: "ftsL"
source_database: "UniProt"
source_id: "P0AEN4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00910, ECO:0000269|PubMed:10027987, ECO:0000269|PubMed:11703663, ECO:0000269|PubMed:11948172, ECO:0000269|PubMed:1332942, ECO:0000269|PubMed:15165235}; Single-pass type II membrane protein {ECO:0000255|HAMAP-Rule:MF_00910, ECO:0000269|PubMed:10027987, ECO:0000269|PubMed:11703663, ECO:0000269|PubMed:11948172, ECO:0000269|PubMed:1332942, ECO:0000269|PubMed:15165235}. Note=Localizes to the division septum where it forms a ring structure. Localization requires FtsZ, FtsA, ZipA, FtsK, FtsQ and FtsB, but not FtsI and FtsN. Localization of FtsB and FtsL is codependent."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ftsL mraR yabD b0083 JW0081"
---

# ftsL

`protein.P0AEN4`

## Static

- Type: `protein`
- Source: `UniProt:P0AEN4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00910, ECO:0000269|PubMed:10027987, ECO:0000269|PubMed:11703663, ECO:0000269|PubMed:11948172, ECO:0000269|PubMed:1332942, ECO:0000269|PubMed:15165235}; Single-pass type II membrane protein {ECO:0000255|HAMAP-Rule:MF_00910, ECO:0000269|PubMed:10027987, ECO:0000269|PubMed:11703663, ECO:0000269|PubMed:11948172, ECO:0000269|PubMed:1332942, ECO:0000269|PubMed:15165235}. Note=Localizes to the division septum where it forms a ring structure. Localization requires FtsZ, FtsA, ZipA, FtsK, FtsQ and FtsB, but not FtsI and FtsN. Localization of FtsB and FtsL is codependent.

## Enriched Summary

FUNCTION: Essential cell division protein. May link together the upstream cell division proteins, which are predominantly cytoplasmic, with the downstream cell division proteins, which are predominantly periplasmic. Can also mediate Zn(2+)-sensitivity probably by increasing the permeability of the inner membrane. {ECO:0000255|HAMAP-Rule:MF_00910, ECO:0000269|PubMed:10613870, ECO:0000269|PubMed:19233928, ECO:0000269|PubMed:21708137}. FtsL is an essential cell division protein that is present in very small amounts of approximately 25 molecules per cell . Localization of FtsL to the septal ring is dependent on FtsZ, FtsA, ZipA, FtsK and FtsQ, but not FtsI . Conversely, FtsL is required for localization of FtsI to the Z ring . Although the hierarchy of dependency in the assembly of cell division proteins is largely linear, results have shown that assembly of the cell division machinery is complex . FtsL is an integral membrane protein with a small N-terminal cytoplasmic domain and a large periplasmic domain . Both the cytoplasmic domain and membrane spanning regions are essential for the role of FtsL in cell division ; the cytoplasmic domain is involved in recruiting downstream cell division proteins . The membrane-spanning and periplasmic regions of FtsL are required for localization to the division septum...

## Biological Role

Component of FtsLBQ cell division complex (complex.ecocyc.CPLX0-7934).

## Annotation

FUNCTION: Essential cell division protein. May link together the upstream cell division proteins, which are predominantly cytoplasmic, with the downstream cell division proteins, which are predominantly periplasmic. Can also mediate Zn(2+)-sensitivity probably by increasing the permeability of the inner membrane. {ECO:0000255|HAMAP-Rule:MF_00910, ECO:0000269|PubMed:10613870, ECO:0000269|PubMed:19233928, ECO:0000269|PubMed:21708137}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7934|complex.ecocyc.CPLX0-7934]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0083|gene.b0083]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEN4`
- `KEGG:ecj:JW0081;eco:b0083;ecoc:C3026_00320;`
- `GeneID:86862593;93777351;944803;`
- `GO:GO:0000917; GO:0005886; GO:0032153; GO:0043093; GO:0051301; GO:1990586; GO:1990587; GO:1990588`

## Notes

Cell division protein FtsL
