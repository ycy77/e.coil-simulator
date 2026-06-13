---
entity_id: "protein.P43676"
entity_type: "protein"
name: "pitB"
source_database: "UniProt"
source_id: "P43676"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:11489853, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pitB b2987 JW2955"
---

# pitB

`protein.P43676`

## Static

- Type: `protein`
- Source: `UniProt:P43676`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:11489853, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Low-affinity inorganic phosphate transporter. {ECO:0000269|PubMed:11489853}. Early work in E. coli indicated that there are two genetically separable transport systems for inorganic phosphate (Pi) - a high affinity, low velocity Pst (phosphate specific transport) system (the ABC-27-CPLX) and a low affinity, high velocity Pit (Pi transport) system *. This latter system is constitutive in nature and catalyses an electrogenic metal phosphate:H+ symport . Pi uptake via Pit is dependent on the presence of divalent cations, like Mg2+, Ca2+, Co2+, or Mn2+, which form soluble metal phosphate (MeHP04) complexes . The Pit system in E. coli K-12 consists of two transporters - PitA and PitB - which have 81% sequence identity at the protein level; pitA is likely constitutive while pitB is repressed or inactivated through the pho regulon; chromosomally encoded PitB catalyses Pi uptake in a phoB-phoR deleted strain; both proteins may have contributed to the kinetic values and substrate specificities determined in earlier studies . The Pit proteins are predicted to contain 10 transmembrane helices . The Pit system also transports the phosphate analogue, arsenate . The PitB phosphate transporter is a member of the Inorganic Phosphate Transporter (PiT) family . Reviews: * The Pit system is lacking in many E. coli K-10 strains .

## Biological Role

Catalyzes phosphate:proton symport (reaction.ecocyc.TRANS-RXN-114), magnesium hydrogenphosphate:proton symport (reaction.ecocyc.TRANS-RXN-277), calcium hydrogenphosphate:proton symport (reaction.ecocyc.TRANS-RXN-278), arsenate:proton symport (reaction.ecocyc.TRANS-RXN0-550). Transports arsenate (molecule.ecocyc.ARSENATE), magnesium hydrogenphosphate (molecule.ecocyc.CPD-18499), calcium hydrogenphosphate (molecule.ecocyc.CPD-18500), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Low-affinity inorganic phosphate transporter. {ECO:0000269|PubMed:11489853}.

## Outgoing Edges (8)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-114|reaction.ecocyc.TRANS-RXN-114]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-277|reaction.ecocyc.TRANS-RXN-277]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-278|reaction.ecocyc.TRANS-RXN-278]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-550|reaction.ecocyc.TRANS-RXN0-550]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.ARSENATE|molecule.ecocyc.ARSENATE]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD-18499|molecule.ecocyc.CPD-18499]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD-18500|molecule.ecocyc.CPD-18500]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b2987|gene.b2987]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P43676`
- `KEGG:ecj:JW2955;eco:b2987;ecoc:C3026_16340;`
- `GeneID:947475;`
- `GO:GO:0005315; GO:0005886; GO:0015293; GO:0016020; GO:0035435`

## Notes

Low-affinity inorganic phosphate transporter PitB
