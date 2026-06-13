---
entity_id: "protein.P75742"
entity_type: "protein"
name: "dtpD"
source_database: "UniProt"
source_id: "P75742"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dtpD ybgH b0709 JW0699"
---

# dtpD

`protein.P75742`

## Static

- Type: `protein`
- Source: `UniProt:P75742`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Probable proton-dependent permease that transports dipeptides. {ECO:0000250}. DtpD is a member of the Proton-dependent Oligopeptide Transporter (POT) family within the Major Facilitator Superfamily (MFS) . DtpD, purified from E. coli strain O157:H7, is monomeric when solubilized in detergent; the overexpressed protein mediates the uptake of a labeled dipeptide mimic (6-aminohexanoic acid); the transporter displays a preference for dipeptides with a cationic amino acid in the in the C-terminal position (dipeptides with lysine or arginine in the C-terminal position inhibit uptake of 6-aminohexanoic acid whereas dipeptides with lysine or arginine at the N-terminus do not) . DtpB contains two pseudosymmetric domains and is believed to function by an alternating access mechanism; a crystal structure of DtpD in the inward facing conformation (ie central cavity open towards the cytosol) is available .

## Biological Role

Catalyzes dipeptide:proton symport (reaction.ecocyc.TRANS-RXN0-288).

## Annotation

FUNCTION: Probable proton-dependent permease that transports dipeptides. {ECO:0000250}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-288|reaction.ecocyc.TRANS-RXN0-288]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0709|gene.b0709]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75742`
- `KEGG:ecj:JW0699;eco:b0709;ecoc:C3026_03545;`
- `GeneID:947368;`
- `GO:GO:0005886; GO:0015031; GO:0015333; GO:0035442; GO:0042937; GO:0071916`

## Notes

Dipeptide permease D
