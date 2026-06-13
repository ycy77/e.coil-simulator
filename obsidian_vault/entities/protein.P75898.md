---
entity_id: "protein.P75898"
entity_type: "protein"
name: "rutA"
source_database: "UniProt"
source_id: "P75898"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rutA ycdM b1012 JW0997"
---

# rutA

`protein.P75898`

## Static

- Type: `protein`
- Source: `UniProt:P75898`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the pyrimidine ring opening between N-3 and C-4 by an unusual flavin hydroperoxide-catalyzed mechanism, adding oxygen atoms in the process to yield ureidoacrylate peracid, that immediately reacts with FMN forming ureidoacrylate and FMN-N(5)-oxide. The FMN-N(5)-oxide reacts spontaneously with NADH to produce FMN. Requires the flavin reductase RutF to regenerate FMN in vivo. RutF can be substituted by Fre in vitro. {ECO:0000269|PubMed:16540542, ECO:0000269|PubMed:20400551, ECO:0000269|PubMed:28661684}. E. coli K-12 contains a previously undescribed pathway for pyrimidine degradation. In the presence of the flavin reductases Fre or RutF, RutA catalyzes the first step in this pathway, the ring opening of uracil at the C4 carbonyl . The reaction was initially thought to produce ureidoacrylate peracid, which would convert to ureidoacrylate either enzymatically or spontaneously . It was later shown that the reaction involves formation of a CPD-22328 intermediate . More recently, used mechanistic and computational studies together with X-ray crystallography to show that flavin-N5-peroxide is the oxygen-transferring species. Expression of the rutABCDEFG operon is under the control of nitrogen regulatory protein C (NtrC) . A rutA insertion mutant loses the ability to utilize pyrimidine nucleosides and bases as the sole source of nitrogen at room temperature...

## Biological Role

Catalyzes RXN-12886 (reaction.ecocyc.RXN-12886), RXN0-6444 (reaction.ecocyc.RXN0-6444). Bound by FMN (molecule.C00061).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the pyrimidine ring opening between N-3 and C-4 by an unusual flavin hydroperoxide-catalyzed mechanism, adding oxygen atoms in the process to yield ureidoacrylate peracid, that immediately reacts with FMN forming ureidoacrylate and FMN-N(5)-oxide. The FMN-N(5)-oxide reacts spontaneously with NADH to produce FMN. Requires the flavin reductase RutF to regenerate FMN in vivo. RutF can be substituted by Fre in vitro. {ECO:0000269|PubMed:16540542, ECO:0000269|PubMed:20400551, ECO:0000269|PubMed:28661684}.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-12886|reaction.ecocyc.RXN-12886]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6444|reaction.ecocyc.RXN0-6444]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1012|gene.b1012]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75898`
- `KEGG:ecj:JW0997;eco:b1012;`
- `GeneID:945643;`
- `GO:GO:0004497; GO:0006208; GO:0006210; GO:0006212; GO:0008726; GO:0019740; GO:0046306; GO:0052614`
- `EC:1.14.99.46`

## Notes

Pyrimidine monooxygenase RutA (EC 1.14.99.46)
