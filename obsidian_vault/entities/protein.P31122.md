---
entity_id: "protein.P31122"
entity_type: "protein"
name: "sotB"
source_database: "UniProt"
source_id: "P31122"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sotB ydeA b1528 JW1521"
---

# sotB

`protein.P31122`

## Static

- Type: `protein`
- Source: `UniProt:P31122`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Involved in the efflux of sugars. The physiological role may be the reduction of the intracellular concentration of toxic sugars or sugar metabolites. Transports L-arabinose and to a lesser extent IPTG. Seems to contribute to the control of the arabinose regulon. YdeA is a member of the major facilitator superfamily (MFS) of transporters . Overexpression of ydeA interferes with the intracellular accumulation of arabinose and this effect is dependent on the proton motive force; mutational activation of the ydeA promoter inhibits activation of the arabinose-inducible PBAD promoter (see also ). Deletion of ydeA (in strain MG1655) does not affect the intracellular concentration of arabinose; overexpression of ydeA reduces the intracellular concentration of arabinose; expression of ydeA is induced by arabinose . YdeA may function to limit the acumulation of toxic sugar phosphates . Crystal structures of YdeA (from E. coli strain BL21) in different conformations have been determined and are informative of the alternating access mechanism of transport . Overexpression of cloned ydeA in a K-12 strain which lacks the major efflux pump permease AcrB (E. coli KAM3; see ) does not impact resistance to a range of antibiotics, dyes and toxic compounds...

## Biological Role

Catalyzes L-arabinose:proton antiport (reaction.ecocyc.TRANS-RXN-40). Transports L-Arabinose (molecule.C00259), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Involved in the efflux of sugars. The physiological role may be the reduction of the intracellular concentration of toxic sugars or sugar metabolites. Transports L-arabinose and to a lesser extent IPTG. Seems to contribute to the control of the arabinose regulon.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-40|reaction.ecocyc.TRANS-RXN-40]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00259|molecule.C00259]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b1528|gene.b1528]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31122`
- `KEGG:ecj:JW1521;eco:b1528;ecoc:C3026_08830;`
- `GeneID:93775692;947218;`
- `GO:GO:0005886; GO:0015144; GO:0022857; GO:0055085`

## Notes

Sugar efflux transporter
