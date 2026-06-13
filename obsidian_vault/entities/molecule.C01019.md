---
entity_id: "molecule.C01019"
entity_type: "small_molecule"
name: "L-Fucose"
source_database: "KEGG"
source_id: "C01019"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Fucose"
  - "L-Fucopyranose"
  - "6-Deoxy-L-galactose"
  - "L-galactomethylose"
---

# L-Fucose

`molecule.C01019`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01019`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Fucose; L-Fucopyranose; 6-Deoxy-L-galactose EcoCyc common name: L-fucopyranose. Fucose is a hexose deoxy sugar. It received its name from the brown algae genus TAX-3011, from which it was first decribed. The alga was named because of its dark redish color, as one of the meanings of the Latin word fucus is "red paint". Algae of the TAX-3009 order produce fucose-rich polysaccahrides known as Fucoidans fucoidans. However, fucose is a common sugar, found in N-linked glycans on the mammalian, insect and plant cell surface, in many bacterial glycans, and in other biomolecules. Most of the fucose found in biology is in the L-fucoses "L conformation", and the use of D-Fucoses is rather rare (for example in some Cardenolide-Glycosides "cardenolide glycosides"). This compound stands for a mixture of CPD-10329 and CPD0-1107. In most cases, each of these compounds mutarotates quickly to form a mixture of the two, and thus it is the general rule to use this non-specific form in reactions unless it is specifically known that an enzyme can accept only one of the forms.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

KEGG compound: L-Fucose; L-Fucopyranose; 6-Deoxy-L-galactose

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.RXN-14813|reaction.ecocyc.RXN-14813]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-20|reaction.ecocyc.TRANS-RXN-20]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R03163|reaction.R03163]] `KEGG` `database` - C01019 <=> C01721
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-20|reaction.ecocyc.TRANS-RXN-20]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.P11551|protein.P11551]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C01019`
- `EcoCyc:L-fucoses`
- `CHEBI:18287`
- `canonicalized_from:molecule.ecocyc.L-fucoses`

## Notes

Included because it appears in at least one E. coli KEGG pathway. | molecule.ecocyc.L-fucoses: EcoCyc:L-fucoses
