---
entity_id: "protein.P52067"
entity_type: "protein"
name: "fsr"
source_database: "UniProt"
source_id: "P52067"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fsr b0479 JW0468"
---

# fsr

`protein.P52067`

## Static

- Type: `protein`
- Source: `UniProt:P52067`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Confers the resistance against fosmidomycin. Fsr is a putative fosmidomycin efflux protein. Expression of cloned fsr in a wild-type strain of E. coli K-12 confers resistance to this antibiotic; Fsr contains 12 putative transmembrane regions . Expression of cloned mdtG in a K-12 strain which lacks the major efflux pump permease AcrB (E. coli KAM3; see ) results in a 32-fold increase in resistance to fosmidomycin and a two-fold increase in resistance to trimethoprim but does not impact the resistance to a range of other antibiotics, dyes and toxic compounds . In the Transporter Classification Database, Fsr is a member of the Fosmidomycin Resistance (Fsr) Family within the Major Facilitator Superfamily . fsr is one of 35 efflux-encoding genes that have been deleted or inactivated in 'Efflux KnockOut-35' (EKO-35) - a K-12 BW25133-derived strain that lacks 35 efflux pumps and can be used as a platform to study their function .

## Biological Role

Catalyzes fosmidomycin:proton antiport (reaction.ecocyc.TRANS-RXN-41). Transports fosmidomycin (molecule.ecocyc.CPD0-441), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Confers the resistance against fosmidomycin.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-41|reaction.ecocyc.TRANS-RXN-41]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.CPD0-441|molecule.ecocyc.CPD0-441]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b0479|gene.b0479]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P52067`
- `KEGG:ecj:JW0468;eco:b0479;ecoc:C3026_02355;`
- `GeneID:75203145;945119;`
- `GO:GO:0005886; GO:0006974; GO:0022857; GO:0046677`

## Notes

Fosmidomycin resistance protein
