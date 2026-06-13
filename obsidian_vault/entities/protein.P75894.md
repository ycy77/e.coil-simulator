---
entity_id: "protein.P75894"
entity_type: "protein"
name: "rutE"
source_database: "UniProt"
source_id: "P75894"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rutE ycdI b1008 JW0993"
---

# rutE

`protein.P75894`

## Static

- Type: `protein`
- Source: `UniProt:P75894`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: May reduce toxic product malonic semialdehyde to 3-hydroxypropionic acid, which is excreted. RutE is apparently supplemented by YdfG. Required in vivo, but not in vitro in pyrimidine nitrogen degradation. {ECO:0000269|PubMed:16540542}. E. coli K-12 contains a previously undescribed pathway for pyrimidine degradation. RutE is not required for the release of ammonium from uracil in vitro; it may function as a malonic semialdehyde reductase . Expression of the rutABCDEFG operon is under the control of nitrogen regulatory protein C (NtrC) . A rutE insertion mutant loses the ability to utilize pyrimidine nucleosides and bases as the sole source of nitrogen at room temperature . RutE: "pyrimidine utilization E" Reviews:

## Biological Role

Catalyzes RXN-8974 (reaction.ecocyc.RXN-8974).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: May reduce toxic product malonic semialdehyde to 3-hydroxypropionic acid, which is excreted. RutE is apparently supplemented by YdfG. Required in vivo, but not in vitro in pyrimidine nitrogen degradation. {ECO:0000269|PubMed:16540542}.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-8974|reaction.ecocyc.RXN-8974]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1008|gene.b1008]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75894`
- `KEGG:ecj:JW0993;eco:b1008;ecoc:C3026_06135;`
- `GeneID:946591;`
- `GO:GO:0006208; GO:0006212; GO:0006974; GO:0010181; GO:0016491; GO:0019740; GO:0035527`
- `EC:1.1.1.298`

## Notes

Probable malonic semialdehyde reductase RutE (EC 1.1.1.298)
