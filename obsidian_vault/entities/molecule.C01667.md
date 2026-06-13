---
entity_id: "molecule.C01667"
entity_type: "small_molecule"
name: "Bacitracin"
source_database: "KEGG"
source_id: "C01667"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Bacitracin"
---

# Bacitracin

`molecule.C01667`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01667`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Bacitracin Bacitracin is a mixture of at least nine closely related homodetic cyclic peptides produced by TAX-1423 and TAX-1402, which is particularly active against Gram-positive bacteria. Bacitracin disrupts cell wall and peptidoglycan synthesis by binding as a complex with metallic ions to UNDECAPRENYL-DIPHOSPHATE, thus preventing its dephosphorylation into CPD-9646 by EC-3.6.1.27. CPD-9646 is a lipid carrier that is essential for the synthesis of many cell wall polymers including peptidoglycan. By sequestrating UNDECAPRENYL-DIPHOSPHATE and preventing its dephosphorylation back into CPD-9646, bacitracin prevents the loading of peptidoglycan precursors on the lipid carrier. Because translocation of these precursors to the external side of the membrane is drastically or totally impaired, further biosynthesis of the constituents of the cell envelope is stopped, eventually resulting in cell death.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00470` D-Amino acid metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

KEGG compound: Bacitracin

## Pathways

- `eco00470` D-Amino acid metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-377|reaction.ecocyc.TRANS-RXN-377]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-377|reaction.ecocyc.TRANS-RXN-377]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.TRANS-200-CPLX|complex.ecocyc.TRANS-200-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C01667`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
