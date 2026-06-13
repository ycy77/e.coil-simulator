---
entity_id: "molecule.C00166"
entity_type: "small_molecule"
name: "Phenylpyruvate"
source_database: "KEGG"
source_id: "C00166"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Phenylpyruvate"
  - "Phenylpyruvic acid"
  - "alpha-Ketohydrocinnamic acid"
  - "keto-Phenylpyruvate"
  - "3-Phenyl-2-oxopropanoate"
  - "2-Oxo-3-phenylpropanoate"
---

# Phenylpyruvate

`molecule.C00166`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00166`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Phenylpyruvate; Phenylpyruvic acid; alpha-Ketohydrocinnamic acid; keto-Phenylpyruvate; 3-Phenyl-2-oxopropanoate; 2-Oxo-3-phenylpropanoate EcoCyc common name: 3-phenyl-2-oxopropanoate. This is the ketol form tautomer of ENOL-PHENYLPYRUVATE.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 9 reaction(s).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)

## Annotation

KEGG compound: Phenylpyruvate; Phenylpyruvic acid; alpha-Ketohydrocinnamic acid; keto-Phenylpyruvate; 3-Phenyl-2-oxopropanoate; 2-Oxo-3-phenylpropanoate

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)

## Outgoing Edges (11)

- `is_product_of` --> [[reaction.R00694|reaction.R00694]] `KEGG` `database` - C00079 + C00026 <=> C00166 + C00025
- `is_product_of` --> [[reaction.ecocyc.PREPHENATEDEHYDRAT-RXN|reaction.ecocyc.PREPHENATEDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-10814|reaction.ecocyc.RXN-10814]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-21990|reaction.ecocyc.RXN-21990]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-24716|reaction.ecocyc.RXN-24716]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-24717|reaction.ecocyc.RXN-24717]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-24718|reaction.ecocyc.RXN-24718]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-24918|reaction.ecocyc.RXN-24918]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7066|reaction.ecocyc.RXN0-7066]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.PHENYLPYRUVATE-TAUTOMERASE-RXN|reaction.ecocyc.PHENYLPYRUVATE-TAUTOMERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.1.1.1.39-RXN|reaction.ecocyc.1.1.1.39-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00166`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
