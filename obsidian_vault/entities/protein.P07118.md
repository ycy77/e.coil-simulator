---
entity_id: "protein.P07118"
entity_type: "protein"
name: "valS"
source_database: "UniProt"
source_id: "P07118"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "valS b4258 JW4215"
---

# valS

`protein.P07118`

## Static

- Type: `protein`
- Source: `UniProt:P07118`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes the attachment of valine to tRNA(Val). As ValRS can inadvertently accommodate and process structurally similar amino acids such as threonine, to avoid such errors, it has a 'posttransfer' editing activity that hydrolyzes mischarged Thr-tRNA(Val) in a tRNA-dependent manner. Valine-tRNA ligase (ValRS) is a member of the family of aminoacyl-tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. ValRS belongs to the Class I aminoacyl-tRNA synthetases . ValRS contains a conserved proline triplet that is critical for activity; it therefore requires EG12099-MONOMER EF-P for expression, which may explain evolution of the EF-P system . ValRS is a monomer in solution . A single binding site for tRNAVal was thought to exist , but evidence for a second binding site has been reported . The reaction mechanism of ValRS includes the formation of an aminoacyl adenylate intermediate, which then serves as the animo acid donor in the aminoacyl-tRNA synthetase reaction . The enzyme rapidly forms a valyl-adenylate and binds a second molecule of valine slowly . Residues in contact with valine and residues that may be part of the editing site have been determined . The ATP binding site of ValRS was determined by affinity labeling...

## Biological Role

Catalyzes L-valine:tRNAVal ligase (AMP-forming) (reaction.R03665), RXN-23924 (reaction.ecocyc.RXN-23924), RXN-23954 (reaction.ecocyc.RXN-23954), RXN-23955 (reaction.ecocyc.RXN-23955), VALINE--TRNA-LIGASE-RXN (reaction.ecocyc.VALINE--TRNA-LIGASE-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

FUNCTION: Catalyzes the attachment of valine to tRNA(Val). As ValRS can inadvertently accommodate and process structurally similar amino acids such as threonine, to avoid such errors, it has a 'posttransfer' editing activity that hydrolyzes mischarged Thr-tRNA(Val) in a tRNA-dependent manner.

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.R03665|reaction.R03665]] `KEGG` `database` - via EC:6.1.1.9
- `catalyzes` --> [[reaction.ecocyc.RXN-23924|reaction.ecocyc.RXN-23924]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-23954|reaction.ecocyc.RXN-23954]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-23955|reaction.ecocyc.RXN-23955]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.VALINE--TRNA-LIGASE-RXN|reaction.ecocyc.VALINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b4258|gene.b4258]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07118`
- `KEGG:ecj:JW4215;eco:b4258;ecoc:C3026_22970;`
- `GeneID:948785;`
- `GO:GO:0000287; GO:0002161; GO:0004832; GO:0005524; GO:0005829; GO:0006438; GO:0045903; GO:0061475`
- `EC:6.1.1.9`

## Notes

Valine--tRNA ligase (EC 6.1.1.9) (Valyl-tRNA synthetase) (ValRS)
