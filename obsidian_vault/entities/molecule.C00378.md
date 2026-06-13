---
entity_id: "molecule.C00378"
entity_type: "small_molecule"
name: "Thiamine"
source_database: "KEGG"
source_id: "C00378"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Thiamine"
  - "Thiamin"
  - "Vitamin B1"
  - "Aneurin"
  - "Antiberiberi factor"
---

# Thiamine

`molecule.C00378`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00378`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Thiamine; Thiamin; Vitamin B1; Aneurin; Antiberiberi factor Thiamin(e), also known as vitamin B1, is known to play a fundamental role in energy metabolism. Its discovery followed from the original early research on the anti-beriberi factor found in rice bran. Beriberi, a neurological disease, was particularly prevalent in Asia, where the refining of rice resulted in the removal of the thiamin-containing husk . The anti-beriberi substance was crystallized from rice polishings by Jansen and Donath in 1926 . The structure and synthesis of thiamine were reported by Williams . The compound was named thiamine when it was believed to be an amine. When it became clear that it is not an amine, the 'e' was dropped, and the name thiamin was used . Today both names are used in the literature.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Annotation

KEGG compound: Thiamine; Thiamin; Vitamin B1; Aneurin; Antiberiberi factor

## Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R02135|reaction.R02135]] `KEGG` `database` - C01081 + C00001 <=> C00378 + C00009
- `is_product_of` --> [[reaction.ecocyc.ABC-32-RXN|reaction.ecocyc.ABC-32-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R02134|reaction.R02134]] `KEGG` `database` - C00002 + C00378 <=> C00008 + C01081
- `is_substrate_of` --> [[reaction.ecocyc.ABC-32-RXN|reaction.ecocyc.ABC-32-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.THIKIN-RXN|reaction.ecocyc.THIKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.ABC-32-CPLX|complex.ecocyc.ABC-32-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00378`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
