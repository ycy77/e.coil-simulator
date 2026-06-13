---
entity_id: "protein.P31667"
entity_type: "protein"
name: "rpnA"
source_database: "UniProt"
source_id: "P31667"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rpnA yhgA b3411 JW3374"
---

# rpnA

`protein.P31667`

## Static

- Type: `protein`
- Source: `UniProt:P31667`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: A low activity DNA endonuclease yielding 3'-hydroxyl ends, equally active on ss or dsDNA, not active on dsRNA (PubMed:28096446). Shows no sequence specificity (PubMed:28096446). Upon expression enhances RecA-independent DNA recombination 49-fold, concomitantly reducing viability by 88% and probably inducing DNA damage as measured by induction of the SOS repair response in RecA cells (PubMed:28096446). RecA-independent DNA recombination leads to replacement of recipient genes with large segments of donor DNA rather than DNA addition to the donor strain; increased expression of RpnA leads to smaller replacement segments, suggesting this protein may play a role in generating crossover events (PubMed:28096446). {ECO:0000269|PubMed:28096446}. In vitro, the RpnA protein has Mg2+-dependent nonspecific DNA endonuclease activity that is stimulated by Ca2+ . RpnA is one of five proteins in E. coli that belong to the "transposase_31" family , which is distantly related to the PD-(D/E)XK nuclease superfamily . It was previously noted that RpnA has similarity to RpnC, which is encoded within the panBCD gene cluster . Overexpression of rpnA increases RecA-independent recombination, reduces cell viability, and induces expression of the DNA damage-inducible gene dinD. Site-directed mutagenesis of predicted active site residues in RpnA abolishes all three phenotypes...

## Biological Role

Catalyzes RXN0-7100 (reaction.ecocyc.RXN0-7100). Bound by Magnesium cation (molecule.C00305).

## Annotation

FUNCTION: A low activity DNA endonuclease yielding 3'-hydroxyl ends, equally active on ss or dsDNA, not active on dsRNA (PubMed:28096446). Shows no sequence specificity (PubMed:28096446). Upon expression enhances RecA-independent DNA recombination 49-fold, concomitantly reducing viability by 88% and probably inducing DNA damage as measured by induction of the SOS repair response in RecA cells (PubMed:28096446). RecA-independent DNA recombination leads to replacement of recipient genes with large segments of donor DNA rather than DNA addition to the donor strain; increased expression of RpnA leads to smaller replacement segments, suggesting this protein may play a role in generating crossover events (PubMed:28096446). {ECO:0000269|PubMed:28096446}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7100|reaction.ecocyc.RXN0-7100]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3411|gene.b3411]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31667`
- `KEGG:ecj:JW3374;eco:b3411;ecoc:C3026_18505;`
- `GeneID:947917;`
- `GO:GO:0006310; GO:0016888; GO:1990238`
- `EC:3.1.21.-`

## Notes

Recombination-promoting nuclease RpnA (EC 3.1.21.-)
