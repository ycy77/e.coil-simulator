---
entity_id: "protein.P0AFC0"
entity_type: "protein"
name: "nudB"
source_database: "UniProt"
source_id: "P0AFC0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nudB ntpA b1865 JW1854"
---

# nudB

`protein.P0AFC0`

## Static

- Type: `protein`
- Source: `UniProt:P0AFC0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the hydrolysis of dihydroneopterin triphosphate to dihydroneopterin monophosphate and pyrophosphate. Required for efficient folate biosynthesis. Can also hydrolyze nucleoside triphosphates with a preference for dATP. {ECO:0000269|PubMed:17698004, ECO:0000269|PubMed:8798731}. Dihydroneopterin triphosphate diphosphatase (DHNTPase) catalyzes the hydrolytic removal of pyrophosphate from dihydroneopterin triphosphate (DHNTP) to yield dihydroneopterin phosphate. This is the committed step in the biosynthesis of folate . DHNTPase was also shown to have nucleotide pyrophosphohydrolase activity with various substrates , but the catalytic efficiency of the enzyme for DHNTP is over 7 times that for dATP. The severe reduction of folate levels in a nudB null mutant similarly argues that DHNTP is the physiological substrate of the enzyme . Crystal structures of NudB have been solved . The amino acid residues involved in coordinating four metal ions were identified, substrate binding was modeled , and a catalytic mechanism was proposed . In an effort to engineer novel biosynthetic pathways for 5-carbon alcohols, it was shown that NudB has a low level of isopentenyl pyrophosphate phosphatase activity in vitro, producing the desired intermediate 3-methyl-3-butenol...

## Biological Role

Catalyzes H2NEOPTERINP3PYROPHOSPHOHYDRO-RXN (reaction.ecocyc.H2NEOPTERINP3PYROPHOSPHOHYDRO-RXN), RXN0-384 (reaction.ecocyc.RXN0-384). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the hydrolysis of dihydroneopterin triphosphate to dihydroneopterin monophosphate and pyrophosphate. Required for efficient folate biosynthesis. Can also hydrolyze nucleoside triphosphates with a preference for dATP. {ECO:0000269|PubMed:17698004, ECO:0000269|PubMed:8798731}.

## Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.H2NEOPTERINP3PYROPHOSPHOHYDRO-RXN|reaction.ecocyc.H2NEOPTERINP3PYROPHOSPHOHYDRO-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-384|reaction.ecocyc.RXN0-384]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1865|gene.b1865]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFC0`
- `KEGG:ecj:JW1854;eco:b1865;`
- `GeneID:75171937;75202729;946383;`
- `GO:GO:0000287; GO:0008828; GO:0019177; GO:0046654; GO:0046656; GO:0046872`
- `EC:3.6.1.67`

## Notes

Dihydroneopterin triphosphate diphosphatase (EC 3.6.1.67) (Dihydroneopterin triphosphate pyrophosphatase) (dATP pyrophosphohydrolase)
