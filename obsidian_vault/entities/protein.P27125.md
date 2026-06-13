---
entity_id: "protein.P27125"
entity_type: "protein"
name: "rhaT"
source_database: "UniProt"
source_id: "P27125"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01532, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:2283027, ECO:0000269|PubMed:8262918}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01532, ECO:0000269|PubMed:8262918}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rhaT b3907 JW3878"
---

# rhaT

`protein.P27125`

## Static

- Type: `protein`
- Source: `UniProt:P27125`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01532, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:2283027, ECO:0000269|PubMed:8262918}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01532, ECO:0000269|PubMed:8262918}.

## Enriched Summary

FUNCTION: Uptake of L-rhamnose across the cytoplasmic membrane with the concomitant transport of protons into the cell (symport system) (PubMed:1551902, PubMed:2283027, PubMed:8384447). Can also transport L-mannose and L-lyxose, but at reduced rates (PubMed:1650346, PubMed:8384447). {ECO:0000269|PubMed:1551902, ECO:0000269|PubMed:1650346, ECO:0000269|PubMed:2283027, ECO:0000269|PubMed:8384447}. RhaT is the sole transporter for rhamnose in E. coli and functions as a rhamnose/proton symporter. rhaT mutants were unable to utilise or transport rhamnose, and this defect could be complemented by the cloned rhaT gene . Studies in membrane vesicles have shown that RhaT can transport rhamnose with moderate affinity (20-40 μM) and that rhamnose transport is coupled with proton transport . RhaT is also able to transport L-lyxose . RhaT is the prototype member of the RhaT family of transporters. Analysis of RhaT-BlaZ fusions has indicated that the RhaT protein contains 10 transmembrane segments . Expression of rhaT is induced by rhamnose in a process involving RhaS and RhaT . An inhibitory effect on rhaT induced by rhamnose appears in the presence of a higher concentration of arabinose or xylose .

## Biological Role

Catalyzes L-rhamnose:proton symport (reaction.ecocyc.TRANS-RXN-112), L-lyxopyranose:proton symport (reaction.ecocyc.TRANS-RXN0-236). Transports L-Rhamnose (molecule.C00507), L-Lyxose (molecule.C01508), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Uptake of L-rhamnose across the cytoplasmic membrane with the concomitant transport of protons into the cell (symport system) (PubMed:1551902, PubMed:2283027, PubMed:8384447). Can also transport L-mannose and L-lyxose, but at reduced rates (PubMed:1650346, PubMed:8384447). {ECO:0000269|PubMed:1551902, ECO:0000269|PubMed:1650346, ECO:0000269|PubMed:2283027, ECO:0000269|PubMed:8384447}.

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-112|reaction.ecocyc.TRANS-RXN-112]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-236|reaction.ecocyc.TRANS-RXN0-236]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00507|molecule.C00507]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C01508|molecule.C01508]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b3907|gene.b3907]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27125`
- `KEGG:ecj:JW3878;eco:b3907;ecoc:C3026_21125;`
- `GeneID:948398;`
- `GO:GO:0005886; GO:0015153; GO:0015293; GO:0015762`

## Notes

L-rhamnose-proton symporter (L-rhamnose-H(+) transport protein)
