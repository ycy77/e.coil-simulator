---
entity_id: "protein.P0A729"
entity_type: "protein"
name: "yceF"
source_database: "UniProt"
source_id: "P0A729"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00528, ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yceF b1087 JW5155"
---

# yceF

`protein.P0A729`

## Static

- Type: `protein`
- Source: `UniProt:P0A729`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00528, ECO:0000305}.

## Enriched Summary

FUNCTION: Nucleoside triphosphate pyrophosphatase that hydrolyzes 7-methyl-GTP (m(7)GTP) (PubMed:24210219). May have a dual role in cell division arrest and in preventing the incorporation of modified nucleotides into cellular nucleic acids (PubMed:24210219). {ECO:0000269|PubMed:24210219}. YceF shows triphosphatase activity with the modified nucleotide 7-methyl-GTP (m7GTP) as a substrate. The authors suggest that the in vivo function of YceF may be to monitor the ribonucleotide pool and prevent unspecific incorporation of modified bases into cellular RNAs . YceF exists as a mixture of monomers and dimers in solution. A crystal structure of the protein has been solved at 1.85 Å resolution . Mutations in predicted active site residues reduce the catalytic activity. The unprotonated Asp69 residue is proposed to function as a general base that produces a nucleophilic hydroxide ion which attacks the α-phosphate of the substrate .

## Biological Role

Catalyzes RXN0-7079 (reaction.ecocyc.RXN0-7079).

## Annotation

FUNCTION: Nucleoside triphosphate pyrophosphatase that hydrolyzes 7-methyl-GTP (m(7)GTP) (PubMed:24210219). May have a dual role in cell division arrest and in preventing the incorporation of modified nucleotides into cellular nucleic acids (PubMed:24210219). {ECO:0000269|PubMed:24210219}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7079|reaction.ecocyc.RXN0-7079]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1087|gene.b1087]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A729`
- `KEGG:ecj:JW5155;eco:b1087;ecoc:C3026_06580;`
- `GeneID:75203673;945631;`
- `GO:GO:0005737; GO:0009117; GO:0047429`
- `EC:3.6.1.-`

## Notes

7-methyl-GTP pyrophosphatase (m(7)GTP pyrophosphatase) (EC 3.6.1.-)
