---
entity_id: "protein.P0AA78"
entity_type: "protein"
name: "exuT"
source_database: "UniProt"
source_id: "P0AA78"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "exuT b3093 JW3064"
---

# exuT

`protein.P0AA78`

## Static

- Type: `protein`
- Source: `UniProt:P0AA78`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Transport of aldohexuronates such as D-glucuronate and D-galacturonate (PubMed:6343797, PubMed:783117). Under anaerobic conditions, can play a critical role as a D-glucose transporter in the absence of sugar-PTS system (PubMed:32038601). {ECO:0000269|PubMed:32038601, ECO:0000269|PubMed:6343797, ECO:0000269|PubMed:783117}. ExuT is a transporter for aldohexuronates such as D-galacturonate and D-glucuronate. Mutations affecting the transport of hexuronates have been shown to map to the exuT gene . ExuT is a member of the major facilitator superfamily (MFS) of transporters and probably functions as an aldohexuronate/proton symporter. The exuT gene constitutes a hexuronate-inducible single gene operon, whose expression is controlled by the ExuR regulator . Imported hexuronates are initially metabolised to 2-keto-3-deoxy-D-gluconate.

## Biological Role

Catalyzes D-galacturonate:proton symport (reaction.ecocyc.TRANS-RXN-123), D-glucuronate:proton symport (reaction.ecocyc.TRANS-RXN-35). Transports D-Glucuronate (molecule.C00191), D-Galacturonate (molecule.C00333), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Transport of aldohexuronates such as D-glucuronate and D-galacturonate (PubMed:6343797, PubMed:783117). Under anaerobic conditions, can play a critical role as a D-glucose transporter in the absence of sugar-PTS system (PubMed:32038601). {ECO:0000269|PubMed:32038601, ECO:0000269|PubMed:6343797, ECO:0000269|PubMed:783117}.

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-123|reaction.ecocyc.TRANS-RXN-123]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-35|reaction.ecocyc.TRANS-RXN-35]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00191|molecule.C00191]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00333|molecule.C00333]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b3093|gene.b3093]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AA78`
- `KEGG:ecj:JW3064;eco:b3093;ecoc:C3026_16890;`
- `GeneID:947601;`
- `GO:GO:0005886; GO:0015134; GO:0015736`

## Notes

Hexuronate transporter (Aldohexuronate transport system)
