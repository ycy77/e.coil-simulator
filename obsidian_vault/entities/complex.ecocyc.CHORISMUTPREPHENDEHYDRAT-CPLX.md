---
entity_id: "complex.ecocyc.CHORISMUTPREPHENDEHYDRAT-CPLX"
entity_type: "complex"
name: "fused chorismate mutase/prephenate dehydratase"
source_database: "EcoCyc"
source_id: "CHORISMUTPREPHENDEHYDRAT-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "chorismate mutase-prephenate hydrolyase(decarboxylating)"
  - "P-protein"
---

# fused chorismate mutase/prephenate dehydratase

`complex.ecocyc.CHORISMUTPREPHENDEHYDRAT-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:CHORISMUTPREPHENDEHYDRAT-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A9J8|protein.P0A9J8]]

## Enriched Summary

Bifunctional chorismate mutase / prephenate dehydratase (PheA) carries out the shared first step in the parallel biosynthetic pathways for the aromatic amino acids tyrosine and phenylalanine, as well as the second step in phenylalanine biosynthesis. The native enzyme is a dimer of identical subunits each containing a dehydratase active site, a mutase active site and a phenylalanine binding site . L-phenylalanine was shown to feedback inhibit both the chorismate mutase and prephenate dehydratase activities of the enzyme by an allosteric mechanism . Early chemical modification studies suggested distinct, or slightly overlapping active sites with a separate phenylalanine binding site . Kinetic studies using radioactive chorismate also suggested two active sites and that prephenate, which is formed from chorismate, dissociates from the mutase site and equilibrates with the bulk medium before combining at the dehydratase site . Differential inactivation of the dehydratase and mutase activities by inhibitors also provided evidence that the two activities are catalyzed at separate sites on the enzyme, or at sites that only slightly overlap . Evidence was also presented for two cysteine residues at or close to the prephenate dehydratase active site, both of which may be essential for prephenate dehydratase activity...

## Biological Role

Catalyzes CHORISMATEMUT-RXN (reaction.ecocyc.CHORISMATEMUT-RXN), PREPHENATEDEHYDRAT-RXN (reaction.ecocyc.PREPHENATEDEHYDRAT-RXN).

## Annotation

Bifunctional chorismate mutase / prephenate dehydratase (PheA) carries out the shared first step in the parallel biosynthetic pathways for the aromatic amino acids tyrosine and phenylalanine, as well as the second step in phenylalanine biosynthesis. The native enzyme is a dimer of identical subunits each containing a dehydratase active site, a mutase active site and a phenylalanine binding site . L-phenylalanine was shown to feedback inhibit both the chorismate mutase and prephenate dehydratase activities of the enzyme by an allosteric mechanism . Early chemical modification studies suggested distinct, or slightly overlapping active sites with a separate phenylalanine binding site . Kinetic studies using radioactive chorismate also suggested two active sites and that prephenate, which is formed from chorismate, dissociates from the mutase site and equilibrates with the bulk medium before combining at the dehydratase site . Differential inactivation of the dehydratase and mutase activities by inhibitors also provided evidence that the two activities are catalyzed at separate sites on the enzyme, or at sites that only slightly overlap . Evidence was also presented for two cysteine residues at or close to the prephenate dehydratase active site, both of which may be essential for prephenate dehydratase activity . Kinetic and structural analysis of mutants lacking either, or both activities also suggested separability of the two active sites . The functional regions of PheA were more definitively mapped by recombinantly expressing, purifying and characterizing polypeptide segments derived from PheA. Chorismate mutase activity was previously localized to residues 1-109 and the crystal structure of this polypeptide was determined . In another study, prephenate dehydratase acti

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.CHORISMATEMUT-RXN|reaction.ecocyc.CHORISMATEMUT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PREPHENATEDEHYDRAT-RXN|reaction.ecocyc.PREPHENATEDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A9J8|protein.P0A9J8]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CHORISMUTPREPHENDEHYDRAT-CPLX`
- `QSPROTEOME:QS00049581`

## Notes

2*protein.P0A9J8
