---
entity_id: "protein.P69829"
entity_type: "protein"
name: "ptsN"
source_database: "UniProt"
source_id: "P69829"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ptsN rpoP yhbI b3204 JW3171"
---

# ptsN

`protein.P69829`

## Static

- Type: `protein`
- Source: `UniProt:P69829`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Seems to have a role in regulating nitrogen assimilation. {ECO:0000250}. ptsN encodes a protein paralogous to Enzyme IIAfru of the phosphoenolpyruvate (PEP)-dependent carbohydrate phosphotransferase system (PTS) . PtsN regulates the activity or expression of potassium transporters . The PtsN protein, also known as Enzyme IIANtr, is part of a phosphorelay system (PTSNtr) in E. coli K-12 that may have a role in the regulation of nitrogen metabolism although this has been questioned . The PTSNtr has been implicated in the control of a stress-responsive YCGO-MONOMER "CvrA" mediated K+ efflux pathway . PtsN can be phosphorylated in vivo; both the energy coupling phosphotransferases of the Ntr PTS (EG12188-MONOMER PtsP and EG12147-MONOMER Npr) as well as the sugar PTS contribute to the phosphorylation of PtsN . Dephosphorylated PtsN interacts with the potassium transporter TrkA and inhibits its activity . Dephosphorylated PtsN also interacts with the sensor kinase KdpD and stimulates its activity, resulting in increased levels of phosphorylated response regulator KdpE, thereby increasing expression of kdpFABC, a high-affinity potassium transporter . Via regulating the intracellular K+ concentration, PtsN affects sigma factor selectivity and thus transcription levels for a number of genes...

## Enriched Pathways

- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: Seems to have a role in regulating nitrogen assimilation. {ECO:0000250}.

## Pathways

- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (1)

- `activates` --> [[reaction.ecocyc.KDPD-RXN|reaction.ecocyc.KDPD-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Reactions

## Incoming Edges (1)

- `encodes` <-- [[gene.b3204|gene.b3204]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69829`
- `KEGG:ecj:JW3171;eco:b3204;ecoc:C3026_17435;`
- `GeneID:86862399;947721;`
- `GO:GO:0004857; GO:0005829; GO:0008982; GO:0009401; GO:0016301; GO:0030295`

## Notes

Nitrogen regulatory protein (Enzyme IIA-NTR) (PTS system EIIA component) (Phosphotransferase enzyme IIA component)
