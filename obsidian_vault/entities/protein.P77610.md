---
entity_id: "protein.P77610"
entity_type: "protein"
name: "ansP"
source_database: "UniProt"
source_id: "P77610"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ansP yncF b1453 JW5234"
---

# ansP

`protein.P77610`

## Static

- Type: `protein`
- Source: `UniProt:P77610`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

L-asparagine permease (L-asparagine transport protein) AnsP is a probable L-asparagine transporter. The equivalent gene to ansP in Salmonella enterica has been expressed and shown to confer L-asparagine uptake . AnsP is a member of the Amino Acid-Polyamine-Organocation (APC) superfamily of transporters and probably functions as an L-asparagine:proton symporter.

## Biological Role

Catalyzes asparagine:proton symport (reaction.ecocyc.TRANS-RXN-262). Transports L-Asparagine (molecule.C00152), hν (molecule.ecocyc.Light).

## Annotation

L-asparagine permease (L-asparagine transport protein)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-262|reaction.ecocyc.TRANS-RXN-262]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00152|molecule.C00152]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b1453|gene.b1453]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77610`
- `KEGG:ecj:JW5234;eco:b1453;ecoc:C3026_08450;`
- `GeneID:75171535;946019;`
- `GO:GO:0005886; GO:0006865; GO:0022857`

## Notes

L-asparagine permease (L-asparagine transport protein)
