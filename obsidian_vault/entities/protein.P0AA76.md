---
entity_id: "protein.P0AA76"
entity_type: "protein"
name: "dgoT"
source_database: "UniProt"
source_id: "P0AA76"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:31083648}; Multi-pass membrane protein {ECO:0000269|PubMed:31083648}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dgoT yidT b3691 JW5859"
---

# dgoT

`protein.P0AA76`

## Static

- Type: `protein`
- Source: `UniProt:P0AA76`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:31083648}; Multi-pass membrane protein {ECO:0000269|PubMed:31083648}.

## Enriched Summary

FUNCTION: Involved in D-galactonate metabolism (PubMed:211976, PubMed:30455279). Catalyzes the proton-dependent uptake of galactonate into the cell (PubMed:31083648). {ECO:0000269|PubMed:211976, ECO:0000269|PubMed:30455279, ECO:0000269|PubMed:31083648}. DgoT is a D-galactonate:H+symporter; in the presence of D-galactonate, DgoT mediates uptake to support growth. Purified, reconstituted DgoT (from E. coli K-12 GM4792)* mediates D-galactonate:proton symport; transport is electrogenic - DgoT likely couples the import of D-galactonate to the movement of more than one proton (see also ). Crystal structures of the transporter in an inward open conformation showing a proton translocation pathway connected to the periplasm, and of a transport-inactive mutant in an outward facing, galactonate-bound conformation, have been reported . dgoT is part of a five gene operon (dgoRKADT) encoding proteins for the metablism of D-galactonate and a transcriptional regulator (DgoR); the operon is derepressed in the presence of D-galactonate . The dgoT::kan single gene deletion strain from the Keio library is unable to grow with D-galactonate as the carbon source . In the Transporter Classification Database, DgoT is a member of the Anion:Cation Symporter (ACS) family within the Major Facilitator Superfamily (MFS)...

## Biological Role

Catalyzes galactonate:proton symport (reaction.ecocyc.TRANS-RXN-16). Transports D-Galactonate (molecule.C00880).

## Annotation

FUNCTION: Involved in D-galactonate metabolism (PubMed:211976, PubMed:30455279). Catalyzes the proton-dependent uptake of galactonate into the cell (PubMed:31083648). {ECO:0000269|PubMed:211976, ECO:0000269|PubMed:30455279, ECO:0000269|PubMed:31083648}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-16|reaction.ecocyc.TRANS-RXN-16]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00880|molecule.C00880]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b3691|gene.b3691]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AA76`
- `KEGG:ecj:JW5859;eco:b3691;ecoc:C3026_20010;`
- `GeneID:948196;`
- `GO:GO:0005886; GO:0015295; GO:0034194; GO:0042875; GO:0042881`

## Notes

D-galactonate transporter (D-galactonate/H(+) symporter)
