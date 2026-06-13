---
entity_id: "protein.P77333"
entity_type: "protein"
name: "pgrR"
source_database: "UniProt"
source_id: "P77333"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pgrR ycjZ b1328 JW1321"
---

# pgrR

`protein.P77333`

## Static

- Type: `protein`
- Source: `UniProt:P77333`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Regulates the expression of genes involved in peptidoglycan (PG) degradation. Could play a role in switch control between recycling and degradation of PG peptides. Negatively regulates the expression of the ycjY-ymjD-ymjC-mpaA operon by binding to the PgrR-box. In addition, other genes are predicted to be under the control of PgrR, including genes related to membrane formation and function. {ECO:0000269|PubMed:23301696}. Based on analysis with the Genomic SELEX screening system, PgrR was identified as a repressor of the expression of genes of the initial enzymes for peptidoglycan (PG) peptide degradation as well as genes of the switch control between recycling and degradation of PG peptides, which are induced upon exposure to heat shock or membrane distortion . PgrR negatively controls ycjY-ymjD-ymjC-mpaA operon expression and binds to the palindromic sequence ATCATTT-AAATGAT . Both the pgrR and ycjY promoters are recognized by RpoH (σ32) and RpoE (σ24), both of which are involved in the heat shock response, and by FecI (σ19), which is involved in the response to extracytoplasmic stimuli . Eleven possible targets were predicted to be under PgrR control. These targets were identified by Genomic SELEX analysis and include genes related to membrane formation and function: leuL, leuO, pheP, ycjY, pgrR, yedS, xapR, yfgF, yfgG, rfaL, and rfaS...

## Annotation

FUNCTION: Regulates the expression of genes involved in peptidoglycan (PG) degradation. Could play a role in switch control between recycling and degradation of PG peptides. Negatively regulates the expression of the ycjY-ymjD-ymjC-mpaA operon by binding to the PgrR-box. In addition, other genes are predicted to be under the control of PgrR, including genes related to membrane formation and function. {ECO:0000269|PubMed:23301696}.

## Outgoing Edges (9)

- `represses` --> [[gene.b1321|gene.b1321]] `RegulonDB` `S` - regulator=PgrR; target=ycjX; function=-
- `represses` --> [[gene.b1322|gene.b1322]] `RegulonDB` `S` - regulator=PgrR; target=ycjF; function=-
- `represses` --> [[gene.b1323|gene.b1323]] `RegulonDB` `S` - regulator=PgrR; target=tyrR; function=-
- `represses` --> [[gene.b1325|gene.b1325]] `RegulonDB` `S` - regulator=PgrR; target=ycjG; function=-
- `represses` --> [[gene.b1326|gene.b1326]] `RegulonDB` `S` - regulator=PgrR; target=mpaA; function=-
- `represses` --> [[gene.b1327|gene.b1327]] `RegulonDB` `S` - regulator=PgrR; target=ycjY; function=-
- `represses` --> [[gene.b1329|gene.b1329]] `RegulonDB` `S` - regulator=PgrR; target=mppA; function=-
- `represses` --> [[gene.b4525|gene.b4525]] `RegulonDB` `S` - regulator=PgrR; target=ymjC; function=-
- `represses` --> [[gene.b4673|gene.b4673]] `RegulonDB` `S` - regulator=PgrR; target=ymjD; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1328|gene.b1328]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77333`
- `KEGG:ecj:JW1321;eco:b1328;ecoc:C3026_07775;`
- `GeneID:945930;`
- `GO:GO:0003677; GO:0003700; GO:0006351; GO:0043565; GO:0045892; GO:0071978`

## Notes

HTH-type transcriptional regulator PgrR (Regulator of PG recycling)
