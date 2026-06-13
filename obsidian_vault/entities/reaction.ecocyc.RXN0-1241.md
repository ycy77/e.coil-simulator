---
entity_id: "reaction.ecocyc.RXN0-1241"
entity_type: "reaction"
name: "RXN0-1241"
source_database: "EcoCyc"
source_id: "RXN0-1241"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1241

`reaction.ecocyc.RXN0-1241`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1241`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PrmB and PrmC have sequence similarity to each other but exhibit distinct substrate specificity . PrmB is a protein-(glutamine-N5) methyltransferase that methylates ribosomal protein L3 . PrmC is a protein-(glutamine-N5) methyltransferase that shows activity toward polypeptide chain release factors RF1 and RF2 . The catalytic mechanism of the reaction as catalyzed by PrmC is discussed . EcoCyc reaction equation: S-ADENOSYLMETHIONINE + Ribosomal-protein-L3-L-glutamine -> Ribosomal-protein-L3-N5M-L-glutamine + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. PrmB and PrmC have sequence similarity to each other but exhibit distinct substrate specificity . PrmB is a protein-(glutamine-N5) methyltransferase that methylates ribosomal protein L3 . PrmC is a protein-(glutamine-N5) methyltransferase that shows activity toward polypeptide chain release factors RF1 and RF2 . The catalytic mechanism of the reaction as catalyzed by PrmC is discussed .

## Biological Role

Catalyzed by prmB (protein.P39199). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a [ribosomal protein uL3]-L-glutamine (molecule.ecocyc.Ribosomal-protein-L3-L-glutamine). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), a [ribosomal protein uL3]-N5-methyl-L-glutamine (molecule.ecocyc.Ribosomal-protein-L3-N5M-L-glutamine).

## Annotation

PrmB and PrmC have sequence similarity to each other but exhibit distinct substrate specificity . PrmB is a protein-(glutamine-N5) methyltransferase that methylates ribosomal protein L3 . PrmC is a protein-(glutamine-N5) methyltransferase that shows activity toward polypeptide chain release factors RF1 and RF2 . The catalytic mechanism of the reaction as catalyzed by PrmC is discussed .

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P39199|protein.P39199]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Ribosomal-protein-L3-N5M-L-glutamine|molecule.ecocyc.Ribosomal-protein-L3-N5M-L-glutamine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Ribosomal-protein-L3-L-glutamine|molecule.ecocyc.Ribosomal-protein-L3-L-glutamine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1241`

## Notes

S-ADENOSYLMETHIONINE + Ribosomal-protein-L3-L-glutamine -> Ribosomal-protein-L3-N5M-L-glutamine + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
