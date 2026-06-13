---
entity_id: "protein.P33595"
entity_type: "protein"
name: "sgrR"
source_database: "UniProt"
source_id: "P33595"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sgrR yabN b0069 JW0068"
---

# sgrR

`protein.P33595`

## Static

- Type: `protein`
- Source: `UniProt:P33595`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Activates the small RNA gene sgrS under glucose-phosphate stress conditions as well as yfdZ. Represses its own transcription under both stress and non-stress conditions; this repression likely provides one measure of control over sgrR at the level of synthesis. Might act as a sensor of the intracellular accumulation of phosphoglucose by binding these molecules in its C-terminal solute-binding domain. {ECO:0000269|PubMed:15522088, ECO:0000269|PubMed:17209026}. "SugaR transport-related Regulator" SgrR is negatively autoregulated and coordinately activates transcription of the divergent operon. This regulator coordinates the response to glucose-phosphate stress . As the intracellular accumulation of glucose-6-phosphate correlates with SgrR induction, it has been proposed as its inducer . Autoregulation of SgrR is not affected by phosphosugar stress . In addition, the induction of sgrS expression by the nonmetabolizable glucose PTS substrate (+/-)-methyl glucoside is abolished in a sgrR mutant . The SgrR protein is a member of a novel family of regulators and contains an N terminal which is characteristic of winged-helix DNA-binding transcriptional regulators and a predicted C-terminal solute-binding domain . Inhibition in vivo of SgrR by glutamate has been shown...

## Annotation

FUNCTION: Activates the small RNA gene sgrS under glucose-phosphate stress conditions as well as yfdZ. Represses its own transcription under both stress and non-stress conditions; this repression likely provides one measure of control over sgrR at the level of synthesis. Might act as a sensor of the intracellular accumulation of phosphoglucose by binding these molecules in its C-terminal solute-binding domain. {ECO:0000269|PubMed:15522088, ECO:0000269|PubMed:17209026}.

## Outgoing Edges (9)

- `activates` --> [[gene.b0070|gene.b0070]] `RegulonDB` `C` - regulator=SgrR; target=setA; function=+
- `activates` --> [[gene.b2379|gene.b2379]] `RegulonDB` `S` - regulator=SgrR; target=alaC; function=+
- `activates` --> [[gene.b4577|gene.b4577]] `RegulonDB` `C` - regulator=SgrR; target=sgrS; function=+
- `activates` --> [[gene.b4662|gene.b4662]] `RegulonDB` `C` - regulator=SgrR; target=sgrT; function=+
- `represses` --> [[gene.b0066|gene.b0066]] `RegulonDB` `C` - regulator=SgrR; target=thiQ; function=-
- `represses` --> [[gene.b0067|gene.b0067]] `RegulonDB` `C` - regulator=SgrR; target=thiP; function=-
- `represses` --> [[gene.b0068|gene.b0068]] `RegulonDB` `C` - regulator=SgrR; target=thiB; function=-
- `represses` --> [[gene.b0069|gene.b0069]] `RegulonDB` `C` - regulator=SgrR; target=sgrR; function=-
- `represses` --> [[gene.b4762|gene.b4762]] `RegulonDB` `C` - regulator=SgrR; target=sroA; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b0069|gene.b0069]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33595`
- `KEGG:ecj:JW0068;eco:b0069;`
- `GeneID:944788;`
- `GO:GO:0000976; GO:0015833; GO:0045892; GO:0045893; GO:1904680`

## Notes

HTH-type transcriptional regulator SgrR
