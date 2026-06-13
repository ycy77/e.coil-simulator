---
entity_id: "molecule.C01898"
entity_type: "small_molecule"
name: "Cellodextrin"
source_database: "KEGG"
source_id: "C01898"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Cellodextrin"
  - "Cellooligosaccharide"
---

# Cellodextrin

`molecule.C01898`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01898`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Cellodextrin; Cellooligosaccharide EcoCyc common name: a cellodextrin. Cellodextrins are β-1,4 linked glucose polymers of varying length (two or more glucose monomers) resulting from the breakdown of cellulose. During the degradation of glucose an endoglucanase first cuts the crystalline cellulose in an amorphous zone producing somewhat shorter glucans. Exoglucanases subsequently cleave these large insoluble chunks of cellulose into smaller, soluble cellodextrins which can be used by the cell. Common cellodextrins are cellotriose, cellotetraose, cellopentaose and cellohexaose.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)

## Annotation

KEGG compound: Cellodextrin; Cellooligosaccharide

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.RXN-2043|reaction.ecocyc.RXN-2043]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R02887|reaction.R02887]] `KEGG` `database` - C01898 + (n-2) C00001 <=> (n-2) C00031 + C00185

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01898`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
