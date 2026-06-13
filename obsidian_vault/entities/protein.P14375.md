---
entity_id: "protein.P14375"
entity_type: "protein"
name: "zraR"
source_database: "UniProt"
source_id: "P14375"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "zraR hydG b4004 JW3968"
---

# zraR

`protein.P14375`

## Static

- Type: `protein`
- Source: `UniProt:P14375`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Part of the Zra signaling pathway, an envelope stress response (ESR) system composed of the periplasmic accessory protein ZraP, the histidine kinase ZraS and the transcriptional regulator ZraR (PubMed:26438879, PubMed:30389436). The ZraPSR system contributes to antibiotic resistance and is important for membrane integrity in the presence of membrane-targeting biocides (PubMed:30389436). ZraR is a member of the two-component regulatory system ZraS/ZraR (PubMed:11243806). When activated by ZraS, acts in conjunction with sigma-54 to regulate the expression of zraP in the presence of high Zn(2+) or Pb(2+) concentrations (PubMed:11243806). Also positively autoregulates the expression of the zraSR operon (PubMed:11243806). Binds to a region within the zraP-zraSR intergenic region that is characterized by two inverted repeats separated by a 14 bp spacer (PubMed:11243806). In addition, controls a regulon of genes of diverse functions that may be critical to maintain envelope integrity and cell survival under stressful conditions (PubMed:30389436). The system has no direct role in zinc or copper resistance (PubMed:26438879). {ECO:0000269|PubMed:11243806, ECO:0000269|PubMed:26438879, ECO:0000269|PubMed:30389436}. ZraR, "zinc resistance-associated regulator," controls the expression of genes involved in tolerance to high zinc concentrations...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Part of the Zra signaling pathway, an envelope stress response (ESR) system composed of the periplasmic accessory protein ZraP, the histidine kinase ZraS and the transcriptional regulator ZraR (PubMed:26438879, PubMed:30389436). The ZraPSR system contributes to antibiotic resistance and is important for membrane integrity in the presence of membrane-targeting biocides (PubMed:30389436). ZraR is a member of the two-component regulatory system ZraS/ZraR (PubMed:11243806). When activated by ZraS, acts in conjunction with sigma-54 to regulate the expression of zraP in the presence of high Zn(2+) or Pb(2+) concentrations (PubMed:11243806). Also positively autoregulates the expression of the zraSR operon (PubMed:11243806). Binds to a region within the zraP-zraSR intergenic region that is characterized by two inverted repeats separated by a 14 bp spacer (PubMed:11243806). In addition, controls a regulon of genes of diverse functions that may be critical to maintain envelope integrity and cell survival under stressful conditions (PubMed:30389436). The system has no direct role in zinc or copper resistance (PubMed:26438879). {ECO:0000269|PubMed:11243806, ECO:0000269|PubMed:26438879, ECO:0000269|PubMed:30389436}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (25)

- `activates` --> [[gene.b0811|gene.b0811]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=glnH; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1557|gene.b1557]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=cspB; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1922|gene.b1922]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=fliA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2597|gene.b2597]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=raiA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2621|gene.b2621]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=ssrA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3094|gene.b3094]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=exuR; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3164|gene.b3164]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3229|gene.b3229]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=sspA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3265|gene.b3265]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=acrE; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3283|gene.b3283]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=yrdD; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3441|gene.b3441]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=yhhY; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3461|gene.b3461]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=rpoH; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3515|gene.b3515]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=gadW; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3619|gene.b3619]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=rfaD; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3710|gene.b3710]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3870|gene.b3870]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=glnA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b4002|gene.b4002]] `RegulonDB` `C` - regulator=ZraR; target=zraP; function=+
- `activates` --> [[gene.b4003|gene.b4003]] `RegulonDB` `S` - regulator=ZraR; target=zraS; function=+
- `activates` --> [[gene.b4004|gene.b4004]] `RegulonDB` `S` - regulator=ZraR; target=zraR; function=+
- `activates` --> [[gene.b4242|gene.b4242]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b4402|gene.b4402]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=yjjY; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b4484|gene.b4484]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=cpxP; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0150|gene.b0150]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0953|gene.b0953]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=rmf; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3556|gene.b3556]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (1)

- `encodes` <-- [[gene.b4004|gene.b4004]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P14375`
- `KEGG:ecj:JW3968;eco:b4004;ecoc:C3026_21625;`
- `GeneID:948505;`
- `GO:GO:0000156; GO:0000160; GO:0000987; GO:0001216; GO:0003677; GO:0005524; GO:0005737; GO:0032993; GO:0045893`

## Notes

Transcriptional regulatory protein ZraR
