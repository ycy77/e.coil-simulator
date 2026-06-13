---
entity_id: "molecule.C05080"
entity_type: "small_molecule"
name: "Novobiocin"
source_database: "KEGG"
source_id: "C05080"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Novobiocin"
---

# Novobiocin

`molecule.C05080`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05080`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Novobiocin The antibiotics CPD-15417, CPD-15421, and CPD-15504 target the bacterial DNA gyrase, to which they bind with KD of 10-8 to 10-10 M . The three antibiotics, which are produced by different microorganisms, share several characteristics. All three antibiotics contain a 7-hydroxy-2-aminocoumarin core. The phenolic 7-hydroxyl group of the bicyclic aminocoumarin scaffold is attached to an L-noviosyl sugar moiety, while the 2-amino group is ligated to a prenylated hydroxybenzoate unit (in CPD-15417 and CPD-15421) or to a methylpyrroledicarboxylic acid that links two aminocoumarin moieties (in CPD-15504). The noviosyl sugar is then methylated at the 4'-OH position and acylated at the 3'-OH position to produce the mature, active antibiotic. The pharmacophore of these antibiotics is the decorated noviosyl sugar, which is presented by the planar aminocoumarin to the ATP binding site of the GyrB subunit of gyrase to interdict DNA replication .

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00401` Novobiocin biosynthesis (KEGG)

## Annotation

KEGG compound: Novobiocin

## Pathways

- `eco00401` Novobiocin biosynthesis (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-353|reaction.ecocyc.TRANS-RXN-353]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-353|reaction.ecocyc.TRANS-RXN-353]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.TRANS-CPLX-202|complex.ecocyc.TRANS-CPLX-202]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C05080`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
