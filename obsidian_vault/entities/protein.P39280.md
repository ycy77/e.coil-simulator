---
entity_id: "protein.P39280"
entity_type: "protein"
name: "epmB"
source_database: "UniProt"
source_id: "P39280"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "epmB yjeK b4146 JW4106"
---

# epmB

`protein.P39280`

## Static

- Type: `protein`
- Source: `UniProt:P39280`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: With EpmA is involved in the beta-lysylation step of the post-translational modification of translation elongation factor P (EF-P) on 'Lys-34'. EpmB appears to act before EpmA. Displays lysine 2,3-aminomutase activity, producing (R)-beta-lysine from (S)-alpha-lysine (L-lysine). Cannot use (S)-ornithine or (R)-alpha-lysine as a substrate. {ECO:0000269|PubMed:17042480, ECO:0000269|PubMed:20729861, ECO:0000269|PubMed:22128152}. Co-expression of EpmB enhances the lysylation of EF-P by EpmA in vivo. EpmB may catalyze the conversion of α-lysyl-EF-P to β-lysyl-EF-P , but preliminary evidence indicates that it acts before EpmA . The epmB gene product is similar to the lysine 2,3-aminomutase of Clostridium subterminale, although phylogenetic clustering has shown that EpmB belongs to a different subfamily than the lysine 2,3-aminomutases . The purified protein has low lysine 2,3-aminomutase activity and produces (R)-β-lysine, the enantiomer of the product of the Clostridium enzyme. The low activity of the E. coli enzyme compared to the clostridial enzyme may indicate that L-lysine is not its natural substrate, or that β-lysine is required in low amounts . EpmB is a member of the "radical SAM" family of enzymes, and the lysyl-free radical intermediate of the reaction has been characterized...

## Biological Role

Catalyzes RXN0-5192 (reaction.ecocyc.RXN0-5192). Bound by Pyridoxal phosphate (molecule.C00018), S-Adenosyl-L-methionine (molecule.C00019), a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

FUNCTION: With EpmA is involved in the beta-lysylation step of the post-translational modification of translation elongation factor P (EF-P) on 'Lys-34'. EpmB appears to act before EpmA. Displays lysine 2,3-aminomutase activity, producing (R)-beta-lysine from (S)-alpha-lysine (L-lysine). Cannot use (S)-ornithine or (R)-alpha-lysine as a substrate. {ECO:0000269|PubMed:17042480, ECO:0000269|PubMed:20729861, ECO:0000269|PubMed:22128152}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5192|reaction.ecocyc.RXN0-5192]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b4146|gene.b4146]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39280`
- `KEGG:ecj:JW4106;eco:b4146;ecoc:C3026_22405;`
- `GeneID:948662;`
- `GO:GO:0016869; GO:0046872; GO:0051539`
- `EC:5.4.3.-`

## Notes

L-lysine 2,3-aminomutase (LAM) (EC 5.4.3.-) (EF-P post-translational modification enzyme B)
