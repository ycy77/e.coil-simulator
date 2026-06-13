---
entity_id: "molecule.C05688"
entity_type: "small_molecule"
name: "L-Selenocysteine"
source_database: "KEGG"
source_id: "C05688"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Selenocysteine"
---

# L-Selenocysteine

`molecule.C05688`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05688`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Selenocysteine Se is known in three biological forms. The first and the most abundant form is L-SELENOCYSTEINE, which is known as the 21st proteinogenic amino acid and is cotranslationally incorporated into selenoproteins. A second role is in the production of a modified tRNA nucleoside (5-METHYLAMINOMETHYL-2-SELENOURIDINE). A third role of Se, found in some bacteria, is in CPD-17760, which serves as a cofactor for some hydroxylases. L-SELENOCYSTEINE is present in several enzymes, including CPLX-5881 "glutathione peroxidase", THYROXINE-DEIODINASE-RXN "thyroxine deiodinase", thioredoxin reductases, FORMATEDEHYDROGH-MONOMER, CPLX-7378 and some hydrogenases. It is similar to cysteine, but with an atom of selenium taking the place of the sulfur. Selenocysteine is co-translationally incorporated into selenoproteins at an in-frame UGA codon, which normally functions as a stop codon.

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00450` Selenocompound metabolism (KEGG)

## Annotation

KEGG compound: L-Selenocysteine

## Pathways

- `eco00450` Selenocompound metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-480|reaction.ecocyc.TRANS-RXN0-480]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7440|reaction.ecocyc.RXN0-7440]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7442|reaction.ecocyc.RXN0-7442]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.SELENOCYSTEINE-LYASE-RXN|reaction.ecocyc.SELENOCYSTEINE-LYASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-480|reaction.ecocyc.TRANS-RXN0-480]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05688`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
