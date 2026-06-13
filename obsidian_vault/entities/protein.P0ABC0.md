---
entity_id: "protein.P0ABC0"
entity_type: "protein"
name: "atpI"
source_database: "UniProt"
source_id: "P0ABC0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "atpI uncI b3739 JW5611"
---

# atpI

`protein.P0ABC0`

## Static

- Type: `protein`
- Source: `UniProt:P0ABC0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: A possible function for this protein is to guide the assembly of the membrane sector of the ATPase enzyme complex. A nonpolar mutation in the atpI gene shows that the AtpI protein is not an essential component of the H+-ATPase complex. However, the mutant has a slightly lower growth yield, and membranes contain 20% less ATPase activity than wild-type . Expression of AtpI is 10 to 20-fold lower than expression of AtpB, which is encoded by the second open reading frame of the atp operon . Processing of the mRNA and low efficiency of translation initiation may account for lower levels of atpI transcript and AtpI protein . atpI appears to affect AtpB expression at a post-translation initiation step . unc: uncoupled mutants (see ). Review:

## Annotation

FUNCTION: A possible function for this protein is to guide the assembly of the membrane sector of the ATPase enzyme complex.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b3739|gene.b3739]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABC0`
- `KEGG:ecj:JW5611;eco:b3739;ecoc:C3026_20260;`
- `GeneID:75173973;75205457;948251;`
- `GO:GO:0005886; GO:0045259; GO:1902600`

## Notes

ATP synthase protein I
