---
entity_id: "reaction.ecocyc.DNA-DIRECTED-RNA-POLYMERASE-RXN"
entity_type: "reaction"
name: "DNA-DIRECTED-RNA-POLYMERASE-RXN"
source_database: "EcoCyc"
source_id: "DNA-DIRECTED-RNA-POLYMERASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DNA-DIRECTED-RNA-POLYMERASE-RXN

`reaction.ecocyc.DNA-DIRECTED-RNA-POLYMERASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DNA-DIRECTED-RNA-POLYMERASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Nucleoside-Triphosphates + RNA-Holder -> PPI + RNA-Holder; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Nucleoside-Triphosphates + RNA-Holder -> PPI + RNA-Holder; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by RNA polymerase, core enzyme (complex.ecocyc.APORNAP-CPLX). Substrates: RNA (molecule.C00046), a nucleoside triphosphate (molecule.ecocyc.Nucleoside-Triphosphates). Products: Diphosphate (molecule.C00013), RNA (molecule.C00046).

## Annotation

Nucleoside-Triphosphates + RNA-Holder -> PPI + RNA-Holder; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.APORNAP-CPLX|complex.ecocyc.APORNAP-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00046|molecule.C00046]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00046|molecule.C00046]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Nucleoside-Triphosphates|molecule.ecocyc.Nucleoside-Triphosphates]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DNA-DIRECTED-RNA-POLYMERASE-RXN`

## Notes

Nucleoside-Triphosphates + RNA-Holder -> PPI + RNA-Holder; direction=PHYSIOL-LEFT-TO-RIGHT
