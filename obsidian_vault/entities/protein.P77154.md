---
entity_id: "protein.P77154"
entity_type: "protein"
name: "ycjT"
source_database: "UniProt"
source_id: "P77154"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ycjT b1316 JW1309"
---

# ycjT

`protein.P77154`

## Static

- Type: `protein`
- Source: `UniProt:P77154`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: In vitro catalyzes the phosphorolysis of D-kojibiose into beta-D-glucose 1-phosphate and D-glucose. No other disaccharides tested substitute for D-kojibiose. In the reverse direction disaccharides can be formed from beta-D-glucose 1-phosphate plus D-glucose, L-sorbose, D-sorbitol, L-iditol or 1,5-anhydro-D-glucitol, but with low efficiency. The beta-D-glucose 1-phosphate product is the substrate for YcjU (AC P77366), the next apparent enzyme in the putative biochemical pathway encoded in this locus (yjcM to ycjW). {ECO:0000269|PubMed:29684280}. YcjT was shown to have kojibiose phosphorylase activity in vitro. However, neither the E. coli K-12 strain BW25113 nor the B strain BL21(DE3) is able to grow on D-kojibiose as the sole source of carbon and energy . YcjT shows sequence similarity to maltose phosphorylase from Lactobacillus sanfranciscensis. A ycjT null mutant does not affect growth on maltose .

## Biological Role

Catalyzes 2-alpha-D-glucosyl-D-glucose:phosphate beta-D-glucosyltransferase (reaction.R07264), 2.4.1.230-RXN (reaction.ecocyc.2.4.1.230-RXN).

## Annotation

FUNCTION: In vitro catalyzes the phosphorolysis of D-kojibiose into beta-D-glucose 1-phosphate and D-glucose. No other disaccharides tested substitute for D-kojibiose. In the reverse direction disaccharides can be formed from beta-D-glucose 1-phosphate plus D-glucose, L-sorbose, D-sorbitol, L-iditol or 1,5-anhydro-D-glucitol, but with low efficiency. The beta-D-glucose 1-phosphate product is the substrate for YcjU (AC P77366), the next apparent enzyme in the putative biochemical pathway encoded in this locus (yjcM to ycjW). {ECO:0000269|PubMed:29684280}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R07264|reaction.R07264]] `KEGG` `database` - via EC:2.4.1.230
- `catalyzes` --> [[reaction.ecocyc.2.4.1.230-RXN|reaction.ecocyc.2.4.1.230-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1316|gene.b1316]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77154`
- `KEGG:ecj:JW1309;eco:b1316;ecoc:C3026_07710;`
- `GeneID:945895;`
- `GO:GO:0004553; GO:0005975; GO:0030246; GO:0033831`
- `EC:2.4.1.230`

## Notes

Kojibiose phosphorylase (EC 2.4.1.230)
