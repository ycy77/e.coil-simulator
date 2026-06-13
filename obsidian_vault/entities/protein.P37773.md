---
entity_id: "protein.P37773"
entity_type: "protein"
name: "mpl"
source_database: "UniProt"
source_id: "P37773"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Secreted."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mpl yjfG b4233 JW4192"
---

# mpl

`protein.P37773`

## Static

- Type: `protein`
- Source: `UniProt:P37773`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Secreted.

## Enriched Summary

FUNCTION: Reutilizes the intact tripeptide L-alanyl-gamma-D-glutamyl-meso-diaminopimelate by linking it to UDP-N-acetylmuramate. The enzyme can also use the tetrapeptide L-alanyl-gamma-D-glutamyl-meso-2,6-diaminoheptanedioyl-D-alanine or the pentapeptide L-alanyl-gamma-D-glutamyl-meso-2,6-diaminoheptandioyl-D-alanyl-D-alanine in vivo and in vitro. {ECO:0000269|PubMed:17384195, ECO:0000269|PubMed:8808921}. UDP-N-acetylmuramate:L-alanyl-γ-D-glutamyl-meso-diaminopimelate ligase (Mpl) acts in murein recycling by enabling ligation of the tripeptide L-Ala-D-Glu-mesoA2pm with UDP-MurNAc and reincorporation into peptidoglycan. L-Ala-D-Glu-mesoA2pm is released while remodelling the cell wall during growth . The enzyme can utilize tri-, tetra-, and pentapeptide in vitro and in vivo, but utilizes either the dipeptide L-Ala-D-Glu or L-Ala alone at a much lower rate. The substrate specificity of Mpl has been investigated . An mpl null mutant shows no obvious growth defect, but has decreased levels of UDP-MurNAc-pentapeptide and increased levels of L-Ala-D-Glu-mesoA2pm . Overexpression of mpl can complement the conditional growth defect of a EG10619 murC mutant, thus showing that Mpl is able to utilize L-alanine as a substrate both in vitro and in vivo . Tpl: "tripeptide ligase"Mpl: "murein peptide ligase" Reviews:

## Biological Role

Catalyzes UDP-N-acetylmuramate:L-alanyl-gamma-D-glutamyl-meso-2,6-diaminoheptandioate ligase (reaction.R10901), RXN0-2361 (reaction.ecocyc.RXN0-2361), RXN0-7022 (reaction.ecocyc.RXN0-7022). Bound by Magnesium cation (molecule.C00305).

## Annotation

FUNCTION: Reutilizes the intact tripeptide L-alanyl-gamma-D-glutamyl-meso-diaminopimelate by linking it to UDP-N-acetylmuramate. The enzyme can also use the tetrapeptide L-alanyl-gamma-D-glutamyl-meso-2,6-diaminoheptanedioyl-D-alanine or the pentapeptide L-alanyl-gamma-D-glutamyl-meso-2,6-diaminoheptandioyl-D-alanyl-D-alanine in vivo and in vitro. {ECO:0000269|PubMed:17384195, ECO:0000269|PubMed:8808921}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R10901|reaction.R10901]] `KEGG` `database` - via EC:6.3.2.45
- `catalyzes` --> [[reaction.ecocyc.RXN0-2361|reaction.ecocyc.RXN0-2361]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7022|reaction.ecocyc.RXN0-7022]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b4233|gene.b4233]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37773`
- `KEGG:ecj:JW4192;eco:b4233;ecoc:C3026_22850;`
- `GeneID:948752;`
- `GO:GO:0005524; GO:0005576; GO:0005737; GO:0008360; GO:0009252; GO:0009254; GO:0042802; GO:0051301; GO:0071555; GO:0097216; GO:0106418`
- `EC:6.3.2.45`

## Notes

UDP-N-acetylmuramate--L-alanyl-gamma-D-glutamyl-meso-2,6-diaminoheptandioate ligase (EC 6.3.2.45) (Murein peptide ligase) (UDP-N-acetylmuramate:L-alanyl-gamma-D-glutamyl-meso-diaminopimelate ligase)
