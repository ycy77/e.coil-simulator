---
entity_id: "protein.P0ABS5"
entity_type: "protein"
name: "dnaG"
source_database: "UniProt"
source_id: "P0ABS5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dnaG dnaP parB b3066 JW3038"
---

# dnaG

`protein.P0ABS5`

## Static

- Type: `protein`
- Source: `UniProt:P0ABS5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: RNA polymerase that catalyzes the synthesis of short RNA molecules used as primers for DNA polymerase during DNA replication. {ECO:0000255|HAMAP-Rule:MF_00974, ECO:0000269|PubMed:1511009, ECO:0000269|PubMed:340457}. DNA primase catalyzes the synthesis of RNA primers on single-stranded template DNA . These primers then serve as the starting point for DNA synthesis by DNA polymerase III . Using single-stranded DNA in vitro, primase and NTPs are sufficient to produce RNA primers . In practice, primase also relies on ssDNA-binding protein (SSB) to stabilize its interaction with the primer. The Chi subunit of DNA polymerase III interacts with SSB near the primer, displacing DNA primase and allowing loading of the DNA polymerase III beta sliding clamp . Primase binds three distinct sites during priming, one of them as far as 115 nucleotides distant from the start of primer synthesis . In the case of lagging strand synthesis, primase dissociates from DNA each time an Okazaki fragment is completed and then repeats this binding process to begin priming of the next fragment . During replication, primase follows DNA helicase as the helicase processively unwinds DNA at the replication fork, putting down primers on the lagging strand in its wake . Three DnaG monomers bind per helicase hexamer via the DnaG carboxy-terminal domain...

## Biological Role

Catalyzes RXN0-5021 (reaction.ecocyc.RXN0-5021). Component of replisome (complex.ecocyc.CPLX0-13320). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco03030` DNA replication (KEGG)

## Annotation

FUNCTION: RNA polymerase that catalyzes the synthesis of short RNA molecules used as primers for DNA polymerase during DNA replication. {ECO:0000255|HAMAP-Rule:MF_00974, ECO:0000269|PubMed:1511009, ECO:0000269|PubMed:340457}.

## Pathways

- `eco03030` DNA replication (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5021|reaction.ecocyc.RXN0-5021]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-13320|complex.ecocyc.CPLX0-13320]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3066|gene.b3066]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABS5`
- `KEGG:ecj:JW3038;eco:b3066;ecoc:C3026_16750;`
- `GeneID:93778927;947570;`
- `GO:GO:0000428; GO:0003677; GO:0003899; GO:0005737; GO:0006260; GO:0006269; GO:0008270; GO:0030894; GO:0031297; GO:1990077; GO:1990156`
- `EC:2.7.7.101`

## Notes

DNA primase (EC 2.7.7.101)
