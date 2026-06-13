---
entity_id: "molecule.C00032"
entity_type: "small_molecule"
name: "Heme"
source_database: "KEGG"
source_id: "C00032"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Heme"
  - "Haem"
  - "Protoheme"
  - "Heme B"
  - "Protoheme IX"
---

# Heme

`molecule.C00032`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00032`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Heme; Haem; Protoheme; Heme B; Protoheme IX EcoCyc common name: heme b. 'Heme' is usually understood as any tetrapyrrolic chelate of iron. The terms 'ferroheme' and 'ferriheme' refer to the Fe(II) and Fe(III) oxidation states in heme (even though Fe(IV) is found as a catalytic intermediate in some systems). Heme-b "Heme b", whose PROTOHEME "ferrous form" is known as protoheme IX, is the immediate product of the heme biosynthesis pathways (by ferro-chelation of PROTOPORPHYRIN_IX) and the most abundant heme form. It is found in common proteins such as hemoglobin and myoglobin. Heme b is part of Cytochromes-B "b-type cytochromes".

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s). Binds cytochrome bd-II ubiquinol:oxygen oxidoreductase (complex.ecocyc.APP-UBIOX-CPLX), formate dehydrogenase O (complex.ecocyc.CPLX0-13310), succinate:quinone oxidoreductase (complex.ecocyc.CPLX0-8160), hydrogenase 1, oxygen tolerant hydrogenase (complex.ecocyc.CPLX0-8167), cytochrome bd-I ubiquinol:oxygen oxidoreductase (complex.ecocyc.CYT-D-UBIOX-CPLX), cytochrome bo3 ubiquinol:oxygen oxidoreductase (complex.ecocyc.CYT-O-UBIOX-CPLX), formate dehydrogenase N (complex.ecocyc.FORMATEDEHYDROGN-CPLX), nitrate reductase A (complex.ecocyc.NITRATREDUCTA-CPLX), and 3 more.

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Heme; Haem; Protoheme; Heme B; Protoheme IX

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (13)

- `binds` --> [[complex.ecocyc.APP-UBIOX-CPLX|complex.ecocyc.APP-UBIOX-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-13310|complex.ecocyc.CPLX0-13310]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-8160|complex.ecocyc.CPLX0-8160]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-8167|complex.ecocyc.CPLX0-8167]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CYT-D-UBIOX-CPLX|complex.ecocyc.CYT-D-UBIOX-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CYT-O-UBIOX-CPLX|complex.ecocyc.CYT-O-UBIOX-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.FORMATEDEHYDROGN-CPLX|complex.ecocyc.FORMATEDEHYDROGN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.NITRATREDUCTA-CPLX|complex.ecocyc.NITRATREDUCTA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.NITRATREDUCTZ-CPLX|complex.ecocyc.NITRATREDUCTZ-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[protein.P0ABE5|protein.P0ABE5]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[protein.P33927|protein.P33927]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_product_of` --> [[reaction.R00310|reaction.R00310]] `KEGG` `database` - C02191 + C14818 <=> C00032 + 2 C00080
- `is_substrate_of` --> [[reaction.ecocyc.RXN-8073|reaction.ecocyc.RXN-8073]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00032`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
