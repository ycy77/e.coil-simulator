---
entity_id: "protein.P0A712"
entity_type: "protein"
name: "kdgT"
source_database: "UniProt"
source_id: "P0A712"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:6094479}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "kdgT b3909 JW5560"
---

# kdgT

`protein.P0A712`

## Static

- Type: `protein`
- Source: `UniProt:P0A712`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:6094479}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Catalyzes the proton-dependent uptake of 2-keto-3-deoxygluconate (KDG) into the cell (PubMed:15555, PubMed:6094479). Expression of this specific KDG-uptake system may allow growth with KDG as the sole carbon source (PubMed:4359651). Can also transport D-glucuronate (PubMed:15555, PubMed:6094479). {ECO:0000269|PubMed:15555, ECO:0000269|PubMed:6094479, ECO:0000303|PubMed:4359651}. KdgT is a probable 2-keto-3-deoxy-D-gluconate (KDG) uptake system. The cloned kdgT gene increased uptake of KDG and to a lesser extent glucuronate and could complement the KDG transport defect in kdgT mutants. KDG transport has been shown in whole cells and membrane vesicles to be via proton symport . KdgT is the prototype representative of the KdgT family of KDG transporters. Expression of kdgT is inducible by KDG and is under the control of the KdgR repressor . Imported KDG is subsequently degraded to pyruvate and triose-phosphate.

## Biological Role

Catalyzes 2-dehydro-3-deoxy-D-gluconate:proton symport (reaction.ecocyc.TRANS-RXN-113). Transports 2-Dehydro-3-deoxy-D-gluconate (molecule.C00204), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Catalyzes the proton-dependent uptake of 2-keto-3-deoxygluconate (KDG) into the cell (PubMed:15555, PubMed:6094479). Expression of this specific KDG-uptake system may allow growth with KDG as the sole carbon source (PubMed:4359651). Can also transport D-glucuronate (PubMed:15555, PubMed:6094479). {ECO:0000269|PubMed:15555, ECO:0000269|PubMed:6094479, ECO:0000303|PubMed:4359651}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-113|reaction.ecocyc.TRANS-RXN-113]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00204|molecule.C00204]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b3909|gene.b3909]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A712`
- `KEGG:ecj:JW5560;eco:b3909;ecoc:C3026_21140;`
- `GeneID:75174150;75204583;948407;`
- `GO:GO:0005886; GO:0015649; GO:0016020; GO:0035429`

## Notes

2-keto-3-deoxygluconate permease (KDG permease) (3-deoxy-2-oxo-D-gluconate-transport system)
