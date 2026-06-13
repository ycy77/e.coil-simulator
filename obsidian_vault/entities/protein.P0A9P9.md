---
entity_id: "protein.P0A9P9"
entity_type: "protein"
name: "idnO"
source_database: "UniProt"
source_id: "P0A9P9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "idnO yjgU b4266 JW4223"
---

# idnO

`protein.P0A9P9`

## Static

- Type: `protein`
- Source: `UniProt:P0A9P9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reduction of 5-keto-D-gluconate to D-gluconate, using either NADH or NADPH. Is likely involved in an L-idonate degradation pathway that allows E.coli to utilize L-idonate as the sole carbon and energy source. Is also able to catalyze the reverse reaction in vitro, but the D-gluconate oxidation by the enzyme can only proceed with NAD. {ECO:0000269|PubMed:9658018}.

## Biological Role

Catalyzes D-gluconate:NAD+ 5-oxidoreductase (reaction.R01738), D-gluconate:NADP+ 5-oxidoreductase (reaction.R01740). Component of 5-keto-D-gluconate 5-reductase (complex.ecocyc.CPLX0-8292).

## Annotation

FUNCTION: Catalyzes the reduction of 5-keto-D-gluconate to D-gluconate, using either NADH or NADPH. Is likely involved in an L-idonate degradation pathway that allows E.coli to utilize L-idonate as the sole carbon and energy source. Is also able to catalyze the reverse reaction in vitro, but the D-gluconate oxidation by the enzyme can only proceed with NAD. {ECO:0000269|PubMed:9658018}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R01738|reaction.R01738]] `KEGG` `database` - via EC:1.1.1.69
- `catalyzes` --> [[reaction.R01740|reaction.R01740]] `KEGG` `database` - via EC:1.1.1.69
- `is_component_of` --> [[complex.ecocyc.CPLX0-8292|complex.ecocyc.CPLX0-8292]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4266|gene.b4266]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9P9`
- `KEGG:ecj:JW4223;eco:b4266;ecoc:C3026_23010;`
- `GeneID:947109;`
- `GO:GO:0008874; GO:0016491; GO:0042803; GO:0046183`
- `EC:1.1.1.69`

## Notes

5-keto-D-gluconate 5-reductase (EC 1.1.1.69)
