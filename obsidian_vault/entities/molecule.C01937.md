---
entity_id: "molecule.C01937"
entity_type: "small_molecule"
name: "Methotrexate"
source_database: "KEGG"
source_id: "C01937"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Methotrexate"
---

# Methotrexate

`molecule.C01937`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01937`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Methotrexate Methotrexate is a chemotherapy agent and immune-system suppressant used to treat cancer, autoimmune diseases, ectopic pregnancy, and for medical abortions. In 2017, it was the 117th most commonly prescribed medication in the United States, with more than six million prescriptions. For cancer, methotrexate competitively inhibits EC-1.5.1.3, and thus interferes with DNA synthesis . As for its action as an immune-system suppressant, several other mechanisms have been suggested .

## Enriched Pathways

- `eco04981` Folate transport and metabolism (KEGG)

## Annotation

KEGG compound: Methotrexate

## Pathways

- `eco04981` Folate transport and metabolism (KEGG)

## Outgoing Edges (3)

- `represses` --> [[reaction.ecocyc.1.5.1.34-RXN|reaction.ecocyc.1.5.1.34-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.DIHYDROFOLATEREDUCT-RXN|reaction.ecocyc.DIHYDROFOLATEREDUCT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GLUTATHIONE-SYN-RXN|reaction.ecocyc.GLUTATHIONE-SYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01937`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
