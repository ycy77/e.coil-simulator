---
entity_id: "protein.P76472"
entity_type: "protein"
name: "arnD"
source_database: "UniProt"
source_id: "P76472"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "arnD pmrJ yfbH b2256 JW2250"
---

# arnD

`protein.P76472`

## Static

- Type: `protein`
- Source: `UniProt:P76472`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the deformylation of 4-deoxy-4-formamido-L-arabinose-phosphoundecaprenol to 4-amino-4-deoxy-L-arabinose-phosphoundecaprenol. The modified arabinose is attached to lipid A and is required for resistance to polymyxin and cationic antimicrobial peptides (Probable). {ECO:0000305|PubMed:15695810}. ArnD is predicted to act as a deformylase that removes the formyl group from undecaprenyl phosphate-L-Ara4FN . Deletion of arnD results in restoration of polymyxin sensitivity in a polymyxin-resitant pmrAc strain . Expression of the arnBCADTEF operon increased during growth with elevated FeSO4, FeCl3, or ZnSO4 and was dependent upon the BasSR two-component signal transduction system .

## Biological Role

Catalyzes RXN0-5409 (reaction.ecocyc.RXN0-5409).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

FUNCTION: Catalyzes the deformylation of 4-deoxy-4-formamido-L-arabinose-phosphoundecaprenol to 4-amino-4-deoxy-L-arabinose-phosphoundecaprenol. The modified arabinose is attached to lipid A and is required for resistance to polymyxin and cationic antimicrobial peptides (Probable). {ECO:0000305|PubMed:15695810}.

## Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5409|reaction.ecocyc.RXN0-5409]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2256|gene.b2256]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76472`
- `KEGG:ecj:JW2250;eco:b2256;ecoc:C3026_12600;`
- `GeneID:93774918;945334;`
- `GO:GO:0009103; GO:0009245; GO:0010041; GO:0016020; GO:0016811; GO:0036108; GO:0046677`
- `EC:3.5.1.n3`

## Notes

Probable 4-deoxy-4-formamido-L-arabinose-phosphoundecaprenol deformylase ArnD (EC 3.5.1.n3)
