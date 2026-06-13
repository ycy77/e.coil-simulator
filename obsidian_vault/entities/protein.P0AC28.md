---
entity_id: "protein.P0AC28"
entity_type: "protein"
name: "ygfA"
source_database: "UniProt"
source_id: "P0AC28"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ygfA b2912 JW2879"
---

# ygfA

`protein.P0AC28`

## Static

- Type: `protein`
- Source: `UniProt:P0AC28`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the removal of 5-formyltetrahydrofolate. In vitro, it is a potent inhibitor of various folate-dependent enzymes in the C1 metabolism network and in vivo it might function as a folate storage. 5-formyltetrahydrofolate is also used as an antifolate rescue agent in cancer chemotherapy. Catalyzes the irreversible ATP-dependent transformation of 5-formyltetrahydrofolate (5-CHO-THF) to form 5,10-methenyltetrahydrofolate (5,10-CH=THF) (PubMed:20952389). The reverse reaction is catalyzed by the serine hydroxymethyltransferase GlyA (SHMT) (PubMed:20952389). {ECO:0000269|PubMed:18519731, ECO:0000269|PubMed:20952389, ECO:0000303|PubMed:20952389}. The YgfA protein appears to be a 5-formyltetrahydrofolate (5-CHO-THF) cyclo-ligase. 5-CHO-THF is formed in a side reaction of GLYOHMETRANS-CPLX and is an inhibitor of various folate-dependent enzymes . ygfA is important for survival under competitive planktonic growth conditions and for formation of dormant persister cells . Overexpression of ygfA leads to increased tolerance to ofloxacin . Deletion of ygfA does not cause a growth defect in rich or minimal medium. However, when grown in minimal medium with added glycine, the strain accumulates 5-CHO-THF...

## Biological Role

Catalyzes 5-FORMYL-THF-CYCLO-LIGASE-RXN (reaction.ecocyc.5-FORMYL-THF-CYCLO-LIGASE-RXN).

## Enriched Pathways

- `eco00670` One carbon pool by folate (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Annotation

FUNCTION: Involved in the removal of 5-formyltetrahydrofolate. In vitro, it is a potent inhibitor of various folate-dependent enzymes in the C1 metabolism network and in vivo it might function as a folate storage. 5-formyltetrahydrofolate is also used as an antifolate rescue agent in cancer chemotherapy. Catalyzes the irreversible ATP-dependent transformation of 5-formyltetrahydrofolate (5-CHO-THF) to form 5,10-methenyltetrahydrofolate (5,10-CH=THF) (PubMed:20952389). The reverse reaction is catalyzed by the serine hydroxymethyltransferase GlyA (SHMT) (PubMed:20952389). {ECO:0000269|PubMed:18519731, ECO:0000269|PubMed:20952389, ECO:0000303|PubMed:20952389}.

## Pathways

- `eco00670` One carbon pool by folate (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.5-FORMYL-THF-CYCLO-LIGASE-RXN|reaction.ecocyc.5-FORMYL-THF-CYCLO-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2912|gene.b2912]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC28`
- `KEGG:ecj:JW2879;eco:b2912;`
- `GeneID:945167;`
- `GO:GO:0005524; GO:0005737; GO:0009396; GO:0022611; GO:0030272; GO:0035999`
- `EC:6.3.3.2`

## Notes

5-formyltetrahydrofolate cyclo-ligase (5-FCL) (EC 6.3.3.2) (5,10-methenyltetrahydrofolate synthetase) (MTHFS)
