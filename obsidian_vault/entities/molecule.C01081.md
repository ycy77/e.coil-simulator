---
entity_id: "molecule.C01081"
entity_type: "small_molecule"
name: "Thiamin monophosphate"
source_database: "KEGG"
source_id: "C01081"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Thiamin monophosphate"
  - "Thiamine monophosphate"
  - "Thiamin phosphate"
  - "Thiamine phosphate"
  - "TMP"
---

# Thiamin monophosphate

`molecule.C01081`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01081`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Thiamin monophosphate; Thiamine monophosphate; Thiamin phosphate; Thiamine phosphate; TMP EcoCyc common name: thiamine phosphate. Thiamin(e), also known as vitamin B1, is known to play a fundamental role in energy metabolism. Its discovery followed from the original early research on the anti-beriberi factor found in rice bran. Beriberi, a neurological disease, was particularly prevalent in Asia, where the refining of rice resulted in the removal of the thiamin-containing husk . The anti-beriberi substance was crystallized from rice polishings by Jansen and Donath in 1926 . The structure and synthesis of thiamine were reported by Williams . The compound was named thiamine when it was believed to be an amine. When it became clear that it is not an amine, the 'e' was dropped, and the name was changed to thiamin .

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 6 reaction(s).

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)

## Annotation

KEGG compound: Thiamin monophosphate; Thiamine monophosphate; Thiamin phosphate; Thiamine phosphate; TMP

## Pathways

- `eco00730` Thiamine metabolism (KEGG)

## Outgoing Edges (9)

- `is_product_of` --> [[reaction.R02134|reaction.R02134]] `KEGG` `database` - C00002 + C00378 <=> C00008 + C01081
- `is_product_of` --> [[reaction.ecocyc.RXN-12610|reaction.ecocyc.RXN-12610]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-12611|reaction.ecocyc.RXN-12611]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-3542|reaction.ecocyc.RXN0-3542]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.THI-P-SYN-RXN|reaction.ecocyc.THI-P-SYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.THIKIN-RXN|reaction.ecocyc.THIKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00617|reaction.R00617]] `KEGG` `database` - C00002 + C01081 <=> C00008 + C00068
- `is_substrate_of` --> [[reaction.R02135|reaction.R02135]] `KEGG` `database` - C01081 + C00001 <=> C00378 + C00009
- `is_substrate_of` --> [[reaction.ecocyc.THI-P-KIN-RXN|reaction.ecocyc.THI-P-KIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01081`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
