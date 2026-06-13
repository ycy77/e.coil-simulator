---
entity_id: "protein.P77397"
entity_type: "protein"
name: "mhpA"
source_database: "UniProt"
source_id: "P77397"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mhpA b0347 JW0338"
---

# mhpA

`protein.P77397`

## Static

- Type: `protein`
- Source: `UniProt:P77397`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the insertion of one atom of molecular oxygen into position 2 of the phenyl ring of 3-(3-hydroxyphenyl)propionate (3-HPP) and hydroxycinnamic acid (3HCI). {ECO:0000269|PubMed:9603882}. E. coli is able to utilize aromatic acids as carbon and energy sources. A meta-cleavage pathway is used for the catabolism of 3-(3-hydroxyphenyl)propionate . mhpA encodes a flavin-type monooxygenase that was purified and biochemically characterized only recently . The C terminus of MhpA does not show similarity to other 3-hydroxyaromatic acid hydroxylases; however, it is required for catalytic activity . A ΔmhpA mutant is unable to grow with 3-(3-hydroxyphenyl)propionate (3HPP, MHP) as the sole source of carbon . Enzyme activity is induced after growth with MHP or hydroxycinnamate (HCA) .

## Biological Role

Catalyzes MHPHYDROXY-RXN (reaction.ecocyc.MHPHYDROXY-RXN), RXN-10040 (reaction.ecocyc.RXN-10040). Bound by FAD (molecule.C00016).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Annotation

FUNCTION: Catalyzes the insertion of one atom of molecular oxygen into position 2 of the phenyl ring of 3-(3-hydroxyphenyl)propionate (3-HPP) and hydroxycinnamic acid (3HCI). {ECO:0000269|PubMed:9603882}.

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.MHPHYDROXY-RXN|reaction.ecocyc.MHPHYDROXY-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-10040|reaction.ecocyc.RXN-10040]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0347|gene.b0347]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77397`
- `KEGG:ecj:JW0338;eco:b0347;ecoc:C3026_24870;`
- `GeneID:945197;`
- `GO:GO:0008688; GO:0019380; GO:0019622; GO:0042802; GO:0071949`
- `EC:1.14.13.127`

## Notes

3-(3-hydroxy-phenyl)propionate/3-hydroxycinnamic acid hydroxylase (3-HCI hydroxylase) (3-HPP hydroxylase) (EC 1.14.13.127)
