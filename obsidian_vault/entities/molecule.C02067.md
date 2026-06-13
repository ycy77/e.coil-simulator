---
entity_id: "molecule.C02067"
entity_type: "small_molecule"
name: "Pseudouridine"
source_database: "KEGG"
source_id: "C02067"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Pseudouridine"
---

# Pseudouridine

`molecule.C02067`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02067`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Pseudouridine Pseudouridine (abbreviated by the Greek letter ψ) is the most prevalent modified nucleoside found in structural (transfer, ribosomal, small nuclear, and small nucleolar) RNA. It is formed post-transcriptionally from uridine by pseudouridine synthase enzymes. Pseudouridine is found in all species, yet its role is still enigmatic. It exerts a subtle but significant "rigidifying" influence on the nearby sugar-phosphate backbone and enhances base stacking. During translation, it is thought to modulate some of the interactions between tRNA molecules and rRNAs/mRNAs. The presence of pseudouridine in tRNAs results in fine-tuning the structure of the molecule, influencing its decoding activity, improving the fidelity of protein biosynthesis, and helping to maintain the proper reading frame. The role within rRNA is less well understood .

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Annotation

KEGG compound: Pseudouridine

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-538|reaction.ecocyc.TRANS-RXN0-538]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.PSEUDOURIDINE-KINASE-RXN|reaction.ecocyc.PSEUDOURIDINE-KINASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-538|reaction.ecocyc.TRANS-RXN0-538]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.P33024|protein.P33024]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C02067`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
