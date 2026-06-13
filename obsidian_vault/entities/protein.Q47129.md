---
entity_id: "protein.Q47129"
entity_type: "protein"
name: "feaR"
source_database: "UniProt"
source_id: "Q47129"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "feaR maoB maoR ydbM b1384 JW1379"
---

# feaR

`protein.Q47129`

## Static

- Type: `protein`
- Source: `UniProt:Q47129`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Positive regulator of tynA/maoA and feaB/padA, the genes for 2-phenylethylamine catabolism. "Phenylethylamine regulator," FeaR, is considered an activator of phenylacetate synthesis from 2-phenylethylamine (PEA). This regulator is regulated by catabolic repression, and highly expressed in the presence of succinate . FeaR controls expression of a pathway for the degradation of potentially toxic aromatic compounds . It is induced by tyramine, and in the absence of glucose, it activates the expression of amine oxidase and phenylacetaldehyde dehydrogenase, proteins involved in 2-phenylethylamine catabolism . Although it has not been possible to test the ligand binding to FeaR, these data and those of others suggest that it is a substrate or intermediate of the TynA/FeaB pathway, as it is more likely that an aldehyde (tyramine) is the direct inducer for the PEA catabolic pathway and a likely coeffector of FeaR . FeaR belongs to the AraC/XylS family of transcriptional regulators . This protein consists of two domains, an amino-terminal domain (NTD) involved in co-inducer recognition and dimerization and a carboxy-terminal domain (CTD) that contains a potential helix-turn-helix DNA-binding motif . Activation by FeaR requires the NTD, which could function as an inhibitor of the CTD in the absence of the coactivator...

## Annotation

FUNCTION: Positive regulator of tynA/maoA and feaB/padA, the genes for 2-phenylethylamine catabolism.

## Outgoing Edges (2)

- `activates` --> [[gene.b1385|gene.b1385]] `RegulonDB` `C` - regulator=FeaR; target=feaB; function=+
- `activates` --> [[gene.b1386|gene.b1386]] `RegulonDB` `C` - regulator=FeaR; target=tynA; function=+

## Incoming Edges (1)

- `encodes` <-- [[gene.b1384|gene.b1384]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q47129`
- `KEGG:ecj:JW1379;eco:b1384;ecoc:C3026_08085;`
- `GeneID:945941;`
- `GO:GO:0000987; GO:0003700; GO:0006355; GO:0045893`

## Notes

Transcriptional activator FeaR
