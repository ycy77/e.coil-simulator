---
entity_id: "molecule.C00251"
entity_type: "small_molecule"
name: "Chorismate"
source_database: "KEGG"
source_id: "C00251"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Chorismate"
  - "Chorismic acid"
  - "(3R,4R)-3-[(1-Carboxyethenyl)oxy]-4-hydroxycyclohexa-1,5-diene-1-carboxylate"
---

# Chorismate

`molecule.C00251`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00251`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Chorismate; Chorismic acid; (3R,4R)-3-[(1-Carboxyethenyl)oxy]-4-hydroxycyclohexa-1,5-diene-1-carboxylate

## Biological Role

Consumed as substrate in 9 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00790` Folate biosynthesis (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)
- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)

## Annotation

KEGG compound: Chorismate; Chorismic acid; (3R,4R)-3-[(1-Carboxyethenyl)oxy]-4-hydroxycyclohexa-1,5-diene-1-carboxylate

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00790` Folate biosynthesis (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)
- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)

## Outgoing Edges (11)

- `is_product_of` --> [[reaction.ecocyc.CHORISMATE-SYNTHASE-RXN|reaction.ecocyc.CHORISMATE-SYNTHASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00985|reaction.R00985]] `KEGG` `database` - C00251 + C00014 <=> C00108 + C00022 + C00001
- `is_substrate_of` --> [[reaction.R00986|reaction.R00986]] `KEGG` `database` - C00251 + C00064 <=> C00108 + C00022 + C00025
- `is_substrate_of` --> [[reaction.ecocyc.ANTHRANSYN-RXN|reaction.ecocyc.ANTHRANSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.CHORISMATEMUT-RXN|reaction.ecocyc.CHORISMATEMUT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.CHORPYRLY-RXN|reaction.ecocyc.CHORPYRLY-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ISOCHORSYN-RXN|reaction.ecocyc.ISOCHORSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PABASYN-RXN|reaction.ecocyc.PABASYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22711|reaction.ecocyc.RXN-22711]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22713|reaction.ecocyc.RXN-22713]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.PREPHENATEDEHYDRAT-RXN|reaction.ecocyc.PREPHENATEDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00251`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
