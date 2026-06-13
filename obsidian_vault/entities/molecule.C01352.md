---
entity_id: "molecule.C01352"
entity_type: "small_molecule"
name: "FADH2"
source_database: "KEGG"
source_id: "C01352"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "FADH2"
---

# FADH2

`molecule.C01352`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01352`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: FADH2 FAD "Flavin adenine dinucleotide" (FAD) is an important redox cofactor involved in many reactions in metabolism. The fully oxidized form, FAD, is converted to the reduced form, FADH2 by receiving two electrons and two protons. The reduced form can be oxidized to a FADH "semireduced form" (semiquinone, FADH) by donating one electron and one proton. The semiquinone is then oxidized back to the fully oxidized form by losing a second electron and proton. Even though FAD has an aromatic ring system, FADH2 does not, making it significantly higher in energy. Many proteins contain a flavin moiety, either in the form of FAD or FMN. They are known as Flavoproteins flavoproteins.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)

## Annotation

KEGG compound: FADH2

## Pathways

- `eco00740` Riboflavin metabolism (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.R00848|reaction.R00848]] `KEGG` `database` - C00093 + C00016 <=> C00111 + C01352
- `is_substrate_of` --> [[reaction.ecocyc.RXN-8506|reaction.ecocyc.RXN-8506]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01352`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
