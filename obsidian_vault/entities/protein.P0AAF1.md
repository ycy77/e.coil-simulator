---
entity_id: "protein.P0AAF1"
entity_type: "protein"
name: "potE"
source_database: "UniProt"
source_id: "P0AAF1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02073, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:9045651, ECO:0000305|PubMed:1939141}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_02073}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "potE b0692 JW0679"
---

# potE

`protein.P0AAF1`

## Static

- Type: `protein`
- Source: `UniProt:P0AAF1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02073, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:9045651, ECO:0000305|PubMed:1939141}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_02073}.

## Enriched Summary

FUNCTION: Catalyzes both the uptake and excretion of putrescine. The uptake of putrescine is dependent on the membrane potential and the excretion involves putrescine-ornithine antiporter activity. {ECO:0000255|HAMAP-Rule:MF_02073, ECO:0000269|PubMed:1584788, ECO:0000269|PubMed:1939141, ECO:0000269|PubMed:9045651}. PotE is a putrescine transporter which mediates putrescine efflux by a putrescine:ornithine antiport reaction and putrescine import by proton symport. potE is located in an operon with speF encoding an inducible ornithine decarboxylase; production and excretion of putrescine may be beneficial for growth under acidic conditions (see ). Overexpression of potE in a polyamine-requiring strain increases putrescine uptake . PotE mediated putrescine uptake (measured in a polyamine requiring strain lacking the putrescine uptake systems PotABCD and PotFGHI) is dependent on membrane potential; uptake stimulates growth in the polyamine requiring mutant; uptake is inhibited by carbonyl cyanide m-chlorophenylhydrazone (CCCP), and by high concentrations of ornithine after putrescine accumulates in cells . PotE mediates the excretion of excess putrescine from intact cells; PotE mediates putrescine efflux via a 1:1 putrescine/ornithine antiport reaction; PotE also mediates putrescine:putrescine and ornithine:ornithine exchange reactions in vitro...

## Biological Role

Catalyzes putrescine:proton symport (reaction.ecocyc.TRANS-RXN-69), putrescine:ornithine antiport (reaction.ecocyc.TRANS-RXN0-211). Transports L-Ornithine (molecule.C00077), Putrescine (molecule.C00134).

## Annotation

FUNCTION: Catalyzes both the uptake and excretion of putrescine. The uptake of putrescine is dependent on the membrane potential and the excretion involves putrescine-ornithine antiporter activity. {ECO:0000255|HAMAP-Rule:MF_02073, ECO:0000269|PubMed:1584788, ECO:0000269|PubMed:1939141, ECO:0000269|PubMed:9045651}.

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-69|reaction.ecocyc.TRANS-RXN-69]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-211|reaction.ecocyc.TRANS-RXN0-211]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00077|molecule.C00077]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00134|molecule.C00134]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b0692|gene.b0692]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAF1`
- `KEGG:ecj:JW0679;eco:b0692;ecoc:C3026_03450;`
- `GeneID:93776795;945422;`
- `GO:GO:0005886; GO:0015293; GO:0015496; GO:0015847`

## Notes

Putrescine transporter PotE (Putrescine-proton symporter / putrescine-ornithine antiporter)
