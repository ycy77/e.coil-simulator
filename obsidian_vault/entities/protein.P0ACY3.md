---
entity_id: "protein.P0ACY3"
entity_type: "protein"
name: "yeaG"
source_database: "UniProt"
source_id: "P0ACY3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:18276156}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yeaG b1783 JW1772"
---

# yeaG

`protein.P0ACY3`

## Static

- Type: `protein`
- Source: `UniProt:P0ACY3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:18276156}.

## Enriched Summary

FUNCTION: Kinase that plays a role in the adaptation to sustained nitrogen starvation (PubMed:26621053). May act by indirectly repressing the transcription of the two toxin/antitoxin modules mqsR/mqsA and dinJ/yafQ, which positively impacts the expression of rpoS, the master regulator of the general bacterial stress response (PubMed:26621053). In vitro, can phosphorylate the isocitrate lyase AceA only in the presence of malate, suggesting that it may play a role during glucose to malate shift (PubMed:33889145). Displays autokinase and casein kinase activities in vitro (PubMed:18276156). It can also phosphorylate specifically a 65 kDa unidentified cytoplasmic protein (Ref.5). {ECO:0000269|PubMed:18276156, ECO:0000269|PubMed:26621053, ECO:0000269|PubMed:33889145, ECO:0000269|Ref.5}. YeaG plays a role in the adaptation to sustained nitrogen (N) starvation . YeaG is a member of the PrkA family of serine protein kinases. Purified YeaG has autokinase and casein kinase activity . YeaG may phosphorylate an unknown 65 kDa cytoplasmic protein . Comparison of the phosphoproteomes of wild-type and a ΔyeaG mutant during the shift from glucose to malate metabolism shows several differentially phosphorylated proteins, including ISOCIT-LYASE-MONOMER (AceA). In vitro, YeaG is able to phosphorylate ISOCIT-LYASE-MONOMER only in the presence of malate...

## Biological Role

Catalyzes PROTEIN-KINASE-RXN (reaction.ecocyc.PROTEIN-KINASE-RXN). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

FUNCTION: Kinase that plays a role in the adaptation to sustained nitrogen starvation (PubMed:26621053). May act by indirectly repressing the transcription of the two toxin/antitoxin modules mqsR/mqsA and dinJ/yafQ, which positively impacts the expression of rpoS, the master regulator of the general bacterial stress response (PubMed:26621053). In vitro, can phosphorylate the isocitrate lyase AceA only in the presence of malate, suggesting that it may play a role during glucose to malate shift (PubMed:33889145). Displays autokinase and casein kinase activities in vitro (PubMed:18276156). It can also phosphorylate specifically a 65 kDa unidentified cytoplasmic protein (Ref.5). {ECO:0000269|PubMed:18276156, ECO:0000269|PubMed:26621053, ECO:0000269|PubMed:33889145, ECO:0000269|Ref.5}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PROTEIN-KINASE-RXN|reaction.ecocyc.PROTEIN-KINASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1783|gene.b1783]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACY3`
- `KEGG:ecj:JW1772;eco:b1783;ecoc:C3026_10170;`
- `GeneID:86946181;946297;`
- `GO:GO:0004672; GO:0004674; GO:0005737; GO:0006995`
- `EC:2.7.11.1`

## Notes

Serine/threonine kinase YeaG (Ser/Thr kinase YeaG) (EC 2.7.11.1) (Protein kinase YeaG) (Stress kinase YeaG)
