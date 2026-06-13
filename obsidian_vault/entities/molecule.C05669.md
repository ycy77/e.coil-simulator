---
entity_id: "molecule.C05669"
entity_type: "small_molecule"
name: "beta-Nitropropanoate"
source_database: "KEGG"
source_id: "C05669"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "beta-Nitropropanoate"
  - "beta-Nitropropanoic acid"
  - "beta-Nitropropionic acid"
  - "3-Nitropropanoate"
  - "3-Nitropropionic acid"
---

# beta-Nitropropanoate

`molecule.C05669`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05669`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: beta-Nitropropanoate; beta-Nitropropanoic acid; beta-Nitropropionic acid; 3-Nitropropanoate; 3-Nitropropionic acid EcoCyc common name: 3-nitropropanoate. CPD-8147 3-Nitropropanoate is a potent inhibitor of succinate dehydrogenase and fumarase, both enzymes of the TCA cycle, and is produced by more than 30 species of plant and fungi as a means of defense against herbivores. The inhibition of these essential metabolic enzymes immediately halts energy production in poisoned cells, causing neurological disorders and, at sufficiently high doses, death . Plants and fungi associated with CPD-8147 production possess detoxifying nitronate monooxygenases (EC-1.13.12.16) as defense from the toxin. CPD-8147 3-Nitropropanoate exists in equilibrium with CPD-321 .

## Enriched Pathways

- `eco00410` beta-Alanine metabolism (KEGG)

## Annotation

KEGG compound: beta-Nitropropanoate; beta-Nitropropanoic acid; beta-Nitropropionic acid; 3-Nitropropanoate; 3-Nitropropionic acid

## Pathways

- `eco00410` beta-Alanine metabolism (KEGG)

## Outgoing Edges (1)

- `represses` --> [[reaction.ecocyc.ISOCIT-CLEAV-RXN|reaction.ecocyc.ISOCIT-CLEAV-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05669`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
