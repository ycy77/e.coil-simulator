---
entity_id: "protein.P14377"
entity_type: "protein"
name: "zraS"
source_database: "UniProt"
source_id: "P14377"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:11243806, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "zraS hydH b4003 JW3967"
---

# zraS

`protein.P14377`

## Static

- Type: `protein`
- Source: `UniProt:P14377`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:11243806, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Part of the Zra signaling pathway, an envelope stress response (ESR) system composed of the periplasmic accessory protein ZraP, the histidine kinase ZraS and the transcriptional regulator ZraR (PubMed:26438879, PubMed:30389436, PubMed:33309686). The ZraPSR system contributes to antibiotic resistance and is important for membrane integrity in the presence of membrane-targeting biocides (PubMed:30389436). ZraS is a member of the two-component regulatory system ZraS/ZraR (PubMed:11243806). Functions as a membrane-associated sensor kinase that phosphorylates ZraR in response to high concentrations of Zn(2+) or Pb(2+) in the medium (PubMed:11243806, PubMed:15522865). Binds one zinc molecule with high affinity via its periplasmic domain, inducing a conformational change that is transmitted to the histidine kinase domain and leads to the activation of ZraR (PubMed:33309686). The system has no direct role in zinc or copper resistance (PubMed:26438879). {ECO:0000269|PubMed:11243806, ECO:0000269|PubMed:15522865, ECO:0000269|PubMed:26438879, ECO:0000269|PubMed:30389436, ECO:0000269|PubMed:33309686}. This is the phosphorylated form of HYDH-MONOMER ZraS - the sensor histidine kinase of the ZraSR two-component signal transduction system...

## Biological Role

Catalyzes 2.7.13.3-RXN (reaction.ecocyc.2.7.13.3-RXN).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Part of the Zra signaling pathway, an envelope stress response (ESR) system composed of the periplasmic accessory protein ZraP, the histidine kinase ZraS and the transcriptional regulator ZraR (PubMed:26438879, PubMed:30389436, PubMed:33309686). The ZraPSR system contributes to antibiotic resistance and is important for membrane integrity in the presence of membrane-targeting biocides (PubMed:30389436). ZraS is a member of the two-component regulatory system ZraS/ZraR (PubMed:11243806). Functions as a membrane-associated sensor kinase that phosphorylates ZraR in response to high concentrations of Zn(2+) or Pb(2+) in the medium (PubMed:11243806, PubMed:15522865). Binds one zinc molecule with high affinity via its periplasmic domain, inducing a conformational change that is transmitted to the histidine kinase domain and leads to the activation of ZraR (PubMed:33309686). The system has no direct role in zinc or copper resistance (PubMed:26438879). {ECO:0000269|PubMed:11243806, ECO:0000269|PubMed:15522865, ECO:0000269|PubMed:26438879, ECO:0000269|PubMed:30389436, ECO:0000269|PubMed:33309686}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.7.13.3-RXN|reaction.ecocyc.2.7.13.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4003|gene.b4003]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P14377`
- `KEGG:ecj:JW3967;eco:b4003;ecoc:C3026_21620;`
- `GeneID:948506;`
- `GO:GO:0000155; GO:0004673; GO:0005524; GO:0005886; GO:0007165; GO:0016020; GO:0036460; GO:0071284; GO:0071294`
- `EC:2.7.13.3`

## Notes

Sensor histidine kinase ZraS (EC 2.7.13.3)
