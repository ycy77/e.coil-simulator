---
entity_id: "molecule.C18237"
entity_type: "small_molecule"
name: "Molybdoenzyme molybdenum cofactor"
source_database: "KEGG"
source_id: "C18237"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Molybdoenzyme molybdenum cofactor"
  - "Molybdenum cofactor"
---

# Molybdoenzyme molybdenum cofactor

`molecule.C18237`

## Static

- Type: `small_molecule`
- Source: `KEGG:C18237`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Molybdoenzyme molybdenum cofactor; Molybdenum cofactor EcoCyc common name: MoO2(OH)-molybdopterin cofactor. The transition element molybdenum is an essential micronutrient for microorganisms, plants, and animals. Molybdenum itself is catalytically inactive and needs to be complexed by a special cofactor to gain catalytic activity. It is bound to a unique pterin (molybdopterin, or MPT), forming the molybdenum cofactor, often referred to as MoCo . The MoCo form that is synthesized initially is CPD-15870. In eukaryotes this form is incorporated into enzymes as-is, or undergoes sulfurylation as described in PWY-5963. However, in prokaryotes the initial form is modified into many different forms. For example, enzymes of the xanthine oxidase family utilize CPD-23445 (MCD), while enzymes of the DMSO reductase family utilize CPD-15873 (bis-MGD) .

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 2 reaction(s). Binds 6-N-hydroxylaminopurine resistance protein (complex.ecocyc.CPLX0-10380), periplasmic protein-L-methionine sulfoxide reducing system (complex.ecocyc.CPLX0-8213), 6-hydroxyaminopurine reductase (complex.ecocyc.CPLX0-8259).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Annotation

KEGG compound: Molybdoenzyme molybdenum cofactor; Molybdenum cofactor

## Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Outgoing Edges (10)

- `binds` --> [[complex.ecocyc.CPLX0-10380|complex.ecocyc.CPLX0-10380]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-8213|complex.ecocyc.CPLX0-8213]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-8259|complex.ecocyc.CPLX0-8259]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_product_of` --> [[reaction.ecocyc.RXN-21563|reaction.ecocyc.RXN-21563]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-24143|reaction.ecocyc.RXN-24143]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16457|reaction.ecocyc.RXN-16457]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-21601|reaction.ecocyc.RXN-21601]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-262|reaction.ecocyc.RXN0-262]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6254|reaction.ecocyc.RXN0-6254]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.CITLY-RXN|reaction.ecocyc.CITLY-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C18237`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
