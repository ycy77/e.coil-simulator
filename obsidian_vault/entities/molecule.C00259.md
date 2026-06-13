---
entity_id: "molecule.C00259"
entity_type: "small_molecule"
name: "L-Arabinose"
source_database: "KEGG"
source_id: "C00259"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Arabinose"
  - "L-Arabinopyranose"
  - "L-Ara"
---

# L-Arabinose

`molecule.C00259`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00259`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Arabinose; L-Arabinopyranose EcoCyc common name: L-arabinopyranose. This compound stands for a mixture of ARABINOSE and BETA-L-ARABINOSE. In most cases, each of these compounds mutarotates quickly to form a mixture of the two, and thus it is the general rule to use this non-specific form in reactions unless it is specifically known that an enzyme can accept only one of the forms.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 6 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: L-Arabinose; L-Arabinopyranose

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (9)

- `is_product_of` --> [[reaction.ecocyc.ABC-2-RXN|reaction.ecocyc.ABC-2-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14808|reaction.ecocyc.RXN-14808]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14809|reaction.ecocyc.RXN-14809]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-8772|reaction.ecocyc.RXN-8772]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-10|reaction.ecocyc.TRANS-RXN-10]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-40|reaction.ecocyc.TRANS-RXN-40]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.ABC-2-RXN|reaction.ecocyc.ABC-2-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-10|reaction.ecocyc.TRANS-RXN-10]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-40|reaction.ecocyc.TRANS-RXN-40]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (3)

- `transports` <-- [[complex.ecocyc.ABC-2-CPLX|complex.ecocyc.ABC-2-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P0AE24|protein.P0AE24]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P31122|protein.P31122]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00259`
- `EcoCyc:L-ARABINOSE`
- `CHEBI:6182`
- `LIGAND-CPD:C11476`
- `PUBCHEM:5460291`
- `CHEMSPIDER:4573877`
- `CAS:147-81-9`
- `canonicalized_from:molecule.ecocyc.L-ARABINOSE`

## Notes

Included because it appears in at least one E. coli KEGG pathway. | molecule.ecocyc.L-ARABINOSE: EcoCyc:L-ARABINOSE
