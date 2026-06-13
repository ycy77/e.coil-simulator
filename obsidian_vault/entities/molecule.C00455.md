---
entity_id: "molecule.C00455"
entity_type: "small_molecule"
name: "Nicotinamide D-ribonucleotide"
source_database: "KEGG"
source_id: "C00455"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Nicotinamide D-ribonucleotide"
  - "NMN"
  - "Nicotinamide mononucleotide"
  - "Nicotinamide ribonucleotide"
  - "Nicotinamide nucleotide"
  - "beta-Nicotinamide D-ribonucleotide"
  - "beta-Nicotinamide ribonucleotide"
  - "beta-Nicotinamide mononucleotide"
---

# Nicotinamide D-ribonucleotide

`molecule.C00455`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00455`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Nicotinamide D-ribonucleotide; NMN; Nicotinamide mononucleotide; Nicotinamide ribonucleotide; Nicotinamide nucleotide; beta-Nicotinamide D-ribonucleotide; beta-Nicotinamide ribonucleotide; beta-Nicotinamide mononucleotide EcoCyc common name: β-nicotinamide D-ribonucleotide.

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 7 reaction(s).

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)

## Annotation

KEGG compound: Nicotinamide D-ribonucleotide; NMN; Nicotinamide mononucleotide; Nicotinamide ribonucleotide; Nicotinamide nucleotide; beta-Nicotinamide D-ribonucleotide; beta-Nicotinamide ribonucleotide; beta-Nicotinamide mononucleotide

## Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)

## Outgoing Edges (11)

- `is_product_of` --> [[reaction.R00103|reaction.R00103]] `KEGG` `database` - C00003 + C00001 <=> C00020 + C00455
- `is_product_of` --> [[reaction.R00382|reaction.R00382]] `KEGG` `database` - C00003 + C00039(n) + C02128(m) <=> C00020 + C00455 + C00039(n+m)
- `is_product_of` --> [[reaction.ecocyc.DNA-LIGASE-NAD_-RXN|reaction.ecocyc.DNA-LIGASE-NAD_-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.NADPYROPHOSPHAT-RXN|reaction.ecocyc.NADPYROPHOSPHAT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RIBOSYLNICOTINAMIDE-KINASE-RXN|reaction.ecocyc.RIBOSYLNICOTINAMIDE-KINASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17920|reaction.ecocyc.RXN-17920]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7346|reaction.ecocyc.RXN0-7346]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00137|reaction.R00137]] `KEGG` `database` - C00002 + C00455 <=> C00013 + C00003
- `is_substrate_of` --> [[reaction.ecocyc.2.7.7.1-RXN|reaction.ecocyc.2.7.7.1-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.NMNAMIDOHYDRO-RXN|reaction.ecocyc.NMNAMIDOHYDRO-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.NMNNUCLEOSID-RXN|reaction.ecocyc.NMNNUCLEOSID-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00455`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
