---
entity_id: "protein.P77788"
entity_type: "protein"
name: "nudG"
source_database: "UniProt"
source_id: "P77788"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nudG ynjG b1759 JW1748"
---

# nudG

`protein.P77788`

## Static

- Type: `protein`
- Source: `UniProt:P77788`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Hydrolase with a preference for pyrimidine substrates. Has high activity with 5-methyl-dCTP, and much lower activity with CTP, dCTP, 5-hydroxy-dCTP, 2-hydroxy-dATP and 8-hydroxy-dGTP. {ECO:0000269|PubMed:11053429, ECO:0000269|PubMed:12509230, ECO:0000269|PubMed:15823026}. NudG is a member of the Nudix hydrolase family and shows high specificity for hydrolysis of pyrimidine (deoxy)nucleoside triphosphates . The enzyme hydrolyzes oxidized nucleotides and is therefore expected to function in DNA damage avoidance . Its preferred substrate appears to be 5-hydroxy-CTP . A solution structure of NudG has been obtained, enabling identification of the substrate binding pocket . A nudG deletion strain exhibits a 2-3-fold elevated rate of HYDROGEN-PEROXIDE-induced mutations, while overexpression of nudG suppressed mutations . Site-directed mutagenesis of various conserved amino acid residues has been performed , and residues involved in substrate binding have been identified .

## Biological Role

Catalyzes CTP diphosphohydrolase (diphosphate-forming); (reaction.R00515), RXN-14188 (reaction.ecocyc.RXN-14188), RXN0-6957 (reaction.ecocyc.RXN0-6957), RXN0-7291 (reaction.ecocyc.RXN0-7291). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Hydrolase with a preference for pyrimidine substrates. Has high activity with 5-methyl-dCTP, and much lower activity with CTP, dCTP, 5-hydroxy-dCTP, 2-hydroxy-dATP and 8-hydroxy-dGTP. {ECO:0000269|PubMed:11053429, ECO:0000269|PubMed:12509230, ECO:0000269|PubMed:15823026}.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R00515|reaction.R00515]] `KEGG` `database` - via EC:3.6.1.65
- `catalyzes` --> [[reaction.ecocyc.RXN-14188|reaction.ecocyc.RXN-14188]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6957|reaction.ecocyc.RXN0-6957]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7291|reaction.ecocyc.RXN0-7291]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1759|gene.b1759]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77788`
- `KEGG:ecj:JW1748;eco:b1759;ecoc:C3026_10040;`
- `GeneID:946277;`
- `GO:GO:0006281; GO:0008413; GO:0016787; GO:0035539; GO:0044715; GO:0044716; GO:0047840`
- `EC:3.6.1.65`

## Notes

CTP pyrophosphohydrolase (EC 3.6.1.65)
