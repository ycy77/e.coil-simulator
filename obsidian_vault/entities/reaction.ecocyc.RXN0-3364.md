---
entity_id: "reaction.ecocyc.RXN0-3364"
entity_type: "reaction"
name: "RXN0-3364"
source_database: "EcoCyc"
source_id: "RXN0-3364"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-3364

`reaction.ecocyc.RXN0-3364`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-3364`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the hydrolysis of a peptide bond in the carboxy-terminal region of HycE, processing it into its active form. EcoCyc reaction equation: HyCE-Ni-Fe-CO-CN2 + WATER -> C-terminal-32-aminoacid-Peptides + HycE-Ni-Fe-CO-CN2; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the hydrolysis of a peptide bond in the carboxy-terminal region of HycE, processing it into its active form.

## Biological Role

Substrates: H2O (molecule.C00001). Products: a C terminal 32 amino-acid peptide (molecule.ecocyc.C-terminal-32-aminoacid-Peptides).

## Annotation

This reaction is the hydrolysis of a peptide bond in the carboxy-terminal region of HycE, processing it into its active form.

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.ecocyc.C-terminal-32-aminoacid-Peptides|molecule.ecocyc.C-terminal-32-aminoacid-Peptides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-3364`

## Notes

HyCE-Ni-Fe-CO-CN2 + WATER -> C-terminal-32-aminoacid-Peptides + HycE-Ni-Fe-CO-CN2; direction=PHYSIOL-LEFT-TO-RIGHT
