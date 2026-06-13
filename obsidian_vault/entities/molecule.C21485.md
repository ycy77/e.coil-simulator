---
entity_id: "molecule.C21485"
entity_type: "small_molecule"
name: "Cytidylyl molybdenum cofactor"
source_database: "KEGG"
source_id: "C21485"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Cytidylyl molybdenum cofactor"
  - "Molybdopterin cytosine dinucleotide cofactor"
---

# Cytidylyl molybdenum cofactor

`molecule.C21485`

## Static

- Type: `small_molecule`
- Source: `KEGG:C21485`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Cytidylyl molybdenum cofactor; Molybdopterin cytosine dinucleotide cofactor EcoCyc common name: cytidylyl MoO2(OH)-molybdopterin cofactor. The name MoO2(OH)Dtpp-mCDP has been suggested as the systematic name for this compound .

## Biological Role

Produced in 1 reaction(s). Binds putative xanthine dehydrogenase (complex.ecocyc.CPLX0-761), aldehyde dehydrogenase (complex.ecocyc.CPLX0-7805).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)

## Annotation

KEGG compound: Cytidylyl molybdenum cofactor; Molybdopterin cytosine dinucleotide cofactor

## Pathways

- `eco00790` Folate biosynthesis (KEGG)

## Outgoing Edges (3)

- `binds` --> [[complex.ecocyc.CPLX0-761|complex.ecocyc.CPLX0-761]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-7805|complex.ecocyc.CPLX0-7805]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_product_of` --> [[reaction.ecocyc.RXN0-6254|reaction.ecocyc.RXN0-6254]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C21485`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
