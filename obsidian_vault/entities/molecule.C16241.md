---
entity_id: "molecule.C16241"
entity_type: "small_molecule"
name: "(R)-Lipoate"
source_database: "KEGG"
source_id: "C16241"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(R)-Lipoate"
  - "(R)-Lipoic acid"
  - "(R)-(+)-Lipoate"
  - "R-(+)-Lipoic acid"
  - "1,2-Dithiolane-3R-pentanoic acid"
---

# (R)-Lipoate

`molecule.C16241`

## Static

- Type: `small_molecule`
- Source: `KEGG:C16241`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (R)-Lipoate; (R)-Lipoic acid; (R)-(+)-Lipoate; R-(+)-Lipoic acid; 1,2-Dithiolane-3R-pentanoic acid LIPOIC-ACID "Lipoate" is an organosulfur compound that is used as an essential cofactor by several important enzyme complexes. The functional group of lipoate is a ditholane ring, which is a cyclic disulfide. The enzyme complexes that require lipoate have a dedicated lipoyl domain, and lipoate is actually produced on this domain. The precursor CPD-195 molecule is first attached to a specific LYS residue within the lipoyl domain, and is then converted to lipoate by EC-2.8.1.8, which is also the source of the two sulfur atoms. Lipoate can be detached from the enzyme complex by EC-3.5.1.138, and be re-attached to the complex by EC-6.3.1.20. Enzyme known to require lipate include EC-1.2.1.105, EC-1.2.1.104, EC-1.4.1.27, EC-1.2.1.25, and EC-2.3.1.190.

## Biological Role

Consumed as substrate in 7 reaction(s). Produced in 2 reaction(s). Binds 2-oxoglutarate dehydrogenase complex (complex.ecocyc.2OXOGLUTARATEDEH-CPLX), glycine cleavage system (complex.ecocyc.GCVMULTI-CPLX), pyruvate dehydrogenase (complex.ecocyc.PYRUVATEDEH-CPLX).

## Enriched Pathways

- `eco00785` Lipoic acid metabolism (KEGG)

## Annotation

KEGG compound: (R)-Lipoate; (R)-Lipoic acid; (R)-(+)-Lipoate; R-(+)-Lipoic acid; 1,2-Dithiolane-3R-pentanoic acid

## Pathways

- `eco00785` Lipoic acid metabolism (KEGG)

## Outgoing Edges (12)

- `binds` --> [[complex.ecocyc.2OXOGLUTARATEDEH-CPLX|complex.ecocyc.2OXOGLUTARATEDEH-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.GCVMULTI-CPLX|complex.ecocyc.GCVMULTI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.PYRUVATEDEH-CPLX|complex.ecocyc.PYRUVATEDEH-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_product_of` --> [[reaction.ecocyc.RXN-13031|reaction.ecocyc.RXN-13031]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-278|reaction.ecocyc.TRANS-RXN0-278]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R07770|reaction.R07770]] `KEGG` `database` - C00002 + C16241 <=> C00013 + C16238
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17127|reaction.ecocyc.RXN-17127]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-8654|reaction.ecocyc.RXN-8654]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1139|reaction.ecocyc.RXN0-1139]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1140|reaction.ecocyc.RXN0-1140]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1141|reaction.ecocyc.RXN0-1141]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-278|reaction.ecocyc.TRANS-RXN0-278]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C16241`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
