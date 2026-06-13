---
entity_id: "protein.P09169"
entity_type: "protein"
name: "ompT"
source_database: "UniProt"
source_id: "P09169"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ompT b0565 JW0554"
---

# ompT

`protein.P09169`

## Static

- Type: `protein`
- Source: `UniProt:P09169`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Protease that can cleave T7 RNA polymerase, ferric enterobactin receptor protein (FEP), antimicrobial peptide protamine and other proteins. This protease has a specificity for paired basic residues. {ECO:0000269|PubMed:9683502}. OmpT is an outer membrane protease with specificity for paired basic residues ; detailed studies on substrate specificity have been performed . OmpT is active under extreme denaturing conditions and shows a preference for denatured substrates . It is responsible for hydrolysis of the antimicrobial peptide protamine and is a virulence determinant in urinary tract infections . OmpT activity is cooperatively modulated by EG10669-MONOMER OmpA and lipopolysaccharide in vitro . OmpT cleaves endonuclease colicin E2 (ColE2), a bacteriocidal protein, and the associated cognate immunity protein (Im2) in the presence of BtuB; specifically, OmpT cleaves the C-terminal DNase domain of ColE2 . OmpT can cleave active human complement component C3 Kinetic parameters of the purified protein have been determined . Based on information from a crystal structure, a novel catalytic mechanism was suggested . Site-directed mutagenesis studies had previously identified essential active site residues Ser99 and His212 ; mutational studies of additional residues support a novel catalytic mechanism...

## Biological Role

Catalyzes 3.4.21.87-RXN (reaction.ecocyc.3.4.21.87-RXN).

## Annotation

FUNCTION: Protease that can cleave T7 RNA polymerase, ferric enterobactin receptor protein (FEP), antimicrobial peptide protamine and other proteins. This protease has a specificity for paired basic residues. {ECO:0000269|PubMed:9683502}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.4.21.87-RXN|reaction.ecocyc.3.4.21.87-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0565|gene.b0565]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P09169`
- `KEGG:ecj:JW0554;eco:b0565;ecoc:C3026_02800;`
- `GeneID:945185;`
- `GO:GO:0004175; GO:0004190; GO:0004252; GO:0006508; GO:0009279`
- `EC:3.4.23.49`

## Notes

Protease 7 (EC 3.4.23.49) (Omptin) (Outer membrane protein 3B) (Protease A) (Protease VII)
