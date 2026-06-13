---
entity_id: "complex.ecocyc.THREODEHYD-CPLX"
entity_type: "complex"
name: "threonine dehydrogenase"
source_database: "EcoCyc"
source_id: "THREODEHYD-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# threonine dehydrogenase

`complex.ecocyc.THREODEHYD-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:THREODEHYD-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P07913|protein.P07913]]

## Enriched Summary

Threonine dehydrogenase (Tdh) catalyzes the conversion of L-threonine to the unstable intermediate L-2-amino-3-oxobutanoate, which can spontaneously decarboxylate yielding aminoacetone and CO2 or be converted to acetyl-CoA and glycine by the second enzyme in the catabolic pathway. This is the major catabolic pathway for threonine utilization. This two step pathway also provides an alternative route for glycine and serine biosynthesis in E. coli. Tdh is a member of the zinc-containing long-chain alcohol/polyol dehydrogenase family . The enzyme is damaged by micromolar concentrations of hydrogen peroxide in vitro due to oxidation of the cysteine residue . Inactivation studies of Tdh have provided evidence for a catalytically essential arginine residue as well as active site cysteine and histidine residues. Mutant studies have also identified functionally important residues including His-90 , and a possible catalytic zinc binding site at Cys-38 . Review: Reitzer, L. (2005) "Catabolism of Amino Acids and Related Compounds" EcoSal 3.4.7 Threonine dehydrogenase (Tdh) catalyzes the conversion of L-threonine to the unstable intermediate L-2-amino-3-oxobutanoate, which can spontaneously decarboxylate yielding aminoacetone and CO2 or be converted to acetyl-CoA and glycine by the second enzyme in the catabolic pathway. This is the major catabolic pathway for threonine utilization...

## Biological Role

Catalyzes RXN-14249 (reaction.ecocyc.RXN-14249). Bound by Zinc cation (molecule.C00038), Fe2+ (molecule.C14818).

## Annotation

Threonine dehydrogenase (Tdh) catalyzes the conversion of L-threonine to the unstable intermediate L-2-amino-3-oxobutanoate, which can spontaneously decarboxylate yielding aminoacetone and CO2 or be converted to acetyl-CoA and glycine by the second enzyme in the catabolic pathway. This is the major catabolic pathway for threonine utilization. This two step pathway also provides an alternative route for glycine and serine biosynthesis in E. coli. Tdh is a member of the zinc-containing long-chain alcohol/polyol dehydrogenase family . The enzyme is damaged by micromolar concentrations of hydrogen peroxide in vitro due to oxidation of the cysteine residue . Inactivation studies of Tdh have provided evidence for a catalytically essential arginine residue as well as active site cysteine and histidine residues. Mutant studies have also identified functionally important residues including His-90 , and a possible catalytic zinc binding site at Cys-38 . Review: Reitzer, L. (2005) "Catabolism of Amino Acids and Related Compounds" EcoSal 3.4.7

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-14249|reaction.ecocyc.RXN-14249]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P07913|protein.P07913]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:THREODEHYD-CPLX`
- `QSPROTEOME:QS00049554`

## Notes

4*protein.P07913
