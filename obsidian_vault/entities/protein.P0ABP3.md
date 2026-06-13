---
entity_id: "protein.P0ABP3"
entity_type: "protein"
name: "dcuC"
source_database: "UniProt"
source_id: "P0ABP3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dcuC b0621 JW0613/JW0616"
---

# dcuC

`protein.P0ABP3`

## Static

- Type: `protein`
- Source: `UniProt:P0ABP3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Responsible for the transport of C4-dicarboxylates during anaerobic growth (PubMed:10368146, PubMed:8955408). Catalyzes the uptake of fumarate coupled to the export of succinate (PubMed:8955408). Can also catalyze the uptake of fumarate and the efflux of succinate, without exchange (PubMed:10368146, PubMed:8955408). Shows low rates of transport, which are sufficient for succinate export during fermentation but not for fumarate-succinate exchange in fumarate respiration, indicating that it may function in vivo as the succinate efflux carrier for glucose fermentation, even if it is also able to operate as a fumarate-succinate antiporter (PubMed:10368146). {ECO:0000269|PubMed:10368146, ECO:0000269|PubMed:8955408}. DcuC is a C4-dicarboxylate transporter which may function primarily as a succinate efflux transporter during glucose fermentation. When grown under anaerobic conditions E. coli K-12 displays transport activities for uptake, efflux and exchange of C4-dicarboxylates. Fumarate:succinate exchange is required for fumarate respiration while succinate efflux (without exchange) occurs during glucose fermentation; net uptake of C4-dicarboxylates is observed experimentally when no counter substrate is present. The exchange reaction is electroneutral while uptake and efflux are electrogenic symport reactions probably of the dicarboxylate with 3 H+ ( and see review by )...

## Biological Role

Catalyzes fumarate:succinate antiport (reaction.ecocyc.TRANS-RXN-106), fumarate:proton symport (reaction.ecocyc.TRANS-RXN-299), succinate:proton symport (reaction.ecocyc.TRANS-RXN-300). Transports Succinate (molecule.C00042).

## Annotation

FUNCTION: Responsible for the transport of C4-dicarboxylates during anaerobic growth (PubMed:10368146, PubMed:8955408). Catalyzes the uptake of fumarate coupled to the export of succinate (PubMed:8955408). Can also catalyze the uptake of fumarate and the efflux of succinate, without exchange (PubMed:10368146, PubMed:8955408). Shows low rates of transport, which are sufficient for succinate export during fermentation but not for fumarate-succinate exchange in fumarate respiration, indicating that it may function in vivo as the succinate efflux carrier for glucose fermentation, even if it is also able to operate as a fumarate-succinate antiporter (PubMed:10368146). {ECO:0000269|PubMed:10368146, ECO:0000269|PubMed:8955408}.

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-106|reaction.ecocyc.TRANS-RXN-106]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-299|reaction.ecocyc.TRANS-RXN-299]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-300|reaction.ecocyc.TRANS-RXN-300]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b0621|gene.b0621]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABP3`
- `KEGG:ecj:JW0613;ecj:JW0616;eco:b0621;ecoc:C3026_03105;`
- `GeneID:75170625;75205017;945000;`
- `GO:GO:0005469; GO:0005886; GO:0015293; GO:0015740; GO:0019664`

## Notes

Anaerobic C4-dicarboxylate transporter DcuC
