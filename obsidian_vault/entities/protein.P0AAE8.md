---
entity_id: "protein.P0AAE8"
entity_type: "protein"
name: "cadB"
source_database: "UniProt"
source_id: "P0AAE8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:16877381}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cadB b4132 JW4093"
---

# cadB

`protein.P0AAE8`

## Static

- Type: `protein`
- Source: `UniProt:P0AAE8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:16877381}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Under acidic conditions, in the presence of lysine, functions as a cadaverine:lysine antiporter that facilitates the excretion of cadaverine and the uptake of lysine (PubMed:14982633, PubMed:1556085). At neutral pH, also catalyzes the uptake of cadaverine via a proton symport mechanism, however the physiological relevance of this uptake activity is probably negligible because the expression of cadB is low at neutral pH (PubMed:14982633). Cadaverine uptake activity is low at acidic pH (PubMed:14982633). {ECO:0000269|PubMed:14982633, ECO:0000269|PubMed:1556085}. CadB, a lysine:cadaverine antiporter and CadA, a lysine decarboxylase constitute a lysine-dependent acid resistance system (LDAR) which functions to protect the cell from mild acid stress; the LDAR system is one of a number of amino acid dependent AR mechanisms in E. coli (reviewed in ). CadA catalyzes the decarboxylation of lysine to cadaverine and CO2 (a process that counteracts acid stress through consumption of cytosolic protons) while CadB exchanges the internal product, cadaverine for the external substrate, L-lysine. Cadaverine accumulates in the external medium when cells are grown anaerobically at pH 5.5 in the presence of L-lysine; this accumulation is negligible in a strain lacking both CadA and CadB and significantly reduced in a strain lacking CadB...

## Biological Role

Catalyzes lysine:cadaverine antiport (reaction.ecocyc.TRANS-RXN-68), cadaverine:proton symport (reaction.ecocyc.TRANS-RXN0-212). Transports L-Lysine (molecule.C00047), Cadaverine (molecule.C01672), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Under acidic conditions, in the presence of lysine, functions as a cadaverine:lysine antiporter that facilitates the excretion of cadaverine and the uptake of lysine (PubMed:14982633, PubMed:1556085). At neutral pH, also catalyzes the uptake of cadaverine via a proton symport mechanism, however the physiological relevance of this uptake activity is probably negligible because the expression of cadB is low at neutral pH (PubMed:14982633). Cadaverine uptake activity is low at acidic pH (PubMed:14982633). {ECO:0000269|PubMed:14982633, ECO:0000269|PubMed:1556085}.

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-68|reaction.ecocyc.TRANS-RXN-68]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-212|reaction.ecocyc.TRANS-RXN0-212]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00047|molecule.C00047]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C01672|molecule.C01672]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b4132|gene.b4132]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAE8`
- `KEGG:ecj:JW4093;eco:b4132;ecoc:C3026_22335;`
- `GeneID:75169651;75203985;948654;`
- `GO:GO:0005886; GO:0015293; GO:0015297; GO:0015839; GO:0043872; GO:1903401; GO:1990451`

## Notes

Cadaverine/lysine antiporter
