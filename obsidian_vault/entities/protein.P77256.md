---
entity_id: "protein.P77256"
entity_type: "protein"
name: "ydjG"
source_database: "UniProt"
source_id: "P77256"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ydjG b1771 JW1760"
---

# ydjG

`protein.P77256`

## Static

- Type: `protein`
- Source: `UniProt:P77256`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the NADH-dependent reduction of methylglyoxal (2-oxopropanal) in vitro (PubMed:16813561). It is not known if this activity has physiological significance (PubMed:16813561). Cannot use NADPH as a cosubstrate (PubMed:16813561). Seems to play some role in intestinal colonization (PubMed:20562286). {ECO:0000269|PubMed:16813561, ECO:0000269|PubMed:20562286}. The YdjG protein belongs to subfamily 11 of the aldo-keto reductase superfamily. Members of this family generally use NADPH as the cosubstrate, although some are able to use both NADH and NADPH. YdjG is the first member of this family that is only able to use NADH. The crystal structure of the dual-specificity xylose reductase from Candida tenuis identified a conserved glutamic acid residue which appears to allow binding of both NAD+ and NADP+. Mutagenesis of the analogous residue in YdjG, D232A or D232E, converts YdjG into a dual-specificity enzyme . The purified enzyme was found to possess a relatively high activity with methylglyoxal as the substrate (Kcat = 15.7 s-1) . The physiological significance of this activity has not been investigated. YdjG is important for survival under competitive planktonic growth conditions . YdjG protein levels appear to be higher in gnotobiotic mice colonized with E...

## Biological Role

Catalyzes RXN0-5213 (reaction.ecocyc.RXN0-5213).

## Enriched Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the NADH-dependent reduction of methylglyoxal (2-oxopropanal) in vitro (PubMed:16813561). It is not known if this activity has physiological significance (PubMed:16813561). Cannot use NADPH as a cosubstrate (PubMed:16813561). Seems to play some role in intestinal colonization (PubMed:20562286). {ECO:0000269|PubMed:16813561, ECO:0000269|PubMed:20562286}.

## Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5213|reaction.ecocyc.RXN0-5213]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1771|gene.b1771]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77256`
- `KEGG:ecj:JW1760;eco:b1771;ecoc:C3026_10110;`
- `GeneID:75203077;946283;`
- `GO:GO:0005829; GO:0019170`
- `EC:1.1.1.-`

## Notes

NADH-specific methylglyoxal reductase (EC 1.1.1.-) (AKR11B2)
