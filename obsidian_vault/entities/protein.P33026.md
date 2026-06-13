---
entity_id: "protein.P33026"
entity_type: "protein"
name: "setB"
source_database: "UniProt"
source_id: "P33026"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "setB yeiO b2170 JW2157"
---

# setB

`protein.P33026`

## Static

- Type: `protein`
- Source: `UniProt:P33026`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Involved in the efflux of sugars. The physiological role may be the detoxification of non-metabolizable sugar analogs. Can transport lactose and glucose. Early work characterized SetB as a sugar transporter; a later study implicated SetB in chromosome segregation. Inside-out membrane vesicles prepared from cells overexpressing setB accumulate significant amounts of lactose in a manner that is sensitive to the proton ionophore, carbonyl cyanide m-chlorophenylhydrazone (CCCP) . SetB can transport lactose and glucose but does not export the sugar analogs isopropyl β-D-thiogalactoside (IPTG) and 2-nitrophenyl-beta-D-thiogalactopyranoside (ONPTG); SetB has a narrower substrate specificity than B0070-MONOMER "SetA" . SetB has been implicated in chromosome segregation . Overexpression of of setB suppresses the growth defect of a mutation in parC (parC1215), encoding a subunit of topoisomerase IV*; deletion of SetB produces a delay in chromosome segregation while overproduction results in cell elongation, filamentation, and stretched or fragmented nucleoids; ΔsetB ftsk::cam double mutants have a synthetic phenotype; a SetB-GFP fusion protein localizes in a helical pattern in the cell and SetB interacts physically with MreB...

## Biological Role

Catalyzes lactose:proton antiport (reaction.ecocyc.TRANS-RXN-82). Transports Lactose (molecule.C00243), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Involved in the efflux of sugars. The physiological role may be the detoxification of non-metabolizable sugar analogs. Can transport lactose and glucose.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-82|reaction.ecocyc.TRANS-RXN-82]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00243|molecule.C00243]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b2170|gene.b2170]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33026`
- `KEGG:ecj:JW2157;eco:b2170;`
- `GeneID:946673;`
- `GO:GO:0005351; GO:0005886; GO:0007059; GO:0015767; GO:0016020; GO:0034219; GO:0036448; GO:1904659`

## Notes

Sugar efflux transporter B
