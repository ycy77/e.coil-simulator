---
entity_id: "protein.P77733"
entity_type: "protein"
name: "focB"
source_database: "UniProt"
source_id: "P77733"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "focB b2492 JW2477"
---

# focB

`protein.P77733`

## Static

- Type: `protein`
- Source: `UniProt:P77733`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Involved in the bidirectional transport of formate during mixed-acid fermentation. {ECO:0000269|PubMed:30247527}. focB is located in an operon (hyfABCDEFGHIR-focB) with genes encoding a putative hydrogenase complex; the FocB protein contains 6 predicted membrane helices and has 50% sequence identity with the formate channel CPLX0-7843 "FocA"; FocB is predicted to import formate for use in a formate hydrogenlyase pathway involving the hyf encoded hydrogenase . FocB activity and the direction of formate translocation is affected by electron donor identity and external pH; in the absence of CPLX0-7843 "FocA" and FocB an unidentifed system serves to transport formate . FocB and FocA are implicated in the maintenance of ion gradients during fermentation . FocB is a member of the FNT family of formate and nitrite transporters .

## Biological Role

Catalyzes TRANS-RXN-1 (reaction.ecocyc.TRANS-RXN-1).

## Annotation

FUNCTION: Involved in the bidirectional transport of formate during mixed-acid fermentation. {ECO:0000269|PubMed:30247527}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-1|reaction.ecocyc.TRANS-RXN-1]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2492|gene.b2492]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77733`
- `KEGG:ecj:JW2477;eco:b2492;ecoc:C3026_13825;`
- `GeneID:949032;`
- `GO:GO:0005886; GO:0015499; GO:0015724; GO:0019664`

## Notes

Formate channel FocB (Formate transporter FocB)
