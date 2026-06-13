---
entity_id: "protein.P31462"
entity_type: "protein"
name: "mdtL"
source_database: "UniProt"
source_id: "P31462"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mdtL yidY b3710 JW3688"
---

# mdtL

`protein.P31462`

## Static

- Type: `protein`
- Source: `UniProt:P31462`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Confers resistance to chloramphenicol. {ECO:0000269|PubMed:11566977}. MdtL (formerly YidY) is a member of the Drug:H+ Antiporter-1 (12 Spanner) (DHA1) family within the Major Facilitator Superfamily (MFS) . Overexpression of mdtL in a K-12 strain which lacks the major efflux pump permease AcrB (E. coli KAM3; see ) results in a two-fold increase in resistance to chloramphenicol but does not impact the resistance to a range of other antibiotics and toxic compounds . mdtL is one of 35 efflux-encoding genes that have been deleted or inactivated in 'Efflux KnockOut-35' (EKO-35) - a K-12 BW25133-derived strain that lacks 35 efflux pumps and can be used as a platform to study their function .

## Biological Role

Catalyzes chloramphenicol:proton antiport (reaction.ecocyc.TRANS-RXN-341). Transports chloramphenicol (molecule.ecocyc.CHLORAMPHENICOL), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Confers resistance to chloramphenicol. {ECO:0000269|PubMed:11566977}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-341|reaction.ecocyc.TRANS-RXN-341]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.CHLORAMPHENICOL|molecule.ecocyc.CHLORAMPHENICOL]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b3710|gene.b3710]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31462`
- `KEGG:ecj:JW3688;eco:b3710;ecoc:C3026_20115;`
- `GeneID:948219;`
- `GO:GO:0005886; GO:0022857; GO:0046677; GO:1990961`

## Notes

Multidrug resistance protein MdtL
