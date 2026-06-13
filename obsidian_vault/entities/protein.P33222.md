---
entity_id: "protein.P33222"
entity_type: "protein"
name: "yjfC"
source_database: "UniProt"
source_id: "P33222"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yjfC b4186 JW4144"
---

# yjfC

`protein.P33222`

## Static

- Type: `protein`
- Source: `UniProt:P33222`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: May be a ligase forming an amide bond. Shows ATPase activity. Despite its similarity to the C-terminal synthetase domain of Gss, is not a glutathionylspermidine (Gsp) synthetase. Cannot synthesize Gsp, glutathione (GSH), or GSH intermediates, from GSH and spermidine, cysteine and glutamate, gamma-glutamylcysteine and spermidine, and gamma-glutamylcysteine and glycine. Does not bind to Gsp. {ECO:0000269|PubMed:23097746}. Based on sequence similarity to the glutathionylspermidine synthetase domain of GSP-CPLX "Gss", EG11165 and EG11812 were predicted to encode additional glutathionylspermidine synthetases. However, while purified YgiC hydrolyzes ATP, it does not synthesize glutathionylspermidine, glutathione, or glutathione intermediates . In addition, a triple mutant lacking EG12882, EG11165 and EG11812 has no growth defect in minimal medium , and deletion of EG11812 has no effect on GLUTATHIONYLSPERMIDINE levels in the cell . A 2023 study that reported high-resolution crystal structures for YgiC and YjfC has shown that while both proteins possess multiple substitutions in key residues required for binding glutathione, they should be able to catalyze the formation of an alternate peptide—spermidine conjugate. The physiological substrates of either enzyme are still unknown, but both enzymes were able to ligate SPERMIDINE to a CPD-26564 peptide...

## Biological Role

Catalyzes RXN-24020 (reaction.ecocyc.RXN-24020).

## Annotation

FUNCTION: May be a ligase forming an amide bond. Shows ATPase activity. Despite its similarity to the C-terminal synthetase domain of Gss, is not a glutathionylspermidine (Gsp) synthetase. Cannot synthesize Gsp, glutathione (GSH), or GSH intermediates, from GSH and spermidine, cysteine and glutamate, gamma-glutamylcysteine and spermidine, and gamma-glutamylcysteine and glycine. Does not bind to Gsp. {ECO:0000269|PubMed:23097746}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-24020|reaction.ecocyc.RXN-24020]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4186|gene.b4186]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33222`
- `KEGG:ecj:JW4144;eco:b4186;ecoc:C3026_22615;`
- `GeneID:948699;`
- `GO:GO:0005524; GO:0016874; GO:0046872`
- `EC:6.3.1.-`

## Notes

Putative acid--amine ligase YjfC (EC 6.3.1.-)
