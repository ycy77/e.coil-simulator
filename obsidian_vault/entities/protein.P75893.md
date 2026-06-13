---
entity_id: "protein.P75893"
entity_type: "protein"
name: "rutF"
source_database: "UniProt"
source_id: "P75893"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rutF ycdH b1007 JW5138"
---

# rutF

`protein.P75893`

## Static

- Type: `protein`
- Source: `UniProt:P75893`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reduction of FMN to FMNH2 which is used to reduce pyrimidine by RutA via the Rut pathway. In vitro, the flavin reductase Fre can substitute for the function of RutF, however, RutF is required for uracil utilization in vivo. {ECO:0000269|PubMed:16540542, ECO:0000269|PubMed:20400551}. E. coli K-12 contains a previously undescribed pathway for pyrimidine degradation. RutF functions as a flavin reductase whose activity is required for the first catalytic step, the flavin hydroperoxide-catalyzed ring opening by the RutA pyrimidine oxygenase . In vitro, the flavin reductase Fre can substitute for the function of RutF; however, RutF is required for uracil utilization in vivo . Expression of the rutABCDEFG operon is under the control of nitrogen regulatory protein C (NtrC) . A rutF insertion mutant loses the ability to utilize pyrimidine nucleosides and bases as the sole source of nitrogen at room temperature . RutF: "pyrimidine utilization F" Reviews:

## Biological Role

Catalyzes RXN-9510 (reaction.ecocyc.RXN-9510).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the reduction of FMN to FMNH2 which is used to reduce pyrimidine by RutA via the Rut pathway. In vitro, the flavin reductase Fre can substitute for the function of RutF, however, RutF is required for uracil utilization in vivo. {ECO:0000269|PubMed:16540542, ECO:0000269|PubMed:20400551}.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-9510|reaction.ecocyc.RXN-9510]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1007|gene.b1007]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75893`
- `KEGG:ecj:JW5138;eco:b1007;ecoc:C3026_06130;`
- `GeneID:946594;`
- `GO:GO:0006208; GO:0006212; GO:0010181; GO:0019740; GO:0042602; GO:0052874`
- `EC:1.5.1.42`

## Notes

FMN reductase (NADH) RutF (EC 1.5.1.42) (FMN reductase) (NADH-flavin reductase RutF) (NADH:flavin oxidoreductase)
