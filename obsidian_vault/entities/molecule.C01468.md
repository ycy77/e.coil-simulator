---
entity_id: "molecule.C01468"
entity_type: "small_molecule"
name: "4-Cresol"
source_database: "KEGG"
source_id: "C01468"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "4-Cresol"
  - "p-Cresol"
  - "4-Hydroxytoluene"
  - "4-Methylphenol"
---

# 4-Cresol

`molecule.C01468`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01468`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 4-Cresol; p-Cresol; 4-Hydroxytoluene; 4-Methylphenol EcoCyc common name: 4-methylphenol. 4-Methylphenol is one of the major Protein-bound-uremic-retention-solutes "protein-bound uremic retention solutes" . At concentrations encountered during uremia it inhibits phagocyte function and decreases leukocyte adhesion to cytokine-stimulated endothelial cells .

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00623` Toluene degradation (KEGG)
- `eco00633` Nitrotoluene degradation (KEGG)

## Annotation

KEGG compound: 4-Cresol; p-Cresol; 4-Hydroxytoluene; 4-Methylphenol

## Pathways

- `eco00623` Toluene degradation (KEGG)
- `eco00633` Nitrotoluene degradation (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R10246|reaction.R10246]] `KEGG` `database` - C00082 + C00019 + C00030 <=> C15809 + C01468 + C05198 + C00073 + C00028
- `is_product_of` --> [[reaction.ecocyc.RXN-11319|reaction.ecocyc.RXN-11319]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-500|reaction.ecocyc.TRANS-RXN0-500]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-500|reaction.ecocyc.TRANS-RXN0-500]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01468`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
