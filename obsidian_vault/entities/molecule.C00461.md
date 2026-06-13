---
entity_id: "molecule.C00461"
entity_type: "small_molecule"
name: "Chitin"
source_database: "KEGG"
source_id: "C00461"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Chitin"
  - "beta-1,4-Poly-N-acetyl-D-glucosamine"
  - "[1,4-(N-Acetyl-beta-D-glucosaminyl)]n"
  - "[1,4-(N-Acetyl-beta-D-glucosaminyl)]n+1"
---

# Chitin

`molecule.C00461`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00461`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Chitin; beta-1,4-Poly-N-acetyl-D-glucosamine; [1,4-(N-Acetyl-beta-D-glucosaminyl)]n; [1,4-(N-Acetyl-beta-D-glucosaminyl)]n+1 CHITIN Chitin is a polymer of repeating units of β-(1,4)-linked N-ACETYL-BETA-D-GLUCOSAMINE (GlcNAc)n. It may be the second most abundant biopolymer in the world, after cellulose. It is the main component of the cell walls of fungi, the exoskeletons of arthropods such as crustaceans and the insects, the radula of mollusks, and the beaks of the cephalopods. Chitin polymers have a high degree of polymerization and are insoluble in water .

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)

## Annotation

KEGG compound: Chitin; beta-1,4-Poly-N-acetyl-D-glucosamine; [1,4-(N-Acetyl-beta-D-glucosaminyl)]n; [1,4-(N-Acetyl-beta-D-glucosaminyl)]n+1

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.R02334|reaction.R02334]] `KEGG` `database` - C00461 + C00001 <=> C01674 + C00461
- `is_substrate_of` --> [[reaction.R02334|reaction.R02334]] `KEGG` `database` - C00461 + C00001 <=> C01674 + C00461
- `is_substrate_of` --> [[reaction.ecocyc.3.2.1.14-RXN|reaction.ecocyc.3.2.1.14-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00461`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
