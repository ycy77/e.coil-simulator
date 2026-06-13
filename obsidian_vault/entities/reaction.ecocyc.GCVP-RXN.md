---
entity_id: "reaction.ecocyc.GCVP-RXN"
entity_type: "reaction"
name: "GCVP-RXN"
source_database: "EcoCyc"
source_id: "GCVP-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Glycine cleavage system P-protein"
  - "Glycine decarboxylase"
---

# GCVP-RXN

`reaction.ecocyc.GCVP-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GCVP-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

One of three reactions of the glycine cleavage system. Glycine is decarboxylated and an amino methyl group is transferred to the prosthetic group of the gcvH protein. EcoCyc reaction equation: GLY + PROTEIN-LIPOYLLYSINE + PROTON -> AMINOMETHYLDIHYDROLIPOYL-GCVH + CARBON-DIOXIDE; direction=REVERSIBLE. One of three reactions of the glycine cleavage system. Glycine is decarboxylated and an amino methyl group is transferred to the prosthetic group of the gcvH protein.

## Biological Role

Catalyzed by glycine decarboxylase (complex.ecocyc.GCVP-CPLX). Substrates: Glycine (molecule.C00037), H+ (molecule.C00080), a [glycine-cleavage complex H protein] N6-[(R)-lipoyl]-L-lysine (molecule.ecocyc.PROTEIN-LIPOYLLYSINE). Products: CO2 (molecule.C00011), a [glycine-cleavage complex H protein] N6-aminomethyldihydrolipoyl-L-lysine (molecule.ecocyc.AMINOMETHYLDIHYDROLIPOYL-GCVH).

## Enriched Pathways

- `ecocyc.GLYCLEAV-PWY` glycine cleavage (EcoCyc)

## Annotation

One of three reactions of the glycine cleavage system. Glycine is decarboxylated and an amino methyl group is transferred to the prosthetic group of the gcvH protein.

## Pathways

- `ecocyc.GLYCLEAV-PWY` glycine cleavage (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.GCVP-CPLX|complex.ecocyc.GCVP-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMINOMETHYLDIHYDROLIPOYL-GCVH|molecule.ecocyc.AMINOMETHYLDIHYDROLIPOYL-GCVH]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.PROTEIN-LIPOYLLYSINE|molecule.ecocyc.PROTEIN-LIPOYLLYSINE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00627|molecule.C00627]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GCVP-RXN`

## Notes

GLY + PROTEIN-LIPOYLLYSINE + PROTON -> AMINOMETHYLDIHYDROLIPOYL-GCVH + CARBON-DIOXIDE; direction=REVERSIBLE
