---
entity_id: "molecule.C15972"
entity_type: "small_molecule"
name: "Enzyme N6-(lipoyl)lysine"
source_database: "KEGG"
source_id: "C15972"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Enzyme N6-(lipoyl)lysine"
  - "Lipoamide-E"
  - "[E2 protein]-N6-lipoyl-L-lysine"
  - "[Lipoyl-carrier protein E2]-N6-lipoyl-L-lysine"
---

# Enzyme N6-(lipoyl)lysine

`molecule.C15972`

## Static

- Type: `small_molecule`
- Source: `KEGG:C15972`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Enzyme N6-(lipoyl)lysine; Lipoamide-E; [E2 protein]-N6-lipoyl-L-lysine; [Lipoyl-carrier protein E2]-N6-lipoyl-L-lysine EcoCyc common name: a [pyruvate dehydrogenase E2 protein] N6-lipoyl-L-lysine. LIPOIC-ACID "Lipoate" is an organosulfur compound that is used as an essential cofactor by many enzyme complexes. The functional group of lipoate is a ditholane ring, which is a cyclic disulfide. The enzyme complexes that require lipoate have a dedicated Lipoyl-Protein "lipoyl domain", and lipoate is actually produced on this domain. The precursor CPD-195 molecule is first attached to a specific LYS residue within the lipoyl domain (producing Octanoylated-domains), and is then converted to lipoate by the enzyme EC-2.8.1.8, resulting in Lipoyl-Protein-N6-lipoyllysine. CPLX0-782 "Lipoate synthase" not only catalyzes the reaction, but is also the source of the two sulfur atoms (see several pathway variants under Lipoate-Biosynthesis).

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)

## Annotation

KEGG compound: Enzyme N6-(lipoyl)lysine; Lipoamide-E; [E2 protein]-N6-lipoyl-L-lysine; [Lipoyl-carrier protein E2]-N6-lipoyl-L-lysine

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R12603|reaction.R12603]] `KEGG` `database` - C15973 + C15498 <=> C15972 + C00001 + C01335
- `is_product_of` --> [[reaction.ecocyc.RXN0-1132|reaction.ecocyc.RXN0-1132]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12508|reaction.ecocyc.RXN-12508]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1134|reaction.ecocyc.RXN0-1134]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C15972`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
