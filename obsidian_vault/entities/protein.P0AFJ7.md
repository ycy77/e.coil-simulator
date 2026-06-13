---
entity_id: "protein.P0AFJ7"
entity_type: "protein"
name: "pitA"
source_database: "UniProt"
source_id: "P0AFJ7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:11489853, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pitA pit b3493 JW3460"
---

# pitA

`protein.P0AFJ7`

## Static

- Type: `protein`
- Source: `UniProt:P0AFJ7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:11489853, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Low-affinity inorganic phosphate transporter (PubMed:11489853, PubMed:328484, PubMed:6998957, PubMed:8110778). Mediates proton-driven uptake of soluble neutral metal phosphate (MeHP04) complexes (PubMed:8110778). It can use Mg(2+), Ca(2+), Co(2+) and Mn(2+) (PubMed:8110778). Activity impacts bacterial growth in low Mg(2+) conditions (PubMed:30276893). Is also involved in Zn(2+) uptake, probably via formation of a ZnHPO4 complex (PubMed:10713426). Can also transport arsenate (PubMed:328484). Involved in the uptake of tellurite (PubMed:23189244). {ECO:0000269|PubMed:10713426, ECO:0000269|PubMed:11489853, ECO:0000269|PubMed:23189244, ECO:0000269|PubMed:30276893, ECO:0000269|PubMed:328484, ECO:0000269|PubMed:6998957, ECO:0000269|PubMed:8110778}. Early work in E. coli indicated that there are two genetically separable transport systems for inorganic phosphate (Pi) - a high affinity, low velocity Pst (phosphate specific transport) system (the ABC-27-CPLX) and a low affinity, high velocity Pit (Pi transport) system *. This latter system is constitutive in nature and catalyses an electrogenic metal phosphate:H+ symport . Pi uptake via Pit is dependent on the presence of divalent cations, like Mg2+, Ca2+, Co2+, or Mn2+, which form soluble metal phosphate (MeHP04) complexes . The Pit system in E...

## Biological Role

Catalyzes phosphate:proton symport (reaction.ecocyc.TRANS-RXN-114), magnesium hydrogenphosphate:proton symport (reaction.ecocyc.TRANS-RXN-277), calcium hydrogenphosphate:proton symport (reaction.ecocyc.TRANS-RXN-278), zinc hydrogenphosphate:proton symport (reaction.ecocyc.TRANS-RXN-279), tellurite:proton symport (reaction.ecocyc.TRANS-RXN-280), arsenate:proton symport (reaction.ecocyc.TRANS-RXN0-550). Transports zinc hydrogenphosphate (molecule.ecocyc.CPD-18501), tellurite (molecule.ecocyc.CPD-4544), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Low-affinity inorganic phosphate transporter (PubMed:11489853, PubMed:328484, PubMed:6998957, PubMed:8110778). Mediates proton-driven uptake of soluble neutral metal phosphate (MeHP04) complexes (PubMed:8110778). It can use Mg(2+), Ca(2+), Co(2+) and Mn(2+) (PubMed:8110778). Activity impacts bacterial growth in low Mg(2+) conditions (PubMed:30276893). Is also involved in Zn(2+) uptake, probably via formation of a ZnHPO4 complex (PubMed:10713426). Can also transport arsenate (PubMed:328484). Involved in the uptake of tellurite (PubMed:23189244). {ECO:0000269|PubMed:10713426, ECO:0000269|PubMed:11489853, ECO:0000269|PubMed:23189244, ECO:0000269|PubMed:30276893, ECO:0000269|PubMed:328484, ECO:0000269|PubMed:6998957, ECO:0000269|PubMed:8110778}.

## Outgoing Edges (9)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-114|reaction.ecocyc.TRANS-RXN-114]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-277|reaction.ecocyc.TRANS-RXN-277]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-278|reaction.ecocyc.TRANS-RXN-278]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-279|reaction.ecocyc.TRANS-RXN-279]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-280|reaction.ecocyc.TRANS-RXN-280]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-550|reaction.ecocyc.TRANS-RXN0-550]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.CPD-18501|molecule.ecocyc.CPD-18501]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD-4544|molecule.ecocyc.CPD-4544]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b3493|gene.b3493]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFJ7`
- `KEGG:ecj:JW3460;eco:b3493;ecoc:C3026_18920;`
- `GeneID:93778500;948009;`
- `GO:GO:0005315; GO:0005385; GO:0005886; GO:0010960; GO:0015295; GO:0015654; GO:0015710; GO:0035435; GO:1901683; GO:1901684`

## Notes

Low-affinity inorganic phosphate transporter PitA (Metal phosphate:H(+) symporter PitA)
